#!/usr/bin/env python3
"""Sucht Duplikate, Zahlenkollisionen und Ausreißer in bank/*/*.jsonl.

Aufruf (aus beliebigem Verzeichnis):
    python3 werkzeuge/duplikate.py

Schreibt duplikate.md in der Wurzel. Deterministisch: dieselbe Bank
ergibt dieselbe Datei (kein Datum, Stand = letzter Commit auf bank/).
Liest die Bank nur, ändert sie nie. Nur Standardbibliothek.

Verglichen wird je Zeile der Aufgabentext samt Grafik (aufgabe und
grafik); ohne die Grafik wären „Wie viel Prozent sind grau?“ mit
verschiedenen Streifen Duplikate.

A. Wortgleich: aufgabe + grafik nach Normierung gleich. Normierung:
   LaTeX-Abstände (\\, \\; \\: \\! \\quad ~) und $ weg, {,} → Komma,
   Tausender zusammen (1 000 → 1000), Dezimalpunkt → Komma,
   Nullen am Ende der Nachkommastellen weg (2,40 → 2,4),
   Leerzeichen zusammengefasst und neben Satz- und Rechenzeichen
   gestrichen.
B. Bis auf Zahlen gleich: nach Normierung jede Zahl durch # ersetzt
   gleich, aber nicht schon wortgleich (mindestens zwei verschiedene
   normierte Texte in der Gruppe). Getrennt nach Reichweite: über
   Einträge hinweg, im selben Eintrag über Sprossen hinweg, in
   derselben Sprosse (Varianten; nach bank.md erlaubt, wenn sich
   auch der Kontext unterscheidet – daher nur kurz gelistet).
C. Gleiches Ergebnis, gleiche Kontextwörter: pruef ausgewertet (wie
   bank-pruef.py: eval mit math), Kontextwörter = Personennamen
   (VORNAMEN, dazu „Frau/Herr X“) und Gegenstände (Treffer der
   Wortliste KONTEXTE); mehr als drei Zeilen mit demselben Paar.
   Zeilen ohne pruef oder ohne Kontextwort zählen nicht.
D. Personennamen (die zehn häufigsten) und Sachkontexte mit
   Häufigkeit (Zeilen je Kontext; eine Zeile kann mehrere haben).
E. aufgabe kürzer als 20 oder länger als 600 Zeichen (Rohtext).
"""

import json
import math
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
BANK = WURZEL / "bank"
ZIEL_DATEI = WURZEL / "duplikate.md"

KURZ, LANG = 20, 600
MINDEST_C = 4          # „mehr als drei Zeilen“

# Vornamen, aus der Bank erhoben (Wortanfang groß, ganzes Wort).
VORNAMEN = set("""
Ali Anna Aylin Ben Can Clara Ela Ella Emil Emma Eva Finn Hanna Ida Ina
Jan Jana Jonas Kai Kaya Kim Lara Lars Lea Lena Leo Leon Lina Lisa Luca
Lukas Malte Mara Max Mehmet Mia Mila Mira Nele Nico Nils Nina Noah Nora
Ole Omar Paul Paula Pia Rosa Sam Sara Sina Sven Tim Timo Tina Tom Uwe
""".split())
ANREDE = re.compile(r"\b(Frau|Herr|Herrn)\s+([A-ZÄÖÜ][a-zäöüß]+)")

# Sachkontexte: Name → Muster (klein geschrieben, auf den Rohtext in
# Kleinbuchstaben). Der Treffer selbst ist das Kontextwort.
KONTEXTE = [
    ("Geld und Einkauf", r"€|\beuro\b|\bpreis\w*|\bkost\w*|\brabatt\w*|"
     r"\bkauf\w*|\bgekauft|\bverkauf\w*|\bladen\b|\bkasse\b|\bangebot\w*"),
    ("Zinsen und Konto", r"\bzins\w*|\bkonto\b|\bguthaben\w*|\bkredit\w*|"
     r"\bspar\w*|\bbank\b|\banlage\b"),
    ("Tarife und Gebühren", r"\bgrundgebühr\w*|\btarif\w*|\bgebühr\w*|"
     r"\bgrundpreis\w*|\bvertrag\w*|\bmiete\w*"),
    ("Schule", r"\bschul\w*|\bschüler\w*|\bklasse\b|\bklassen\b|"
     r"\blehrer\w*|\bnote\b|\bnoten\b|\bklassenarbeit\w*"),
    ("Sport und Spiel", r"\bsport\w*|\bfußball\w*|\bbasketball\w*|"
     r"\btor\b|\btore\b|\btraining\w*|\bspieler\w*|\bmannschaft\w*|"
     r"\bschwimm\w*|\bläuf\w*|\blauf\b|\bsprung\w*|\bverein\w*|\bwette\w*"),
    ("Verkehr und Fahrt", r"\bauto\w*|\bzug\b|\bzüge\b|\bbus\b|\bbusse\b|"
     r"\bfahrrad\w*|km/h|\bfährt\b|\bfahr\w*|\bbenzin\b|\bflugzeug\w*|"
     r"\bbahn\b|\bstau\b"),
    ("Glücksspiel und Zufallsgeräte", r"\bmünze\w*|\bglücksrad\w*|\burne\b|"
     r"\blose\b|\blosen\b|\blos\b|\bkugeln\b|\bspielkarte\w*|\bwürfelt\w*|"
     r"\baugenzahl\w*|\bgewinnspiel\w*|\bniete\w*|\blotto\b|\bwürfeln\b"),
    ("Essen und Kochen", r"\brezept\w*|\bmehl\b|\bbrötchen\b|\bpizza\w*|"
     r"\bäpfel\b|\bapfel\b|\beier\b|\bkuchen\w*|\beis\b|\bsaft\w*|"
     r"\bbäcker\w*|\bzucker\b|\bmilch\b|\bschokolade\w*|\bbirne\w*|"
     r"\bobst\b|\bkaffee\b|\bsuppe\b|\bnudeln\b"),
    ("Garten, Bau und Wohnen", r"\bbeet\w*|\bzaun\w*|\bgarten\w*|\brasen\w*|"
     r"\bmauer\w*|\bwand\b|\bwände\b|\bdach\w*|\brampe\w*|\bleiter\b|"
     r"\bfliese\w*|\bbrett\w*|\bteppich\w*|\bzimmer\w*|\bhaus\b|"
     r"\bhäuser\b|\btisch\w*|\bzelt\w*|\bsonnensegel\w*|\bbeton\b|"
     r"\bfenster\w*|\btreppe\w*|\bbrücke\w*|\bturm\w*|\bseil\w*"),
    ("Wasser und Behälter", r"\bwasser\w*|\bbecken\w*|\btank\w*|\bpool\w*|"
     r"\bliter\w*|\bglas\b|\bzufluss\w*|\bzuflussrate\w*|\bdose\w*|"
     r"\bbehälter\w*|\bflasche\w*|\bkanne\w*|\beimer\w*|\bvase\w*"),
    ("Temperatur und Wetter", r"\btemperatur\w*|°c|\bregen\w*|\bwetter\w*|"
     r"\bschnee\w*|\bsonne\b"),
    ("Wachstum und Bestand", r"\bbakterie\w*|\bbestand\w*|\bpopulation\w*|"
     r"\bwachstum\w*|\bzerfall\w*|\bhalbwertszeit\w*|\bmedikament\w*|"
     r"\bwirkstoff\w*|\binfiz\w*|\beinwohner\w*"),
    ("Umfrage und Medizin", r"\bbefragt\w*|\bumfrage\w*|\bhaushalt\w*|"
     r"\bkrank\w*|\berkrank\w*|\bpositiv\w*|\bimpf\w*|\bpatient\w*|"
     r"\bstudie\w*|\bwähler\w*"),
    ("Produktion und Qualität", r"\bausschuss\w*|\bdefekt\w*|\bfehlerhaft\w*|"
     r"\bproduktion\w*|\bproduz\w*|\bfabrik\w*|\bmaschine\w*|\bpaket\w*|"
     r"\blieferung\w*|\bfirma\b|\bbetrieb\w*|\bhersteller\w*"),
    ("Natur und Tiere", r"\bhund\w*|\bkatze\w*|\btier\w*|\bbaum\b|\bbäume\b|"
     r"\bpflanze\w*|\bvogel\w*|\bvögel\w*|\bfisch\w*|\bsamen\b|\bblume\w*|"
     r"\bwald\b|\bpferd\w*"),
    ("Freizeit und Veranstaltung", r"\bkino\w*|\bkonzert\w*|\bbesucher\w*|"
     r"\bgäste\b|\bgast\b|\beintritt\w*|\bparty\w*|\bfest\b|\bmuseum\w*|"
     r"\bzoo\b|\bausflug\w*|\breise\w*|\burlaub\w*|\bfreizeitpark\w*"),
    ("Handy und Technik", r"\bhandy\w*|\bapp\b|\bapps\b|\bsmartphone\w*|"
     r"\bcomputer\w*|\bdatei\w*|\bdownload\w*|\bakku\w*|\bdrucker\w*|"
     r"\bcode\b|\bcodes\b|\bpasswort\w*|\bpin\b"),
    ("Karte und Gelände", r"\bmaßstab\w*|\bstadtplan\w*|\blandkarte\w*|"
     r"\bstadt\b|\bberg\w*|\bschatten\w*|\bfluss\b|\bstraße\w*|\bweg\b"),
]
KONTEXT_MUSTER = [(n, re.compile(m)) for n, m in KONTEXTE]
OHNE_KONTEXT = "ohne Sachkontext (innermathematisch)"

ABSTAND = re.compile(r"\\[,;:!> ]|\\q?quad\b|~")
ZAHL = re.compile(r"\d+(?:,\d+)?")


def normiert(text):
    t = ABSTAND.sub(" ", text)
    t = t.replace("{,}", ",").replace("$", "")
    t = re.sub(r"(\d) +(?=\d{3}\b)", r"\1", t)          # 1 000 → 1000
    t = re.sub(r"(\d)\.(?=\d)", r"\1,", t)                # 2.5 → 2,5
    t = re.sub(r"(\d,\d*?)0+\b", r"\1", t)                # 2,40 → 2,4
    t = re.sub(r"(\d),(?!\d)", r"\1", t)                  # 2, → 2
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r" ?([^\wÄÖÜäöüß ]) ?", r"\1", t)


def skelett(t):
    return ZAHL.sub("#", t)


def vergleichstext(z):
    g = z.get("grafik") or ""
    return normiert(z["aufgabe"] + (" ‖ Grafik: " + g if g else ""))


def wert(pruef):
    """pruef ausgewertet und gerundet, sonst der Text ohne Leerzeichen."""
    if not isinstance(pruef, str) or not pruef.strip():
        return None
    try:
        w = eval(pruef, {"__builtins__": {}}, {"math": math})
    except Exception:
        return re.sub(r"\s+", "", pruef)

    def rund(x):
        if isinstance(x, (list, tuple)):
            return "[" + ", ".join(rund(y) for y in x) + "]"
        if isinstance(x, bool):
            return str(x)
        if isinstance(x, (int, float)):
            if isinstance(x, float) and not math.isfinite(x):
                return str(x)
            r = float(f"{x:.10g}")
            return str(int(r)) if r == int(r) else repr(r)
        return str(x)
    return rund(w)


def namen(text):
    gefunden = set()
    for w in re.findall(r"\b[A-ZÄÖÜ][a-zäöüß]+\b", text):
        if w in VORNAMEN:
            gefunden.add(w)
    for m in ANREDE.finditer(text):
        gefunden.add(("Herr" if m.group(1) == "Herrn" else m.group(1))
                     + " " + m.group(2))
    return gefunden


def sachwoerter(text):
    """(Kontexte, Kontextwörter) der Zeile."""
    klein = text.lower()
    kontexte, woerter = set(), set()
    for name, muster in KONTEXT_MUSTER:
        treffer = {m.group(0) for m in muster.finditer(klein)}
        if treffer:
            kontexte.add(name)
            woerter |= treffer
    return kontexte, woerter


def lies_bank():
    zeilen = []
    for pfad in sorted(BANK.glob("*/*.jsonl")):
        with pfad.open(encoding="utf-8") as f:
            for roh in f:
                if roh.strip():
                    z = json.loads(roh)
                    z["_nr"] = len(zeilen)
                    zeilen.append(z)
    return zeilen


def sprosse(z):
    return (z["eintrag"], z["einheit"], z["kette_nr"], z["sprosse"])


def reichweite(gruppe):
    if len({z["eintrag"] for z in gruppe}) > 1:
        return "über Einträge"
    if len({sprosse(z) for z in gruppe}) > 1:
        return "im Eintrag"
    return "in der Sprosse"


REICHWEITEN = ["über Einträge", "im Eintrag", "in der Sprosse"]


def gruppen_nach(zeilen, schluessel):
    g = defaultdict(list)
    for z in zeilen:
        k = schluessel(z)
        if k is not None:
            g[k].append(z)
    return g


def ordne(gruppen, schluessel=None):
    """Nach Reichweite, dann (bei B) nach Länge des gemeinsamen Texts,
    dann nach Größe und erster Zeile."""
    def lang(g):
        return -len(schluessel(g[0])) if schluessel else 0
    return sorted(gruppen, key=lambda g: (REICHWEITEN.index(reichweite(g)),
                                          lang(g), -len(g), g[0]["_nr"]))


def code(text, hoechstens=None):
    t = text.replace("\n", " ")
    if hoechstens and len(t) > hoechstens:
        t = t[:hoechstens].rstrip() + " …"
    zaun = "``" if "`" in t else "`"
    rand = " " if zaun == "``" else ""
    return f"{zaun}{rand}{t}{rand}{zaun}"


def ids(gruppe):
    return ", ".join(z["id"] for z in gruppe)


def bank_stand():
    try:
        aus = subprocess.run(
            ["git", "-C", str(WURZEL), "log", "-1", "--format=%h %cs",
             "--", "bank"], capture_output=True, text=True, check=True)
        return aus.stdout.strip() or "unbekannt"
    except (OSError, subprocess.CalledProcessError):
        return "unbekannt"


def main():
    zeilen = lies_bank()
    eintraege = sorted({z["eintrag"] for z in zeilen})
    for z in zeilen:
        z["_text"] = vergleichstext(z)
        z["_namen"] = namen(z["aufgabe"])
        z["_kontexte"], z["_dinge"] = sachwoerter(z["aufgabe"])

    # A: wortgleich
    a = ordne([g for g in gruppen_nach(zeilen, lambda z: z["_text"]).values()
               if len(g) > 1])
    # B: bis auf Zahlen gleich, nicht schon wortgleich
    b = ordne([g for g in gruppen_nach(
        zeilen, lambda z: skelett(z["_text"])).values()
        if len(g) > 1 and len({z["_text"] for z in g}) > 1],
        lambda z: skelett(z["_text"]))
    b_je = {r: [g for g in b if reichweite(g) == r] for r in REICHWEITEN}

    # C: gleiches Ergebnis, gleiche Kontextwörter
    def c_schluessel(z):
        w = wert(z.get("pruef"))
        kontext = z["_namen"] | z["_dinge"]
        if w is None or not kontext:
            return None
        return (w, tuple(sorted(kontext)))
    c_gruppen = gruppen_nach(zeilen, c_schluessel)
    c = sorted(((k, g) for k, g in c_gruppen.items() if len(g) >= MINDEST_C),
               key=lambda kg: (-len(kg[0][1]), -len(kg[1]), kg[1][0]["_nr"]))
    c_stark = [kg for kg in c if len(kg[0][1]) >= 2]

    # D: Namen und Sachkontexte
    namen_zahl = Counter(n for z in zeilen for n in z["_namen"])
    namen_zeilen = sum(1 for z in zeilen if z["_namen"])
    kontext_zahl = Counter(k for z in zeilen for k in z["_kontexte"])
    ohne = sum(1 for z in zeilen if not z["_kontexte"])

    # E: Länge
    kurz = [z for z in zeilen if len(z["aufgabe"]) < KURZ]
    lang = [z for z in zeilen if len(z["aufgabe"]) > LANG]

    o = []
    o.append("# Duplikate und Zahlenkollisionen der Bank")
    o.append("")
    o.append("Gebaut mit werkzeuge/duplikate.py; nicht von Hand ändern, "
             "nach jedem Bank-Auftrag neu bauen.")
    o.append(f"Quelle: bank/*/*.jsonl, {len(eintraege)} Einträge, "
             f"{len(zeilen)} Zeilen. Stand der Bank: {bank_stand()} "
             "(letzter Commit auf bank/).")
    o.append("Verglichen wird aufgabe samt grafik nach Normierung "
             "(LaTeX-Abstände und $ weg, {,} → Komma, Tausender zusammen, "
             "Dezimalpunkt → Komma, Endnullen weg, Leerzeichen neben "
             "Zeichen gestrichen); „bis auf Zahlen“ ersetzt jede Zahl "
             "durch #. Reichweite: über Einträge / im Eintrag (über "
             "Sprossen) / in der Sprosse (Varianten).")
    o.append("")
    o.append("## Zahl je Befundart")
    o.append("")
    o.append("| Befundart | Gruppen | Zeilen |")
    o.append("|---|--:|--:|")

    def zeilenzahl(gs):
        return sum(len(g) for g in gs)
    for r in REICHWEITEN:
        gs = [g for g in a if reichweite(g) == r]
        o.append(f"| A wortgleich, {r} | {len(gs)} | {zeilenzahl(gs)} |")
    for r in REICHWEITEN:
        o.append(f"| B bis auf Zahlen gleich, {r} | {len(b_je[r])} | "
                 f"{zeilenzahl(b_je[r])} |")
    o.append(f"| C gleiches Ergebnis und gleiche Kontextwörter "
             f"(> 3 Zeilen) | {len(c)} | {zeilenzahl(g for _, g in c)} |")
    o.append(f"| D Personennamen (verschiedene) | {len(namen_zahl)} | "
             f"{namen_zeilen} |")
    o.append(f"| D Sachkontexte (Zeilen mit mindestens einem) | "
             f"{len(kontext_zahl)} | {len(zeilen) - ohne} |")
    o.append(f"| E aufgabe kürzer als {KURZ} Zeichen | – | {len(kurz)} |")
    o.append(f"| E aufgabe länger als {LANG} Zeichen | – | {len(lang)} |")
    o.append("")

    o.append("## A Wortgleich nach Normierung")
    o.append("")
    if not a:
        o.append("Keine.")
    for i, g in enumerate(a, 1):
        o.append(f"- A-{i:03d} ({reichweite(g)}, {len(g)} Zeilen): {ids(g)}  ")
        o.append(f"  {code(g[0]['_text'])}")
    o.append("")

    nummer = 0
    for r, titel in [("über Einträge", "über Einträge hinweg"),
                     ("im Eintrag", "im selben Eintrag, über Sprossen hinweg"),
                     ("in der Sprosse", "in derselben Sprosse (Varianten)")]:
        o.append(f"## B Bis auf Zahlen gleich, {titel}")
        o.append("")
        if r == "in der Sprosse":
            o.append("Nach bank.md unterscheiden sich Varianten einer Sprosse "
                     "in Zahlen und Kontext; hier fehlt der andere Kontext "
                     "(oder die Aufgabe hat keinen). Nur Kennung, Zeilen "
                     "und Text gekürzt.")
            o.append("")
        if not b_je[r]:
            o.append("Keine.")
        for g in b_je[r]:
            nummer += 1
            if r == "in der Sprosse":
                o.append(f"- B-{nummer:03d} ({len(g)}): {ids(g)} – "
                         f"{code(skelett(g[0]['_text']), 120)}")
            else:
                o.append(f"- B-{nummer:03d} ({len(g)} Zeilen): {ids(g)}  ")
                o.append(f"  {code(skelett(g[0]['_text']))}")
        o.append("")

    o.append("## C Gleiches Ergebnis und gleiche Kontextwörter "
             "(mehr als drei Zeilen)")
    o.append("")
    o.append(f"Davon mit mindestens zwei gemeinsamen Kontextwörtern: "
             f"{len(c_stark)}. Ein einzelnes Kontextwort (ein Name, ein "
             "Glücksrad) mit kleinem Ergebnis ist ein schwacher Befund.")
    o.append("")
    if not c:
        o.append("Keine.")
    for i, ((w, kontext), g) in enumerate(c, 1):
        o.append(f"- C-{i:03d} ({reichweite(g)}, {len(g)} Zeilen, "
                 f"{len(kontext)} Kontextwort"
                 f"{'e' if len(kontext) != 1 else ''}): "
                 f"Ergebnis {code(w)}, Kontext {code(', '.join(kontext))}: "
                 f"{ids(g)}  ")
        o.append(f"  {code(g[0]['aufgabe'], 200)}")
    o.append("")

    o.append("## D Personennamen und Sachkontexte")
    o.append("")
    o.append(f"Personennamen: {len(namen_zahl)} verschiedene in "
             f"{namen_zeilen} Zeilen (gezählt je Zeile). Die zehn häufigsten:")
    o.append("")
    o.append("| Rang | Name | Zeilen |")
    o.append("|--:|---|--:|")
    for i, (n, k) in enumerate(sorted(namen_zahl.items(),
                                      key=lambda x: (-x[1], x[0]))[:10], 1):
        o.append(f"| {i} | {n} | {k} |")
    o.append("")
    o.append("Sachkontexte (Wortliste KONTEXTE im Skript; eine Zeile kann "
             "mehrere haben):")
    o.append("")
    o.append("| Sachkontext | Zeilen |")
    o.append("|---|--:|")
    for n, k in sorted(kontext_zahl.items(), key=lambda x: (-x[1], x[0])):
        o.append(f"| {n} | {k} |")
    o.append(f"| {OHNE_KONTEXT} | {ohne} |")
    o.append("")

    o.append(f"## E Länge der aufgabe (unter {KURZ} oder über {LANG} Zeichen)")
    o.append("")
    for titel, liste in [(f"Kürzer als {KURZ}", kurz),
                         (f"Länger als {LANG}", lang)]:
        o.append(f"{titel} Zeichen: {len(liste)} Zeilen.")
        o.append("")
        for z in liste:
            o.append(f"- {z['id']} ({len(z['aufgabe'])}): "
                     f"{code(z['aufgabe'], 160)}")
        o.append("")

    text = "\n".join(o).rstrip("\n") + "\n"
    ZIEL_DATEI.write_text(text, encoding="utf-8", newline="\n")

    print(f"{len(eintraege)} Einträge, {len(zeilen)} Zeilen -> duplikate.md")
    for r in REICHWEITEN:
        print(f"  A {r:<15} {sum(1 for g in a if reichweite(g) == r):>4}")
    for r in REICHWEITEN:
        print(f"  B {r:<15} {len(b_je[r]):>4}")
    print(f"  C               {len(c):>4}")
    print(f"  E kurz/lang     {len(kurz)}/{len(lang)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

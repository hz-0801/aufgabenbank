#!/usr/bin/env python3
"""Sammelt Befunde und Offene Punkte aller bank/<eintrag>/stand.md.

Aufruf (nach jedem Bank-Auftrag, aus beliebigem Verzeichnis):
    python3 werkzeuge/befunde.py

Schreibt befunde.md in der Wurzel. Deterministisch: dieselben
stand.md ergeben dieselbe Datei (kein Datum, Stand = letzter Commit
auf bank/). Nur Standardbibliothek.

1. Einlesen: je stand.md die Abschnitte, deren Überschrift mit
   „## Befunde“ (auch „Befunde zu …“, „Befunde der …“) oder
   „## Offene Punkte“ beginnt. Ein Punkt beginnt mit „- “, „* “ oder
   „1. “; eingerückte Folgezeilen gehören dazu und werden mit einem
   Leerzeichen angehängt. Der Wortlaut bleibt sonst unverändert
   (ohne das Aufzählungszeichen).
2. Ziel: zuerst der Kopf des Punkts (Text vor dem ersten
   Doppelpunkt, wenn er in den ersten 60 Zeichen steht, sonst die
   ersten 40 Zeichen); gewinnt das Schlüsselwort, das dort am
   weitesten vorn steht („Katalog/bank.md“ → Katalog). Trifft im
   Kopf nichts, entscheidet der ganze Text nach der Rangfolge in
   RANG_TEXT. Trifft auch dort nichts: Sonstiges.
3. Gruppen: GRUPPEN nennt je Gruppe ein Muster (und ein
   Ausschlussmuster); ein Punkt gehört zur ersten Gruppe, die passt.
   Eine Gruppenzeile entsteht, wenn die Gruppe in mindestens zwei
   Einträgen vorkommt.
4. Sek II: alle Einträge außer SEK1; Bausteinwünsche nach
   BAUSTEIN_WUNSCH, benannt nach BAUSTEIN_NAMEN.
5. Gegenprobe: Aufzählungspunkte unter den Überschriften, direkt
   gezählt, gegen die Befundzeilen der geschriebenen befunde.md;
   die Differenz steht im Kopf und in der Ausgabe.
"""

import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
BANK = WURZEL / "bank"
ZIEL_DATEI = WURZEL / "befunde.md"

ABSCHNITT = re.compile(r"^## (Befunde|Offene Punkte)\b")
PUNKT = re.compile(r"^(- |\* |\d+\. )")

# Ziele in der Reihenfolge von befunde.md, mit Kürzel für die Nummer.
ZIELE = [
    ("Katalog", "K"),
    ("Prüfskript", "P"),
    ("bank.md", "B"),
    ("Vorlage/Bausteine", "V"),
    ("Zusammenbau", "Z"),
    ("Sonstiges", "S"),
]

# Schlüsselwörter je Ziel (reguläre Ausdrücke, ohne Groß-/Kleinschreibung,
# außer in (?-i:…)). Mappe und Katalogzeilen zählen zum Katalog, der
# Auftrag (auftrag-eintrag.md) zu bank.md.
SCHLUESSEL = {
    "Katalog": [
        r"Katalog", r"\bMappe\b", r"mappe\.py", r"Abschnitt 2",
        r"Erkennungsschritt", r"Sprossenzeile", r"Zielmarke",
        r"\bZ\. ?\d", r"\bZeilen? \d",
    ],
    "Prüfskript": [
        r"Prüfskript", r"\bSkript", r"\bSperr", r"Sperre", r"\bpruef\b",
        r"Ergebnisstelle", r"(?-i:KENNUNG)", r"(?-i:STANDARD)",
        r"normiert", r"Ankreuzprobe", r"--katalog", r"ksys_bereiche",
        r"Dublettenprobe", r"Zahlenfang", r"unbekannte[rn]? Baustein",
        r"gesperrt", r"unter v0\.\d",
    ],
    "bank.md": [
        r"bank\.md", r"\bAuftrag\b", r"Gegenprobe", r"\bform kennt\b",
        r"Kein Feld",
        r"id-Muster",
    ],
    "Vorlage/Bausteine": [
        r"Vorlage", r"_bausteine", r"\bkein(en)? [\w-]*Baustein",
        r"Baustein[^.;]*\bfehlt", r"\bfehl\w*[^.;]*Baustein",
        r"Bausteine? für", r"Rasterbaustein", r"^Bausteine\b",
        r"als Baustein nicht", r"Karofeld", r"beziffert",
    ],
    "Zusammenbau": [
        r"Zusammenbau", r"LaTeX", r"kompilier", r"\bRender",
        r"gerendert", r"ungesetzt", r"nicht gesetzt", r"Blattbau",
        r"beim Auswählen", r"Auswahl", r"ungeprüft",
        r"Dezimal(punkt|komma)", r"Blätter\b", r"ein Blatt\b", r"je Blatt",
        r"fürs Blatt",
    ],
}

# Rangfolge, wenn der Kopf nichts trifft (ganzer Text).
RANG_TEXT = ["Vorlage/Bausteine", "Zusammenbau", "Prüfskript", "bank.md",
             "Katalog"]

# Gruppen: (Name, Muster, Ausschluss oder None). Erste passende gewinnt.
GRUPPEN = [
    ("Erkennungsschritt doppelt über Einheitsgrenzen oder mehrfach geführt",
     r"Erkennungsschritt[^.]*(Einheitsgrenzen|innerhalb (derselben|einer)"
     r" Einheit|vor Einheit \d+ und \d+|vor e\d und e\d|zweimal|an zwei"
     r" Stellen|dreifach|nur einmal|in E1 als Kette)"
     r"|(vor Einheit \d+ und \d+|zweimal|an zwei Stellen|dreifach)"
     r"[^.]*Erkennungsschritt"
     r"|Vorstufe von zwei Ketten|Erkennungsschritt vor e\d und e\d",
     None),
    ("Erkennungsschritt wiederholt Vorstufe",
     r"Erkennungsschritt[^.]*Vorstufe|Vorstufe[^.]*Erkennungsschritt"
     r"|Vorstufen[^.]*doppelt|Erkennungsschritte[^.]*decken sich",
     None),
    ("Grundfall „viermal“ im Katalog gegen 5 Zeilen in bank.md",
     r"viermal", None),
    ("„Fertigkeit bis zum Doppelpunkt“ passt nicht",
     r"bis zum Doppelpunkt|keinen Doppelpunkt|ohne Doppelpunkt"
     r"|Doppelpunkten in der Klammer|keine[nr]? Doppelpunkt", None),
    ("Katalog nennt Nachzüge nach dem Katalog-Commit",
     r"Katalog-Commit|Nachz(ug|üge)[^.]*2026-09-2[89]", None),
    ("Kennungen der Sprossen fehlen in Abschnitt 2 der Mappe",
     r"(fehl\w*|nicht|weder)[^.]{0,80}Abschnitt 2"
     r"|Abschnitt 2[^.]{0,40}(fehl|nicht|führt sie nicht)"
     r"|(Mappe|mappe\.py) nicht aufnimmt|Mappe führt (sie|beide|das"
     r" Original) nicht|nicht in der Mappe|nur in der Mappe fehlen"
     r"|Mappe[^.]*führt (sie|beide) nicht",
     r"obwohl beide in Abschnitt 2|in Abschnitt 2, aber in keiner"),
    ("Feld original verwirft Kennungsform (Landes-, IQB-, fhr-Kennung)",
     r"(?-i:KENNUNG)|original unvollständig|fhr-Kennungen"
     r"|iqb-Kennungen|Kennungen[^.]*Muster", None),
    ("Integral als Unicode ∫ oder in Worten",
     r"∫|Integral-Schreibweise", None),
    ("Standard-LaTeX fehlt in STANDARD (\\int, \\lim, \\binom, \\sin …)",
     r"(?-i:STANDARD)|Standardbefehl|unbekannte[rn]? Baustein"
     r"|fehlende[rn]? Baustein|fremde[rn]? Baustein|nicht in _bausteine"
     r"|kein Baustein ist|weder Baustein noch|als Baustein (ablehnt|nicht"
     r" geprüft)|kein erlaubter Befehl|erlaubte[nr]? (LaTeX-)?Befehl"
     r"|\\binom fehlt|\\binom kein|Prüfskript \\?int kennt"
     r"|\\int und \\lim fehlen|\\int fehlt",
     None),
    ("Kastenzahl-Gegenprobe wörtlich nicht einhaltbar (bank.md festlegen)",
     r"Kastenzahl[^.]*(wörtlich|widersprich|nicht einhaltbar|nicht"
     r" erfüllbar|Allerweltszahlen|jede Zehnerpotenz|ausnehmen|verschieden)"
     r"|(Kastenzahlen?)“[^.]*(widerspricht|wörtlich)"
     r"|Kastenzahlregel|Umrechnungszahlen",
     None),
    ("Mehrstellige Kastenzahlen prüft das Skript nicht",
     r"Kastenzahl[^.]*(prüft (es|das Skript) nicht|nicht geprüft"
     r"|fängt[^.]*nicht|erfasst[^.]*nicht|meldet[^.]*nicht|keine Probe"
     r"|fehlt|prüft es nicht)"
     r"|(Keine Probe|nicht)[^.]*Kastenzahl|einzelne Kastenzahlen"
     r"|einzelne mehrstellige Kastenzahl",
     None),
    ("Gegenprobe Kastenzahlen bestanden (Bericht)",
     r"Kastenzahl|Zahlen im Merkkasten", None),
    ("Sperre erfasst Tripel mit Semikolon oder Tripel überhaupt nicht",
     r"Semikolon|Tripel[^.]*nicht gesperrt|Tripel nur mit"
     r"|zahlenpaare kennt nur", None),
    ("Sperre fängt Terme mit π, Wurzel oder Hochzahl nicht",
     r"(Sperr\w*|fängt)[^.]*(π|Wurzel|Hochzahl|belegten Terme)"
     r"|meldet x² = 36", None),
    ("Sperre zu breit (Gegenstand des Themas, Achsenpunkte, Allerweltsangaben)",
     r"Sperr\w*[^.]*(Gegenstand|Allerwelts|Achsen|Eckpunkte|Schreib"
     r"(weise|muster)|Einzelangaben|eng\b|Uhrzeit|Vertauschungsmatrix"
     r"|Präfix|zu breit|Zahlenpaar|x \+ y \+ z|k\(x\)|Parameterform"
     r"|F\(w\)|P\(X = 1\)|verbindet)"
     r"|(Achsen|Achsen- und Einheits)punkte[^.]*Sperre"
     r"|Kastenfunktion|nicht belegt \(2x² gesperrt\)",
     None),
    ("pruef \"\" nur bei pflicht begruenden erlaubt",
     r"pruef \"\"|pruef fehlt|verlangt pruef|verlangen pruef"
     r"|braucht pruef|ein pruef\b|Ersatzwert|Kontrollzahl|pruef als"
     r" JSON", None),
    ("Termlösungen nur über eine Zahl geprüft",
     r"(Term\w*|Nachweis\w*)[^.]*(nur (die )?erste Zahl|nur eine Zahl"
     r"|ersten Koeffizienten|nur Zahlanteile|nur über (eine Zahl|den"
     r" ersten|einen Koeffizienten)|nicht den Term|gleichwertig"
     r"|nicht die Umformung|nicht die Form|Zahlen, nicht)"
     r"|prüft Zahlen, nicht die Form|nur die Komponenten", None),
    ("Exponenten und Potenzen als Ergebnis nicht prüfbar",
     r"Exponent[^.]*(Zahl|prüfbar|Lösungsziffer)|normiert streicht"
     r" Exponenten", None),
    ("Ergebnisstelle erkennt Schreibweise nicht",
     r"Ergebnisstelle|Aufzählung|kennt „°“|Ergebnis nach", None),
    ("normiert() und \\mid",
     r"\\mid", None),
    ("Summen einer Vierfeldertafel und Relationen nicht geprüft",
     r"Randsummen|Spaltensummen", None),
    ("Ankreuzprobe: Teilwort, Mehrfachauswahl oder Termoptionen",
     r"Teilwort|„stumpf“|Mehrfachauswahl|Zahloption|\\janein"
     r"|Ankreuz\w*[^.]*(Gleichungen als Optionen|Option)", None),
    ("Wortauslöser verlangen eine Grafik (Lies, Graph, im Koordinatensystem)",
     r"verlangt eine Grafik|erzwingt eine Grafik|Ableseauftrag"
     r"|gilt als (Zeichen|Ablese)auftrag|Das Wort „Graph", None),
    ("Pool-Dubletten zählen als zwei Originale",
     r"Dublette[^.]*(Original|nicht geregelt)|Pool-Dubletten", None),
    ("Menge bei mehreren Originalen je Sprosse ungeregelt",
     r"zwei Originalen|mehr Originalen als|2 je Original|Original 3×"
     r"|Menge sprosse = 3|Menge 3 je Sprosse", None),
    ("Mehrere Verfahrensketten oder Prüfungshöhen je Einheit ungeregelt",
     r"(zwei|beide[nr]?) (Verfahrens)?[Kk]etten|genau eine Sprosse mit"
     r" hoehe pruefung|eine Prüfungssprosse je Einheit|je Verfahrenskette"
     r"|in beiden Ketten eine Prüfungshöhe|zwei Kettenzeilen"
     r"|10 statt 5 Grundfall|zehn Grundfallzeilen|je Kette oder je Einheit",
     None),
    ("Prüfungshöhe ohne Original ungeregelt",
     r"Prüfungs(höhe|sprosse) ohne (P10-)?Original|original null bei"
     r" pruefung|Zielmarke ohne Original|\(ohne Original; Zielmarke"
     r"|hoehe pruefung braucht ein original", None),
    ("Prüfungshöhe verlangt, was die Kette nicht einführt",
     r"2\.4 c|Kette nicht einführt|erst Einheit \d einführt|erst e\d"
     r" einführt|führt die Kette nicht ein|erst s\d einführt|das die"
     r" Kette nicht hat|keine Sprosse führt|Zwischensprosse fehlt"
     r"|voraussetzt \(Z\.", None),
    ("Zone nennt Begriffe des Themas (unterrichtsblatt 2.2)",
     r"2\.2[^.]*(Zone|Begriff|verbiet)|Zone[^.]*2\.2", None),
    ("Katalog-Ermessen: Zeilen wandern mit dem Typ",
     r"wander", None),
    ("Originale ohne Bankzeile oder nicht verfremdet",
     r"^(Ohne Zeile|Nicht verfremdet|Nicht als eigene Zeilen)"
     r"|in keiner Zeile verfremdet|blieb(en)? ohne Zeile"
     r"|ohne eigene Prüfungszeilen", None),
    ("Feld original nachtragen, sobald die Mappe die Kennung führt",
     r"sobald die Mappe", None),
    ("Kein Vieleck-Baustein für ksys3",
     r"Vieleck-Baustein", None),
    ("Grafik ohne Achsen, Achsenzahlen oder Skalenzahlen fehlt",
     r"ohne (Achsen|Achsenzahlen|Zahlen|vorgegebene Achsen)\b"
     r"|beschriftet die Achsen immer|beziffert", None),
    ("Dezimalkomma in Bausteinen ungeprüft",
     r"Dezimal(punkt|komma)|Punkt statt eines Kommas", None),
    ("Konvention gleichungsraster abgleichen",
     r"gleichungsraster", None),
    ("Kein LaTeX-Lauf: Satz und Grafiken ungeprüft",
     r"nicht kompiliert|kein LaTeX|LaTeX nicht|ungerendert"
     r"|nicht gerendert|nicht am Render|Rendern ungeprüft|ungesetzt"
     r"|nicht gesetzt worden|LaTeX-Lauf|Render prüfen|am Render"
     r"|nur auf Bausteinname", None),
    ("Rechner, Teil B oder Niveau beim Blattbau kennzeichnen",
     r"Rechner|Teil[- ]B|Zielmarke kennzeichnen|als Zielmarke setzen"
     r"|Niveaumarke|LK-Zusatz|nur LK|LK-Stoff|GK-Blätter|kein Blattstoff"
     r"|Niveau III", None),
    ("Pflichtelement darstellung oder anwendung fehlt",
     r"keine darstellung|kein Pflichtelement|Pflichtelemente anwendung"
     r"|ohne Pflichtelemente", None),
]

# Einträge der Sekundarstufe I; alle anderen gelten als Sek II
# (auch neu hinzukommende).
SEK1 = {
    "binomische-formeln", "bruchrechnung", "brueche-dezimalzahlen",
    "einheiten", "flaechen", "koerper", "kreis", "lineare-funktionen",
    "lineare-gleichungen", "lineare-gleichungssysteme", "potenzen-wurzeln",
    "prozentrechnung", "pyramide-kegel-kugel", "pythagoras",
    "quadratische-funktionen", "quadratische-gleichungen",
    "rationale-zahlen", "reelle-zahlen", "strahlensaetze",
    "symmetrie-abbildungen", "terme", "trigonometrie",
    "trigonometrische-funktionen", "wahrscheinlichkeit", "winkel-dreiecke",
    "zinsrechnung", "zuordnungen",
}

# Ein Punkt ist ein Bausteinwunsch, wenn eines dieser Muster trifft.
BAUSTEIN_WUNSCH = [
    r"\bkein(en)? [\w-]*Baustein\b(?! ist)", r"Baustein[^.;]*\bfehl",
    r"\bfehl\w*[^.;]*Baustein", r"Bausteine? für", r"keine Satzform",
    r"Vorlage (kennt|hat) kein", r"Diagramm-Baustein",
    r"Koordinatensystem ohne Achsenzahlen", r"beschriftet die Achsen immer",
    r"Schreibweise lim", r"Figur ohne Achsen", r"Karofeld ohne",
    r"\\binom\b", r"\\int\b", r"\\lim\b", r"\\sum\b", r"\\ln\b", r"\\max\b",
    r"\\tan\b", r"\\middle\b", r"\\iff\b", r"Integralzeichen",
    r"_bausteine\.md nicht belegt",
]

# Name des gewünschten Bausteins (mehrere möglich), in dieser Reihenfolge.
BAUSTEIN_NAMEN = [
    ("Spaltenvektor", r"Spaltenvektor"),
    ("Vektorpfeil im ebenen ksys", r"Vektorpfeil"),
    ("Matrix", r"Matri(x|zen)|pmatrix"),
    ("Pfeil-/Übergangsdiagramm", r"Pfeildiagramm|Diagramm-Baustein"),
    ("Vieleck in ksys3", r"Vieleck"),
    ("Schrägbild-Konvention ksys3", r"Schrägbild-Konvention"),
    ("Verteilungsfunktion (Graph)", r"Verteilungsfunktion"),
    ("Baum mit drei Ästen", r"drei Ästen"),
    ("Binomialkoeffizient \\binom", r"\\binom\b|Binomialkoeffizient"),
    ("Integral \\int", r"\\int\b|Integralzeichen"),
    ("Grenzwert \\lim", r"\\lim\b|Schreibweise lim"),
    ("Summe \\sum", r"\\sum\b"),
    ("\\ln", r"\\ln\b"),
    ("\\max", r"\\max\b"),
    ("\\tan", r"\\tan\b"),
    ("\\iff", r"\\iff\b"),
    ("\\middle", r"\\middle\b"),
    ("Koordinatensystem ohne Achsenzahlen", r"ohne Achsenzahlen|Achsen immer"),
    ("Karofeld ohne Achsen", r"Karofeld ohne"),
    ("Figur ohne Achsen", r"Figur ohne Achsen"),
]

KATALOGZEILE = re.compile(
    r"(?:\bZ\.|\bZeilen?|Katalogzeile)\s*"
    r"(\d+(?:\s*(?:[–-]|,|und|bzw\.|/)\s*\d+)*)")


def kompiliere(muster):
    return re.compile(muster, re.I)


SCHLUESSEL_RE = {z: [kompiliere(m) for m in ms] for z, ms in SCHLUESSEL.items()}
GRUPPEN_RE = [(n, kompiliere(m), kompiliere(a) if a else None)
              for n, m, a in GRUPPEN]
WUNSCH_RE = [kompiliere(m) for m in BAUSTEIN_WUNSCH]
NAMEN_RE = [(n, kompiliere(m)) for n, m in BAUSTEIN_NAMEN]


def lies_stand(pfad):
    """Punkte und direkte Zählung der Aufzählungszeichen einer stand.md."""
    punkte, roh, fliesstext = [], 0, []
    abschnitt, aktuell = None, None
    for zeile in pfad.read_text(encoding="utf-8").split("\n"):
        if zeile.startswith("#"):
            if aktuell:
                punkte.append(aktuell)
                aktuell = None
            abschnitt = zeile[3:].strip() if ABSCHNITT.match(zeile) else None
            continue
        if abschnitt is None:
            continue
        m = PUNKT.match(zeile)
        if m:
            roh += 1
            if aktuell:
                punkte.append(aktuell)
            aktuell = {"abschnitt": abschnitt, "text": zeile[m.end():].strip()}
        elif zeile.strip() == "":
            continue
        elif zeile[:1] in (" ", "\t") and aktuell:
            aktuell["text"] += " " + zeile.strip()
        else:
            fliesstext.append(zeile.strip())
    if aktuell:
        punkte.append(aktuell)
    return punkte, roh, fliesstext


def kopf(text):
    text = re.sub(r"^\((erledigt|teilweise)[^)]*\)\s*", "", text)
    text = re.sub(r"^N\d+\s+", "", text)
    i = text.find(":")
    return text[:i] if 0 <= i <= 60 else text[:40]


def frueh(k):
    """Ziel, dessen Schlüsselwort in k am weitesten vorn steht, oder None."""
    treffer = []
    for rang, (ziel, _) in enumerate(ZIELE[:-1]):
        for rx in SCHLUESSEL_RE[ziel]:
            m = rx.search(k)
            if m:
                treffer.append((m.start(), rang, ziel))
    return min(treffer)[2] if treffer else None


def ziel_von(text, abschnitt):
    z = frueh(kopf(text))
    if z:
        return z
    # „Befunde zu bank.md“, „Befunde zum Prüfskript (…)“
    z = frueh(re.sub(r"^(Befunde|Offene Punkte)\s*", "", abschnitt))
    if z:
        return z
    for ziel in RANG_TEXT:
        if any(rx.search(text) for rx in SCHLUESSEL_RE[ziel]):
            return ziel
    return "Sonstiges"


def gruppe_von(text):
    for name, rx, aus in GRUPPEN_RE:
        if rx.search(text) and not (aus and aus.search(text)):
            return name
    return ""


def status_von(text):
    if re.search(r"teilweise erledigt|\(erledigt v[\d.]+ für", text):
        return "teilweise"
    if re.search(r"\(erledigt\b", text):
        return "erledigt"
    return "offen"


def katalogzeilen(text):
    return "; ".join(m.group(1) for m in KATALOGZEILE.finditer(text))


def zelle(text):
    return text.replace("|", "\\|")


def bank_stand():
    try:
        aus = subprocess.run(
            ["git", "-C", str(WURZEL), "log", "-1", "--format=%h %cs",
             "--", "bank"], capture_output=True, text=True, check=True)
        return aus.stdout.strip() or "unbekannt"
    except (OSError, subprocess.CalledProcessError):
        return "unbekannt"


def main():
    staende = sorted(BANK.glob("*/stand.md"))
    zeilen, roh_summe, fliess = [], 0, []
    for pfad in staende:
        eintrag = pfad.parent.name
        punkte, roh, ft = lies_stand(pfad)
        roh_summe += roh
        fliess += [(eintrag, t) for t in ft]
        for p in punkte:
            t = p["text"]
            zeilen.append({
                "eintrag": eintrag,
                "art": "Offen" if p["abschnitt"].startswith("Offene")
                       else "Befund",
                "text": t,
                "ziel": ziel_von(t, p["abschnitt"]),
                "gruppe": gruppe_von(t),
                "status": status_von(t),
            })

    # Nummern je Ziel: Eintrag alphabetisch, dann Reihenfolge in stand.md.
    kuerzel = dict(ZIELE)
    je_ziel = {z: [r for r in zeilen if r["ziel"] == z] for z, _ in ZIELE}
    for z, rs in je_ziel.items():
        for i, r in enumerate(rs, 1):
            r["nr"] = f"{kuerzel[z]}-{i:03d}"

    gruppen = {}
    for r in zeilen:
        if r["gruppe"]:
            gruppen.setdefault(r["gruppe"], []).append(r)
    gruppen_mehr = []
    for name, rs in gruppen.items():
        eintraege = sorted({r["eintrag"] for r in rs})
        if len(eintraege) >= 2:
            ziele = sorted({r["ziel"] for r in rs},
                           key=[z for z, _ in ZIELE].index)
            gruppen_mehr.append((name, eintraege, rs, ziele))
    gruppen_mehr.sort(key=lambda g: (-len(g[1]), -len(g[2]), g[0]))
    in_gruppe = {g[0] for g in gruppen_mehr}

    sek2 = []
    for r in zeilen:
        if r["eintrag"] in SEK1:
            continue
        if any(rx.search(r["text"]) for rx in WUNSCH_RE):
            namen = [n for n, rx in NAMEN_RE if rx.search(r["text"])]
            sek2.append((namen, r))
    reihen = [n for n, _ in BAUSTEIN_NAMEN]
    sek2.sort(key=lambda x: (reihen.index(x[0][0]) if x[0] else len(reihen),
                             x[1]["eintrag"], x[1]["nr"]))

    # Schreiben
    o = []
    o.append("# Befunde der Bank")
    o.append("")
    o.append("Gebaut mit werkzeuge/befunde.py; nicht von Hand ändern, "
             "nach jedem Bank-Auftrag neu bauen.")
    o.append(f"Quelle: bank/*/stand.md, {len(staende)} Einträge, Abschnitte "
             "„Befunde …“ und „Offene Punkte“. Stand der Bank: "
             f"{bank_stand()} (letzter Commit auf bank/).")
    o.append("Ziel: Kopf des Punkts (vor dem ersten Doppelpunkt), sonst "
             "Schlüsselwörter im Text (Liste im Skript); Mappe und "
             "Katalogzeilen zählen zum Katalog, der Auftrag zu bank.md. "
             "Status „erledigt“ heißt: der Punkt trägt selbst "
             "„(erledigt …)“.")
    o.append("GEGENPROBE_PLATZHALTER")
    o.append("")
    o.append("## Zahl je Ziel")
    o.append("")
    o.append("| Ziel | Befunde | Offene Punkte | zusammen | davon erledigt |")
    o.append("|---|--:|--:|--:|--:|")
    for z, _ in ZIELE:
        rs = je_ziel[z]
        b = sum(r["art"] == "Befund" for r in rs)
        e = sum(r["status"] == "erledigt" for r in rs)
        o.append(f"| {z} | {b} | {len(rs) - b} | {len(rs)} | {e} |")
    b = sum(r["art"] == "Befund" for r in zeilen)
    e = sum(r["status"] == "erledigt" for r in zeilen)
    o.append(f"| Summe | {b} | {len(zeilen) - b} | {len(zeilen)} | {e} |")
    o.append("")
    o.append("## Die zehn häufigsten Gruppen")
    o.append("")
    o.append("Gezählt nach Einträgen; eine Gruppe ist derselbe Befund in "
             "mindestens zwei Einträgen (Muster im Skript).")
    o.append("")
    o.append("| Rang | Gruppe | Einträge | Punkte | Ziele |")
    o.append("|--:|---|--:|--:|---|")
    for i, (name, ein, rs, ziele) in enumerate(gruppen_mehr[:10], 1):
        o.append(f"| {i} | {zelle(name)} | {len(ein)} | {len(rs)} | "
                 f"{', '.join(ziele)} |")
    o.append("")
    o.append("## Gruppenzeilen")
    o.append("")
    o.append(f"{len(gruppen_mehr)} Gruppen mit mindestens zwei Einträgen.")
    o.append("")
    o.append("| Gruppe | Einträge | Liste | Punkte |")
    o.append("|---|--:|---|---|")
    for name, ein, rs, _ in gruppen_mehr:
        o.append(f"| {zelle(name)} | {len(ein)} | {', '.join(ein)} | "
                 f"{', '.join(r['nr'] for r in rs)} |")
    for k, (z, kz) in enumerate(ZIELE, 1):
        rs = je_ziel[z]
        o.append("")
        o.append(f"## {k} {z} ({len(rs)})")
        o.append("")
        if z == "Katalog":
            o.append("| Nr | Eintrag | Ziel | Zeile | Art | Status | Gruppe "
                     "| Befund |")
            o.append("|---|---|---|---|---|---|---|---|")
        else:
            o.append("| Nr | Eintrag | Ziel | Art | Status | Gruppe | Befund |")
            o.append("|---|---|---|---|---|---|---|")
        for r in rs:
            g = zelle(r["gruppe"]) if r["gruppe"] in in_gruppe else ""
            mitte = f" {katalogzeilen(r['text'])} |" if z == "Katalog" else ""
            o.append(f"| {r['nr']} | {r['eintrag']} | {z} |{mitte} "
                     f"{r['art']} | {r['status']} | {g} | {zelle(r['text'])} |")
    o.append("")
    o.append(f"## Bausteine, die Sek II braucht ({len(sek2)})")
    o.append("")
    o.append("Aus den Ständen der Sek-II-Einträge (alle außer den 27 "
             "Sek-I-Einträgen der Liste SEK1): jeder Punkt, der einen "
             "fehlenden Baustein, eine fehlende Satzform oder einen "
             "fehlenden LaTeX-Befehl nennt. Ziel Prüfskript heißt: "
             "Standard-LaTeX, das nur die Liste STANDARD nicht kennt.")
    o.append("")
    o.append("| Baustein | Eintrag | Ziel | Nr | Wortlaut |")
    o.append("|---|---|---|---|---|")
    for namen, r in sek2:
        o.append(f"| {zelle(', '.join(namen)) or '–'} | {r['eintrag']} | "
                 f"{r['ziel']} | {r['nr']} | {zelle(r['text'])} |")
    o.append("")
    text = "\n".join(o)

    # Gegenprobe gegen die Datei selbst: Befundzeilen = Tabellenzeilen
    # mit Nummer in den Zielabschnitten.
    ziel_teil = text.split("## Bausteine, die Sek II braucht")[0]
    datei_zeilen = len(re.findall(r"^\| [KPBVZS]-\d{3} \|", ziel_teil, re.M))
    diff = datei_zeilen - roh_summe
    grund = ""
    if diff:
        grund = (" Grund: Fließtext ohne Aufzählungszeichen unter den "
                 f"Überschriften ({len(fliess)} Zeilen)." if fliess
                 else " Grund: unbekannt, Skript prüfen.")
    gegen = (f"Gegenprobe: {roh_summe} Aufzählungspunkte unter „Befunde …“ "
             f"und „Offene Punkte“ in den stand.md, {datei_zeilen} "
             f"Befundzeilen in dieser Datei, Differenz {diff}.{grund}")
    text = text.replace("GEGENPROBE_PLATZHALTER", gegen)
    ZIEL_DATEI.write_text(text, encoding="utf-8", newline="\n")

    print(f"{len(staende)} stand.md, {len(zeilen)} Punkte -> befunde.md")
    for z, _ in ZIELE:
        print(f"  {z:<18} {len(je_ziel[z]):>4}")
    print(f"Gruppen mit >= 2 Einträgen: {len(gruppen_mehr)}; "
          f"Sek-II-Bausteinwünsche: {len(sek2)}")
    for eintrag, t in fliess:
        print(f"  Fließtext ohne Aufzählungszeichen: {eintrag}: {t}")
    print(f"Gegenprobe: roh {roh_summe}, Datei {datei_zeilen}, "
          f"Differenz {diff}")
    return 0 if diff == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

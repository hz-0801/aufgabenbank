#!/usr/bin/env python3
"""bericht.py – baut bau/render-alle/bericht.md aus ergebnis.json.

Die Deutung (Fehlerklassen, Gegenproben, Vorschläge) steht als Text in
KLASSEN und DEUTUNG unten; die Zahlen kommen aus ergebnis.json und aus der
Bank (Zählung der betroffenen Zeilen je Klasse über alle bank/*/*.jsonl).

    python3 bau/render-alle/bericht.py
"""
import glob
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parents[1]
ERG = json.load(open(HIER / "ergebnis.json", encoding="utf-8"))
E = ERG["eintraege"]


def git(*args, cwd=WURZEL):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                          text=True).stdout.strip()


# --- Bank lesen -------------------------------------------------------------

def lies_bank():
    rows = []
    for f in sorted(glob.glob(str(WURZEL / "bank" / "*" / "*.jsonl"))):
        for i, l in enumerate(open(f, encoding="utf-8"), 1):
            r = json.loads(l)
            r["_f"] = Path(f).relative_to(WURZEL).as_posix()
            r["_i"] = i
            rows.append(r)
    return rows


BANK = lies_bank()
FELDER = ("aufgabe", "loesung", "grafik", "loesungsgrafik")


def feld(r, name):
    return r.get(name) or ""


# --- Fehlerklassen ----------------------------------------------------------
# Jede Klasse: Schlüssel, Titel, Erkennung an der Fehlerstelle (Bausteinaufruf
# und Zeilentext aus dem Quelltext), Zählung in der Bank, Vorschlag.

def k1_stelle(f):
    return f["baustein"] in ("\\gl", "\\swz") and "\\text{" in f["zeilentext"] \
        and (f["id"] or "").startswith("quadratische-gleichungen")


def k1_bank(r):
    a = feld(r, "aufgabe")
    return r.get("form") == "gleichungsraster" and "$" not in a and \
        not re.search(r"[A-Za-zÄÖÜäöü]{3,}", re.sub(r"\\[a-z]+", "", a)) and \
        re.search(r"[\^_\\]", a)


def k2_stelle(f):
    return "__" in f["zeilentext"]


def k2_bank(r):
    return "__" in feld(r, "aufgabe")


def k3_stelle(f):
    return f["baustein"] == "\\dreieck" and "$" in f["zeilentext"]


def k3_bank(r):
    for n in FELDER:
        for m in re.finditer(r"\\dreieck\{[^}]*\}\{[^}]*\}\{[^}]*\}((?:\{[^}]*\}){6})",
                             feld(r, n)):
            if "$" in m.group(1):
                return True
    return False


def k4_stelle(f):
    return f["baustein"] == "\\saeulenab" and re.search(r"ylabel=[^{,\]]*=", f["zeilentext"])


def k4_bank(r):
    for n in FELDER:
        for m in re.finditer(r"\\saeulenab\[([^\]]*)\]", feld(r, n)):
            if re.search(r"ylabel=[^{,\]]*=", m.group(1)):
                return True
    return False


WT = re.compile(r"\\wertetabelle(\[[^\]]*\])?\{[^}]*\}\{[^}]*\}\{[^}]*\}\s*\\\\")


def k5_stelle(f):
    return f["baustein"] == "\\wertetabelle" and WT.search(f["zeilentext"])


def k5_bank(r):
    return any(WT.search(feld(r, n)) for n in FELDER)


def k6_stelle(f):
    return "$<$$" in f["zeilentext"] or "$>$$" in f["zeilentext"]


def k6_bank(r):
    a = r.get("antwort") or ""
    return "$" in a and re.search(r"[<>]", a) is not None


KLASSEN = [
    ("K1", "`\\gl{\\text{…}}` / `\\swz{$\\text{…}$}`: Gleichung ohne `$` im "
           "Feld aufgabe (form gleichungsraster)", k1_stelle, k1_bank,
     "Missing $ inserted – `^`, `_` oder `\\cdot` stehen in `\\text{}`"),
    ("K2", "`__` als Lücke im Feld aufgabe", k2_stelle, k2_bank,
     "Missing $ inserted – `_` im Textmodus"),
    ("K3", "`\\dreieck` mit `$…$` in den Beschriftungen", k3_stelle, k3_bank,
     "Missing $ inserted – die Vorlage setzt die sechs Labels selbst in `$…$`"),
    ("K4", "`\\saeulenab[… ylabel=$P(X = k)$ …]` – `=` im Optionswert ohne "
           "Klammern", k4_stelle, k4_bank,
     "Extra }, or forgotten $ – pgfkeys zerlegt den Wert am `=`"),
    ("K5", "`\\wertetabelle{…}{…}{…} \\\\` – Zeilenumbruch nach dem "
           "Blockbaustein", k5_stelle, k5_bank,
     "There's no line here to end – `\\wertetabelle` endet mit `\\par`"),
    ("K6", "Antwortgerüst mit `$…<…$`: Zusammenbau setzt `$<$` in ein "
           "offenes `$…$`", k6_stelle, k6_bank,
     "Command \\item/\\end{list} invalid in math mode – Mathe bleibt offen"),
]

VORSCHLAG = {
    "K1": ("Bankzeile", "aufgabe als `$x^2 = 81$` schreiben – so halten es alle "
           "anderen 668 gleichungsraster-Zeilen der Bank; `gl_inhalt()` streift "
           "das `$` dann ab und `\\gl{x^2 = 81}` steht wie in der Anleitung. "
           "Zweitbester Weg: Zusammenbau, `gl_inhalt()` gibt Zeilen ohne `$` "
           "und ohne Wörter roh weiter statt in `\\text{}`."),
    "K2": ("Bankzeile", "`__` im Lückensatz durch `\\leerfeld` ersetzen "
           "(bank.md: aufgabe trägt `\\leerfeld` nur im Lückensatz, das Gerüst "
           "gehört nach antwort). 13 Zeilen, alle in brueche-dezimalzahlen."),
    "K3": ("Bankzeile", "Beschriftungen ohne `$`: `{45\\text{ cm}}`, `{90^\\circ}` "
           "(Befund der Render-Probe vom 27.09., unverändert 25 Zeilen: "
           "pythagoras 17, flaechen 8). Alternativ Vorlage: `\\dreieck` könnte "
           "die Labels mit `\\ensuremath` statt `$…$` setzen, dann gingen "
           "beide Schreibweisen."),
    "K4": ("Bankzeile", "`ylabel={$P(X = k)$ in \\%}` mit Klammern (Befund der "
           "Render-Probe, unverändert 9 Zeilen). Alternativ Vorlage: der "
           "Optionsparser von `\\saeulenab` könnte `ylabel` als letzten "
           "Schlüssel mit Rest der Zeichenkette lesen – aufwendiger."),
    "K5": ("Bankzeile", "das `\\\\` nach `\\wertetabelle{…}` streichen (der "
           "Baustein schließt den Absatz selbst; vor ihm reicht ein Leerraum "
           "oder ebenfalls kein `\\\\`). 7 Zeilen in quadratische-funktionen. "
           "Anleitung könnte den Satz „Blockbaustein, kein `\\\\` danach“ "
           "tragen; in der Vorlage ließe sich ein folgendes `\\\\` mit "
           "`\\@ifnextchar` schlucken."),
    "K6": ("Zusammenbau", "`antwortfeld()` setzt `<`/`>` nur außerhalb `$…$` "
           "in Mathe (heute: nur, wenn kein `$` oder `\\` direkt davor steht). "
           "Die 6 Bankzeilen (reelle-zahlen e1 k1 s5, s9) brauchen Mathe im "
           "Gerüst wegen `\\sqrt{}`; sie sind nach bank.md („Gerüst wie auf "
           "dem Blatt“) vertretbar."),
}

GEGENPROBE = {
    "K1": "quadratische-gleichungen lernblatt und schwach: `\\text{…}` um die "
          "Gleichungen entfernt → 0 Fehlerzeilen (vorher 1035 / 1575).",
    "K2": "brueche-dezimalzahlen lernblatt: `__` → `\\leerfeld` in den drei Zeilen "
          "→ 0 Fehlerzeilen (vorher 25); s9-v1 war Folgefehler.",
    "K3": "pythagoras lernblatt: eine Zeile (e1-k2-s2-v1) auf `{45\\text{ cm}}…{90^\\circ}` "
          "→ 0 Fehlerzeilen (vorher 51); alle 18 anderen Stellen waren Folgefehler.",
    "K4": "binomialverteilung lernblatt: `ylabel={…}` in drei Aufrufen → 0 "
          "Fehlerzeilen (vorher 55, darunter der Abbruch „Emergency stop“).",
    "K5": "quadratische-funktionen lernblatt: `\\\\` nach `\\wertetabelle` gestrichen "
          "→ 0 Fehlerzeilen (vorher 8).",
    "K6": "reelle-zahlen lernblatt: `$< \\sqrt{6} $<$$` → `$< \\sqrt{6} <$` → 0 "
          "Fehlerzeilen (vorher 10).",
}


def klasse_von(f):
    for key, _, stelle, _, _ in KLASSEN:
        if stelle(f):
            return key
    return "Folge"


# --- Auswertung -------------------------------------------------------------

def zahl(x):
    return "–" if x is None else str(x)


def erster_fehler(x):
    if not x.get("vorhanden"):
        return "–"
    if x["kompiliert"]:
        return ""
    if not x["fehler"]:
        return "kein PDF"
    f = x["fehler"][0]
    ort = f"{f['datei']}:{f['zeile']}" if f["zeile"] else f["datei"]
    return f"{ort} {f['meldung'][:48]}"


def hauptblock():
    z = []
    laeufe = 0
    for e, v in E.items():
        for lauf, w in v.items():
            for datei, x in w.items():
                if x.get("vorhanden"):
                    laeufe += len(x["versuche"])
    n_lb = sum(1 for v in E.values() if "lernblatt" in v)
    ok_lb = sum(1 for v in E.values() if v["lernblatt"]["gesamt.tex"]["kompiliert"])
    n_sw = sum(1 for v in E.values() if "schwach" in v)
    ok_sw = sum(1 for v in E.values() if "schwach" in v and v["schwach"]["gesamt.tex"]["kompiliert"])
    ok_lo = sum(1 for v in E.values() for lauf in v if v[lauf]["loesungen.tex"]["kompiliert"])
    n_lo = sum(1 for v in E.values() for lauf in v)
    ok_beide = sum(1 for v in E.values()
                   if all(w["gesamt.tex"]["kompiliert"] for w in v.values()))
    seiten_lb = sum(v["lernblatt"]["gesamt.tex"]["seiten"] or 0 for v in E.values())
    seiten_sw = sum(v["schwach"]["gesamt.tex"]["seiten"] or 0 for v in E.values() if "schwach" in v)
    fehlende = Counter()
    for v in E.values():
        for w in v.values():
            for x in w.values():
                for c, n in x.get("fehlende_zeichen", {}).items():
                    fehlende[c] += n
    return dict(laeufe=laeufe, n_lb=n_lb, ok_lb=ok_lb, n_sw=n_sw, ok_sw=ok_sw,
                ok_lo=ok_lo, n_lo=n_lo, ok_beide=ok_beide, seiten_lb=seiten_lb,
                seiten_sw=seiten_sw, fehlende=fehlende)


def main():
    S = hauptblock()
    heute = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M UTC"],
                           capture_output=True, text=True).stdout.strip()
    bank_commit = git("log", "-1", "--format=%h %s")
    alle_stand = git("log", "-1", "--format=%h %ad", "--date=short", "--", "bau/_alle")
    sty = (WURZEL / "bau" / "_alle" / "bruchrechnung" / "lernblatt" / "mathblatt.sty")
    sty_version = re.search(r"Version (\S+)", sty.read_text(encoding="utf-8")).group(1)
    bb = WURZEL.parent / "blattbau"
    if (bb / "mathblatt.sty").exists():
        bb_commit = git("log", "-1", "--format=%h", cwd=bb)
        gleich = "byte-gleich" if (bb / "mathblatt.sty").read_bytes() == sty.read_bytes() else "abweichend"
    else:
        bb_commit, gleich = "?", "nicht verglichen (blattbau nicht geklont)"

    out = []
    w = out.append
    w("# Render-Lauf über alle Einträge")
    w("")
    w(f"Stand {heute}. Quelltexte: bau/_alle/ (Zusammenbau v0.1, Stand {alle_stand}), "
      f"Bank beim Commit {bank_commit}. Vorlage: mathblatt.sty „Version {sty_version}“ "
      f"aus bau/_alle/<eintrag>/<lauf>/ – {gleich} mit hz-0801/blattbau@{bb_commit}. "
      f"Umgebung: {ERG['xelatex']}, Ubuntu-Pakete nach werkzeuge/render.md, "
      "Einrichtung ohne Befund (apt erreichbar, xelatex und pdftotext lagen "
      "nach der Installation vor).")
    w("")
    w("Weg: bau/render-alle/render.py kopiert jeden Lauf in eine Arbeitskopie "
      "außerhalb des Repos und kompiliert dort gesamt.tex (Auftrag) und "
      "loesungen.tex (Zusatz, weil die Lösungsdateien nicht in gesamt.tex "
      "stecken) mit `xelatex -interaction=nonstopmode -file-line-error`, "
      "zwei Läufe je Datei (Abhakseite, Sprungziele), ein dritter nur bei "
      "„Rerun“ in der .log – nirgends nötig. Zählgrenze 3 Versuche je Datei, "
      f"nie erreicht. Kompilierläufe insgesamt: {S['laeufe']}. Je Versuch stehen "
      "die ersten 60 Fehlerzeilen der .log mit Kontext in logs/<eintrag>-<lauf>-<datei>.txt. "
      "Danach pdfinfo (Seiten) und pdftotext (Textgehalt: jedes PDF enthält "
      "Text, kein leeres Blatt). Fehlerstellen sind je (Datei, Zeile) die erste "
      "Meldung; xelatex läuft nach einem Fehler weiter und meldet Folgefehler "
      "bis zum Dateiende, darum steht in der Tabelle die Zahl der Stellen, "
      "nicht der Logzeilen. Die Bankzeile zu einer Stelle ermittelt render.py "
      "über den Text der Teilaufgabe (118 Stellen in Teilaufgaben: 2 wörtlich, 116 nach "
      "Ähnlichkeit, alle ≥ 0,95; die 8 übrigen Stellen liegen in abhaken.tex "
      "und gesamt.tex – Folgefehler ohne Bankzeile); ergebnis.json hält alles.")
    w("")
    w("## Ergebnis")
    w("")
    w(f"- gesamt.tex Lernblatt: **{S['ok_lb']} von {S['n_lb']} Einträgen kompilieren** "
      f"fehlerfrei; schwach: {S['ok_sw']} von {S['n_sw']}; beide Läufe eines "
      f"Eintrags fehlerfrei: {S['ok_beide']} von {S['n_lb']}. "
      f"Alle {S['n_lb']} Einträge liefern ein PDF, auch die mit Fehlern (xelatex "
      "setzt nach einem Fehler weiter; nur binomialverteilung/lernblatt bricht "
      "mit „Emergency stop“ ab und hat ein unvollständiges PDF).")
    w(f"- loesungen.tex: {S['ok_lo']} von {S['n_lo']} Läufen fehlerfrei.")
    w(f"- Seiten: {S['seiten_lb']} (Lernblatt gesamt.tex) + {S['seiten_sw']} (schwach).")
    w("- Sechs Fehlerklassen, alle mit Gegenprobe bestätigt (Abschnitt „Fehler "
      "nach Baustein“): fünf liegen in Bankzeilen, eine im Zusammenbau. Die "
      "Vorlage hat keinen Kompilierfehler.")
    n_fz = sum(S["fehlende"].values())
    w(f"- Stiller Befund ohne Fehlerzeile: **{n_fz} fehlende Zeichen** "
      "(„Missing character“ in der .log): Unicode-Zeichen wie ≈, α, β, γ, π, ∫, "
      "ℝ, ⇔, ✓ stehen im Text, Latin Modern Roman hat sie nicht, im PDF bleibt "
      "die Stelle leer. Abschnitt „Fehlende Zeichen“.")
    w("")
    w("## Je Eintrag")
    w("")
    w("gesamt.tex je Lauf: kompiliert (ja/nein), Seiten, Zahl der Fehlerstellen "
      "und der erste Fehler mit Datei:Zeile. Lös.: loesungen.tex Lernblatt/schwach "
      "(Seiten, alle fehlerfrei). Zeichen: fehlende Zeichen im Lernblatt gesamt.tex. "
      "„–“: kein schwach-Lauf (Sek II).")
    w("")
    w("| Eintrag | LB | Seiten | Stellen | erster Fehler | schwach | Seiten | Stellen | erster Fehler | Lös. | Zeichen |")
    w("| --- | --- | --: | --: | --- | --- | --: | --: | --- | --- | --: |")
    for e in sorted(E):
        v = E[e]
        lb = v["lernblatt"]["gesamt.tex"]
        sw = v.get("schwach", {}).get("gesamt.tex")
        lo = zahl(v["lernblatt"]["loesungen.tex"]["seiten"])
        if "schwach" in v:
            lo += "/" + zahl(v["schwach"]["loesungen.tex"]["seiten"])
        fz = sum(lb["fehlende_zeichen"].values())
        row = [e, "ja" if lb["kompiliert"] else "**nein**", zahl(lb["seiten"]),
               str(lb["fehlerstellen"]), erster_fehler(lb)]
        if sw:
            row += ["ja" if sw["kompiliert"] else "**nein**", zahl(sw["seiten"]),
                    str(sw["fehlerstellen"]), erster_fehler(sw)]
        else:
            row += ["–", "–", "–", "–"]
        row += [lo, str(fz) if fz else ""]
        w("| " + " | ".join(row) + " |")
    w("")

    # Fehler nach Baustein
    w("## Fehler nach Baustein")
    w("")
    w("Jede Fehlerstelle des Laufs (gesamt.tex, beide Läufe) ist einer Klasse "
      "zugeordnet; „Folgefehler“ sind Stellen, die nach einer Gegenprobe mit "
      "der ersten Ursache verschwinden (Umgebung nach dem Fehler nicht mehr "
      "geschlossen, `\\item`-Meldungen an jedem weiteren `\\teil`, Meldungen "
      "an `\\end{aufgabe}`, in abhaken.tex und gesamt.tex). Die Spalte "
      "„Bank“ zählt alle Zeilen der Bank mit demselben Muster, auch die im "
      "Lauf nicht gewählten Varianten (Regel „Variante 1“).")
    w("")
    stellen = defaultdict(list)
    folge = defaultdict(list)
    for e, v in E.items():
        for lauf, wv in v.items():
            for f in wv["gesamt.tex"]["fehler"]:
                k = klasse_von(f)
                if k == "Folge":
                    folge[(e, lauf)].append(f)
                else:
                    stellen[k].append((e, lauf, f))
    bankzeilen = {}
    for key, _, _, bank, _ in KLASSEN:
        bankzeilen[key] = [r for r in BANK if bank(r)]
    w("| Klasse | Bausteinaufruf | Meldung | Stellen im Lauf | Bankzeilen im Lauf | Bank gesamt | Einträge | Vorschlag |")
    w("| --- | --- | --- | --: | --: | --: | --- | --- |")
    for key, titel, _, _, meldung in KLASSEN:
        st = stellen[key]
        ids = sorted({f["id"] for _, _, f in st if f["id"]})
        bz = bankzeilen[key]
        eintr = Counter(r["eintrag"] for r in bz)
        w(f"| {key} | {titel} | {meldung} | {len(st)} | {len(ids)} | {len(bz)} | "
          + ", ".join(f"{k} {n}" for k, n in sorted(eintr.items()))
          + f" | **{VORSCHLAG[key][0]}** |")
    n_folge = sum(len(v) for v in folge.values())
    w(f"| – | Folgefehler | `\\item`-Meldungen an `\\teil`/`\\swz`, `\\end{{aufgabe}}`, abhaken.tex, gesamt.tex, Emergency stop | {n_folge} | – | – | "
      + ", ".join(f"{e}/{l} {len(v)}" for (e, l), v in sorted(folge.items())) + " | keiner |")
    w("")
    for key, titel, _, _, meldung in KLASSEN:
        st = stellen[key]
        ids = sorted({f["id"] for _, _, f in st if f["id"]})
        bz = bankzeilen[key]
        w(f"### {key} – {titel}")
        w("")
        w(f"- Meldung: {meldung}.")
        w(f"- Im Lauf: {len(st)} Stellen, Bankzeilen: " + ", ".join(ids) + ".")
        w(f"- In der Bank gesamt: {len(bz)} Zeilen – " + ", ".join(
            f"{r['id']} ({r['_f']}:{r['_i']})" for r in bz) + ".")
        w(f"- Gegenprobe: {GEGENPROBE[key]}")
        w(f"- Vorschlag: **{VORSCHLAG[key][0]}** – {VORSCHLAG[key][1]}")
        w("")
    w("Vorlage: keine der sechs Klassen ist ein Fehler in mathblatt.sty; bei "
      "K3, K4 und K5 könnte die Vorlage nachsichtiger werden (oben je genannt), "
      "der Fehler liegt aber in der Schreibweise der Zeile gegen die Anleitung.")
    w("")
    w("Strukturprüfung des Zusammenbaus (bau/_alle/bericht.md): sie meldete K1 "
      "und K2 („^/_ außerhalb Mathe“) und die zwei `\\rechnung`-Stellen in "
      "quadratische-funktionen e3/e4 – die kompilieren hier ohne Fehlermeldung "
      "(das Bild dieser Stellen wurde nicht angesehen). Nicht gesehen "
      "hat sie K3–K6: `$` in Argumenten, die der Baustein selbst in Mathe "
      "setzt; `=` in Optionswerten; `\\\\` nach einem Blockbaustein; das "
      "Gerüst aus antwort. Vorschlag Zusammenbau: die vier Muster in "
      "`modusfehler()` bzw. `pruefe_struktur()` aufnehmen, dazu die "
      "Argumentliste der Bausteine mit „setzt selbst Mathe“ aus der Anleitung.")
    w("")

    # Fehlende Zeichen
    w("## Fehlende Zeichen")
    w("")
    w("„Missing character: There is no X“ in der .log heißt: das Zeichen fehlt "
      "in der Schrift, im PDF steht nichts. Kein Fehler, kein Hinweis auf dem "
      "Blatt. Zählung über gesamt.tex und loesungen.tex beider Läufe (ein "
      "Zeichen zählt in jeder Datei, in der es gesetzt wird):")
    w("")
    w("| Zeichen | Vorkommen |")
    w("| --- | --: |")
    for c, n in S["fehlende"].most_common():
        w(f"| {c} | {n} |")
    w("")
    je = defaultdict(Counter)
    for e, v in E.items():
        for c, n in v["lernblatt"]["gesamt.tex"]["fehlende_zeichen"].items():
            je[e][c] += n
    w(f"Betroffen (Lernblatt gesamt.tex): {len(je)} von {S['n_lb']} Einträgen – "
      + "; ".join(f"{e} {sum(c.values())} ({', '.join(k.split(' ')[0] + ' ' + str(n) for k, n in c.most_common(3))})"
                  for e, c in sorted(je.items(), key=lambda kv: -sum(kv[1].values()))) + ".")
    w("")
    # Bank: Zeilen mit diesen Zeichen
    zeichen = {k.split(" ")[0] for k in S["fehlende"]}
    im_text, in_mathe = Counter(), Counter()
    zeilen = set()
    for r in BANK:
        for n in FELDER + ("antwort",):
            m = False
            for ch in feld(r, n):
                if ch == "$":
                    m = not m
                elif ch in zeichen:
                    (in_mathe if m else im_text)[ch] += 1
                    zeilen.add(r["id"])
    w(f"In der Bank tragen {len(zeilen)} Zeilen diese Zeichen, fast alle im "
      f"Textmodus ({sum(im_text.values())} im Text, {sum(in_mathe.values())} in "
      f"`$…$` – dort meldet XeTeX sie ebenfalls, weil auch die Mathe-Schrift "
      "sie nicht als Unicode kennt). Dazu kommen Titel aus den Mappen "
      "(„Bruch ↔ Dezimalzahl“, Befund der Render-Probe).")
    w("")
    w("Vorschlag: **Vorlage.** Eine Zuordnungstabelle in mathblatt.sty "
      "(`\\RequirePackage{newunicodechar}`, je Zeichen "
      "`\\newunicodechar{≈}{\\ensuremath{\\approx}}`, `{α}{\\ensuremath{\\alpha}}`, "
      "… für die 37 Zeichen der Tabelle) setzt sie im Text und in Mathe richtig; "
      "Gegenprobe: winkel-dreiecke (62 fehlende Zeichen) und trigonometrie (44) "
      "mit dieser Tabelle im Vorspann → 0 fehlende Zeichen, 0 Fehler. Die "
      f"Alternative – {len(zeilen)} Bankzeilen auf `$\\approx$`, `$\\alpha$` "
      "umschreiben – ist teurer und bank.md verlangt sie nicht (Umlaute und "
      "Sonderzeichen „direkt“). Die Tabelle kann nach dem Umbau der Vorlage "
      "als Regel in bank.md stehen: erlaubt sind genau die Zeichen der Tabelle.")
    w("")

    # Weitere Beobachtungen
    w("## Weitere Beobachtungen aus der .log")
    w("")
    ub = {e: v["lernblatt"]["gesamt.tex"]["ueberbreit"] for e, v in E.items()}
    mw = {e: v["lernblatt"]["gesamt.tex"]["mathblatt_warnungen"] for e, v in E.items()}
    ub_sw = {e: v["schwach"]["gesamt.tex"]["ueberbreit"] for e, v in E.items() if "schwach" in v}
    w(f"- Überbreite Zeilen (`Overfull \\hbox` über 5 pt): {sum(ub.values())} im "
      f"Lernblatt, {sum(ub_sw.values())} in schwach. Lernblatt am meisten: "
      + ", ".join(f"{e} {n}" for e, n in sorted(ub.items(), key=lambda kv: -kv[1])[:8] if n)
      + ". Meist lange Formeln oder Grafiken neben Text; im Lauf nicht geprüft, "
      "ob sie über den Rand ragen.")
    w(f"- `Package mathblatt Warning`: {sum(mw.values())} im Lernblatt ("
      + ", ".join(f"{e} {n}" for e, n in sorted(mw.items(), key=lambda kv: -kv[1]) if n)
      + f"), {sum(v['schwach']['gesamt.tex']['mathblatt_warnungen'] for v in E.values() if 'schwach' in v)} in schwach – "
      "Hauptnummern, die nicht auf eine Seite passen (Vorlage bricht sie dann "
      "doch um). Deckt sich mit den 227 WARNUNG-Zeilen des Zusammenbaus "
      "(Halbseitenmaß), das v0.1 nur im Fokus teilt.")
    w("- Nicht geprüft: Seitenbild (Lage der Grafiken, Felder neben Streifen, "
      "Abhakseite mit Zone) – nur Log und Seitenzahl, kein Blick aufs PDF. "
      "Das ist der nächste Schritt, sobald die sechs Klassen behoben sind: je "
      "Eintrag ein Blick auf die Seiten mit WARNUNG.")
    w("")
    w("## Dateien")
    w("")
    w("- render.py – der Lauf (Arbeitskopie unter $RENDER_ARBEIT, Standard /tmp/render-alle; PDFs bleiben dort).")
    w("- ergebnis.json – alle Messwerte je Eintrag, Lauf und Datei; Fehlerstellen mit Bankzeile-id und Zuordnungsgüte.")
    w("- logs/<eintrag>-<lauf>-<datei>.txt – je Versuch die ersten 60 Fehlerzeilen der .log mit drei Kontextzeilen.")
    w("- bericht.py – baut diese Datei aus ergebnis.json; Deutung und Vorschläge stehen im Skript.")
    w("- Gegenproben liefen in Arbeitskopien außerhalb des Repos (Bankzeilen und Skripte unverändert).")
    (HIER / "bericht.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"bericht.md geschrieben: {S['ok_lb']}/{S['n_lb']} Lernblatt, {S['ok_sw']}/{S['n_sw']} schwach, "
          f"{S['laeufe']} Kompilierläufe, {n_fz} fehlende Zeichen")


if __name__ == "__main__":
    main()

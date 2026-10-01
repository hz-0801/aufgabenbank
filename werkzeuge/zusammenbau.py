#!/usr/bin/env python3
"""zusammenbau.py v1.0 – aus bank/<eintrag>/ LaTeX-Quelltexte für mathblatt.sty.

Aufruf:
    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach] [--klasse 7]
        [--kasten] [--aus <ordner>] [--vorlage <mathblatt.sty>]
        [--ohne-register] [--kuerzel <_kuerzel.csv>] [--nummer n]
        [--mit-sachaufgaben]
    python3 werkzeuge/zusammenbau.py <eintrag> <eintrag> … --heft [msa|
        abitur-gk|abitur-lk|fhr] [--nur-basis] [--titel <text>] --aus <ordner>
    python3 werkzeuge/zusammenbau.py --zettel basis [--nummer n]
        [--ohne-register]
    python3 werkzeuge/zusammenbau.py <eintrag> --fokus-pruefung <kette>
        [--heft msa|abitur-gk|abitur-lk|fhr] [--einheiten n] [--aus <ordner>]
    python3 werkzeuge/zusammenbau.py <eintrag> --kompetenz <kette>
        --einheiten n [--niveau for|ebr] [--dicht] [--ohne <ids>]

v1.0 (2026-10-01, auftrag-lernblatt-v10.md, Befunde des Lehrers am TER-L4):
Rezept L (Lernblatt); F, S und K unverändert, wo sie den Code teilen.
- Blattfolge aus der Mappe („Blattfolge: 2, 3, 4, 1“); je Einheit erst die
  Ketten ohne Textaufgabe im Grundfall, dann die mit (log FOLGE).
- Keine Verzeichniszeile, kein „Einheit n von m“, keine Zweigzeile: je
  Einheit nur der Titel; Typen nur für das Gymnasium: „GYM“ klein im Titel.
- Titel der Hauptnummern im Infinitiv (ich-kann.csv, Spalte titel).
- Auftrag nur bei Mehrdeutigkeit: kein Auftrag über nackten Zahlrechnungen
  und Termen mit „=“; einmal oben nur bei nackten Termen und Gleichungen,
  sonst je Teilaufgabe der ganze Satz.
- Rechenweg-Striche wie die Antwortlinie, halbe Breite, eine Zeile Luft;
  Grafik links, Antwort rechts; Ankreuzen nebeneinander nur bis 120 Zeichen.
- Keine Teilung unter 27 Teilaufgaben, kein „– weiter“.
- Test „Kannst du das schon?“ am Kopf jeder Einheit (statt „Prüfe dich“
  und „Das kann ich“); Pflichtelemente je Sorte eine Teilaufgabe in
  „Verstanden?“ am Ende der Einheit; je Kette höchstens eine Teilaufgabe
  mit Sachkontext (--mit-sachaufgaben hebt das auf).
- Lösungen am Ende des Gesamt.

v0.9 (2026-09-30): Lernblatt (Rezept L, dazu F und S, wo sie denselben Code
nutzen) im Satz des Kompetenzblatts (KbSatz, vorspann.tex):
- Auftrag einmal über der Nummer: „Verb …: Term“, „Verb. Term“, gleicher
  Satzanfang mit Lücke, gleicher Schlusssatz, gleiche Aufgabe mit anderen
  Zahlen an höchstens zwei Stellen (laeufe_von); ein Auftrag steht nie zweimal
  in einer Hauptnummer (zerteile teilt dort, „– weiter“).
- Kurze Terme (bis 30 Zeichen) und kurze Ankreuzaufgaben zwei nebeneinander
  (\\lbpaar), „= ____“ hinter dem Term, kein Raum; Vorstufen paarweise.
- Titel: Ich-kann-Satz aus bau/regal/ich-kann.csv je Hauptnummer (Kette,
  Sprosse, p, Pflichtelement, Zone, Zone-Paar); Ersatz „Ich kann: <merkmal>.“
- Zweigzeile „Hier lernst du, …“ · Zeitmarke · Prüfungswort · „baut auf: …“.
- Mengen nach bank.md: Vorstufe alle, Grundfall vier von fünf, jede weitere
  Sprosse eine, Prüfungshöhe je Original eine, Typ ohne Kette alle, Pflicht
  je Zeile; Zone je Fertigkeit zwei sehr leichte, eine mittlere, je Fallstrick
  eine, Zone-Paar; Teilung 2.3 g ausgewogen.
- Zone: „Hängst du hier? → Nr. n“ auf die erste Nummer, die die Fertigkeit
  braucht. Fußzeile nur Kennung und Seite (Befund 2). --nummer auch für L/F/S.
v0.9, zweiter Durchgang (2026-09-30, auftrag-lernblatt-v09.md):
- Grundfall so oft wie „(n×)“ in der Sprossenzeile der Mappe (sonst vier);
  Prüfungshöhe nach der Regel des Kompetenzblatts (waehle_originale: je
  Original eine, jüngste fünf Jahrgänge, Formulierungen, bis fünf).
- Auftrag einmal auch im Kompetenzblatt; Teilung erst nach Maß, dann am
  wiederholten Auftrag (auch einer einzelnen Teilaufgabe); Prüfung AUFTRAG.
- Zweigzeile „Hier lernst du, <Titel> – <Beschreibung wie im Katalog>“;
  „baut auf“ und Blatt-0-Verweis aus den Einheiten der Voraussetzungszeile.
- Blatt 0: Verweis „Hängst du hier → Nr. n“ als Zeile unter der Nummer,
  Zone-Paar am Ende, Lösung „falsch → Lücke: …“ bei Fallstricken.
- Schluss „Prüfe dich“ (je Verfahrenskette die mittlere Sprosse, gemischt)
  und „Das kann ich“ je Kette darunter; Kopf „Thema · Lernblatt“.

v0.8 (2026-09-28): Rezept K nach dem Sprachlauf (bau/sprachlauf/regeln.md):
- Aufgabe in ganzen Sätzen: ein normaler Absatz, kein halbfetter Auftakt mit
  Kurzfrage; „Verb. Term“: Verb als Anweisung, Term halbfett (satzform).
- Keine Anweisung aus ich-kann.csv, wenn die Aufgabe selbst auffordert.
- Befund 49: keine Linie unter Abschnittsüberschrift und Merkkastentitel.
- Befund 37/53: Abschnitt „Schritt für Schritt“ entfällt.
- Befund 40/52: Merkkasten als Mathe ($…$, \\frac, \\sqrt; Division als
  Bruch), kasten_mathe.
- Zone-Auswahl ohne den Aufgabentext (merkmal, sprosse_text, loesung), damit
  eine Umformulierung die Auswahl nicht verschiebt.

v0.7 (2026-09-28): Rezept K, Kompetenzblatt (--kompetenz <kette>, Kennung
XXX-K<n>): Zone „Das kennst du schon“, Leiter der Kette (je Sprosse eine
Hauptnummer, Variante 1), Prüfungshöhen nach Beschluss d, Merkkasten; Layout
nach bau/layout-befunde.md im Vorspann vorspann.tex; Lösungen eigene Datei.

v0.6 (2026-09-28): Rezept P, Prüfungs-Fokus (--fokus-pruefung <kette>,
Kennung XXX-P<n>): Anlauf der Kette, alle Prüfungshöhen im Profil,
Merkkasten der Einheit am Ende.

v0.5 (2026-09-28): Rezept Zettel (--zettel basis, Kennung BAS-Z<n>,
zehn Aufgaben aus bank/_basis/); Prüfkennung kurz in allen Rezepten
(„(P24)“, „(P26F)“, „(A23L)“, „(F25)“, Sternchen wie im Original
dahinter); Zweigzeile mit Zahl der Jahrgänge („P10 ×5“, „Abi GK ×8“).

Ohne Schalter: Lernblatt mit Zone und allen Einheiten, Mengen nach bank.md
(seit v0.9), ohne Klasse. Jeder Bau bekommt eine Kennung XXX-R<n>
(Kürzel des Eintrags, Rezept L/F/S/H, laufende Nummer aus
bau/register.csv) und landet unter bau/<eintrag>/<kennung>/, mit --aus
im genannten Ordner. Die Registerzeile wird angehängt, daneben
bau.json (Bauzettel). --ohne-register: Kennung XXX-R0, keine Zeile.
Die Quelltexte hängen nur von Bank, Mappe, Schaltern und Kennung ab.

Liest bank/<eintrag>/*.jsonl, mappen/<eintrag>.md (Abschnitt 1),
mappen/_bausteine.md und aus werkzeuge/bank-pruef.py die Liste
STANDARD. Schreibt je Einheit e<n>_a.tex (Aufgaben) und e<n>_l.tex
(Lösungen), für die Zone blatt0_a/_l, die Rahmendateien, eine Kopie
von mathblatt.sty und zusammenbau.log. Anleitung:
werkzeuge/zusammenbau.md.
"""

import argparse
import csv
import datetime
import importlib.util
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from bisect import bisect_right
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
VERSION = "v1.0"

# Befehle der Rahmendateien, die weder in STANDARD (bank-pruef.py) noch
# in _bausteine.md stehen; jede Argumentzahl zulässig.
RAHMEN = {"documentclass", "usepackage", "input", "clearpage", "setcounter",
          "hfill", "bigskip", "medskip", "smallskip", "def", "ifdefined",
          "fi", "mitzone", "linewidth"}
# minipage: Zettel (v0.5), Text links, Grafik rechts in einer Hauptnummer
RAHMEN_UMGEBUNG = {"document", "minipage"}
# Kompetenzblatt (v0.7): Befehle und Umgebungen aus dem Vorspann (vorspann.tex)
KB_BEFEHLE = {"kbnummer", "kbhalb", "kbpaar", "kbteilpaar", "kbkopfzeile", "kbtitel", "kbspalte", "bfseries", "boldmath", "kbfeld", "kbfeldk", "item", "kbabschnitt", "kbanweisung", "kbteil",
              "kbfrage", "kbantwort", "kbzweispaltig", "kbdarunter", "kbkreuz",
              "kbraum", "kbwertetabelle", "kbmerk", "kbloesung", "par",
              "noindent", "textbf", "vspace", "hspace"}
RAHMEN |= KB_BEFEHLE
RAHMEN_UMGEBUNG |= {"kbaufgabe", "kbblock"}
# Lernblatt (v0.9): Befehle aus VORSPANN_LERN
RAHMEN |= {"lbfeld", "lbhaengst", "lbpaar"}
# Lernblatt v1.0: VORSPANN_LERN10
RAHMEN |= {"lbgym", "lbantwortrechts"}
RAHMEN_UMGEBUNG |= {"lbdaskannich"}

PFLICHT_NAME = {"fehler": "Fehler finden", "begruenden": "Begründen",
                "darstellung": "Darstellungswechsel",
                "anwendung": "Anwendung"}
EINHEIT_WORT = {"%", "€", "kg", "g", "mg", "t", "m", "cm", "mm", "km", "dm",
                "l", "ml", "h", "min", "s", "m²", "cm²", "m³", "cm³",
                "Kästchen", "Kinder", "Stück", "Jahre", "Tage", "Grad", "°"}
KENNUNG = re.compile(r"\s*\((?:P10|FHR|Abitur) [^()]*\)")
GRAFIK = re.compile(r"\\(streifen\w*|sachtabelle|bruchrechteck|bruchkreis|"
                    r"zahlenstrahl|kreisdiagramm\w*|kreisleer|kreissektor|"
                    r"saeulen\w*|balkenab|liniendia|baum\w+|wertetabelle\w*|"
                    r"vierfeldertafel|histogramm|strichliste)\b|"
                    r"\\begin\{(ksys3?|dreisatz|kreis|zahlengerade|boxplots)\}")


# --- Kennung und Register --------------------------------------------------

REGISTER = WURZEL / "bau" / "register.csv"
REGISTER_KOPF = ["kennung", "datum", "eintraege", "rezept", "bestellung",
                 "bank_commit", "zusammenbau", "vorlage", "pfad"]
REZEPT = {"L": "Lernblatt", "F": "Fokus", "S": "schwach", "H": "Heft",
          "Z": "Zettel", "P": "Prüfungs-Fokus", "K": "Kompetenzblatt"}
KENNUNG_MUSTER = re.compile(r"^([A-Z]{3})-([LFSHZPK])(\d+)$")


def finde_kuerzelliste(angabe):
    kandidaten = []
    if angabe:
        kandidaten.append(Path(angabe))
    if os.environ.get("MATHE_NACHHILFE"):
        kandidaten.append(Path(os.environ["MATHE_NACHHILFE"]) / "katalog"
                          / "_kuerzel.csv")
    kandidaten += [WURZEL.parent / "mathe-nachhilfe" / "katalog" / "_kuerzel.csv",
                   WURZEL.parent / "hz-0801" / "mathe-nachhilfe" / "katalog"
                   / "_kuerzel.csv"]
    for k in kandidaten:
        if k.is_file():
            return k
    return None


def kuerzel_von(eintrag, liste):
    """(Kürzel, Quelle): aus katalog/_kuerzel.csv (Spalten kuerzel;eintrag),
    sonst die ersten drei Buchstaben des Eintrags groß."""
    if liste:
        with open(liste, encoding="utf-8", newline="") as f:
            zeilen = [z for z in f if z.strip() and not z.startswith("#")]
        for z in csv.DictReader(zeilen, delimiter=";"):
            if (z.get("eintrag") or "").strip() == eintrag:
                k = (z.get("kuerzel") or "").strip()
                if re.fullmatch(r"[A-Z]{3}", k):
                    return k, f"{liste.name} ({liste.parent.parent.name})"
        grund = f"{eintrag} fehlt in {liste}"
    else:
        grund = "katalog/_kuerzel.csv nicht gefunden"
    buchst = re.sub(r"[^a-z]", "", eintrag.lower())[:3].upper()
    return buchst, f"Ersatz: erste drei Buchstaben ({grund})"


def lies_register():
    if not REGISTER.exists():
        return []
    with open(REGISTER, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def naechste_nummer(kuerzel, rezept, register):
    hoechste = 0
    for z in register:
        m = KENNUNG_MUSTER.match(z.get("kennung", ""))
        if m and m.group(1) == kuerzel and m.group(2) == rezept:
            hoechste = max(hoechste, int(m.group(3)))
    return hoechste + 1


def haenge_an_register(zeile):
    neu = not REGISTER.exists()
    REGISTER.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTER, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=REGISTER_KOPF, delimiter=";",
                           lineterminator="\n")
        if neu:
            w.writeheader()
        w.writerow(zeile)


def bank_commit():
    """Kurzhash von HEAD; „+geändert“, wenn bank/, mappen/ oder
    werkzeuge/ im Arbeitsbaum vom Commit abweichen."""
    try:
        h = subprocess.run(["git", "-C", str(WURZEL), "rev-parse", "--short",
                            "HEAD"], capture_output=True, text=True,
                           check=True).stdout.strip()
        st = subprocess.run(["git", "-C", str(WURZEL), "status", "--porcelain",
                             "--", "bank", "mappen", "werkzeuge"],
                            capture_output=True, text=True).stdout.strip()
        return h + ("+geändert" if st else "")
    except (OSError, subprocess.CalledProcessError):
        return "?"


def heute():
    """Datum wie `date +%F` (Uhr des Rechners)."""
    try:
        return subprocess.run(["date", "+%F"], capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return datetime.date.today().isoformat()


# --- Hilfen --------------------------------------------------------------

def lade_bankpruef():
    pfad = WURZEL / "werkzeuge" / "bank-pruef.py"
    spec = importlib.util.spec_from_file_location("bank_pruef", pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


BP = lade_bankpruef()


class Log:
    def __init__(self):
        self.zeilen = []

    def __call__(self, text):
        self.zeilen.append(text)


def lies_jsonl(pfad):
    aus = []
    with open(pfad, encoding="utf-8") as f:
        for zeile in f:
            if zeile.strip():
                aus.append(json.loads(zeile))
    return aus


def pct(text):
    """Nacktes % im Text zu \\%."""
    return re.sub(r"(?<!\\)%", r"\\%", text)


def _mathe_wort(m):
    w = re.sub(r"([_^])\(([^()]*)\)", r"\1{(\2)}", m.group(0))
    return f"${w}$"


def klar(text):
    """Klartext (Kettenname, Mappe, Antwortgerüst) für LaTeX: % zu \\%,
    Wörter mit _ oder ^ außerhalb $…$ in Mathe, ^(…) zu ^{(…)}."""
    teile = re.split(r"((?<!\\)\$[^$]*(?<!\\)\$)", text)
    for i in range(0, len(teile), 2):
        teile[i] = re.sub(r"[^\s$]*(?<!\\)[_^][^\s$]*", _mathe_wort, teile[i])
    return pct("".join(teile))


# --- Merkkasten als Mathe (v0.8, Befund 40 und 52) --------------------------

KM_FUNK = ("sin", "cos", "tan", "ln")
KM_HOCH = dict(zip("⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿˣᵗ", "0123456789-nxt"))
KM_TIEF = dict(zip("₀₁₂₃₄₅₆₇₈₉", "0123456789"))
KM_OP = {"=": "=", "+": "+", "−": "-", "-": "-", "·": r"\cdot", "±": r"\pm",
         "→": r"\rightarrow", "≈": r"\approx", "<": "<", ">": ">",
         "≤": r"\le", "≥": r"\ge", "|": r"\,|\,", "≠": r"\ne",
         "≙": r"\widehat{=}"}
KM_GRIECH = {"α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta"}
KM_WORT = re.compile(r"[A-Za-zÄÖÜäöüß]{2,}")
KM_FUNK_RE = re.compile(r"(sin|cos|tan|ln)(?![A-Za-zäöüß])")
KM_EINHEIT = {"m", "l", "g", "h", "s"}
KM_BRUCHWORT = re.compile(r"[\w()−\-,~ÄÖÜäöüß]+/[\w()−\-,~ÄÖÜäöüß]+")
KM_ZEICHEN = set("0123456789,.()/:%°√") | set(KM_OP) | set(KM_HOCH) \
    | set(KM_TIEF) | set(KM_GRIECH)


def km_token_mathe(t):
    """Ist ein Wort des Merkkastens Mathe? Zahlen, einzelne Buchstaben
    (Variablen, auch f(x), P(3), x₁), Operatoren, sin/cos/tan, Wort/Wort."""
    if KM_BRUCHWORT.fullmatch(t):
        return True
    if KM_WORT.search(KM_FUNK_RE.sub("", t)):
        return False
    return all(c in KM_ZEICHEN or c.isalpha() for c in t) and \
        any(c not in "()" for c in t)


class _KmLeser:
    """Kleiner Leser für eine Formelstrecke: Atome (Zahl, Variable, Klammer,
    Wurzel, Funktion) mit Hoch-/Tiefzahlen; a/b und a : b werden \\frac."""

    def __init__(self, s):
        self.s, self.i = s, 0

    def spitze(self):
        while self.i < len(self.s) and self.s[self.i] == " ":
            self.i += 1
        return self.s[self.i] if self.i < len(self.s) else ""

    def ausdruck(self, ende=""):
        teile = []          # Liste von (art, latex); art: "a" Atom, "o" Operator
        while True:
            c = self.spitze()
            if not c or c in ende:
                break
            if c in "/:" and teile and teile[-1][0] == "a":
                self.i += 1
                if self.spitze() in ("", ")") or self.spitze() in KM_OP:
                    teile.append(("o", ":" if c == ":" else "/"))
                    continue
                nenner = self.atom()
                zaehler = teile.pop()[1]
                teile.append(("a", r"\frac{" + ohne_klammer(zaehler) + "}{"
                              + ohne_klammer(nenner) + "}"))
            elif c in KM_OP or c in "/:":
                self.i += 1
                teile.append(("o", KM_OP.get(c, c)))
            else:
                a = self.atom()
                if a is None:
                    self.i += 1
                    teile.append(("o", c))
                else:
                    teile.append(("a", a))
        return " ".join(t for _, t in teile)

    def nachsatz(self, a):
        """Hoch-, Tiefzahlen, Grad und Prozent an ein Atom hängen."""
        while self.i < len(self.s):
            c = self.s[self.i]
            if c in KM_HOCH:
                j = self.i
                while j < len(self.s) and self.s[j] in KM_HOCH:
                    j += 1
                a += "^{" + "".join(KM_HOCH[x] for x in self.s[self.i:j]) + "}"
                self.i = j
            elif c in KM_TIEF:
                j = self.i
                while j < len(self.s) and (self.s[j] in KM_TIEF or (
                        self.s[j] == "," and j + 1 < len(self.s)
                        and self.s[j + 1] in KM_TIEF)):
                    j += 1
                a += "_{" + "".join(KM_TIEF.get(x, x) for x in
                                    self.s[self.i:j]) + "}"
                self.i = j
            elif c == "°":
                a += r"^{\circ}"
                self.i += 1
            elif c == "%":
                a += r"\,\%"
                self.i += 1
            elif c == "‹":
                j = self.s.index("›", self.i)
                e = self.s[self.i + 1:j]
                a += r"\,\text{" + e.rstrip("²³") + "}" + "".join(
                    "^{" + KM_HOCH[x] + "}" for x in e if x in "²³")
                self.i = j + 1
            elif c == " " and self.s[self.i:].lstrip()[:1] in ("%", "‹"):
                self.spitze()
            else:
                break
        return a

    def atom(self):
        c = self.spitze()
        s = self.s
        m = re.match(r"\d+(?:,\d+)?", s[self.i:])
        if m:
            self.i += m.end()
            return self.nachsatz(m.group(0).replace(",", "{,}"))
        m = KM_FUNK_RE.match(s, self.i)
        if m:
            self.i = m.end()
            kopf = self.nachsatz(r"\mathrm{" + m.group(1) + "}")
            arg = self.atom() if self.spitze() not in ("", "=") else ""
            return kopf + (r"\," + arg if arg else "")
        m = re.match(r"[A-Za-zÄÖÜäöüß~]{2,}", s[self.i:])
        if m:
            self.i += m.end()
            w = m.group(0)
            if re.fullmatch(r"[a-z]{2}", w):        # „px“: zwei Variablen
                return self.nachsatz(w)
            return self.nachsatz(r"\text{" + w + "}")
        if c == "(":
            self.i += 1
            innen = self.ausdruck(")")
            if self.spitze() == ")":
                self.i += 1
            return self.nachsatz("(" + innen + ")")
        if c == "√":
            self.i += 1
            return self.nachsatz(r"\sqrt{" + ohne_klammer(self.atom() or "")
                                 + "}")
        if c in KM_GRIECH:
            self.i += 1
            return self.nachsatz(KM_GRIECH[c])
        if c.isalpha():
            self.i += 1
            return self.nachsatz(c)
        return None


def ohne_klammer(t):
    """Äußere Klammer weg, wenn sie den ganzen Ausdruck umschließt."""
    if t.startswith("(") and t.endswith(")"):
        tiefe = 0
        for i, c in enumerate(t):
            tiefe += c == "("
            tiefe -= c == ")"
            if tiefe == 0 and i < len(t) - 1:
                return t
        return t[1:-1].strip()
    return t


def km_strecke(worte):
    """Formelstrecke (Liste von Wörtern) → (vor, $…$, nach): Klammern am
    Rand ohne Partner bleiben Text."""
    s = " ".join(worte)
    vor = nach = ""
    while s.startswith("(") and s.count("(") > s.count(")"):
        vor, s = vor + "(", s[1:]
    while s.endswith(")") and s.count(")") > s.count("("):
        nach, s = ")" + nach, s[:-1]
    if not s:
        return vor + nach
    return vor + "$" + _KmLeser(s).ausdruck() + "$" + nach


def kasten_mathe(zeile):
    """Eine Merkkastenzeile der Mappe (Klartext) in LaTeX: Formeln in $…$,
    Bruch und Division als \\frac, Wurzel als \\sqrt; drei Leerzeichen
    trennen Beispiele (\\quad)."""
    aus = []
    for stueck in re.split(r"\s{3,}", zeile.replace("&", "und").strip()):
        # Division mit Wörtern als Bruch (Befund 52): „(neu − alt) : alt“,
        # „Ganzes : 100“, „Höhe : waagerechte Strecke“
        stueck = re.sub(r"\(([A-Za-zÄÖÜäöüß]+) [−-] ([A-Za-zÄÖÜäöüß]+)\) : "
                        r"([A-Za-zÄÖÜäöüß]+)", r"(\1−\2)/\3", stueck)
        stueck = re.sub(
            r"(?<![\w)|])([A-Za-zÄÖÜäöüß]+|\d+(?:,\d+)?) : "
            r"([a-zäöüß]+ [A-ZÄÖÜ][a-zäöüß]+|[A-Za-zÄÖÜäöüß]+|\d+(?:,\d+)?)"
            r"(?![\w(])",
            lambda m: m.group(1) + "/" + m.group(2).replace(" ", "~"), stueck)
        worte, strecke = [], []
        for w in stueck.split(" "):
            kern, satz = w, ""
            m = re.match(r"^(.*?)([.,;:!?“”„]+)$", w)
            if m and m.group(1):      # Satzzeichen am Wortende bleibt Text
                kern, satz = m.group(1), m.group(2)
            if kern.rstrip("²³") in KM_EINHEIT and strecke and \
                    re.fullmatch(r"[−-]?\d+(?:,\d+)?", strecke[-1]):
                kern = "‹" + kern + "›"          # Einheit nach einer Zahl
            elif kern and km_token_mathe(kern) and strecke and \
                    re.fullmatch(r"\d+(?:,\d+)?", kern) and \
                    re.fullmatch(r"[A-Za-zα-ω]", strecke[-1]):
                worte.append(km_strecke(strecke))   # „α 7 cm“: zwei Strecken
                strecke = []
            if kern and (kern.startswith("‹") or km_token_mathe(kern)
                         or re.fullmatch(r"[a-z]{2}", kern) and strecke
                         and strecke[-1] in KM_OP):
                strecke.append(kern)
                if satz:
                    worte.append(km_strecke(strecke) + satz)
                    strecke = []
                continue
            if strecke:
                worte.append(km_strecke(strecke))
                strecke = []
            worte.append(klar(w))
        if strecke:
            worte.append(km_strecke(strecke))
        aus.append(" ".join(worte))
    return r" \quad ".join(aus)


# --- Mappe---------------------------------------------------------------

def typen_teilen(text):
    """Typen einer Zeile „Typen je Lerneinheit“: an „ · “ außerhalb von
    Klammern geteilt (v1.0; „Term mal Term (x · x = x²) [GYM 8]“ bleibt
    ganz)."""
    teile, akt, tiefe = [], "", 0
    i = 0
    text = text.strip().rstrip(".")
    while i < len(text):
        c = text[i]
        tiefe += c in "(["
        tiefe -= c in ")]"
        if tiefe == 0 and text.startswith(" · ", i):
            teile.append(akt.strip())
            akt, i = "", i + 3
            continue
        akt += c
        i += 1
    teile.append(akt.strip())
    return [x for x in teile if x]


class Mappe:
    """Abschnitt 1 der Mappe: Thema, Lerneinheiten mit Marken,
    Voraussetzungen, Merkkästen. Was nicht passt, bleibt None."""

    def __init__(self, pfad, log):
        self.thema = None
        self.einheiten = {}      # n -> {"titel", "marken"}
        self.fertigkeiten = []   # (text vor „ – “, Einheitenangabe, {n})
        self.kasten = {}         # n -> [Zeilen]
        self.sprossen = {}       # Kette (casefold) -> n, aus „Sprossen je Verfahrenstyp“ (v0.7)
        self.grundfall_zahl = {}  # Kette (casefold) -> „(4×)“ am Grundfall (v0.9)
        self.typen = {}          # n -> Text der Zeile „Typen je Lerneinheit“ (v0.7)
        self.fertigkeit_zeilen = []  # ganze Voraussetzungszeilen (v0.7)
        self.blattfolge = []     # Einheiten in der Folge des Lernblatts (v1.0)
        self.gym_typen = {}      # n -> [Typen nur für das Gymnasium] (v1.0)
        if not pfad.exists():
            log(f"MAPPE fehlt: {pfad.name} – Köpfe, Marken, Kästen als TODO")
            return
        text = pfad.read_text(encoding="utf-8")
        teil = text.split("## 1 Katalogeintrag", 1)[-1].split("\n## 2 ", 1)[0]
        zeilen = []
        for z in teil.splitlines():
            m = re.match(r"^\s*(\d+)(?:  (.*))?$", z)
            if m:
                zeilen.append(m.group(2) or "")
        abschnitt, block = None, {}
        for z in zeilen:
            if z.startswith("# ") and self.thema is None:
                self.thema = z[2:].strip()
            elif z.startswith("### "):
                abschnitt = z[4:].strip()
                block[abschnitt] = []
            elif abschnitt:
                block[abschnitt].append(z)
        self._einheiten(block.get("Lerneinheiten", []))
        self._voraussetzungen(block.get("Voraussetzungen (Blatt 0)", []))
        self._kasten(block.get("Merkkasten", []))
        for z in block.get("Für schwache Schüler", []):
            m = re.match(r"^- (.+?) \(Einheit (\d+)", z)
            if m:
                self.sprossen.setdefault(m.group(1).strip().casefold(),
                                         int(m.group(2)))
                # erste Zahl „(n×“ der Zeile = Grundfall-Aufgaben auf dem Blatt
                # (bank.md „Mengen je Kette“); Vorstufen tragen keine
                g = re.search(r"\((\d+)\s*×", z.split("):", 1)[-1])
                if g:
                    self.grundfall_zahl.setdefault(
                        m.group(1).strip().casefold(), int(g.group(1)))
        for z in block.get("Typen je Lerneinheit", []):
            m = re.match(r"^Einheit (\d+): (.+)$", z)
            if m:
                self.typen[int(m.group(1))] = m.group(2)
                # v1.0: Typen mit Klammer nur für das Gymnasium („[GYM 8]“
                # ohne OS-Angabe)
                for typ in typen_teilen(m.group(2)):
                    k = re.search(r"\[([^\]]*)\]\s*$", typ.strip())
                    if k and "GYM" in k.group(1) and "OS" not in k.group(1):
                        self.gym_typen.setdefault(int(m.group(1)), []).append(
                            typ[:k.start()].strip())

    def _einheiten(self, zeilen):
        aktuell = None
        for z in zeilen:
            m = (re.match(r"^(\d+)\. (.+?) – (.*)$", z)
                 or re.match(r"^(\d+)\. ([^:(]+?)()(?:[:(].*)?$", z))
            if m:
                aktuell = int(m.group(1))
                self.einheiten[aktuell] = {"titel": m.group(2).strip(),
                                           "marken": None,
                                           "beschreibung": m.group(3).strip()}
                continue
            m = re.match(r"^\s+Marken: (.+)$", z)
            if m and aktuell:
                self.einheiten[aktuell]["marken"] = m.group(1).strip()
                continue
            # v1.0: „Blattfolge: 2, 3, 4, 1“ (katalog/_vorlage.md, optional)
            m = re.match(r"^Blattfolge:\s*(.+)$", z)
            if m:
                self.blattfolge = [int(x) for x in re.findall(r"\d+",
                                                               m.group(1))]

    def _voraussetzungen(self, zeilen):
        self.fertigkeit_zeilen = []
        for z in zeilen:
            if z.startswith("Erkennungsschritte"):
                break
            if z.startswith("- "):
                self.fertigkeit_zeilen.append(z[2:].strip())
            m = re.match(r"^- (.+?) – (.+)$", z)
            if not m:
                continue
            angabe = m.group(2).split(". ", 1)[0].rstrip(".")
            nummern = set()
            for a, b in re.findall(r"(\d+)(?: bis (\d+))?", angabe):
                if b:
                    nummern |= set(range(int(a), int(b) + 1))
                else:
                    nummern.add(int(a))
            if not angabe.startswith("Einheit"):
                nummern = set()
            self.fertigkeiten.append((m.group(1).strip(), angabe, nummern))

    def _kasten(self, zeilen):
        aktuell = None
        for z in zeilen:
            m = re.match(r"^Einheit (\d+) \(.*\):$", z)
            if m:
                aktuell = int(m.group(1))
                self.kasten[aktuell] = []
                continue
            if not z.strip() or z.startswith("Quelle"):
                if not z.strip():
                    aktuell = None
                continue
            if aktuell is None or not z.startswith("    "):
                continue
            inhalt = z.strip()
            if inhalt.startswith(("Formelsammlung", "Auswendig")):
                continue
            self.kasten[aktuell].append(inhalt)

    def fertigkeit(self, kette):
        """Voraussetzungszeile zur Zone-Kette (Anfang wortgleich)."""
        for text, angabe, nummern in self.fertigkeiten:
            if text == kette or text.startswith(kette):
                return angabe, nummern
        return None, None


# --- Marken und Zweigzeile ------------------------------------------------

def marke_zerlegen(marken):
    """(os, gym, pruefwort) aus der Marken-Zeile; os/gym als (von, bis)."""
    if not marken:
        return None, None, None
    teile = [t.strip() for t in marken.split(" · ")]
    os_, gym, wort = None, None, None
    for t in teile:
        m = re.match(r"^OS Kl\. (\d+)(?:–(\d+))?", t)
        if m and os_ is None:
            os_ = (int(m.group(1)), int(m.group(2) or m.group(1)))
            continue
        m = re.match(r"^GYM Kl\. (\d+)(?:–(\d+))?", t)
        if m and gym is None:
            gym = (int(m.group(1)), int(m.group(2) or m.group(1)))
            continue
        if re.match(r"^(P10|keine|Abitur|FHR)", t) and wort is None:
            wort = t
    return os_, gym, wort


def zeitmarke(os_, gym, klasse):
    """Zeitmarke nach unterrichtsblatt 1.5; None, wenn nicht ableitbar."""
    if os_ is None:
        return None
    von, bis = os_
    if klasse is None:
        text = f"ab Kl. {von}"
        if bis != von:
            text += f", je nach Buch bis Kl. {bis}"
        if gym and gym[0] != von:
            text += f" (am Gymnasium ab Kl. {gym[0]})"
        return text
    if von < klasse <= bis:
        text = "neu oder schon bekannt – je nach Buch"
    elif von == klasse < bis:
        text = f"neu in diesem Jahr, je nach Buch bis Klasse {bis}"
    elif von < klasse:
        text = f"kennst du wahrscheinlich seit Klasse {von}"
    elif von == klasse:
        text = "neu in diesem Jahr"
    elif von == klasse + 1:
        text = "kommt nächstes Jahr"
    else:
        text = f"kommt in Klasse {von}"
    if gym and gym[0] != von:
        g = gym[0]
        if g < klasse:
            text += f" (am Gymnasium schon seit Klasse {g})"
        elif g == klasse:
            text += " (am Gymnasium in diesem Jahr)"
        else:
            text += f" (am Gymnasium in Klasse {g})"
    return text


PROFIL_WORT = {"msa": "P10", "abitur-gk": "Abi GK", "abitur-lk": "Abi LK",
               "fhr": "FHR"}


def profil_papier(papier, datei=""):
    """Prüfungsprofil aus dem Papier eines Originals oder einer
    Katalogzeile (wie profil_von)."""
    if papier in MSA_PAPIER or datei.startswith("msa/"):
        return "msa"
    if papier in ("A", "B", "C") or datei.startswith("fhr/"):
        return "fhr"
    if re.search(r"-(ga|gk)(-|$)", papier or ""):
        return "abitur-gk"
    return "abitur-lk"


def pruefwort_zahl(marken, zeilen, log=None):
    """Prüfungswort der Zweigzeile mit Zahl der Jahrgänge (v0.5, Beschluss
    des Lehrers vom 28.09.): „P10 ×5“ = der Typ kam in fünf Jahrgängen
    vor. Je Prüfungsmarke der Marken-Zeile (P10, Abitur GK/LK, FHR) die
    Typen der Originale dieser Einheit (Bankzeilen, Profil wie im Heft),
    dazu aus den Prüfungskatalogen die verschiedenen Jahre, in denen einer
    dieser Typen im Profil vorkommt. Ohne Katalog: die Jahre der Originale
    selbst; ohne Original die Marke ohne Zahl („P10“). „keine …“ bleibt
    wörtlich. None, wenn die Marken-Zeile keine Prüfungsmarke trägt."""
    if not marken:
        return None
    kat = kataloge_still()
    aus = []
    for t in [t.strip() for t in marken.split(" · ")]:
        if t.startswith("keine"):
            aus.append(t)
            continue
        if re.match(r"^P10\b", t):
            profil = "msa"
        elif t.startswith("Abitur GK"):
            profil = "abitur-gk"
        elif t.startswith("Abitur LK"):
            profil = "abitur-lk"
        elif re.match(r"^FHR\b", t):
            profil = "fhr"
        else:
            continue
        origs = {}
        for z in zeilen:
            o = z.get("original") or {}
            if o.get("id") and profil_papier(o.get("papier")) == profil:
                origs[o["id"]] = o.get("jahr")
        typen = {kat[i]["typ"] for i in origs if kat.get(i, {}).get("typ")}
        if typen:
            jahre = {k["jahr"] for k in kat.values() if k.get("typ") in typen
                     and profil_papier(k.get("papier"), k.get("datei", ""))
                     == profil and k.get("jahr")}
            quelle = f"Kataloge, {len(typen)} Typen"
        else:
            jahre = {j for j in origs.values() if j}
            quelle = "Jahre der Originale"
        wort = PROFIL_WORT[profil]
        aus.append(f"{wort} ×{len(jahre)}" if jahre else wort)
        if log:
            log(f"PRÜFWORT „{t}“ → „{aus[-1]}“ ({quelle}; "
                f"{len(origs)} Originale)")
    return " · ".join(aus) if aus else None


# --- Auswahl -------------------------------------------------------------

def kettenart(zeilen):
    hoehen = {z["hoehe"] for z in zeilen}
    if hoehen == {"pflicht"}:
        return "pflicht"
    if "grundfall" in hoehen:
        return "verfahren"
    if hoehen == {"vorstufe"}:
        return "erkennung"
    return "ohne"


RANG = {"erkennung": 0, "verfahren": 1, "ohne": 2, "pflicht": 3}


def ketten_von(zeilen):
    """[(kette_nr, name, art, [zeilen])] in der Folge des Auftrags."""
    gruppen = {}
    for z in zeilen:
        gruppen.setdefault(z["kette_nr"], []).append(z)
    aus = []
    for nr, zz in gruppen.items():
        aus.append((nr, zz[0]["kette"], kettenart(zz), zz))
    aus.sort(key=lambda k: (RANG[k[2]], k[0]))
    return aus


def je_sprosse_erste(zeilen, log, wo):
    """Je Sprosse die Zeile mit der kleinsten Variante."""
    sprossen = {}
    for z in zeilen:
        sprossen.setdefault(z["sprosse"], []).append(z)
    aus = []
    for s in sorted(sprossen):
        zz = sorted(sprossen[s], key=lambda z: z["variante"])
        wahl = zz[0]
        rest = ", ".join(f"v{z['variante']}" for z in zz[1:])
        grund = ("Variante 1" if wahl["variante"] == 1 else
                 f"kleinste Variante (v{wahl['variante']}; v1 fehlt)")
        log(f"AUSWAHL {wahl['id']} – {wo}, Sprosse {s}: {grund}"
            + (f"; übergangen {rest}" if rest else ""))
        aus.append(wahl)
    return aus


# --- Satz einer Teilaufgabe ------------------------------------------------

def antwortfeld(antwort):
    """Antwortgerüst („__ %“, „__ von __“) als \\leerfeld-Folge."""
    if not antwort:
        return ""
    stuecke = antwort.split("__")
    aus = [klar(stuecke[0].strip())]
    for rest in stuecke[1:]:
        m = re.match(r"^ (\S+)(.*)$", rest)
        if m and m.group(1).rstrip(",;") in EINHEIT_WORT:
            einheit = m.group(1).rstrip(",;")
            aus.append(f"\\leerfeld[{pct(einheit)}]")
            rest = m.group(1)[len(einheit):] + m.group(2)
        else:
            aus.append("\\leerfeld")
        rest = rest.strip()
        if rest:
            rest = re.sub(r"(?<![$\\])([<>])", r"$\1$", rest)
            aus.append(klar(rest))
    return " ".join(a for a in aus if a)


PAPIER_KURZ = {"OS": "", "FOR": "F", "EBR": "E", "GYM": "G"}
_KATALOG = None


def kataloge_still():
    """Prüfungskataloge (lies_kataloge) einmal je Lauf, ohne Log."""
    global _KATALOG
    if _KATALOG is None:
        _KATALOG = lies_kataloge(lambda *_: None)
    return _KATALOG


def kurzkennung(k, z=None):
    """Prüfkennung in Kurzform (Beschluss des Lehrers vom 28.09., v0.5):
    „(P10 2024 OS)“ → „(P24)“, Papier nur, wenn nicht OS („(P26F)“,
    „(P25E)“, „(P22G)“); „(Abitur 2023 GK)“ → „(A23)“, LK → „(A23L)“;
    „(FHR 2025)“ → „(F25)“. Sternchen wie im Original dahinter („(P26F*)“),
    wenn das Original der Zeile (gleiches Jahr) im Prüfungskatalog stern = ja
    trägt. Andere Formen bleiben, wie sie sind."""
    innen = k.strip()[1:-1].strip()
    m = re.fullmatch(r"P10 (\d{4}) (OS|FOR|EBR|GYM)", innen)
    if m:
        jahr, kurz = m.group(1), f"P{m.group(1)[2:]}{PAPIER_KURZ[m.group(2)]}"
    else:
        m = re.fullmatch(r"Abitur (\d{4}) (GK|LK)", innen)
        if m:
            jahr = m.group(1)
            kurz = f"A{jahr[2:]}" + ("L" if m.group(2) == "LK" else "")
        else:
            m = re.fullmatch(r"FHR (\d{4})", innen)
            if not m:
                return k.strip()
            jahr, kurz = m.group(1), f"F{m.group(1)[2:]}"
    o = (z or {}).get("original") or {}
    if o.get("id") and str(o.get("jahr")) == jahr:
        if kataloge_still().get(o["id"], {}).get("stern") == "ja":
            kurz += "*"
    return f"({kurz})"


def mit_kennung(aufgabe, hat_feld, z=None):
    """Prüfkennung wie im Muster 2026-09-22: „\\hfill (P24)“, seit v0.5 in
    Kurzform (kurzkennung)."""
    m = KENNUNG.search(aufgabe)
    if not m:
        return aufgabe, False
    vor, nach = aufgabe[:m.start()], aufgabe[m.end():]
    neu = vor + " \\hfill " + kurzkennung(m.group(0), z) + nach
    am_ende = not nach.strip()
    if am_ende and hat_feld:
        neu += " \\\\"
    return neu, True


def feld_im_grafik(z):
    g = z.get("grafik", "")
    return "\\streifenfeld" in g or "\\dsleer" in g


def teil_normal(z, stern=False):
    """Zeilen für eine Teilaufgabe im teile-Block (stern: \\steil)."""
    feld = "" if feld_im_grafik(z) else antwortfeld(z.get("antwort", ""))
    aufgabe, _ = mit_kennung(z["aufgabe"], bool(feld), z)
    grafik = z.get("grafik", "")
    t = "\\steil" if stern else "\\teil"
    if not grafik:
        return [f"{t} {aufgabe}" + (f" {feld}" if feld else "")]
    zeilen = [f"{t} {aufgabe}", "", grafik]
    if feld:
        zeilen.append(feld)
    return zeilen


def gl_inhalt(aufgabe):
    t = aufgabe.strip()
    if t.startswith("$") and t.endswith("$") and t.count("$") == 2:
        return t[1:-1]
    return "\\text{" + t + "}"


def teile_normal(folge, stern=frozenset()):
    """Teilaufgaben in teile- und gleichungsraster-Blöcken; ids in stern
    bekommen \\steil bzw. \\sgl (Heft: Sternchen wie im Original)."""
    aus, block = [], None
    for z in folge:
        art = "raster" if z["form"] == "gleichungsraster" else "teile"
        if art != block:
            if block == "teile":
                aus.append("\\end{teile}")
            elif block == "raster":
                aus.append("\\end{gleichungsraster}")
            aus.append("\\begin{teile}" if art == "teile"
                       else "\\begin{gleichungsraster}[2]")
            block, spalte = art, 0
        if art == "teile":
            aus += teil_normal(z, z.get("id") in stern)
        else:
            trenner = " &" if spalte == 0 else " \\\\"
            g = "\\sgl" if z.get("id") in stern else "\\gl"
            aus.append(f"{g}{{{gl_inhalt(z['aufgabe'])}}}" + trenner)
            spalte = 1 - spalte
    if block == "raster" and aus[-1].endswith(" &"):
        aus[-1] = aus[-1][:-2] + " & \\\\"
    if block == "teile":
        aus.append("\\end{teile}")
    elif block == "raster":
        aus.append("\\end{gleichungsraster}")
    return aus


def teil_schwach(z, log, nr):
    """Eine Teilaufgabe in Form schwach (2.8): (Zeilen, Art, TODO?)."""
    feld = antwortfeld(z.get("antwort", ""))
    grafik = z.get("grafik", "")
    form, hoehe = z["form"], z["hoehe"]
    pflicht = z.get("pflicht")
    if form == "streifenfeld" and "\\streifenfeld" in grafik:
        grafik = grafik.replace("\\streifenfeld", "\\streifen", 1)
        log(f"SCHWACH {z['id']} (Nr. {nr}): \\streifenfeld → \\streifen, "
            f"Feld in den Text (rechte Spalte zu schmal für Streifen + Feld)")
    elif "\\streifenfeld" in grafik or "\\dsleer" in grafik:
        feld = ""
    aufgabe, _ = mit_kennung(z["aufgabe"], False, z)
    text = aufgabe + (f" {feld}" if feld and form != "dreisatz" else "")
    if pflicht == "begruenden":
        return [f"\\swfrage{{{aufgabe}}}"], "frage"
    if form in ("streifenfeld", "streifenleer", "zeichnen", "tabelle") and grafik:
        return [f"\\swa{{{text}}}{{{grafik}}}"], "swa"
    if form == "ankreuzen" or (hoehe == "vorstufe" and not grafik):
        return ["\\begin{teile}", f"\\teil {text}", "\\end{teile}"], "teil"
    zeilen = 3 if (pflicht in ("fehler", "anwendung") or hoehe == "pruefung"
                   or form == "text") else 2
    opt = "" if zeilen == 2 else f"[{zeilen}]"
    rechnung = aufgabe if form != "gleichungsraster" else f"${gl_inhalt(aufgabe)}$"
    aus = []
    if not grafik and hoehe != "pruefung" and pflicht is None:
        aus.append("%% TODO Darstellung für schwach fehlt in der Bank "
                   f"({z['id']}; Abschnitt „Für schwache Schüler“)")
    aus.append(f"\\swz{opt}{{{rechnung}}}{{{grafik}}}")
    return aus, "swz"


# --- Satz einer Teilaufgabe im Stil des Kompetenzblatts ------------------

class KbSatz:
    """Satz einer Teilaufgabe im Stil des Kompetenzblatts (v0.7/v0.8), gemeinsam
    für Rezept K und seit v0.9 für das Lernblatt (Rezept L, F): braucht
    self.log."""

    def satz_teil(self, z, buchst, anweisung):
        """LaTeX-Zeilen einer Teilaufgabe (Inhalt eines kbblock); die
        Anweisung der Hauptnummer steht über der ersten Teilaufgabe."""
        wo = z["id"]
        t = zerlege(z)
        grafik = z.get("grafik", "") or ""
        if z["form"] == "zeichnen" and grafik:
            grafik = ksys_verkleinern(grafik, self.log, wo)
        tabellen = [tabelle_text(x) for x in t["tabellen"]]
        feld = [] if feld_im_grafik(z) else antwort_zeilen(z.get("antwort", ""))
        n_raum = rechenzeilen(z)
        if z["form"] == "gleichungsraster" and not feld:
            feld = [antwortfeld("Lösung: __").replace("\\leerfeld", "\\kbfeld")]
            self.log(f"ANTWORT {wo}: Bank ohne Antwortgerüst – „Lösung: __“")
        kopf = t["kopf"]
        frage = list(t["frage"])
        fett = t["fett"]
        sf = satzform(z)
        if sf:
            # v0.8: ganze Sätze als ein Absatz; eine Anweisung aus
            # ich-kann.csv entfällt, wenn der Text selbst auffordert
            kopf, fett, frage, t["vor"] = sf["kopf"], sf["fett"], [], sf["vor"]
            if anweisung and (sf["auffordernd"] or sf["vor"]):
                self.log(f"ANWEISUNG {wo}: „{anweisung}“ entfällt – die "
                         "Aufgabe fordert selbst auf (Sprachregeln)")
                anweisung = ""
        if z["form"] == "gleichungsraster":
            a = z["aufgabe"].strip()
            if "$" not in a:
                kopf, fett, frage = f"${a}$", True, []
        if not kopf and frage and len(schlicht(frage[0])) <= 70 \
                and len(frage) > 1:
            kopf, frage = frage[0], frage[1:]
        if anweisung and len(frage) == 1 and frage[0].endswith("?") \
                and len(schlicht(frage[0]).split()) <= 3:
            self.log(f"FRAGE {wo}: Kurzfrage „{frage[0]}“ entfällt – die "
                     f"Anweisung „{anweisung}“ sagt es (Befund 5)")
            frage = []
        if not kopf and len(frage) == 1 and not t["kennung"]:
            kopf, frage = frage[0], []
        kopf_satz = (f"{{\\bfseries\\boldmath {kopf}}}" if fett and kopf
                     else kopf)
        if not anweisung and t["vor"]:
            anweisung = t["vor"]
        if (not feld and not t["kreuze"] and not t["tabellen"] and not grafik
                and z["form"] in ("teil", "text") and n_raum == 0
                and not z.get("pflicht") and "\\janein" not in z["aufgabe"]):
            feld = ["\\kbfeld"]
            self.log(f"ANTWORT {wo}: Bank ohne Antwortgerüst – leeres Feld")
        anw = f"\\kbanweisung{{{klar(anweisung)}}}" if anweisung else ""
        kopfzeile = f"\\kbteil{{{buchst}}}{{{kopf_satz}}}{{{t['kennung']}}}"
        frage_satz = ("\\kbfrage{" + " \\\\ ".join(frage) + "}") if frage else ""
        kreuze = []
        for k in t["kreuze"]:
            m = re.match(r"\\kreuz\{(.*)\}$", k, re.S)
            kreuze.append(f"\\kbkreuz{{{m.group(1) if m else k}}}")
        antw = "".join(f"\\kbantwort{{{f}}}" for f in feld)
        raum = f"\\kbraum{{{n_raum}}}" if n_raum else ""
        bilder = tabellen + ([grafik] if grafik else [])
        halb = TEXTBREITE_CM * 0.5
        aus = [x for x in (anw, kopfzeile, frage_satz) if x]
        lern = getattr(self, "lern_grafik", False)
        if bilder:
            masse = [(grafik_mass_lern if lern else grafik_mass)(
                b if not b.startswith("\\kbwertetabelle")
                else "\\wertetabelle" + b[len("\\kbwertetabelle"):])
                for b in bilder]
            rechts = "".join(kreuze) + antw + raum
            if lern and len(bilder) == 1 and rechts and \
                    masse[0][0] <= TEXTBREITE_CM - 4.5:
                # Lernblatt v1.0 (Befund 13 des Lehrers, 27): Grafik links,
                # Antwort rechts daneben, nie als lose Linie darunter
                anteil = min(0.72, max(0.3, masse[0][0] / TEXTBREITE_CM + 0.04))
                tief = max(0.0, masse[0][1] / 2 - 0.4) if not raum and \
                    not kreuze else 0.0
                rechts = rechts.replace(
                    "\\kbantwort{", f"\\lbantwortrechts[{tief:.1f}cm]{{"
                    if tief else "\\lbantwortrechts{")
                aus.append(f"\\kbzweispaltig[{anteil:.2f}]{{{bilder[0]}}}"
                           f"{{{rechts}}}")
                self.log(f"GRAFIK {wo}: Grafik links ({masse[0][0]:.1f} cm), "
                         "Antwort rechts")
            elif len(bilder) == 2 and sum(m[0] for m in masse) <= TEXTBREITE_CM - 0.5:
                # Tabelle und Koordinatensystem nebeneinander (Befund 27)
                anteil = min(0.6, max(0.3, masse[0][0] / TEXTBREITE_CM + 0.02))
                aus.append(f"\\kbzweispaltig[{anteil:.2f}]{{{bilder[0]}}}"
                           f"{{{bilder[1]}}}")
                if rechts:
                    aus.append(rechts)
            elif len(bilder) == 1 and masse[0][0] <= halb and rechts:
                anteil = min(0.58, max(0.3, masse[0][0] / TEXTBREITE_CM + 0.07))
                aus.append(f"\\kbzweispaltig[{anteil:.2f}]{{{bilder[0]}}}"
                           f"{{{rechts}}}")
            elif (len(bilder) == 1 and masse[0][0] <= halb and not rechts
                  and z["form"] == "zeichnen" and frage):
                # Zeichnen: Koordinatensystem links, Auftrag rechts daneben
                aus = [x for x in (anw, kopfzeile) if x]
                anteil = min(0.55, max(0.3, masse[0][0] / TEXTBREITE_CM + 0.03))
                aus.append(f"\\kbzweispaltig[{anteil:.2f}]{{{bilder[0]}}}"
                           "{" + " \\\\ ".join(frage) + "}")
            else:
                for b in bilder:
                    aus.append(f"\\kbdarunter{{{b}}}")
                if rechts:
                    aus.append(rechts)
        elif kreuze:
            aus += kreuze
            if antw:
                aus.append(antw)
        elif raum and not antw:
            aus.append(f"\\item[]{raum}")
        elif raum:
            # Rechenraum rechts neben der Aufgabe (Befund 9, 27)
            grenze = 32 if fett else 52
            if not t["kennung"] and len(schlicht(kopf)) <= grenze and \
                    len(schlicht(" ".join(frage))) <= 70:
                links = "".join(x for x in (anw, kopfzeile, frage_satz) if x)
                aus = [f"\\kbzweispaltig[0.46]{{\\kbspalte{{{links}{antw}}}}}"
                       f"{{{raum}}}"]
            else:
                aus.append(f"\\kbzweispaltig[0.46]{{{antw}}}{{{raum}}}")
        else:
            if antw:
                aus.append(antw)
        return aus

    def halb_tauglich(self, z):
        """Zeichenaufgabe, deren Koordinatensystem in eine halbe Spalte passt
        (Paarsatz: zwei nebeneinander, Befund 27 „Platz nutzen“)."""
        g = z.get("grafik") or ""
        if z["form"] != "zeichnen" or "\\begin{ksys}" not in g:
            return False
        g = ksys_verkleinern(g, lambda *_: None, "")
        return grafik_mass(g)[0] <= TEXTBREITE_CM * 0.485 - 0.7

    def satz_halb_text(self, z, anweisung):
        """Rechenaufgabe in einer halben Spalte: Text, Antwort, Raum darunter."""
        t = zerlege(z)
        kopf, frage = t["kopf"], list(t["frage"])
        sf = satzform(z)
        if sf:
            kopf, frage, t["fett"], t["vor"] = sf["kopf"], [], sf["fett"], \
                sf["vor"]
            if sf["auffordernd"] or sf["vor"]:
                anweisung = ""
        if not kopf and len(frage) > 1:
            kopf, frage = frage[0], frage[1:]
        if not anweisung and t["vor"]:
            anweisung = t["vor"]
        kopf_satz = (f"{{\\bfseries\\boldmath {kopf}}}" if t["fett"] and kopf
                     else kopf)
        n = rechenzeilen(z)
        feld = antwort_zeilen(z.get("antwort", "")) or ([] if n else
                                                        ["\\kbfeld"])
        aus = []
        if anweisung:
            aus.append(f"\\kbanweisung{{{klar(anweisung)}}}")
        aus.append(f"\\kbteil{{}}{{{kopf_satz}}}{{}}")
        if frage:
            aus.append("\\kbfrage{" + " \\\\ ".join(frage) + "}")
        aus += [f"\\kbantwort{{{f}}}" for f in feld]
        if n:
            aus.append(f"\\item[]\\kbraum{{{n}}}")
        return aus

    def satz_halb(self, z, buchst, anweisung):
        """Zeichenaufgabe in einer halben Spalte: Text oben, Grafik darunter."""
        t = zerlege(z)
        g = ksys_verkleinern(z.get("grafik") or "", self.log, z["id"])
        kopf, frage = t["kopf"], list(t["frage"])
        sf = satzform(z)
        if sf:
            kopf, frage, t["fett"] = sf["kopf"], [], sf["fett"]
            if sf["auffordernd"]:
                anweisung = ""
            if sf["vor"]:
                anweisung = sf["vor"]
        if not kopf and len(frage) > 1:
            kopf, frage = frage[0], frage[1:]
        kopf_satz = (f"{{\\bfseries\\boldmath {kopf}}}" if t["fett"] and kopf
                     else kopf)
        aus = []
        if anweisung:
            aus.append(f"\\kbanweisung{{{klar(anweisung)}}}")
        aus.append(f"\\kbteil{{{buchst}}}{{{kopf_satz}}}{{{t['kennung']}}}")
        if frage:
            aus.append("\\kbfrage{" + " \\\\ ".join(frage) + "}")
        aus.append(f"\\kbdarunter{{{g}}}")
        return aus



# --- Bau -----------------------------------------------------------------

class Hauptnummer:
    def __init__(self, titel, folge, art, kette, einheit, weiter=False):
        self.titel = titel
        self.folge = folge
        self.art = art
        self.kette = kette
        self.einheit = einheit
        self.weiter = weiter
        self.nr = None
        self.buchstaben = []   # (Buchstabe, Zeile oder None für Erklärzeile)
        # Lernblatt v0.9
        self.lage = art        # zone, zonepaar, erkennung, vorstufe, leiter, pruefung, ohne, pflicht
        self.anweisung = ""    # Spalte anweisung aus ich-kann.csv
        self.laeufe = []       # [(Auftrag oder "", [Zeilen], [Rest oder None])]
        self.verweis = None    # Zone: Nummer der ersten Hauptnummer, die die Fertigkeit braucht
        self.erster = None     # „– weiter“: Hauptnummer, deren Fortsetzung sie ist
        self.ziel = None       # Prüfe dich: Nummer der Kette im Blatt (Lösung)


def platzhalter_titel(kette, art, folge):
    if art == "pflicht":
        namen = []
        for z in folge:
            n = PFLICHT_NAME.get(z.get("pflicht"), z.get("pflicht"))
            if n not in namen:
                namen.append(n)
        return f"{kette} – " + ", ".join(namen)
    return kette


def teile_nach_mass(folge):
    """Teilung nach 2.3 g an Sprossengrenzen: höchstens 12 Teilaufgaben
    ohne Grafik, 6 mit Grafik je Hauptnummer."""
    gruppen = []
    for z in folge:
        if gruppen and gruppen[-1][0]["sprosse"] == z["sprosse"]:
            gruppen[-1].append(z)
        else:
            gruppen.append([z])
    teile, akt = [], []
    for g in gruppen:
        neu = akt + g
        grenze = 6 if any(z.get("grafik") for z in neu) else 12
        if akt and len(neu) > grenze:
            teile.append(akt)
            akt = list(g)
        else:
            akt = neu
    if akt:
        teile.append(akt)
    return teile


def buchstabe(i):
    return "abcdefghijklmnopqrstuvwxyz"[i] if i < 26 else f"?{i + 1}"


# --- Lernblatt v0.9: Auftrag über der Nummer, Terme nebeneinander ----------

# Verben, mit denen ein Auftrag beginnt, der nicht in IMPERATIV steht
LB_VERB = re.compile(r"^(Klammere|Fasse|Multipliziere|Vereinfache|Unterstreiche|"
                     r"Kreise|Addiere|Subtrahiere|Dividiere|Wandle|Schreibe|"
                     r"Setze|Löse|Rechne|Berechne|Bestimme|Gib)\b")
# Aufträge, hinter deren Term „= ____“ steht (Rechnen, Umformen)
LB_RECHNEN = re.compile(r"^(Fasse|Multipliziere|Berechne|Rechne|Löse die Klammer|"
                        r"Klammere|Vereinfache|Addiere|Subtrahiere|Dividiere)\b")
# Aufträge ohne Antwortfeld (die Antwort steht im Term selbst)
LB_OHNE_FELD = re.compile(r"\b(Unterstreiche|Kreise|Markiere|Zeichne|Fülle|"
                          r"Verbinde)\b")
LB_KURZ = 30            # Term bis etwa 30 Zeichen: zwei nebeneinander
LB_TEIL_MAX = 12        # 2.3 g: höchstens 12 Teilaufgaben je Hauptnummer,
LB_TEIL_MAX_GRAFIK = 6  # mit Grafik 6
LB_GRUNDFALL = 4        # bank.md „Mengen je Kette“: vier von fünf auf dem Blatt
PFLICHT_FOLGE = ["fehler", "begruenden", "darstellung", "anwendung"]
PFLICHT_ICHKANN = {"fehler": "Ich finde den Fehler und rechne richtig.",
                   "begruenden": "Ich kann begründen.",
                   "darstellung": "Ich kann zwischen Term, Bild und Worten "
                                  "wechseln.",
                   "anwendung": "Ich kann damit Aufgaben aus dem Alltag lösen."}
# Trennbare Vorsilben für den zu-Infinitiv der Zweigzeile („aufzulösen“)
TRENNBAR = ("zusammen", "heraus", "herunter", "dar", "auf", "aus", "ab", "an",
            "ein", "mit", "vor", "nach", "um", "her", "hin", "weg", "fest",
            "zu", "los", "durch")
VORSPANN_LERN = r"""% Lernblatt (zusammenbau v0.9): Antwortfeld hinter kurzen Termen,
% Verweis der Zone auf die Nummer im Lernblatt
\newcommand{\lbfeld}{\mbox{\underline{\hspace{2.6cm}}}}
% „Das kann ich“ unter „Prüfe dich“ (wie abhakseite, ohne neue Seite)
\newenvironment{lbdaskannich}{\par\addvspace{14pt}\Needspace*{8\baselineskip}%
  \einheitenkopf[abhaken][Das kann ich]{Das kann ich}%
  \begingroup\small\setlength{\parskip}{1pt}\setlength{\parindent}{0pt}}%
  {\par\endgroup}
\newcommand{\lbhaengst}[1]{\par\vspace{3pt}{\footnotesize\color{mbgrau}Hängst du hier $\rightarrow$ Nr.~#1}\par}
% Zwei Teilaufgaben nebeneinander; Buchstaben in derselben Flucht wie
% untereinander (links hängend)
\newlength{\lbhalbbreite}
\newcommand{\lbpaar}[2]{\item[]\hspace*{-\leftmargin}%
  \setlength{\lbhalbbreite}{\dimexpr0.5\linewidth+0.5\leftmargin-0.6em\relax}%
  \begin{minipage}[t]{\lbhalbbreite}\kbhalb{#1}\end{minipage}\hfill
  \begin{minipage}[t]{\lbhalbbreite}\kbhalb{#2}\end{minipage}\par}"""


def auftrag_zerlegen(z):
    """Auftrag einer Teilaufgabe und der Term dahinter (v0.9): „Verb …: Term“
    → („Verb ….“, Term, "doppelpunkt"); „Satzanfang Term.“ → („Satzanfang.“,
    Term, "satz"); „Satzanfang Term Satzrest“ → („Satzanfang … Satzrest“,
    Term, "luecke"). None, wenn die Aufgabe eine Prüfkennung, einen Befehl,
    mehrere Sätze vor dem Term oder mehr als drei Wörter zwischen den Termen
    trägt."""
    t = z["aufgabe"].strip()
    if KENNUNG.search(t) or "\\\\" in t:
        return None
    s, st = schuetze(t)
    phs = list(re.finditer(r"\x00(\d+)\x01", s))
    if not phs or any(not st[int(m.group(1))].startswith("$") for m in phs):
        return None
    vor, nach = s[:phs[0].start()], s[phs[-1].end():]
    mitte = s[phs[0].start():phs[-1].end()]
    zwischen = re.sub(r"\x00\d+\x01", " ", mitte)
    if re.search(r"[.?!:]", zwischen) or len(re.sub(r"[,;]", " ", zwischen)
                                                  .split()) > 3:
        return None
    p, n = vor.strip(), nach.strip()
    if n in ("", ".") and re.fullmatch(r"[^.?!:]+\.", p) and \
            (IMPERATIV.match(p) or LB_VERB.match(p)):
        return p, zurueck(mitte, st), "doppelpunkt"     # „Berechne. Term“
    if not p or re.search(r"[.?!]", p) or not (IMPERATIV.match(p)
                                                 or LB_VERB.match(p)):
        return None
    term = zurueck(mitte, st)
    if n in ("", ".") and p.endswith(":"):
        return p[:-1].rstrip() + ".", term, "doppelpunkt"
    if p.endswith(":"):
        return None
    if n in ("", "."):
        return p + ".", term, "satz"
    if re.search(r"\x00", n):
        return None
    rest = zurueck(n, st)
    if rest.startswith(". "):       # Term am Satzende, dann ein zweiter Satz:
        return p + rest, term, "luecke"   # „Löse die Gleichung. Gib … an.“
    return (p + " …" + rest if re.match(r"^[?.,!]", rest)
            else p + " … " + rest), term, "luecke"


def schluss_auftrag(z):
    """Gleicher Auftragssatz am Ende (v0.9): „Das Vierfache … vermindert.
    Kreuze den Term an, der dazu passt. \\\\ \\kreuz{…}“ → („Kreuze den Term
    an, der dazu passt.“, Rest ohne den Satz, "schluss"). Nur, wenn vor dem
    Satz noch ein Satz steht; eine Prüfkennung bleibt am Rest."""
    t = z["aufgabe"].strip()
    kennung = ""
    m = KENNUNG.search(t)
    if m:        # Prüfkennung bleibt am Rest (klein rechts in der Auftaktzeile)
        kennung, t = m.group(0).strip(), (t[:m.start()] + t[m.end():]).strip()
    kopf, schwanz = t, ""
    m = re.search(r"\s*\\\\", t)
    if m:
        kopf, schwanz = t[:m.start()], t[m.start():]
    s, st = schuetze(kopf)
    teile = saetze(s)
    if len(teile) < 2:
        return None
    letzt = teile[-1]
    if not (IMPERATIV.match(letzt) or LB_VERB.match(letzt)) or \
            not re.search(r"[.!]$", letzt) or letzt.startswith(("Wie", "Was",
                                                                 "Welche")):
        return None
    rest = zurueck(" ".join(teile[:-1]), st) + (" " + kennung if kennung
                                                  else "") + schwanz
    return zurueck(letzt, st), rest, "schluss"


def zerlege_auftrag(z):
    return auftrag_zerlegen(z) or schluss_auftrag(z)


def geruest_von(z):
    """(Gerüst, [Mathe-Stücke]) einer Aufgabe ohne Prüfkennung und ohne
    Befehle: jedes $…$ als \\x00#\\x01; None sonst."""
    t = z["aufgabe"].strip()
    if KENNUNG.search(t) or "\\\\" in t or z.get("grafik"):
        return None
    s, st = schuetze(t)
    if any(not x.startswith("$") for x in st):
        return None
    return re.sub(r"\x00\d+\x01", "\x00#\x01", s), st


def vorlage_mehrfach(zeilen):
    """Gleiche Aufgabe mit anderen Zahlen an höchstens zwei Stellen (v0.9):
    („Erfinde … zu der der Term … passt. … für … und erkläre …“,
    ["$15 + 3x$, $x = 2$", …]) oder None."""
    g = [geruest_von(z) for z in zeilen]
    if any(x is None for x in g) or len({x[0] for x in g}) != 1:
        return None
    n = len(g[0][1])
    anders = [k for k in range(n) if len({x[1][k] for x in g}) > 1]
    if not 1 <= len(anders) <= 2:
        return None
    stuecke = g[0][0].split("\x00#\x01")
    auftrag = stuecke[0]
    for k in range(n):
        auftrag += ("…" if k in anders else g[0][1][k]) + stuecke[k + 1]
    if not (IMPERATIV.match(auftrag) or LB_VERB.match(auftrag)
            or re.search(r"[.?!] (Berechne|Schreibe|Gib|Bestimme)", auftrag)):
        return None
    return auftrag.strip(), [", ".join(x[1][k] for k in anders) for x in g]


def laeufe_von(folge):
    """Folge in Läufe mit gleichem Auftrag: [(Auftrag, [Zeilen], [Terme])];
    ohne gemeinsamen Auftrag je Zeile ein Lauf ("", [z], [None]). Ein
    einzelner „Verb …: Term“ gilt als Lauf, Satzanfang und Lücke erst ab zwei
    Teilaufgaben."""
    zer = [zerlege_auftrag(z) for z in folge]
    aus, i = [], 0
    while i < len(folge):
        a = zer[i]
        j = i + 1
        if a:
            while j < len(folge) and zer[j] and zer[j][0] == a[0]:
                j += 1
        if a and (j - i >= 2 or a[2] == "doppelpunkt"):
            aus.append((a[0], folge[i:j], [zer[k][1] for k in range(i, j)]))
            i = j
            continue
        # gleiche Aufgabe mit anderen Zahlen (zwei Stellen): längste Folge ab i
        m = len(folge)
        while m - i >= 2 and not vorlage_mehrfach(folge[i:m]):
            m -= 1
        if m - i >= 2:
            auftrag, terme = vorlage_mehrfach(folge[i:m])
            aus.append((auftrag, folge[i:m], terme))
            i = m
            continue
        aus.append(("", [folge[i]], [None]))
        i += 1
    return aus


def teile_ausgewogen(folge):
    """2.3 g: höchstens 12 Teilaufgaben je Hauptnummer, 6 mit Grafik; Teilung
    an Sprossengrenzen in möglichst gleich große Stücke (13 → 7 + 6, nicht
    12 + 1)."""
    def grenze(t):
        return LB_TEIL_MAX_GRAFIK if any(z.get("grafik") for z in t) \
            else LB_TEIL_MAX
    if len(folge) <= grenze(folge):
        return [folge]
    gruppen = []
    for z in folge:
        if gruppen and gruppen[-1][0]["sprosse"] == z["sprosse"]:
            gruppen[-1].append(z)
        else:
            gruppen.append([z])
    k = -(-len(folge) // grenze(folge))
    while True:
        ziel = -(-len(folge) // k)
        teile, akt = [], []
        for g in gruppen:
            if akt and len(akt) + len(g) > ziel:
                teile.append(akt)
                akt = []
            akt = akt + g
        teile.append(akt)
        if all(len(t) <= grenze(t) for t in teile) or k >= len(gruppen):
            return teile
        k += 1


def teile_nach_auftrag(folge):
    """Stücke an einem Auftrag, der im Stück schon einmal stand (kein
    Auftrag zweimal in einer Nummer); zählt auch den Auftrag einer einzelnen
    Teilaufgabe mit ganzem Text (Prüfung AUFTRAG, v0.9)."""
    stuecke, akt, gesehen = [], [], set()
    for auftrag, zz, _ in laeufe_von(folge):
        if not auftrag and len(zz) == 1:
            a = zerlege_auftrag(zz[0])
            auftrag = a[0] if a else ""
        if auftrag and auftrag in gesehen:
            stuecke.append(akt)
            akt, gesehen = [], set()
        akt += zz
        if auftrag:
            gesehen.add(auftrag)
    if akt:
        stuecke.append(akt)
    return stuecke


def zerteile(folge):
    """Hauptnummer in Stücke: erst nach 2.3 g (höchstens 12 Teilaufgaben, 6
    mit Grafik, ausgewogen), dann in jedem Stück an einem Auftrag, der darin
    schon stand – so trennt die Teilung nach Maß zwei gleiche Aufträge oft
    schon, und es entsteht kein Stück aus einer Teilaufgabe (v0.9, zweiter
    Durchgang; bis dahin Auftrag zuerst)."""
    aus = []
    for s in teile_ausgewogen(folge):
        aus += teile_nach_auftrag(s)
    return aus


def zu_infinitiv(titel):
    """„Terme aufstellen und berechnen“ → „Terme aufzustellen und zu
    berechnen“; „Ausklammern“ → „auszuklammern“. None ohne Verb."""
    w = titel.split()
    verben = [i for i, x in enumerate(w)
              if re.fullmatch(r"[a-zäöüß]+(en|ern|eln)", x) and i > 0]
    if not verben and len(w) == 1 and re.fullmatch(
            r"[A-ZÄÖÜ][a-zäöüß]+(en|ern|eln)", w[0]) and (
            w[0].lower().startswith(TRENNBAR) or w[0].endswith("ieren")) \
            and not re.search(r"(ung|heit|keit|schaft|gab)en$", w[0]):
        # nur substantivierte Verben („Ausklammern“, „Faktorisieren“), nicht
        # Mehrzahlen wie „Sachaufgaben“
        w[0], verben = w[0].lower(), [0]
    if not verben:
        return None
    for i in verben:
        v = w[i]
        for p in TRENNBAR:
            if v.startswith(p) and len(v) > len(p) + 3:
                w[i] = p + "zu" + v[len(p):]
                break
        else:
            w[i] = "zu " + v
    return " ".join(w)


BESCHREIBUNG_META = re.compile(r"→|\.md|Kl\.|LISUM|RLP|Zeile|Fachbrief|"
                               r"amtlich|Reihe|Katalog|\[")


def ohne_bankwort(text):
    """Glieder einer Aufzählung (Komma, Semikolon auf oberster Ebene), die
    ein Bank-Wort tragen, fallen weg („… als Grundfall“)."""
    teile, akt, tiefe = [], "", 0
    for c in text:
        tiefe += c in "([" 
        tiefe -= c in ")]"
        if c in ",;" and tiefe == 0:
            teile.append(akt)
            akt = ""
            continue
        akt += c
    teile.append(akt)
    rest = [t.strip() for t in teile if t.strip() and not BANKWORT.search(t)]
    return ", ".join(rest)


def beschreibung_katalog(info):
    """Beschreibung der Lerneinheit wie im Katalog (Text nach „ – “), ohne
    Eingabe-Marke („← Eingabe …“), ohne Klammern mit Hinweisen für den
    Lehrer (Verweise auf andere Einträge, Klassen, LISUM, RLP, Zeilen), ohne
    Glieder mit Bank-Wort und ohne Schlusspunkt."""
    b = (info.get("beschreibung") or "").split(" ← ", 1)[0].strip()
    alt = None
    while alt != b:
        alt = b
        b = re.sub(r"\s*\([^()]*\)", lambda m: "" if BESCHREIBUNG_META.search(
            m.group(0)) else m.group(0).replace("(", "\x02").replace(
            ")", "\x03"), b)
    b = b.replace("\x02", "(").replace("\x03", ")")
    if BANKWORT.search(b):
        b = ohne_bankwort(b)
    return b.strip().rstrip(".").strip()


def hier_lernst_du(info):
    """Teil 1 der Zweigzeile (v0.9, zweiter Durchgang): „Hier lernst du,
    <Titel als zu-Infinitiv> – <Beschreibung wie im Katalog>“. Ist die
    Beschreibung schon ein Satz („Hier lernst du …“), steht sie allein."""
    if not info:
        return None, "keine Lerneinheit in der Mappe"
    b = beschreibung_katalog(info)
    if re.match(r"^(Hier lernst du|Du lernst)\b", b):
        return b, "Beschreibung der Lerneinheit"
    inf = zu_infinitiv(info["titel"])
    if inf and b:
        return f"Hier lernst du, {inf} – {b}", "Titel und Beschreibung der " \
            "Lerneinheit"
    if inf:
        return f"Hier lernst du, {inf}", "aus dem Titel (keine Beschreibung)"
    if b:
        return f"Hier lernst du: {b}", "Beschreibung (Titel ohne Verb)"
    return None, "Titel ohne Verb, keine Beschreibung"


def fertigkeit_name(zeile):
    """Kurzname einer Voraussetzungszeile: Text vor „ (“ und „ – “."""
    return re.split(r" \(| – ", zeile, 1)[0].strip()


# --- Lernblatt v1.0 (Befunde des Lehrers am TER-L4, 01.10.) ----------------

LB_TEIL_GRENZE = 26     # Teilung erst über 26 Teilaufgaben (Befund 9)
LB_KREUZ_PAAR = 120     # Ankreuzen nebeneinander bis 120 Zeichen Quelltext
LB_SACH_WOERTER = 12    # Sachkontext: mehr als zwölf Wörter vor dem Auftrag
LB_HALB_ZEILE = 45      # ganze Aufgabe in einer Zeile der halben Spalte
# feste Ersatzsätze des Skripts (PFLICHT_ICHKANN, Zone-Paar) im Infinitiv
ERSATZ_INFINITIV = {
    "Ich finde den Fehler und rechne richtig.":
        "Den Fehler finden und richtig rechnen",
    "Ich kann das auch in Aufgaben aus der Prüfung.":
        "Das auch in Aufgaben aus der Prüfung können"}
TEST_TITEL = "Kannst du das schon?"
VERSTANDEN_TITEL = "Verstanden?"
VORSPANN_LERN10 = r"""% Lernblatt v1.0 (Befund 6 und 13 des Lehrers vom 01.10.): Striche für den
% Rechenweg so stark wie die Antwortlinie, halbe Breite, eine Zeile Luft
% zwischen Aufgabentext und erstem Strich bzw. Antwortfeld
\newlength{\lbstrichbreite}
\renewcommand{\kbraum}[1]{\par\setlength{\lbstrichbreite}{0.5\textwidth}%
  \ifdim\lbstrichbreite>\linewidth\setlength{\lbstrichbreite}{\linewidth}\fi
  \vspace{\baselineskip}\setcounter{mbsz}{0}%
  \loop\ifnum\value{mbsz}<#1\relax
    \nointerlineskip\vskip\mbschreibhoehe
    \hbox{\hskip\@totalleftmargin\underline{\hspace{\lbstrichbreite}}}%
    \stepcounter{mbsz}\repeat
  \nointerlineskip\hbox{\vrule\@width\z@\@height\z@\@depth\mbschreibtiefe}\prevdepth\z@}
\renewcommand{\kbantwort}[1]{\par\vspace{\baselineskip}\noindent#1\par}
% Antwort rechts neben der Grafik, etwa auf halber Höhe der Grafik
\newcommand{\lbantwortrechts}[2][0pt]{\par\vspace*{#1}\noindent#2\par}
% Kennzeichen „GYM“ rechts im Titel der Hauptnummer (wie die Prüfkennung)
\newcommand{\lbgym}{\hfill{\footnotesize GYM}}"""


def text_vor_auftrag(z):
    """Sätze vor dem ersten Auftrag (Imperativ, Verb des Lernblatts oder
    Frage), Mathe und Befehle als je ein Wort; Prüfkennung und alles nach
    dem ersten Zeilenumbruch \\\\ (Ankreuzoptionen) bleiben außen vor."""
    t = KENNUNG.sub("", z.get("aufgabe") or "").split("\\\\")[0]
    s, _ = schuetze(t)
    vor = []
    for satz in saetze(s):
        if IMPERATIV.match(satz) or LB_VERB.match(satz) or \
                satz.rstrip().endswith("?"):
            break
        vor.append(re.sub(r"\x00\d+\x01", " X ", satz))
    return " ".join(vor)


def kontext_woerter(z):
    return len(re.findall(r"[^\s,;:.!?–-]+", text_vor_auftrag(z)))


def hat_sachkontext(z):
    """Heuristik des Auftrags (Punkt 10, 12): mehr als zwölf Wörter vor dem
    Auftrag (Mathe als ein Wort)."""
    return kontext_woerter(z) > LB_SACH_WOERTER


def ist_textaufgabe(z):
    """Textaufgabe für die Folge der Ketten (Punkt 1): form text oder ein
    Satz vor dem Auftrag („Das Vierfache einer Zahl x …“)."""
    return z.get("form") == "text" or kontext_woerter(z) > 0


def nackt(term):
    """Term ohne Wörter außerhalb der Mathe („$4x$, $7$“ ja, „$4x - 3$ für
    $x = 5$“ nein)."""
    return term is not None and not re.search(
        r"[A-Za-zÄÖÜäöüß]", re.sub(r"\$[^$]*\$", "", term))


def zahlrechnung(term):
    """Reine Zahlrechnung: in der Mathe kein Buchstabe (Befehle wie \\cdot,
    \\frac ausgenommen)."""
    if not nackt(term):
        return False
    mathe = " ".join(re.findall(r"\$([^$]*)\$", term))
    mathe = re.sub(r"\\[A-Za-z]+", "", mathe)
    return bool(mathe.strip()) and not re.search(r"[A-Za-z]", mathe)


def infinitiv_titel(satz):
    """„Ich kann einen Term aufstellen.“ → „Einen Term aufstellen“; „Ich
    kann: <merkmal>.“ → „<Merkmal>“; None, wenn der Satz nicht mit „Ich
    kann“ beginnt (dann Spalte titel in ich-kann.csv)."""
    s = (satz or "").strip()
    for vor in ("Ich kann: ", "Ich kann "):
        if s.startswith(vor):
            r = s[len(vor):].strip().rstrip(".").strip()
            return r[:1].upper() + r[1:] if r else None
    return None


def nummern_bereich(nrn):
    """[6, 7, 8, 11] → „6–8, 11“."""
    nrn = sorted(set(nrn))
    teile, i = [], 0
    while i < len(nrn):
        j = i
        while j + 1 < len(nrn) and nrn[j + 1] == nrn[j] + 1:
            j += 1
        teile.append(str(nrn[i]) if i == j else f"{nrn[i]}–{nrn[j]}")
        i = j + 1
    return ", ".join(teile)


class Bau(KbSatz):
    """Rezept L (Lernblatt), F (Fokus), S (schwach). Seit v0.9 setzen L und F
    im Satz des Kompetenzblatts (KbSatz, vorspann.tex); S behält die Form
    2.8 (\\swz, \\swa)."""

    def __init__(self, args, log):
        self.a = args
        self.log = log
        self.eintrag = args.eintrag
        bank = WURZEL / "bank" / self.eintrag
        if not bank.is_dir():
            sys.exit(f"bank/{self.eintrag}/ fehlt")
        self.mappe = Mappe(WURZEL / "mappen" / f"{self.eintrag}.md", log)
        self.thema = self.mappe.thema or self.eintrag
        self.e = {}
        for p in sorted(bank.glob("e*.jsonl"),
                        key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
            self.e[int(p.stem[1:])] = lies_jsonl(p)
        zp = bank / "zone.jsonl"
        self.zone = lies_jsonl(zp) if zp.exists() else []
        self.fokus = args.fokus
        self.schwach = args.schwach
        self.klasse = args.klasse
        self.kennung = args.kennung
        self.ik = lies_ichkann()
        self.todo_frei = []
        self.reihenfolge = []   # (Hauptnummer, Aufgabendatei) in Blattfolge
        self.lage = {}          # id -> lage (bau.json)
        self.zeichen = []
        self.ichkann_fehlt = []
        self.lernblatt = not (self.fokus or self.schwach)   # Rezept L
        self.auftrag_doppelt = []   # Prüfung AUFTRAG (v0.9)
        self.satz_doppelt = []      # Hinweis AUFTRAG-SATZ (v0.9)
        # Lernblatt v1.0
        self.titel_csv = lies_titel()
        self.mit_sach = bool(getattr(args, "mit_sachaufgaben", False))
        self.lern_grafik = self.lernblatt   # Grafik links, Antwort rechts
        self.titel_fehlt = []       # log TITEL: kein Infinitiv ableitbar
        self.gym = []               # log GYM
        self.sach_weg = []          # log TEXT: ausgelassene Sachkontexte
        self.test_wahl = []         # log TEST

    # Titel ---------------------------------------------------------------
    def ich_kann(self, einheit, kette, sprosse, ersatz):
        """(Titel, Anweisung) aus bau/regal/ich-kann.csv; fehlt die Zeile,
        der Ersatz und ICH-KANN fehlt in der log."""
        k = (self.eintrag, einheit, kette.casefold(), sprosse)
        if k in self.ik and self.ik[k][0]:
            satz, anw = self.ik[k]
        else:
            self.log(f"ICH-KANN fehlt in bau/regal/ich-kann.csv: e{einheit} "
                     f"„{kette}“ Sprosse „{sprosse}“ – Ersatz „{ersatz}“")
            self.ichkann_fehlt.append(f"e{einheit} {kette} {sprosse}".strip())
            satz, anw = ersatz, ""
        if self.lernblatt:
            return self.titel_infinitiv(k, satz), anw
        return satz, anw

    def titel_infinitiv(self, k, satz):
        """Lernblatt v1.0 (Befund 4): Titel im Infinitiv – Spalte titel in
        ich-kann.csv, sonst „Ich kann …“ maschinell umgeformt; geht beides
        nicht, der Satz ohne Punkt und log TITEL."""
        if k in self.titel_csv:
            return self.titel_csv[k]
        if satz in ERSATZ_INFINITIV:
            return ERSATZ_INFINITIV[satz]
        inf = infinitiv_titel(satz)
        if inf:
            return inf
        if satz not in self.titel_fehlt:
            self.titel_fehlt.append(satz)
            self.log(f"TITEL „{satz}“: kein Infinitiv ableitbar, keine Spalte "
                     f"titel in ich-kann.csv (e{k[1]} „{k[2]}“ „{k[3]}“) – "
                     "Satz ohne Punkt")
        return satz.rstrip(".")

    def grundfall_zahl(self, kette):
        """Zahl der Grundfall-Aufgaben aus „(n×)“ der Sprossenzeile der Mappe
        (bank.md „Mengen je Kette“); ohne Angabe LB_GRUNDFALL."""
        k = kette.casefold()
        for name, n in self.mappe.grundfall_zahl.items():
            if name == k or name.startswith(k) or k.startswith(name):
                return n
        self.log(f"GRUNDFALL „{kette}“: keine Zahl „(n×)“ in der Mappe – "
                 f"{LB_GRUNDFALL}")
        return LB_GRUNDFALL

    @staticmethod
    def merkmal_titel(z, kette):
        """Ersatztitel „Ich kann: <merkmal>.“ ohne Bank-Wort am Anfang
        („Vorstufe: …“); trägt er dann noch eines, „Ich kann: <Kette>.“"""
        m = re.sub(r"^(Vorstufe|Grundfall|Fallstrick|Sprosse|Prüfungshöhe)"
                   r"\s*\d*\s*[:–-]\s*", "", z.get("merkmal") or kette)
        t = "Ich kann: " + re.split(r"[:;,(]", m)[0].strip() + "."
        return t if not BANKWORT.search(t) else f"Ich kann: {kette}."

    def hn(self, titel_anw, folge, art, kette, n, weiter_titel=None):
        """Hauptnummer(n) aus einer Folge: geteilt nach zerteile; Stücke nach
        dem ersten tragen den Ich-kann-Satz ihrer ersten Sprosse, wenn es ihn
        gibt, sonst „<Titel> – weiter“."""
        titel, anw = titel_anw
        aus = []
        if self.lernblatt:
            return self.hn_lern(titel, anw, folge, art, kette, n)
        stuecke = zerteile(folge) if not self.schwach else [folge]
        for i, t in enumerate(stuecke):
            if i == 0:
                h = Hauptnummer(titel, t, art, kette, n)
                h.anweisung = anw
            else:
                k = (self.eintrag, n, kette.casefold(), str(t[0]["sprosse"]))
                eigen = weiter_titel and k in self.ik and self.ik[k][0]
                h = Hauptnummer(self.ik[k][0] if eigen else f"{titel} – weiter",
                                t, art, kette, n, weiter=not eigen)
                h.erster = aus[0]
                self.log(f"TEILUNG „{titel[:50]}“: Stück {i + 1} ab "
                         f"{t[0]['id']} ({len(t)} Teilaufgaben)"
                         + (" – eigener Ich-kann-Satz der Sprosse" if eigen
                            else " – „weiter“"))
            h.lage = art
            h.laeufe = laeufe_von(t) if not self.schwach else []
            for z in t:
                if z.get("id"):
                    self.lage[z["id"]] = art
            aus.append(h)
        return aus

    def hn_lern(self, titel, anw, folge, art, kette, n):
        """Lernblatt v1.0 (Befund 9): eine Hauptnummer läuft über die Seite;
        geteilt wird nur über 26 Teilaufgaben, an einer Sprossengrenze, und
        jedes weitere Stück trägt die Fertigkeit seiner ersten Sprosse
        (ich-kann.csv, Spalte sprosse), nie „weiter“."""
        stuecke = [folge]
        if len(folge) > LB_TEIL_GRENZE:
            gruppen = []
            for z in folge:
                if gruppen and gruppen[-1][0]["sprosse"] == z["sprosse"]:
                    gruppen[-1].append(z)
                else:
                    gruppen.append([z])
            stuecke, akt = [], []
            for g in gruppen:
                if akt and len(akt) + len(g) > LB_TEIL_GRENZE:
                    stuecke.append(akt)
                    akt = []
                akt = akt + g
            stuecke.append(akt)
        aus = []
        for i, t in enumerate(stuecke):
            if i == 0:
                h = Hauptnummer(titel, t, art, kette, n)
                h.anweisung = anw
            else:
                sp = str(t[0]["sprosse"])
                ersatz = "Ich kann: " + (t[0].get("merkmal") or kette) + "."
                tt, _ = self.ich_kann(n, kette, sp, ersatz)
                h = Hauptnummer(tt, t, art, kette, n)
                h.erster = aus[0]
                self.log(f"TEILUNG „{titel[:50]}“: Stück {i + 1} ab {t[0]['id']} "
                         f"({len(t)} Teilaufgaben, über {LB_TEIL_GRENZE}) – Titel "
                         f"der Sprosse „{tt}“")
            h.lage = art
            h.laeufe = self.laeufe_lern(t)
            for z in t:
                if z.get("id"):
                    self.lage[z["id"]] = art
            aus.append(h)
        return aus

    def laeufe_lern(self, folge):
        """Lernblatt v1.0 (Befund 3): ein gemeinsamer Auftrag über der Nummer
        nur bei nackten Termen und Gleichungen („Fasse zusammen: $7x + 2x$“);
        Teilaufgaben mit Bedingung oder Kontext („… $4x - 3$ für $x = 5$“,
        Sachtext, gleicher Schlusssatz, gleiche Vorlage) tragen je den ganzen
        Satz."""
        aus = []
        for auftrag, zz, terme in laeufe_von(folge):
            if not auftrag:
                aus.append((auftrag, zz, terme))
                continue
            arten = [zerlege_auftrag(z) for z in zz]
            gut = all(a and a[2] == "doppelpunkt" and nackt(a[1])
                      for a in arten)
            if gut:
                aus.append((auftrag, zz, terme))
                continue
            for z in zz:
                aus.append(("", [z], [None]))
            self.log(f"AUFTRAG-SATZ-JE-TEIL {zz[0]['id']} …: „{auftrag}“ – "
                     f"Bedingung oder Kontext, je Teilaufgabe der ganze Satz "
                     f"({len(zz)} Teilaufgaben)")
        return aus

    def anweisung_noetig(self, h, auftrag, zeilen, terme):
        """Lernblatt v1.0 (Befund 3): Die Anweisung entfällt, wenn jede
        Teilaufgabe form teil ist und ein „=“ trägt oder eine reine
        Zahlrechnung ist, und der Titel der Hauptnummer die Handlung schon
        nennt (Verb im Infinitiv)."""
        if not auftrag or not self.lernblatt or h.lage == "test":
            return bool(auftrag)
        for z, term in zip(zeilen, terme):
            if z["form"] != "teil":
                return True
            t = term if term is not None else z["aufgabe"]
            mathe = " ".join(re.findall(r"\$([^$]*)\$", t))
            if not ("=" in mathe or zahlrechnung(t)):
                return True
        if not zu_infinitiv(h.titel) and not re.search(
                r"\b[a-zäöüß]+(en|ern|eln)\b", h.titel):
            return True
        self.log(f"ANWEISUNG-WEG Nr. {h.nr}: „{auftrag}“ – nackte Rechnung, "
                 f"der Titel „{h.titel}“ nennt die Handlung")
        return False

    # Auswahl je Einheit
    def einheiten(self):
        alle = sorted(self.e)
        if self.a.einheiten:
            wahl = [int(x) for x in self.a.einheiten.split(",") if x.strip()]
            fehlt = [n for n in wahl if n not in self.e]
            if fehlt:
                sys.exit(f"Einheit(en) {fehlt} nicht in bank/{self.eintrag}/")
            alle = [n for n in alle if n in wahl]
        if self.fokus:
            treffer = [n for n in alle if any(
                z["kette"].casefold() == self.fokus.casefold()
                for z in self.e[n])]
            if not treffer:
                namen = sorted({z["kette"] for n in alle for z in self.e[n]})
                sys.exit(f"Kette „{self.fokus}“ nicht gefunden; vorhanden: "
                         + "; ".join(namen))
            alle = treffer
        if self.lernblatt and self.mappe.blattfolge:
            # v1.0: Reihenfolge des Lernblatts aus der Zeile „Blattfolge“ der
            # Mappe; Einheiten, die sie nicht nennt, danach in Katalogfolge
            bf = [n for n in self.mappe.blattfolge if n in alle]
            alle = bf + [n for n in alle if n not in bf]
            self.log(f"BLATTFOLGE {self.mappe.blattfolge} aus der Mappe → "
                     f"Einheiten {alle}")
        elif self.lernblatt:
            self.log("BLATTFOLGE: keine Zeile in der Mappe – Katalogfolge")
        return alle

    def pflicht_hn(self, zeilen, name, n, wo, alle=True):
        aus = []
        je = {}
        for z in zeilen:
            je.setdefault(z.get("pflicht"), []).append(z)
        for p in PFLICHT_FOLGE + sorted(set(je) - set(PFLICHT_FOLGE),
                                        key=str):
            if p not in je:
                continue
            folge = sorted(je[p], key=lambda z: (z["sprosse"], z["variante"]))
            if not alle:
                folge = folge[:1]
            for z in folge:
                self.log(f"AUSWAHL {z['id']} – {wo}, Pflicht {p}: je Zeile "
                         "eine Teilaufgabe")
            tk = self.ich_kann(n, name, p or "", PFLICHT_ICHKANN.get(
                p, self.merkmal_titel(folge[0], name)))
            aus += self.hn(tk, folge, "pflicht", name, n)
        return aus

    def lern_einheit(self, n):
        """Lernblatt v1.0: Ketten ohne Textaufgabe im Grundfall zuerst, dann
        die mit (Befund 1, log FOLGE); Mengen wie v0.9, aber je Kette höchstens
        eine Teilaufgabe mit Sachkontext (Befund 12); die Pflichtelemente je
        Sorte eine Teilaufgabe in einer Nummer „Verstanden?“ am Ende
        (Befund 11). Der Test am Kopf entsteht in baue (braucht das ganze
        Blatt)."""
        log = self.log
        aus = []
        ketten = ketten_von(self.e[n])

        def grund(zeilen):
            gz = [z for z in zeilen if z["hoehe"] == "grundfall"] or \
                sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))[:1]
            return gz[0] if gz else None

        def schluessel(k):
            nr, name, art, zeilen = k
            g = grund(zeilen)
            return (art == "pflicht", bool(g and ist_textaufgabe(g)),
                    RANG[art], nr)
        ketten.sort(key=schluessel)
        log(f"FOLGE e{n}: " + " → ".join(
            f"„{name}“ ({art}{', Textaufgabe im Grundfall' if schluessel((nr, name, art, zeilen))[1] else ''})"
            for nr, name, art, zeilen in ketten if art != "pflicht"))
        pflicht = []
        for nr, name, art, zeilen in ketten:
            wo = f"e{n} k{nr} „{name}“ ({art})"
            if art == "erkennung":
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Erkennungsschritt, alle "
                        "Zeilen")
                aus += self.hn(self.ich_kann(n, name, "", self.merkmal_titel(
                    folge[0], name)), folge, "erkennung", name, n)
            elif art == "pflicht":
                pflicht.append((name, zeilen))
            elif art == "ohne":
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Typ ohne Kette, alle Zeilen")
                aus += self.hn(self.ich_kann(n, name, "", self.merkmal_titel(
                    folge[0], name)), folge, "ohne", name, n)
            else:
                aus += self.verfahren_hn(zeilen, name, n, wo)
        if pflicht:
            aus += self.verstanden_hn(pflicht, n)
        return aus

    def verstanden_hn(self, pflicht, n):
        """Befund 11: je Sorte (fehler, begründen, darstellung, anwendung)
        eine Teilaufgabe – die kleinste Sprosse und Variante über alle
        Pflichtketten der Einheit –, zusammen in „Verstanden?“, Anwendung
        zuletzt. Die übrigen Zeilen bleiben für Fokus und Wiederholung."""
        je = {}
        for name, zeilen in pflicht:
            for z in zeilen:
                je.setdefault(z.get("pflicht"), []).append(z)
        folge = []
        for s in PFLICHT_FOLGE + sorted(set(je) - set(PFLICHT_FOLGE), key=str):
            if s not in je:
                continue
            zz = sorted(je[s], key=lambda z: (z["sprosse"], z["variante"]))
            folge.append(zz[0])
            self.log(f"AUSWAHL {zz[0]['id']} – e{n} Pflicht {s}: eine "
                     f"Teilaufgabe „Verstanden?“ (übrig {len(zz) - 1})")
        if "anwendung" in je:       # Anwendung zuletzt
            folge = [z for z in folge if z.get("pflicht") != "anwendung"] + \
                [z for z in folge if z.get("pflicht") == "anwendung"]
        return self.hn((VERSTANDEN_TITEL, ""), folge, "pflicht",
                       pflicht[0][0], n)

    def hauptnummern_einheit(self, n):
        if self.lernblatt:
            return self.lern_einheit(n)
        log = self.log
        aus = []
        for nr, name, art, zeilen in ketten_von(self.e[n]):
            wo = f"e{n} k{nr} „{name}“ ({art})"
            if self.fokus:
                if name.casefold() != self.fokus.casefold():
                    log(f"WEG {wo} – Fokus: andere Kette entfällt")
                    continue
                if art == "pflicht":
                    aus += self.pflicht_hn(zeilen, name, n, wo)
                    continue
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Fokus, alle Varianten")
                tk = self.ich_kann(n, name, "", self.merkmal_titel(folge[0],
                                                                    name))
                aus += self.hn(tk, folge, "leiter", name, n, weiter_titel=True)
                continue
            if self.schwach:
                if art == "verfahren":
                    grund = [z for z in zeilen if z["hoehe"] == "grundfall"]
                    rest = [z for z in zeilen if z["hoehe"] != "grundfall"]
                    vor = [z for z in rest if z["sprosse"] < grund[0]["sprosse"]]
                    nach = [z for z in rest if z["sprosse"] > grund[0]["sprosse"]]
                    folge = je_sprosse_erste(vor, log, wo)
                    for z in sorted(grund, key=lambda z: z["variante"]):
                        log(f"AUSWAHL {z['id']} – {wo}: schwach, Grundfall als "
                            "Päckchen (alle Varianten, unterrichtsblatt 2.8)")
                    folge += sorted(grund, key=lambda z: z["variante"])
                    folge.append({"paeckchen": True})
                    folge += je_sprosse_erste(nach, log, wo)
                else:
                    folge = je_sprosse_erste(zeilen, log, wo)
                erste = next(z for z in folge if not z.get("paeckchen"))
                sp = "" if art != "pflicht" else (erste.get("pflicht") or "")
                ersatz = (PFLICHT_ICHKANN.get(sp) if art == "pflicht" else None) \
                    or self.merkmal_titel(erste, name)
                aus += self.hn(self.ich_kann(n, name, sp, ersatz), folge, art,
                               name, n)
                log(f"KETTE {wo} → eine Hauptnummer (schwach)")
                continue
            # Rezept L: Mengen nach bank.md „Mengen je Kette“
            if art == "erkennung":
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Erkennungsschritt, alle "
                        "Zeilen")
                aus += self.hn(self.ich_kann(n, name, "", self.merkmal_titel(
                    folge[0], name)), folge, "erkennung", name, n)
            elif art == "pflicht":
                aus += self.pflicht_hn(zeilen, name, n, wo)
            elif art == "ohne":
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Typ ohne Kette, alle Zeilen")
                aus += self.hn(self.ich_kann(n, name, "", self.merkmal_titel(
                    folge[0], name)), folge, "ohne", name, n)
            else:
                aus += self.verfahren_hn(zeilen, name, n, wo)
        return aus

    def verfahren_hn(self, zeilen, name, n, wo):
        log = self.log
        aus = []
        vor = {}
        for z in zeilen:
            if z["hoehe"] == "vorstufe":
                vor.setdefault(z["sprosse"], []).append(z)
        for s in sorted(vor):
            folge = sorted(vor[s], key=lambda z: z["variante"])
            for z in folge:
                log(f"AUSWAHL {z['id']} – {wo}, Vorstufe {s}: alle Zeilen")
            aus += self.hn(self.ich_kann(n, name, str(s), self.merkmal_titel(
                folge[0], name)), folge, "vorstufe", name, n)
        grund = sorted([z for z in zeilen if z["hoehe"] == "grundfall"],
                       key=lambda z: (z["sprosse"], z["variante"]))
        # bank.md: „(4×)“ am Grundfall im Katalog ist die Zahl auf dem Blatt;
        # ohne Angabe vier von fünf
        zahl = self.grundfall_zahl(name)
        for z in grund[:zahl]:
            log(f"AUSWAHL {z['id']} – {wo}: Grundfall ({zahl} von "
                f"{len(grund)})")
        for z in grund[zahl:]:
            log(f"RESERVE {z['id']} – {wo}: Grundfall über {zahl} (Päckchen "
                "wechselt)")
        weitere = je_sprosse_erste([z for z in zeilen if z["hoehe"]
                                    not in ("vorstufe", "grundfall", "pruefung",
                                            "pflicht")], log, wo)
        leiter = grund[:zahl] + weitere
        pr = [z for z in zeilen if z["hoehe"] == "pruefung"]
        # v0.9 (Auftrag 30.09., zweiter Durchgang): Regel des Kompetenzblatts –
        # je Original eine Aufgabe, jüngste fünf Jahrgänge, verschiedene
        # Formulierungen zuerst, bis fünf; ohne Original eine der drei Zeilen
        wahl = waehle_originale(pr, log, KOMPETENZ_PRUEF_MAX,
                                ohne_original_eins=True) if pr else []
        if self.lernblatt and not self.mit_sach:
            # v1.0 (Befund 12): je Kette höchstens eine Teilaufgabe mit
            # Sachkontext – die oberste Sprosse bzw. die Prüfungshöhe; der
            # Grundfall bleibt immer
            sach = [z for z in weitere + wahl if hat_sachkontext(z)]
            if len(sach) > 1:
                bleibt = max(sach, key=lambda z: (z["sprosse"],
                                                  z["hoehe"] == "pruefung"))
                weg = [z for z in sach if z is not bleibt]
                weitere = [z for z in weitere if z not in weg]
                wahl = [z for z in wahl if z not in weg]
                self.sach_weg += [z["id"] for z in weg]
                log(f"TEXT {wo}: Sachkontext bleibt {bleibt['id']}; "
                    "ausgelassen " + ", ".join(z["id"] for z in weg))
            else:
                log(f"TEXT {wo}: {len(sach)} Teilaufgabe mit Sachkontext – "
                    "nichts ausgelassen")
            gs = [z["id"] for z in grund[:zahl] if hat_sachkontext(z)]
            if gs:
                log(f"TEXT {wo}: Grundfall mit Sachkontext bleibt: "
                    + ", ".join(gs))
            leiter = grund[:zahl] + weitere
        if leiter:
            aus += self.hn(self.ich_kann(n, name, "", self.merkmal_titel(
                leiter[0], name)), leiter, "leiter", name, n,
                weiter_titel=True)
        for z in wahl:
            o = (z.get("original") or {}).get("id") or "ohne Original"
            log(f"AUSWAHL {z['id']} – {wo}: Prüfungshöhe ({o})")
        if wahl:
            aus += self.hn(self.ich_kann(n, name, "p", "Ich kann das auch in "
                                         "Aufgaben aus der Prüfung."),
                           wahl, "pruefung", name, n)
        return aus

    def hauptnummern_zone(self, gewaehlt):
        """Zone (v0.9, bank.md): je Fertigkeit die zwei sehr leichten, die
        mittlere und je Fallstrick eine; das Zone-Paar (Fehler finden und
        gleichartige Rechnung) als eigene Nummer hinter seiner Fertigkeit.
        --zone kurz: eine leichte und ein Fallstrick."""
        log = self.log
        if self.a.zone == "nein" or not self.zone:
            if not self.zone:
                log("ZONE: zone.jsonl fehlt")
            return []
        aus, paare = [], []
        einschraenken = bool(self.a.einheiten or self.fokus)
        for nr, name, art, zeilen in ketten_von(self.zone):
            wo = f"Zone f{nr} „{name[:40]}“"
            angabe, nummern = self.mappe.fertigkeit(name)
            if einschraenken:
                if nummern and not (nummern & set(gewaehlt)):
                    log(f"WEG {wo} – gebraucht in {angabe}, nicht bestellt")
                    continue
                if not nummern:
                    log(f"ZONE {wo}: Einheitenangabe nicht lesbar, bleibt")
            zz = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
            fehler = [z for z in zz if z["hoehe"] == "pflicht"
                      and z.get("pflicht") == "fehler"]
            folgezeilen = [z for f in fehler for z in zz
                           if z["sprosse"] == f["sprosse"] + 1
                           and z["hoehe"] != "pflicht"]
            leicht = [z for z in zz if z["hoehe"] == "grundfall"]
            falle = [z for z in zz if z["hoehe"] == "sprosse"
                     and re.match(r"^Fallstrick", z.get("merkmal") or "")
                     and z not in folgezeilen]
            mittel = [z for z in zz if z["hoehe"] == "sprosse"
                      and z not in falle and z not in folgezeilen]
            if self.a.zone == "kurz":
                folge = leicht[:1] + falle[:1]
            else:
                folge = leicht[:2] + mittel[:1] + falle
            folge.sort(key=lambda z: (z["sprosse"], z["variante"]))
            for z in folge:
                log(f"AUSWAHL {z['id']} – {wo}: "
                    + ("sehr leicht" if z in leicht else "Fallstrick"
                       if z in falle else "mittel"))
            for z in zz:
                if z not in folge and z not in fehler and z not in folgezeilen:
                    log(f"WEG {z['id']} – {wo}: über der Menge (zwei sehr "
                        "leichte, eine mittlere, je Fallstrick eine)")
            tk = self.ich_kann(0, name, "", "Ich kann " + name.split(",")[0]
                               .split(" (")[0] + ".")
            if folge:
                aus += self.hn(tk, folge, "zone", name, 0)
            if self.a.zone == "ja" and fehler:
                paar = fehler[:1] + folgezeilen[:1]
                for z in paar:
                    log(f"AUSWAHL {z['id']} – Zone-Paar {wo} (am Ende der Zone)")
                hp = self.hn(self.ich_kann(0, name, "paar", PFLICHT_ICHKANN[
                    "fehler"]), paar, "zonepaar", name, 0)
                if self.lernblatt:
                    paare += hp
                else:
                    aus += hp
        # Lernblatt v0.9 (zweiter Durchgang): das Zone-Paar steht am Ende der
        # Zone; Fokus und schwach behalten es hinter seiner Fertigkeit
        return aus + paare

    def pruefe_dich(self, gewaehlt, einheiten):
        """Seite „Prüfe dich“ (ziel.md § 2, v0.9): je Verfahrenskette des
        Blatts eine Aufgabe, gemischt, ohne Titel – die mittlere Sprosse der
        Kette (Grundfall und Sprossen, ohne Vorstufe und Prüfungshöhe) in der
        kleinsten Variante, die im Blatt nicht steht; fehlt eine, Variante 1
        (log PRÜFE-DICH). Die Lösung verweist auf die Nummer der Kette."""
        log = self.log
        im_blatt = set(self.lage)
        aus = []
        for n in gewaehlt:
            for nr, name, art, zeilen in ketten_von(self.e[n]):
                if art != "verfahren":
                    continue
                wo = f"e{n} k{nr} „{name}“"
                sp = sorted({z["sprosse"] for z in zeilen
                             if z["hoehe"] in ("grundfall", "sprosse")})
                if not sp:
                    log(f"PRÜFE-DICH {wo}: keine Sprosse – entfällt")
                    continue
                mitte = sp[len(sp) // 2]
                zz = sorted([z for z in zeilen if z["sprosse"] == mitte],
                            key=lambda z: z["variante"])
                frei = [z for z in zz if z["id"] not in im_blatt]
                if frei:
                    wahl = frei[0]
                    log(f"PRÜFE-DICH {wahl['id']} – {wo}: mittlere Sprosse "
                        f"{mitte} von {sp[0]}–{sp[-1]}, kleinste Variante, die "
                        "im Blatt nicht steht")
                else:
                    wahl = zz[0]
                    log(f"PRÜFE-DICH {wahl['id']} – {wo}: mittlere Sprosse "
                        f"{mitte}, alle Varianten stehen schon im Blatt – "
                        "Variante 1 (doppelt)")
                ziel = next((h for m, hs in einheiten if m == n for h in hs
                             if h.kette == name and h.lage == "leiter"
                             and any(z["sprosse"] == mitte for z in h.folge)),
                            None)
                h = Hauptnummer("", [wahl], "pruefe-dich", name, n)
                h.lage = "pruefe-dich"
                h.laeufe = laeufe_von([wahl])
                h.ziel = ziel.nr if ziel else None
                aus.append(h)
        # gemischt: feste Folge aus der Prüfsumme der id (wortgleich bei
        # gleicher Bestellung), keine Kettenfolge
        aus.sort(key=lambda h: hashlib.md5(h.folge[0]["id"].encode())
                 .hexdigest())
        for h in aus:
            self.lage[h.folge[0]["id"]] = "pruefe-dich"
        return aus

    # Zone → Lernblatt ------------------------------------------------------
    def fertigkeit_ziel(self, zeile, einheiten_hn):
        """(Einheiten, Einheit, Hauptnummer, Grund) einer Voraussetzungszeile
        (v0.9, zweiter Durchgang): die Einheiten, die die Zeile nennt
        („Einheit 2“, „ab Einheit 2“); bei „alle Einheiten“, „jede Einheit“
        oder ohne Angabe die erste Einheit des Blatts. Ziel des Verweises ist
        die erste Hauptnummer der kleinsten genannten Einheit im Blatt."""
        nummern, art = fertigkeit_einheiten(zeile)
        blatt = [n for n, hs in einheiten_hn if hs]
        if not blatt:
            return set(), None, None, "kein Lernblatt"
        rest = zeile.split(" – ", 1)[-1].split("Thema ", 1)[0]
        if art == "alle" or re.search(r"jede[rn]? Einheit", rest):
            gilt, grund = set(blatt), "alle Einheiten"
        elif art == "genannt":
            gilt, grund = nummern & set(blatt), "Einheit genannt"
            if not gilt:
                gilt, grund = {blatt[0]}, ("genannte Einheit nicht im Blatt: "
                                           "erste Einheit")
        else:
            gilt, grund = {blatt[0]}, "ohne Angabe: erste Einheit"
        n = min(gilt, key=blatt.index)
        h = next(hs[0] for m, hs in einheiten_hn if m == n)
        return gilt, n, h, grund

    def zone_zeile(self, kette):
        return next((x for x in self.mappe.fertigkeit_zeilen
                     if x == kette or x.startswith(kette)), None)

    # Satz ------------------------------------------------------------------
    def kurz_tauglich(self, z, term):
        if term is None or z.get("grafik") or z.get("pflicht"):
            return False
        if z["form"] not in ("teil", "gleichungsraster"):
            return False
        if re.search(r"\\(rechnung|kreuz|wertetabelle)", z["aufgabe"]):
            return False
        if (z.get("antwort") or "").count("__") > 2 or ";" in (z.get("antwort")
                                                             or ""):
            return False        # breites Antwortgerüst passt nicht in eine Hälfte
        return len(schlicht(term)) <= LB_KURZ

    def kurz_text(self, z, term, auftrag):
        """Kurzer Term mit Feld dahinter: „7x + 2x = ____“ (Befund 42)."""
        if LB_OHNE_FELD.search(auftrag):
            feld = []
        else:
            feld = antwort_zeilen(z.get("antwort") or "") or ["\\lbfeld"]
            feld = ["\\lbfeld" if f.strip() == "\\kbfeld" else f for f in feld]
        text_ohne = re.sub(r"\$[^$]*\$", "", term)
        rechnen = LB_RECHNEN.match(auftrag) and "=" not in term and \
            not re.search(r"[A-Za-zÄÖÜäöüß]{2,}", text_ohne)
        if not feld:
            return term
        if rechnen and term.count("$") == 2 and term.startswith("$") \
                and term.endswith("$"):
            return term[:-1] + " =$ " + " \\quad ".join(feld)
        if rechnen:
            return term + " $=$ " + " \\quad ".join(feld)
        return term + " \\quad " + " \\quad ".join(feld)

    def kreuz_tauglich(self, z, rest):
        """Ankreuzaufgabe, die in eine halbe Spalte passt: kurzer Text, kurze
        Optionen, keine Grafik, keine Prüfkennung."""
        if rest is None or z["form"] != "ankreuzen" or z.get("grafik") or \
                KENNUNG.search(z["aufgabe"]):
            return False
        text, kreuze = befehle_heraus(rest, "kreuz")
        if self.lernblatt:
            # v1.0 (Befund 8): nebeneinander nur, wenn Text und Optionen
            # zusammen höchstens 120 Zeichen Quelltext haben
            return bool(kreuze) and len(rest.strip()) <= LB_KREUZ_PAAR
        return bool(kreuze) and len(schlicht(text.replace("\\\\", ""))) <= 110 \
            and all(len(schlicht(k[7:-1])) <= 24 for k in kreuze)

    def vorstufe_paar(self, z):
        """Vorstufe, die als ganze Aufgabe in eine halbe Spalte passt (v1.0
        im Lernblatt: in eine Zeile der halben Spalte, Befund 8 – kein
        Umbruch mitten im Satz)."""
        if self.lernblatt and len(schlicht(z["aufgabe"])) > LB_HALB_ZEILE:
            return False
        return (z["hoehe"] == "vorstufe" and z["form"] == "teil"
                and not z.get("grafik") and not KENNUNG.search(z["aufgabe"])
                and not re.search(r"\\(rechnung|kreuz|wertetabelle)|\\\\",
                                  z["aufgabe"])
                and len(schlicht(z["aufgabe"])) <= 75)

    def teil_lern(self, z, rest, b, anw):
        """Eine Teilaufgabe über satz_teil (Kompetenzblatt); Lernblatt-Regeln
        davor und danach: Term ohne Gleichheitszeichen mit „= ____“ (Befund
        42), Gleichung mit Text als Textaufgabe, Aufzählungen (1), (2) je eine
        Zeile, Textaufgabe ohne Antwortgerüst mit Schreibzeilen."""
        z2 = dict(z) if rest is None else dict(z, aufgabe=rest)
        if z["hoehe"] == "vorstufe":
            z2["loesung"] = ""      # Befund 38: kein Raum bei Erkennen, Eintragen
        rein = re.fullmatch(r"\s*(\$[^$]*\$[\s,;]*)+", z2["aufgabe"]) is not None
        if z["form"] == "gleichungsraster":
            if rein and "=" not in z2["aufgabe"]:
                z2["antwort"] = "= __"
            elif not rein:
                z2["form"], z2["antwort"] = "text", ""
        elif rein and "=" not in z2["aufgabe"] and anw and \
                LB_RECHNEN.match(anw) and (z2.get("antwort") or "").strip() == "__":
            z2["antwort"] = "= __"
        liste = []
        if "\\\\" in z2["aufgabe"] and "\\kreuz" not in z2["aufgabe"]:
            geschuetzt, st = schuetze(z2["aufgabe"])   # \\\\ in \\rechnung bleibt
            stuecke = [zurueck(x, st).strip()
                       for x in re.split(r"\\\\", geschuetzt)]
            if len(stuecke) > 1 and all(stuecke):
                z2["aufgabe"], liste = stuecke[0], stuecke[1:]
        zeilen = self.satz_teil(z2, b, anw)
        if liste:
            k = 0
            while k < len(zeilen) and zeilen[k].startswith(
                    ("\\kbanweisung", "\\kbteil", "\\kbfrage")):
                k += 1
            if k:
                zeilen.insert(k, "\\kbfrage{" + " \\\\ ".join(liste) + "}")
            else:
                zeilen = self.satz_teil(dict(z2, aufgabe=" ".join(
                    [z2["aufgabe"]] + liste)), b, anw)
        # Schreibraum für Text-, Fehler- und Anwendungsaufgaben ohne
        # Antwortgerüst (Befund 9: Rechnen und Begründen), statt eines
        # einzelnen Felds oder gar nichts
        n_raum = 3 if z.get("pflicht") == "anwendung" else 2
        if LB_OHNE_FELD.search(" ".join([anw, z["aufgabe"]])) and \
                not z2.get("antwort"):
            zeilen = [x for x in zeilen if x != "\\kbantwort{\\kbfeld}"]
        if z2["form"] == "text" and not z2.get("antwort") and \
                "\\kbantwort{\\kbfeld}" in zeilen:
            zeilen[zeilen.index("\\kbantwort{\\kbfeld}")] = \
                f"\\item[]\\kbraum{{{n_raum}}}"
        elif z2["form"] in ("text", "teil") and not z2.get("antwort") and \
                not z2.get("grafik") and "\\kreuz" not in z2["aufgabe"] and \
                not any(("\\kbraum" in x or "\\kbantwort" in x) for x in zeilen) \
                and (z.get("pflicht") or z2["form"] == "text"):
            zeilen.append(f"\\item[]\\kbraum{{{n_raum}}}")
            self.log(f"RAUM {z['id']}: {n_raum} Schreibzeilen (Text ohne "
                     "Antwortgerüst)")
        return zeilen

    def satz_lern(self, h):
        """Hauptnummer im Satz des Kompetenzblatts (v0.9): Titel = Ich-kann-
        Satz, Auftrag eines Laufs einmal darüber, kurze Terme und kurze
        Ankreuzaufgaben paarweise nebeneinander."""
        titel = klar(h.titel) + ("\\lbgym" if getattr(h, "gym", False) else "")
        aus = ["", f"% {h.lage}: " + ", ".join(z["id"] for z in h.folge),
               f"\\begin{{kbaufgabe}}{{{titel}}}"]
        mehr = len(h.folge) > 1
        h.buchstaben = []
        # Einheiten des Satzes: ("gruppe", Auftrag, [(z, Term)], Art) für
        # Läufe nebeneinander, ("einzel", Auftrag, z, Term) sonst
        teile = []
        for auftrag, zz, terme in h.laeufe:
            art = None
            if auftrag and len(zz) >= 2:
                if all(self.kurz_tauglich(z, t) for z, t in zip(zz, terme)):
                    art = "kurz"
                elif all(self.kreuz_tauglich(z, t) for z, t in zip(zz, terme)):
                    art = "kreuz"
            if art:
                teile.append(("gruppe", auftrag, list(zip(zz, terme)), art))
                continue
            for j, (z, t) in enumerate(zip(zz, terme)):
                teile.append(("einzel", auftrag if t is not None and j == 0
                              else "", z, t))
        # Vorstufen ohne gemeinsamen Auftrag (Faktor 3, Faktor 2 …): kurze
        # ganze Aufgaben paarweise, ohne Schreibraum
        k, neu = 0, []
        while k < len(teile):
            m = k
            while m < len(teile) and teile[m][0] == "einzel" and \
                    self.vorstufe_paar(teile[m][2]):
                m += 1
            if m - k >= 2:
                neu.append(("gruppe", "", [(u[2], None) for u in teile[k:m]],
                            "vorstufe"))
                k = m
            else:
                neu.append(teile[k])
                k += 1
        teile = neu
        i = 0
        erste = True
        voll = []           # Teilaufgaben mit ganzem Text (Auftrag darin)
        for u in teile:
            if u[0] == "gruppe":
                _, auftrag, paare, art = u
                self.log(f"NEBENEINANDER Nr. {h.nr}: {len(paare)} Teilaufgaben "
                         f"({art})" + (f", Auftrag „{auftrag}“" if auftrag
                                       else ""))
                for k in range(0, len(paare), 2):
                    halb = []
                    for z, t in paare[k:k + 2]:
                        b = buchstabe(i) + ")"
                        if art == "kurz":
                            halb.append(f"\\kbteil{{{b}}}{{"
                                        f"{self.kurz_text(z, t, auftrag)}}}{{}}")
                        elif art == "vorstufe" and re.search(
                                r"^[^:$]+: \$[^$]*\$$", z["aufgabe"].strip()):
                            # „Klammere den Faktor 3 aus: $9x + 21$“ als ein
                            # Satz, nicht als halbfetter Auftakt
                            halb.append("\n".join(self.teil_lern(
                                z, z["aufgabe"].strip() + ".", b, "")))
                        else:
                            halb.append("\n".join(self.teil_lern(z, t, b, "")))
                        h.buchstaben.append((buchstabe(i), z))
                        i += 1
                    if len(halb) == 1:
                        halb.append("\\item[]")
                    aus.append("\\begin{kbblock}")
                    anw_g = auftrag or (h.anweisung if erste else "")
                    if k == 0 and anw_g and self.anweisung_noetig(
                            h, anw_g, [p_[0] for p_ in paare],
                            [p_[1] for p_ in paare]):
                        aus.append(f"\\kbanweisung{{{klar(anw_g)}}}")
                    aus += ["\\lbpaar{" + halb[0], "}{" + halb[1] + "}"]
                    aus.append("\\end{kbblock}")
                erste = False
                continue
            _, anw, z, t = u
            b = buchstabe(i) + ")" if mehr else ""
            if t is None:
                voll.append(z)
                anw = h.anweisung if erste else ""
                if not anw and z["form"] == "gleichungsraster" and \
                        "=" in z["aufgabe"] and "$" not in z["aufgabe"]:
                    anw = "Löse die Gleichung."
            # v1.0 (Befund 3): Auftrag nur, wo der Term allein mehrdeutig ist
            zeige = self.anweisung_noetig(h, anw, [z], [t]) if anw else False
            aus.append("\\begin{kbblock}")
            if t is not None and anw and self.kurz_tauglich(z, t) and \
                    rechenzeilen(z) == 0:
                # kurzer Term allein: „$3 \\cdot (-6a) =$ ____“ in einer Zeile
                # wie im Paar (Befund 42), kein Raum
                aus += ([f"\\kbanweisung{{{klar(anw)}}}"] if zeige else []) + \
                    [f"\\kbteil{{{b}}}{{{self.kurz_text(z, t, anw)}}}{{}}"]
                self.log(f"KURZ {z['id']}: Term und Feld in einer Zeile")
            else:
                aus += self.teil_lern(z, t, b, anw if zeige else "")
            aus.append("\\end{kbblock}")
            h.buchstaben.append((buchstabe(i) if mehr else "", z))
            i += 1
            erste = False
        self.pruefe_auftrag(h, aus, voll)
        if h.lage == "pruefe-dich" and not h.titel:
            # Prüfe dich: kein Ich-kann-Titel; der Auftrag steht in der
            # Zeile der Nummer statt in einer eigenen Zeile darunter
            k = next((i for i, x in enumerate(aus)
                      if x.startswith("\\kbanweisung{")), None)
            if k is None:
                k = next((i for i, x in enumerate(aus) if "\\kbanweisung{"
                          in x), None)
            if k is not None:
                m = re.search(r"\\kbanweisung\{((?:[^{}]|\{[^{}]*\})*)\}",
                              aus[k])
                aus[k] = aus[k].replace(m.group(0), "", 1)
                if not aus[k]:
                    del aus[k]
                j = aus.index("\\begin{kbaufgabe}{}")
                aus[j] = f"\\begin{{kbaufgabe}}{{{m.group(1)}}}"
        if h.verweis:
            # Blatt 0 (v0.9, zweiter Durchgang): Verweis als eigene Zeile unter
            # der Hauptnummer, im letzten Block (bricht nicht allein um)
            k = max(i for i, x in enumerate(aus) if x == "\\end{kbblock}")
            aus.insert(k, f"\\item[]\\lbhaengst{{{h.verweis}}}")
        aus.append("\\end{kbaufgabe}")
        n_teil = len(h.buchstaben)
        n_graf = sum(1 for _, z in h.buchstaben if z and z.get("grafik"))
        if (n_graf == 0 and n_teil > LB_TEIL_MAX) or \
                (n_graf > 0 and n_teil > LB_TEIL_MAX_GRAFIK):
            self.log(f"WARNUNG Nr. {h.nr}: {n_teil} Teilaufgaben, {n_graf} "
                     "mit Grafik – über dem Halbseitenmaß (2.3 g)")
        return aus

    def pruefe_auftrag(self, h, aus, voll):
        """Prüfung AUFTRAG (v0.9): kein Auftragssatz zweimal in einer
        Hauptnummer – gezählt über die Anweisungen (\\kbanweisung) und die
        Aufträge in Teilaufgaben mit ganzem Text."""
        saetze_ = [m.group(1) for x in aus for m in
                   [re.match(r"^\\kbanweisung\{(.*)\}$", x)] if m]
        if self.lernblatt:
            # v1.0 (Befund 3): Prüfung AUFTRAG nur für nackte Terme und
            # Gleichungen; Teilaufgaben mit Bedingung oder Kontext tragen
            # ihren Satz mit Absicht je einzeln
            voll = [z for z in voll for a in [zerlege_auftrag(z)]
                    if a and a[2] == "doppelpunkt" and nackt(a[1])]
        for z in voll:
            a = zerlege_auftrag(z)
            if a:
                saetze_.append(klar(a[0]))
        for x in sorted(set(saetze_)):
            if saetze_.count(x) > 1:
                self.auftrag_doppelt.append(f"Nr. {h.nr}: {x}")
                self.log(f"AUFTRAG Nr. {h.nr}: „{x}“ steht "
                         f"{saetze_.count(x)}-mal")
        # Satzebene (Hinweis): gleicher Aufforderungs- oder Fragesatz, Mathe
        # als „…“, in Anweisung und ganzen Teilaufgaben – meist verschieden
        # formulierte Bankzeilen oder Ankreuz- und Kontextaufgaben
        orte = [m.group(1) for x in aus for m in
                [re.match(r"^\\kbanweisung\{(.*)\}$", x)] if m]
        orte += [KENNUNG.sub("", z["aufgabe"]).split("\\\\")[0] for z in voll]
        zaehl = {}
        for text in orte:
            t, _ = schuetze(text)
            t = re.sub(r"\x00\d+\x01", "…", t)
            for satz in set(saetze(t)):
                if IMPERATIV.match(satz) or LB_VERB.match(satz) or \
                        satz.endswith("?"):
                    zaehl[satz] = zaehl.get(satz, 0) + 1
        for satz, n in sorted(zaehl.items()):
            if n > 1:
                self.satz_doppelt.append(f"Nr. {h.nr}: {satz}")
                self.log(f"AUFTRAG-SATZ Nr. {h.nr}: „{satz}“ steht {n}-mal "
                         "(Hinweis: Satz wiederholt, kein gemeinsamer Auftrag erkannt)")

    def satz_schwach(self, h):
        """Rezept S: Form 2.8 wie bis v0.8, Titel aus ich-kann.csv."""
        aus = [f"\\begin{{aufgabe}}{{{klar(h.titel)}}}"]
        h.buchstaben = []
        i = 0
        for z in h.folge:
            if z.get("paeckchen"):
                aus.append("\\swfrage{Was bleibt gleich, was ändert sich?}")
                h.buchstaben.append((buchstabe(i), None))
                i += 1
                continue
            zeilen, _ = teil_schwach(z, self.log, h.nr)
            aus += zeilen
            h.buchstaben.append((buchstabe(i), z))
            i += 1
        aus.append("\\end{aufgabe}")
        return aus

    def satz_hauptnummer(self, h):
        return self.satz_schwach(h) if self.schwach else self.satz_lern(h)

    def satz_loesung(self, h):
        teile = []
        vor = []
        for b, z in h.buchstaben:
            if z is None:
                teile.append(f"{b}) \\ldots")
                vor.append(f"%% TODO Lösung der Erklärzeile {h.nr}{b}) "
                           "fehlt in der Bank")
                continue
            lo = f"{b}) {z['loesung']}" if b else z["loesung"]
            m = re.match(r"^Fallstrick:\s*(.+)$", z.get("merkmal") or "")
            if h.lage in ("zone", "zonepaar") and m:
                # Blatt 0 (v0.9): falsche Antwort zeigt die Lücke
                lo += f" (falsch $\\rightarrow$ Lücke: {m.group(1).strip()})"
            if h.lage == "pruefe-dich" and h.ziel:
                lo += f" (falsch $\\rightarrow$ Nr.~{h.ziel})"
            if h.lage == "test" and getattr(h, "test_ziel", {}).get(z["id"]):
                # v1.0 (Befund 10): richtig → die Nummern der Kette überspringen
                lo += (" (richtig $\\rightarrow$ "
                       f"{h.test_ziel[z['id']]} überspringen)")
            teile.append(lo)
        aus = vor + [f"\\erg{{{h.nr}}}{{" + " \\quad ".join(teile) + "}"]
        for b, z in h.buchstaben:
            if z and z.get("loesungsgrafik"):
                aus += ["", f"{h.nr}{b})", "", z["loesungsgrafik"], ""]
        return aus

    def kasten(self, n):
        zeilen = self.mappe.kasten.get(n)
        if not zeilen:
            return [f"%% TODO Merkkasten Einheit {n} nicht in der Mappe lesbar"]
        return ["\\kbmerk{Zum Merken}{" + " \\\\ ".join(
            kasten_mathe(z) for z in zeilen) + "}"]

    def kopf(self, n, pos, anzahl, baut_auf):
        info = self.mappe.einheiten.get(n)
        titel = info["titel"] if info else None
        aus = []
        if titel is None:
            aus.append(f"%% TODO Einheitentitel {n} nicht in der Mappe lesbar")
            titel = f"Einheit {n}"
        if self.fokus:
            text = f"Einheit {n} · {titel}"
        else:
            text = f"Einheit {pos} von {anzahl} · {titel}"
        aus.append(f"\\einheitenkopf[e{n}]{{{klar(text)}}}")
        os_, gym, wort = marke_zerlegen(info["marken"] if info else None)
        wort = pruefwort_zahl(info["marken"] if info else None,
                              self.e.get(n, []), self.log) or wort
        zm = zeitmarke(os_, gym, self.klasse)
        satz, quelle = hier_lernst_du(info)
        teile = [t for t in (satz, zm, wort) if t]
        if baut_auf:
            teile.append("baut auf: " + ", ".join(baut_auf))
        if not satz:
            aus.insert(0, f"%% TODO Zweigzeile Teil 1 Einheit {n}: {quelle}")
        if teile:
            aus.append("\\zweigzeile{" + klar(" · ".join(teile)) + "}")
        self.log(f"KOPF Einheit {n}: „{text}“; Zweigzeile „{' · '.join(teile)}“ "
                 f"(Satz: {quelle}; Marken „{info['marken'] if info else None}“)")
        return aus, titel

    # Lernblatt v1.0 ----------------------------------------------------------
    def einheit_titel(self, n):
        info = self.mappe.einheiten.get(n)
        return info["titel"] if info else None

    def test_hn(self, n, hs, naechst, im_blatt):
        """Befund 10: Test am Kopf der Einheit – je Verfahrenskette (Folge wie
        im Blatt) eine Teilaufgabe der obersten Sprosse ohne Textaufgabe: die
        höchste Sprosse, deren form nicht text ist und die keinen Sachkontext
        trägt, in einer Variante, die im Blatt nicht steht (die kleinste
        freie; fehlt eine, die mit der höchsten Variantennummer). Ohne
        Verfahrenskette die Typen ohne Kette."""
        log = self.log
        # Pflichtketten tragen oft den Namen der Verfahrenskette
        # („Zusammenfassen“): sie zählen hier nicht
        ketten = {name: (art, zeilen) for _, name, art, zeilen in
                  ketten_von(self.e[n]) if art != "pflicht"}
        folge_namen = []
        for h in hs:
            if h.lage == "leiter" and h.kette not in folge_namen and \
                    ketten.get(h.kette, ("",))[0] == "verfahren":
                folge_namen.append(h.kette)
        quelle = "Verfahrenskette"
        if not folge_namen:
            folge_namen = [h.kette for h in hs if h.lage == "ohne"]
            folge_namen = list(dict.fromkeys(folge_namen))
            quelle = "Typ ohne Kette (keine Verfahrenskette in der Einheit)"
        wahl = []
        for name in folge_namen:
            art, zeilen = ketten[name]
            kand = [z for z in zeilen
                    if z["hoehe"] in ("grundfall", "sprosse", "pruefung")
                    and z["form"] != "text" and not hat_sachkontext(z)]
            if not kand:
                log(f"TEST e{n} „{name}“: keine Sprosse ohne Textaufgabe – "
                    "keine Teilaufgabe")
                continue
            top = max(z["sprosse"] for z in kand)
            zz = sorted([z for z in kand if z["sprosse"] == top],
                        key=lambda z: z["variante"])
            frei = [z for z in zz if z["id"] not in im_blatt]
            if frei:
                w = frei[0]
                grund = "kleinste freie Variante"
            else:
                w = zz[-1]
                grund = ("alle Varianten stehen im Blatt – höchste "
                         "Variantennummer (doppelt)")
            wahl.append(w)
            im_blatt.add(w["id"])
            self.test_wahl.append(f"e{n} {name}: {w['id']}")
            log(f"TEST {w['id']} – e{n} „{name}“ ({quelle}): oberste Sprosse "
                f"ohne Textaufgabe {top} ({w['hoehe']}), {grund}")
        if not wahl:
            log(f"TEST e{n}: keine Teilaufgabe – kein Test")
            return None
        titel = TEST_TITEL + (f" Dann weiter zu „{naechst}“" if naechst
                              else " Dann bist du fertig")
        h = Hauptnummer(titel, wahl, "test", wahl[0]["kette"], n)
        h.lage = "test"
        h.laeufe = self.laeufe_lern(wahl)
        h.test_ketten = [z["kette"] for z in wahl]
        for z in wahl:
            self.lage[z["id"]] = "test"
        return h

    def gym_markieren(self, n, hs):
        """Befund 5: Typen, die der Katalog nur dem Gymnasium zuordnet
        („[GYM 8]“ ohne OS), bekommen rechts im Titel der Hauptnummer „GYM“ –
        wenn alle Teilaufgaben der Nummer zu einem solchen Typ gehören (Typ
        wortgleich im Kettennamen, in sprosse_text oder mit seinem
        Klammerinhalt). Sonst nichts; log GYM."""
        typen = self.mappe.gym_typen.get(n, [])
        if not typen:
            return

        def passt(z, typ):
            kopf = re.split(r"\s*\(", typ, 1)[0].strip().casefold()
            klammer = re.findall(r"\(([^()]*)\)", typ)
            st = (z.get("sprosse_text") or "").casefold()
            return (kopf and (kopf == z["kette"].casefold() or kopf in st)) \
                or any(k.strip() and k.strip().casefold() in st
                       for k in klammer)
        for typ in typen:
            treffer = []
            for h in hs:
                zz = [z for z in h.folge if z.get("id")]
                gut = [z for z in zz if passt(z, typ)]
                if zz and len(gut) == len(zz):
                    h.gym = True
                    self.gym.append(f"Nr. {h.nr}: {typ}")
                    self.log(f"GYM Nr. {h.nr} „{h.titel}“: Typ „{typ}“ nur "
                             "Gymnasium")
                    treffer.append(h)
                elif gut:
                    self.log(f"GYM e{n} Typ „{typ}“: Teilaufgaben "
                             + ", ".join(z["id"] for z in gut)
                             + f" in Nr. {h.nr} „{h.titel}“, die Nummer trägt "
                             "auch anderes – keine Marke")
            if not any(passt(z, typ) for h in hs for z in h.folge
                       if z.get("id")):
                self.log(f"GYM e{n} Typ „{typ}“: keine Teilaufgabe zugeordnet – "
                         "keine Marke")

    def baue_lern(self):
        """Rezept L ab v1.0: Zone, je Einheit in Blattfolge Titel, Test,
        Nummern, „Verstanden?“; Lösungen am Ende des Gesamt."""
        log = self.log
        gewaehlt = self.einheiten()
        self.einheiten_folge = gewaehlt
        log(f"EINHEITEN {gewaehlt}")
        zone = self.hauptnummern_zone(gewaehlt)
        einheiten = [(n, self.hauptnummern_einheit(n)) for n in gewaehlt]
        im_blatt = set(self.lage)
        for i, (n, hs) in enumerate(einheiten):
            naechst = (self.einheit_titel(einheiten[i + 1][0])
                       or f"Einheit {einheiten[i + 1][0]}") \
                if i + 1 < len(einheiten) else None
            th = self.test_hn(n, hs, naechst, im_blatt)
            if th:
                hs.insert(0, th)
        nr = 0
        for h in zone:
            nr += 1
            h.nr = nr
        for _, hs in einheiten:
            for h in hs:
                nr += 1
                h.nr = nr
        for n, hs in einheiten:
            self.gym_markieren(n, hs)
            for h in hs:
                if h.lage != "test":
                    continue
                h.test_ziel = {}
                for z in h.folge:
                    nrn = [x.nr for x in hs if x.kette == z["kette"]
                           and x.lage in ("vorstufe", "leiter", "pruefung",
                                          "ohne")]
                    if nrn:
                        h.test_ziel[z["id"]] = "Nr.~" + nummern_bereich(nrn)
                        log(f"TEST-ZIEL Nr. {h.nr}: {z['id']} richtig → "
                            f"Nr. {nummern_bereich(nrn)} überspringen")
        # Zone → erste Nummer der Einheit, die die Voraussetzungszeile nennt
        for zeile in self.mappe.fertigkeit_zeilen:
            gilt, n_ziel, h_ziel, grund = self.fertigkeit_ziel(zeile, einheiten)
            if h_ziel is None:
                continue
            for h in zone:
                if self.zone_zeile(h.kette) == zeile:
                    h.verweis = h_ziel.nr
                    log(f"ZONE-VERWEIS Nr. {h.nr} → Nr. {h_ziel.nr} "
                        f"(Einheit {n_ziel}; {grund})")
        for h in zone:
            if h.verweis is None:
                log(f"ZONE-VERWEIS Nr. {h.nr}: Fertigkeit nicht in den "
                    "Voraussetzungen der Mappe – kein Verweis")
        dateien = {}
        if zone:
            a = ["% Zone „Das kennst du schon“ – aus bank/"
                 f"{self.eintrag}/zone.jsonl (zusammenbau {VERSION})",
                 "\\einheitenkopf[zone][Das kennst du schon]"
                 "{Das kennst du schon}", "\\setcounter{aufgabe}{0}"]
            for h in zone:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, "blatt0_a.tex"))
            dateien["blatt0_a.tex"] = a
            l = ["% Lösungen Zone (zusammenbau " + VERSION + ")",
                 "\\kbabschnitt{Das kennst du schon}", ""]
            for h in zone:
                l += self.satz_loesung(h)
            dateien["blatt0_l.tex"] = l
        for n, hs in einheiten:
            titel = self.einheit_titel(n)
            kopf = []
            if titel is None:
                kopf.append(f"%% TODO Einheitentitel {n} nicht in der Mappe "
                            "lesbar")
                titel = f"Einheit {n}"
            # Befund 5, 7: nur der Titel – kein „Einheit n von m“, keine
            # Zweigzeile; Kopfzeile „Thema · Lernblatt · <Titel>“
            kopf.append(f"\\einheitenkopf[e{n}][{klar(titel)}]{{{klar(titel)}}}")
            log(f"KOPF Einheit {n}: „{titel}“ (nur Titel)")
            start = hs[0].nr if hs else nr + 1
            a = [f"% Einheit {n} – {titel} (bank/{self.eintrag}/e{n}.jsonl, "
                 f"zusammenbau {VERSION})"] + kopf
            if self.a.kasten:
                a += self.kasten(n)
            a.append(f"\\setcounter{{aufgabe}}{{{start - 1}}}")
            for h in hs:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, f"e{n}_a.tex"))
            dateien[f"e{n}_a.tex"] = a
            l = [f"% Lösungen Einheit {n} – {titel} (zusammenbau {VERSION})",
                 f"\\kbabschnitt{{{klar(titel)}}}", ""]
            for h in hs:
                l += self.satz_loesung(h)
            dateien[f"e{n}_l.tex"] = l
        dateien.update(self.rahmen_lern(zone, einheiten))
        texte = [z for v in dateien.values() for z in v]
        zeichen, self.zeichen = zeichen_vorspann(texte)
        vorspann = VORSPANN.rstrip("\n").split("\n")
        vorspann = vorspann[:-1] + VORSPANN_LERN.split("\n") + \
            VORSPANN_LERN10.split("\n") + (
                ["% Zeichen dieses Blatts, die Latin Modern nicht hat"] + zeichen
                if zeichen else []) + vorspann[-1:]
        dateien["vorspann.tex"] = vorspann
        log(f"ZEICHEN Ersatz im Vorspann: {''.join(self.zeichen) or '–'}")
        log(f"AUFTRAG {len(self.auftrag_doppelt)} Hauptnummern mit einem "
            "Auftragssatz in mehr als einer Teilaufgabe (nackte Terme); "
            f"Hinweis AUFTRAG-SATZ {len(self.satz_doppelt)} Sätze")
        log(f"TEXT {len(self.sach_weg)} Teilaufgaben mit Sachkontext "
            "ausgelassen" + (" (--mit-sachaufgaben: keine Grenze)"
                             if self.mit_sach else ""))
        log(f"GYM {len(self.gym)} Hauptnummern mit Marke")
        for name, zeilen in sorted(dateien.items()):
            if not name.endswith("_a.tex"):
                continue
            for zeile in zeilen:
                if not zeile.startswith("%") and BANKWORT.search(zeile):
                    log(f"BANKWORT „{BANKWORT.search(zeile).group(0)}“ in "
                        f"{name}: {zeile[:80]}")
        return dateien

    def rahmen_lern(self, zone, einheiten):
        """Dokumente des Lernblatts v1.0: keine Verzeichniszeile (Befund 2),
        Einheiten in Blattfolge, kein „Prüfe dich“, kein „Das kann ich“; das
        Gesamt endet mit den Lösungen auf neuer Seite (Befund 14)."""
        th = klar(self.thema)
        kopf = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}",
                "\\input{vorspann}"]
        k = self.kennung

        def dok(blatt, rumpf):
            return kopf + ["\\begin{document}",
                           f"\\blattkopf*{{{th}}}{{{blatt}}}{{{k}}}"] + \
                rumpf + ["\\end{document}"]
        e_inputs = []
        for i, (n, _) in enumerate(einheiten):
            if i:
                e_inputs.append("\\clearpage")
            e_inputs.append(f"\\input{{e{n}_a}}")
        l_inputs = []
        if zone:
            l_inputs.append("\\input{blatt0_l}")
        for n, _ in einheiten:
            if l_inputs:
                l_inputs.append("\\bigskip")
            l_inputs.append(f"\\input{{e{n}_l}}")
        dateien = {}
        if zone:
            dateien[f"{k}-blatt0.tex"] = dok("Lernblatt", ["\\input{blatt0_a}"])
        for n, _ in einheiten:
            dateien[f"{k}-e{n}.tex"] = dok("Lernblatt", [f"\\input{{e{n}_a}}"])
        dateien[f"{k}.tex"] = dok("Lernblatt", e_inputs)
        g = (["\\input{blatt0_a}", "\\clearpage"] if zone else []) + e_inputs
        g += ["\\clearpage", "% Lösungen am Ende des Gesamt (Befund 14); "
              "Kopfzeile „Thema · Lernblatt · Lösungen“",
              "\\einheitenkopf[loesungen][Lösungen]{Lösungen}"] + l_inputs
        dateien[f"{k}-gesamt.tex"] = dok("Lernblatt", g)
        dateien[f"{k}-loesungen.tex"] = dok("Lernblatt · Lösungen", l_inputs)
        return dateien

    def baue(self):
        if self.lernblatt:
            return self.baue_lern()
        log = self.log
        gewaehlt = self.einheiten()
        log(f"EINHEITEN {gewaehlt}")
        zone = self.hauptnummern_zone(gewaehlt)
        einheiten = [(n, self.hauptnummern_einheit(n)) for n in gewaehlt]
        nr = 0
        for h in zone:
            nr += 1
            h.nr = nr
        for _, hs in einheiten:
            for h in hs:
                nr += 1
                h.nr = nr
        # „Prüfe dich“ nur im Lernblatt (Rezept L)
        pruefe = self.pruefe_dich(gewaehlt, einheiten) if self.lernblatt \
            else []
        for h in pruefe:
            nr += 1
            h.nr = nr
        # Zone → erste Nummer der Einheit, die die Voraussetzungszeile nennt;
        # „baut auf“ je Einheit aus denselben Zeilen
        baut_auf = {n: [] for n, _ in einheiten}
        for zeile in self.mappe.fertigkeit_zeilen:
            gilt, n_ziel, h_ziel, grund = self.fertigkeit_ziel(zeile, einheiten)
            if h_ziel is None:
                continue
            for n, _ in einheiten:
                if n in gilt and fertigkeit_name(zeile) not in baut_auf[n]:
                    baut_auf[n].append(fertigkeit_name(zeile))
            for h in zone:
                if self.zone_zeile(h.kette) == zeile:
                    h.verweis = h_ziel.nr
                    log(f"ZONE-VERWEIS Nr. {h.nr} → Nr. {h_ziel.nr} "
                        f"(Einheit {n_ziel}; {grund})")
        for h in zone:
            if h.verweis is None and not self.schwach:
                log(f"ZONE-VERWEIS Nr. {h.nr}: Fertigkeit nicht in den "
                    "Voraussetzungen der Mappe – kein Verweis")
        if self.schwach:
            for h in zone:
                h.verweis = None
        dateien = {}
        # Zone
        if zone:
            a = ["% Zone „Das kennst du schon“ – aus bank/"
                 f"{self.eintrag}/zone.jsonl (zusammenbau {VERSION})",
                 "\\einheitenkopf[zone][" + ("Das kennst du schon"
                                             if self.lernblatt else
                                             "Kennst du schon") +
                 "]{Das kennst du schon}", "\\setcounter{aufgabe}{0}"]
            if self.schwach:
                a.append("%% TODO Grundvorstellungs-Aufgabe als erste Hauptnummer "
                         "der Zone (2.8) fehlt in der Bank")
            for h in zone:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, "blatt0_a.tex"))
            dateien["blatt0_a.tex"] = a
            l = ["% Lösungen Zone (zusammenbau " + VERSION + ")",
                 "\\einheitenkopf[][" + ("Das kennst du schon" if self.lernblatt
                                         else "Kennst du schon") +
                 "]{Das kennst du schon}", ""]
            for h in zone:
                l += self.satz_loesung(h)
            dateien["blatt0_l.tex"] = l
        # Einheiten
        anzahl = len(einheiten)
        bereiche = []
        for pos, (n, hs) in enumerate(einheiten, 1):
            kopf, titel = self.kopf(n, pos, anzahl, baut_auf.get(n))
            start = hs[0].nr if hs else nr + 1
            wer = f"Einheit {n}" if self.fokus else f"Einheit {pos} von {anzahl}"
            a = [f"% {wer} – {titel} (bank/{self.eintrag}/"
                 f"e{n}.jsonl, zusammenbau {VERSION})"] + kopf
            if self.a.kasten and not self.schwach:
                a += self.kasten(n)
            a.append(f"\\setcounter{{aufgabe}}{{{start - 1}}}")
            for h in hs:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, f"e{n}_a.tex"))
            if self.schwach:
                a.append("")
                a += self.kasten(n)
            dateien[f"e{n}_a.tex"] = a
            kopf_l = (f"Einheit {n} · {titel}" if self.fokus
                      else f"Einheit {pos} von {anzahl} · {titel}")
            l = [f"% Lösungen {wer} – {titel} (zusammenbau {VERSION})",
                 f"\\einheitenkopf{{{klar(kopf_l)}}}", ""]
            for h in hs:
                l += self.satz_loesung(h)
            dateien[f"e{n}_l.tex"] = l
            if hs:
                bereiche.append((n, pos, titel, hs[0].nr, hs[-1].nr))
        # Prüfe dich (v0.9): gemischt, ohne Titel; Lösung mit Verweis
        if pruefe:
            a = ["% Prüfe dich – je Verfahrenskette eine Aufgabe, gemischt "
                 f"(zusammenbau {VERSION})",
                 "\\einheitenkopf[pruefe][Prüfe dich]{Prüfe dich}",
                 f"\\setcounter{{aufgabe}}{{{pruefe[0].nr - 1}}}"]
            for h in pruefe:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, "pruefe_a.tex"))
            dateien["pruefe_a.tex"] = a
            l = [f"% Lösungen Prüfe dich (zusammenbau {VERSION})",
                 "\\einheitenkopf{Prüfe dich}", ""]
            for h in pruefe:
                l += self.satz_loesung(h)
            dateien["pruefe_l.tex"] = l
        dateien.update(self.rahmen(zone, einheiten, bereiche, pruefe))
        # Vorspann: Satz des Kompetenzblatts, Lernblatt-Ergänzung, Zeichen
        texte = [z for v in dateien.values() for z in v]
        zeichen, self.zeichen = zeichen_vorspann(texte)
        vorspann = VORSPANN.rstrip("\n").split("\n")
        vorspann = vorspann[:-1] + VORSPANN_LERN.split("\n") + (
            ["% Zeichen dieses Blatts, die Latin Modern nicht hat"] + zeichen
            if zeichen else []) + vorspann[-1:]
        dateien["vorspann.tex"] = vorspann
        log(f"ZEICHEN Ersatz im Vorspann: {''.join(self.zeichen) or '–'}")
        log(f"AUFTRAG {len(self.auftrag_doppelt)} Hauptnummern mit einem "
            "Auftragssatz in mehr als einer Teilaufgabe; Hinweis AUFTRAG-SATZ "
            f"{len(self.satz_doppelt)} Sätze")
        for name, zeilen in sorted(dateien.items()):
            if not name.endswith("_a.tex"):
                continue
            for zeile in zeilen:
                if not zeile.startswith("%") and BANKWORT.search(zeile):
                    log(f"BANKWORT „{BANKWORT.search(zeile).group(0)}“ in "
                        f"{name}: {zeile[:80]}")
        return dateien

    def rahmen(self, zone, einheiten, bereiche, pruefe=()):
        th = klar(self.thema)
        kopf = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}",
                "\\input{vorspann}"]
        dateien = {}
        k = self.kennung

        def dok(blatt, rumpf, vorspann=()):
            # Befund 2: Fußzeile nur Kennung (links) und Seite; Thema,
            # Blattart und Einheit stehen in der Kopfzeile
            z = kopf + list(vorspann) + ["\\begin{document}",
                                         f"\\blattkopf*{{{th}}}{{{blatt}}}{{{k}}}"]
            if self.schwach and not blatt.endswith("Lösungen"):
                z.append("\\weit")
            return z + rumpf + ["\\end{document}"]

        def nummern(a, b):
            return f"Nr.~{a}" if a == b else f"Nr.~{a}–{b}"

        verz_e = [f"\\verz{{e{n}}}{{{pos} {klar(t)} ({nummern(a, b)})}}"
                  for n, pos, t, a, b in bereiche]
        e_inputs = []
        for i, (n, _) in enumerate(einheiten):
            if i:
                e_inputs.append("\\clearpage")
            e_inputs.append(f"\\input{{e{n}_a}}")
        l_inputs = []
        if zone:
            l_inputs.append("\\input{blatt0_l}")
        for n, _ in einheiten:
            if l_inputs:
                l_inputs.append("\\bigskip")
            l_inputs.append(f"\\input{{e{n}_l}}")
        if self.fokus:
            rumpf = []
            if zone:
                rumpf += ["\\input{blatt0_a}", "\\clearpage"]
            rumpf += e_inputs
            dateien[f"{k}.tex"] = dok(f"Fokus {klar(self.fokus)}", rumpf)
            dateien[f"{k}-loesungen.tex"] = dok(
                f"Fokus {klar(self.fokus)} · Lösungen", l_inputs)
            return dateien
        # Lernblatt v0.9 (Befund 1, 2): Kopf „Thema · Lernblatt“ in jedem
        # Dokument, dazu die Kurzform der Einheit; schwach wie bisher
        lb = self.lernblatt
        if zone:
            dateien[f"{k}-blatt0.tex"] = dok(
                "Lernblatt" if lb else "Kennst du schon", ["\\input{blatt0_a}"])
        for pos, (n, _) in enumerate(einheiten, 1):
            dateien[f"{k}-e{n}.tex"] = dok("Lernblatt" if lb else
                                           f"Einheit {pos}",
                                           [f"\\input{{e{n}_a}}"])
        schluss = ["\\input{abhaken}"]
        verz_l = list(verz_e)
        if pruefe:
            verz_l.append(f"\\verz{{pruefe}}{{Prüfe dich "
                          f"({nummern(pruefe[0].nr, pruefe[-1].nr)})}}")
            schluss = ["\\clearpage", "\\input{pruefe_a}", "\\input{abhaken}"]
            l_inputs += ["\\bigskip", "\\input{pruefe_l}"]
        verz_l.append("\\verz{abhaken}{Das kann ich}")
        dateien[f"{k}.tex"] = dok(
            "Lernblatt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_l) + "}"]
            + e_inputs + schluss)
        verz_g = list(verz_l)
        g_rumpf = []
        if zone:
            verz_g.insert(0, "\\verz{zone}{" + ("Das kennst du schon" if lb
                                                else "Kennst du schon")
                          + f" ({nummern(zone[0].nr, zone[-1].nr)})}}")
            g_rumpf = ["\\input{blatt0_a}", "\\clearpage"]
        dateien[f"{k}-gesamt.tex"] = dok(
            "Lernblatt" if lb else "Gesamt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_g) + "}"]
            + g_rumpf + e_inputs + schluss,
            vorspann=["\\def\\mitzone{1}"] if zone else [])
        dateien[f"{k}-loesungen.tex"] = dok(
            "Lernblatt · Lösungen" if lb else "Lösungen", l_inputs)
        if lb:
            dateien["abhaken.tex"] = self.das_kann_ich(zone, einheiten,
                                                       bereiche)
            return dateien
        # Abhakseite: je Ich-kann-Satz eine Zeile; „– weiter“ zählt zur
        # Nummer, deren Fortsetzung sie ist (14–15)

        def abhak(hs):
            aus = []
            for h in hs:
                if h.weiter:
                    continue
                folgen = [x for x in hs if x.erster is h and x.weiter]
                nrn = str(h.nr) + (f"–{folgen[-1].nr}" if folgen else "")
                aus.append(f"\\abhak{{{nrn}}}{{{klar(h.titel)}}}")
            return aus
        ab = ["% Abhakseite „Das kann ich“ – Zone nur im Gesamt (\\mitzone)",
              "\\begin{abhakseite}"]
        if zone:
            ab += ["\\ifdefined\\mitzone", "\\abhakgruppe{Kennst du schon}"]
            ab += abhak(zone)
            ab.append("\\fi")
        for (n, hs), (_, pos, titel, _, _) in zip(
                [e for e in einheiten if e[1]], bereiche):
            ab.append(f"\\abhakgruppe{{Einheit {pos} · {klar(titel)}}}")
            ab += abhak(hs)
        ab.append("\\end{abhakseite}")
        dateien["abhaken.tex"] = ab
        return dateien


    def das_kann_ich(self, zone, einheiten, bereiche):
        """„Das kann ich“ unter „Prüfe dich“ (v0.9, ersetzt die Abhakseite im
        Lernblatt): je Kette die Ich-kann-Zeile der Kette mit ihren Nummern;
        im Gesamt davor je Fertigkeit der Zone ihre Zeile."""
        def bereich(nrn):
            nrn = sorted(nrn)
            teile, i = [], 0
            while i < len(nrn):
                j = i
                while j + 1 < len(nrn) and nrn[j + 1] == nrn[j] + 1:
                    j += 1
                teile.append(str(nrn[i]) if i == j else f"{nrn[i]}–{nrn[j]}")
                i = j + 1
            return ", ".join(teile)

        def zeilen(hs, einheit):
            je = {}
            for h in hs:
                je.setdefault(h.kette.casefold(), []).append(h)
            aus = []
            for kk, gruppe in je.items():
                h0 = gruppe[0]
                kette = h0.kette
                if einheit == 0:
                    ersatz = next((h.titel for h in gruppe
                                   if h.lage == "zone"), h0.titel)
                else:
                    ersatz = next((h.titel for h in gruppe if h.lage in (
                        "leiter", "erkennung", "ohne") and not h.weiter),
                        h0.titel)
                titel, _ = self.ich_kann(einheit, kette, "", ersatz)
                aus.append(f"\\abhak{{{bereich(h.nr for h in gruppe)}}}"
                           f"{{{klar(titel)}}}")
            return aus
        ab = ["% „Das kann ich“ (zusammenbau " + VERSION + "): je Kette eine "
              "Zeile – Zone nur im Gesamt (\\mitzone)",
              "\\begin{lbdaskannich}"]
        if zone:
            ab += ["\\ifdefined\\mitzone", "\\abhakgruppe{Das kennst du schon}"]
            ab += zeilen(zone, 0)
            ab.append("\\fi")
        for (n, hs), (_, pos, titel, _, _) in zip(
                [e for e in einheiten if e[1]], bereiche):
            ab.append(f"\\abhakgruppe{{Einheit {pos} · {klar(titel)}}}")
            ab += zeilen(hs, n)
        ab.append("\\end{lbdaskannich}")
        return ab


# --- Rezept Heft (v0.4) ------------------------------------------------------
#
# Prüfungsheft nach Themen aus mehreren Einträgen (Beschluss des Lehrers vom
# 28.09.): je Kette zwei Lagen – Anlauf (Vorstufe, ein Grundfall, eine
# Sprosse mit dem häufigsten Fallstrick, ohne Prüfkennung) und danach alle
# Prüfungshöhen der Kette im gewählten Prüfungsprofil (alle Varianten, mit
# Prüfkennung, Sternchen wie im Original). --nur-basis: nur Originale aus
# dem Basisteil (OS/FOR/EBR, id mit „-B“), ohne Anlauf.

HEFT_PROFIL = {
    "msa": "P10 (MSA: OS, FOR, EBR, GYM)",
    "abitur-gk": "Abitur, grundlegendes Niveau (GK)",
    "abitur-lk": "Abitur, erhöhtes Niveau (LK)",
    "fhr": "FHR",
}
MSA_PAPIER = {"OS", "FOR", "EBR", "GYM"}
BASIS_PAPIER = {"OS", "FOR", "EBR"}
FALLSTRICK = re.compile(r"Fallstrick|Falle|Fehler|verwechs|vertausch|"
                        r"Vorzeichen|Klammer|Sonderfall|negativ|Null\b",
                        re.I)
KATALOGE = ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv",
            "msa/msa-katalog-gym.csv", "abitur/abi-katalog.csv",
            "abitur/iqb-katalog.csv", "fhr/fhr-katalog.csv"]


def profil_von(z):
    """Prüfungsprofil einer Bankzeile: aus original.papier, sonst aus der
    Prüfkennung im Aufgabentext; None, wenn die Zeile keins trägt."""
    o = z.get("original") or {}
    p = o.get("papier")
    if p:
        if p in MSA_PAPIER:
            return "msa"
        if p in ("A", "B", "C"):
            return "fhr"
        if re.search(r"-(ga|gk)(-|$)", p):
            return "abitur-gk"
        return "abitur-lk"
    m = KENNUNG.search(z.get("aufgabe", ""))
    if not m:
        return None
    k = m.group(0)
    if "P10" in k:
        return "msa"
    if "FHR" in k:
        return "fhr"
    return "abitur-gk" if "GK" in k else "abitur-lk"


def ist_basis(z):
    o = z.get("original") or {}
    return (o.get("papier") in BASIS_PAPIER
            and re.search(r"-(OS|FOR|EBR)-B\d", o.get("id", "")) is not None)


def lies_kataloge(log):
    """{id: {punkte, stern, datei}} aus den Prüfungskatalogen von
    mathe-nachhilfe (für Sternchen und Punkte der Originale)."""
    wurzeln = []
    if os.environ.get("MATHE_NACHHILFE"):
        wurzeln.append(Path(os.environ["MATHE_NACHHILFE"]))
    wurzeln += [WURZEL.parent / "mathe-nachhilfe",
                WURZEL.parent / "hz-0801" / "mathe-nachhilfe"]
    kat = {}
    for w in wurzeln:
        if not (w / "msa").is_dir():
            continue
        for rel in KATALOGE:
            p = w / rel
            if not p.is_file():
                log(f"KATALOG fehlt: {rel}")
                continue
            with open(p, encoding="utf-8", newline="") as f:
                kopf = f.readline()
                f.seek(0)
                for zeile in csv.DictReader(f, delimiter=";" if ";" in kopf
                                            else ","):
                    kat[zeile["id"]] = {"punkte": zeile.get("punkte") or "",
                                        "stern": zeile.get("stern") or "",
                                        "datei": rel,
                                        "typ": zeile.get("typ") or "",
                                        "jahr": zeile.get("jahr") or "",
                                        "papier": zeile.get("papier") or ""}
        log(f"KATALOGE aus {w}: {len(kat)} Zeilen")
        return kat
    log("KATALOGE nicht gefunden (mathe-nachhilfe neben dem Repo klonen): "
        "keine Sternchen, keine Punkte")
    return kat


def ohne_kennung(z):
    """Kopie der Zeile ohne Prüfkennung (Anlauf: ohne Kennzeichnung)."""
    if not KENNUNG.search(z["aufgabe"]):
        return z
    neu = dict(z)
    neu["aufgabe"] = KENNUNG.sub("", z["aufgabe"]).rstrip()
    neu["kennung_entfernt"] = True
    return neu


class HeftBau:
    """Rezept H: ein Heft aus mehreren Einträgen, je Kette Anlauf und
    Prüfungslage. Die Hauptnummern laufen über das ganze Heft."""

    def __init__(self, args, log):
        self.a = args
        self.log = log
        self.profil = args.heft
        self.basis = args.nur_basis
        self.kennung = args.kennung
        self.titel = args.titel
        self.kat = lies_kataloge(log)
        self.eintraege = []      # (eintrag, thema, {n: zeilen})
        self.fehlend = []
        for e in args.eintraege:
            bank = WURZEL / "bank" / e
            if not bank.is_dir():
                log(f"FEHLT bank/{e}/ – Eintrag entfällt")
                self.fehlend.append(e)
                continue
            mappe = Mappe(WURZEL / "mappen" / f"{e}.md", log)
            einheiten = {}
            for p in sorted(bank.glob("e*.jsonl"),
                            key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
                if re.fullmatch(r"e\d+", p.stem):
                    einheiten[int(p.stem[1:])] = lies_jsonl(p)
            self.eintraege.append((e, mappe.thema or e, einheiten))
        self.stern = set()
        self.reihenfolge = []
        self.info = {}           # id -> {lage, original, punkte, stern}

    def ist_pruefung(self, z):
        if self.basis:
            return profil_von(z) == "msa" and ist_basis(z)
        return profil_von(z) == self.profil

    def anlauf(self, zeilen, pruef, wo):
        """Vorstufe, Grundfall, Sprosse mit Fallstrick – je eine Zeile, ohne
        Original, kleinste Variante."""
        log = self.log
        frei = [z for z in zeilen if not z.get("original")
                and z["id"] not in pruef and z["hoehe"] != "pflicht"]
        if not frei:
            log(f"ANLAUF {wo}: keine Zeile ohne Original – entfällt")
            return []

        def erste(zz):
            return sorted(zz, key=lambda z: (z["sprosse"], z["variante"]))[0]

        aus = []
        grund = [z for z in frei if z["hoehe"] == "grundfall"]
        g_sprosse = min(z["sprosse"] for z in grund) if grund else None
        vor = [z for z in frei if z["hoehe"] == "vorstufe"
               and (g_sprosse is None or z["sprosse"] < g_sprosse)]
        if vor:
            w = erste(vor)
            aus.append(w)
            log(f"AUSWAHL {w['id']} – {wo}: Anlauf, Vorstufe")
        if grund:
            w = erste(grund)
            aus.append(w)
            log(f"AUSWAHL {w['id']} – {wo}: Anlauf, Grundfall")
        rest = [z for z in frei if z["hoehe"] == "sprosse"
                and (g_sprosse is None or z["sprosse"] > g_sprosse)]
        if rest:
            treffer = [z for z in rest if FALLSTRICK.search(z.get("merkmal", ""))]
            if treffer:
                w = erste(treffer)
                grund_w = f"Fallstrick im Merkmal („{w['merkmal'][:50]}“)"
            else:
                w = erste(rest)
                grund_w = ("kein Fallstrick im Merkmal; erste Sprosse nach "
                           "dem Grundfall")
            aus.append(w)
            log(f"AUSWAHL {w['id']} – {wo}: Anlauf, Sprosse – {grund_w}")
        if not aus:
            w = erste(frei)
            aus.append(w)
            log(f"AUSWAHL {w['id']} – {wo}: Anlauf, einzige Sprosse "
                "(Kette ohne Grundfall)")
        return [ohne_kennung(z) for z in aus]

    def hauptnummern(self, eintrag, einheiten):
        log = self.log
        aus = []
        for n in sorted(einheiten):
            gruppen = {}
            for nr, name, art, zeilen in ketten_von(einheiten[n]):
                gruppen.setdefault(name, []).append((nr, art, zeilen))
            for name, teile in gruppen.items():
                zeilen = [z for _, _, zz in teile for z in zz]
                wo = f"{eintrag} e{n} „{name}“"
                pruef = [z for z in zeilen if self.ist_pruefung(z)]
                if not pruef:
                    log(f"WEG {wo} – keine Prüfungshöhe im Profil "
                        f"{'basis' if self.basis else self.profil}")
                    continue
                pruef_ids = {z["id"] for z in pruef}
                if not self.basis:
                    kette = [z for nr, art, zz in teile if art != "pflicht"
                             for z in zz]
                    anl = self.anlauf(kette, pruef_ids, wo)
                    if anl:
                        h = Hauptnummer(f"{name} – Anlauf", anl, "anlauf",
                                        name, n)
                        aus.append(h)
                        for z in anl:
                            self.info[z["id"]] = {"lage": "anlauf"}
                folge = sorted(pruef, key=lambda z: (z["sprosse"], z["variante"],
                                                     z["kette_nr"]))
                for z in folge:
                    o = z.get("original") or {}
                    k = self.kat.get(o.get("id"), {})
                    st = k.get("stern") == "ja"
                    if st:
                        self.stern.add(z["id"])
                    self.info[z["id"]] = {"lage": "pruefung",
                                          "original": o.get("id"),
                                          "punkte": k.get("punkte") or None,
                                          "stern": st}
                    log(f"AUSWAHL {z['id']} – {wo}: Prüfungshöhe "
                        f"({o.get('id') or 'Kennung im Text'}"
                        + (", Stern" if st else "") + ")")
                stuecke = teile_nach_mass(folge)
                if len(stuecke) > 1:
                    log(f"TEILUNG {wo}: {len(folge)} Prüfungsaufgaben in "
                        f"{len(stuecke)} Hauptnummern an Sprossengrenzen (2.3 g)")
                for i, t in enumerate(stuecke):
                    titel = f"{name} – Prüfungsaufgaben" + (" – weiter" if i else "")
                    aus.append(Hauptnummer(titel, t, "pruefung", name, n,
                                           weiter=bool(i)))
        return aus

    def satz(self, h):
        # gleichungsraster nur für reine Gleichungen; Text (Sachaufgabe im
        # Raster) liefe als \\text{…} in einer Zeile über die Spalte hinaus
        folge = []
        for z in h.folge:
            a = z["aufgabe"].strip()
            if (z.get("form") == "gleichungsraster" and "$" not in a
                    and not re.search(r"[A-Za-zÄÖÜäöüß]{3,}",
                                      re.sub(r"\\[A-Za-z]+", "", a))):
                # reine Gleichung ohne $ (x^2 = 81): als Mathe setzen
                z = dict(z, aufgabe=f"${a}$")
                self.log(f"FORM {z['id']} (Nr. {h.nr}): Gleichung ohne $ "
                         "im Raster als Mathe gesetzt")
            if (z.get("form") == "gleichungsraster"
                    and gl_inhalt(z["aufgabe"]).startswith("\\text{")):
                z = dict(z, form="teil")
                self.log(f"FORM {z['id']} (Nr. {h.nr}): gleichungsraster mit "
                         "Text → teile")
            folge.append(z)
        h.folge = folge
        aus = [f"\\begin{{aufgabe}}{{{klar(h.titel)}}}"]
        aus += teile_normal(h.folge, self.stern)
        aus.append("\\end{aufgabe}")
        h.buchstaben = [(buchstabe(i), z) for i, z in enumerate(h.folge)]
        n_teil = len(h.buchstaben)
        n_graf = sum(1 for z in h.folge if z.get("grafik"))
        if n_teil > 26:
            self.log(f"FEHLER Nr. {h.nr}: {n_teil} Teilaufgaben > 26 (\\alph)")
        if (n_graf == 0 and n_teil > 12) or (n_graf > 0 and n_teil > 6):
            self.log(f"WARNUNG Nr. {h.nr}: {n_teil} Teilaufgaben, {n_graf} "
                     "mit Grafik – über dem Halbseitenmaß (2.3 g)")
        return aus

    satz_loesung = Bau.satz_loesung

    def baue(self):
        dateien = {}
        teile = []
        nr = 0
        for i, (e, thema, einheiten) in enumerate(self.eintraege, 1):
            hs = self.hauptnummern(e, einheiten)
            if not hs:
                self.log(f"LEER {e}: keine Kette mit Prüfungshöhe – Eintrag "
                         "entfällt im Heft")
                continue
            for h in hs:
                nr += 1
                h.nr = nr
            teile.append((i, e, thema, hs))
        self.teile = teile
        for i, e, thema, hs in teile:
            a = [f"% {thema} – bank/{e}/ (zusammenbau {VERSION}, Heft)",
                 f"\\einheitenkopf[t{i}]{{{klar(thema)}}}",
                 f"\\setcounter{{aufgabe}}{{{hs[0].nr - 1}}}"]
            for h in hs:
                a.append("")
                if h.art == "anlauf":
                    a.append("% Anlauf (ohne Prüfkennung)")
                a += self.satz(h)
                self.reihenfolge.append((h, f"{e}_a.tex"))
            dateien[f"{e}_a.tex"] = a
            l = [f"% Lösungen {thema} (zusammenbau {VERSION}, Heft)",
                 f"\\einheitenkopf{{{klar(thema)}}}", ""]
            for h in hs:
                l += self.satz_loesung(h)
            dateien[f"{e}_l.tex"] = l
        dateien.update(self.rahmen(teile))
        return dateien

    def rahmen(self, teile):
        k = self.kennung
        th = self.titel
        weit = self.profil == "msa"
        kopf = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}"]

        def dok(blatt, rumpf):
            fuss = f"{th} · {blatt} · {k}"
            if self.stern and not blatt.endswith("Lösungen"):
                fuss += " · $\\star$ = Original mit Sternchen (nur FOR)"
            z = kopf + ["\\begin{document}",
                        f"\\blattkopf*{{{klar(th)}}}{{{blatt}}}{{{klar(fuss)}}}"]
            if weit and not blatt.endswith("Lösungen"):
                z.append("\\weit")
            return z + rumpf + ["\\end{document}"]

        verz = []
        for i, e, thema, hs in teile:
            a, b = hs[0].nr, hs[-1].nr
            nrn = f"Nr.~{a}" if a == b else f"Nr.~{a}–{b}"
            verz.append(f"\\verz{{t{i}}}{{{klar(thema)} ({nrn})}}")
        a_in, l_in = [], []
        for j, (i, e, thema, hs) in enumerate(teile):
            if j:
                a_in.append("\\clearpage")
                l_in.append("\\bigskip")
            a_in.append(f"\\input{{{e}_a}}")
            l_in.append(f"\\input{{{e}_l}}")
        name = "Prüfungsheft Basis" if self.basis else "Prüfungsheft"
        rumpf = (["\\verzeichniszeile{" + " \\verztrenn ".join(verz) + "}"]
                 if verz else []) + a_in
        return {f"{k}.tex": dok(name, rumpf),
                f"{k}-loesungen.tex": dok(f"{name} · Lösungen", l_in)}


# --- Rezept Prüfungs-Fokus (v0.6) -------------------------------------------
#
# Beschluss des Lehrers vom 28.09.: ein kleines Prüfungsheft zu genau einer
# Kette. Anlauf (Vorstufe, ein Grundfall, eine Sprosse mit Fallstrick, ohne
# Prüfkennung) wie im Heft, danach alle Prüfungshöhen der Kette im Profil
# (alle Varianten, alle Originale, Prüfkennung kurz, Sternchen), am Ende der
# Merkkasten der Einheit aus der Mappe (wie --kasten).

FOKUS_PROFIL_WORT = {"msa": "MSA", "abitur-gk": "Abitur GK",
                     "abitur-lk": "Abitur LK", "fhr": "FHR"}
FOKUS_MARKE = {"msa": "P10", "abitur-gk": "Abitur GK",
               "abitur-lk": "Abitur LK", "fhr": "FHR"}


class FokusPruefBau(HeftBau):
    """Rezept P: eine Kette einer Einheit, Anlauf und Prüfungslage."""

    def __init__(self, args, log):
        self.a = args
        self.log = log
        self.profil = args.heft
        self.basis = False
        self.kennung = args.kennung
        self.kat = lies_kataloge(log)
        self.eintrag = args.eintrag
        bank = WURZEL / "bank" / self.eintrag
        if not bank.is_dir():
            sys.exit(f"bank/{self.eintrag}/ fehlt")
        self.mappe = Mappe(WURZEL / "mappen" / f"{self.eintrag}.md", log)
        self.thema = self.mappe.thema or self.eintrag
        self.e = {}
        for p in sorted(bank.glob("e*.jsonl"),
                        key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
            if re.fullmatch(r"e\d+", p.stem):
                self.e[int(p.stem[1:])] = lies_jsonl(p)
        self.stern = set()
        self.reihenfolge = []
        self.info = {}
        self.kette_wunsch = args.fokus_pruefung
        self.einheit, self.kette = self.waehle()
        self.titel = (f"{self.thema} · {self.kette} · Prüfungs-Fokus "
                      f"{FOKUS_PROFIL_WORT[self.profil]}")
        self.kasten_status = None
        self.pruefwort = None

    def zeilen_der_kette(self, n, name):
        return [z for z in self.e[n] if z["kette"].casefold() == name.casefold()]

    def waehle(self):
        """(Einheit, Kettenname wie in der Bank): --einheiten n, sonst die
        erste Einheit, in der die Kette Prüfungshöhen im Profil hat."""
        log, k = self.log, self.kette_wunsch
        if self.a.einheiten:
            wahl = [int(x) for x in self.a.einheiten.split(",") if x.strip()]
            if len(wahl) != 1 or wahl[0] not in self.e:
                sys.exit(f"--einheiten: genau eine Einheit aus bank/"
                         f"{self.eintrag}/ ({sorted(self.e)})")
            kandidaten = wahl
        else:
            kandidaten = sorted(self.e)
        for n in kandidaten:
            zz = self.zeilen_der_kette(n, k)
            if zz and any(self.ist_pruefung(z) for z in zz):
                log(f"EINHEIT e{n} – Kette „{zz[0]['kette']}“ mit "
                    f"{sum(self.ist_pruefung(z) for z in zz)} Prüfungshöhen "
                    f"im Profil {self.profil}"
                    + (" (--einheiten)" if self.a.einheiten else
                       " (erste Einheit mit Prüfungshöhen)"))
                return n, zz[0]["kette"]
        namen = sorted({z["kette"] for n in kandidaten for z in self.e[n]})
        sys.exit(f"Kette „{k}“ ohne Prüfungshöhe im Profil {self.profil} in "
                 f"Einheit(en) {kandidaten}; vorhanden: " + "; ".join(namen))

    def kopf(self):
        n = self.einheit
        info = self.mappe.einheiten.get(n)
        titel = info["titel"] if info else f"Einheit {n}"
        aus = [f"\\einheitenkopf[e{n}]{{{klar(f'Einheit {n} · {titel}')}}}"]
        os_, gym, _ = marke_zerlegen(info["marken"] if info else None)
        zm = zeitmarke(os_, gym, None) if self.profil == "msa" else None
        # Prüfungswort nur für das Profil des Fokus, gezählt über die Typen
        # der Originale dieser Kette (nicht der ganzen Einheit)
        self.pruefwort = pruefwort_zahl(FOKUS_MARKE[self.profil],
                                        self.zeilen_der_kette(n, self.kette),
                                        self.log)
        teile = [t for t in (zm, self.pruefwort) if t]
        if teile:
            aus.append("\\zweigzeile{" + " · ".join(teile) + "}")
        self.log(f"KOPF Einheit {n}: „{titel}“; Zeitmarke „{zm}“, "
                 f"Prüfungswort „{self.pruefwort}“")
        return aus, titel

    def kasten(self):
        n = self.einheit
        zeilen = self.mappe.kasten.get(n)
        if not zeilen:
            self.kasten_status = "fehlt in der Mappe"
            self.log(f"KASTEN Einheit {n}: nicht in der Mappe lesbar – entfällt")
            return []
        self.kasten_status = f"{len(zeilen)} Zeilen"
        aus = ["", "\\medskip"]
        if len(zeilen) > 5:
            aus.append(f"%% Merkkasten Einheit {n}: {len(zeilen)} Zeilen, "
                       "Vorgabe höchstens fünf (3.1) – ungekürzt")
            self.kasten_status += " (über fünf)"
        inhalt = [re.sub(r"\s{3,}", r" \\quad ", klar(z.replace("&", "und")))
                  for z in zeilen]
        aus.append("\\uebersichtskasten{" + " \\\\ ".join(inhalt) + "}")
        self.log(f"KASTEN Einheit {n}: {self.kasten_status}")
        return aus

    def baue(self):
        n, name = self.einheit, self.kette
        zeilen = self.zeilen_der_kette(n, name)
        wo = f"{self.eintrag} e{n} „{name}“"
        pruef = [z for z in zeilen if self.ist_pruefung(z)]
        pruef_ids = {z["id"] for z in pruef}
        hs = []
        kette = [z for z in zeilen if z["hoehe"] != "pflicht"]
        anl = self.anlauf(kette, pruef_ids, wo)
        if anl:
            hs.append(Hauptnummer(f"{name} – Anlauf", anl, "anlauf", name, n))
            for z in anl:
                self.info[z["id"]] = {"lage": "anlauf"}
        folge = sorted(pruef, key=lambda z: (z["sprosse"], z["variante"],
                                             z["kette_nr"]))
        for z in folge:
            o = z.get("original") or {}
            k = self.kat.get(o.get("id"), {})
            st = k.get("stern") == "ja"
            if st:
                self.stern.add(z["id"])
            self.info[z["id"]] = {"lage": "pruefung", "original": o.get("id"),
                                  "jahr": o.get("jahr"),
                                  "punkte": k.get("punkte") or None,
                                  "stern": st}
            self.log(f"AUSWAHL {z['id']} – {wo}: Prüfungshöhe "
                     f"({o.get('id') or 'Kennung im Text'}"
                     + (", Stern" if st else "") + ")")
        stuecke = teile_nach_mass(folge)
        if len(stuecke) > 1:
            self.log(f"TEILUNG {wo}: {len(folge)} Prüfungsaufgaben in "
                     f"{len(stuecke)} Hauptnummern an Sprossengrenzen (2.3 g)")
        for i, t in enumerate(stuecke):
            hs.append(Hauptnummer(f"{name} – Prüfungsaufgaben"
                                  + (" – weiter" if i else ""), t, "pruefung",
                                  name, n, weiter=bool(i)))
        for i, h in enumerate(hs, 1):
            h.nr = i
        self.hs = hs
        kopf, titel = self.kopf()
        a = [f"% {self.titel} – bank/{self.eintrag}/e{n}.jsonl "
             f"(zusammenbau {VERSION}, Prüfungs-Fokus)"] + kopf
        a.append("\\setcounter{aufgabe}{0}")
        for h in hs:
            a.append("")
            if h.art == "anlauf":
                a.append("% Anlauf (ohne Prüfkennung)")
            a += self.satz(h)
            self.reihenfolge.append((h, f"e{n}_a.tex"))
        a += self.kasten()
        l = [f"% Lösungen {self.titel} (zusammenbau {VERSION})",
             f"\\einheitenkopf{{{klar(f'Einheit {n} · {titel}')}}}", ""]
        for h in hs:
            l += self.satz_loesung(h)
        dateien = {f"e{n}_a.tex": a, f"e{n}_l.tex": l}
        k = self.kennung
        kopf_d = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}"]
        blatt = f"{name} · Prüfungs-Fokus {FOKUS_PROFIL_WORT[self.profil]}"

        def dok(bez, rumpf, loesung=False):
            fuss = f"{self.titel}" + (" · Lösungen" if loesung else "") + f" · {k}"
            if self.stern and not loesung:
                fuss += " · $\\star$ = Original mit Sternchen (nur FOR)"
            z = kopf_d + ["\\begin{document}",
                          f"\\blattkopf*{{{klar(self.thema)}}}{{{klar(bez)}}}"
                          f"{{{klar(fuss)}}}"]
            if self.profil == "msa" and not loesung:
                z.append("\\weit")
            return z + rumpf + ["\\end{document}"]

        dateien[f"{k}.tex"] = dok(blatt, [f"\\input{{e{n}_a}}"])
        dateien[f"{k}-loesungen.tex"] = dok(f"{blatt} · Lösungen",
                                            [f"\\input{{e{n}_l}}"], True)
        return dateien


# --- Rezept Kompetenzblatt (v0.7) -------------------------------------------
#
# Beschluss des Lehrers vom 28.09.: Grundeinheit des Bauens ist das
# Kompetenzblatt – genau eine Kette, 2–4 Seiten, eigene Kennung XXX-K<n>.
# Aufbau: kurze Zone „Das kennst du schon“ (nur Fertigkeiten, die diese
# Kette braucht, 2–4 Aufgaben), die Leiter der Kette von der Vorstufe bis
# zur Prüfungshöhe (je Sprosse eine Hauptnummer mit Variante 1, die
# Prüfungshöhen nach Beschluss d), am Ende der Merkkasten der Einheit;
# Lösungen als eigene Datei. Stern entfällt, das Niveau wird bestellt
# (--niveau for: mit Sternaufgaben, ohne Kennzeichnung; ebr: ohne sie).
# Keine Punkte. Layout nach bau/layout-befunde.md; was mathblatt.sty dafür
# fehlt, steht im Vorspann (vorspann.tex), den der Zusammenbau schreibt.

ICHKANN = WURZEL / "bau" / "regal" / "ich-kann.csv"
KOMPETENZ_JAHRGAENGE = 5      # Prüfungshöhen nur aus den jüngsten fünf Jahrgängen
KOMPETENZ_PRUEF_MIN = 4       # 4–5 Teilaufgaben, wenn es so viele Originale gibt
KOMPETENZ_PRUEF_MAX = 5
ZONE_FERTIGKEITEN = 3         # höchstens drei Fertigkeiten, je eine Aufgabe
TEXTBREITE_CM = 17.4          # A4 mit 18 mm Rand (mathblatt.sty)
KSYS_HOEHE_CM = 7.5           # Koordinatensystem zum Zeichnen höchstens so hoch
BANKWORT = re.compile(r"Anlauf|Prüfungsaufgaben|Sprosse|Vorstufe|Grundfall|"
                      r"Fallstrick|Variante|P10-Form|Prüfungsform|ausgelassen|"
                      r"\bKette\b|Prüfungshöhe")
# Zeichen, die Latin Modern Roman nicht hat (gemessen 28.09. mit fontTools an
# lmroman10-regular.otf über alle Zeichen in bank/ und mappen/, dazu
# naheliegende Verwandte). Im Text setzt der Vorspann sie aus einer
# Ersatzschrift (FreeSerif, DejaVu Serif, Cambria, Segoe UI Symbol – die
# erste vorhandene), in Mathe als Mathebefehl; Hoch- und Tiefzeichen in
# Mathe als Glyphe der Ersatzschrift.
LM_FEHLT = ("ʳʸˣαβγδελμπσφϱᵀᵃᵈᵏᵗᶜ′″⁰⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₀₁₂₃₄₅₆₈₋ℓℕℚℝℤ↔↦⇒⇔∈∘∙∠∥∨"
            "∩∪∫≈≙≠≤≥⊂⊥①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑮⑯⑰⑲⑳□☆☐✓㉑㉒㉓"
            "ΔΣΩθρτωξηζνκχψ∞∉∅∑∆∇≡∼∝⊆⊇∧⇐↑↓⟂✗⁾⁽₍₎")
MATHE_ZEICHEN = {
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta",
    "ε": r"\varepsilon", "λ": r"\lambda", "μ": r"\mu", "π": r"\pi",
    "σ": r"\sigma", "φ": r"\varphi", "ϱ": r"\varrho", "θ": r"\theta",
    "ρ": r"\rho", "τ": r"\tau", "ω": r"\omega", "ξ": r"\xi", "η": r"\eta",
    "ζ": r"\zeta", "ν": r"\nu", "κ": r"\kappa", "χ": r"\chi", "ψ": r"\psi",
    "Δ": r"\Delta", "Σ": r"\Sigma", "Ω": r"\Omega",
    "′": r"{}^{\prime}", "″": r"{}^{\prime\prime}", "ℓ": r"\ell",
    "ℕ": r"\mathbb{N}", "ℚ": r"\mathbb{Q}", "ℝ": r"\mathbb{R}",
    "ℤ": r"\mathbb{Z}", "↔": r"\leftrightarrow", "↦": r"\mapsto",
    "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow", "⇐": r"\Leftarrow",
    "∈": r"\in", "∉": r"\notin", "∘": r"\circ", "∙": r"\cdot",
    "∠": r"\angle", "∥": r"\parallel", "∨": r"\vee", "∧": r"\wedge",
    "∩": r"\cap", "∪": r"\cup", "∫": r"\int", "≈": r"\approx",
    "≙": r"\mathrel{\widehat{=}}", "≠": r"\neq", "≤": r"\leq", "≥": r"\geq",
    "⊂": r"\subset", "⊆": r"\subseteq", "⊇": r"\supseteq", "⊥": r"\perp",
    "⟂": r"\perp", "∞": r"\infty", "∅": r"\emptyset", "∑": r"\sum",
    "∆": r"\Delta", "∇": r"\nabla", "≡": r"\equiv", "∼": r"\sim",
    "∝": r"\propto", "↑": r"\uparrow", "↓": r"\downarrow",
    "□": r"\square", "☐": r"\square", "✓": r"\checkmark",
}
IMPERATIV = re.compile(
    r"^(Berechne|Bestimme|Zeige|Ergänze|Prüfe|Runde|Gib|Begründe|Zeichne|"
    r"Trage|Fülle|Schreibe|Lies|Kreuze|Löse|Markiere|Beschreibe|Nenne|"
    r"Entscheide|Stimmt|Wie|Welche[rsnm]?|Was|Wo|Wann|Womit|Um|An|Ist|Sind|"
    r"Hat|Haben|Kann|Gibt|Drücke|Leite|Gehe|Notiere|Erkläre|Vergleiche|"
    r"Ordne|Setze|Teile|Wähle|Überprüfe|Untersuche|Stelle|Rechne|Finde|"
    r"Kontrolliere|Bilde|Verbinde|Welchen|Warum|Wieso|Weshalb|Wer|Wie viel)\b")
FRAGEWORT_KLEIN = re.compile(
    r"^(wie|welche[rsnm]?|was|wo|wann|womit|um|an|ist|sind|hat|gibt|stimmt|"
    r"warum|wer|wie viel|kann)\b")


def lies_ichkann():
    """{(eintrag, einheit, kette casefold, sprosse): (ich_kann, anweisung)}
    aus bau/regal/ich-kann.csv; sprosse „“ = Titel der Kette, „p“ = die
    Prüfungshöhen, Zahl = Sprosse; Einheit 0 = Fertigkeit der Zone."""
    aus = {}
    if not ICHKANN.exists():
        return aus
    with open(ICHKANN, encoding="utf-8", newline="") as f:
        zeilen = [z for z in f if z.strip() and not z.startswith("#")]
    for z in csv.DictReader(zeilen, delimiter=";"):
        try:
            n = int(z["einheit"])
        except (TypeError, ValueError):
            continue
        aus[(z["eintrag"].strip(), n, z["kette"].strip().casefold(),
             (z.get("sprosse") or "").strip())] = (
            (z.get("ich_kann") or "").strip(),
            (z.get("anweisung") or "").strip())
    return aus


def lies_titel():
    """{(eintrag, einheit, kette casefold, sprosse): titel} aus der Spalte
    titel von bau/regal/ich-kann.csv (v1.0): der Titel im Infinitiv, wo der
    Ich-kann-Satz keinen ergibt („Ich erkenne …“, „Ich finde …“)."""
    aus = {}
    if not ICHKANN.exists():
        return aus
    with open(ICHKANN, encoding="utf-8", newline="") as f:
        zeilen = [z for z in f if z.strip() and not z.startswith("#")]
    for z in csv.DictReader(zeilen, delimiter=";"):
        titel = (z.get("titel") or "").strip()
        try:
            n = int(z["einheit"])
        except (TypeError, ValueError):
            continue
        if titel:
            aus[(z["eintrag"].strip(), n, z["kette"].strip().casefold(),
                 (z.get("sprosse") or "").strip())] = titel
    return aus


def kennung_kompetenz(k, z=None):
    """Prüfkennung für Kompetenzblätter (Beschluss c): „P10 ’24“, anderes
    Papier dahinter („P10 ’26 F“); „Abi ’23“, „Abi ’23 LK“; „FHR ’25“.
    Ohne Stern (Beschluss b)."""
    innen = k.strip()[1:-1].strip()
    m = re.fullmatch(r"P10 (\d{4}) (OS|FOR|EBR|GYM)", innen)
    if m:
        p = {"OS": "", "FOR": " F", "EBR": " E", "GYM": " G"}[m.group(2)]
        return f"P10 ’{m.group(1)[2:]}{p}"
    m = re.fullmatch(r"Abitur (\d{4}) (GK|LK)", innen)
    if m:
        return f"Abi ’{m.group(1)[2:]}" + (" LK" if m.group(2) == "LK" else "")
    m = re.fullmatch(r"FHR (\d{4})", innen)
    if m:
        return f"FHR ’{m.group(1)[2:]}"
    return ""


def schuetze(t):
    """Mathe ($…$) und Befehle samt Argumenten durch Platzhalter ersetzen,
    damit Zerlegen an Doppelpunkt, Gedankenstrich und Satzende nichts
    darin trifft. (text, [stücke])"""
    st, aus, i = [], [], 0

    def ph(s):
        st.append(s)
        return f"\x00{len(st) - 1}\x01"

    while i < len(t):
        c = t[i]
        if c == "$" and (i == 0 or t[i - 1] != "\\"):
            j = i + 1
            while j < len(t) and not (t[j] == "$" and t[j - 1] != "\\"):
                j += 1
            aus.append(ph(t[i:j + 1]))
            i = j + 1
        elif c == "\\" and re.match(r"\\[A-Za-z]+", t[i:]):
            m = re.match(r"\\[A-Za-z]+\*?", t[i:])
            k = i + m.end()
            while k < len(t) and t[k] in "[{":
                k = BP.klammer(t, k)
            aus.append(ph(t[i:k]))
            i = k
        else:
            aus.append(c)
            i += 1
    return "".join(aus), st


def zurueck(s, st):
    while "\x00" in s:
        s = re.sub(r"\x00(\d+)\x01", lambda m: st[int(m.group(1))], s)
    return s


def schlicht(s):
    """Grobe Druckbreite: Mathe und Befehle ungefähr, für Längenregeln."""
    s = re.sub(r"\$([^$]*)\$", lambda m: re.sub(r"\\[A-Za-z]+|[{}^_]", "",
                                                m.group(1)), s)
    s = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", "", s)
    return re.sub(r"[{}]", "", s).strip()


def befehle_heraus(t, name):
    """Alle Aufrufe \\name[…]{…}… aus t: (rest, [aufrufe])."""
    aus, rest, i = [], [], 0
    muster = re.compile(r"\\" + name + r"(?![A-Za-z])")
    while True:
        m = muster.search(t, i)
        if not m:
            rest.append(t[i:])
            break
        rest.append(t[i:m.start()])
        k = m.end()
        while k < len(t) and t[k] in "[{":
            k = BP.klammer(t, k)
        aus.append(t[m.start():k])
        i = k
    return "".join(rest), aus


def saetze(t):
    """Sätze eines Textes (mit Platzhaltern) – Grenze nach . ? ! vor
    Großbuchstaben oder Anführung."""
    teile = re.split(r"(?<=[.?!])\s+(?=[A-ZÄÖÜ„\x00])", t.strip())
    return [s.strip() for s in teile if s.strip()]


def gross_anfang(s):
    """Frage beginnt groß: Fragewort oder klein geschriebenes Wort ab drei
    Buchstaben („ordnen?“ → „Ordnen?“); Variablen („p und q?“) bleiben."""
    if FRAGEWORT_KLEIN.match(s) or re.match(r"^[a-zäöü]{3,}\b", s):
        return s[0].upper() + s[1:]
    return s


def satzform(z):
    """v0.8 (bau/sprachlauf/regeln.md): Ist die Aufgabe in ganzen Sätzen
    geschrieben (kein „ – “ als Satzersatz, kein Stichwort mit Doppelpunkt,
    Satzende am Schluss)? Dann {"kopf", "fett", "vor", "auffordernd"}:
    „Verb. Term“ → vor = Verb-Satz, kopf = Term (halbfett); sonst kopf =
    ganzer Text als normaler Absatz. Sonst None (alte Zerlegung)."""
    t = KENNUNG.sub("", z["aufgabe"])
    t, _ = befehle_heraus(t, "wertetabelle")
    t, _ = befehle_heraus(t, "kreuz")
    t = t.replace("\\janein", "")
    t = re.sub(r"(\\\\\s*)+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    s, st = schuetze(t)
    if not s or " – " in s:
        return None
    m = re.match(r"^([^:\x00]{2,45}): ", s)
    if m and not re.search(r"[.?!]", m.group(1)):
        w = m.group(1).split()
        if len(w) <= 2 and not re.search(
                r"(sagt|schreibt|behauptet|rechnet|steht|gilt|fragt)$",
                m.group(1)):
            return None
    teile = saetze(s)
    if len(teile) == 2 and IMPERATIV.match(teile[0]) and \
            re.fullmatch(r"(\x00\d+\x01[;,]?\s*)+", teile[1]):
        term = re.sub(r"\$([^$]+)\$", r"$\\displaystyle \1$",
                      zurueck(teile[1], st))
        return {"kopf": term, "fett": True,
                "vor": zurueck(teile[0], st), "auffordernd": True}
    if not re.search(r"[.?!“]$", s):
        return None
    auff = any(x.endswith("?") or IMPERATIV.match(x) for x in teile)
    return {"kopf": zurueck(s, st), "fett": False, "vor": "",
            "auffordernd": auff}


def zerlege(z):
    """Aufgabentext einer Bankzeile in Teile nach layout-befunde 3–8, 28:
    kopf (Auftakt oder Kontext, erste Zeile), fett (Auftakt halbfett?),
    frage (Sätze, je eine Zeile), tabellen, kreuze, kennung."""
    t = z["aufgabe"]
    kennung = ""
    m = KENNUNG.search(t)
    if m:
        kennung = kennung_kompetenz(m.group(0))
        t = t[:m.start()] + t[m.end():]
    t, tabellen = befehle_heraus(t, "wertetabelle")
    t, kreuze = befehle_heraus(t, "kreuz")
    t = t.replace("\\janein", "")
    t = re.sub(r"(\\\\\s*)+", " ", t)          # Zeilenenden des Banktexts
    t = re.sub(r"\s+", " ", t).strip()
    s, st = schuetze(t)
    kopf, fett, rest, vor = "", False, s, ""
    k = s.rfind(" – ")
    m = re.match(r"^([^:\x00]{2,45}): (.+)$", s)
    if k > 0 and len(schlicht(zurueck(s[k + 3:], st))) <= 90:
        # „Kontext – Frage?“: Kontext als Auftakt, Frage darunter
        kopf, rest = s[:k].strip(), s[k + 3:].strip()
        fett = len(schlicht(zurueck(kopf, st))) <= 70
    elif m and not re.search(r"[.?!]", m.group(1)):
        # „Auftakt: Auftrag“; ist der Auftakt ein Auftrag („Rechne: 3 · 4“),
        # steht er als Aufforderung über dem Rest
        kopf, fett, rest = m.group(1), True, m.group(2)
        if IMPERATIV.match(kopf) and len(kopf.split()) <= 3:
            vor = kopf + "."
            kopf, rest = rest, ""
            fett = len(schlicht(zurueck(kopf, st))) <= 70
    frage = saetze(rest)
    if not kopf and len(frage) > 1:
        # Kontext = Sätze vor der ersten Aufforderung (Frage, Imperativ)
        i = 0
        while i < len(frage) - 1 and not (frage[i].endswith("?")
                                          or IMPERATIV.match(frage[i])):
            i += 1
        if i:
            kopf, frage = " ".join(frage[:i]), frage[i:]
    frage = [gross_anfang(zurueck(f, st)) for f in frage]
    return {"kopf": zurueck(kopf, st).strip(), "fett": fett, "vor": vor,
            "frage": [f for f in frage if f], "tabellen": tabellen,
            "kreuze": kreuze, "kennung": kennung}


def ksys_optionen(grafik):
    m = re.search(r"\\begin\{ksys\}(\[([^\]]*)\])?", grafik)
    if not m:
        return None
    opt = {}
    for teil in (m.group(2) or "").split(","):
        if "=" in teil:
            k, v = teil.split("=", 1)
            opt[k.strip()] = v.strip()
        elif teil.strip():
            opt[teil.strip()] = True
    return opt


def _zahl(v, vorgabe):
    try:
        return float(str(v).replace("{,}", ".").replace(",", "."))
    except (TypeError, ValueError):
        return vorgabe


def grafik_mass(g):
    """(Breite, Höhe) in cm, grob; unbekannte Grafik: volle Breite."""
    o = ksys_optionen(g)
    if o is not None:
        karo = 0.8
        if o.get("ablesen"):
            karo = 0.6
        if o.get("klein"):
            karo = 0.35
        karo = _zahl(o.get("karo"), karo)
        xs, ys = _zahl(o.get("xstep"), 1), _zahl(o.get("ystep"), 1)
        b = (_zahl(o.get("xmax"), 4) - _zahl(o.get("xmin"), -4)) / xs * karo
        h = (_zahl(o.get("ymax"), 4) - _zahl(o.get("ymin"), -4)) / ys * karo
        return b + 1.0, h + 0.8
    m = re.match(r"\\wertetabelle(\[[^\]]*\])?\{([^}]*)\}\{([^}]*)\}\{(.*)\}$",
                 g.strip(), re.S)
    if m:
        n = len(m.group(4).split(","))
        kopf = max(len(schlicht(m.group(2))), len(schlicht(m.group(3))))
        return 0.5 + 0.19 * kopf + n * 1.25, 1.9
    return 99.0, 4.0


def grafik_mass_lern(g):
    """Wie grafik_mass, dazu (v1.0, Lernblatt) die Figuren der Vorlage:
    \\viereck und \\dreieck aus den Koordinaten (cm) plus Rand für die
    Beschriftung, \\termbaum etwa 6 cm, \\sachtabelle 1,6 cm je Spalte."""
    s = g.strip()
    if re.match(r"\\(viereck|dreieck)\b", s):
        xs = [float(x) for x in re.findall(r"\((-?[\d.]+)\s*,\s*-?[\d.]+\)", s)]
        ys = [float(y) for y in re.findall(r"\(-?[\d.]+\s*,\s*(-?[\d.]+)\)", s)]
        if xs and ys:
            return max(xs) - min(xs) + 1.6, max(ys) - min(ys) + 1.2
    if s.startswith("\\termbaum"):
        return 6.0, 3.0
    m = re.match(r"\\sachtabelle\{([^}]*)\}", s)
    if m:
        return 0.4 + 1.6 * len(re.findall(r"[lcrp]", m.group(1))), 1.6
    return grafik_mass(g)


def ksys_verkleinern(g, log, wo):
    """Koordinatensystem zum Zeichnen höchstens KSYS_HOEHE_CM hoch
    (Befund 21, Seitenumfang 2–4): Karo kleiner, Bereich unverändert."""
    o = ksys_optionen(g)
    if o is None:
        return g
    b, h = grafik_mass(g)
    if h <= KSYS_HOEHE_CM:
        return g
    karo = 0.8 if not o.get("ablesen") else 0.6
    karo = _zahl(o.get("karo"), karo)
    neu = max(0.5, round(karo * (KSYS_HOEHE_CM - 0.8) / (h - 0.8), 2))
    if neu >= karo:
        return g
    log(f"KSYS {wo}: Karo {karo} → {neu} cm (Höhe {h:.1f} → "
        f"{(h - 0.8) * neu / karo + 0.8:.1f} cm)")

    def ersetze(m):
        inhalt = m.group(2) or ""
        inhalt = re.sub(r",?\s*karo=[^,\]]*", "", inhalt).strip(",")
        return "\\begin{ksys}[" + (inhalt + "," if inhalt else "") + \
            f"karo={neu}]"
    return re.sub(r"\\begin\{ksys\}(\[([^\]]*)\])?", ersetze, g, count=1)


def tabellenkopf(h):
    """Tabellenkopf im Textmodus (Befund 26): Variable in Mathe, Wörter
    als Text („Zeit in h“)."""
    h = h.strip()
    if re.fullmatch(r"[A-Za-z](\([A-Za-z]\))?|[A-Za-z]_\{?\w+\}?|[A-Za-z]\d?",
                    h):
        return f"${h}$"
    if h.startswith("$") or "\\" in h:
        return h
    return klar(h)


def tabelle_text(t):
    """\\wertetabelle[…]{a}{b}{…} → \\kbwertetabelle mit Textköpfen."""
    m = re.match(r"\\wertetabelle(\[[^\]]*\])?", t)
    k = m.end()
    args = []
    while k < len(t) and t[k] == "{":
        e = BP.klammer(t, k)
        args.append(t[k + 1:e - 1])
        k = e
    if len(args) != 3:
        return t
    return (f"\\kbwertetabelle{m.group(1) or ''}{{{tabellenkopf(args[0])}}}"
            f"{{{tabellenkopf(args[1])}}}{{{args[2]}}}")


def antwort_zeilen(antwort):
    """Antwortgerüst als Zeilen (Befund 4, 29): „x1“ → $x_1$, „;“ trennt
    Zeilen, je Zeile Felder \\kbfeld (2,2 cm), in Punkten „( | )“ kurz."""
    if not antwort:
        return []
    if antwort.strip() == "\\janein":
        return ["\\janein"]
    a = re.sub(r"(?<![\\$A-Za-z])([a-zA-Z])(\d)(?![\d])", r"$\1_\2$", antwort)
    a = re.sub(r"(?<![\\$A-Za-z])([A-Za-z]{1,2})(?= (=|≈) )",
               lambda m: m.group(1) if len(m.group(1)) > 1 and
               m.group(1)[0].islower() else f"${m.group(1)}$", a)
    zeilen = [x.strip() for x in a.split(";") if x.strip()]
    aus = []
    for x in zeilen:
        f = antwortfeld(x)
        feld = "\\kbfeldk" if "|" in x else "\\kbfeld"
        f = f.replace("\\leerfeld", feld).replace(" ,", ",")
        aus.append(f)
    return aus


def rechenzeilen(z):
    """Bearbeitungsraum (Befund 9): 0 bei Ankreuzen, Zeichnen, Ein-Zahl-
    Antwort ohne Rechnung; 2 bei Rechnung; 3 bei langer Rechnung.
    Rechenschritte: Operatoren der Lösung, dazu die Gleichheitszeichen über
    die Zahl der Antwortfelder hinaus („$p = -1$, $q = -12$“ ist Ablesen)."""
    if z["form"] in ("ankreuzen", "zeichnen", "streifenfeld", "streifenleer"):
        return 0
    if z.get("pflicht") == "begruenden":
        return 3
    if z["form"] == "gleichungsraster" and z["hoehe"] != "vorstufe" \
            and z.get("eintrag") and z["einheit"]:
        return 2
    lo = z.get("loesung", "")
    felder = max(1, (z.get("antwort") or "").count("__"))
    schritte = len(re.findall(r"\\cdot|\\pm|\\sqrt|\\frac|(?<![a-z]) : |"
                              r"\\mid|\^|\\approx", lo))
    schritte += max(0, lo.count("=") - felder)
    if schritte < 2:
        return 0
    if z["hoehe"] == "pruefung" and (len(lo) > 160 or schritte > 6):
        return 3
    return 2


def zeichen_vorspann(texte):
    """newunicodechar-Zeilen für alle Zeichen aus LM_FEHLT, die in den
    Texten vorkommen."""
    alle = set("".join(texte))
    aus = []
    for c in sorted(alle & set(LM_FEHLT), key=ord):
        mathe = MATHE_ZEICHEN.get(c)
        if mathe:
            aus.append(f"\\newunicodechar{{{c}}}{{\\kbzeichen{{{c}}}"
                       f"{{{mathe}}}}}")
        else:
            aus.append(f"\\newunicodechar{{{c}}}{{\\kbzeichenhoch{{{c}}}}}")
    return aus, sorted(alle & set(LM_FEHLT), key=ord)


VORSPANN = r"""% vorspann.tex – Kompetenzblatt, zusammenbau v0.7 (2026-09-28).
% Ergänzt mathblatt.sty für Kompetenzblätter, ohne sie zu ändern
% (layout-befunde.md 1–34 vom 28.09.). Wird nach \usepackage{mathblatt}
% eingelesen.
\makeatletter
\RequirePackage{newunicodechar}
% Zeichen, die Latin Modern nicht hat (Befund 20): Text aus einer
% Ersatzschrift, Mathe als Befehl; ohne Ersatzschrift auch Text als Mathe.
\newif\ifkbersatz
\IfFontExistsTF{FreeSerif}{\newfontfamily\kbersatzschrift{FreeSerif}\kbersatztrue}{%
 \IfFontExistsTF{DejaVu Serif}{\newfontfamily\kbersatzschrift{DejaVu Serif}\kbersatztrue}{%
  \IfFontExistsTF{Cambria Math}{\newfontfamily\kbersatzschrift{Cambria Math}\kbersatztrue}{%
   \IfFontExistsTF{Segoe UI Symbol}{\newfontfamily\kbersatzschrift{Segoe UI Symbol}\kbersatztrue}{}}}}
\newcommand{\kbzeichen}[2]{\ifmmode #2\else\ifkbersatz{\kbersatzschrift #1}\else\ensuremath{#2}\fi\fi}
\newcommand{\kbzeichenhoch}[1]{\ifkbersatz\ifmmode\text{\kbersatzschrift #1}\else{\kbersatzschrift #1}\fi\else ?\fi}
% Kopf- und Fußzeile (Befund 1, 2): Kopf Thema · Blattart, Fuß Kennung und Seite
\newcommand{\kbkopfzeile}[2]{\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}%
  \fancyhead[L]{\footnotesize\color{mbgrau}#1}%
  \fancyfoot[L]{\footnotesize\color{mbgrau}#2}%
  \fancyfoot[R]{\footnotesize\color{mbgrau}Seite \thepage}}
% Flattersatz überall (Befund 25)
\raggedright
% Titel des Blatts: Ich-kann-Satz, darunter Zweigzeile
\newcommand{\kbtitel}[2]{\par\noindent{\Large\bfseries\raggedright #1\par}%
  \ifblank{#2}{}{\par\smallskip\noindent{\small #2}\par}\medskip}
% Abschnitt: „Das kennst du schon“, „Zum Merken“
\newcommand{\kbabschnitt}[1]{\par\addvspace{12pt}\Needspace*{5\baselineskip}%
  \noindent{\bfseries #1}\par\nobreak\vspace{3pt}}
% Hauptnummer: Titel hängt am ersten Block; jeder Block (Teilaufgabe) bricht
% nicht, passt er nicht mehr, rückt er ganz auf die nächste Seite (Befund 21).
\newif\ifkbtitel
\newsavebox{\kbbox}
\newlength{\kbhoehe}
\newlength{\kbnummerabstand}\setlength{\kbnummerabstand}{10pt}
\newlength{\kbteilabstand}\setlength{\kbteilabstand}{6pt}
\newenvironment{kbaufgabe}[1]{\stepcounter{aufgabe}\setcounter{teil}{0}%
  \gdef\kbtiteltext{\noindent\hangindent1.6em\hangafter1\makebox[1.6em][l]{\textbf{\theaufgabe.}}#1\par}%
  \global\kbtiteltrue\par\addvspace{\kbnummerabstand}}{\par}
\newenvironment{kbblock}{\par\addvspace{\kbteilabstand}\begin{lrbox}{\kbbox}%
  \begin{minipage}[t]{\linewidth}\raggedright\parskip\z@
  \ifkbtitel\kbtiteltext\vspace{2pt}\global\kbtitelfalse\fi
  \list{}{\leftmargin1.6em\labelwidth1.4em\labelsep0.2em\topsep\z@\partopsep\z@
    \parsep\z@\itemsep\z@\rightmargin\z@}\raggedright}%
  {\endlist\end{minipage}\end{lrbox}%
  \setlength{\kbhoehe}{\dimexpr\ht\kbbox+\dp\kbbox\relax}%
  \Needspace*{\kbhoehe}\noindent\usebox{\kbbox}\par}
% Paarsatz (Platz nutzen, Befund 27): zwei Hauptnummern oder zwei
% Teilaufgaben mit Zeichenaufgabe nebeneinander, als ein Block
\newcommand{\kbnummer}[1]{\stepcounter{aufgabe}\setcounter{teil}{0}%
  \noindent\hangindent1.6em\hangafter1\makebox[1.6em][l]{\textbf{\theaufgabe.}}#1\par\vspace{2pt}}
\newcommand{\kbhalb}[1]{\list{}{\leftmargin1.6em\labelwidth1.4em\labelsep0.2em\topsep\z@
  \partopsep\z@\parsep\z@\itemsep\z@}\raggedright #1\endlist}
\newcommand{\kbpaar}[2]{\par\addvspace{\kbnummerabstand}\begin{lrbox}{\kbbox}%
  \begin{minipage}[t]{0.485\linewidth}\raggedright\parskip\z@ #1\end{minipage}\hfill
  \begin{minipage}[t]{0.485\linewidth}\raggedright\parskip\z@ #2\end{minipage}\end{lrbox}%
  \setlength{\kbhoehe}{\dimexpr\ht\kbbox+\dp\kbbox\relax}\Needspace*{\kbhoehe}\noindent\usebox{\kbbox}\par}
\newcommand{\kbteilpaar}[2]{\item[]\noindent
  \begin{minipage}[t]{0.485\linewidth}\kbhalb{#1}\end{minipage}\hfill
  \begin{minipage}[t]{0.485\linewidth}\kbhalb{#2}\end{minipage}\par}
% Anweisung der Hauptnummer, eigene Zeile über der Teilaufgabe (Befund 5)
\newcommand{\kbanweisung}[1]{\item[]#1\par\vspace{2pt}}
% Kopfzeile einer Teilaufgabe: Buchstabe, Auftakt (halbfett oder Kontext),
% Prüfkennung klein rechts (Befund 3, 12, Beschluss c)
\newlength{\kbkennbreite}\setlength{\kbkennbreite}{1.9cm}
\newcommand{\kbkennung}[1]{{\footnotesize #1}}
\newcommand{\kbteil}[3]{\item[#1]\ifblank{#3}%
  {\parbox[t]{\linewidth}{\raggedright #2}}%
  {\parbox[t]{\dimexpr\linewidth-\kbkennbreite\relax}{\raggedright #2}\hfill
   \parbox[t]{\kbkennbreite}{\raggedleft\kbkennung{#3}}}\par}
% Frage in eigener Zeile (Befund 4), ein Satz je Zeile (Befund 10)
\newcommand{\kbfrage}[1]{\par\vspace{2pt}#1\par}
% Antwortfeld in eigener Zeile darunter, linksbündig (Befund 4, 8)
\newcommand{\kbantwort}[1]{\par\vspace{4pt}\noindent#1\par}
% Zwei Spalten: links Grafik/Tabelle/Aufgabe, rechts Antwort oder Rechenraum
% (Befund 27); oben bündig. Beginnt einen eigenen Listenpunkt ohne Marke.
\newcommand{\kbzweispaltig}[3][0.48]{\item[]\noindent
  \begin{minipage}[t]{#1\linewidth}\raggedright #2\end{minipage}\hfill
  \begin{minipage}[t]{\dimexpr0.98\linewidth-#1\linewidth\relax}\raggedright #3\end{minipage}\par}
% Linke Spalte mit Teilaufgabe (Buchstabe hängt links heraus wie in der Liste)
\newcommand{\kbspalte}[1]{\list{}{\leftmargin\z@\labelwidth1.4em\labelsep0.2em\topsep\z@
  \partopsep\z@\parsep\z@\itemsep\z@}\raggedright #1\endlist}
% Antwortfelder: 2,2 cm, in Punkten 1,2 cm; ohne Umbruch davor
\newcommand{\kbfeld}[1][]{\mbox{\underline{\hspace{2.2cm}}\ifblank{#1}{}{\,#1}}}
\newcommand{\kbfeldk}[1][]{\mbox{\underline{\hspace{1.2cm}}\ifblank{#1}{}{\,#1}}}
% Grafik oder Tabelle unter dem Text, linksbündig (Befund 8, 28)
\newcommand{\kbdarunter}[1]{\par\vspace{4pt}\noindent#1\par}
% Ankreuzen: je Option eine Zeile, linksbündig (Befund 6, 7)
\newcommand{\kbkreuz}[1]{\par\vspace{2pt}\noindent$\square$\ #1\par}
% Bearbeitungsraum (Befund 9): Schreibzeilen wie mathblatt (9 mm)
\newcommand{\kbraum}[1]{\schreibzeilen{#1}}
% Wertetabelle mit Köpfen im Textmodus (Befund 26): wie \wertetabelle der
% Vorlage, aber die Köpfe setzt der Aufruf selbst ($x$, „Zeit in h“).
\NewDocumentCommand{\kbwertetabelle}{o m m m}{%
  \def\mbkopf{}\def\mbwerte{}\def\mbleer{}\setcounter{mbn}{0}%
  \foreach \v in {#4}{\xappto\mbkopf{& $\v$}\xappto\mbleer{& }\stepcounter{mbn}\xdef\mbnn{\arabic{mbn}}}%
  \IfNoValueTF{#1}{}{\foreach \v in {#1}{\ifdefempty{\v}{\xappto\mbwerte{& }}{\xappto\mbwerte{& $\v$}}}}%
  \begingroup\renewcommand{\arraystretch}{1.3}%
  \edef\mbpre{|>{\noexpand\columncolor{mbkasten}}l|*{\mbnn}{>{\noexpand\centering\noexpand\arraybackslash}p{\noexpand\mbzell}|}}%
  \expandafter\mbtabstart\expandafter{\mbpre}\hline
  #2 \mbkopf \\ \hline
  \IfNoValueTF{#1}{\rule{0pt}{\mbzeile}#3 \mbleer \\ \hline}{#3 \mbwerte \\ \hline}
  \end{tabular}\endgroup}
% Merkkasten am Ende (Aufbau des Kompetenzblatts)
\newcommand{\kbmerk}[2]{\par\addvspace{14pt}\begin{lrbox}{\kbbox}\begin{minipage}[t]{\linewidth}%
  \noindent{\bfseries #1}\par\vspace{4pt}%
  \uebersichtskasten{\raggedright #2}\end{minipage}\end{lrbox}%
  \setlength{\kbhoehe}{\dimexpr\ht\kbbox+\dp\kbbox\relax}\Needspace*{\kbhoehe}\noindent\usebox{\kbbox}\par}
% Lösungsblatt: Nummer und Buchstabe halbfett, Lösung daneben
\newcommand{\kbloesung}[2]{\par\addvspace{3pt}\noindent\hangindent2.8em\hangafter1\makebox[2.8em][l]{\textbf{#1}}#2\par}
\makeatother
"""


def waehle_originale(pr, log, auffuellen_bis, ohne_original_eins=False):
    """Prüfungshöhen einer Kette (Kompetenzblatt Beschluss d, seit v0.9 auch
    Lernblatt): je Original höchstens eine Aufgabe (kleinste Sprosse und
    Variante); nur die jüngsten fünf Jahrgänge der Kette; verschiedene
    Formulierungen zuerst, höchstens fünf; mit gleicher Formulierung
    aufgefüllt bis auffuellen_bis. ohne_original_eins: alle Zeilen ohne
    Original zählen als ein Original (Lernblatt: eine der drei Zeilen)."""
    je = {}
    for z in sorted(pr, key=lambda z: (z["sprosse"], z["variante"])):
        o = (z.get("original") or {}).get("id") or (
            "ohne Original" if ohne_original_eins else z["id"])
        if o in je:
            log(f"RESERVE {z['id']} ({o}) – weitere Variante desselben "
                "Originals")
        je.setdefault(o, z)
    if not je:
        log("PRÜFUNG keine Prüfungshöhe in der Kette")
        return []

    def jahr(z):
        return int((z.get("original") or {}).get("jahr") or 0)

    jahre = sorted({jahr(z) for z in je.values()}, reverse=True)
    fenster = set(jahre[:KOMPETENZ_JAHRGAENGE])
    log(f"PRÜFUNG {len(je)} Originale, Jahrgänge {sorted(jahre)}; "
        f"Fenster (jüngste fünf): {sorted(fenster)}")
    kand = sorted([z for z in je.values() if jahr(z) in fenster],
                  key=lambda z: (-jahr(z), z["sprosse"], z["variante"]))
    for z in je.values():
        if jahr(z) not in fenster:
            log(f"RESERVE {z['id']} ({(z.get('original') or {}).get('id')})"
                " – älter als die jüngsten fünf Jahrgänge")

    def form(z):
        s, st = schuetze(KENNUNG.sub("", z["aufgabe"]))
        s = re.sub(r"\x00\d+\x01", "#", s)
        s = re.sub(r"\d+([.,]\d+)?", "#", s)
        return " ".join(s.split()[:6])

    wahl, formen = [], set()
    for z in kand:
        if len(wahl) >= KOMPETENZ_PRUEF_MAX:
            break
        f = form(z)
        if f not in formen:
            wahl.append(z)
            formen.add(f)
    for z in kand:
        if len(wahl) >= auffuellen_bis:
            break
        if z not in wahl:
            wahl.append(z)
            log(f"FORMULIERUNG {z['id']}: gleiche Formulierung wie eine "
                f"schon gewählte – aufgefüllt auf {auffuellen_bis}")
    wahl.sort(key=lambda z: (-jahr(z), z["sprosse"], z["variante"]))
    for z in kand:
        if z not in wahl:
            log(f"RESERVE {z['id']} ({(z.get('original') or {}).get('id')})"
                " – Formulierung schon vertreten oder mehr als fünf")
    return wahl


class KompetenzBau(KbSatz):
    """Rezept K: Kompetenzblatt zu genau einer Kette."""

    def __init__(self, args, log):
        self.a = args
        self.log = log
        self.eintrag = args.eintrag
        self.niveau = args.niveau or "for"
        bank = WURZEL / "bank" / self.eintrag
        if not bank.is_dir():
            sys.exit(f"bank/{self.eintrag}/ fehlt")
        self.mappe = Mappe(WURZEL / "mappen" / f"{self.eintrag}.md", log)
        self.thema = self.mappe.thema or self.eintrag
        self.e = {}
        for p in bank.glob("e*.jsonl"):
            if re.fullmatch(r"e\d+", p.stem):
                self.e[int(p.stem[1:])] = lies_jsonl(p)
        zp = bank / "zone.jsonl"
        self.zone_bank = lies_jsonl(zp) if zp.exists() else []
        self.kat = kataloge_still()
        self.ik = lies_ichkann()
        self.ohne = set((args.ohne or "").split(",")) - {""}
        self.dicht = bool(getattr(args, "dicht", False))
        self.kennung = args.kennung
        self.einheit, self.kette = self.waehle(args.kompetenz)
        self.zeilen = [z for z in self.e[self.einheit]
                       if z["kette"].casefold() == self.kette.casefold()]
        self.m, self.m_methode = mappe_einheit(self.mappe, self.kette,
                                               self.zeilen, self.einheit)
        log(f"EINHEIT Bank e{self.einheit}, Katalog Einheit {self.m} "
            f"({self.m_methode})")
        self.info = {}
        self.hs = []            # [(Titel, Anweisung, [Zeilen], lage)]
        self.zone_wahl = []
        self.zeichen = []
        self.titel_quelle = {}

    def waehle(self, wunsch):
        if self.a.einheiten:
            wahl = [int(x) for x in self.a.einheiten.split(",") if x.strip()]
            if len(wahl) != 1 or wahl[0] not in self.e:
                sys.exit(f"--einheiten: genau eine Einheit aus bank/"
                         f"{self.eintrag}/ ({sorted(self.e)})")
            kandidaten = wahl
        else:
            kandidaten = sorted(self.e)
        for n in kandidaten:
            zz = [z for z in self.e[n] if z["kette"].casefold()
                  == wunsch.casefold() and z["hoehe"] != "pflicht"]
            if zz:
                return n, zz[0]["kette"]
        namen = sorted({z["kette"] for n in kandidaten for z in self.e[n]})
        sys.exit(f"Kette „{wunsch}“ nicht in Einheit(en) {kandidaten}; "
                 "vorhanden: " + "; ".join(namen))

    # -- Titel -------------------------------------------------------------
    def ich_kann(self, einheit, kette, sprosse, ersatz):
        k = (self.eintrag, einheit, kette.casefold(), sprosse)
        if k in self.ik and self.ik[k][0]:
            return self.ik[k]
        self.log(f"ICH-KANN fehlt in bau/regal/ich-kann.csv: e{einheit} "
                 f"„{kette}“ Sprosse „{sprosse}“ – aus der Bank umformuliert: "
                 f"„{ersatz}“")
        return ersatz, ""

    # -- Auswahl -------------------------------------------------------------
    def stern(self, z):
        o = z.get("original") or {}
        return self.kat.get(o.get("id"), {}).get("stern") == "ja"

    def leiter(self):
        log = self.log
        wo = f"{self.eintrag} e{self.einheit} „{self.kette}“"
        sprossen = {}
        for z in self.zeilen:
            if z["hoehe"] == "pruefung" or z["id"] in self.ohne:
                continue
            sprossen.setdefault(z["sprosse"], []).append(z)
        aus = []
        for s in sorted(sprossen):
            zz = sorted(sprossen[s], key=lambda z: z["variante"])
            frei = [z for z in zz if not z.get("original")]
            wahl = frei[0] if frei else ohne_kennung(zz[0])
            grund = ("Variante 1" if wahl["variante"] == 1 else
                     f"kleinste Variante ohne Original (v{wahl['variante']})"
                     if frei else "Variante 1, Prüfkennung entfernt "
                     "(alle Varianten mit Original)")
            log(f"AUSWAHL {wahl['id']} – {wo}, Sprosse {s} ({wahl['hoehe']}): "
                f"{grund}")
            ersatz = "Ich kann: " + re.split(r"[:;,(]", wahl.get("merkmal")
                                             or self.kette)[0].strip() + "."
            titel, anw = self.ich_kann(self.einheit, self.kette, str(s), ersatz)
            aus.append((titel, anw, [wahl], "leiter"))
            self.info[wahl["id"]] = {"lage": "leiter", "sprosse": s}
        return aus

    def pruefung(self):
        """Beschluss d: je Original höchstens eine Aufgabe; nur die jüngsten
        fünf Jahrgänge der Kette; 4–5 Teilaufgaben mit verschiedenen
        Formulierungen, sonst so viele Originale, wie es gibt."""
        log = self.log
        pr = [z for z in self.zeilen if z["hoehe"] == "pruefung"
              and z["id"] not in self.ohne]
        if self.niveau == "ebr":
            weg = [z for z in pr if self.stern(z)]
            for z in weg:
                log(f"WEG {z['id']} – Niveau EBR: Original mit Stern")
            pr = [z for z in pr if not self.stern(z)]
        wahl = waehle_originale(pr, log, KOMPETENZ_PRUEF_MIN)
        if not wahl:
            return []
        for z in wahl:
            o = z.get("original") or {}
            self.info[z["id"]] = {"lage": "pruefung", "original": o.get("id"),
                                  "jahr": o.get("jahr"),
                                  "stern_im_original": self.stern(z)}
            log(f"AUSWAHL {z['id']} – Prüfungshöhe ({o.get('id')}, "
                f"{o.get('jahr')})")
        titel, anw = self.ich_kann(self.einheit, self.kette, "p",
                                   "Ich kann das auch in Aufgaben aus der "
                                   "Prüfung.")
        return [(titel, anw, wahl, "pruefung")]

    def zone(self):
        """Fertigkeiten der Zone, die diese Kette braucht: Voraussetzungs-
        zeilen der Mappe mit der Katalogeinheit der Kette (spezifische
        zuerst, dann „alle Einheiten“), höchstens drei, je Grundfall v1."""
        log = self.log
        ketten = []
        for z in self.zone_bank:
            if z["kette"] not in ketten:
                ketten.append(z["kette"])
        self.kettenwoerter = set()
        for z in self.zeilen:
            self.kettenwoerter |= staemme(" ".join(
                [z.get("merkmal", ""),
                 z.get("sprosse_text", ""), z.get("loesung", "")]))
        kand = []
        for i, k in enumerate(ketten):
            zeile = next((x for x in self.mappe.fertigkeit_zeilen
                          if x == k or x.startswith(k)), None)
            if zeile is None:
                log(f"ZONE „{k}“: nicht in den Voraussetzungen der Mappe")
                continue
            nummern, art = fertigkeit_einheiten(zeile)
            angabe = (f"Einheit {', '.join(map(str, sorted(nummern)[:6]))}"
                      if art == "genannt" else art)
            if art == "genannt" and self.m not in nummern:
                log(f"ZONE „{k}“ ({angabe}): nicht für Katalogeinheit {self.m}")
                continue
            treffer = len(staemme(k) & self.kettenwoerter)
            rang = (0 if art == "genannt" else 1, -treffer, len(nummern) or 9,
                    i)
            kand.append((rang, k, angabe + f", {treffer} gemeinsame Wörter"))
        kand.sort()
        aus = []
        for rang, k, angabe in kand[:ZONE_FERTIGKEITEN]:
            zz = sorted([z for z in self.zone_bank if z["kette"] == k
                         and z["id"] not in self.ohne],
                        key=lambda z: ({"grundfall": 0, "sprosse": 1}.get(
                            z["hoehe"], 2), z["sprosse"], z["variante"]))
            if not zz:
                continue
            w = zz[0]
            titel, anw = self.ich_kann(0, k, "", "Ich kann " + k.split(",")[0]
                                       + ".")
            aus.append((titel, anw, [w], "zone"))
            self.info[w["id"]] = {"lage": "zone"}
            self.zone_wahl.append(k)
            log(f"ZONE „{k}“ ({angabe}) → {w['id']}")
        for rang, k, angabe in kand[ZONE_FERTIGKEITEN:]:
            log(f"ZONE „{k}“ ({angabe}): passt, aber über {ZONE_FERTIGKEITEN} "
                "Fertigkeiten – entfällt")
        if len(aus) == 1:
            k = aus[0][2][0]["kette"]
            zz = [z for z in self.zone_bank if z["kette"] == k
                  and z["id"] != aus[0][2][0]["id"] and z["id"] not in self.ohne]
            if zz:
                w = sorted(zz, key=lambda z: (z["sprosse"], z["variante"]))[0]
                aus[0][2].append(w)
                self.info[w["id"]] = {"lage": "zone"}
                log(f"ZONE nur eine Fertigkeit – zweite Aufgabe {w['id']}")
        return aus

    def dicht_tauglich(self, h):
        """--dicht: Hauptnummer mit einer Rechenaufgabe ohne Grafik, Tabelle,
        Kreuze und Prüfkennung, kurzer Text – darf neben eine zweite."""
        titel, anw, zeilen, lage = h
        if lage != "leiter" or len(zeilen) != 1:
            return False
        z = zeilen[0]
        if z.get("grafik") or z["form"] not in ("teil", "text") or \
                "\\wertetabelle" in z["aufgabe"] or "\\kreuz" in z["aufgabe"] \
                or KENNUNG.search(z["aufgabe"]) or "\\rechnung" in z["aufgabe"]:
            return False
        return len(schlicht(z["aufgabe"])) <= 150

    def satz(self):
        a = []
        nr = 0
        self.reihenfolge = []
        hs = self.hs
        i = 0
        while i < len(hs):
            titel, anw, zeilen, lage = hs[i]
            if lage == "zone" and (i == 0 or hs[i - 1][3] != "zone"):
                a += ["", "\\kbabschnitt{Das kennst du schon}"]
            # Paar: zwei Hauptnummern mit je einer Zeichenaufgabe nebeneinander
            if (lage != "zone" and len(zeilen) == 1 and i + 1 < len(hs)
                    and hs[i + 1][3] == lage and len(hs[i + 1][2]) == 1
                    and self.halb_tauglich(zeilen[0])
                    and self.halb_tauglich(hs[i + 1][2][0])):
                halben = []
                for tt, aa, zz, ll in (hs[i], hs[i + 1]):
                    nr += 1
                    halben.append("\\kbnummer{" + klar(tt) + "}"
                                  + "\\kbhalb{" + "\n".join(
                                      self.satz_halb(zz[0], "", aa)) + "}")
                    self.reihenfolge.append((nr, "", zz[0]))
                a += ["", f"% {lage}: {zeilen[0]['id']}, {hs[i + 1][2][0]['id']}"
                      " (Paar)", "\\kbpaar{", halben[0], "}{", halben[1], "}"]
                self.log(f"PAAR Nr. {nr - 1} und {nr}: zwei Zeichenaufgaben "
                         "nebeneinander")
                i += 2
                continue
            if (self.dicht and i + 1 < len(hs) and self.dicht_tauglich(hs[i])
                    and self.dicht_tauglich(hs[i + 1])):
                halben = []
                for tt, aa, zz, ll in (hs[i], hs[i + 1]):
                    nr += 1
                    halben.append("\\kbnummer{" + klar(tt) + "}"
                                  + "\\kbhalb{" + "\n".join(
                                      self.satz_halb_text(zz[0], aa)) + "}")
                    self.reihenfolge.append((nr, "", zz[0]))
                a += ["", f"% {lage}: {zeilen[0]['id']}, {hs[i + 1][2][0]['id']}"
                      " (Paar, dicht)", "\\kbpaar{", halben[0], "}{", halben[1],
                      "}"]
                self.log(f"PAAR Nr. {nr - 1} und {nr}: dicht (Rechenaufgaben "
                         "nebeneinander)")
                i += 2
                continue
            nr += 1
            a += ["", f"% {lage}: " + ", ".join(z["id"] for z in zeilen),
                  f"\\begin{{kbaufgabe}}{{{klar(titel)}}}"]
            mehr = len(zeilen) > 1
            anweisung = anw
            # v0.9: derselbe Auftrag in allen Teilaufgaben steht einmal über
            # der Nummer, die Teilaufgaben tragen nur den Rest (wie im
            # Lernblatt; Prüfkennung und Zusatzfrage bleiben am Rest)
            if len(zeilen) > 1 and not anweisung:
                lf = laeufe_von(zeilen)
                if len(lf) == 1 and lf[0][0] and all(r is not None
                                                     for r in lf[0][2]):
                    anweisung = lf[0][0]
                    zeilen = [dict(z, aufgabe=r) for z, r in zip(zeilen,
                                                                 lf[0][2])]
                    self.log(f"AUFTRAG Nr. {nr}: „{anweisung}“ einmal über "
                             f"{len(zeilen)} Teilaufgaben")
            if not anweisung and all(z["form"] == "gleichungsraster"
                                     for z in zeilen):
                anweisung = "Löse die Gleichung."
                self.log(f"ANWEISUNG Nr. {nr}: nackte Gleichung – "
                         "„Löse die Gleichung.“ (aus form)")
            j = 0
            while j < len(zeilen):
                z = zeilen[j]
                b = buchstabe(j) + ")" if mehr else ""
                if (j + 1 < len(zeilen) and self.halb_tauglich(z)
                        and self.halb_tauglich(zeilen[j + 1])):
                    z2 = zeilen[j + 1]
                    b2 = buchstabe(j + 1) + ")"
                    a.append("\\begin{kbblock}")
                    a.append("\\kbteilpaar{")
                    a += self.satz_halb(z, b, anweisung if j == 0 else "")
                    a.append("}{")
                    a += self.satz_halb(z2, b2, "")
                    a.append("}")
                    a.append("\\end{kbblock}")
                    self.reihenfolge.append((nr, buchstabe(j), z))
                    self.reihenfolge.append((nr, buchstabe(j + 1), z2))
                    self.log(f"PAAR Nr. {nr}{buchstabe(j)}/{buchstabe(j + 1)}: "
                             "nebeneinander")
                    j += 2
                    continue
                a.append("\\begin{kbblock}")
                a += self.satz_teil(z, b, anweisung if j == 0 else "")
                a.append("\\end{kbblock}")
                self.reihenfolge.append((nr, buchstabe(j) if mehr else "", z))
                j += 1
            a.append("\\end{kbaufgabe}")
            i += 1
        return a

    def kasten(self):
        zeilen = self.mappe.kasten.get(self.m)
        if not zeilen:
            self.kasten_status = "fehlt in der Mappe"
            self.log(f"KASTEN Katalogeinheit {self.m}: nicht lesbar – entfällt")
            return []
        self.kasten_status = f"{len(zeilen)} Zeilen"
        inhalt = [kasten_mathe(z) for z in zeilen]     # v0.8: Befund 40, 52
        self.log(f"KASTEN Katalogeinheit {self.m}: {len(zeilen)} Zeilen")
        return ["", "\\kbmerk{Zum Merken}{" + " \\\\ ".join(inhalt) + "}"]

    def loesungen(self):
        aus = []
        for nr, b, z in self.reihenfolge:
            lo = z.get("loesung", "") or "\\ldots"
            aus.append(f"\\kbloesung{{{nr}{b})}}{{{lo}}}" if b else
                       f"\\kbloesung{{{nr}.}}{{{lo}}}")
            if z.get("loesungsgrafik"):
                aus.append("\\par\\vspace{2pt}\\noindent\\hspace*{2.8em}"
                           + z["loesungsgrafik"] + "\\par")
        return aus

    def kopf(self):
        info = self.mappe.einheiten.get(self.m)
        os_, gym, _ = marke_zerlegen(info["marken"] if info else None)
        zm = zeitmarke(os_, gym, None)
        self.pruefwort = pruefwort_zahl("P10" if self.profil() == "msa"
                                        else PROFIL_WORT_MARKE.get(
                                            self.profil(), "P10"),
                                        self.zeilen, self.log)
        teile = [t for t in (zm, self.pruefwort) if t]
        self.zweig = " · ".join(teile)
        self.klasse_os, self.klasse_gym = os_, gym
        return self.zweig

    def profil(self):
        for z in self.zeilen:
            p = profil_von(z)
            if p:
                return p
        return "msa"

    def baue(self):
        titel, _ = self.ich_kann(self.einheit, self.kette, "",
                                 "Ich kann: " + self.kette + ".")
        self.titel = titel
        self.hs = self.zone() + self.leiter() + self.pruefung()
        zweig = self.kopf()
        k = self.kennung
        rumpf = [f"% Kompetenzblatt {k}: {self.eintrag} e{self.einheit} "
                 f"„{self.kette}“ (zusammenbau {VERSION}, Niveau "
                 f"{self.niveau.upper()})",
                 f"\\kbtitel{{{klar(titel)}}}{{{klar(zweig)}}}",
                 "\\setcounter{aufgabe}{0}"]
        rumpf += self.satz()
        rumpf += self.kasten()
        loes = [f"% Lösungen {k}",
                f"\\kbtitel{{Lösungen}}{{{klar(titel)}}}"] + self.loesungen()
        kopf_a = f"{klar(self.thema)} · Kompetenzblatt"
        kopf_l = f"{klar(self.thema)} · Kompetenzblatt · Lösungen"

        def dok(kopfzeile, zeilen):
            return (["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}",
                     "\\input{vorspann}", "\\begin{document}",
                     f"\\kbkopfzeile{{{kopfzeile}}}{{{k}}}"]
                    + zeilen + ["\\end{document}"])

        a = dok(kopf_a, rumpf)
        l = dok(kopf_l, loes)
        zeichen, self.zeichen = zeichen_vorspann(a + l)
        vorspann = VORSPANN.rstrip("\n").split("\n")
        if zeichen:
            vorspann = vorspann[:-1] + ["% Zeichen dieses Blatts, die Latin "
                                        "Modern nicht hat"] + zeichen + \
                vorspann[-1:]
        self.log(f"ZEICHEN Ersatz im Vorspann: {''.join(self.zeichen) or '–'}")
        for zeile in a:
            if not zeile.startswith("%") and BANKWORT.search(zeile):
                self.log(f"BANKWORT „{BANKWORT.search(zeile).group(0)}“ im "
                         f"Blatt: {zeile[:80]}")
        return {f"{k}.tex": a, f"{k}-loesungen.tex": l,
                "vorspann.tex": vorspann}


PROFIL_WORT_MARKE = {"msa": "P10", "abitur-gk": "Abitur GK",
                     "abitur-lk": "Abitur LK", "fhr": "FHR"}


def staemme(text):
    """Wortstämme (erste sechs Buchstaben, klein) ab fünf Buchstaben – für
    die Nähe einer Zonen-Fertigkeit zur Kette (v0.7)."""
    t = re.sub(r"\\[A-Za-z]+|\$[^$]*\$", " ", text)
    return {w[:6] for w in re.findall(r"[a-zäöüß]{5,}", t.casefold())}


def fertigkeit_einheiten(zeile):
    """Katalogeinheiten, für die eine Voraussetzungszeile gilt (v0.7):
    (menge, art) mit art „alle“, „genannt“ oder „ohne Angabe“. Klammern
    [...] und alles ab „Thema “ (Einheit des anderen Themas) zählen nicht."""
    t = re.sub(r"\[[^\]]*\]", "", zeile)
    t = t.split("Thema ", 1)[0]
    if re.search(r"alle Einheiten", t):
        return set(), "alle"
    t = re.sub(r"\([^()]*\)", "", t)
    nummern = set()
    for m in re.finditer(r"(ab )?Einheit(?:en)? ((?:\d+(?:\s*(?:,|und|bis|–)\s*"
                         r"(?:Einheit )?)?)+)", t):
        teil = m.group(2)
        zahlen = [int(x) for x in re.findall(r"\d+", teil)]
        if m.group(1):
            nummern |= set(range(zahlen[0], 20))
            continue
        for a, b in re.findall(r"(\d+)\s*bis\s*(\d+)", teil):
            nummern |= set(range(int(a), int(b) + 1))
        nummern |= set(zahlen)
    if nummern:
        return nummern, "genannt"
    return set(), "ohne Angabe"


def mappe_einheit(mappe, kette, zeilen, bank_n):
    """Katalogeinheit der Kette (die Bank zählt Einheiten mit ihrem
    Katalog-Commit, die Mappe mit dem aktuellen): 1. Zeile „- <Kette>
    (Einheit n“ in „Sprossen je Verfahrenstyp“, 2. Titel der Lerneinheit
    enthält den Kettennamen, 3. Typen je Lerneinheit enthält ihn, 4. größte
    Wortüberdeckung mit Titel und Beschreibung, 5. Nummer der Bank."""
    k = kette.casefold()
    for name, n in mappe.sprossen.items():
        if name == k:
            return n, "Sprossen je Verfahrenstyp"
    for name, n in mappe.sprossen.items():
        if name.startswith(k) or k.startswith(name):
            return n, "Sprossen je Verfahrenstyp (Anfang)"
    for n, info in mappe.einheiten.items():
        if k in info["titel"].casefold():
            return n, "Titel der Lerneinheit"
    for n, text in mappe.typen.items():
        if k in text.casefold():
            return n, "Typen je Lerneinheit"
    woerter = set(re.findall(r"[a-zäöüß]{4,}", " ".join(
        [kette] + [z.get("sprosse_text", "") for z in zeilen[:3]]).casefold()))
    best, n_best = 0, None
    for n, info in mappe.einheiten.items():
        text = (info.get("beschreibung") or info["titel"]) + " " + \
            mappe.typen.get(n, "")
        treffer = len(woerter & set(re.findall(r"[a-zäöüß]{4,}",
                                               text.casefold())))
        if treffer > best:
            best, n_best = treffer, n
    if n_best and best >= 2:
        return n_best, f"Wortüberdeckung ({best} Wörter)"
    return bank_n, "Nummer der Bank (keine Zuordnung in der Mappe)"


def main_kompetenz(args):
    """Rezept K (v0.7): Kompetenzblatt zu einer Kette."""
    log = Log()
    if len(args.eintrag) != 1:
        sys.exit("--kompetenz: genau ein Eintrag")
    args.eintrag = args.eintrag[0]
    args.niveau = args.niveau or "for"
    if args.fokus or args.schwach or args.nur_basis or args.heft or \
            args.klasse is not None or args.titel or args.fokus_pruefung:
        sys.exit("--kompetenz verträgt nur --einheiten, --niveau, --ohne, "
                 "--aus, --vorlage, --kuerzel, --ohne-register")
    aufruf = ["zusammenbau.py", args.eintrag, "--kompetenz",
              f"„{args.kompetenz}“", "--niveau", args.niveau]
    if args.einheiten:
        aufruf += ["--einheiten", args.einheiten]
    if args.ohne:
        aufruf += ["--ohne", args.ohne]
    if args.dicht:
        aufruf.append("--dicht")
    if args.ohne_register:
        aufruf.append("--ohne-register")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))
    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version} (unverändert; Ergänzungen im "
        "Vorspann)")
    rezept = "K"
    kuerzel, k_quelle = kuerzel_von(args.eintrag,
                                    finde_kuerzelliste(args.kuerzel))
    register = lies_register()
    if args.nummer:
        nummer = args.nummer
    else:
        nummer = 0 if args.ohne_register else naechste_nummer(kuerzel, rezept,
                                                              register)
    args.kennung = f"{kuerzel}-{rezept}{nummer}"
    if not args.ohne_register and any(z.get("kennung") == args.kennung
                                      for z in register):
        sys.exit(f"{args.kennung} steht schon in bau/register.csv")
    log(f"KENNUNG {args.kennung} – Kürzel {kuerzel} aus {k_quelle}; Rezept K "
        "(Kompetenzblatt)")
    bau = KompetenzBau(args, log)
    ziel = (Path(args.aus) if args.aus
            else WURZEL / "bau" / "kompetenz" / args.kennung)
    if not args.ohne_register and ziel.exists() and any(
            p.suffix == ".tex" for p in ziel.iterdir()):
        sys.exit(f"{ziel} enthält schon Quelltexte – nichts gebaut")
    dateien = bau.baue()
    texte = {k: "\n".join(v) + "\n" for k, v in dateien.items()}
    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur({k: v for k, v in texte.items()
                              if k != "vorspann.tex"}, sig)
    ziel.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(texte.items()):
        (ziel / name).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(vorlage, ziel / "mathblatt.sty")
    log(f"STRUKTUR {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        log(f"  FEHLER {name}:{zl}: {meldung}")
    (ziel / "zusammenbau.log").write_text("\n".join(log.zeilen) + "\n",
                                          encoding="utf-8", newline="\n")
    datum = heute()
    commit = bank_commit()
    try:
        pfad = ziel.resolve().relative_to(WURZEL).as_posix()
    except ValueError:
        pfad = ziel.resolve().as_posix()
    bestellung = {"kompetenz": bau.kette, "einheiten": str(bau.einheit),
                  "niveau": args.niveau, "dicht": args.dicht,
                  "ohne": args.ohne or None,
                  "aus": args.aus, "ohne_register": args.ohne_register}
    aufgaben = []
    for nr, b, z in bau.reihenfolge:
        aufgaben.append({"aufgabe": f"A{nr}", "hauptnummer": nr,
                         "teilaufgabe": b, "id": z["id"],
                         "datei": f"{args.kennung}.tex",
                         **bau.info.get(z["id"], {})})
    pr = [x for x in aufgaben if x.get("lage") == "pruefung"]
    zettel = {
        "kennung": args.kennung, "datum": datum, "eintraege": [args.eintrag],
        "titel": bau.titel, "thema": bau.thema, "kette": bau.kette,
        "einheit": bau.einheit, "einheit_katalog": bau.m,
        "einheit_katalog_quelle": bau.m_methode, "niveau": args.niveau,
        "zweigzeile": bau.zweig, "pruefwort": bau.pruefwort,
        "klasse_os": list(bau.klasse_os) if bau.klasse_os else None,
        "klasse_gym": list(bau.klasse_gym) if bau.klasse_gym else None,
        "zone": bau.zone_wahl, "kasten": bau.kasten_status,
        "hauptnummern": len({x["hauptnummer"] for x in aufgaben}),
        "teilaufgaben": len(aufgaben),
        "pruefungshoehe": len(pr),
        "originale": [x["original"] for x in pr],
        "jahrgaenge": sorted({str(x["jahr"]) for x in pr if x.get("jahr")}),
        "ersatzzeichen": "".join(bau.zeichen),
        "rezept": rezept, "rezept_name": REZEPT[rezept],
        "bestellung": bestellung, "bank_commit": commit,
        "zusammenbau": VERSION, "vorlage": version, "pfad": pfad,
        "kuerzel_quelle": k_quelle, "strukturfehler": len(fehler),
        "ausgelassen": sorted(bau.ohne), "aufgaben": aufgaben,
    }
    (ziel / "bau.json").write_text(
        json.dumps(zettel, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    if not args.ohne_register:
        haenge_an_register({
            "kennung": args.kennung, "datum": datum,
            "eintraege": args.eintrag, "rezept": rezept,
            "bestellung": ", ".join(
                f"{k}={'ja' if v is True else 'nein' if v is False else '–' if v is None else v}"
                for k, v in bestellung.items() if k != "ohne_register"),
            "bank_commit": commit, "zusammenbau": VERSION,
            "vorlage": version, "pfad": pfad})
        print(f"REGISTER {args.kennung} an bau/register.csv angehängt")
    print(f"KENNUNG {args.kennung} – {bau.titel}")
    print(f"{len(texte)} Quelltexte nach {ziel}; {zettel['hauptnummern']} "
          f"Hauptnummern, {len(aufgaben)} Teilaufgaben, Prüfungshöhe {len(pr)}; "
          f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


# --- Strukturprüfung ------------------------------------------------------

UMLAUT_ALT = re.compile(r"\\\"[aouAOUs]|\\ss\b|\\glqq|\\grqq|\\euro\b")

# Mathe-Modus: Befehle mit Text in den Argumenten (werden durchlaufen),
# Befehle mit Mathe im Argument, Textbefehle in Mathe, Ausrichtungen.
# Andere Bausteine (Grafik, Rahmen) werden samt Argumenten übergangen.
TEXT_ARG = {"teil", "steil", "tz", "stz", "swz", "swa", "swfrage", "erg",
            "abhak", "abhakgruppe", "uebersichtskasten", "einheitenkopf",
            "zweigzeile", "verz", "verzeichniszeile", "blattkopf",
            "leerfeld", "kreuz", "verfahren", "achtung",
            "kbtitel", "kbabschnitt", "kbanweisung", "kbteil", "kbfrage",
            "kbantwort", "kbzweispaltig", "kbdarunter", "kbkreuz", "kbmerk",
            "kbloesung", "kbkopfzeile", "kbspalte", "kbnummer", "kbhalb",
            "kbpaar", "kbteilpaar", "lbpaar"}
MATHE_ARG = {"gl", "sgl", "rechnung"}
TEXT_IN_MATHE = {"text", "textbf", "textit", "mbox", "emph"}
AUSRICHTUNG = {"tabular", "array", "aligned", "matrix", "pmatrix", "cases",
               "gleichungsraster"}
GRAFIK_UMGEBUNG = {"ksys", "ksys3", "boxplots", "kreis", "dreisatz",
                   "zahlengerade"}


def modusfehler(rein, zeile):
    """[(zeile, meldung)]: _ ^ # außerhalb Mathe, & außerhalb einer
    Ausrichtung, $ in Mathe-Argumenten, \\rechnung in Mathe."""
    aus = set()
    modus, gruppen, umg, naechste = ["t"], [], [], None
    k = 0
    while k < len(rein):
        c = rein[k]
        if c == "\\":
            m = re.match(r"\\(?:([A-Za-z]+)\*?|(.))", rein[k:], re.S)
            name, e = m.group(1), k + m.end()
            if name in ("begin", "end"):
                u = re.match(r"\{([^}]*)\}", rein[e:])
                if u:
                    if name == "begin" and u.group(1) in GRAFIK_UMGEBUNG:
                        j = rein.find("\\end{" + u.group(1) + "}", e)
                        k = len(rein) if j < 0 else j + len(u.group(1)) + 6
                        continue
                    if name == "begin":
                        umg.append(u.group(1))
                    elif umg and umg[-1] == u.group(1):
                        umg.pop()
                    e += u.end()
            elif name in MATHE_ARG:
                if name == "rechnung" and any(x != "t" for x in modus):
                    aus.add((zeile(k), "\\rechnung in Mathe oder \\text "
                             "(Absatz im Argument)"))
                naechste = "m"
            elif name in TEXT_IN_MATHE:
                if modus[-1] != "t":
                    naechste = "t"
            elif name and name not in TEXT_ARG and name not in BP.STANDARD:
                while e < len(rein) and rein[e] in "[{":
                    e = BP.klammer(rein, e)
            elif m.group(2) in ("(", "["):
                modus.append("m")
            elif m.group(2) in (")", "]") and len(modus) > 1:
                modus.pop()
            k = e
            continue
        if c == "{":
            gruppen.append(len(modus))
            if naechste:
                modus.append(naechste)
                naechste = None
        elif c == "}":
            if gruppen:
                del modus[max(gruppen.pop(), 1):]
        elif c == "$":
            if modus[-1] == "$":
                modus.pop()
            elif modus[-1] == "m":
                aus.add((zeile(k), "$ in einem Mathe-Argument (\\gl, "
                         "\\rechnung)"))
            else:
                modus.append("$")
        elif c in "_^" and modus[-1] == "t":
            aus.add((zeile(k), f"{c} außerhalb Mathe"))
        elif c == "#":
            aus.add((zeile(k), "# im Text"))
        elif c == "&" and modus[-1] == "t" and not (set(umg) & AUSRICHTUNG):
            aus.add((zeile(k), "& außerhalb einer Ausrichtung"))
        k += 1
    return sorted(aus)


def pruefe_struktur(dateien, sig):
    """[(datei, zeile, meldung)] für alle .tex-Texte {name: text}."""
    fehler = []
    for name in sorted(dateien):
        text = dateien[name]
        zeilen = text.split("\n")
        # Kommentarzeilen (ab Spalte 0 „%“) leeren, Länge bleibt
        rein = "\n".join(("" if z.startswith("%") else z) for z in zeilen)
        starts = [0]
        for z in rein.split("\n")[:-1]:
            starts.append(starts[-1] + len(z) + 1)

        def zeile(pos):
            return bisect_right(starts, pos)

        for i, z in enumerate(zeilen, 1):
            if z.startswith("%"):
                continue
            if re.search(r"(?<!\\)%", z):
                fehler.append((name, i, "nacktes % (Kommentar mitten in der Zeile)"))
            if UMLAUT_ALT.search(z):
                fehler.append((name, i, "Umlaut/Sonderzeichen nicht direkt: "
                               + UMLAUT_ALT.search(z).group(0)))
        # Klammern
        tiefe, offen = 0, []
        k = 0
        while k < len(rein):
            c = rein[k]
            if c == "\\":
                k += 2
                continue
            if c == "{":
                offen.append(k)
            elif c == "}":
                if offen:
                    offen.pop()
                else:
                    fehler.append((name, zeile(k), "schließende } ohne öffnende"))
            k += 1
        for p in offen:
            fehler.append((name, zeile(p), "öffnende { nicht geschlossen"))
        # Mathemodus
        dollar = [m.start() for m in re.finditer(r"(?<!\\)\$", rein)]
        if len(dollar) % 2:
            fehler.append((name, zeile(dollar[-1]), "ungerade Zahl von $"))
        fehler += [(name, zl, meldung) for zl, meldung in modusfehler(rein, zeile)]
        # Befehle und Umgebungen
        stapel = []
        teil_zaehler = None
        for m in re.finditer(r"\\(?:([A-Za-z]+)\*?|.)", rein):
            cmd = m.group(1)
            if not cmd:
                continue
            opt, pflicht = BP.argumente(rein, m.end())
            zl = zeile(m.start())
            if cmd in ("begin", "end"):
                if not pflicht:
                    fehler.append((name, zl, f"\\{cmd} ohne Umgebungsname"))
                    continue
                umg = pflicht[0]
                if cmd == "begin":
                    stapel.append((umg, zl))
                    if umg == "aufgabe":
                        teil_zaehler = 0
                    if umg in BP.UMGEBUNG_STANDARD or umg in RAHMEN_UMGEBUNG:
                        continue
                    key = "begin:" + umg
                    if key not in sig:
                        fehler.append((name, zl, f"Umgebung {umg} weder Standard "
                                       "noch Baustein"))
                    elif len(pflicht) - 1 not in sig[key]:
                        soll = "/".join(str(x) for x in sorted(sig[key]))
                        fehler.append((name, zl, f"\\begin{{{umg}}} mit "
                                       f"{len(pflicht) - 1} Argumenten, Anleitung {soll}"))
                else:
                    if not stapel:
                        fehler.append((name, zl, f"\\end{{{umg}}} ohne \\begin"))
                    elif stapel[-1][0] != umg:
                        fehler.append((name, zl, f"\\end{{{umg}}} schließt "
                                       f"\\begin{{{stapel[-1][0]}}} aus Zeile "
                                       f"{stapel[-1][1]}"))
                        stapel.pop()
                    else:
                        stapel.pop()
                    if umg == "aufgabe":
                        if teil_zaehler and teil_zaehler > 26:
                            fehler.append((name, zl, f"{teil_zaehler} Teilaufgaben "
                                           "in einer Hauptnummer (\\alph bis z)"))
                        teil_zaehler = None
                continue
            if teil_zaehler is not None and cmd in ("teil", "steil", "tz", "stz",
                                                    "swz", "swa", "swfrage",
                                                    "gl", "sgl"):
                teil_zaehler += 1
            if cmd in BP.STANDARD or cmd in RAHMEN:
                continue
            if cmd not in sig:
                fehler.append((name, zl, f"\\{cmd} weder Standard-LaTeX noch "
                               "Baustein aus _bausteine.md"))
            elif len(pflicht) not in sig[cmd]:
                soll = "/".join(str(x) for x in sorted(sig[cmd]))
                fehler.append((name, zl, f"\\{cmd} mit {len(pflicht)} Argumenten, "
                               f"Anleitung {soll}"))
        for umg, zl in stapel:
            fehler.append((name, zl, f"\\begin{{{umg}}} nicht geschlossen"))
    return fehler


# --- Hauptprogramm ---------------------------------------------------------

def finde_vorlage(angabe):
    kandidaten = []
    if angabe:
        kandidaten.append(Path(angabe))
    if os.environ.get("BLATTBAU"):
        kandidaten.append(Path(os.environ["BLATTBAU"]) / "mathblatt.sty")
    kandidaten += [WURZEL.parent / "hz-0801" / "blattbau" / "mathblatt.sty",
                   WURZEL.parent / "blattbau" / "mathblatt.sty"]
    for k in kandidaten:
        if k.is_file():
            return k
    sys.exit("mathblatt.sty nicht gefunden – hz-0801/blattbau klonen und "
             "--vorlage <pfad/mathblatt.sty> angeben")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("eintrag", nargs="*",
                   help="Eintrag; mit --heft mehrere in Heftfolge")
    p.add_argument("--zettel", choices=["basis"],
                   help="Rezept Z: Zettel mit zehn Basisaufgaben aus "
                        "bank/_basis/ (Kennung BAS-Z<n>)")
    p.add_argument("--nummer", type=int,
                   help="Zettel: Nummer n (sonst die nächste freie aus "
                        "bau/register.csv)")
    p.add_argument("--heft", nargs="?", const="msa", choices=sorted(HEFT_PROFIL),
                   help="Rezept H: Prüfungsheft (Profil, Voreinstellung msa)")
    p.add_argument("--nur-basis", action="store_true",
                   help="Heft: nur Originale aus dem Basisteil (OS/FOR/EBR, "
                        "id mit -B), ohne Anlauf")
    p.add_argument("--titel", help="Heft: Titel in Kopf und Fußzeile")
    p.add_argument("--einheiten", help="Auswahl, z. B. 1,3")
    p.add_argument("--zone", choices=["ja", "nein", "kurz"], default="ja")
    p.add_argument("--fokus-pruefung", metavar="KETTE",
                   help="Rezept P: Prüfungs-Fokus zu dieser Kette (Profil "
                        "über --heft, Einheit über --einheiten oder die erste "
                        "mit Prüfungshöhen)")
    p.add_argument("--kompetenz", metavar="KETTE",
                   help="Rezept K: Kompetenzblatt zu dieser Kette (Kennung "
                        "XXX-K<n>, Einheit über --einheiten)")
    p.add_argument("--niveau", choices=["for", "ebr"],
                   help="Kompetenzblatt: for mit Sternaufgaben (ohne "
                        "Kennzeichnung), ebr ohne sie; Voreinstellung for")
    p.add_argument("--dicht", action="store_true",
                   help="Kompetenzblatt: kurze Rechenaufgaben paarweise "
                        "nebeneinander (wenn das Blatt sonst über 4 Seiten hat)")
    p.add_argument("--ohne", metavar="IDS",
                   help="Kompetenzblatt: Bankzeilen (ids, Komma) weglassen – "
                        "etwa nach einem Kompilierfehler; Buchstaben neu")
    p.add_argument("--fokus", metavar="KETTE",
                   help="Kettenname wortgleich aus der Bank (Feld kette)")
    p.add_argument("--schwach", action="store_true")
    p.add_argument("--klasse", type=int)
    p.add_argument("--kasten", action="store_true",
                   help="Merkkasten am Anfang jeder Einheit (3.1 „mit kasten“)")
    p.add_argument("--aus", metavar="ORDNER",
                   help="Ausgabeordner statt bau/<eintrag>/<datum>/")
    p.add_argument("--vorlage", metavar="STY", help="Pfad zu mathblatt.sty")
    p.add_argument("--ohne-register", action="store_true",
                   help="Probe: keine Registerzeile, Kennung XXX-R0")
    p.add_argument("--kuerzel", metavar="CSV",
                   help="Pfad zu katalog/_kuerzel.csv (mathe-nachhilfe)")
    p.add_argument("--mit-sachaufgaben", action="store_true",
                   help="Lernblatt: alle Sachaufgaben der Ketten (sonst je "
                        "Kette höchstens eine Teilaufgabe mit Sachkontext)")
    args = p.parse_args(argv)
    if args.zettel:
        return main_zettel(args)
    if not args.eintrag:
        p.error("Eintrag fehlt (ohne --zettel)")
    if args.kompetenz:
        return main_kompetenz(args)
    if args.fokus_pruefung:
        return main_fokus_pruefung(args)
    if args.nur_basis and not args.heft:
        args.heft = "msa"
    if args.heft:
        return main_heft(args)
    if len(args.eintrag) > 1:
        sys.exit("mehrere Einträge nur mit --heft")
    args.eintrag = args.eintrag[0]
    if args.fokus and args.schwach:
        sys.exit("--fokus und --schwach zusammen kann v0.3 nicht")

    log = Log()
    aufruf = ["zusammenbau.py", args.eintrag]
    for name in ("einheiten", "zone", "fokus", "klasse", "nummer"):
        wert = getattr(args, name)
        if wert is not None and not (name == "zone" and wert == "ja"):
            aufruf += [f"--{name}", str(wert)]
    for name in ("schwach", "kasten", "mit_sachaufgaben"):
        if getattr(args, name):
            aufruf.append("--" + name.replace("_", "-"))
    if args.ohne_register:
        aufruf.append("--ohne-register")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))

    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version}")

    # Kennung: Kürzel des (ersten) Eintrags, Rezept, laufende Nummer
    if not (WURZEL / "bank" / args.eintrag).is_dir():
        sys.exit(f"bank/{args.eintrag}/ fehlt")
    eintraege = [args.eintrag]
    rezept = "F" if args.fokus else "S" if args.schwach else "L"
    kuerzel, k_quelle = kuerzel_von(eintraege[0],
                                    finde_kuerzelliste(args.kuerzel))
    register = lies_register()
    if args.nummer and not args.ohne_register:
        # v0.9: --nummer n wie im Kompetenzblatt (Kennung vorgegeben)
        nummer = args.nummer
    else:
        nummer = 0 if args.ohne_register else naechste_nummer(kuerzel, rezept,
                                                              register)
    args.kennung = f"{kuerzel}-{rezept}{nummer}"
    if not args.ohne_register and any(z.get("kennung") == args.kennung
                                      for z in register):
        sys.exit(f"{args.kennung} steht schon in bau/register.csv")
    log(f"KENNUNG {args.kennung} – Kürzel {kuerzel} aus {k_quelle}; Rezept "
        f"{rezept} ({REZEPT[rezept]}); "
        + ("ohne Register (Probe)" if args.ohne_register else
           f"Nummer {nummer} = vorgegeben (--nummer)" if args.nummer else
           f"Nummer {nummer} = nächste freie in bau/register.csv"))
    if k_quelle.startswith("Ersatz"):
        print(f"HINWEIS Kürzel {kuerzel}: {k_quelle}")

    if args.aus:
        ziel = Path(args.aus)
    else:
        ziel = WURZEL / "bau" / args.eintrag / args.kennung
    if not args.ohne_register and ziel.exists() and any(ziel.iterdir()):
        sys.exit(f"{ziel} ist nicht leer – Register und Ordner passen nicht "
                 "zusammen; nichts gebaut")

    bau = Bau(args, log)
    dateien = bau.baue()
    texte = {k: "\n".join(v) + "\n" for k, v in dateien.items()}

    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur({k: v for k, v in texte.items()
                              if k != "vorspann.tex"}, sig)

    ziel.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(texte.items()):
        (ziel / name).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(vorlage, ziel / "mathblatt.sty")

    todo = []
    for name, text in sorted(texte.items()):
        for i, z in enumerate(text.split("\n"), 1):
            if z.startswith("%% TODO"):
                todo.append(f"{name}:{i}: {z[3:]}")
    log(f"TODO {len(todo)} Stellen in den Quelltexten:")
    for t in todo:
        log("  " + t)
    log(f"STRUKTUR {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        log(f"  FEHLER {name}:{zl}: {meldung}")
    (ziel / "zusammenbau.log").write_text("\n".join(log.zeilen) + "\n",
                                          encoding="utf-8", newline="\n")

    # Bauzettel und Registerzeile
    datum = heute()
    commit = bank_commit()
    try:
        pfad = ziel.resolve().relative_to(WURZEL).as_posix()
    except ValueError:
        pfad = ziel.resolve().as_posix()
    bestellung = {
        "einheiten": args.einheiten or "alle",
        "zone": args.zone,
        "fokus": args.fokus,
        "schwach": args.schwach,
        "klasse": args.klasse,
        "kasten": args.kasten,
        "nummer": args.nummer,
        "aus": args.aus,
        "ohne_register": args.ohne_register,
    }
    if rezept == "L":
        # v1.0: Schalter nur im Lernblatt; vor ohne_register, damit die
        # Registerzeile ihn nennt
        bestellung = {k: v for k, v in bestellung.items()
                      if k != "ohne_register"}
        bestellung["mit_sachaufgaben"] = args.mit_sachaufgaben
        bestellung["ohne_register"] = args.ohne_register
    aufgaben = []
    # bau.json v0.9: lage in fünf Werten (Auftrag 30.09.), art wie bisher
    lage_von = {"zone": "zone", "zonepaar": "zone", "erkennung": "leiter",
                "vorstufe": "leiter", "leiter": "leiter", "ohne": "leiter",
                "pruefung": "pruefung", "pflicht": "pflicht",
                "pruefe-dich": "pruefe-dich", "test": "test"}
    for h, datei in bau.reihenfolge:
        for b, z in h.buchstaben:
            art = bau.lage.get(z["id"], h.lage) if z else None
            aufgaben.append({
                "aufgabe": f"A{h.nr}",
                "hauptnummer": h.nr,
                "teilaufgabe": b,
                "id": z["id"] if z else None,
                "datei": datei,
                **({"lage": lage_von.get(art, art), "art": art} if z else
                   {"hinweis": "Erklärzeile (schwach), keine Bankzeile"}),
            })
    je_einheit = {}
    for a in aufgaben:
        e = a["datei"].split("_")[0]
        d = je_einheit.setdefault(e, {"hauptnummern": set(),
                                      "teilaufgaben": 0})
        d["hauptnummern"].add(a["hauptnummer"])
        d["teilaufgaben"] += 1
    zettel = {
        "kennung": args.kennung,
        "datum": datum,
        "eintraege": eintraege,
        "rezept": rezept,
        "rezept_name": REZEPT[rezept],
        "bestellung": bestellung,
        "bank_commit": commit,
        "zusammenbau": VERSION,
        "vorlage": version,
        "pfad": pfad,
        "kuerzel_quelle": k_quelle,
        "strukturfehler": len(fehler),
        "hauptnummern": len({a["hauptnummer"] for a in aufgaben}),
        "teilaufgaben": len(aufgaben),
        "ersatzzeichen": "".join(bau.zeichen),
        "ichkann_fehlt": bau.ichkann_fehlt,
        "auftrag_doppelt": bau.auftrag_doppelt,
        "auftrag_satz_doppelt": bau.satz_doppelt,
        **({"titel_fehlt": bau.titel_fehlt, "gym": bau.gym,
            "sachkontext_ausgelassen": bau.sach_weg,
            "test": bau.test_wahl,
            "blattfolge": bau.einheiten_folge} if rezept == "L" else {}),
        "je_datei": {e: {"hauptnummern": len(d["hauptnummern"]),
                         "teilaufgaben": d["teilaufgaben"]}
                     for e, d in je_einheit.items()},
        "aufgaben": aufgaben,
    }
    (ziel / "bau.json").write_text(
        json.dumps(zettel, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    if not args.ohne_register:
        haenge_an_register({
            "kennung": args.kennung,
            "datum": datum,
            "eintraege": ",".join(eintraege),
            "rezept": rezept,
            "bestellung": ", ".join(
                f"{k}={'ja' if v is True else 'nein' if v is False else '–' if v is None else v}"
                for k, v in bestellung.items() if k != "ohne_register"),
            "bank_commit": commit,
            "zusammenbau": VERSION,
            "vorlage": version,
            "pfad": pfad,
        })
        print(f"REGISTER {args.kennung} an bau/register.csv angehängt")
    print(f"KENNUNG {args.kennung}")
    print(f"{len(texte)} Quelltexte nach {ziel}; {len(todo)} TODO; "
          f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


def main_heft(args):
    """Rezept H (v0.4): Prüfungsheft aus mehreren Einträgen."""
    log = Log()
    args.eintraege = list(args.eintrag)
    for name in ("fokus", "klasse", "einheiten"):
        if getattr(args, name) is not None:
            sys.exit(f"--{name} gibt es im Heft nicht")
    if args.schwach or args.kasten or args.zone != "ja":
        sys.exit("--schwach, --kasten, --zone gibt es im Heft nicht")
    if args.nur_basis and args.heft != "msa":
        sys.exit("--nur-basis nur mit dem Profil msa")
    aufruf = ["zusammenbau.py"] + args.eintraege + ["--heft", args.heft]
    if args.nur_basis:
        aufruf.append("--nur-basis")
    if args.titel:
        aufruf += ["--titel", args.titel]
    if args.ohne_register:
        aufruf.append("--ohne-register")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))
    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version}")
    vorhanden = [e for e in args.eintraege if (WURZEL / "bank" / e).is_dir()]
    if not vorhanden:
        sys.exit("kein Eintrag des Hefts liegt in bank/")
    rezept = "H"
    kuerzel, k_quelle = kuerzel_von(vorhanden[0],
                                    finde_kuerzelliste(args.kuerzel))
    nummer = 0 if args.ohne_register else naechste_nummer(kuerzel, rezept,
                                                          lies_register())
    args.kennung = f"{kuerzel}-{rezept}{nummer}"
    log(f"KENNUNG {args.kennung} – Kürzel {kuerzel} aus {k_quelle} (erster "
        f"Eintrag {vorhanden[0]}); Rezept H (Heft)")
    if not args.titel:
        args.titel = ("Prüfungsheft Basis" if args.nur_basis
                      else f"Prüfungsheft {HEFT_PROFIL[args.heft]}")
    ziel = (Path(args.aus) if args.aus
            else WURZEL / "bau" / "hefte" / args.kennung)
    if not args.ohne_register and ziel.exists() and any(
            p.suffix == ".tex" for p in ziel.iterdir()):
        sys.exit(f"{ziel} enthält schon Quelltexte – nichts gebaut")
    bau = HeftBau(args, log)
    dateien = bau.baue()
    texte = {k: "\n".join(v) + "\n" for k, v in dateien.items()}
    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur(texte, sig)
    ziel.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(texte.items()):
        (ziel / name).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(vorlage, ziel / "mathblatt.sty")
    log(f"STRUKTUR {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        log(f"  FEHLER {name}:{zl}: {meldung}")
    (ziel / "zusammenbau.log").write_text("\n".join(log.zeilen) + "\n",
                                          encoding="utf-8", newline="\n")
    datum = heute()
    commit = bank_commit()
    try:
        pfad = ziel.resolve().relative_to(WURZEL).as_posix()
    except ValueError:
        pfad = ziel.resolve().as_posix()
    bestellung = {"heft": args.heft, "nur_basis": args.nur_basis,
                  "titel": args.titel, "aus": args.aus,
                  "ohne_register": args.ohne_register}
    aufgaben = []
    for h, datei in bau.reihenfolge:
        for b, z in h.buchstaben:
            info = bau.info.get(z["id"], {})
            aufgaben.append({"aufgabe": f"A{h.nr}", "hauptnummer": h.nr,
                             "teilaufgabe": b, "id": z["id"], "datei": datei,
                             **info})
    zettel = {
        "kennung": args.kennung, "datum": datum,
        "eintraege": [e for e, _, _ in bau.eintraege],
        "fehlende_eintraege": bau.fehlend,
        "leere_eintraege": [e for e, _, _ in bau.eintraege
                            if e not in {t[1] for t in bau.teile}],
        "rezept": rezept, "rezept_name": REZEPT[rezept],
        "bestellung": bestellung, "bank_commit": commit,
        "zusammenbau": VERSION, "vorlage": version, "pfad": pfad,
        "kuerzel_quelle": k_quelle, "strukturfehler": len(fehler),
        "ausgelassen": [], "aufgaben": aufgaben,
    }
    (ziel / "bau.json").write_text(
        json.dumps(zettel, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    if not args.ohne_register:
        haenge_an_register({
            "kennung": args.kennung, "datum": datum,
            "eintraege": ",".join(e for e, _, _ in bau.eintraege),
            "rezept": rezept,
            "bestellung": ", ".join(
                f"{k}={'ja' if v is True else 'nein' if v is False else '–' if v is None else v}"
                for k, v in bestellung.items() if k != "ohne_register"),
            "bank_commit": commit, "zusammenbau": VERSION,
            "vorlage": version, "pfad": pfad})
        print(f"REGISTER {args.kennung} an bau/register.csv angehängt")
    print(f"KENNUNG {args.kennung}")
    print(f"{len(texte)} Quelltexte nach {ziel}; {len(aufgaben)} Teilaufgaben; "
          f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


def main_fokus_pruefung(args):
    """Rezept P (v0.6): Prüfungs-Fokus zu einer Kette."""
    log = Log()
    if len(args.eintrag) != 1:
        sys.exit("--fokus-pruefung: genau ein Eintrag")
    args.eintrag = args.eintrag[0]
    args.heft = args.heft or "msa"
    if args.fokus or args.schwach or args.nur_basis or args.klasse is not None \
            or args.zone != "ja" or args.titel:
        sys.exit("--fokus-pruefung verträgt nur --heft, --einheiten, --aus, "
                 "--vorlage, --kuerzel, --ohne-register")
    aufruf = ["zusammenbau.py", args.eintrag, "--fokus-pruefung",
              args.fokus_pruefung, "--heft", args.heft]
    if args.einheiten:
        aufruf += ["--einheiten", args.einheiten]
    if args.ohne_register:
        aufruf.append("--ohne-register")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))
    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version}")
    if not (WURZEL / "bank" / args.eintrag).is_dir():
        sys.exit(f"bank/{args.eintrag}/ fehlt")
    rezept = "P"
    kuerzel, k_quelle = kuerzel_von(args.eintrag,
                                    finde_kuerzelliste(args.kuerzel))
    nummer = 0 if args.ohne_register else naechste_nummer(kuerzel, rezept,
                                                          lies_register())
    args.kennung = f"{kuerzel}-{rezept}{nummer}"
    log(f"KENNUNG {args.kennung} – Kürzel {kuerzel} aus {k_quelle}; Rezept P "
        "(Prüfungs-Fokus)")
    bau = FokusPruefBau(args, log)
    ziel = (Path(args.aus) if args.aus
            else WURZEL / "bau" / "fokus" / args.kennung)
    if not args.ohne_register and ziel.exists() and any(
            p.suffix == ".tex" for p in ziel.iterdir()):
        sys.exit(f"{ziel} enthält schon Quelltexte – nichts gebaut")
    dateien = bau.baue()
    texte = {k: "\n".join(v) + "\n" for k, v in dateien.items()}
    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur(texte, sig)
    ziel.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(texte.items()):
        (ziel / name).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(vorlage, ziel / "mathblatt.sty")
    log(f"STRUKTUR {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        log(f"  FEHLER {name}:{zl}: {meldung}")
    (ziel / "zusammenbau.log").write_text("\n".join(log.zeilen) + "\n",
                                          encoding="utf-8", newline="\n")
    datum = heute()
    commit = bank_commit()
    try:
        pfad = ziel.resolve().relative_to(WURZEL).as_posix()
    except ValueError:
        pfad = ziel.resolve().as_posix()
    bestellung = {"fokus_pruefung": bau.kette, "heft": args.heft,
                  "einheiten": str(bau.einheit), "aus": args.aus,
                  "ohne_register": args.ohne_register}
    aufgaben = []
    for h, datei in bau.reihenfolge:
        for b, z in h.buchstaben:
            aufgaben.append({"aufgabe": f"A{h.nr}", "hauptnummer": h.nr,
                             "teilaufgabe": b, "id": z["id"], "datei": datei,
                             **bau.info.get(z["id"], {})})
    pr = [a for a in aufgaben if a.get("lage") == "pruefung"]
    zettel = {
        "kennung": args.kennung, "datum": datum, "eintraege": [args.eintrag],
        "titel": bau.titel, "kette": bau.kette, "einheit": bau.einheit,
        "profil": args.heft, "pruefwort": bau.pruefwort,
        "kasten": bau.kasten_status or "fehlt in der Mappe",
        "anlauf": sum(1 for a in aufgaben if a.get("lage") == "anlauf"),
        "pruefungshoehe": len(pr),
        "originale": sorted({a["original"] for a in pr if a.get("original")}),
        "jahrgaenge": sorted({str(a["jahr"]) for a in pr if a.get("jahr")}),
        "rezept": rezept, "rezept_name": REZEPT[rezept],
        "bestellung": bestellung, "bank_commit": commit,
        "zusammenbau": VERSION, "vorlage": version, "pfad": pfad,
        "kuerzel_quelle": k_quelle, "strukturfehler": len(fehler),
        "ausgelassen": [], "aufgaben": aufgaben,
    }
    (ziel / "bau.json").write_text(
        json.dumps(zettel, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    if not args.ohne_register:
        haenge_an_register({
            "kennung": args.kennung, "datum": datum,
            "eintraege": args.eintrag, "rezept": rezept,
            "bestellung": ", ".join(
                f"{k}={'ja' if v is True else 'nein' if v is False else '–' if v is None else v}"
                for k, v in bestellung.items() if k != "ohne_register"),
            "bank_commit": commit, "zusammenbau": VERSION,
            "vorlage": version, "pfad": pfad})
        print(f"REGISTER {args.kennung} an bau/register.csv angehängt")
    print(f"KENNUNG {args.kennung} – {bau.titel}")
    print(f"{len(texte)} Quelltexte nach {ziel}; Anlauf {zettel['anlauf']}, "
          f"Prüfungshöhe {len(pr)}, Originale {len(zettel['originale'])}; "
          f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


# --- Rezept Zettel (v0.5) ----------------------------------------------------
#
# Beschluss des Lehrers vom 28.09.: Basisaufgaben (Teil A der P10, ohne
# Rechner) werden getrennt geübt – am Stundenanfang ein Zettel mit zehn
# kurzen Aufgaben, je Stunde ein neuer, ohne Wiederholung. Der Inhalt von
# Zettel n hängt nur vom Vorrat (bank/_basis/) und von n ab: der Plan wird
# von Zettel 1 bis n durchgerechnet.

BASIS = WURZEL / "bank" / "_basis"
ZETTEL_ZAHL = 10          # Aufgaben je Zettel
JAHRGAENGE_ALLE = 13      # P10 2014–2026
GROSS_HOECHSTENS = 2      # große Grafiken (ksys, Wertetabellen) je Zettel
GROSS = re.compile(r"\\begin\{ksys\}|\\wertetabelle")
SEITE_CM = 25.0           # geschätzte Höhe aller zehn Aufgaben höchstens
ZEILE_CM = 1.45           # kleinste geschätzte Höhe einer Aufgabe


def zettel_hoehe(z):
    """Geschätzte Höhe einer Aufgabe auf dem Zettel in cm (geeicht an 41
    Probezetteln vom 28.09.: bis 25 cm blieb jeder auf einer Seite).
    Text: Zeichen ohne Formeln und Befehle, 92 je volle Zeile, 52 neben
    einer Grafik; Grafik nach Baustein; Text und Grafik nebeneinander
    zählen einmal (das Höhere)."""
    g = z.get("grafik", "")
    t = re.sub(r"\\kreuz\{[^{}]*\}", "X" * 8, z["aufgabe"])
    t = re.sub(r"\$[^$]*\$", "XXXX", t)
    t = re.sub(r"\\[A-Za-z]+", "", t)
    unter = not g or "\\quad" in g or "\\wertetabelle" in g
    zeilen = len(t) // (92 if unter else 52) + 1
    text = (zeilen * 0.5 + (0.6 if z.get("antwort") else 0)
            + (0.5 if "\\kreuz" in z["aufgabe"] else 0))
    if not g:
        bild = 0
    elif "ksys" in g:
        bild = 4.1
    elif "\\wertetabelle" in g:
        bild = 3.9
    elif "parallelenpaar" in g:
        bild = 3.9
    elif "\\quad" in g:
        bild = 2.0
    elif "kreissektor" in g:
        bild = 2.8
    elif "array" in g:
        bild = 0.5 * (g.count("\\\\") + 1)
    else:
        bild = 2.9
    return (text + bild if unter else max(text, bild)) + 0.45
# Reihenfolge auf dem Zettel: nach Bereich wie im Basisteil der P10
ZETTEL_FOLGE = ["brueche-dezimalzahlen", "rationale-zahlen", "potenzen-wurzeln",
                "prozentrechnung", "zinsrechnung", "einheiten", "zuordnungen",
                "terme", "lineare-gleichungen", "quadratische-gleichungen",
                "lineare-funktionen", "quadratische-funktionen",
                "symmetrie-abbildungen", "winkel-dreiecke", "flaechen", "kreis",
                "koerper", "trigonometrie", "bruchrechnung", "daten",
                "wahrscheinlichkeit"]


def lies_vorrat():
    """(typen, vorrat): typen aus bank/_basis/typen.csv (Liste von dicts mit
    jahrgaenge als int), vorrat {typ: [Zeilen nach Variante]}."""
    with open(BASIS / "typen.csv", encoding="utf-8", newline="") as f:
        typen = list(csv.DictReader(f, delimiter=";"))
    for t in typen:
        t["jahrgaenge"] = int(t["jahrgaenge"])
    vorrat = {}
    for p in sorted(BASIS.glob("*.jsonl")):
        for z in lies_jsonl(p):
            vorrat.setdefault(z["kette"], []).append(z)
    for zz in vorrat.values():
        zz.sort(key=lambda z: z["variante"])
    typen = [t for t in typen if vorrat.get(t["typ"])]
    return typen, vorrat


def zettel_plan(typen, vorrat, bis):
    """[[(typ, zeile)] je Zettel 1..bis] und die Nummer des ersten Zettels,
    für den der Vorrat nicht mehr reicht (None, wenn er bis dahin reicht).

    Gewicht eines Typs = Zahl der Jahrgänge (typen.csv). Typen, die in
    allen 13 Jahrgängen vorkommen, stehen auf jedem Zettel; die übrigen
    Plätze gehen nach Stride-Verfahren im Wechsel: jeder Typ hat einen
    Stand, gewählt werden die kleinsten Stände (bei Gleichstand das größere
    Gewicht, dann die Folge in typen.csv), nach der Wahl steigt der Stand
    um 1/Gewicht. So kommt ein Typ mit neun Jahrgängen neunmal so oft wie
    einer mit einem. Startstand: die Typen gleichen Gewichts w (Anzahl m,
    i-ter in typen.csv) beginnen gestaffelt bei (i + 0,5) / (m · w); so
    mischen sich häufige und seltene Typen von Zettel 1 an, statt dass die
    seltenen alle vorn oder alle hinten stehen. Je Typ höchstens eine Aufgabe je Zettel; der
    k-te Einsatz eines Typs nimmt Variante k, keine Aufgabe zweimal.
    Höchstens zwei große Grafiken (Koordinatensystem, Wertetabellen) je
    Zettel und geschätzte Höhe höchstens SEITE_CM, damit er auf eine Seite
    passt: ein Typ, der nicht mehr passt, wartet auf den nächsten Zettel
    (sein Stand bleibt, er kommt dann zuerst). Geht das gegen Ende des
    Vorrats nicht mehr auf, wird ohne Maß gewählt (die log nennt die
    geschätzte Höhe); erschöpft ist der Vorrat erst, wenn weniger als zehn
    Typen übrig sind."""
    gleich = {}
    for t in typen:
        gleich.setdefault(t["jahrgaenge"], []).append(t["typ"])
    stand = {}
    for w, reihe in gleich.items():
        for i, t in enumerate(reihe):
            stand[t] = (i + 0.5) / (len(reihe) * w)
    genutzt = {t["typ"]: 0 for t in typen}
    rang = {t["typ"]: i for i, t in enumerate(typen)}
    gewicht = {t["typ"]: t["jahrgaenge"] for t in typen}
    plan = []
    for n in range(1, bis + 1):
        frei = [t for t in stand if genutzt[t] < len(vorrat[t])]
        if len(frei) < ZETTEL_ZAHL:
            return plan, n
        pflicht = [t for t in frei if gewicht[t] >= JAHRGAENGE_ALLE]
        rest = sorted((t for t in frei if t not in pflicht),
                      key=lambda t: (stand[t], -gewicht[t], rang[t]))
        for streng in (True, False):
            wahl, gross, hoehe = [], 0, 0.0
            for t in pflicht + rest:
                z = vorrat[t][genutzt[t]]
                g = bool(GROSS.search(z.get("grafik", "")))
                h = zettel_hoehe(z)
                # Platz für die noch offenen Plätze freihalten (je ZEILE_CM)
                offen = ZETTEL_ZAHL - len(wahl) - 1
                if len(wahl) == ZETTEL_ZAHL or (streng and t not in pflicht
                        and ((g and gross >= GROSS_HOECHSTENS)
                             or hoehe + h + offen * ZEILE_CM > SEITE_CM)):
                    continue
                wahl.append(t)
                gross += g
                hoehe += h
            if len(wahl) == ZETTEL_ZAHL:
                break
        # ohne Maß (streng False) nur, wenn der Rest des Vorrats nicht anders
        # passt; die log des Zettels nennt dann die geschätzte Höhe
        zettel = []
        for t in wahl:
            zettel.append((t, vorrat[t][genutzt[t]]))
            genutzt[t] += 1
            stand[t] += 1 / gewicht[t]
        plan.append(zettel)
    return plan, None


def zettel_erschoepft(typen, vorrat):
    """Nummer des ersten Zettels, für den der Vorrat nicht reicht."""
    gesamt = sum(len(v) for v in vorrat.values())
    _, ab = zettel_plan(typen, vorrat, gesamt // ZETTEL_ZAHL + 2)
    return ab


def zettel_satz(nr, typ, z, log):
    """Eine Hauptnummer des Zettels: Text (mit Feld und Kennung) links,
    Grafik rechts; eine Reihe von Figuren (Grafik mit \\quad) darunter."""
    feld = "" if feld_im_grafik(z) else antwortfeld(z.get("antwort", ""))
    aufgabe, _ = mit_kennung(z["aufgabe"], bool(feld), z)
    # kurze Ankreuzoptionen in einer Zeile (Platz: ein Zettel ist eine Seite)
    opt = re.findall(r"\\kreuz\{((?:[^{}]|\{[^{}]*\})*)\}", aufgabe)
    if len(opt) > 1 and sum(len(o) for o in opt) <= 70:
        teile = re.split(r"\s*\\\\\s*(?=\\kreuz\{)", aufgabe)
        aufgabe = teile[0] + " \\\\ " + " ".join(t.strip() for t in teile[1:])
        log(f"SATZ Nr. {nr}: {len(opt)} kurze Ankreuzoptionen in einer Zeile")
    text = aufgabe + (f" {feld}" if feld else "")
    grafik = z.get("grafik", "")
    if ",ablesen]" in grafik:
        # Ablesegrafik (Karo 6 mm, 6 cm hoch) in der kleinen Form (Karo
        # 3,5 mm): zwei Koordinatensysteme passen sonst nicht auf eine Seite
        grafik = grafik.replace(",ablesen]", ",klein]")
        log(f"SATZ Nr. {nr}: ksys ablesen → klein (Karo 3,5 mm)")
    kopf = [f"% {nr}: {typ} – {z['id']} (Original "
            f"{(z.get('original') or {}).get('id')})"]
    if not grafik:
        return kopf + [f"\\begin{{aufgabe}}{{{text}}}", "\\end{aufgabe}"]
    if "\\quad" in grafik or "\\wertetabelle" in grafik:
        log(f"SATZ Nr. {nr}: Grafik unter dem Text (Reihe von Figuren)")
        return kopf + [f"\\begin{{aufgabe}}{{{text}}}", "", grafik,
                       "\\end{aufgabe}"]
    return kopf + [
        "\\begin{aufgabe}{\\begin{minipage}[t]{0.6\\linewidth}"
        f"{text}\\end{{minipage}}\\hfill"
        "\\begin{minipage}[t]{0.37\\linewidth}\\vspace{0pt}",
        grafik,
        "\\end{minipage}}", "\\end{aufgabe}"]


def main_zettel(args):
    """Rezept Z (v0.5): Zettel mit zehn Basisaufgaben, BAS-Z<n>."""
    log = Log()
    if args.eintrag or args.heft or args.fokus or args.schwach:
        sys.exit("--zettel nimmt keinen Eintrag und kein anderes Rezept")
    typen, vorrat = lies_vorrat()
    if not typen:
        sys.exit("bank/_basis/ ist leer – kein Vorrat")
    kuerzel, rezept = "BAS", "Z"
    register = lies_register()
    nummer = args.nummer or naechste_nummer(kuerzel, rezept, register)
    kennung = f"{kuerzel}-{rezept}{0 if args.ohne_register else nummer}"
    aufruf = ["zusammenbau.py", "--zettel", args.zettel]
    if args.nummer:
        aufruf += ["--nummer", str(args.nummer)]
    if args.ohne_register:
        aufruf.append("--ohne-register")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))
    ab = zettel_erschoepft(typen, vorrat)
    log(f"VORRAT {len(typen)} Typen, {sum(len(v) for v in vorrat.values())} "
        f"Aufgaben; Vorrat erschöpft ab Zettel {ab}")
    if ab is not None and nummer >= ab:
        print(f"Vorrat erschöpft ab Zettel {ab} – Zettel {nummer} nicht gebaut")
        return 1
    if (not args.ohne_register and args.nummer
            and any(z.get("kennung") == kennung for z in register)):
        sys.exit(f"{kennung} steht schon in bau/register.csv – nichts gebaut")
    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version}")
    log(f"KENNUNG {kennung} – Kürzel BAS (Basisvorrat, fest), Rezept Z "
        f"(Zettel); Inhalt von Zettel {nummer}"
        + (" (Probe ohne Register)" if args.ohne_register else
           "" if args.nummer else " = nächste freie Nummer in bau/register.csv"))
    plan, _ = zettel_plan(typen, vorrat, nummer)
    zettel = plan[-1]
    info = {t["typ"]: t for t in typen}

    def folge(tz):
        e = tz[1]["eintrag"]
        return (ZETTEL_FOLGE.index(e) if e in ZETTEL_FOLGE else 99, e,
                tz[1]["kette_nr"])
    zettel = sorted(zettel, key=folge)
    geschaetzt = sum(zettel_hoehe(z) for _, z in zettel)
    log(f"HÖHE geschätzt {geschaetzt:.1f} cm (Maß {SEITE_CM} cm)"
        + (" – ÜBER DEM MASS, Render prüfen" if geschaetzt > SEITE_CM else ""))
    a = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}",
         "\\begin{document}",
         f"\\blattkopf*{{Basisaufgaben}}{{{kennung}}}"
         f"{{Basisaufgaben · Zettel · {kennung}}}",
         f"\\einheitenkopf[][Zettel {nummer}]{{Basisaufgaben · Zettel "
         f"{nummer}}}",
         "\\zweigzeile{ohne Taschenrechner · je Aufgabe 1 Punkt · Lösungen "
         "auf der Rückseite}",
         "% \\small: zehn Aufgaben mit bis zu zwei Koordinatensystemen auf "
         "einer Seite (Render 28.09.)", "\\small", ""]
    l = ["\\begleitteil"]
    aufgaben = []
    for i, (typ, z) in enumerate(zettel, 1):
        a += zettel_satz(i, typ, z, log) + [""]
        l.append(f"\\erg{{{i}}}{{{z['loesung']}}}")
        t = info[typ]
        log(f"AUSWAHL Nr. {i}: {z['id']} – {typ} (Jahrgänge {t['jahrgaenge']}, "
            f"Variante {z['variante']})")
        aufgaben.append({"aufgabe": f"A{i}", "hauptnummer": i,
                         "id": z["id"], "kette": typ,
                         "jahrgaenge": t["jahrgaenge"],
                         "variante": z["variante"],
                         "original": (z.get("original") or {}).get("id")})
    texte = {f"{kennung}.tex": "\n".join(a + l + ["\\end{document}"]) + "\n"}
    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur(texte, sig)
    ziel = Path(args.aus) if args.aus else WURZEL / "bau" / "zettel" / kennung
    if not args.ohne_register and ziel.exists() and any(ziel.iterdir()):
        sys.exit(f"{ziel} ist nicht leer – nichts gebaut")
    ziel.mkdir(parents=True, exist_ok=True)
    for name, text in texte.items():
        (ziel / name).write_text(text, encoding="utf-8", newline="\n")
    shutil.copyfile(vorlage, ziel / "mathblatt.sty")
    log(f"STRUKTUR {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        log(f"  FEHLER {name}:{zl}: {meldung}")
    (ziel / "zusammenbau.log").write_text("\n".join(log.zeilen) + "\n",
                                          encoding="utf-8", newline="\n")
    datum = heute()
    commit = bank_commit()
    try:
        pfad = ziel.resolve().relative_to(WURZEL).as_posix()
    except ValueError:
        pfad = ziel.resolve().as_posix()
    bestellung = {"zettel": args.zettel, "nummer": nummer,
                  "ohne_register": args.ohne_register}
    bauzettel = {
        "kennung": kennung, "datum": datum, "eintraege": ["_basis"],
        "rezept": rezept, "rezept_name": REZEPT[rezept],
        "bestellung": bestellung, "bank_commit": commit,
        "zusammenbau": VERSION, "vorlage": version, "pfad": pfad,
        "kuerzel_quelle": "fest (Basisvorrat)", "strukturfehler": len(fehler),
        "vorrat_erschoepft_ab": ab, "aufgaben": aufgaben}
    (ziel / "bau.json").write_text(
        json.dumps(bauzettel, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8", newline="\n")
    if not args.ohne_register:
        haenge_an_register({
            "kennung": kennung, "datum": datum, "eintraege": "_basis",
            "rezept": rezept,
            "bestellung": f"zettel={args.zettel}, nummer={nummer}",
            "bank_commit": commit, "zusammenbau": VERSION,
            "vorlage": version, "pfad": pfad})
        print(f"REGISTER {kennung} an bau/register.csv angehängt")
    print(f"KENNUNG {kennung}")
    print(f"{len(texte)} Quelltext nach {ziel}; Typen: "
          + "; ".join(t for t, _ in zettel))
    print(f"Vorrat erschöpft ab Zettel {ab}")
    print(f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""zusammenbau.py v0.7 – aus bank/<eintrag>/ LaTeX-Quelltexte für mathblatt.sty.

Aufruf:
    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach] [--klasse 7]
        [--kasten] [--aus <ordner>] [--vorlage <mathblatt.sty>]
        [--ohne-register] [--kuerzel <_kuerzel.csv>]
    python3 werkzeuge/zusammenbau.py <eintrag> <eintrag> … --heft [msa|
        abitur-gk|abitur-lk|fhr] [--nur-basis] [--titel <text>] --aus <ordner>
    python3 werkzeuge/zusammenbau.py --zettel basis [--nummer n]
        [--ohne-register]
    python3 werkzeuge/zusammenbau.py <eintrag> --fokus-pruefung <kette>
        [--heft msa|abitur-gk|abitur-lk|fhr] [--einheiten n] [--aus <ordner>]
    python3 werkzeuge/zusammenbau.py <eintrag> --kompetenz <kette>
        --einheiten n [--niveau for|ebr] [--dicht] [--ohne <ids>]

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

Ohne Schalter: Lernblatt mit Zone und allen Einheiten, je Sprosse
Variante 1, ohne Klasse. Jeder Bau bekommt eine Kennung XXX-R<n>
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
import json
import os
import re
import shutil
import subprocess
import sys
from bisect import bisect_right
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
VERSION = "v0.7"

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


# --- Mappe ---------------------------------------------------------------

class Mappe:
    """Abschnitt 1 der Mappe: Thema, Lerneinheiten mit Marken,
    Voraussetzungen, Merkkästen. Was nicht passt, bleibt None."""

    def __init__(self, pfad, log):
        self.thema = None
        self.einheiten = {}      # n -> {"titel", "marken"}
        self.fertigkeiten = []   # (text vor „ – “, Einheitenangabe, {n})
        self.kasten = {}         # n -> [Zeilen]
        self.sprossen = {}       # Kette (casefold) -> n, aus „Sprossen je Verfahrenstyp“ (v0.7)
        self.typen = {}          # n -> Text der Zeile „Typen je Lerneinheit“ (v0.7)
        self.fertigkeit_zeilen = []  # ganze Voraussetzungszeilen (v0.7)
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
        for z in block.get("Typen je Lerneinheit", []):
            m = re.match(r"^Einheit (\d+): (.+)$", z)
            if m:
                self.typen[int(m.group(1))] = m.group(2)

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


class Bau:
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
        self.todo_frei = []
        self.reihenfolge = []   # (Hauptnummer, Aufgabendatei) in Blattfolge

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
        return alle

    def hauptnummern_einheit(self, n):
        log = self.log
        aus = []
        for nr, name, art, zeilen in ketten_von(self.e[n]):
            wo = f"e{n} k{nr} „{name}“ ({art})"
            if self.fokus:
                if name.casefold() != self.fokus.casefold():
                    log(f"WEG {wo} – Fokus: andere Kette entfällt")
                    continue
                folge = sorted(zeilen, key=lambda z: (z["sprosse"], z["variante"]))
                for z in folge:
                    log(f"AUSWAHL {z['id']} – {wo}: Fokus, alle Varianten")
                teile = teile_nach_mass(folge)
                if len(teile) > 1:
                    log(f"TEILUNG {wo}: {len(folge)} Teilaufgaben in "
                        f"{len(teile)} Hauptnummern an Sprossengrenzen "
                        "(unterrichtsblatt 2.3 g, 2.5)")
                for i, t in enumerate(teile):
                    if art == "pflicht":
                        titel = platzhalter_titel(name, art, t)
                    else:
                        titel = platzhalter_titel(name, art, folge) \
                            + (" – weiter" if i else "")
                    aus.append(Hauptnummer(titel, t, art, name, n,
                                           weiter=bool(i)))
                continue
            if self.schwach and art == "verfahren":
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
            aus.append(Hauptnummer(platzhalter_titel(name, art, folge),
                                   folge, art, name, n))
            log(f"KETTE {wo} → eine Hauptnummer"
                + (" (Erkennungsschritt: eigene Kette nach bank.md, zählt "
                   "als Hauptnummer)" if art == "erkennung" else ""))
        return aus

    def hauptnummern_zone(self, gewaehlt):
        log = self.log
        if self.a.zone == "nein" or not self.zone:
            if not self.zone:
                log("ZONE: zone.jsonl fehlt")
            return []
        aus, paar = [], []
        paar_weg = [z for z in self.zone if z["hoehe"] == "pflicht"
                    and z.get("pflicht") == "fehler"]
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
            paar += [z for z in zeilen if z["hoehe"] == "pflicht"
                     and z.get("pflicht") == "fehler"]
            s1 = [z for z in zeilen if z["sprosse"] == 1 and z["hoehe"] != "pflicht"]
            s2 = [z for z in zeilen if z["sprosse"] == 2 and z["hoehe"] != "pflicht"]
            folge = je_sprosse_erste(s1, log, wo)
            if self.a.zone == "ja":
                folge += je_sprosse_erste(s2, log, wo)
            else:
                log(f"ZONE {wo}: kurz – nur Sprosse 1")
            ueber = sorted({z["sprosse"] for z in zeilen} - {1, 2})
            if ueber:
                log(f"WEG {wo} – Sprossen {ueber} (Fallstricke) nicht bestellt "
                    f"(Zone {self.a.zone}: s1" + (" und s2)" if self.a.zone == "ja" else ")"))
            aus.append(Hauptnummer(name, folge, "zone", name, 0))
        if self.a.zone == "ja":
            if paar:
                f = paar[0]
                folgezeile = [z for z in self.zone if z["kette_nr"] == f["kette_nr"]
                              and z["sprosse"] == f["sprosse"] + 1]
                aus.append(Hauptnummer(f"{f['kette']} – Fehler finden", [f],
                                       "zonepaar", f["kette"], 0))
                log(f"AUSWAHL {f['id']} – Zone-Paar, Fehler finden")
                if folgezeile:
                    aus.append(Hauptnummer(f"{f['kette']} – selbst rechnen",
                                           [folgezeile[0]], "zonepaar",
                                           f["kette"], 0))
                    log(f"AUSWAHL {folgezeile[0]['id']} – Zone-Paar, "
                        "gleichartige Rechenaufgabe")
            elif paar_weg:
                log(f"WEG {paar_weg[0]['id']} – Zone-Paar: Fertigkeit "
                    "„" + paar_weg[0]["kette"][:40] + "“ nicht bestellt")
            else:
                log("TODO Zone-Paar (Fehler finden + gleichartige Rechnung, "
                    "unterrichtsblatt 2.2) fehlt in zone.jsonl")
                self.todo_frei.append("zonepaar")
        return aus

    # Satz
    def satz_hauptnummer(self, h):
        aus = []
        titel = klar(h.titel)
        aus.append(f"%% TODO Titel: Ich-kann-Satz fehlt in der Bank "
                   f"(Platzhalter: Kettenname) – Nr. {h.nr}")
        aus.append(f"%% TODO Anweisung: ein Satz über der ersten Teilaufgabe "
                   f"fehlt in der Bank – Nr. {h.nr}")
        aus.append(f"\\begin{{aufgabe}}{{{titel}}}")
        if h.art == "verfahren" and not h.weiter and not self.schwach:
            aus.append("%% TODO \\rechenplatz{n}: Schrittzahl des Grundfalls "
                       "fehlt in der Bank (nur bei fester Schreibform, 2.3 b)")
        folge = h.folge
        h.buchstaben = []
        i = 0
        if self.schwach:
            for z in folge:
                if z.get("paeckchen"):
                    aus.append("\\swfrage{Was bleibt gleich, was ändert sich?}")
                    h.buchstaben.append((buchstabe(i), None))
                    i += 1
                    continue
                zeilen, _ = teil_schwach(z, self.log, h.nr)
                aus += zeilen
                h.buchstaben.append((buchstabe(i), z))
                i += 1
        else:
            aus += teile_normal(folge)
            for z in folge:
                h.buchstaben.append((buchstabe(i), z))
                i += 1
        aus.append("\\end{aufgabe}")
        # Maß 2.3 g
        n_teil = len(h.buchstaben)
        n_graf = sum(1 for _, z in h.buchstaben if z and z.get("grafik"))
        if n_teil > 26:
            self.log(f"FEHLER Nr. {h.nr}: {n_teil} Teilaufgaben > 26 (\\alph)")
        if (n_graf == 0 and n_teil > 12) or (n_graf > 0 and n_teil > 6):
            self.log(f"WARNUNG Nr. {h.nr}: {n_teil} Teilaufgaben, {n_graf} "
                     "mit Grafik – über dem Halbseitenmaß (2.3 g); v0.1 teilt "
                     "nur im Fokus")
        return aus

    def satz_loesung(self, h):
        teile = []
        vor = []
        for b, z in h.buchstaben:
            if z is None:
                teile.append(f"{b}) \\ldots")
                vor.append(f"%% TODO Lösung der Erklärzeile {h.nr}{b}) "
                           "fehlt in der Bank")
                continue
            teile.append(f"{b}) {z['loesung']}")
        aus = vor + [f"\\erg{{{h.nr}}}{{" + " \\quad ".join(teile) + "}"]
        for b, z in h.buchstaben:
            if z and z.get("loesungsgrafik"):
                aus += ["", f"{h.nr}{b})", "", z["loesungsgrafik"], ""]
        return aus

    def kasten(self, n):
        zeilen = self.mappe.kasten.get(n)
        if not zeilen:
            return [f"%% TODO Merkkasten Einheit {n} nicht in der Mappe lesbar"]
        aus = []
        if len(zeilen) > 5:
            aus.append(f"%% TODO Merkkasten Einheit {n}: {len(zeilen)} Zeilen, "
                       "Vorgabe höchstens fünf (3.1)")
        inhalt = [re.sub(r"\s{3,}", r" \\quad ", klar(z.replace("&", "und")))
                  for z in zeilen]
        aus.append("\\uebersichtskasten{" + " \\\\ ".join(inhalt) + "}")
        return aus

    def kopf(self, n, pos, anzahl):
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
        aus.append(f"\\einheitenkopf[e{n}]{{{text}}}")
        os_, gym, wort = marke_zerlegen(info["marken"] if info else None)
        wort = pruefwort_zahl(info["marken"] if info else None,
                              self.e.get(n, []), self.log) or wort
        zm = zeitmarke(os_, gym, self.klasse)
        teile = []
        aus.insert(0, f"%% TODO Zweigzeile Teil 1: was hier gelernt wird "
                      f"(Satz in Schülersprache aus dem Einheitstitel) – Einheit {n}")
        if zm:
            teile.append(zm)
        else:
            aus.insert(0, f"%% TODO Zeitmarke Einheit {n}: Marken-Zeile nicht lesbar")
        if wort:
            teile.append(wort)
        else:
            aus.insert(0, f"%% TODO Prüfungswort Einheit {n}: nicht in der Marken-Zeile")
        if teile:
            aus.append("\\zweigzeile{" + " · ".join(teile) + "}")
        self.log(f"KOPF Einheit {n}: „{text}“; Marken „{info['marken'] if info else None}“"
                 f" → Zeitmarke „{zm}“, Prüfungswort „{wort}“")
        return aus, titel

    def baue(self):
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
        dateien = {}
        # Zone
        if zone:
            a = ["% Zone „Das kennst du schon“ – aus bank/"
                 f"{self.eintrag}/zone.jsonl (zusammenbau {VERSION})",
                 "\\einheitenkopf[zone][Kennst du schon]{Das kennst du schon}",
                 "\\setcounter{aufgabe}{0}"]
            if self.schwach:
                a.append("%% TODO Grundvorstellungs-Aufgabe als erste Hauptnummer "
                         "der Zone (2.8) fehlt in der Bank")
            if "zonepaar" in self.todo_frei:
                pass
            for h in zone:
                a.append("")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, "blatt0_a.tex"))
            if "zonepaar" in self.todo_frei:
                a += ["", "%% TODO Zone-Paar (Fehler finden + gleichartige "
                      "Rechenaufgabe, 2.2) fehlt in zone.jsonl"]
            dateien["blatt0_a.tex"] = a
            l = ["% Lösungen Zone (zusammenbau " + VERSION + ")",
                 "\\einheitenkopf[][Kennst du schon]{Das kennst du schon}"]
            zuordnung = []
            for h in zone:
                angabe, _ = self.mappe.fertigkeit(h.kette)
                if angabe:
                    zuordnung.append(f"{h.nr} → {angabe}")
                else:
                    zuordnung.append(f"{h.nr} → ?")
                    l.append(f"%% TODO Zuordnung Nr. {h.nr}: Fertigkeit nicht "
                             "in den Voraussetzungen der Mappe gefunden")
            l += ["", "Zuordnung: " + " · ".join(zuordnung), ""]
            for h in zone:
                l += self.satz_loesung(h)
            dateien["blatt0_l.tex"] = l
        # Einheiten
        anzahl = len(einheiten)
        bereiche = []
        for pos, (n, hs) in enumerate(einheiten, 1):
            kopf, titel = self.kopf(n, pos, anzahl)
            start = hs[0].nr if hs else nr + 1
            wer = f"Einheit {n}" if self.fokus else f"Einheit {pos} von {anzahl}"
            a = [f"% {wer} – {titel} (bank/{self.eintrag}/"
                 f"e{n}.jsonl, zusammenbau {VERSION})"] + kopf
            if self.a.kasten and not self.schwach:
                a += self.kasten(n)
            a.append(f"\\setcounter{{aufgabe}}{{{start - 1}}}")
            verfahren = [h for h in hs if h.art == "verfahren" and not h.weiter]
            for h in hs:
                a.append("")
                if len(verfahren) >= 2 and h in verfahren:
                    a.append("%% TODO \\verfahren{…}: Verfahrensüberschrift in "
                             "Sachsprache fehlt in der Bank (2.3 b)")
                a += self.satz_hauptnummer(h)
                self.reihenfolge.append((h, f"e{n}_a.tex"))
            if self.schwach:
                a.append("")
                a += self.kasten(n)
            dateien[f"e{n}_a.tex"] = a
            kopf_l = (f"Einheit {n} · {titel}" if self.fokus
                      else f"Einheit {pos} von {anzahl} · {titel}")
            l = [f"% Lösungen {wer} – {titel} (zusammenbau {VERSION})",
                 f"\\einheitenkopf{{{kopf_l}}}", ""]
            for h in hs:
                l += self.satz_loesung(h)
            dateien[f"e{n}_l.tex"] = l
            if hs:
                bereiche.append((n, pos, titel, hs[0].nr, hs[-1].nr))
        dateien.update(self.rahmen(zone, einheiten, bereiche))
        return dateien

    def rahmen(self, zone, einheiten, bereiche):
        th = self.thema
        weit = self.klasse is None or self.klasse <= 10
        if self.klasse is None:
            sek1 = any("OS Kl." in (e.get("marken") or "")
                       for e in self.mappe.einheiten.values())
            weit = sek1
        kopf = ["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}"]
        dateien = {}

        k = self.kennung

        def dok(blatt, rumpf, vorspann=()):
            # Kennung in der Fußzeile links, wo \blattfuss die Bezeichnung
            # trägt: \blattkopf* setzt dort sein drittes Argument
            # (\blattfuss selbst löscht die Kopfzeile von \blattkopf).
            fuss = f"{th} · {blatt} · {k}"
            z = kopf + list(vorspann) + ["\\begin{document}",
                                         f"\\blattkopf*{{{th}}}{{{blatt}}}{{{fuss}}}"]
            if weit and blatt != "Lösungen" and not blatt.endswith("Lösungen"):
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
            dateien[f"{k}.tex"] = dok(f"Fokus {self.fokus}", rumpf)
            dateien[f"{k}-loesungen.tex"] = dok(f"Fokus {self.fokus} · Lösungen",
                                                l_inputs)
            return dateien
        if zone:
            dateien[f"{k}-blatt0.tex"] = dok("Kennst du schon",
                                             ["\\input{blatt0_a}"])
        for pos, (n, _) in enumerate(einheiten, 1):
            dateien[f"{k}-e{n}.tex"] = dok(f"Einheit {pos}", [f"\\input{{e{n}_a}}"])
        verz_l = verz_e + ["\\verz{abhaken}{Das kann ich}"]
        dateien[f"{k}.tex"] = dok(
            "Lernblatt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_l) + "}"]
            + e_inputs + ["\\input{abhaken}"])
        verz_g = list(verz_l)
        g_rumpf = []
        if zone:
            verz_g.insert(0, f"\\verz{{zone}}{{Kennst du schon "
                             f"({nummern(zone[0].nr, zone[-1].nr)})}}")
            g_rumpf = ["\\input{blatt0_a}", "\\clearpage"]
        dateien[f"{k}-gesamt.tex"] = dok(
            "Gesamt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_g) + "}"]
            + g_rumpf + e_inputs + ["\\input{abhaken}"],
            vorspann=["\\def\\mitzone{1}"] if zone else [])
        dateien[f"{k}-loesungen.tex"] = dok("Lösungen", l_inputs)
        # Abhakseite
        ab = ["% Abhakseite „Das kann ich“ – Zone nur im Gesamt (\\mitzone)",
              "%% TODO Ich-kann-Sätze: Platzhalter wie in den Aufgabendateien",
              "\\begin{abhakseite}"]
        if zone:
            ab += ["\\ifdefined\\mitzone", "\\abhakgruppe{Kennst du schon}"]
            ab += [f"\\abhak{{{h.nr}}}{{{klar(h.titel)}}}" for h in zone]
            ab.append("\\fi")
        for (n, hs), (_, pos, titel, _, _) in zip(
                [e for e in einheiten if e[1]], bereiche):
            ab.append(f"\\abhakgruppe{{Einheit {pos} · {klar(titel)}}}")
            ab += [f"\\abhak{{{h.nr}}}{{{klar(h.titel)}}}" for h in hs]
        ab.append("\\end{abhakseite}")
        dateien["abhaken.tex"] = ab
        return dateien


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
  \noindent{\bfseries #1}\par\nobreak\vspace{1pt}\noindent{\color{mbgrau}\rule{\linewidth}{0.4pt}}\par\nobreak}
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
  \noindent{\bfseries #1}\par\vspace{1pt}\noindent{\color{mbgrau}\rule{\linewidth}{0.4pt}}\par\vspace{4pt}%
  \uebersichtskasten{\raggedright #2}\end{minipage}\end{lrbox}%
  \setlength{\kbhoehe}{\dimexpr\ht\kbbox+\dp\kbbox\relax}\Needspace*{\kbhoehe}\noindent\usebox{\kbbox}\par}
% Lösungsblatt: Nummer und Buchstabe halbfett, Lösung daneben
\newcommand{\kbloesung}[2]{\par\addvspace{3pt}\noindent\hangindent2.8em\hangafter1\makebox[2.8em][l]{\textbf{#1}}#2\par}
\makeatother
"""


class KompetenzBau:
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
        je = {}
        for z in sorted(pr, key=lambda z: (z["sprosse"], z["variante"])):
            o = (z.get("original") or {}).get("id") or z["id"]
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
            if len(wahl) >= KOMPETENZ_PRUEF_MIN:
                break
            if z not in wahl:
                wahl.append(z)
                log(f"FORMULIERUNG {z['id']}: gleiche Formulierung wie eine "
                    "schon gewählte – aufgefüllt auf vier")
        wahl.sort(key=lambda z: (-jahr(z), z["sprosse"], z["variante"]))
        for z in kand:
            if z not in wahl:
                log(f"RESERVE {z['id']} ({(z.get('original') or {}).get('id')})"
                    " – Formulierung schon vertreten oder mehr als fünf")
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
                [z.get("aufgabe", ""), z.get("merkmal", ""),
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

    # -- Satz --------------------------------------------------------------
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
        if bilder:
            masse = [grafik_mass(b if not b.startswith("\\kbwertetabelle")
                                 else "\\wertetabelle" + b[len("\\kbwertetabelle"):])
                     for b in bilder]
            rechts = "".join(kreuze) + antw + raum
            if len(bilder) == 2 and sum(m[0] for m in masse) <= TEXTBREITE_CM - 0.5:
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

    def satz_halb_text(self, z, anweisung):
        """Rechenaufgabe in einer halben Spalte: Text, Antwort, Raum darunter."""
        t = zerlege(z)
        kopf, frage = t["kopf"], list(t["frage"])
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
            if lage != "zone" and i > 0 and hs[i - 1][3] == "zone":
                a += ["", "\\kbabschnitt{Schritt für Schritt}"]
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
        inhalt = [re.sub(r"\s{3,}", r" \\quad ", klar(z.replace("&", "und")))
                  for z in zeilen]
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
            "kbpaar", "kbteilpaar"}
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
    for name in ("einheiten", "zone", "fokus", "klasse"):
        wert = getattr(args, name)
        if wert is not None and not (name == "zone" and wert == "ja"):
            aufruf += [f"--{name}", str(wert)]
    for name in ("schwach", "kasten"):
        if getattr(args, name):
            aufruf.append(f"--{name}")
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
    nummer = 0 if args.ohne_register else naechste_nummer(kuerzel, rezept,
                                                          register)
    args.kennung = f"{kuerzel}-{rezept}{nummer}"
    log(f"KENNUNG {args.kennung} – Kürzel {kuerzel} aus {k_quelle}; Rezept "
        f"{rezept} ({REZEPT[rezept]}); "
        + ("ohne Register (Probe)" if args.ohne_register else
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
    fehler = pruefe_struktur(texte, sig)

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
        "aus": args.aus,
        "ohne_register": args.ohne_register,
    }
    aufgaben = []
    for h, datei in bau.reihenfolge:
        for b, z in h.buchstaben:
            aufgaben.append({
                "aufgabe": f"A{h.nr}",
                "hauptnummer": h.nr,
                "teilaufgabe": b,
                "id": z["id"] if z else None,
                "datei": datei,
                **({} if z else {"hinweis": "Erklärzeile (schwach), "
                                            "keine Bankzeile"}),
            })
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

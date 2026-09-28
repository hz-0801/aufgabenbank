#!/usr/bin/env python3
"""zusammenbau.py v0.5 – aus bank/<eintrag>/ LaTeX-Quelltexte für mathblatt.sty.

Aufruf:
    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach] [--klasse 7]
        [--kasten] [--aus <ordner>] [--vorlage <mathblatt.sty>]
        [--ohne-register] [--kuerzel <_kuerzel.csv>]
    python3 werkzeuge/zusammenbau.py <eintrag> <eintrag> … --heft [msa|
        abitur-gk|abitur-lk|fhr] [--nur-basis] [--titel <text>] --aus <ordner>
    python3 werkzeuge/zusammenbau.py --zettel basis [--nummer n]
        [--ohne-register]

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
VERSION = "v0.5"

# Befehle der Rahmendateien, die weder in STANDARD (bank-pruef.py) noch
# in _bausteine.md stehen; jede Argumentzahl zulässig.
RAHMEN = {"documentclass", "usepackage", "input", "clearpage", "setcounter",
          "hfill", "bigskip", "medskip", "smallskip", "def", "ifdefined",
          "fi", "mitzone", "linewidth"}
# minipage: Zettel (v0.5), Text links, Grafik rechts in einer Hauptnummer
RAHMEN_UMGEBUNG = {"document", "minipage"}

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
          "Z": "Zettel"}
KENNUNG_MUSTER = re.compile(r"^([A-Z]{3})-([LFSHZ])(\d+)$")


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

    def _einheiten(self, zeilen):
        aktuell = None
        for z in zeilen:
            m = re.match(r"^(\d+)\. (.+?) – ", z)
            if m:
                aktuell = int(m.group(1))
                self.einheiten[aktuell] = {"titel": m.group(2).strip(),
                                           "marken": None}
                continue
            m = re.match(r"^\s+Marken: (.+)$", z)
            if m and aktuell:
                self.einheiten[aktuell]["marken"] = m.group(1).strip()

    def _voraussetzungen(self, zeilen):
        for z in zeilen:
            if z.startswith("Erkennungsschritte"):
                break
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


# --- Strukturprüfung ------------------------------------------------------

UMLAUT_ALT = re.compile(r"\\\"[aouAOUs]|\\ss\b|\\glqq|\\grqq|\\euro\b")

# Mathe-Modus: Befehle mit Text in den Argumenten (werden durchlaufen),
# Befehle mit Mathe im Argument, Textbefehle in Mathe, Ausrichtungen.
# Andere Bausteine (Grafik, Rahmen) werden samt Argumenten übergangen.
TEXT_ARG = {"teil", "steil", "tz", "stz", "swz", "swa", "swfrage", "erg",
            "abhak", "abhakgruppe", "uebersichtskasten", "einheitenkopf",
            "zweigzeile", "verz", "verzeichniszeile", "blattkopf",
            "leerfeld", "kreuz", "verfahren", "achtung"}
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
    Stand (Start 0), gewählt werden die kleinsten Stände (bei Gleichstand
    das größere Gewicht, dann die Folge in typen.csv), nach der Wahl steigt
    der Stand um 1/Gewicht. So kommt ein Typ mit neun Jahrgängen neunmal so
    oft wie einer mit einem. Je Typ höchstens eine Aufgabe je Zettel; der
    k-te Einsatz eines Typs nimmt Variante k, keine Aufgabe zweimal.
    Höchstens zwei große Grafiken (Koordinatensystem, Wertetabellen) je
    Zettel, damit er auf eine Seite passt: ein dritter solcher Typ wartet
    auf den nächsten Zettel (sein Stand bleibt, er kommt dann zuerst)."""
    stand = {t["typ"]: 0.0 for t in typen}
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
        wahl, gross = [], 0
        for t in pflicht + rest:
            g = bool(GROSS.search(vorrat[t][genutzt[t]].get("grafik", "")))
            if len(wahl) == ZETTEL_ZAHL or (g and gross >= GROSS_HOECHSTENS
                                            and t not in pflicht):
                continue
            wahl.append(t)
            gross += g
        if len(wahl) < ZETTEL_ZAHL:
            return plan, n
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

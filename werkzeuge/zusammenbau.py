#!/usr/bin/env python3
"""zusammenbau.py v0.1 – aus bank/<eintrag>/ LaTeX-Quelltexte für mathblatt.sty.

Aufruf:
    python3 werkzeuge/zusammenbau.py <eintrag> [--einheiten 1,3]
        [--zone ja|nein|kurz] [--fokus <kette>] [--schwach] [--klasse 7]
        [--kasten] [--aus bau/<eintrag>/<datum>/] [--vorlage <mathblatt.sty>]

Ohne Schalter: Lernblatt mit Zone und allen Einheiten, je Sprosse
Variante 1, ohne Klasse. Ausgabe unter bau/<eintrag>/<datum>/ (Datum
des Rechners), mit --aus in den genannten Ordner. Die Quelltexte
hängen nur von Bank, Mappe und Schaltern ab (kein Datum darin).

Liest bank/<eintrag>/*.jsonl, mappen/<eintrag>.md (Abschnitt 1),
mappen/_bausteine.md und aus werkzeuge/bank-pruef.py die Liste
STANDARD. Schreibt je Einheit e<n>_a.tex (Aufgaben) und e<n>_l.tex
(Lösungen), für die Zone blatt0_a/_l, die Rahmendateien, eine Kopie
von mathblatt.sty und zusammenbau.log. Anleitung:
werkzeuge/zusammenbau.md.
"""

import argparse
import datetime
import importlib.util
import json
import os
import re
import shutil
import sys
from bisect import bisect_right
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
VERSION = "v0.1"

# Befehle der Rahmendateien, die weder in STANDARD (bank-pruef.py) noch
# in _bausteine.md stehen; jede Argumentzahl zulässig.
RAHMEN = {"documentclass", "usepackage", "input", "clearpage", "setcounter",
          "hfill", "bigskip", "medskip", "smallskip", "def", "ifdefined",
          "fi", "mitzone"}
RAHMEN_UMGEBUNG = {"document"}

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


def mit_kennung(aufgabe, hat_feld):
    """Prüfkennung wie im Muster 2026-09-22: „\\hfill (P10 …)“."""
    m = KENNUNG.search(aufgabe)
    if not m:
        return aufgabe, False
    vor, nach = aufgabe[:m.start()], aufgabe[m.end():]
    neu = vor + " \\hfill " + m.group(0).strip() + nach
    am_ende = not nach.strip()
    if am_ende and hat_feld:
        neu += " \\\\"
    return neu, True


def feld_im_grafik(z):
    g = z.get("grafik", "")
    return "\\streifenfeld" in g or "\\dsleer" in g


def teil_normal(z):
    """Zeilen für eine Teilaufgabe im teile-Block."""
    feld = "" if feld_im_grafik(z) else antwortfeld(z.get("antwort", ""))
    aufgabe, _ = mit_kennung(z["aufgabe"], bool(feld))
    grafik = z.get("grafik", "")
    if not grafik:
        return [f"\\teil {aufgabe}" + (f" {feld}" if feld else "")]
    zeilen = [f"\\teil {aufgabe}", "", grafik]
    if feld:
        zeilen.append(feld)
    return zeilen


def gl_inhalt(aufgabe):
    t = aufgabe.strip()
    if t.startswith("$") and t.endswith("$") and t.count("$") == 2:
        return t[1:-1]
    return "\\text{" + t + "}"


def teile_normal(folge):
    """Teilaufgaben in teile- und gleichungsraster-Blöcken."""
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
            aus += teil_normal(z)
        else:
            trenner = " &" if spalte == 0 else " \\\\"
            aus.append(f"\\gl{{{gl_inhalt(z['aufgabe'])}}}" + trenner)
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
    aufgabe, _ = mit_kennung(z["aufgabe"], False)
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
        self.todo_frei = []

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

        def dok(blatt, rumpf, vorspann=()):
            z = kopf + list(vorspann) + ["\\begin{document}",
                                         f"\\blattkopf{{{th}}}{{{blatt}}}"]
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
            dateien["fokus.tex"] = dok(f"Fokus {self.fokus}", rumpf)
            dateien["fokus_loesungen.tex"] = dok(f"Fokus {self.fokus} · Lösungen",
                                                 l_inputs)
            return dateien
        if zone:
            dateien["blatt0.tex"] = dok("Kennst du schon", ["\\input{blatt0_a}"])
        for pos, (n, _) in enumerate(einheiten, 1):
            dateien[f"e{n}.tex"] = dok(f"Einheit {pos}", [f"\\input{{e{n}_a}}"])
        verz_l = verz_e + ["\\verz{abhaken}{Das kann ich}"]
        dateien["lernblatt.tex"] = dok(
            "Lernblatt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_l) + "}"]
            + e_inputs + ["\\input{abhaken}"])
        verz_g = list(verz_l)
        g_rumpf = []
        if zone:
            verz_g.insert(0, f"\\verz{{zone}}{{Kennst du schon "
                             f"({nummern(zone[0].nr, zone[-1].nr)})}}")
            g_rumpf = ["\\input{blatt0_a}", "\\clearpage"]
        dateien["gesamt.tex"] = dok(
            "Gesamt",
            ["\\verzeichniszeile{" + " \\verztrenn ".join(verz_g) + "}"]
            + g_rumpf + e_inputs + ["\\input{abhaken}"],
            vorspann=["\\def\\mitzone{1}"] if zone else [])
        dateien["loesungen.tex"] = dok("Lösungen", l_inputs)
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
    p.add_argument("eintrag")
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
    args = p.parse_args(argv)
    if args.fokus and args.schwach:
        sys.exit("--fokus und --schwach zusammen kann v0.1 nicht")

    log = Log()
    aufruf = ["zusammenbau.py", args.eintrag]
    for name in ("einheiten", "zone", "fokus", "klasse"):
        wert = getattr(args, name)
        if wert is not None and not (name == "zone" and wert == "ja"):
            aufruf += [f"--{name}", str(wert)]
    for name in ("schwach", "kasten"):
        if getattr(args, name):
            aufruf.append(f"--{name}")
    log(f"# zusammenbau {VERSION}: " + " ".join(aufruf))

    vorlage = finde_vorlage(args.vorlage)
    version = vorlage.read_text(encoding="utf-8").splitlines()[1].lstrip("% ")
    version = version.split(" (", 1)[0]
    log(f"VORLAGE mathblatt.sty: {version}")

    bau = Bau(args, log)
    dateien = bau.baue()
    texte = {k: "\n".join(v) + "\n" for k, v in dateien.items()}

    sig = BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md")
    fehler = pruefe_struktur(texte, sig)

    if args.aus:
        ziel = Path(args.aus)
    else:
        ziel = WURZEL / "bau" / args.eintrag / datetime.date.today().isoformat()
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
    print(f"{len(texte)} Quelltexte nach {ziel}; {len(todo)} TODO; "
          f"Strukturprüfung {len(fehler)} Fehler")
    for name, zl, meldung in fehler:
        print(f"FEHLER {name}:{zl}: {meldung}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())

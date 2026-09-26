#!/usr/bin/env python3
"""Baut die Mappe eines Katalogeintrags (bank.md, „Quellen je Sitzung").

Aufruf:
    python3 werkzeuge/mappe.py <eintrag> [<eintrag> ...]

Schreibt mappen/<eintrag>.md und dazu mappen/_bausteine.md. Quellen
sind die Raw-URLs von hz-0801/mathe-nachhilfe und hz-0801/blattbau
(Zweig main):

1. Kopf: Eintrag, Katalog-Commit (letzter Commit auf der Datei),
   Datum.
2. Der Katalogeintrag mit Zeilennummern, ohne „Status", „Offene
   Punkte" und „Prüfliste".
3. Originale: je Kennung aus „Prüfungsform" und „Zielmarke" die
   Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren,
   fehlerquelle, format, antwort aus den Prüfungsdateien (CSV).
4. Maßstab: unterrichtsblatt.md 2.2, 2.3 c, 2.4 b–c, 3.6 wortgleich.

Den Commit liefert die GitHub-API; ist sie gesperrt, ein Klon ohne
Dateiinhalte (git clone --filter=blob:none) und git log. Nur
Standardbibliothek.
"""

import csv
import io
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAW = "https://raw.githubusercontent.com/{repo}/main/{pfad}"
API = ("https://api.github.com/repos/{repo}/commits"
       "?sha=main&path={pfad}&per_page=1")
KATALOG = "hz-0801/mathe-nachhilfe"
VORLAGE = "hz-0801/blattbau"
PRUEFDATEIEN = ["msa/msa-katalog-kontext.csv", "msa/msa-katalog-basis.csv",
                "msa/msa-katalog-gym.csv", "fhr/fhr-katalog.csv",
                "abitur/abi-katalog.csv", "abitur/iqb-katalog.csv"]
SPALTEN = ["id", "jahr", "papier", "punkte", "gegeben", "gesucht",
           "verfahren", "fehlerquelle", "format", "antwort"]
ZAUN = "````"

_klone = {}


def hole(repo, pfad):
    """Raw-Datei als Text; drei Versuche."""
    url = RAW.format(repo=repo, pfad=pfad)
    for versuch in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise SystemExit(f"nicht gefunden: {url}")
            fehler = e
        except OSError as e:
            fehler = e
        time.sleep(2 ** (versuch + 1))
    raise SystemExit(f"nicht erreichbar: {url} ({fehler})")


def klon(repo):
    if repo not in _klone:
        ziel = Path(tempfile.mkdtemp(prefix="mappe-")) / repo.split("/")[1]
        subprocess.run(["git", "clone", "--quiet", "--filter=blob:none",
                        "--no-checkout", "--single-branch", "--branch",
                        "main", f"https://github.com/{repo}", str(ziel)],
                       check=True)
        _klone[repo] = ziel
    return _klone[repo]


def letzter_commit(repo, pfad):
    """(hash, datum, betreff, weg) des letzten Commits auf pfad."""
    try:
        with urllib.request.urlopen(API.format(repo=repo, pfad=pfad),
                                    timeout=30) as r:
            c = json.load(r)[0]
        return (c["sha"], c["commit"]["committer"]["date"],
                c["commit"]["message"].split("\n")[0], "GitHub-API")
    except (OSError, ValueError, IndexError, KeyError):
        pass
    aus = subprocess.run(
        ["git", "-C", str(klon(repo)), "log", "-1",
         "--format=%H%x09%cI%x09%s", "main", "--", pfad],
        check=True, capture_output=True, text=True).stdout.strip()
    if not aus:
        raise SystemExit(f"kein Commit auf {repo}/{pfad}")
    h, d, s = aus.split("\t", 2)
    return h, d, s, "git log (GitHub-API gesperrt)"


def stand_zeile(repo, pfad):
    h, d, s, weg = letzter_commit(repo, pfad)
    return f"{h} ({d}, „{s}“; ermittelt über {weg})"


# --- 2 Katalogeintrag --------------------------------------------------

def katalog_zeilen(text):
    """[(nr, zeile)] ohne Status-Zeile, „Offene Punkte" und Prüfliste."""
    aus = []
    weg = False
    for nr, z in enumerate(text.split("\n"), 1):
        if re.match(r"#{1,6} ", z):
            weg = bool(re.match(r"#{1,6} (Offene Punkte|Prüfliste)", z))
        if weg or z.startswith("Status:"):
            continue
        aus.append((nr, z))
    while aus and aus[-1][1] == "":
        aus.pop()
    return aus


def abschnitt(text, titel):
    """Text des Abschnitts '### <titel>…' bis zur nächsten Überschrift."""
    zeilen = text.split("\n")
    aus, drin = [], False
    for z in zeilen:
        if re.match(r"#{1,6} ", z):
            drin = z.lstrip("#").strip().startswith(titel)
            continue
        if drin:
            aus.append(z)
    return "\n".join(aus)


# --- 3 Originale -------------------------------------------------------

def lade_pruefdateien():
    tabelle = {}
    for pfad in PRUEFDATEIEN:
        text = hole(KATALOG, pfad)
        for zeile in csv.DictReader(io.StringIO(text), delimiter=";"):
            tabelle.setdefault(zeile["id"], (pfad, zeile))
    return tabelle


def kennungen(text, tabelle):
    """Kennungen der Tabelle in text, in der Folge ihres Auftretens."""
    treffer = []
    for kid in tabelle:
        m = re.search(r"(?<![\w.-])" + re.escape(kid)
                      + r"(?![\w-]|\.\w)", text)
        if m:
            treffer.append((m.start(), kid))
    return [k for _, k in sorted(treffer)]


KANDIDAT = re.compile(r"(?<![\w.-])\d{4}-[A-Za-z]+-[A-Za-z0-9]+"
                      r"(?:\.[A-Za-z0-9]+)*(?![\w-])")


def originale(eintrag_text, tabelle):
    pf = abschnitt(eintrag_text, "Prüfungsform")
    ziel = "\n".join(z for z in eintrag_text.split("\n")
                     if z.startswith("Zielmarke"))
    quelle = pf + "\n" + ziel
    ids = kennungen(quelle, tabelle)
    unbekannt = {k for k in KANDIDAT.findall(quelle) if k not in tabelle}
    staemme = sorted(k for k in unbekannt
                     if any(re.fullmatch(re.escape(k) + r"[a-z]", t)
                            for t in tabelle))
    fehlt = sorted(unbekannt - set(staemme))
    rest = kennungen(eintrag_text, tabelle)
    ausserhalb = [k for k in rest if k not in ids]
    aus = ["Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge "
           "ihres ersten Auftretens; Spalten " + ", ".join(SPALTEN) + ".",
           ""]
    for kid in ids:
        pfad, z = tabelle[kid]
        aus.append(f"### {kid} ({pfad.split('/')[-1]})")
        aus.append("")
        aus.append(f"jahr {z['jahr']} · papier {z['papier']} · punkte "
                   f"{z['punkte']} · format {z['format']} · antwort "
                   f"{z['antwort']}")
        for sp in ("gegeben", "gesucht", "verfahren", "fehlerquelle"):
            wert = " / ".join(t.strip() for t in z[sp].split("\n"))
            aus.append(f"- {sp}: {wert}")
        aus.append("")
    if fehlt:
        aus.append("Nicht in den Prüfungsdateien gefunden: "
                   + ", ".join(fehlt))
        aus.append("")
    if staemme:
        aus.append("Als Stamm ohne Teilaufgabe genannt (aufgenommen sind "
                   "nur einzeln genannte Teilaufgaben): "
                   + ", ".join(staemme))
        aus.append("")
    if ausserhalb:
        aus.append("Nur außerhalb von „Prüfungsform“ genannt, nicht "
                   "aufgenommen: " + ", ".join(ausserhalb))
        aus.append("")
    return aus, len(ids)


# --- 4 Maßstab ---------------------------------------------------------

def bereich(zeilen, anfang, ende, ab=0):
    """Zeilen von der ersten, die anfang trifft (ab Index ab), bis vor
    die nächste, die ende trifft."""
    for i in range(ab, len(zeilen)):
        if re.match(anfang, zeilen[i]):
            break
    else:
        raise SystemExit(f"unterrichtsblatt: {anfang!r} fehlt")
    j = i + 1
    while j < len(zeilen) and not re.match(ende, zeilen[j]):
        j += 1
    aus = zeilen[i:j]
    while aus and not aus[-1].strip():
        aus.pop()
    return aus, i


def massstab(text):
    z = text.split("\n")
    teile = []
    s22, _ = bereich(z, r"2\.2 ", r"2\.3 ")
    teile.append(("2.2", s22))
    _, i23 = bereich(z, r"2\.3 ", r"2\.4 ")
    s23c, _ = bereich(z, r"c\) ", r"[d-z]\) |2\.4 ", i23)
    teile.append(("2.3 c", s23c))
    _, i24 = bereich(z, r"2\.4 ", r"2\.5 ")
    s24, _ = bereich(z, r"b\) ", r"d\) |2\.5 ", i24)
    teile.append(("2.4 b–c", s24))
    s36, _ = bereich(z, r"3\.6 ", r"\d\.\d+ |#")
    teile.append(("3.6", s36))
    aus = []
    for titel, zeilen in teile:
        aus += [f"### {titel}", "", ZAUN + "text", *zeilen, ZAUN, ""]
    return aus


# --- Mappe und Bausteine -----------------------------------------------

def jetzt():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def baue_mappe(eintrag, tabelle, massstab_text, massstab_stand, ziel):
    pfad = f"katalog/{eintrag}.md"
    text = hole(KATALOG, pfad)
    stand = stand_zeile(KATALOG, pfad)
    kz = katalog_zeilen(text)
    breite = len(str(kz[-1][0]))
    orig, n_orig = originale(text, tabelle)
    aus = [f"# Mappe: {eintrag}", "",
           f"Eintrag: {KATALOG}, {pfad}",
           f"Katalog-Commit: {stand}",
           f"Maßstab: {VORLAGE}, unterrichtsblatt.md, Commit "
           f"{massstab_stand}",
           f"Datum: {jetzt()}",
           "Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.", "",
           "Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab", "",
           "## 1 Katalogeintrag", "",
           "Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am "
           "Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld "
           "quelle).", "", ZAUN + "text"]
    aus += [f"{nr:>{breite}}  {z}".rstrip() for nr, z in kz]
    aus += [ZAUN, "", f"## 2 Originale ({n_orig})", ""] + orig
    aus += ["## 3 Maßstab (unterrichtsblatt.md, wortgleich)", ""]
    aus += massstab_text
    while aus[-1] == "":
        aus.pop()
    ziel.write_text("\n".join(aus) + "\n", encoding="utf-8")
    return len(aus)


ABSATZ = [r"`\\anweisung", r"`\\rechenplatz", r"Die Umgebung `beispiel`",
          r"Der Befehl `\\beispiel", r"`\\streifenfeld", r"`\\swz`"]


def baue_bausteine(ziel):
    pfad = "Anleitung_mathblatt.md"
    text = hole(VORLAGE, pfad)
    stand = stand_zeile(VORLAGE, pfad)
    zeilen = text.split("\n")
    aus = ["# Bausteine der Vorlage", "",
           f"Quelle: {VORLAGE}, {pfad}, Commit {stand}",
           f"Datum: {jetzt()}",
           "Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern. "
           "werkzeuge/bank-pruef.py liest hieraus Namen und "
           "Argumentzahl der Bausteine.", "",
           "## Kurzreferenz", "",
           "Alle Zeilen der Anleitung, die mit `\\` oder `\\begin{` "
           "beginnen (auch eingerückt), je Block unter dessen "
           "Überschrift.", ""]
    im_block, titel, block = False, "Ohne Block", []
    letzte = ""
    n_ref = 0

    def schliesse():
        nonlocal block
        if block:
            aus.extend([f"### {titel}", "", ZAUN + "text", *block, ZAUN,
                        ""])
        block = []

    for z in zeilen:
        if z.startswith("```"):
            if not im_block:
                schliesse()
                titel = letzte or "Ohne Titel"
                if len(titel) > 72:     # Absatz statt Überschrift
                    titel = titel[:60].rstrip() + " …"
            im_block = not im_block
            continue
        if z.lstrip().startswith("\\"):
            if not im_block and titel != "Außerhalb der Blöcke":
                schliesse()
                titel = "Außerhalb der Blöcke"
            block.append(z.rstrip())
            n_ref += 1
        if not im_block and z.strip():
            letzte = z.strip()
    schliesse()
    aus += ["## Absätze", "",
            "Wortgleich die Absätze zu \\anweisung, \\rechenplatz, "
            "beispiel, \\streifenfeld, \\swz.", ""]
    for muster in ABSATZ:
        treffer = [z for z in zeilen if re.match(muster, z)]
        if not treffer:
            raise SystemExit(f"Anleitung: Absatz {muster!r} fehlt")
        for z in treffer:
            aus += [z.rstrip(), ""]
    while aus[-1] == "":
        aus.pop()
    ziel.write_text("\n".join(aus) + "\n", encoding="utf-8")
    return len(aus), n_ref


def main(argv):
    if len(argv) < 2 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    wurzel = Path(__file__).resolve().parent.parent
    ordner = wurzel / "mappen"
    ordner.mkdir(exist_ok=True)
    n, n_ref = baue_bausteine(ordner / "_bausteine.md")
    print(f"mappen/_bausteine.md: {n} Zeilen ({n_ref} Referenzzeilen)")
    tabelle = lade_pruefdateien()
    ub = "unterrichtsblatt.md"
    massstab_text = massstab(hole(VORLAGE, ub))
    massstab_stand = stand_zeile(VORLAGE, ub)
    for eintrag in argv[1:]:
        ziel = ordner / f"{eintrag}.md"
        n = baue_mappe(eintrag, tabelle, massstab_text, massstab_stand,
                       ziel)
        print(f"mappen/{eintrag}.md: {n} Zeilen")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

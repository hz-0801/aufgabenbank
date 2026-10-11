#!/usr/bin/env python3
"""originalneu.py v0.1 – Prüfstein „Original neu“ (pruefung.md § 4) für ein
P10-Heft: Schnitt und Stufen wie das Original, neu gesetzt, durchsuchbar,
Punkte am Rand; am Ende Lösungsblatt mit Register nach der amtlichen
Gliederung (jede Teilaufgabe unter Haupt- und Nebenthema, Sprungmarken).

    python3 werkzeuge/originalneu.py --heft 2026-for [--privat <ordner>]
        [--katalog <ordner msa/>] [--vorlage <mathblatt.sty>] [--kein-pdf]

Quellen (nur privat, nie im öffentlichen Repo): aufgabenbank-privat/
basis-originale.jsonl (Aufgabe 1) und hauptteil-originale.jsonl (Aufgaben
2 ff.), Themen aus mathe-nachhilfe/msa/msa-katalog-{basis,kontext}.csv
(Felder thema = Hauptthema, neben = Nebenthema). Ausgabe:
aufgabenbank-privat/originalneu/<heft>/src/ und pdf/. Nur für den Lehrer.
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
VERSION = "0.1"


def finde(pfad_arg, env, kandidaten, name):
    k = []
    if pfad_arg:
        k.append(Path(pfad_arg))
    if os.environ.get(env):
        k.append(Path(os.environ[env]))
    k += kandidaten
    for p in k:
        if p.exists():
            return p
    sys.exit(f"{name} nicht gefunden (gesucht: {', '.join(map(str, k))})")


def lies_jsonl(pfad, jahr, papier):
    zeilen = []
    if not pfad.is_file():
        return zeilen
    with open(pfad, encoding="utf-8") as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            z = json.loads(l)
            if z["jahr"] == jahr and z["papier"] == papier:
                zeilen.append(z)
    return zeilen


def lies_katalog(ordner, praefix):
    kat = {}
    for name in ("msa-katalog-basis.csv", "msa-katalog-kontext.csv"):
        p = ordner / name
        if not p.is_file():
            continue
        with open(p, encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter=";"):
                if r["id"].startswith(praefix):
                    kat[r["id"]] = r
    return kat


# ---------- LaTeX ----------

def esc(s):
    return s


def antwortzeile(a):
    if not a:
        return ""
    t = a.replace("__", "\\rule[-0.4ex]{2.2cm}{0.4pt}")
    return "\\par\\smallskip\\noindent " + t + "\\par"


def grafik_tex(g):
    if not g:
        return ""
    if g.lstrip().startswith("\\"):
        return "\\par\\smallskip\\noindent " + g + "\\par"
    marke = "" if g.startswith("Abbildung") else "Abbildung: "
    return ("\\par\\smallskip\\noindent{\\small\\itshape\\color{mbgrau}"
            "[" + marke + g + "]}\\par")


def optionen_tex(opts):
    if not opts:
        return ""
    buchst = "ABCDEFGH"
    graf = any(o.lstrip().startswith("\\begin{") for o in opts)
    if graf:
        n = len(opts)
        teile = []
        for b, o in zip(buchst, opts):
            teile.append("\\begin{minipage}[t]{%.3f\\linewidth}\\centering"
                         "\\textbf{%s}\\,$\\square$\\\\[3pt]%s\\end{minipage}"
                         % (0.98 / n, b, o))
        return "\\par\\medskip\\noindent" + "\\hfill".join(teile) + "\\par"
    return "".join("\\pfkreuzab{%s}{%s}" % (b, o) for b, o in zip(buchst, opts))


def teilaufgabe_tex(z):
    out = []
    grafik = grafik_tex(z.get("grafik", ""))
    if z.get("stamm"):
        # Abbildung gehört zum Stamm (steht im Heft daneben)
        out.append("\\par\\medskip\\noindent " + z["stamm"] + grafik
                   + "\\par\\medskip")
        grafik = ""
    kopf = z["teil"] + ")"
    out.append("\\hypertarget{%s}{}\\label{%s}" % (z["id"], z["id"]))
    out.append("\\begin{pfaufg}{}{%s}{%d P}" % (kopf, z["punkte"]))
    out.append(z["aufgabe"])
    out.append(grafik)
    out.append(optionen_tex(z.get("optionen") or []))
    out.append(antwortzeile(z.get("antwort", "")))
    out.append("\\end{pfaufg}")
    return "\n".join(o for o in out if o)


def aufgabe_tex(nr, titel, gp, zeilen):
    out = ["\\clearpage",
           "\\hypertarget{aufg%d}{}\\pfabschnitt{Aufgabe %d: %s\\hfill"
           "{\\normalsize\\mdseries\\color{mbgrau}(%d Punkte)}}"
           % (nr, nr, titel, gp)]
    for z in zeilen:
        out.append(teilaufgabe_tex(z))
    return "\n".join(out)


def loesungen_tex(aufgaben):
    """Je Aufgabe eine kompakte Tabelle: Teilaufgabe, Lösung, Typ grau."""
    out = ["\\clearpage\\hypertarget{loesungen}{}\\pfabschnitt{Lösungen}",
           "{\\small\\color{mbgrau}Keine amtlichen Lösungen zur P10; Ergebnisse "
           "aus dem Katalog (eigene Rechnung).}\\par"]
    for nr, titel, gp, zeilen in aufgaben:
        out.append("\\par\\addvspace{5pt}\\Needspace*{4\\baselineskip}"
                   "\\noindent\\textbf{%d}\\ %s\\par\\nobreak\\vspace{1pt}" % (nr, titel))
        out.append("\\noindent\\small\\begin{tabular}{@{}>{\\bfseries}p{0.06\\linewidth}@{}"
                   ">{\\raggedright\\arraybackslash}p{0.60\\linewidth}@{\\hspace{0.02\\linewidth}}"
                   ">{\\raggedright\\arraybackslash\\color{mbgrau}}p{0.32\\linewidth}@{}}")
        for z in zeilen:
            out.append("\\hyperlink{%s}{%d%s} & %s & %s\\\\"
                       % (z["id"], nr, z["teil"], z["loesung"], z.get("typ", "")))
        out.append("\\end{tabular}\\normalsize\\par")
    return "\n".join(out)


def register_tex(aufgaben, kat):
    """Je Thema die Teilaufgaben: Hauptthema fett, Nebenthema grau; mit
    Sprungmarke und Seitenzahl. Kompakt: eine Zeile je Thema."""
    haupt = defaultdict(list)
    neben = defaultdict(list)
    fehlt = []
    for nr, titel, gp, zeilen in aufgaben:
        for z in zeilen:
            k = kat.get(z["id"])
            marke = "%d%s" % (nr, z["teil"])
            if not k:
                fehlt.append(z["id"])
                continue
            if k.get("thema"):
                haupt[k["thema"]].append((marke, z["id"]))
            if k.get("neben"):
                neben[k["neben"]].append((marke, z["id"]))
    themen = sorted(set(haupt) | set(neben), key=str.casefold)
    out = ["\\par\\addvspace{10pt}\\pfabschnitt{Register nach Themen}",
           "{\\small\\color{mbgrau}fett: Hauptthema, grau: Nebenthema; "
           "Nummer = Aufgabe und Teilaufgabe, dahinter die Seite}\\par\\smallskip",
           "\\begin{multicols}{2}\\begin{list}{}{\\small\\setlength{\\leftmargin}{1.5em}"
           "\\setlength{\\itemindent}{-1.5em}\\setlength{\\itemsep}{1pt}"
           "\\setlength{\\parsep}{0pt}}"]
    for t in themen:
        eintr = []
        for marke, id_ in haupt.get(t, []):
            eintr.append("\\textbf{\\hyperlink{%s}{%s}}\\,\\pageref*{%s}"
                         % (id_, marke, id_))
        for marke, id_ in neben.get(t, []):
            eintr.append("{\\color{mbgrau}\\hyperlink{%s}{%s}\\,\\pageref*{%s}}"
                         % (id_, marke, id_))
        out.append("\\item \\textbf{%s}\\quad " % t + " · ".join(eintr))
    out.append("\\end{list}\\end{multicols}")
    if fehlt:
        out.append("\\par{\\small\\color{mbgrau}Ohne Katalogzeile: %s}"
                   % ", ".join(fehlt))
    return "\n".join(out), fehlt


def heft_tex(heft, jahr, papier, aufgaben, kat):
    q = aufgaben[0][3][0].get("quelle", {}).get("datei", "")
    qname = (q[:-4] if q.endswith(".pdf") else q) or "26_P10_Ma_%s_A" % papier
    qname = qname.replace("_", "\\_")
    gesamt = sum(gp for _, _, gp, _ in aufgaben)
    reg, fehlt = register_tex(aufgaben, kat)
    kopf = [
        "\\documentclass[11pt]{article}",
        "\\usepackage{mathblatt}",
        "\\usepackage{needspace,multicol}",
        "\\begin{document}",
        "\\pfheftstil",
        "\\pflaufkopf[P10 · Original neu]{%d %s}{%s}" % (jahr, papier, heft),
        "\\pfseitevon",
        "\\pfheftkopf{Prüfung am Ende der Jahrgangsstufe 10 · %d %s}{}"
        % (jahr, papier),
        "\\pfstufenzeile{Mathematik · Aufgaben %s · %d Punkte · "
        "neu gesetzt nach %s · nur für den Lehrer · "
        "\\hyperlink{loesungen}{Lösungen und Register am Ende}}"
        % ("1–%d" % aufgaben[-1][0], gesamt, qname),
    ]
    # Übersicht der Aufgaben mit Sprungmarken
    kopf.append("\\par\\medskip\\noindent\\begin{tabular}{@{}llr@{}}")
    for nr, titel, gp, zeilen in aufgaben:
        kopf.append("\\hyperlink{aufg%d}{Aufgabe %d: %s} & S.\\,\\pageref*{%s} "
                    "& {\\color{mbgrau}%d P}\\\\" % (nr, nr, titel, zeilen[0]["id"], gp))
    kopf.append("\\end{tabular}\\par")
    koerper = [aufgabe_tex(nr, t, gp, z) for nr, t, gp, z in aufgaben]
    # Aufgabe 1 beginnt nicht auf neuer Seite
    koerper[0] = koerper[0].replace("\\clearpage", "", 1)
    ende = [loesungen_tex(aufgaben), reg, "\\end{document}"]
    return "\n".join(kopf + koerper + ende), fehlt


# ---------- Ablauf ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heft", required=True, help="z. B. 2026-for")
    ap.add_argument("--privat")
    ap.add_argument("--katalog")
    ap.add_argument("--vorlage")
    ap.add_argument("--kein-pdf", action="store_true")
    a = ap.parse_args()

    jahr_s, papier = a.heft.split("-", 1)
    jahr, papier = int(jahr_s), papier.upper()
    privat = finde(a.privat, "PRIVAT", [WURZEL.parent / "aufgabenbank-privat"],
                   "aufgabenbank-privat")
    katalog = finde(a.katalog, "KATALOG",
                    [WURZEL.parent / "mathe-nachhilfe" / "msa"], "Katalog msa/")
    vorlage = finde(a.vorlage, "BLATTBAU",
                    [WURZEL.parent / "blattbau" / "mathblatt.sty",
                     WURZEL.parent / "hz-0801" / "blattbau" / "mathblatt.sty"],
                    "mathblatt.sty")
    if vorlage.is_dir():
        vorlage = vorlage / "mathblatt.sty"

    basis = lies_jsonl(privat / "basis-originale.jsonl", jahr, papier)
    haupt = lies_jsonl(privat / "hauptteil-originale.jsonl", jahr, papier)
    if not basis and not haupt:
        sys.exit("keine Zeilen für %s" % a.heft)
    kat = lies_katalog(katalog, "%d-%s-" % (jahr, papier))

    aufgaben = []
    if basis:
        basis.sort(key=lambda z: z["teil"])
        aufgaben.append((1, "Basisaufgaben", sum(z["punkte"] for z in basis), basis))
    nummern = sorted({z["nummer"] for z in haupt})
    for n in nummern:
        zl = sorted([z for z in haupt if z["nummer"] == n], key=lambda z: z["teil"])
        gp = zl[0].get("gesamtpunkte") or sum(z["punkte"] for z in zl)
        if gp != sum(z["punkte"] for z in zl):
            print("WARNUNG Aufgabe %d: Punkte %d, Heft nennt %d"
                  % (n, sum(z["punkte"] for z in zl), gp))
        aufgaben.append((n, zl[0]["titel"], gp, zl))

    tex, fehlt = heft_tex(a.heft, jahr, papier, aufgaben, kat)
    ziel = privat / "originalneu" / a.heft
    src, pdf = ziel / "src", ziel / "pdf"
    src.mkdir(parents=True, exist_ok=True)
    pdf.mkdir(parents=True, exist_ok=True)
    name = "%s-original-neu" % a.heft
    (src / (name + ".tex")).write_text(tex, encoding="utf-8")
    shutil.copyfile(vorlage, src / "mathblatt.sty")
    n_teil = sum(len(z) for _, _, _, z in aufgaben)
    print("Zeilen: %d Teilaufgaben in %d Aufgaben; ohne Katalogzeile: %d"
          % (n_teil, len(aufgaben), len(fehlt)))
    if a.kein_pdf:
        return
    for _ in range(3):
        r = subprocess.run(["xelatex", "-interaction=nonstopmode",
                            "-file-line-error", name + ".tex"],
                           cwd=src, capture_output=True, text=True)
    log = (src / (name + ".log")).read_text(encoding="utf-8", errors="replace")
    fehler = [l for l in log.splitlines() if ".tex:" in l and ":" in l.split(".tex:")[-1][:6]]
    if r.returncode != 0 or not (src / (name + ".pdf")).is_file():
        print("\n".join(fehler[:20]))
        sys.exit("xelatex fehlgeschlagen, siehe " + str(src / (name + ".log")))
    shutil.copyfile(src / (name + ".pdf"), pdf / (name + ".pdf"))
    print("PDF:", pdf / (name + ".pdf"), "– Fehlerzeilen im Log:", len(fehler))


if __name__ == "__main__":
    main()

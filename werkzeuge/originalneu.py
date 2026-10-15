#!/usr/bin/env python3
"""originalneu.py v0.3 (15.10.: gezeichnete Figuren aus privat bau/original-neu/grafik/<id>.tex statt Text) –
v0.2 „Original neu“ im Layout der Blätter (v0.2, 14.10.2026, plan.md § 10, 14.10. g; Ausgabe
aufgabenbank-privat bau/original-neu/<heft>/, blatt.pdf und loesung.pdf); v0.1 mit --form alt:
Prüfstein „Original neu“ (pruefung.md § 4) für ein
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
import re
import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
VERSION = "0.3"


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


def heft_tex_alt(heft, jahr, papier, aufgaben, kat):
    """v0.1 (Prüfstein mit Register, 04.10.) – abgelöst durch blatt_tex (14.10.), bleibt für --form alt."""
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
        "\\pfheftkopf{Prüfung am Ende der Jahrgangsstufe 10 · %d %s}{}" % (jahr, papier),
    ]
    koerper = [aufgabe_tex(nr, t, gp, z) for nr, t, gp, z in aufgaben]
    koerper[0] = koerper[0].replace("\\clearpage", "", 1)
    ende = [loesungen_tex(aufgaben), reg, "\\end{document}"]
    return "\n".join(kopf + koerper + ende), fehlt


# ---------- v0.2: Original neu im Layout der Blätter (plan.md § 10, 14.10. g) ----------
# Kopf links „P10 · Original ’JJ“, rechts Kennung mit Fassung; Buchstabenspalte (gemeinsam.md); keine Marke,
# kein Mehr, keine Heranführung; Schnitt und Folge wie im Heft; Lösung nach gemeinsam.md „Lösungen“ (eigene Datei,
# Tabelle je Teilaufgabe, links Ergebnis fett, rechts der Weg klein; keine Punkte). Kennung: P · O (Original) ·
# Jahr, bei getrenntem Heft F/E (PO25, PO26F, PO26E) – Entscheidung des Setzers, Schema plan.md § 10, 14.10. b.

PRAEAMBEL = r"""\documentclass[11pt]{article}
\usepackage{mathblatt}
\usepackage{needspace}
\newcommand{\karo}[1]{\par\smallskip\noindent\begin{tikzpicture}
  \clip (0,0) rectangle ({\linewidth-1mm},{#1*10mm});
  \draw[black!16,line width=0.3pt,step=5mm] (0,0) grid ({\linewidth},{#1*10mm});
  \end{tikzpicture}\par}
\newcommand{\pkt}{\textperiodcentered{}}
% Teilaufgabe: Buchstabe in eigener Spalte neben der Nummernspalte (gemeinsam.md „Buchstabenspalte“)
\newenvironment{onteil}[1]{\makebox[\mbpfteil][l]{\textbf{#1}}%
  \begin{minipage}[t]{\dimexpr\linewidth-\mbpfteil\relax}\raggedright\strut\ignorespaces}{\end{minipage}}
\begin{document}
"""


def kennung(jahr, papier):
    return "PO%02d%s" % (jahr % 100, {"FOR": "F", "EBR": "E"}.get(papier, ""))


def kopf_links(jahr, papier):
    return "P10 \\pkt{} Original ’%02d%s" % (jahr % 100, "" if papier == "OS" else " " + papier)


def ist_tex(g):
    return g.lstrip()[:1] in ("\\", "{")


def lies_grafiken(privat):
    """Gezeichnete Figuren (v0.3, 15.10.): privat bau/original-neu/grafik/<id>.tex ersetzt den Beschreibungstext
    im Feld grafik; <id>-loesung.tex ist die fertige Zeichnung einer Lösung, die eine Zeichnung ist (ersetzt den
    Teil „Skizze: …“ der Lösung). Eine Datei nur mit Kommentar (% entfällt …) = Schmuckbild ohne Information;
    erste Zeile „% karo“ = Zeichenaufgabe, die Figur zeigt nur den Gegenstand, Karo bleibt."""
    d = privat / "bau" / "original-neu" / "grafik"
    g = {}
    if d.is_dir():
        for p in sorted(d.glob("*.tex")):
            roh = p.read_text(encoding="utf-8").splitlines()
            t = "\n".join(l for l in roh if not l.lstrip().startswith("%")).strip()
            g[p.stem] = t
            if roh and roh[0].strip() == "% karo":
                g[p.stem + "-karo"] = "1"
    return g


def teile_klammer(s, sep=";"):
    """s an sep teilen, nicht in $…$ und nicht in Klammern."""
    out, cur, m, k = [], "", False, 0
    for i, c in enumerate(s):
        if c == "$" and (i == 0 or s[i - 1] != "\\"):
            m = not m
        k += (c == "(") - (c == ")")
        if c == sep and not m and k <= 0:
            out.append(cur)
            cur = ""
            continue
        cur += c
    return [x.strip() for x in out + [cur] if x.strip()]


def grafik_neu(g):
    if not g:
        return ""
    if ist_tex(g):
        return "\\par\\smallskip\\noindent " + g + "\\par"
    return "\\par\\smallskip\\noindent{\\small\\itshape\\color{mbgrau}Abbildung: " + g + "}\\par"


def raum(z):
    """Rechenraum wie auf dem Blatt: Karo bei Rechnung, Begründung, Zeichnung ohne Vorlage; sonst die Antwortzeile."""
    if z.get("antwort") or z.get("optionen"):
        return ""
    f = z.get("form", "")
    if f in ("rechnung", "begruendung"):
        return "\\karo{%d}" % min(6, max(2, z.get("punkte", 1) + 1))
    if f == "zeichnen" and (not ist_tex(z.get("grafik", "")) or z.get("_karo")):
        return "\\karo{4}"
    return ""


def teil_tex(nr, z, erster):
    inhalt = [z["aufgabe"], grafik_neu(z.get("grafik", "") if not z.get("_grafik_im_stamm") else ""),
              optionen_tex(z.get("optionen") or []), antwortzeile(z.get("antwort", "")), raum(z)]
    out = ["\\hypertarget{%s}{}\\label{%s}" % (z["id"], z["id"]),
           "\\begin{pfaufg}{}{%s}{%d P}" % ("%d." % nr if erster else "", z["punkte"]),
           "\\begin{onteil}{%s)}" % z["teil"]] + [x for x in inhalt if x] + ["\\end{onteil}", "\\end{pfaufg}"]
    return "\n".join(out)


def aufgabe_neu(nr, titel, zeilen):
    out = ["\\Needspace*{0.18\\textheight}\\pfstufekopf{%d \\pkt{} %s}{}" % (nr, titel)]
    stamm = next((z for z in zeilen if z.get("stamm")), None)
    if stamm:
        out.append("\\begin{pfaufg}{}{%d.}{}" % nr)
        out.append(stamm["stamm"] + grafik_neu(stamm.get("grafik", "")))
        out.append("\\end{pfaufg}")
        stamm["_grafik_im_stamm"] = True
    for i, z in enumerate(zeilen):
        out.append(teil_tex(nr, z, i == 0 and not stamm))
    return "\n".join(out)


def blatt_tex(jahr, papier, kenn, aufgaben):
    titel = " \\pkt{} ".join(t for _, t, _, _ in aufgaben)
    out = [PRAEAMBEL, "\\pfheftstil",
           "\\pflaufkopf[%s]{Original}{%s}\\pfseitevon" % (kopf_links(jahr, papier), kenn),
           "\\pfheftkopf{Original ’%02d%s}{}" % (jahr % 100, "" if papier == "OS" else " " + papier),
           "\\pfstufenzeile{%s}" % titel]
    out += [aufgabe_neu(nr, t, z) for nr, t, _, z in aufgaben]
    out.append("\\end{document}")
    return "\n".join(out)


def teile_aussen(s, sep=";"):
    """s an sep teilen, nicht innerhalb von $…$."""
    out, cur, m = [], "", False
    for i, c in enumerate(s):
        if c == "$" and (i == 0 or s[i - 1] != "\\"):
            m = not m
        if c == sep and not m:
            out.append(cur)
            cur = ""
            continue
        cur += c
    return [x.strip() for x in out + [cur] if x.strip()]


def ergebnis(lo):
    """Ergebnis = je Teil (an „;“ außerhalb der Formel) die letzte Gleichung auf „Name op Wert“ verkürzt;
    Weg = die ganze Lösung, wenn sie mehr als das Ergebnis zeigt."""
    erg = []
    for t in teile_aussen(lo):
        m = re.fullmatch(r"\$([^$]*)\$(.*)", t)
        if m and not m.group(2).strip():
            f = m.group(1)
            ops = [(x.start(), x.group(0)) for x in re.finditer(r"=|\\approx", f)]
            if len(ops) >= 2:
                lhs = f[:ops[0][0]].strip()
                wert = f[ops[-1][0] + len(ops[-1][1]):].strip()
                erg.append("$%s %s %s$" % (lhs, ops[-1][1], wert))
                continue
        erg.append(t)
    e = "; ".join(erg)
    return e, (lo if e != "; ".join(teile_aussen(lo)) else "")


def loesung_tex(jahr, papier, kenn, aufgaben):
    out = [PRAEAMBEL, "\\pfheftstil",
           "\\pflaufkopf[%s]{Original \\pkt{} Lösungen}{%s}\\pfseitevon" % (kopf_links(jahr, papier), kenn),
           "\\pfheftkopf{Original ’%02d%s}{Lösungen}" % (jahr % 100, "" if papier == "OS" else " " + papier),
           "\\pfstufenzeile{%s}" % " \\pkt{} ".join(t for _, t, _, _ in aufgaben)]
    for nr, t, _, zeilen in aufgaben:
        out.append("\\pfstufekopf{%d \\pkt{} %s}{}" % (nr, t))
        out.append("\\begin{pfloesungb}{}")
        for i, z in enumerate(zeilen):
            lo, fig = z.get("loesung", ""), z.get("_loesung_grafik", "")
            if fig:
                lo = " ;  ".join(t for t in teile_klammer(lo) if not t.startswith("Skizze:"))
            e, w = ergebnis(lo)
            if fig:
                e = (e + "\\newline " if e else "") + "{\\unboldmath\\mdseries " + fig + "}"
            out.append("\\lzb{%s}{%s)}{%s}{%s}" % ("%d." % nr if i == 0 else "", z["teil"], e, w))
        out.append("\\end{pfloesungb}")
    out.append("\\end{document}")
    return "\n".join(out)


def fingerabdruck(aufgaben):
    import hashlib
    return hashlib.sha1(json.dumps([[nr, t, z] for nr, t, _, z in aufgaben], ensure_ascii=False,
                                   sort_keys=True).encode()).hexdigest()[:12]


def fassung(privat, kenn, abdruck, heft):
    """Fassung wie bei den Blättern (gemeinsam.md „Kennung mit Fassung“): steigt nur mit den Daten. Register
    privat (bau/original-neu/fassungen.csv), weil die Zeile den Heftpfad nennt."""
    p = privat / "bau" / "original-neu" / "fassungen.csv"
    zeilen = p.read_text(encoding="utf-8").splitlines() if p.exists() else ["kennung;fassung;fingerabdruck;heft"]
    eig = [z.split(";") for z in zeilen[1:] if z.split(";")[0] == kenn]
    if eig and eig[-1][2] == abdruck:
        return int(eig[-1][1])
    f = (int(eig[-1][1]) + 1) if eig else 1
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(zeilen + ["%s;%d;%s;%s" % (kenn, f, abdruck, heft)]) + "\n", encoding="utf-8")
    return f


def xe(src, name, vorlage):
    shutil.copyfile(vorlage, src / "mathblatt.sty")
    for _ in range(3):
        subprocess.run(["xelatex", "-interaction=nonstopmode", name + ".tex"], cwd=src, capture_output=True)
    log = (src / (name + ".log")).read_text(encoding="utf-8", errors="replace")
    return [l for l in log.splitlines() if l.startswith("!")], (src / (name + ".pdf"))


# ---------- Ablauf ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heft", required=True, help="z. B. 2026-for")
    ap.add_argument("--privat")
    ap.add_argument("--katalog")
    ap.add_argument("--vorlage")
    ap.add_argument("--kein-pdf", action="store_true")
    ap.add_argument("--form", choices=["blatt", "alt"], default="blatt",
                    help="blatt (v0.2, 14.10.): Layout der Blätter nach privat bau/original-neu/<heft>/; "
                         "alt: Prüfstein v0.1 nach originalneu/<heft>/")
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
    grafiken = lies_grafiken(privat)
    for z in basis + haupt:
        if z["id"] in grafiken:
            z["grafik"] = grafiken[z["id"]]
            if z["id"] + "-karo" in grafiken:
                z["_karo"] = True
        if z["id"] + "-loesung" in grafiken:
            z["_loesung_grafik"] = grafiken[z["id"] + "-loesung"]

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

    if a.form == "blatt":
        kenn = kennung(jahr, papier)
        kenn = "%s-%d" % (kenn, fassung(privat, kenn, fingerabdruck(aufgaben), a.heft))
        ziel = privat / "bau" / "original-neu" / a.heft
        src, pdf = ziel / "src", ziel / "pdf"
        src.mkdir(parents=True, exist_ok=True)
        pdf.mkdir(parents=True, exist_ok=True)
        fehler_alle = []
        for name, tex in (("blatt", blatt_tex(jahr, papier, kenn, aufgaben)),
                          ("loesung", loesung_tex(jahr, papier, kenn, aufgaben))):
            (src / (name + ".tex")).write_text(tex, encoding="utf-8")
            if a.kein_pdf:
                continue
            fehler, p = xe(src, name, vorlage)
            fehler_alle += fehler
            if p.is_file() and not fehler:
                shutil.copyfile(p, pdf / (name + ".pdf"))
            print("%s: %s" % (name, "Fehler: " + "; ".join(fehler[:3]) if fehler else "ok"))
        print("Kennung %s; %d Teilaufgaben in %d Aufgaben; Ordner %s"
              % (kenn, sum(len(z) for _, _, _, z in aufgaben), len(aufgaben), ziel))
        sys.exit(1 if fehler_alle else 0)
    tex, fehlt = heft_tex_alt(a.heft, jahr, papier, aufgaben, kat)
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

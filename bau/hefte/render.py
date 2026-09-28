#!/usr/bin/env python3
"""render.py – kompiliert die Prüfungshefte unter bau/hefte/<name>/.

Aufruf (aus der Repo-Wurzel):
    python3 bau/hefte/render.py [<name> …]

Je Heft höchstens 3 Versuche. Ein Versuch kopiert den Ordner in eine
Arbeitskopie (Scratch, außerhalb des Repos) und kompiliert <K>.tex und
<K>-loesungen.tex mit `xelatex -interaction=nonstopmode -file-line-error`
je zweimal. Die Fehlerzeilen der .log (je Datei und Zeile die erste
Meldung) gehen nach fehler-v<n>.txt im Heftordner. Liegt ein Fehler in
einer Teilaufgabe, wird sie im Quelltext auskommentiert und durch
„(ausgelassen)“ ersetzt – Buchstabe und Lösungszeile bleiben, damit die
Zählung stimmt –, bau.json bekommt „ausgelassen: <id>, Grund“, und der
nächste Versuch läuft. Fehler in einer Lösung (\\erg-Zeile) werden je
Teil in einem Kleinstdokument gesucht. Ergebnis: ergebnis.json neben
diesem Skript, PDFs im Heftordner, wenn kleiner als 2 MB.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
ARBEIT = Path("/tmp/claude-0/hefte-arbeit")
FEHLER = re.compile(r"^\./([^:]+\.tex):(\d+): (.*)$")
START = re.compile(r"^\\(s?teil|s?gl)\b")
ENDE = re.compile(r"^\\(end|begin)\{(teile|gleichungsraster)\}")
MAX_PDF = 2 * 1024 * 1024


def xelatex(ordner, datei, laeufe=2):
    for _ in range(laeufe):
        subprocess.run(["xelatex", "-interaction=nonstopmode",
                        "-file-line-error", datei],
                       cwd=ordner, capture_output=True, timeout=600)
    log = (ordner / datei).with_suffix(".log")
    return log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""


def fehler_aus(log):
    """[(datei, zeile, meldung)], je (Datei, Zeile) die erste Meldung."""
    aus, gesehen = [], set()
    for z in log.splitlines():
        m = FEHLER.match(z)
        if m:
            k = (m.group(1), int(m.group(2)))
            if k not in gesehen:
                gesehen.add(k)
                aus.append((m.group(1), int(m.group(2)), m.group(3).strip()))
    if "Emergency stop" in log or "Fatal error" in log:
        aus.append(("?", 0, "Abbruch (Emergency stop / Fatal error)"))
    return aus


def fehlende_zeichen(log):
    return re.findall(r"Missing character: There is no (\S+)", log)


def teilaufgaben(zeilen):
    """[(hn, index, von, bis)] – Zeilen 1-basiert, bis einschließlich."""
    hn, idx, aus = None, -1, []
    offen = None
    for i, z in enumerate(zeilen, 1):
        m = re.match(r"^\\setcounter\{aufgabe\}\{(\d+)\}", z)
        if m:
            hn = int(m.group(1))
        if z.startswith("\\begin{aufgabe}"):
            hn = (hn or 0) + 1
            idx = -1
        if START.match(z) or ENDE.match(z) or z.startswith("\\end{aufgabe}"):
            if offen:
                aus.append((*offen, i - 1))
                offen = None
        if START.match(z) and not z.startswith("%"):
            idx += 1
            offen = (hn, idx, i)
    return aus


def teil_ersatz(z):
    """Ersatzzeile für eine ausgelassene Teilaufgabe."""
    if z.startswith(("\\gl", "\\sgl")):
        cmd = "\\sgl" if z.startswith("\\sgl") else "\\gl"
        trenner = ""
        for t in (" & \\\\", " &", " \\\\"):
            if z.rstrip().endswith(t):
                trenner = t
                break
        return f"{cmd}{{\\text{{(ausgelassen)}}}}{trenner}"
    cmd = "\\steil" if z.startswith("\\steil") else "\\teil"
    return f"{cmd} \\textit{{(ausgelassen)}}"


def lasse_aus(ordner, datei_a, von, bis, id_, grund):
    pfad = ordner / datei_a
    zeilen = pfad.read_text(encoding="utf-8").split("\n")
    alt = zeilen[von - 1:bis]
    neu = [f"% AUSGELASSEN {id_}: {grund}"] + ["% " + z for z in alt] \
        + [teil_ersatz(alt[0])]
    zeilen[von - 1:bis] = neu
    pfad.write_text("\n".join(zeilen), encoding="utf-8", newline="\n")


def loesung_aus(ordner, datei_l, hn, buchst):
    pfad = ordner / datei_l
    zeilen = pfad.read_text(encoding="utf-8").split("\n")
    for i, z in enumerate(zeilen):
        if z.startswith(f"\\erg{{{hn}}}{{"):
            kopf = f"\\erg{{{hn}}}{{"
            rumpf = z[len(kopf):-1]
            teile = re.split(r" \\quad (?=[a-z]\) )", rumpf)
            teile = [f"{buchst}) ausgelassen" if t.startswith(f"{buchst}) ")
                     else t for t in teile]
            zeilen[i] = kopf + " \\quad ".join(teile) + "}"
            break
    pfad.write_text("\n".join(zeilen), encoding="utf-8", newline="\n")


def loesungsteil_fehler(ordner, zeile):
    """Buchstaben der Teile einer \\erg-Zeile, die allein nicht kompilieren."""
    m = re.match(r"^\\erg\{(\d+)\}\{(.*)\}$", zeile)
    if not m:
        return []
    probe = ARBEIT / "_probe"
    if probe.exists():
        shutil.rmtree(probe)
    probe.mkdir(parents=True)
    shutil.copyfile(ordner / "mathblatt.sty", probe / "mathblatt.sty")
    schlecht = []
    for t in re.split(r" \\quad (?=[a-z]\) )", m.group(2)):
        (probe / "p.tex").write_text(
            "\\documentclass[11pt]{article}\\usepackage{mathblatt}\n"
            "\\begin{document}\n\\erg{1}{" + t + "}\n\\end{document}\n",
            encoding="utf-8")
        log = xelatex(probe, "p.tex", 1)
        if fehler_aus(log):
            schlecht.append(t.split(")", 1)[0])
    return schlecht


def teil_allein_fehlerhaft(ordner, zeilen, von, bis):
    """Kompiliert eine Teilaufgabe allein in einem Kleinstdokument; True,
    wenn sie dort Fehler wirft (trennt Ursache von Folgefehlern)."""
    probe = ARBEIT / "_probe"
    if probe.exists():
        shutil.rmtree(probe)
    probe.mkdir(parents=True)
    shutil.copyfile(ordner / "mathblatt.sty", probe / "mathblatt.sty")
    teil = zeilen[von - 1:bis]
    if teil and teil[0].startswith(("\\gl", "\\sgl")):
        rumpf = (["\\begin{gleichungsraster}[2]"]
                 + [re.sub(r"( & \\\\| &| \\\\)\s*$", "", teil[0]) + " & \\\\"]
                 + teil[1:] + ["\\end{gleichungsraster}"])
    else:
        rumpf = ["\\begin{teile}"] + teil + ["\\end{teile}"]
    (probe / "p.tex").write_text(
        "\n".join(["\\documentclass[11pt]{article}", "\\usepackage{mathblatt}",
                   "\\begin{document}", "\\begin{aufgabe}{Probe}"] + rumpf
                  + ["\\end{aufgabe}", "\\end{document}", ""]),
        encoding="utf-8")
    return bool(fehler_aus(xelatex(probe, "p.tex", 1)))


def render(name, ergebnis):
    heft = HIER / name
    zettel = json.loads((heft / "bau.json").read_text(encoding="utf-8"))
    k = zettel["kennung"]
    nach_stelle = {(a["datei"], a["hauptnummer"], a["teilaufgabe"]): a["id"]
                   for a in zettel["aufgaben"]}
    zettel.setdefault("ausgelassen", [])
    e = {"heft": name, "kennung": k, "versuche": 0, "fehler_je_versuch": [],
         "fehler": [], "ausgelassen": [], "seiten": None,
         "seiten_loesungen": None, "pdf_groesse": {}, "fehlende_zeichen": 0}
    for versuch in range(1, 4):
        e["versuche"] = versuch
        ziel = ARBEIT / name
        if ziel.exists():
            shutil.rmtree(ziel)
        shutil.copytree(heft, ziel, ignore=shutil.ignore_patterns(
            "*.pdf", "fehler-v*.txt"))
        logs = {d: xelatex(ziel, d) for d in (f"{k}.tex", f"{k}-loesungen.tex")}
        fehler = []
        for d, log in logs.items():
            fehler += [(d, f, z, m) for f, z, m in fehler_aus(log)]
        with open(heft / f"fehler-v{versuch}.txt", "w", encoding="utf-8",
                  newline="\n") as f:
            f.write(f"# {name} ({k}), Versuch {versuch}: {len(fehler)} "
                    "Fehlerstellen (je Datei und Zeile die erste Meldung)\n")
            for d, datei, z, m in fehler:
                f.write(f"{d} → {datei}:{z}: {m}\n")
        e["fehler_je_versuch"].append(len(fehler))
        e["fehler"] = [{"dokument": d, "datei": datei, "zeile": z,
                        "meldung": m} for d, datei, z, m in fehler]
        if not fehler:
            break
        if versuch == 3:
            break
        # Fehler den Teilaufgaben zuordnen
        treffer = {}
        for d, datei, z, m in fehler:
            if datei.endswith("_a.tex"):
                zeilen = (heft / datei).read_text(encoding="utf-8").split("\n")
                for hn, idx, von, bis in teilaufgaben(zeilen):
                    if von <= z <= bis:
                        b = "abcdefghijklmnopqrstuvwxyz"[idx]
                        treffer.setdefault((datei, hn, b), (von, bis, m))
                        break
            elif datei.endswith("_l.tex"):
                zeilen = (heft / datei).read_text(encoding="utf-8").split("\n")
                zl = zeilen[z - 1] if 0 < z <= len(zeilen) else ""
                mm = re.match(r"^\\erg\{(\d+)\}", zl)
                if not mm:
                    continue
                hn = int(mm.group(1))
                a_datei = datei[:-6] + "_a.tex"
                a_zeilen = (heft / a_datei).read_text(encoding="utf-8").split("\n")
                for b in loesungsteil_fehler(heft, zl):
                    for h2, idx, von, bis in teilaufgaben(a_zeilen):
                        if h2 == hn and "abcdefghijklmnopqrstuvwxyz"[idx] == b:
                            treffer.setdefault((a_datei, hn, b),
                                               (von, bis, "Lösung: " + m))
        # Ursache von Folgefehlern trennen: nur Teilaufgaben, die allein
        # fehlschlagen; schlägt keine allein fehl, die erste je Datei
        bestaetigt = {}
        for (datei, hn, b), (von, bis, m) in treffer.items():
            zeilen = (heft / datei).read_text(encoding="utf-8").split("\n")
            if m.startswith("Lösung: ") or teil_allein_fehlerhaft(
                    heft, zeilen, von, bis):
                bestaetigt[(datei, hn, b)] = (von, bis, m)
        for datei in {t[0] for t in treffer}:
            if not any(t[0] == datei for t in bestaetigt):
                erste = min((t for t in treffer.items() if t[0][0] == datei),
                            key=lambda t: t[1][0])
                bestaetigt[erste[0]] = erste[1]
        e.setdefault("folgefehler_verschont", []).extend(
            f"{d} Nr. {hn}{b}" for (d, hn, b) in treffer if (d, hn, b)
            not in bestaetigt)
        treffer = bestaetigt
        if not treffer:
            break
        # von unten nach oben ersetzen, damit Zeilennummern stimmen
        for (datei, hn, b), (von, bis, m) in sorted(
                treffer.items(), key=lambda t: (t[0][0], -t[1][0])):
            id_ = nach_stelle.get((datei, hn, b), "?")
            lasse_aus(heft, datei, von, bis, id_, m)
            loesung_aus(heft, datei[:-6] + "_l.tex", hn, b)
            eintrag = f"ausgelassen: {id_}, {m} (Nr. {hn}{b}, Versuch {versuch})"
            zettel["ausgelassen"].append(eintrag)
            e["ausgelassen"].append({"id": id_, "nr": f"{hn}{b}",
                                     "datei": datei, "grund": m,
                                     "versuch": versuch})
        (heft / "bau.json").write_text(
            json.dumps(zettel, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8", newline="\n")
    ziel = ARBEIT / name
    for d, schluessel in ((f"{k}.pdf", "seiten"),
                          (f"{k}-loesungen.pdf", "seiten_loesungen")):
        pdf = ziel / d
        if pdf.exists():
            info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                  text=True).stdout
            m = re.search(r"Pages:\s+(\d+)", info)
            e[schluessel] = int(m.group(1)) if m else None
            groesse = pdf.stat().st_size
            e["pdf_groesse"][d] = groesse
            if groesse < MAX_PDF:
                shutil.copyfile(pdf, heft / d)
    log = (ziel / f"{k}.log").read_text(encoding="utf-8", errors="replace")
    e["fehlende_zeichen"] = len(fehlende_zeichen(log))
    e["fehlende_zeichen_art"] = sorted(set(fehlende_zeichen(log)))
    ergebnis[name] = e
    print(f"{name}: {e['versuche']} Versuch(e), Fehler {e['fehler_je_versuch']}, "
          f"ausgelassen {len(e['ausgelassen'])}, Seiten {e['seiten']}"
          f"+{e['seiten_loesungen']}", flush=True)


def main():
    namen = sys.argv[1:] or sorted(p.name for p in HIER.iterdir()
                                   if (p / "bau.json").exists())
    pfad = HIER / "ergebnis.json"
    ergebnis = json.loads(pfad.read_text(encoding="utf-8")) if pfad.exists() else {}
    for n in namen:
        render(n, ergebnis)
        pfad.write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()

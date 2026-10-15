#!/usr/bin/env python3
"""neusatz-abi.py – alle Abitur-GK-Blätter neu setzen, dann Bestellkarte, Handreichung und (mit --mappe) Mappe, ohne Modell.

Anlass: 15.10.2026, 33 Blätter Abitur GK (plan.md § 7 M5); Muster werkzeuge/neusatz-p10.py. Einheiten, Folge und
Ordner aus mathe-nachhilfe abitur/gliederung/*.md (werkzeuge/p10einheiten.py abi_einheiten). Je Einheit
  pruefheft.py --pruefung abitur --kapitel <k> --art p --einheit "<Einheit>" --datum <d>
               --aus bau/pruefung/<d>/abitur/<ordner>
Bericht je Blatt: Seiten des Blatts (2-blatt), LaTeX-Fehler und Overfull über 5 pt über alle fünf Dateien
(1-uebersicht … 5-mehr-loesungen; Log in <ordner>/src/*.log, pruefheft.py v0.17). Kein Abbruch beim ersten Fehler.
Danach bestellkarte.py --pruefung abi-gk (Karte und Handreichung), mit --mappe zuletzt mappe-abi.py.

  python3 werkzeuge/neusatz-abi.py --datum 2026-10-15 [--nur nullstellen,baum] [--jobs 4] [--ohne-karte] [--mappe]
Rückgabe 1, wenn ein Blatt mit Fehler gesetzt wurde oder ein Folgeskript scheiterte.
"""
import argparse, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import abi_einheiten, MN_VORGABE  # noqa: E402

DATEI = re.compile(r'^(\d-[\w-]+): (\d+) Seiten, Fehler (\d+), Missing character (\d+), Overfull (\d+)'
                   r'(?: \(über 5 pt: (\d+)(?:, max ([\d.]+) pt)?\))?')


def setze(e, a):
    aus = os.path.join(BANK, 'bau', 'pruefung', a.datum, 'abitur', e['ordner'])
    r = subprocess.run([sys.executable, os.path.join(HIER, 'pruefheft.py'), '--pruefung', 'abitur',
                        '--kapitel', e['kapitel'], '--art', 'p', '--einheit', e['einheit'], '--datum', a.datum,
                        '--aus', aus, '--mn', a.mn, '--bb', a.bb], capture_output=True, text=True, cwd=BANK)
    dateien = [DATEI.match(z) for z in r.stdout.splitlines()]
    dateien = [m for m in dateien if m]
    blatt = next((int(m.group(2)) for m in dateien if m.group(1) == '2-blatt'), 0)
    fehler = sum(int(m.group(3)) for m in dateien)
    missing = sum(int(m.group(4)) for m in dateien)
    gross = sum(int(m.group(6) or 0) for m in dateien)
    gmax = max([float(m.group(7)) for m in dateien if m.group(7)] or [0])
    tex_fehler = [z.strip() for z in r.stdout.splitlines() if z.startswith('    !')]
    hinweise = [z[9:] for z in r.stdout.splitlines() if z.startswith('Hinweis: ')]
    schlecht = r.returncode != 0 or not dateien or fehler > 0 or gross > 0 or missing > 0
    zeile = (f'{e["kennung"]:6} {e["ordner"]:22} Blatt {blatt} S. · LaTeX-Fehler {fehler} · Overfull > 5 pt {gross}'
             + (f' (max {gmax:.1f} pt)' if gross else '') + (f' · Missing character {missing}' if missing else '')
             + (' · ABBRUCH' if r.returncode or not dateien else '') + (' FEHLER' if schlecht else ''))
    rest = tex_fehler[:3] + ([(r.stdout + r.stderr).strip()[-600:]] if r.returncode or not dateien else [])
    return e, zeile, schlecht, rest, hinweise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--bb', default=os.path.join(os.path.dirname(BANK), 'blattbau'))
    ap.add_argument('--nur', default='', help='Ordner oder Kennungen, durch Komma getrennt')
    ap.add_argument('--jobs', type=int, default=4, help='Blätter gleichzeitig (je Lauf ein eigener Arbeitsordner)')
    ap.add_argument('--hinweise', action='store_true', help='Hinweise des Setzers je Blatt mit ausgeben')
    ap.add_argument('--ohne-karte', action='store_true', help='keine Bestellkarte und Handreichung')
    ap.add_argument('--mappe', action='store_true', help='zuletzt mappe-abi.py (beide Ausgaben)')
    a = ap.parse_args()
    nur = {x.strip() for x in a.nur.split(',') if x.strip()}
    eins = [e for e in abi_einheiten(a.mn) if not nur or e['ordner'] in nur or e['kennung'] in nur]
    if nur and not eins:
        sys.exit(f'--nur {a.nur}: keine Einheit')
    fehler = []
    with ThreadPoolExecutor(max_workers=max(1, a.jobs)) as ex:
        for e, zeile, schlecht, rest, hinweise in ex.map(lambda e: setze(e, a), eins):   # Ausgabe in Lernfolge
            print(zeile, flush=True)
            for z in rest:
                print('   ', z)
            if a.hinweise:
                for h in hinweise:
                    print('    Hinweis:', h)
            if schlecht:
                fehler.append(e['kennung'])
    print(f'Blätter: {len(eins)}, mit Fehler {len(fehler)}' + (f' ({", ".join(fehler)})' if fehler else ''))
    folge = [] if a.ohne_karte else [['bestellkarte.py', '--pruefung', 'abi-gk'],
                                      ['bestellkarte.py', '--pruefung', 'abi-gk', '--handreichung']]
    if a.mappe:
        folge.append(['mappe-abi.py'])
    for skript, *extra in folge:
        r = subprocess.run([sys.executable, os.path.join(HIER, skript), '--datum', a.datum, '--mn', a.mn] + extra,
                           capture_output=True, text=True, cwd=BANK)
        print(skript, *extra, '\n'.join(r.stdout.strip().splitlines()[-3:]), r.stderr.strip()[-800:])
        if r.returncode:
            fehler.append(skript)
    print('Fehler:', ', '.join(fehler) or 'keine')
    sys.exit(1 if fehler else 0)


if __name__ == '__main__':
    main()

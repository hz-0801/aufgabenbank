#!/usr/bin/env python3
"""neusatz-p10.py – alle P10-Blätter neu setzen, dann Bestellkarte und Gesamtheft, ohne Modell.

Anlass: plan.md § 7 Schritt 2 (14.10.): Neusatz per Skript statt Schleife von Hand. Einheiten, Folge und Ordner
aus den Gliederungen (werkzeuge/p10einheiten.py). Je Einheit
  pruefheft.py --kapitel <k> --art p --einheit "<Zuschnitt>" --datum <d> --aus bau/pruefung/<d>/<ordner>
(Register und Fassungsregister wie bei jedem Bau), danach bestellkarte.py und gesamtheft.py.

  python3 werkzeuge/neusatz-p10.py --datum 2026-10-14 [--nur pythagoras,winkel] [--ohne-heft]
Rückgabe 1, wenn ein Blatt mit Fehler gesetzt wurde.
"""
import argparse, os, re, subprocess, sys

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from p10einheiten import einheiten, MN_VORGABE  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=MN_VORGABE)
    ap.add_argument('--nur', default='')
    ap.add_argument('--ohne-heft', action='store_true')
    a = ap.parse_args()
    nur = {x for x in a.nur.split(',') if x}
    fehler = []
    for e in einheiten(a.mn):
        if nur and e['ordner'] not in nur:
            continue
        aus = os.path.join(BANK, 'bau', 'pruefung', a.datum, e['ordner'])
        r = subprocess.run([sys.executable, os.path.join(HIER, 'pruefheft.py'), '--kapitel', e['kapitel'], '--art', 'p',
                            '--einheit', e['einheit'], '--datum', a.datum, '--aus', aus, '--mn', a.mn],
                           capture_output=True, text=True, cwd=BANK)
        zeilen = [z for z in r.stdout.splitlines() if re.match(r'^\d-\w+: ', z) or z.startswith('Kennung ')]
        f = r.returncode != 0 or any(not re.search(r'Fehler 0,', z) for z in zeilen if re.match(r'^\d-', z))
        print(f'{e["kennung"]} {e["ordner"]}: ' + ' | '.join(zeilen) + (' FEHLER' if f else ''), flush=True)
        if f:
            fehler.append(e['ordner'])
            print(r.stdout[-1500:], r.stderr[-1500:])
    if not a.ohne_heft:
        for skript in ('bestellkarte.py', 'gesamtheft.py'):
            r = subprocess.run([sys.executable, os.path.join(HIER, skript), '--datum', a.datum, '--mn', a.mn],
                               capture_output=True, text=True, cwd=BANK)
            print(skript, r.stdout.strip(), r.stderr.strip()[-800:])
            if r.returncode:
                fehler.append(skript)
    print('Fehler:', ', '.join(fehler) or 'keine')
    sys.exit(1 if fehler else 0)


if __name__ == '__main__':
    main()

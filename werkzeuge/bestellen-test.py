#!/usr/bin/env python3
"""bestellen-test.py – prüft werkzeuge/bestellen.py an allen Fällen von plan.md § 10, 15.10.2026 (k).

Trägt die Testschülerin „Lena“ als S99 (P10, FOR) in aufgabenbank-privat schueler.md ein, bestellt alle Fälle
(Eingabe -> Rückfrage -> Lieferung), führt einige mit --ausfuehren aus (Lieferzeilen, Laufzeit ≤ 60 s je P10-Blatt,
einmal mit frischem Satz in einen Tagesordner --datum 2099-01-01) und räumt am Ende alles wieder weg: Zeilen in
schueler.md, Lieferzeilen in eingang/gebaut.csv, bau/register.csv, bau/fassungen.csv, den Tagesordner.

  python3 werkzeuge/bestellen-test.py            Rückgabe 0 = alle Fälle grün
"""
import json
import os
import shutil
import subprocess
import sys
import time

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
PRIVAT = os.environ.get('PRIVAT') or os.path.join(os.path.dirname(BANK), 'aufgabenbank-privat')
SCHUELER = os.path.join(PRIVAT, 'schueler.md')
SICHERN = [SCHUELER, os.path.join(BANK, 'eingang', 'gebaut.csv'), os.path.join(BANK, 'bau', 'register.csv'),
           os.path.join(BANK, 'bau', 'fassungen.csv')]
FRISCH = '2099-01-01'
ergebnis = []


def b(eingabe, *extra):
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(HIER, 'bestellen.py'), eingabe, *extra],
                       capture_output=True, text=True, cwd=BANK)
    try:
        d = json.loads(r.stdout)
    except ValueError:
        d = {'fehler': (r.stdout + r.stderr)[-800:]}
    d['_zeit'] = time.time() - t0
    return d


def pruef(name, bed, d, mehr=''):
    ergebnis.append(bool(bed))
    print(('ok    ' if bed else 'FEHLER') + f' {name}' + (f' – {mehr}' if mehr else '') +
          ('' if bed else '\n       ' + json.dumps({k: v for k, v in d.items() if v}, ensure_ascii=False)[:600]))


def endet(d, *namen):
    return [os.path.basename(x) for x in d.get('dateien', [])] == list(namen)


def main():
    alt = {p: open(p, encoding='utf-8').read() for p in SICHERN}
    t = alt[SCHUELER]
    a = t.find('\n## Schüler')
    e = t.find('\n## ', a + 3)
    open(SCHUELER, 'w', encoding='utf-8').write(
        t[:e].rstrip('\n') + '\n| 99 | Lena | 10 | Regine-Hildebrandt-Schule | ? | P10 | FOR |\n' + t[e:])
    try:
        faelle()
    finally:
        for p, inhalt in alt.items():
            open(p, 'w', encoding='utf-8').write(inhalt)
        shutil.rmtree(os.path.join(BANK, 'bau', 'pruefung', FRISCH), ignore_errors=True)
        print('aufgeräumt: schueler.md, gebaut.csv, register.csv, fassungen.csv, Tagesordner', FRISCH)
    n = len(ergebnis)
    print(f'{sum(ergebnis)} von {n} grün')
    sys.exit(0 if all(ergebnis) else 1)


def faelle():
    d = b('Lena ana')
    pruef('Lena ana -> 1 Wahl, Vorschlag + 2', d.get('frage') and len(d['frage']['optionen']) == 3
          and 'Vorschlag' in d['frage']['optionen'][0] and 'PA10' in d['frage']['optionen'][0], d)
    d = b('Lena ana', '--wahl', '1')
    pruef('Lena ana --wahl 1 -> Übersicht, Blatt, Lösung', endet(d, '1-uebersicht.pdf', '2-blatt.pdf',
                                                               '3-loesungen.pdf') and 'Lena · P10' in d['zeile'], d)
    d = b('Lena Parabel')
    pruef('Lena Parabel -> keine Frage, PA30', not d['frage'] and '(PA30' in d['zeile']
          and endet(d, '1-uebersicht.pdf', '2-blatt.pdf', '3-loesungen.pdf'), d)
    d = b('Lena PA30', '--ausfuehren')
    pruef('Lena PA30 --ausfuehren -> drei PDFs, Lieferzeile, ≤ 60 s', len(d.get('pdf', [])) == 3 and d.get('lieferung')
          and 'angehängt' in d['lieferung'][0] and d['_zeit'] <= 60, d, f'{d["_zeit"]:.1f} s (Tagesordner)')
    d = b('Lena PA30')
    pruef('Lena PA30 nochmal -> keine Frage, Hinweis „hatte schon“', not d['frage'] and 'schon' in (d['hinweis'] or ''),
          d)
    d = b('Lena ana')
    pruef('Lena ana nach PA30 -> Vorschlag PA40', d.get('frage') and 'PA40' in d['frage']['optionen'][0], d)
    d = b('Lena PA30 mehr', '--ausfuehren')
    pruef('Lena PA30 mehr -> Mehr + Lösung', endet(d, 'mehr.pdf', 'mehr-loesung.pdf') and len(d.get('pdf', [])) == 2,
          d, f'{d["_zeit"]:.1f} s')
    d = b('Lena Lösung PA30')
    pruef('Lena Lösung PA30 -> nur Lösung', endet(d, '3-loesungen.pdf'), d)
    d = b('Lena basis')
    pruef('Lena basis -> 1 Wahl Zettel', d.get('frage') and 'BAS-Z1' in d['frage']['optionen'][0], d)
    d = b('Lena basis', '--wahl', '1', '--ausfuehren')
    pruef('Lena basis --wahl 1 -> Zettel mit Ergebnissen', endet(d, 'BAS-Z1.pdf') and d.get('lieferung'), d)
    d = b('Lena basis')
    pruef('Lena basis danach -> Vorschlag BAS-Z2', d.get('frage') and 'BAS-Z2' in d['frage']['optionen'][0], d)
    d = b('Original 24')
    pruef('Original 24 -> Heftseiten privat', endet(d, '2024-os.pdf') and 'aufgabenbank-privat' in d['dateien'][0]
          and 'nur Lehrer' in d['zeile'], d)
    d = b('Original neu 24')
    pruef('Original neu 24 -> Blatt + Lösung privat', endet(d, 'blatt.pdf', 'loesung.pdf') and
          'original-neu/2024-os' in d['dateien'][0], d)
    d = b('Lena Probeprüfung')
    pruef('Lena Probeprüfung -> 1 Wahl Jahr, neuestes zuerst', d.get('frage') and '’26' in d['frage']['optionen'][0], d)
    d = b('Lena Probeprüfung', '--wahl', '1', '--ausfuehren')
    pruef('Lena Probeprüfung --wahl 1 -> Original neu ’26 ganz + Lösung', endet(d, 'blatt.pdf', 'loesung.pdf')
          and '2026-for' in d['dateien'][0] and d.get('lieferung'), d)
    d = b('Lena Probeprüfung')
    pruef('Lena Probeprüfung danach -> neuestes offenes ’25', d.get('frage') and '’25' in d['frage']['optionen'][0], d)
    for w, n in (('Karte', 'bestellkarte.pdf'), ('Handreichung', 'handreichung-muster.pdf'),
                 ('Gesamtheft', 'gesamtheft-p10.pdf'), ('Mappe', 'mappe-p10.pdf')):
        d = b(w)
        pruef(f'{w} -> {n}', endet(d, n) and os.path.exists(d['dateien'][0]), d)
    pruef('Mappe liegt privat', 'aufgabenbank-privat' in d['dateien'][0], d)
    d = b('Lena Liste')
    pruef('Lena Liste -> Lieferungen', len(d.get('liste', [])) >= 4 and any('PA30' in z for z in d['liste']), d)
    d = b('Lena was Leichteres zu Parabeln')
    pruef('Freitext „was Leichteres zu Parabeln“ -> PA30 + „leichter gibt es noch nicht“', '(PA30' in d['zeile']
          and 'leichter gibt es noch nicht' in (d['hinweis'] or ''), d)
    d = b('PA30')
    pruef('ohne Namen PA30 -> ohne Lieferzeile', not d['zeile'].startswith('Du bekommst: Lena') and
          'Du bekommst: P10' in d['zeile'], d)
    d = b('ana', '--wahl', '2', '--ausfuehren')
    pruef('ohne Namen ana --wahl 2 --ausfuehren -> keine Lieferzeile', not d.get('lieferung') and
          len(d.get('pdf', [])) == 3, d, f'{d["_zeit"]:.1f} s')
    d = b('Testa ana')
    pruef('unbekannter Name -> einmal Prüfung erfragen', d.get('frage') and 'Testa' in d['frage']['text']
          and any('Abitur' in o for o in d['frage']['optionen']), d)
    abi = 1 + next(i for i, o in enumerate(d['frage']['optionen']) if o == 'Abitur GK')
    d = b('Testa ana', '--wahl', str(abi))
    eingetragen = '| Testa |' in open(SCHUELER, encoding='utf-8').read()
    pruef('unbekannter Name --wahl Abitur GK -> eingetragen, keine zweite Frage, Zeile was fehlt', eingetragen and
          not d['frage'] and 'Abitur' in (d['hinweis'] or '') and 'Abitur GK' in d['zeile'], d)
    d = b('Testa Handreichung')
    pruef('Abitur GK Handreichung -> was es gibt', endet(d, 'handreichung-abi-gk-2027.pdf'), d)
    d = b('Testa Original 24')
    pruef('Abitur Original -> Zeile was fehlt', not d['dateien'] and 'Originale' in (d['hinweis'] or ''), d)
    d = b('Testb geo')
    fhr = 1 + next(i for i, o in enumerate(d['frage']['optionen']) if o == 'FHR')
    d = b('Testb geo', '--wahl', str(fhr))
    pruef('FHR -> Zeile was fehlt', not d['dateien'] and 'FHR' in (d['hinweis'] or ''), d)
    d = b('Lena Lernblatt Terme')
    pruef('Lernblatt Terme -> bauen mit Thema', d.get('bauen') and d['bauen']['eintrag'] == 'terme'
          and 'wird gebaut' in d['zeile'], d)
    d = b('Lena Klasse 9 Brüche')
    pruef('Lena Klasse 9 Brüche -> bauen, Klasse 9', d.get('bauen') and d['bauen']['klasse'] == 9
          and 'br' in d['bauen']['eintrag'], d)
    d = b('Lena PA10', '--datum', FRISCH, '--ausfuehren')
    pruef('frischer Satz eines P10-Blatts ≤ 60 s', len(d.get('pdf', [])) == 3 and d.get('befehle')
          and d['_zeit'] <= 60, d, f'{d["_zeit"]:.1f} s (Setzer)')


if __name__ == '__main__':
    main()

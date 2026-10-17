#!/usr/bin/env python3
"""satz-pruef.py – Satz-Checkliste für Kapitelblätter P10, Teil Skript
(plan.md § 7 Schritt 3; die übrigen Punkte prüft der Kritiker nach
bau/satz-checkliste.md). Liest nur, schreibt nichts.

  python3 werkzeuge/satz-pruef.py --kapitel quadratische --datum 2026-10-17

Gelesen: bau/kapitel/<datum>/<kapitel>/ (PDFs und src/*.tex),
mathe-nachhilfe msa/buchkapitel-p10.csv (Zeilen mit blatt = --kapitel),
msa/kapitel-p10/<kapitel>.csv; FOR-Regel aus pruefheft.stern_fuer.

Muster neben das Skript (kandidaten.md 16.10. d): Jede Prüfung muss am
abgenommenen Muster (PA30, bau/kapitel/2026-10-17/quadratische) 0 melden;
Grenzwerte (Karo, Kästchengröße) sind die des Musters. Ändert sich das
Muster, wird das Skript daran neu gelaufen, bevor es für die Breite gilt.

Prüfungen (Kennung – Quelle):
  S1 DATEIEN    je bestellbarem Abschnitt Blatt und Lösung (17.10. Punkt 9)
  S2 SEITEN     Hinweis (kein Fehler): Abschnitt über 3 Seiten, mit Unter-
                abschnitten über 4 – 17.10. d erlaubt mehr, wenn sonst Originale
                oder Rechenraum fehlten; das urteilt der Kritiker
  S3 KOPF       Kennung oben rechts auf Seite 1 (17.10. Punkt 3)
  S4 UEBERSCHR  keine Abschnittsüberschrift als letzte Zeile einer Seite
                (Lehrer 15.10. PG10, gemeinsam.md „Ruhe“)
  S5 FOR        „* nur FOR“ genau einmal, wenn eine FOR-Aufgabe gedruckt
                ist, sonst nie; kein „nur FOR“ an der Aufgabe (17.10. P. 6)
  S6 TEILEN     kein Geteilt-Zeichen in Formeln (15.10. q)
  S7 BEIWERK    kein Kern, kein Formelkasten, kein Mehr (17.10. a, d)
  S8 KAESTCHEN  Koordinatensystem mit Kästchen ≥ 0,45 cm (17.10. P. 7,
                Muster)
  S9 RECHENRAUM jede Aufgabe mit Karo hat mindestens 2 Zeilen (Muster;
                „voll, eher mehr“ urteilt der Kritiker, 17.10. d)
  S10 ZWEI      Lösung: zweiter Wert (x₂, S₂, N₂) nie am Zeilenanfang
                (17.10. P. 8)
  S11 TEILBUCHST  kein „a)“ im Wortlaut einer Einzelaufgabe (Lehrer 16.10.
                PA10, 16.10. PA20)
"""
import argparse, csv, os, re, subprocess, sys

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def lies(p):
    return list(csv.DictReader(open(p, encoding='utf-8'), delimiter=';'))


def text(pdf, seite=None):
    a = ['pdftotext', '-layout'] + (['-f', str(seite), '-l', str(seite)] if seite else []) + [pdf, '-']
    return subprocess.run(a, capture_output=True, text=True).stdout


def seiten(pdf):
    out = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    m = re.search(r'Pages:\s+(\d+)', out)
    return int(m.group(1)) if m else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--kapitel', required=True)
    ap.add_argument('--datum', required=True)
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe'))
    a = ap.parse_args()
    ordner = os.path.join(BANK, 'bau', 'kapitel', a.datum, a.kapitel)
    buch = [b for b in lies(os.path.join(a.mn, 'msa', 'buchkapitel-p10.csv'))
            if b.get('blatt', a.kapitel) == a.kapitel and not re.search(r'-B\d', b['id'])]   # 17.10. q
    zeilen = [r for r in lies(os.path.join(a.mn, 'msa', 'kapitel-p10', f'{a.kapitel}.csv'))
              if not all(re.search(r'-B\d', d) for d in r['deckt'].split())]
    sys.path.insert(0, os.path.join(BANK, 'werkzeuge'))
    import pruefheft as P   # dieselbe FOR-Regel wie der Setzer (stern_fuer)
    import kapitelblatt as K
    D = P.Daten(a.mn, K.DATEN.get(a.kapitel, a.kapitel))
    meld, hinweis = [], []

    def m(k, s):
        meld.append(f'{k}: {s}')

    # Abschnitte wie kapitelblatt.gliedern
    kap = list(dict.fromkeys(b['kapitel'] for b in buch))
    stuecke = ['']
    unter = {}
    for i, k in enumerate(kap):
        bst = 'ABCDEFGH'[i]
        stuecke.append(bst)
        ab = list(dict.fromkeys(b['abschnitt'] for b in buch if b['kapitel'] == k))
        if len(ab) > 1:
            unter[bst] = [f'{bst}{j + 1}' for j in range(len(ab))]
            stuecke += unter[bst]
    namen = {b['kapitel'] for b in buch} | {b['abschnitt'] for b in buch if b['abschnitt']}
    ueber = re.compile(r'^\s*[A-H]\d?\s+(' + '|'.join(re.escape(n) for n in sorted(namen, key=len, reverse=True)) + r')\s*$')

    for s in stuecke:
        vor = s + '-' if s else ''
        for art in ('blatt', 'loesung'):
            pdf = os.path.join(ordner, f'{vor}{art}.pdf')
            if not os.path.exists(pdf):
                m('S1 DATEIEN', f'{vor}{art}.pdf fehlt')
                continue
            n = seiten(pdf)
            if art == 'blatt' and s:
                grenze = 4 if s in unter else 3
                if n > grenze:
                    hinweis.append(f'S2 SEITEN (Hinweis an den Kritiker): {vor}blatt {n} Seiten, Richtwert {grenze} – länger nur, wenn sonst Originale oder Rechenraum fehlten (17.10. d)')
            t = text(pdf)
            if art == 'blatt':
                if not re.search(r'\bP[AGSZ]\d{2}\b', text(pdf, 1)[:3000]):
                    m('S3 KOPF', f'{vor}blatt: keine Kennung oben')
                # S4: letzte Inhaltszeile einer Seite ist eine Überschrift
                for nr, seite in enumerate(t.split('\f'), 1):
                    zz = [z for z in seite.split('\n') if re.search(r'[A-Za-zÄÖÜäöüß]{3}', z)
                          and not re.search(r'\|\s*\d+:', z) and not re.match(r'^\s*\d+/\d+\s*$', z)]
                    if zz and ueber.match(zz[-1]):
                        m('S4 UEBERSCHR', f'{vor}blatt S. {nr}: „{zz[-1].strip()}“ allein unten')
                gedr = re.findall(r'^% DRUCK (\S+) deckt (.*)$',
                                  open(os.path.join(ordner, 'src', f'{vor}blatt.tex'), encoding='utf-8').read(), re.M)
                hat_for = any(all(P.stern_fuer(D, d) for d in set(dk.split()) | {re.sub(r'-\d$', '', i)}) for i, dk in gedr)
                n_for = len(re.findall(r'^\s*\*\s*nur FOR\s*$', t, re.M))
                if n_for != (1 if hat_for else 0):
                    m('S5 FOR', f'{vor}blatt: „* nur FOR“ {n_for}-mal, FOR-Aufgabe {"ja" if hat_for else "nein"}')
                if len(re.findall(r'nur FOR', t)) > n_for:
                    m('S5 FOR', f'{vor}blatt: „nur FOR“ an einer Aufgabe')
                if re.search(r'^\s*[A-H]?\d?\s*(Kern|Formelkasten|Mehr|Ältere Prüfungsaufgaben)\b', t, re.M):
                    m('S7 BEIWERK', f'{vor}blatt: Kern, Formelkasten oder Mehr')
            else:
                for z in t.split('\n'):
                    if re.match(r'^\s*(x|S|N|P)₂\b', z):
                        m('S10 ZWEI', f'{vor}loesung: „{z.strip()[:40]}“')
    # Daten
    for r in zeilen:
        roh = r['wortlaut'] + ' ' + r['grafik']
        for mm in re.findall(r'\$[^$]*\$', r['wortlaut']):
            if '\\div' in mm or re.search(r'[0-9a-z)]\s*:\s*[0-9a-z(]', mm):
                m('S6 TEILEN', f'{r["id"]}: {mm[:40]}')
        for k in re.findall(r'karo=([0-9.]+)', r['grafik']):
            if float(k) < 0.45:
                m('S8 KAESTCHEN', f'{r["id"]}: karo={k}')
        if 'karo' in r['form'].split('+') and int(r['karo'] or 0) < 2:
            m('S9 RECHENRAUM', f'{r["id"]}: {r["karo"] or 0} Zeilen')
        if not r['gruppe'] and re.search(r'(^|\s)a\)', r['wortlaut']):
            m('S11 TEILBUCHST', f'{r["id"]}: „a)“ ohne Gruppe')
    for z in meld + hinweis:
        print(z)
    print(f'satz-pruef {a.kapitel}: {len(meld)} Meldungen, {len(stuecke)} Stücke, {len(zeilen)} Aufgaben')
    sys.exit(1 if meld else 0)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""mappe-pruef.py – Abnahme der Mappe P10 (plan.md § 10, 14.10. f) per Skript.

Prüft je PDF: jede Sprungmarke (Link mit Ziel, benannt oder direkt) trifft eine vorhandene Seite; jedes Lesezeichen
trifft. Mit --fund: jede Fundstelle aus mathe-nachhilfe msa/mehr-p10/*.csv und aus bau/register.csv (Blätter des
Datums) steht im Fundstellenregister. Mit --oeffentlich: das PDF enthält keinen Wortlaut der Originale (Satzvergleich
gegen aufgabenbank-privat, Sätze ab 40 Zeichen ohne Zahlen-Unterschied).
  python3 werkzeuge/mappe-pruef.py <pdf> [--fund --datum 2026-10-14] [--oeffentlich]
"""
import argparse, csv, glob, json, os, re, sys
import pypdf

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELTERN = os.path.dirname(BANK)


def links(pdf):
    r = pypdf.PdfReader(pdf)
    namen = r.named_destinations
    n, kaputt = 0, []
    for i, p in enumerate(r.pages):
        for a in p.get('/Annots') or []:
            a = a.get_object()
            if a.get('/Subtype') != '/Link':
                continue
            ziel = a.get('/Dest')
            act = a.get('/A')
            if ziel is None and act is not None:
                act = act.get_object()
                if act.get('/S') == '/GoTo':
                    ziel = act.get('/D')
                else:
                    continue
            if ziel is None:
                continue
            n += 1
            if isinstance(ziel, (str, pypdf.generic.TextStringObject, pypdf.generic.ByteStringObject)):
                if str(ziel) not in namen:
                    kaputt.append((i + 1, str(ziel)))
            else:
                try:
                    r.get_destination_page_number(pypdf.generic.Destination('x', ziel[0], ziel[1]))
                except Exception:
                    kaputt.append((i + 1, repr(ziel)[:40]))
    lz = 0
    def lauf(o):
        nonlocal lz
        for x in o:
            if isinstance(x, list):
                lauf(x)
            else:
                lz += 1
                if r.get_destination_page_number(x) is None:
                    kaputt.append(('Lesezeichen', x.title))
    lauf(r.outline)
    return n, lz, kaputt, len(r.pages)


def fund(pdf, mn, datum):
    r = pypdf.PdfReader(pdf)
    text = ''
    for p in r.pages[-40:]:
        text += p.extract_text() + '\n'
    text = re.sub(r'\s+', '', text).replace("'", '’')
    ids = set()
    for f in glob.glob(os.path.join(mn, 'msa', 'mehr-p10', '*.csv')):
        for z in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            ids.add(z['eltern_id'].strip())
    for z in open(os.path.join(BANK, 'bau', 'register.csv'), encoding='utf-8').read().splitlines()[1:]:
        if f';{datum};' in z and 'art=p' in z:
            m = re.search(r'ids=([^,]*)', z)
            ids |= {re.sub(r'-m\d+$', '', i) for i in (m.group(1).split() if m else [])}
    fehlt = []
    # Register: unter der Jahreszeile „P10 ’25“ die Einträge „P10 ’25 · 4a“
    for i in sorted(ids):
        m = re.match(r'^(\d{4})-([A-Z]+)-[BK](\d+)([a-z]?)$', i)
        j, pap, n, t = m.groups()
        marke = f'P10’{j[2:]}' + ('' if pap == 'OS' else pap) + f'·{n}{t}'
        eintrag = re.search(re.escape(marke) + r'Blattoder ?Mehr\d', text)
        if not eintrag:
            fehlt.append(i)
    return len(ids), fehlt


def oeffentlich(pdf, privat):
    saetze = set()
    for n in ('basis-originale.jsonl', 'hauptteil-originale.jsonl'):
        for l in open(os.path.join(privat, n), encoding='utf-8'):
            z = json.loads(l)
            for feld in ('stamm', 'aufgabe'):
                s = re.sub(r'\\[a-zA-Z]+|[{}$~\\]', ' ', z.get(feld) or '')
                for satz in re.split(r'(?<=[.?!:])\s+', s):
                    satz = re.sub(r'\s+', ' ', satz).strip()
                    if len(satz) >= 40 and re.search(r'\d', satz):
                        saetze.add(re.sub(r'\s+', '', satz).lower())
    text = re.sub(r'\s+', '', ' '.join(p.extract_text() for p in pypdf.PdfReader(pdf).pages)).lower()
    return [s for s in saetze if s in text]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--fund', action='store_true')
    ap.add_argument('--oeffentlich', action='store_true')
    ap.add_argument('--datum', default='2026-10-14')
    ap.add_argument('--mn', default=os.path.join(ELTERN, 'mathe-nachhilfe'))
    ap.add_argument('--privat', default=os.path.join(ELTERN, 'aufgabenbank-privat'))
    a = ap.parse_args()
    n, lz, kaputt, s = links(a.pdf)
    print(f'{os.path.basename(a.pdf)}: {s} Seiten, {n} Sprungmarken, {lz} Lesezeichen, ohne Ziel {len(kaputt)}')
    for k in kaputt[:10]:
        print('  ohne Ziel:', k)
    rc = bool(kaputt)
    if a.fund:
        m, fehlt = fund(a.pdf, a.mn, a.datum)
        print(f'Fundstellen: {m} Originale aus mehr-p10 und Register, fehlen im Register {len(fehlt)}'
              + (': ' + ' '.join(fehlt[:20]) if fehlt else ''))
        rc |= bool(fehlt)
    if a.oeffentlich:
        t = oeffentlich(a.pdf, a.privat)
        print(f'Originalwortlaut (Sätze mit Zahl, ab 40 Zeichen): {len(t)} Treffer')
        rc |= bool(t)
    sys.exit(1 if rc else 0)


if __name__ == '__main__':
    main()

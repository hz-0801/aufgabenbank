#!/usr/bin/env python3
"""mappe-pruef.py – Abnahme der Mappe P10 (plan.md § 10, 14.10. f) per Skript.

Prüft je PDF: jede Sprungmarke (Link mit Ziel, benannt oder direkt) trifft eine vorhandene Seite; jedes Lesezeichen
trifft; jede Kennung aus mathe-nachhilfe msa/gliederung/*.md steht im Inhalt mit Sprungmarke auf die Seite, die
sie trägt; mit --seiten N die Seitenzahl. Mit --fund: jede Fundstelle aus mathe-nachhilfe msa/mehr-p10/*.csv und aus bau/register.csv (Blätter des
Datums) steht im Fundstellenregister. Mit --oeffentlich: das PDF enthält keinen Wortlaut der Originale (Satzvergleich
gegen aufgabenbank-privat, Sätze ab 40 Zeichen ohne Zahlen-Unterschied).
  python3 werkzeuge/mappe-pruef.py <pdf> [--seiten 372] [--fund --datum 2026-10-14] [--oeffentlich]
--pruefung abitur (15.10.2026, Mappe Abitur GK aus mappe-abi.py): Kennungen aus abitur/gliederung/*.md, Fundstellen
(„GK ’24 · B2.1a“) aus abitur/mehr-abi-gk/*.csv, Wortlaut gegen aufgabenbank-privat abitur/wortlaut-*.csv.
  python3 werkzeuge/mappe-pruef.py <pdf> --pruefung abitur --fund [--oeffentlich]
"""
import argparse, csv, glob, json, os, re, sys
import pypdf

BANK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELTERN = os.path.dirname(BANK)


def links(pdf):
    r = pypdf.PdfReader(pdf)
    namen = r.named_destinations
    seiten = {p.indirect_reference.idnum for p in r.pages}
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
                # direktes Ziel [Seite, /XYZ, …]: die Seite muss eine Seite dieses PDFs sein (15.10.: vorher baute
                # Destination('x', Seite, /XYZ) ohne die Koordinaten und warf bei jedem Ziel – 1812 Fehlmeldungen)
                seite = ziel[0] if len(ziel) else None
                if not isinstance(seite, pypdf.generic.IndirectObject) or seite.idnum not in seiten:
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


def kennungen_soll(mn, pruefung='p10'):
    """Kennungen der Einheiten aus msa/gliederung/*.md (Zeile „Kennung: <Zuschnitt> = PG50“), Abitur aus
    abitur/gliederung/*.md („Kennung: Nullstellen = AA20“)."""
    soll = set()
    ordner, muster = ('abitur', r'A[A-Z]\d{2,3}') if pruefung == 'abitur' else ('msa', r'P[A-Z]\d{2,3}')
    for f in glob.glob(os.path.join(mn, ordner, 'gliederung', '*.md')):
        for z in open(f, encoding='utf-8'):
            m = re.match(r'^Kennung:\s.*=\s*(' + muster + r')\s*$', z.strip())
            if m:
                soll.add(m.group(1))
    return soll


def kennungen(pdf, soll, vorn=12):
    """Jede Kennung aus der Gliederung steht im Inhalt (erste Seiten) in einer Zeile mit Sprungmarke, und das Ziel
    ist die Seite, deren Text die Kennung trägt. Rückgabe {Kennung: Befund} der Fehler."""
    r = pypdf.PdfReader(pdf)
    idx = {p.indirect_reference.idnum: i for i, p in enumerate(r.pages)}
    text = {}
    def seitentext(i):
        if i not in text:
            text[i] = re.sub(r'\s+', '', r.pages[i].extract_text() or '')
        return text[i]
    gefunden = {}
    for i, p in enumerate(r.pages[:vorn]):
        zeilen = {}
        p.extract_text(visitor_text=lambda t, cm, tm, fd, fs: zeilen.__setitem__(
            round(tm[5], 1), zeilen.get(round(tm[5], 1), '') + t))
        marken = []
        for a in p.get('/Annots') or []:
            a = a.get_object()
            ziel = a.get('/Dest')
            if a.get('/Subtype') == '/Link' and isinstance(ziel, list) and ziel:
                marken.append((float(a['/Rect'][1]), float(a['/Rect'][3]), idx.get(getattr(ziel[0], 'idnum', None))))
        for y, z in zeilen.items():
            for k in re.findall(r'[PA][A-Z]\d{2,3}', re.sub(r'\s+', '', z)):
                if k not in soll or gefunden.get(k) is True:
                    continue
                ziele = [t for (u, o, t) in marken if u - 2 <= y <= o + 2 and t is not None]
                if not ziele:
                    gefunden[k] = f'Inhalt S. {i + 1}: ohne Sprungmarke'
                elif any(k in seitentext(t) for t in ziele):
                    gefunden[k] = True
                else:
                    gefunden[k] = f'Inhalt S. {i + 1}: Ziel S. {ziele[0] + 1} trägt die Kennung nicht'
    return {k: gefunden.get(k, 'nicht im Inhalt') for k in sorted(soll) if gefunden.get(k) is not True}


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
        eintrag = re.search(re.escape(marke) + r'(?:Blatt|Mehr)\d', text)   # 15.10.: vorher wörtlich „Blattoder Mehr“
        if not eintrag:
            fehlt.append(i)
    return len(ids), fehlt


ABI_GK = re.compile(r'^(\d{4})-(?:bebb|bb|be)-gk(?:-cas)?-([AB]\d+(?:\.\d+)?[a-z]?)$')


def fund_abi(pdf, mn):
    """Abitur: jede Fundstelle der GK-Hefte aus abitur/mehr-abi-gk/*.csv steht im Register als „GK ’24 · B2.1a“
    mit Blatt- oder Mehr-Seite."""
    text = re.sub(r'\s+', '', '\n'.join(p.extract_text() for p in pypdf.PdfReader(pdf).pages[-12:])).replace("'", '’')
    ids = set()
    for f in glob.glob(os.path.join(mn, 'abitur', 'mehr-abi-gk', '*.csv')):
        for z in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            if ABI_GK.match((z.get('eltern_id') or '').strip()):
                ids.add(z['eltern_id'].strip())
    fehlt = []
    for i in sorted(ids):
        j, st = ABI_GK.match(i).groups()
        if not re.search(re.escape(f'GK’{j[2:]}·{st}') + r'(?:Blatt|Mehr)\d', text):
            fehlt.append(i)
    return len(ids), fehlt


def oeffentlich(pdf, privat, pruefung='p10'):
    saetze = set()
    if pruefung == 'abitur':
        # Wortlaut der Abitur-Originale liegt nur privat (abitur/wortlaut-*.csv, Spalte wortlaut)
        for f in glob.glob(os.path.join(privat, 'abitur', 'wortlaut-*.csv')):
            for z in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
                s = re.sub(r'\\[a-zA-Z]+|[{}$~\\]', ' ', z.get('wortlaut') or '')
                for satz in re.split(r'(?<=[.?!:])\s+', s):
                    satz = re.sub(r'\s+', ' ', satz).strip()
                    if len(satz) >= 40 and re.search(r'\d', satz):
                        saetze.add(re.sub(r'\s+', '', satz).lower())
    for n in (() if pruefung == 'abitur' else ('basis-originale.jsonl', 'hauptteil-originale.jsonl')):
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
    ap.add_argument('--pruefung', choices=['p10', 'abitur'], default='p10', help='Mappe P10 (Vorgabe) oder Abitur GK')
    ap.add_argument('--seiten', type=int, default=0, help='erwartete Seitenzahl (0: nicht prüfen)')
    ap.add_argument('--mn', default=os.path.join(ELTERN, 'mathe-nachhilfe'))
    ap.add_argument('--privat', default=os.path.join(ELTERN, 'aufgabenbank-privat'))
    a = ap.parse_args()
    n, lz, kaputt, s = links(a.pdf)
    print(f'{os.path.basename(a.pdf)}: {s} Seiten, {n} Sprungmarken, {lz} Lesezeichen, ohne Ziel {len(kaputt)}')
    for k in kaputt[:10]:
        print('  ohne Ziel:', k)
    rc = bool(kaputt)
    if a.seiten and s != a.seiten:
        print(f'Seitenzahl {s}, erwartet {a.seiten}')
        rc = True
    soll = kennungen_soll(a.mn, a.pruefung)
    fk = kennungen(a.pdf, soll)
    print(f'Kennungen aus {"abitur" if a.pruefung == "abitur" else "msa"}/gliederung: {len(soll)}, ohne Ziel im Inhalt {len(fk)}')
    for k, b in fk.items():
        print(f'  {k}: {b}')
    rc |= bool(fk)
    if a.fund:
        m, fehlt = fund_abi(a.pdf, a.mn) if a.pruefung == 'abitur' else fund(a.pdf, a.mn, a.datum)
        print(f'Fundstellen: {m} Originale aus {"mehr-abi-gk" if a.pruefung == "abitur" else "mehr-p10 und Register"}, fehlen im Register {len(fehlt)}'
              + (': ' + ' '.join(fehlt[:20]) if fehlt else ''))
        rc |= bool(fehlt)
    if a.oeffentlich:
        t = oeffentlich(a.pdf, a.privat, a.pruefung)
        print(f'Originalwortlaut (Sätze mit Zahl, ab 40 Zeichen): {len(t)} Treffer')
        rc |= bool(t)
    sys.exit(1 if rc else 0)


if __name__ == '__main__':
    main()

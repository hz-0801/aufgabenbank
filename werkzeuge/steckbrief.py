"""steckbrief.py – liest die Steckbriefe aus mathe-nachhilfe/katalog/steckbrief/*.md (Format:
katalog/steckbrief/README.md). Ohne Modell, ohne Abhängigkeiten.

    import steckbrief
    sb = steckbrief.finde(mn, 'prozent', fokus='grundwert')            # oder None
    sb = steckbrief.lies('…/katalog/steckbrief/pythagoras-seite.md')

Ein Steckbrief ist ein dict:
    datei, name (Dateiname ohne .md), titel, kapitel, stufen [..], bank [..],
    teil1 {Schlüssel: Wert}, teil2 {Schlüssel: Wert}, luecke (Text aus **Lücke:** in Teil 2),
    kurz [(Satz, Herkunft)], lang [(Satz, Herkunft)], befunde [Text]
Werte mit Unterpunkten (Typische Fehler) sind Listen. Schlüssel ohne Klammerzusatz („Leiter (Katalog
Einheit 4)“ -> „Leiter“, „Vorher können (Rückblick)“ -> „Vorher können“).

Hilfen zum Setzen: schuelertext() streicht Belege [..] und Vermerke „Vorschlag …, zur Bestätigung“;
zitate() liefert die Sätze in „…“ (Schülerwortlaut); ids() die Bank-ids eines Werts.
"""
import glob
import os
import re

TEILE = {'1': 'teil1', '2': 'teil2', '3': 'teil3', '4': 'teil4'}


def _schluessel(k):
    return re.sub(r'\s*\(.*\)\s*$', '', k.strip()).strip()


def lies(pfad):
    txt = open(pfad, encoding='utf-8').read()
    sb = {'datei': pfad, 'name': os.path.splitext(os.path.basename(pfad))[0], 'titel': '', 'kapitel': '',
          'stufen': [], 'bank': [], 'teil1': {}, 'teil2': {}, 'luecke': '', 'kurz': [], 'lang': [],
          'befunde': []}
    teil, key, liste3 = None, None, None
    for zeile in txt.splitlines():
        if zeile.startswith('# ') and not sb['titel']:
            sb['titel'] = zeile[2:].strip()
            continue
        m = re.match(r'##\s+(\d)\b', zeile)
        if m:
            teil, key, liste3 = TEILE.get(m.group(1)), None, None
            continue
        if teil is None:
            m = re.match(r'(Kapitel|Stufen|Bank):\s*(.*)$', zeile)
            if m:
                w = m.group(2).strip()
                if m.group(1) == 'Kapitel':
                    sb['kapitel'] = w
                else:
                    sb[m.group(1).lower()] = [x.strip() for x in w.split('|') if x.strip()]
            continue
        if teil in ('teil1', 'teil2'):
            m = re.match(r'- \*\*(.+?):\*\*\s*(.*)$', zeile)
            if m:
                key = _schluessel(m.group(1))
                sb[teil][key] = m.group(2).strip()
                continue
            m = re.match(r'\s{2,}- (.*)$', zeile)
            if m and key:
                v = sb[teil][key]
                if isinstance(v, str):
                    v = [v] if v else []
                v.append(m.group(1).strip())
                sb[teil][key] = v
                continue
            m = re.match(r'\s{2,}(\S.*)$', zeile)
            if m and key:
                v = sb[teil][key]
                if isinstance(v, list):
                    v[-1] += ' ' + m.group(1).strip()
                else:
                    sb[teil][key] = (v + ' ' + m.group(1).strip()).strip()
                continue
            if not zeile.strip():
                continue
            key = None
        elif teil == 'teil3':
            m = re.match(r'(kurz|lang):\s*$', zeile.strip())
            if m:
                liste3 = m.group(1)
                continue
            m = re.match(r'- (.*)$', zeile)
            if m and liste3:
                sb[liste3].append(m.group(1).strip())
                continue
            m = re.match(r'\s{2,}(\S.*)$', zeile)
            if m and liste3 and sb[liste3]:
                sb[liste3][-1] += ' ' + m.group(1).strip()
        elif teil == 'teil4':
            m = re.match(r'- (.*)$', zeile)
            if m:
                sb['befunde'].append(m.group(1).strip())
            elif zeile.startswith('  ') and sb['befunde']:
                sb['befunde'][-1] += ' ' + zeile.strip()
    for k in ('kurz', 'lang'):
        out = []
        for s in sb[k]:
            m = re.match(r'(.*?)\s*\(([^()]*)\)\s*$', s)
            out.append((m.group(1), m.group(2)) if m else (s, ''))
        sb[k] = out
    for v in sb['teil2'].values():
        if isinstance(v, str):
            m = re.search(r'\*\*Lücke:\*\*\s*(.*)$', v)
            if m:
                sb['luecke'] = m.group(1).strip()
    for k, v in list(sb['teil2'].items()):
        if isinstance(v, str):
            sb['teil2'][k] = re.sub(r'\s*\*\*Lücke:\*\*.*$', '', v)
    return sb


def alle(mn):
    return [lies(p) for p in sorted(glob.glob(os.path.join(mn, 'katalog', 'steckbrief', '*.md')))
            if not os.path.basename(p).lower().startswith('readme')]


def _kap(a, b):
    a, b = (a or '').lower(), (b or '').lower()
    return bool(a) and (a == b or a.startswith(b) or b.startswith(a))


def finde(mn, kapitel, fokus=None, stufen=None):
    """Steckbrief zum Kapitel: über den Fokus (Dateiname gleich oder endet auf „-<fokus>“) oder über die
    Stufen (alle Stufen des Blatts stehen im Steckbrief). Keiner: None."""
    sbs = [s for s in alle(mn) if _kap(s['kapitel'], kapitel)]
    if fokus:
        f = fokus.lower()
        for s in sbs:
            n = s['name'].lower()
            if n == f or n.endswith('-' + f) or n.startswith(f + '-'):
                return s
    if stufen:
        for s in sbs:
            if set(stufen) <= set(s['stufen']):
                return s
    return None


def schuelertext(s):
    """Belege [..] und Vermerke „(Vorschlag …)“ / „; Vorschlag …“ weg, Leerraum glätten."""
    s = s or ''
    s = re.sub(r'\s*\[[^\]]*\]', '', s)
    s = re.sub(r';\s*Vorschlag[^)]*', '', s)
    s = re.sub(r'\s*\((?:[^()]*\b(?:Vorschlag|Original\w*|Lauf|Lehrer)\b[^()]*)\)', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def zitate(s):
    return [z.strip() for z in re.findall(r'„([^“]+)“', s or '')]


def ids(s):
    return re.findall(r'[a-z-]+-e\d+-k\d+-s\d+(?:-v\d+)?', s or '')


def wert(sb, teil, key):
    v = sb[teil].get(key, '')
    return v

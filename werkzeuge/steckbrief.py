"""steckbrief.py – liest die Steckbriefe (Fokus-Blöcke „## Fokus <name>“) aus der Prüfungsgliederung
mathe-nachhilfe/msa/gliederung/<kapitel>.md bzw. abitur/gliederung/<kapitel>.md (Format:
msa/gliederung/README.md; bis 08.10.2026 eigene Dateien katalog/steckbrief/*.md, jetzt archiv/).
Ohne Modell, ohne Abhängigkeiten.

    import steckbrief
    sb = steckbrief.finde(mn, 'prozent', fokus='grundwert')            # oder None
    sb = steckbrief.lies('…/archiv/steckbrief-pythagoras-seite-2026-10-08.md')   # alte Einzeldatei
    sb = steckbrief.lies_gliederung(mn, '…/msa/gliederung/prozent.md', 'grundwert')

Verweise (W2: Merkkasten, Formel, Fehler stehen nur im Katalog): ein Wert „→ katalog/<eintrag>.md,
Typische Fehler: Anfang | Anfang …“ wird beim Lesen durch die Sätze der Katalogliste ersetzt, die mit
den genannten Wörtern beginnen (Reihenfolge der Nennung; fehlt ein Satz: Hinweis in sb['befunde']).
Andere Verweise („→ katalog/…“ ohne Auswahl) bleiben Text.

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
from collections import OrderedDict

TEILE = {'1': 'teil1', '2': 'teil2', '3': 'teil3', '4': 'teil4'}


def _schluessel(k):
    return re.sub(r'\s*\(.*\)\s*$', '', k.strip()).strip()


def lies(pfad, mn=None):
    """Steckbrief als eigene Datei (altes Format)."""
    return lies_text(open(pfad, encoding='utf-8').read(), pfad, os.path.splitext(os.path.basename(pfad))[0], mn)


def fokus_bloecke(pfad):
    """[(name, Text)] der Blöcke „## Fokus <name>“ einer Gliederungsdatei; Überschriften eine Ebene hoch
    (### 1 Verständnis -> ## 1 Verständnis, #### Art -> ### Art), so dass der Block ein Steckbrief ist."""
    txt = open(pfad, encoding='utf-8').read()
    out = []
    for b in re.split(r'^(?=## )', txt, flags=re.M)[1:]:
        kopf = b.splitlines()[0]
        if not kopf.startswith('## Fokus '):
            continue
        zl = []
        for z in b.splitlines()[1:]:
            if z.startswith('### ') or z.startswith('#### '):
                z = z[1:]
            zl.append(z)
        out.append((kopf[9:].strip(), '\n'.join(zl) + '\n'))
    return out


def lies_gliederung(mn, pfad, name):
    """Fokus-Block <name> der Gliederungsdatei pfad als Steckbrief; None, wenn es ihn nicht gibt."""
    for n, txt in fokus_bloecke(pfad):
        if n == name:
            kap = os.path.splitext(os.path.basename(pfad))[0]
            sb = lies_text(txt, f'{pfad}#{n}', f'{kap}-{n}', mn)
            sb['fokus'] = n
            return sb
    return None


def lies_text(txt, pfad, name, mn=None):
    sb = {'datei': pfad, 'name': name, 'titel': '', 'kapitel': '',
          'stufen': [], 'bank': [], 'teil1': {}, 'teil2': {}, 'luecke': '', 'kurz': [], 'lang': [],
          'befunde': []}
    teil, key, liste3 = None, None, None
    for zeile in txt.splitlines():
        if zeile.startswith('# ') and not sb['titel']:
            sb['titel'] = zeile[2:].strip()
            continue
        if zeile.startswith('Titel:') and not sb['titel'] and teil is None:
            sb['titel'] = zeile[6:].strip()
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
    sb['arten_kopf'], sb['arten'] = lies_arten(txt)
    for k, v in list(sb['teil1'].items()):
        if isinstance(v, str) and v.startswith('→'):
            sb['teil1'][k] = verweis(mn, v, sb)
    return sb


def verweis(mn, wert, sb=None):
    """„→ katalog/<datei>.md, <Abschnitt>: A | B“ -> Sätze des Abschnitts (### <Abschnitt>, Zeilen „- …“), die mit
    A, B … beginnen (ohne Groß/Klein), in dieser Folge; ohne Auswahl oder ohne Katalog bleibt der Text."""
    m = re.match(r'→\s*(katalog/[\w.-]+\.md)\s*,\s*([^:]+?)\s*:\s*(.+)$', wert)
    if not m or not mn:
        return wert
    pfad = os.path.join(mn, m.group(1))
    if not os.path.exists(pfad):
        if sb is not None:
            sb['befunde'].append(f'Verweis: {m.group(1)} fehlt')
        return wert
    txt = open(pfad, encoding='utf-8').read()
    mm = re.search(r'^###\s+' + re.escape(m.group(2)) + r'\s*$(.*?)(?=^###? |\Z)', txt, re.M | re.S)
    saetze = re.findall(r'^- (.*)$', mm.group(1), re.M) if mm else []
    out = []
    for anfang in [x.strip() for x in m.group(3).split('|') if x.strip()]:
        treffer = [z for z in saetze if z.lower().startswith(anfang.lower())]
        if treffer:
            out.append(treffer[0])
        else:
            out.append(anfang)
            if sb is not None:
                sb['befunde'].append(f'Verweis: kein Satz „{anfang} …“ in {m.group(1)}, {m.group(2)}')
    return out


def _felder(zeilen):
    """„- **Schlüssel:** Wert“ mit Fortsetzung und Unterpunkten -> {Schlüssel: Wert | [Unterpunkte]}."""
    f, key = OrderedDict(), None
    for z in zeilen:
        m = re.match(r'- \*\*(.+?):\*\*\s*(.*)$', z)
        if m:
            key = _schluessel(m.group(1))
            f[key] = m.group(2).strip()
            continue
        m = re.match(r'\s{2,}- (.*)$', z)
        if m and key:
            v = f[key]
            if isinstance(v, str):
                v = [] if not v or v.startswith('(') else [v]
            v.append(m.group(1).strip())
            f[key] = v
            continue
        m = re.match(r'\s{2,}(\S.*)$', z)
        if m and key:
            if isinstance(f[key], list) and f[key]:
                f[key][-1] += ' ' + m.group(1).strip()
            elif isinstance(f[key], str):
                f[key] = (f[key] + ' ' + m.group(1).strip()).strip()
            continue
        if z.strip():
            key = None
    return f


def lies_arten(txt):
    """Teil 5 „Arten“ (Beschlüsse 07.10., Format in README.md): (Kopf, [Art]); Kopf und Art sind dicts der
    Felder; je Art dazu „name“ (Überschrift ###), „aufgaben“ (P10-ids), „gruppen“ [(Name, [ids])],
    „nur_gekuerzt“ {id: Grund}. Ohne Teil 5: ({}, [])."""
    m = re.search(r'^## 5 Arten\s*$', txt, re.M)
    if not m:
        return {}, []
    rest = txt[m.end():]
    rest = re.split(r'^## \d', rest, flags=re.M)[0]
    bloecke = re.split(r'^### ', rest, flags=re.M)
    kopf = _felder(bloecke[0].splitlines())
    arten = []
    for b in bloecke[1:]:
        zl = b.splitlines()
        a = _felder(zl[1:])
        a['name'] = zl[0].strip()
        idre = r'\d{4}-[A-Z]+-[A-Z]\d+[a-z]'
        a['aufgaben'] = re.findall(idre, a.get('Aufgaben', ''))
        a['gruppen'] = []
        for g in [x for x in (a.get('Gruppen') or '').split(' | ') if x.strip()]:
            n, _, ids = g.partition(':')
            # P10-ids und Kennungen fremder Aufgaben (F1: das Programm filtert sie über handgriffe)
            a['gruppen'].append((n.strip(), [i for i in ids.split() if re.search(r'\d', i)]))
        a['nur_gekuerzt'] = OrderedDict()
        for t in re.split(r'\s*·\s*', a.get('Nur gekürzt', '')):
            mm = re.match(r'(' + idre + r')\s*(?:\((.*)\))?', t.strip())
            if mm:
                a['nur_gekuerzt'][mm.group(1)] = mm.group(2) or ''
        arten.append(a)
    return kopf, arten


def alle(mn):
    """Alle Fokus-Blöcke der Prüfungsgliederung (msa/gliederung, abitur/gliederung)."""
    out = []
    for ordner in ('msa', 'abitur'):
        for p in sorted(glob.glob(os.path.join(mn, ordner, 'gliederung', '*.md'))):
            if os.path.basename(p).lower() == 'readme.md':
                continue
            for n, _ in fokus_bloecke(p):
                out.append(lies_gliederung(mn, p, n))
    return out


def _kap(a, b):
    a, b = (a or '').lower(), (b or '').lower()
    return bool(a) and (a == b or a.startswith(b) or b.startswith(a))


def finde(mn, kapitel, fokus=None, stufen=None):
    """Steckbrief zum Kapitel: über den Fokus (Blockname „## Fokus <name>“ gleich, beginnt mit „<fokus>-“ oder
    endet auf „-<fokus>“) oder über die
    Stufen (alle Stufen des Blatts stehen im Steckbrief). Keiner: None."""
    sbs = [s for s in alle(mn) if _kap(s['kapitel'], kapitel)]
    if fokus:
        f = fokus.lower()
        for s in sbs:
            n = (s.get('fokus') or s['name']).lower()
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

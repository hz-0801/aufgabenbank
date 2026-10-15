#!/usr/bin/env python3
"""sprungziele.py – feste Seitenziele für Mappe und Gesamtheft (plan.md § 10, 15.10.2026 k).

Warum: einfache Betrachter (Handy, Edge) springen nicht zuverlässig zu benannten Zielen. Nach dem Satz ersetzt
feste_ziele() jedes Linkziel (benannt oder GoTo) durch ein explizites /Dest [Seite /XYZ links oben null], stellt die
Lesezeichen ebenso um und entfernt die benannten Ziele aus dem PDF.

Abschnittsziele: Der Setzer (pruefheft.py --art p) legt je Stufenkopf ein Ziel „stufe-<slug>“ in 2-blatt.pdf.
Ein Link „<teil>@<slug>“ (\\hyperlink in Karte, Handreichung, Inhalt) springt im Gesamtdokument auf die Seite und
Höhe dieses Stufenkopfs im Teil <teil> (dessen erste Seite trägt das benannte Ziel „<teil>.1“ von pdfpages).

  from sprungziele import slug, stufenziele, feste_ziele, pruefe
"""
import re
import unicodedata

ZUGABE = 36   # pt über dem Ziel des Stufenkopfs (das Ziel steht unter der Kopfzeile)


def slug(name):
    s = re.sub(r'\\[a-zA-Z]+\s*', '', name.replace('~', ' ')).replace('\\', '')   # TeX aus der Karte
    s = s.lower().replace('ß', 'ss')
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def _ziel(r, d):
    """(Seitenindex, oben) eines pypdf-Ziels."""
    seite = r.get_destination_page_number(d)
    oben = None
    try:
        oben = float(d.top) if d.top is not None else None
    except Exception:
        oben = None
    return seite, oben


def stufenziele(pdf):
    """slug -> (Seitenindex im Blatt, Höhe) aus den Zielen „stufe-<slug>“ von 2-blatt.pdf."""
    import pypdf
    r = pypdf.PdfReader(pdf)
    out = {}
    for k, v in r.named_destinations.items():
        if k.startswith('stufe-'):
            out.setdefault(k[6:], _ziel(r, v))
    return out


def feste_ziele(pdf, teile_blatt=None):
    """Alle internen Sprünge im PDF auf feste Seitenziele umstellen. teile_blatt: {teil: pfad 2-blatt.pdf} für
    Links „<teil>@<slug>“. Rückgabe (Zahl der Links, Fehlerliste); bei Fehlern wird nichts geschrieben."""
    import pypdf
    from pypdf.generic import ArrayObject, NameObject, NullObject, FloatObject, NumberObject
    r = pypdf.PdfReader(pdf)
    w = pypdf.PdfWriter(clone_from=r)
    benannt = {k: _ziel(r, v) for k, v in r.named_destinations.items()}
    hoehe = [float(p.mediabox.top) for p in w.pages]
    abschnitt = {t: stufenziele(p) for t, p in (teile_blatt or {}).items()}
    fehler, n = [], 0

    def aufloesen(name):
        m = re.match(r'^(.+)@(.+)$', name)
        if m:
            t, s = m.groups()
            if t not in abschnitt or s not in abschnitt[t] or f'{t}.1' not in benannt:
                return None
            sb, y = abschnitt[t][s]
            seite = benannt[f'{t}.1'][0] + sb
            return seite, (min(hoehe[seite], y + ZUGABE) if y is not None else hoehe[seite])
        if name not in benannt:
            return None
        seite, y = benannt[name]
        return seite, (y if y is not None else hoehe[seite])

    def fest(seite, y):
        return ArrayObject([w.pages[seite].indirect_reference, NameObject('/XYZ'), NullObject(),
                            FloatObject(round(y, 2)), NullObject()])

    for i, p in enumerate(w.pages):
        for a in p.get('/Annots') or []:
            a = a.get_object()
            if a.get('/Subtype') != '/Link':
                continue
            d = a.get('/Dest')
            act = a.get('/A')
            if d is None and act is not None:
                act = act.get_object()
                if act.get('/S') != '/GoTo':
                    continue
                d = act.get('/D')
            if d is None:
                continue
            n += 1
            if isinstance(d, ArrayObject):
                continue          # schon fest
            ziel = aufloesen(str(d))
            if ziel is None:
                fehler.append(f'S. {i + 1}: Ziel „{d}“ fehlt')
                continue
            a[NameObject('/Dest')] = fest(*ziel)
            if '/A' in a:
                del a['/A']
    # Lesezeichen
    def gliederung(knoten):
        while knoten is not None:
            k = knoten.get_object()
            d = k.get('/Dest')
            act = k.get('/A')
            if d is None and act is not None and act.get_object().get('/S') == '/GoTo':
                d = act.get_object().get('/D')
            if d is not None and not isinstance(d, ArrayObject):
                ziel = aufloesen(str(d))
                if ziel is None:
                    fehler.append(f'Lesezeichen „{k.get("/Title")}“: Ziel „{d}“ fehlt')
                else:
                    k[NameObject('/Dest')] = fest(*ziel)
                    if '/A' in k:
                        del k[NameObject('/A')]
            if '/First' in k:
                gliederung(k['/First'])
            knoten = k.get('/Next')
    root = w._root_object
    if '/Outlines' in root and '/First' in root['/Outlines'].get_object():
        gliederung(root['/Outlines'].get_object()['/First'])
    if fehler:
        return n, fehler
    if '/Names' in root and '/Dests' in root['/Names'].get_object():
        del root['/Names'].get_object()[NameObject('/Dests')]
    if '/Dests' in root:
        del root[NameObject('/Dests')]
    with open(pdf, 'wb') as f:
        w.write(f)
    return n, []


def pruefe(pdf, erwartet=()):
    """Jeder Link und jedes Lesezeichen hat ein festes Ziel auf einer vorhandenen Seite; keine benannten Ziele;
    erwartet: [(Seite der Quelle 1-basiert oder None, Zielseite 1-basiert, Beschreibung)] – mindestens ein Link der
    Quellseite zeigt auf die Zielseite. Rückgabe (Zahl der Links, Fehlerliste)."""
    import pypdf
    from pypdf.generic import ArrayObject
    r = pypdf.PdfReader(pdf)
    seiten = {p.indirect_reference.idnum: i for i, p in enumerate(r.pages)}
    fehler, n, von = [], 0, {}
    if r.named_destinations:
        fehler.append(f'{len(r.named_destinations)} benannte Ziele übrig')
    for i, p in enumerate(r.pages):
        for a in p.get('/Annots') or []:
            a = a.get_object()
            if a.get('/Subtype') != '/Link' or ('/A' in a and a['/A'].get_object().get('/S') == '/URI'):
                continue
            n += 1
            d = a.get('/Dest')
            if not isinstance(d, ArrayObject) or d[0].idnum not in seiten or str(d[1]) != '/XYZ':
                fehler.append(f'S. {i + 1}: Link ohne festes Ziel ({d})')
                continue
            von.setdefault(i + 1, set()).add(seiten[d[0].idnum] + 1)
    for q, z, was in erwartet:
        if q is None:
            if not any(z in s for s in von.values()):
                fehler.append(f'{was}: kein Link auf S. {z}')
        elif z not in von.get(q, set()):
            fehler.append(f'{was}: S. {q} springt nicht auf S. {z}')
    return n, fehler

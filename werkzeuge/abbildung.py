#!/usr/bin/env python3
"""abbildung.py – Abbildungen aus der Beschreibung im Feld abbildung der Wortlaut-Dateien
(msa/wortlaut-eigen-<kapitel>.csv, abitur/…) als TikZ/pgfplots (Lauf C, 06.10.2026).

pruefheft.py ruft abbildung(desc, D, iid, vorspann_abb); der Textsetzer tx kommt über einrichten().
Typ = Wort am Anfang der Beschreibung (vor „:“ bzw. „(“); „… aus dem Vorspann“ und „… aus <Teil>“
verweisen. Typen mit mindestens zwei Zeilen werden gezeichnet, seltene als grauer
Beschreibungsrahmen; unbekannte meldet das Programm als Datenbefund.

  python3 werkzeuge/abbildung.py --typen [--mn ../mathe-nachhilfe]   Typenliste mit Häufigkeit
"""
import math, os, re, sys

tx = None   # Textsetzer aus pruefheft.py (einrichten)


def einrichten(textsetzer):
    global tx
    tx = textsetzer


# ---------------------------------------------------------------------------
# Abbildungen aus der Beschreibung (Feld abbildung) – Typ am Anfang erkannt
# ---------------------------------------------------------------------------
def zahl(s):
    return float(s.replace(',', '.'))


def abb_saeulen(desc, D, iid):
    kopf, _, rest = desc.partition(':')
    paare = re.findall(r'([A-Za-zÄÖÜäöü0-9]+):?\s+(\d+(?:,\d+)?)', rest)
    if len(paare) < 2:
        D.befund(f'{iid}: Säulendiagramm ohne lesbare Wertepaare')
        return ''
    ymin = 0
    m = re.search(r'Achse beginnt bei (\d+)', kopf)
    if m:
        ymin = int(m.group(1))
    ylabel = re.sub(r'Säulendiagramm|\(.*?\)|[,]', '', kopf).strip() or 'Anzahl'
    werte = [zahl(v) for _, v in paare]
    ymax = max(werte) * 1.2
    if ymin:
        ymax = ymin + (max(werte) - ymin) * 1.25
    coords = ' '.join(f'({k},{zahl(v)})' for k, v in paare)
    cats = ','.join(k for k, _ in paare)
    breite = min(15, 1.3 * len(paare) + 2)
    return (r'\begin{tikzpicture}\begin{axis}[ybar,width=%.1fcm,height=4.6cm,ymin=%s,ymax=%.2f,'
            r'symbolic x coords={%s},xtick=data,enlarge x limits=0.08,bar width=6mm,'
            r'ylabel={%s},ylabel style={font=\small},tick label style={font=\small},'
            r'nodes near coords,every node near coord/.append style={font=\scriptsize,'
            r'/pgf/number format/.cd,use comma,1000 sep={}},'
            r'ymajorgrids,grid style={mbgitter}]'
            r'\addplot[fill=mbkasten,draw=black] coordinates {%s};\end{axis}\end{tikzpicture}'
            % (breite, ymin, ymax, cats, tx(ylabel), coords))


def abb_tabelle_spalten(desc, D, iid):
    # „Tabelle (Spalten 11. bis 15. Geburtstag): Zinsen –, 4,00 €, …; Einzahlung je 200,00 €; …“
    m = re.match(r'Tabelle \(Spalten (\d+)\. bis (\d+)\. (\w+)\):\s*(.*)', desc)
    if not m:
        return None
    a, b, wort, rest = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    n = b - a + 1
    kopf = ' & '.join([wort] + [f'{k}.' for k in range(a, b + 1)])
    zeilen = []
    for teil in rest.split(';'):
        teil = teil.strip()
        mm = re.match(r'([A-Za-zÄÖÜäöüß ]+?)\s+(je\s+)?(.*)', teil)
        if not mm:
            continue
        name, je, werte = mm.group(1), mm.group(2), mm.group(3)
        if je:
            vals = [werte] * n
        else:
            vals = [v.strip() for v in werte.split(', ')]
        if len(vals) != n:
            D.befund(f'{iid}: Tabellenzeile „{name}“ mit {len(vals)} statt {n} Werten')
            return ''
        vals = [r'\leerzelle' if v == 'leer' else tx(v) for v in vals]
        zeilen.append(' & '.join([name] + vals))
    return r'\sachtabelle{l%s}{%s}{%s}' % ('r' * n, kopf, r'\\ '.join(zeilen))


def abb_dreieck(desc):
    w = re.search(r'waagerechte Kathete (\d+(?:,\d+)?) ?(\w+)', desc)
    s = re.search(r'senkrechte Kathete[^\d]*(\d+(?:,\d+)?) ?(\w+)', desc)
    h = re.search(r'Hypotenuse (\w+)', desc)
    a = re.search(r'Anstiegswinkel (\S+)', desc)
    lw = f'{w.group(1)} {w.group(2)}' if w else ''
    ls = f'{s.group(1)} {s.group(2)}' if s else ''
    lh = h.group(1) if h else ''
    la = a.group(1) if a else ''
    # nicht maßstabsgerecht: Höhe überzeichnet, damit die Stufe sichtbar bleibt
    return (r'\begin{tikzpicture}[line width=0.6pt]\draw (0,0) -- (6,0) -- (6,1.4) -- cycle;'
            r'\draw (5.7,0) -- (5.7,0.3) -- (6,0.3);'
            r'\node[below,font=\small] at (3,0) {%s};\node[right,font=\small] at (6,0.7) {%s};'
            r'\node[above left,font=\small] at (3,0.7) {%s};\node[font=\small] at (1.1,0.12) {%s};'
            r'\node[font=\scriptsize,mbgrau,anchor=west] at (0,-0.75) {nicht maßstabsgerecht};'
            r'\end{tikzpicture}' % (tx(lw), tx(ls), tx('$' + lh + '$' if lh else ''),
                                    tx(la)))


def abb_tabelle_zeilen(desc):
    # „Tabelle: Kopf | Kopf; Zeile | Wert; …“ (Reparatur 06.10., Punkt 10)
    teile = [t.strip() for t in desc.split(':', 1)[1].split(';') if t.strip()]
    zeilen = [[tx(z.strip()) for z in t.split(' | ')] for t in teile]
    n = max(len(z) for z in zeilen)
    zeilen = [z + [''] * (n - len(z)) for z in zeilen]
    return r'\sachtabelle{l%s}{%s}{%s}' % ('r' * (n - 1), ' & '.join(zeilen[0]),
                                          r'\\ '.join(' & '.join(z) for z in zeilen[1:]))


def abb_saeulenraster(desc):
    # „Säulenraster (14 Kästchen hoch): y-Achse …; x-Achse …; Spanisch 7,8; ___ 10,5; Arabisch –“
    h = int(re.search(r'\((\d+) Kästchen hoch\)', desc).group(1))
    teile = [t.strip() for t in desc.split(':', 1)[1].split(';')]
    ylab = re.sub(r'^y-Achse\s*|\s*ohne Einteilung', '', teile[0])
    xlab = re.sub(r'^x-Achse\s*', '', teile[1])
    saeulen = [re.match(r'(.*\S)\s+(\S+)$', t).groups() for t in teile[2:]]
    b = 5 * len(saeulen) + 1
    out = [r'\begin{tikzpicture}[x=0.45cm,y=0.45cm]',
           r'\draw[mbgitter,line width=0.3pt] (0,0) grid (%d,%d);' % (b, h),
           r'\draw[line width=0.7pt,->] (0,0) -- (0,%.1f) node[above,font=\small] {%s};' % (h + 0.6, tx(ylab)),
           r'\draw[line width=0.7pt,->] (0,0) -- (%.1f,0) node[right,font=\small] {%s};' % (b + 0.6, tx(xlab))]
    for i, (name, wert) in enumerate(saeulen):
        x = 2 + 5 * i
        if wert not in ('–', '-'):
            out.append(r'\fill[mbkasten,draw=black] (%d,0) rectangle (%d,%s);' % (x, x + 2, wert.replace(',', '.')))
        lab = r'\leerzelle' if name.startswith('_') else tx(name)
        out.append(r'\node[below=2pt,font=\small] at (%d,0) {%s};' % (x + 1, lab))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def _pgf(term):
    """Term der Wortlaut-CSV (Python-Schreibweise) -> pgfplots-Ausdruck."""
    t = term.replace('**', '^').replace('e', 'EULER').replace('EULERxp', 'exp').replace('dEULERg', 'deg')
    t = re.sub(r'(?<![a-z])EULER(?![a-z])', '2.718281828', t)
    return t


def _ist_term(t):
    return re.search(r'\bx\b|exp|sin', t) is not None


def abb_graph_term(d, D, iid):
    """Abbildungstyp „Graph: <Name>: <Term> [für a..b] [gestrichelt]; …; x a..b; y c..d; Gitter ja|nein
    [; Linie (x|y)-(x|y)…] [; Bogen (x|y) r w1..w2] [; Kreis (x|y) r] [; Achsen t | h(t)] [; Marken pi]“
    (Lauf B3): gezeichnet mit pgfplots aus dem Term."""
    teile = [t.strip() for t in d.split(':', 1)[1].split(';')]
    kurven, opt = [], {}
    for t in teile:
        m = re.match(r'^x (-?[\d.]+)\.\.(-?[\d.]+)$', t) or re.match(r'^y (-?[\d.]+)\.\.(-?[\d.]+)$', t)
        if m:
            opt[t[0]] = (float(m.group(1)), float(m.group(2)))
            continue
        if t.startswith('Gitter'):
            opt['gitter'] = t.endswith('ja'); continue
        if t.startswith(('Linie', 'Bogen', 'Kreis', 'Achsen', 'Marken')):
            opt.setdefault('extra', []).append(t); continue
        m = re.match(r'^(?:(.+?):\s*)?(.+?)(?:\s+für (-?[\d.]+)\.\.(-?[\d.]+))?(\s+gestrichelt)?$', t)
        if m and _ist_term(m.group(2)):
            name = m.group(1) or (kurven[-1][0] if kurven else '')
            kurven.append((name if m.group(1) else '', m.group(2), m.group(3), m.group(4), bool(m.group(5))))
    if not kurven or 'x' not in opt or 'y' not in opt:
        return None
    (x0, x1), (y0, y1) = opt['x'], opt['y']
    xl, yl = 'x', 'y'
    for e in opt.get('extra', []):
        if e.startswith('Achsen'):
            xl, yl = [z.strip() for z in e[6:].split('|')]
    ax = [f'xmin={x0},xmax={x1},ymin={y0},ymax={y1}', 'axis lines=middle', 'width=11cm', 'height=7cm',
          f'xlabel={{${xl}$}}', f'ylabel={{${yl}$}}', 'tick label style={font=\\scriptsize}',
          'samples=160', 'clip=true', 'every axis plot/.append style={line width=0.9pt}',
          '/pgf/number format/use comma']
    if opt.get('gitter'):
        ax += ['grid=both', 'grid style={mbgitter}', 'minor tick num=1']
    if any(e.startswith(('Kreis', 'Bogen')) for e in opt.get('extra', [])):
        ax = [x for x in ax if not x.startswith('height')] + ['axis equal image']   # Kreis bleibt rund
    if any('Marken pi' in e for e in opt.get('extra', [])):
        ax += ['xtick={1.5708,3.1416,4.7124,6.2832,7.854,9.4248}',
               'xticklabels={$\\frac{\\pi}{2}$,$\\pi$,$\\frac{3\\pi}{2}$,$2\\pi$,$\\frac{5\\pi}{2}$,$3\\pi$}']
    out = [r'\begin{tikzpicture}\begin{axis}[' + ','.join(ax) + ']']
    beschriftet = set()
    for name, term, a, b, gestr in kurven:
        dom = f'domain={a}:{b}' if a else f'domain={x0}:{x1}'
        stil = 'black' + (',dashed' if gestr else '')
        out.append(r'\addplot[%s,%s] {%s};' % (stil, dom, _pgf(term)))
        if name and name not in beschriftet:
            beschriftet.add(name)
            # Beschriftung an einer Stelle, an der die Kurve im Fenster liegt (von rechts gesucht)
            import math
            pyt = term.replace('^', '**').replace('deg(x)', 'x')
            lo, hi = (float(a), float(b)) if a else (x0, x1)
            xb = None
            for k in range(40):
                xt = hi - (hi - lo) * (0.12 + 0.02 * k)
                try:
                    yt = eval(pyt, {'x': xt, 'exp': math.exp, 'sin': math.sin, 'e': math.e})
                except Exception:
                    continue
                if y0 + 0.08 * (y1 - y0) < yt < y1 - 0.15 * (y1 - y0):
                    xb = xt
                    break
            if xb is None:
                xb = lo + 0.5 * (hi - lo)
            lab = name.replace('G_', 'G_').replace("'", "'")
            lab = re.sub(r'^G_(\w)$', r'G_\1', lab)
            lab = '$' + lab + '$' if re.fullmatch(r"[A-Za-z_' ]{1,5}|I+", lab) else tx(lab)
            out.append(r'\node[font=\small,fill=white,inner sep=1pt,anchor=south west] at (axis cs:%s,{%s}) {%s};'
                       % (xb, _pgf(term).replace('x', '(%s)' % xb).replace('e(%s)p' % xb, 'exp'), lab))
    for e in opt.get('extra', []):
        if e.startswith('Linie'):
            pts = re.findall(r'\((-?[\d.]+)\|(-?[\d.]+)\)', e)
            out.append(r'\draw[black] ' + ' -- '.join(f'(axis cs:{x},{y})' for x, y in pts) + ';')
        elif e.startswith('Bogen'):
            m = re.match(r'Bogen \((-?[\d.]+)\|(-?[\d.]+)\) ([\d.]+) (-?\d+)\.\.(-?\d+)', e)
            cx, cy, r_, w1, w2 = m.groups()
            out.append(r'\addplot[black,domain=%s:%s,samples=60] ({%s+%s*cos(x)},{%s+%s*sin(x)});'
                       % (w1, w2, cx, r_, cy, r_))
        elif e.startswith('Kreis'):
            m = re.match(r'Kreis \((-?[\d.]+)\|(-?[\d.]+)\) ([\d.]+)', e)
            cx, cy, r_ = m.groups()
            out.append(r'\addplot[black!60,domain=0:360,samples=90] ({%s+%s*cos(x)},{%s+%s*sin(x)});'
                       % (cx, r_, cy, r_))
    out.append(r'\end{axis}\end{tikzpicture}')
    D.abb_gezeichnet = getattr(D, 'abb_gezeichnet', 0) + 1
    return ''.join(out)




# ===========================================================================
# Lauf C: alle Typen der P10-Wortlautdateien
# ===========================================================================
def rahmen(d, D=None, iid='', grund=''):
    """Grauer Beschreibungsrahmen (seltene Typen, Beschreibung reicht nicht zum Zeichnen)."""
    if D is not None:
        D.abb_rahmen = getattr(D, 'abb_rahmen', 0) + 1
        if grund:
            D.abb_rahmen_grund = getattr(D, 'abb_rahmen_grund', [])
            D.abb_rahmen_grund.append(f'{iid}: {grund}')
            if hasattr(D, 'befund'):
                D.befund(f'{iid}: Abbildung als Beschreibungsrahmen ({grund[:90]})')
    return (r'\fbox{\parbox{0.9\linewidth}{\footnotesize\color{mbgrau}Abbildung im Original: '
            + tx(d.strip()) + '}}')


def _z(s):
    return float(s.strip().replace(',', '.').replace('−', '-'))


def _num_de(v, nachkomma=None):
    if nachkomma is None:
        s = ('%.3f' % v).rstrip('0').rstrip('.')
    else:
        s = ('%.' + str(nachkomma) + 'f') % v
    return s.replace('.', '{,}')


def _oben_teile(s, sep=', '):
    """Teilt an sep außerhalb von (), [], „“ und $…$."""
    out, cur, tiefe, m = [], '', 0, False
    i = 0
    while i < len(s):
        c = s[i]
        if c == '$':
            m = not m
        elif not m and c in '([„':
            tiefe += 1
        elif not m and c in ')]“' and tiefe > 0:
            tiefe -= 1
        if not m and tiefe == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c
        i += 1
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


def _wertepaare(rest):
    """„Name: Wert, Name: Wert“ (Wert Zahl oder leer) -> [(name, wert|None)] oder None."""
    paare = []
    for teil in _oben_teile(rest):
        m = re.match(r'^(.+?):\s*(leer|-?\d+(?:[.,]\d+)?)$', teil.strip())
        if not m:
            m = re.match(r'^(\S+)\s+(leer|-?\d+(?:,\d+)?)$', teil.strip())   # „Mo 170“
        if not m:
            return None
        paare.append((m.group(1).strip(), None if m.group(2) == 'leer' else _z(m.group(2))))
    return paare


def abb_diagramm(d, D, iid, liegend=False):
    """Säulen- und Balkendiagramm (Lauf C): „Säulendiagramm (Achse beginnt bei 390), Größe: Kat: Wert, …“;
    Wert „leer“ = Säule fehlt (Raster zum Selbstzeichnen); „(Achse ohne Einteilung), Länge in Kästchen“ =
    Balken auf Karo ohne Zahlen, mit Schreiblinie je Balken."""
    m = re.match(r'^(Säulendiagramm|Balkendiagramm)\s*(\(([^)]*)\))?\s*,?\s*(.*)$', d)
    kopf = m.group(3) or ''
    rest = re.split(r';\s*', m.group(4))[0]
    # Größe vor dem ersten „:“, wenn dahinter Wertepaare folgen
    groesse = ''
    erstes = rest.split(', ')[0]
    if erstes.count(':') >= 2 or (re.search(r'[A-Za-zÄÖÜäöü]{3,} in ', erstes.split(':')[0]) and erstes.count(':') == 2):
        groesse, _, rest = rest.partition(':')
        rest = rest.strip()
    paare = _wertepaare(rest)
    if paare is None and ':' in rest:
        groesse, _, r2 = rest.partition(':')
        paare = _wertepaare(r2.strip())
    if not paare or len(paare) < 2:
        return None
    groesse = groesse.strip().rstrip(',')
    ohne = 'ohne Einteilung' in kopf
    y0 = 0.0
    mm = re.search(r'beginnt bei (\d+(?:,\d+)?)', kopf)
    if mm:
        y0 = _z(mm.group(1))
    werte = [w for _, w in paare if w is not None]
    hoch = max(werte)
    n = len(paare)
    if ohne:
        # Kästchen-Balken (2018-OS-K3a): Länge in Kästchen, Achse ohne Zahlen
        k = 0.45
        L = int(math.ceil(hoch)) + 2
        out = [r'\begin{tikzpicture}[x=%.2fcm,y=%.2fcm]' % (k, k)]
        out.append(r'\draw[mbgitter,line width=0.3pt,step=1] (0,0) grid (%d,%d);' % (L + 8, 2 * n + 1))
        out.append(r'\draw[line width=0.7pt] (0,0) -- (0,%d);' % (2 * n + 1))
        out.append(r'\draw[line width=0.7pt,->] (0,0) -- (%d,0);' % (L + 1))
        for i, (name, w) in enumerate(paare):
            y = 2 * (n - i) - 1
            out.append(r'\fill[mbkasten,draw=black] (0,%.2f) rectangle (%s,%.2f);' % (y - 0.4, w or 0, y + 0.4))
            out.append(r'\node[left,font=\small] at (0,%d) {%s};' % (y, tx(name)))
            out.append(r'\draw[line width=0.4pt] (%d,%.1f) -- (%d,%.1f);' % (L + 1, y - 0.4, L + 7, y - 0.4))
        out.append(r'\end{tikzpicture}')
        return ''.join(out)
    # Achse: glatte Teilung
    spanne = hoch - y0 if hoch > y0 else hoch
    roh = spanne / 5
    p10 = 10 ** math.floor(math.log10(roh)) if roh > 0 else 1
    schritt = min((s * p10 for s in (1, 2, 2.5, 5, 10) if s * p10 >= roh), default=p10 * 10)
    ymax = y0 + schritt * math.ceil((hoch - y0) / schritt + 0.35)
    leer = any(w is None for _, w in paare)
    lab = groesse or ''
    nd = max((len(('%g' % w).split('.')[1]) if '.' in ('%g' % w) else 0) for w in werte)
    zahlfmt = r'/pgf/number format/use comma,/pgf/number format/1000 sep={\,},/pgf/number format/fixed,/pgf/number format/precision=%d' % max(nd, 0)
    lang = max(len(name) for name, _ in paare) > 6
    ax = [f'ymin={_g(y0)}', f'ymax={_g(ymax)}', f'ytick distance={_g(schritt)}',
          'tick label style={font=\\small}', 'xtick pos=bottom', 'ytick pos=left',
          'yticklabel style={%s}' % zahlfmt, 'ymajorgrids', 'grid style={mbgitter}',
          'xtick={%s}' % ','.join(str(i) for i in range(n)), 'xticklabels={%s}' % ','.join('{%s}' % tx(nm) for nm, _ in paare),
          'xmin=-0.5', 'xmax=%s' % _g(n - 0.5),
          'bar width=%s' % ('5mm' if n > 8 else '7mm')]
    if leer:
        ax += ['minor y tick num=1', 'yminorgrids']   # Raster zum Ergänzen der fehlenden Säule
    if liegend:
        ax = [a.replace('ymin', 'xmin').replace('ymax', 'xmax').replace('ytick distance', 'xtick distance')
              .replace('ymajorgrids', 'xmajorgrids').replace('yminorgrids', 'xminorgrids')
              .replace('minor y tick', 'minor x tick').replace('yticklabel style', 'xticklabel style')
              .replace('xtick={', 'ytick={').replace('xticklabels', 'yticklabels')
              .replace('xmin=-0.5', 'ymin=-0.5').replace('xmax=%s' % _g(n - 0.5), 'ymax=%s' % _g(n - 0.5))
              for a in ax]
        ax = [x for x in ax if not x.startswith('bar width')] + ['bar width=4mm', 'xtick pos=bottom', 'ytick pos=left']
        ax = [x for x in ax if x not in ('xtick pos=bottom', 'ytick pos=left')] + ['xtick pos=bottom', 'ytick pos=left']
        ax += ['xbar', 'y dir=reverse', 'width=11cm', 'height=%.1fcm' % (0.75 * n + 1.6)]
        if lab:
            ax.append('xlabel={%s}' % tx(lab))
        coords = ' '.join(f'({_g(w)},{i})' for i, (_, w) in enumerate(paare) if w is not None)
    else:
        breite = min(13.5, (1.1 if not lang else 1.9) * n + 2.5)
        ax += ['ybar', 'width=%.1fcm' % breite, 'height=5.2cm']
        if lab:
            ax += ['ylabel={%s}' % tx(lab), 'ylabel style={font=\\small}']
        if lang:
            ax.append('xticklabel style={text width=2cm,align=center,font=\\scriptsize}')
        coords = ' '.join(f'({i},{_g(w)})' for i, (_, w) in enumerate(paare) if w is not None)
    if y0 > 0:
        # Achse beginnt nicht bei null: Unterbrechung an der Achse andeuten
        pass
    return (r'\begin{tikzpicture}\begin{axis}[' + ','.join(ax) + ']'
            r'\addplot[fill=mbkasten,draw=black] coordinates {' + coords + r'};\end{axis}\end{tikzpicture}')


def _g(v):
    return ('%.4f' % v).rstrip('0').rstrip('.')


# --- Kreisdiagramm, Glücksrad, Zahlenscheiben --------------------------------
FUELL = {'grau': 'black!25', 'hellgrau': 'black!10', 'dunkel': 'black!60', 'schwarz': 'black!80'}


def _sektor_muster(a1, a2, r, art):
    """Schraffur/Punkte in einem Sektor (ohne Bibliothek patterns)."""
    out = [r'\begin{scope}\clip (0,0) -- (%s:%s) arc (%s:%s:%s) -- cycle;' % (_g(a1), r, _g(a1), _g(a2), r)]
    if art == 'schraffiert':
        out.append(r'\foreach \i in {-12,...,12}{\draw[line width=0.3pt] (\i*0.18-2.5,-2.5) -- ++(5,5);}')
    else:
        out.append(r'\foreach \i in {-14,...,14}{\foreach \j in {-14,...,14}{\fill (\i*0.16,\j*0.16) circle (0.5pt);}}')
    out.append(r'\end{scope}')
    return ''.join(out)


def abb_kreisdiagramm(d, D, iid):
    m = re.match(r'Kreisdiagramm:\s*Sektoren (im|gegen den) Uhrzeigersinn ab (\d+) Uhr:\s*(.*)$', d)
    if not m:
        return None
    uhr = m.group(1) == 'im'
    start = 90 - (int(m.group(2)) % 12) * 30
    teile = [t.strip() for t in m.group(3).split(';')]
    linie_alle = any('an jedem Sektor eine Schreiblinie' in t for t in teile[1:])
    linie_leere = any('an den leeren Sektoren' in t for t in teile[1:])
    sek = []
    for it in _oben_teile(teile[0]):
        mm = re.match(r'^(?:\[([^\]]*)\])?\s*(.*?)\s*(\d+(?:,\d+)?)°\s*(?:\(([^)]*)\))?$', it)
        if not mm:
            return None
        attr = [x.strip() for x in ((mm.group(1) or '') + ',' + (mm.group(4) or '')).split(',') if x.strip()]
        sek.append(dict(attr=attr, text=mm.group(2).strip(), w=_z(mm.group(3))))
    if abs(sum(s['w'] for s in sek) - 360) > 1.5:
        D.befund(f'{iid}: Kreisdiagramm, Winkelsumme {sum(s["w"] for s in sek):g}° statt 360°')
    r = 2.0
    out = [r'\begin{tikzpicture}[line width=0.6pt,baseline=(current bounding box.north)]']
    a = start
    beschr = []
    for s in sek:
        b = a - s['w'] if uhr else a + s['w']
        lo, hi = min(a, b), max(a, b)
        fill = next((FUELL[x] for x in s['attr'] if x in FUELL), None)
        ohne_linie = any('ohne weitere Trennlinie' in x for x in s['attr'])
        if fill:
            out.append(r'\fill[%s] (0,0) -- (%s:%s) arc (%s:%s:%s) -- cycle;' % (fill, _g(lo), r, _g(lo), _g(hi), r))
        for x in s['attr']:
            if x in ('gepunktet', 'schraffiert'):
                out.append(_sektor_muster(lo, hi, r, x))
        if not ohne_linie:
            out.append(r'\draw (0,0) -- (%s:%s);' % (_g(a), r))
        mitte = (lo + hi) / 2
        leer = 'leer' in s['attr'] or not s['text']
        pfeil3 = any('drei Schreiblinien' in x for x in s['attr'])
        if pfeil3:
            beschr.append((mitte, 3))
        elif s['text']:
            out.append(r'\node[font=\small,anchor=%s] at (%s:%.2f) {%s};'
                       % (_g((mitte + 180) % 360), _g(mitte), r + 0.15, tx(s['text'])))
        elif ohne_linie:
            pass
        elif linie_alle or linie_leere or leer:
            beschr.append((mitte, 1))
        a = b
    out.append(r'\draw (0,0) circle (%s); \fill (0,0) circle (1.3pt);' % r)
    for mitte, n in beschr:
        rechts = math.cos(math.radians(mitte)) >= 0
        out.append(r'\draw[line width=0.4pt] (%s:%.2f) -- (%s:%.2f);' % (_g(mitte), r * 0.7, _g(mitte), r + 0.4))
        for k in range(n):
            out.append(r'\draw[line width=0.4pt] ($(%s:%.2f)+(0,%.2f)$) -- ++(%s,0);'
                       % (_g(mitte), r + 0.4, -0.55 * k, '1.8' if rechts else '-1.8'))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def _rad(felder, r=1.6, zeiger=True, leer=False):
    n = len(felder)
    out = [r'\begin{tikzpicture}[line width=0.6pt,baseline=(current bounding box.north)]']
    out.append(r'\draw (0,0) circle (%s);' % r)
    for i in range(n):
        out.append(r'\draw (0,0) -- (%s:%s);' % (_g(90 - i * 360 / n), r))
        mitte = 90 - (i + 0.5) * 360 / n
        if leer:
            out.append(r'\draw[line width=0.4pt] ($(%s:%.2f)+(-0.25,-0.12)$) rectangle ++(0.5,0.32);' % (_g(mitte), r * 0.62))
        else:
            out.append(r'\node[font=\small] at (%s:%.2f) {%s};' % (_g(mitte), r * 0.65, tx(felder[i])))
    out.append(r'\fill (0,0) circle (1.3pt);')
    if zeiger:
        out.append(r'\fill (0,%.2f) -- (-0.15,%.2f) -- (0.15,%.2f) -- cycle;' % (r - 0.05, r + 0.35, r + 0.35))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def abb_gluecksrad(d, D, iid):
    m = re.match(r'Glücksrad:\s*(\d+) gleich große Felder, im Uhrzeigersinn ab 12 Uhr:\s*([^;]*)', d)
    if not m:
        return None
    felder = [x.strip() for x in m.group(2).split(',')]
    if len(felder) != int(m.group(1)):
        D.befund(f'{iid}: Glücksrad mit {len(felder)} statt {m.group(1)} Feldern')
        return None
    return _rad(felder)


def abb_zahlenscheiben(d, D, iid):
    m = re.match(r'Zahlenscheiben:\s*zwei Scheiben mit je (\d+) gleich großen Sektoren, Pfeil oben;\s*(.*)$', d)
    if not m:
        return None
    n, rest = int(m.group(1)), m.group(2)
    if 'alle Sektoren leer' in rest:
        return _rad([''] * n, 1.3, leer=True) + r'\hspace{1.2cm}' + _rad([''] * n, 1.3, leer=True)
    mm = re.match(r'links im Uhrzeigersinn ab 12 Uhr:\s*([^;]*);\s*rechts:\s*(.*)$', rest)
    if not mm:
        return None
    l = [x.strip() for x in mm.group(1).split(',')]
    r_ = [x.strip() for x in mm.group(2).split(',')]
    if len(l) != n or len(r_) != n:
        return None
    return _rad(l, 1.3) + r'\hspace{1.2cm}' + _rad(r_, 1.3)


def abb_wuerfelnetze(d, D, iid, vorspann_abb=''):
    m = re.match(r'Würfelnetze\s*\(([^)]*)\):\s*(.*)$', d)
    if not m:
        return None
    k = 0.6
    bilder = []
    for teil in m.group(2).split(' | '):
        mm = re.match(r'(Würfel \w+)(?: \(neu\))?:\s*(.*)$', teil.strip())
        if not mm:
            return None
        name, rest = mm.group(1), mm.group(2)
        if 'alle Felder leer' in rest:
            ob, reihe, un = '', [''] * 4, ''
        else:
            m2 = re.match(r'oben (\S*);\s*Reihe ([^;]*);\s*unten (\S*)$', rest)
            if not m2:
                return None
            ob, reihe, un = m2.group(1), [x.strip() for x in m2.group(2).split(',')], m2.group(3)
            if len(reihe) != 4:
                return None
        z = [r'\begin{tikzpicture}[x=%scm,y=%scm,line width=0.6pt,baseline=(current bounding box.north)]' % (k, k)]
        felder = [(1, 2, ob)] + [(i, 1, reihe[i]) for i in range(4)] + [(1, 0, un)]
        for x, y, t in felder:
            z.append(r'\draw (%d,%d) rectangle ++(1,1); \node[font=\small] at (%.1f,%.1f) {%s};' % (x, y, x + .5, y + .5, tx(t)))
        z.append(r'\node[font=\small,anchor=south west] at (2.2,2.1) {%s};' % tx(name))
        z.append(r'\end{tikzpicture}')
        bilder.append(''.join(z))
    return r'\hspace{1cm}'.join(bilder)


# --- Baumdiagramm ------------------------------------------------------------
def abb_baum(d, D, iid):
    m = re.match(r'Baumdiagramm\s*\(([^)]*)\):\s*(.*)$', d)
    if not m:
        return None
    kopf, rest = m.group(1), m.group(2)
    rest = re.split(r';\s*darunter ', rest)[0]
    stufen, aeste, nur = [], None, None
    for t in kopf.split(';'):
        t = t.strip()
        if t.startswith('Stufen:'):
            stufen = [x.strip() for x in t[7:].split('|')]
        elif t.startswith('Äste '):
            aeste = [x.strip() for x in t[5:].split(',')]
        elif re.match(r'nur (.+) verzweigt weiter', t):
            nur = re.match(r'nur (.+) verzweigt weiter', t).group(1).strip()
        elif t == 'eine Stufe':
            stufen = ['']
    werte, fett, alle_leer, uebrige = {}, set(), False, False
    for t in [x.strip() for x in rest.split(';') if x.strip()]:
        if re.match(r'alle \d+ Äste leer', t):
            alle_leer = True; continue
        if t.startswith('übrige Äste'):
            uebrige = True; continue
        mm = re.match(r'^(.+?):\s*(leer|\d+/\d+)(\s*\(Pfad fett\))?$', t)
        if not mm:
            return None
        for p in mm.group(1).split(','):
            werte[tuple(x.strip() for x in p.strip().split('>'))] = mm.group(2)
            if mm.group(3):
                fett.add(tuple(x.strip() for x in p.strip().split('>')))
    tiefe = len(stufen) or max(len(p) for p in werte)
    if aeste is None:
        aeste = [p[0] for p in werte if len(p) == 1]
    if not aeste:
        return None
    # Pfade: voller Baum, außer „nur X verzweigt weiter“ (dann nur die genannten Pfade)
    if nur:
        pfade = set()
        for p in werte:
            for i in range(1, len(p) + 1):
                pfade.add(p[:i])
        # Geschwister ergänzen (jeder Knoten, der verzweigt, hat alle Äste)
        for p in list(pfade):
            for a in aeste:
                pfade.add(p[:-1] + (a,))
    else:
        pfade = set()
        def voll(pre):
            if len(pre) == tiefe:
                return
            for a in aeste:
                pfade.add(pre + (a,)); voll(pre + (a,))
        voll(())
    blaetter = sorted([p for p in pfade if not any(q[:len(p)] == p and len(q) > len(p) for q in pfade)],
                      key=lambda p: [aeste.index(x) if x in aeste else 9 for x in p])
    dy = 0.95 if len(aeste) > 2 else (0.62 if len(blaetter) > 6 else 0.9)
    dx = 3.4 if tiefe <= 2 else 3.0
    pos = {}
    for i, b in enumerate(blaetter):
        pos[b] = (len(b) * dx, -i * dy)
    def lage(p):
        if p in pos:
            return pos[p]
        kinder = [q for q in pfade if len(q) == len(p) + 1 and q[:len(p)] == p]
        ys = [lage(q)[1] for q in kinder]
        pos[p] = (len(p) * dx, sum(ys) / len(ys))
        return pos[p]
    lage(())
    name = {p: 'k%d' % i for i, p in enumerate(sorted(pfade, key=lambda p: (len(p), p)))}
    name[()] = 'k0w'
    out = [r'\begin{tikzpicture}[line width=0.5pt,baseline=(current bounding box.north)]']
    ytop = max(y for _, y in pos.values()) + 0.7
    for i, s in enumerate(stufen):
        if s:
            out.append(r'\node[font=\scriptsize,mbgrau] at (%.2f,%.2f) {%s};' % ((i + 0.6) * dx, ytop, tx(s)))
    out.append(r'\fill (0,%.2f) circle (1.3pt) coordinate (k0w);' % pos[()][1])
    for p in sorted(pfade, key=len):
        out.append(r'\node[font=\scriptsize,inner sep=2pt] (%s) at (%.2f,%.2f) {%s};' % (name[p], pos[p][0], pos[p][1], tx(p[-1])))
    for p in sorted(pfade, key=len):
        stil = 'line width=1.4pt' if any(f[:len(p)] == p for f in fett) else ''
        von = name[p[:-1]] + ('.east' if p[:-1] else '')
        w = werte.get(p, 'leer' if alle_leer else None)
        anker = 'south' if pos[p][1] >= pos[p[:-1]][1] else 'north'   # Feld auf der Außenseite des Asts
        lab = ''
        if w is not None:
            if w == 'leer':
                lab = r'node[pos=0.55,anchor=%s,draw,line width=0.3pt,fill=white,minimum width=0.7cm,minimum height=0.34cm,inner sep=0pt] {}' % anker
            else:
                lab = r'node[pos=0.55,anchor=%s,font=\scriptsize,fill=white,inner sep=1pt] {%s}' % (anker, tx(w))
        out.append(r'\draw[%s] (%s) -- %s (%s.west);' % (stil, von, lab, name[p]))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


# --- Achsenkreuz ohne Einteilung ----------------------------------------------
def abb_achsenkreuz_leer(d, D, iid):
    m = re.search(r'Karoraster(?: (\d+) × (\d+) Kästchen)?', d)
    nx = ny = None
    if m and m.group(1):
        nx, ny = int(m.group(1)), int(m.group(2))
    ox = oy = 1
    mm = re.search(r'Ursprung (\d+) Kästchen vom linken und (?:(\d+) )?vom unteren Rand', d)
    if mm:
        ox = int(mm.group(1)); oy = int(mm.group(2) or mm.group(1))
    mm = re.search(r'(\d+) Kästchen nach rechts, (\d+) nach oben', d)
    if mm:
        nx, ny = int(mm.group(1)) + ox + 1, int(mm.group(2)) + oy + 1
    if not nx:
        return None
    k = min(0.45, 15.0 / nx, 11.0 / ny)
    tl = re.search(r'Teilstriche alle (\d+) Kästchen, x-Achse (\d+), y-Achse (\d+)', d)
    namen = re.findall(r'„([^“]*)“ \((rechts|oben)\)', d)
    out = [r'\begin{tikzpicture}[x=%.3fcm,y=%.3fcm]' % (k, k),
           r'\draw[mbgitter,line width=0.3pt,step=1] (0,0) grid (%d,%d);' % (nx, ny),
           r'\draw[line width=0.7pt,-{Stealth[length=2mm]}] (%d,%d) -- (%.1f,%d);' % (ox, oy, nx - 0.3, oy),
           r'\draw[line width=0.7pt,-{Stealth[length=2mm]}] (%d,%d) -- (%d,%.1f);' % (ox, oy, ox, ny - 0.3)]
    if tl:
        s, ax, ay = int(tl.group(1)), int(tl.group(2)), int(tl.group(3))
        for i in range(1, ax + 1):
            out.append(r'\draw[line width=0.5pt] (%d,%.2f) -- (%d,%.2f);' % (ox + i * s, oy - .25, ox + i * s, oy + .25))
        for i in range(1, ay + 1):
            out.append(r'\draw[line width=0.5pt] (%.2f,%d) -- (%.2f,%d);' % (ox - .25, oy + i * s, ox + .25, oy + i * s))
    for t, wo in namen:
        if wo == 'rechts':
            out.append(r'\node[font=\small,anchor=north east] at (%.1f,%.1f) {%s};' % (nx - 0.3, oy - 0.2, tx(t)))
        else:
            out.append(r'\node[font=\small,anchor=south west] at (%.1f,%.1f) {%s};' % (ox + 0.3, ny - 0.3, tx(t)))
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


# --- Graph und Koordinatensystem (P10) -----------------------------------------
def _pgf_p10(term):
    """Term (Python-Schreibweise, ^ oder **) -> pgfmath; Potenzen geklammert, weil pgfmath das
    Vorzeichen vor ^ bindet (-x^2 wäre sonst (-x)^2)."""
    t = term.replace('**', '^').replace(' ', '')
    out, i = '', 0
    while i < len(t):
        if t[i] == '^':
            # linken Operanden finden
            j = len(out) - 1
            if out[j] == ')':
                tiefe = 0
                while j >= 0:
                    tiefe += {')': 1, '(': -1}.get(out[j], 0)
                    if tiefe == 0:
                        break
                    j -= 1
            else:
                while j > 0 and (out[j - 1].isalnum() or out[j - 1] == '.'):
                    j -= 1
            mm = re.match(r'\(?-?[\d.]+\)?|[a-z]', t[i + 1:])
            exp = mm.group(0)
            out = out[:j] + '(' + out[j:] + '^' + exp + ')'
            i += 1 + len(exp)
            continue
        out += t[i]
        i += 1
    return out


def _py(term):
    return term.replace('^', '**')


def _achsenwort(s):
    s = s.strip()
    if re.fullmatch(r"[A-Za-z](\([a-z]\))?|[A-Za-z]_\w|h\(t\)", s):
        return '$' + s + '$'
    return tx(s)


def abb_graph_p10(d, D, iid):
    """„Graph: f: Term [für a..b] | g: Term; x a..b; y c..d; Gitter ja [(Kästchen 0,5)];
    [Achsen X | Y]; [Punkte A(0|-2), B(2|-2) [als Dreieck verbunden]]; [β bei B zwischen BA und BC]“
    und „Koordinatensystem: …“ (ohne Kurven). Kleine Bereiche als Karo (1 Einheit = 1 Kästchen),
    große mit fester Breite."""
    typ, _, rest = d.partition(':')
    teile = [t.strip() for t in rest.split(';')]
    kurven, opt, punkte, winkel, verb = [], {}, [], [], False
    for t in teile:
        m = re.match(r'^([xy]) (-?[\d.]+)\.\.(-?[\d.]+)$', t.replace('−', '-'))
        if m:
            opt[m.group(1)] = (float(m.group(2)), float(m.group(3))); continue
        if t.startswith('Gitter'):
            opt['gitter'] = 'ja' in t
            mk = re.search(r'Kästchen (\d+(?:,\d+)?)', t)
            opt['kaestchen'] = _z(mk.group(1)) if mk else 1.0
            continue
        if t.startswith('Achsen '):
            opt['achsen'] = [x.strip() for x in t[7:].split('|')]; continue
        if t.startswith('Punkte '):
            verb = 'verbunden' in t
            for mm in re.finditer(r'([A-Z]\w*)\((-?[\d.,−]+)\|(-?[\d.,−]+)\)', t):
                punkte.append((mm.group(1), _z(mm.group(2)), _z(mm.group(3))))
            continue
        mw = re.match(r'^(\S+) bei ([A-Z]) zwischen ([A-Z])([A-Z]) und ([A-Z])([A-Z])$', t)
        if mw:
            winkel.append(mw.groups()); continue
        if typ == 'Graph':
            for k in t.split(' | '):
                mm = re.match(r'^(?:([^:]+):\s*)?(.+?)(?:\s+für (-?[\d.]+)\.\.(-?[\d.]+))?$', k.strip())
                if not mm or not re.search(r'x|\d', mm.group(2)):
                    return None
                kurven.append((mm.group(1) or '', mm.group(2), mm.group(3), mm.group(4)))
            continue
        return None   # unbekannter Teil -> Rahmen
    if 'x' not in opt or 'y' not in opt:
        return None
    (x0, x1), (y0, y1) = opt['x'], opt['y']
    klein = (x1 - x0) <= 16 and (y1 - y0) <= 16
    ax = [f'xmin={_g(x0)},xmax={_g(x1)},ymin={_g(y0)},ymax={_g(y1)}', 'axis lines=middle',
          'tick label style={font=\\scriptsize}', 'clip=true', '/pgf/number format/use comma',
          'axis line style={-{Stealth[length=2mm]}}', 'every axis plot/.append style={line width=0.9pt}']
    if klein:
        k = opt.get('kaestchen', 1.0)
        e = 0.55 if max(x1 - x0, y1 - y0) <= 12 else 0.42
        if k < 1:
            e = 0.9
        ax += [f'x={e}cm', f'y={e}cm', 'xtick distance=1', 'ytick distance=1', 'enlargelimits=false']
        if opt.get('gitter'):
            ax += ['grid=both', 'grid style={mbgitter,line width=0.3pt}', 'major grid style={mbgitter}']
            if k < 1:
                ax += ['minor tick num=%d' % (round(1 / k) - 1)]
        ax += ['xlabel={$x$}', 'ylabel={$y$}', 'x label style={anchor=west}', 'y label style={anchor=south}']
    else:
        ax += ['width=11.5cm', 'height=7.5cm']
        if opt.get('gitter'):
            ax += ['grid=both', 'grid style={mbgitter,line width=0.3pt}', 'minor tick num=1']
        if x0 >= 0 and y0 >= 0:
            ax = [a for a in ax if a != 'axis lines=middle'] + ['axis lines=left']
        xl, yl = opt.get('achsen', ['x', 'y'])
        ax += ['xlabel={%s}' % _achsenwort(xl), 'ylabel={%s}' % _achsenwort(yl),
               'label style={font=\\small}', 'scaled ticks=false',
               '/pgf/number format/1000 sep={\\,}']
    if klein and 'achsen' in opt:
        xl, yl = opt['achsen']
        ax = [a for a in ax if not a.startswith(('xlabel', 'ylabel'))] + \
             ['xlabel={%s}' % _achsenwort(xl), 'ylabel={%s}' % _achsenwort(yl)]
    out = [r'\begin{tikzpicture}\begin{axis}[' + ','.join(ax) + ']']
    beschriftet = set()
    gesetzt = []   # (x, y) schon gesetzter Namen, in Achsenanteilen
    for name, term, a, b in kurven:
        lo, hi = (float(a), float(b)) if a else (x0, x1)
        out.append(r'\addplot[black,domain=%s:%s,samples=%d] {%s};' % (_g(lo), _g(hi), 120, _pgf_p10(term)))
        if name and name not in beschriftet:
            beschriftet.add(name)
            xb = None
            for kk in range(40):
                xt = hi - (hi - lo) * (0.08 + 0.022 * kk)
                try:
                    yt = eval(_py(term), {'x': xt, 'exp': math.exp})
                except Exception:
                    continue
                fx, fy = (xt - x0) / (x1 - x0), (yt - y0) / (y1 - y0)
                if 0.08 < fy < 0.88 and all(abs(fx - gx) > 0.12 or abs(fy - gy) > 0.1 for gx, gy in gesetzt):
                    xb = xt
                    break
            if xb is None:
                continue
            yb = eval(_py(term), {'x': xb, 'exp': math.exp})
            gesetzt.append(((xb - x0) / (x1 - x0), (yb - y0) / (y1 - y0)))
            lab = '$' + name + '$' if re.fullmatch(r'[A-Za-z]\w?', name) else tx(name)
            out.append(r'\node[font=\small,fill=white,inner sep=1pt,anchor=south west] at (axis cs:%s,%s) {%s};'
                       % (_g(xb), _g(yb), lab))
    if punkte:
        if verb:
            out.append(r'\draw[line width=0.8pt] ' + ' -- '.join(f'(axis cs:{_g(x)},{_g(y)})' for _, x, y in punkte) + ' -- cycle;')
        for n, x, y in punkte:
            out.append(r'\fill (axis cs:%s,%s) circle (1.6pt) node[above right,font=\small,inner sep=1pt] {$%s$};' % (_g(x), _g(y), n))
    pk = {n: (x, y) for n, x, y in punkte}
    for lab, s, p1, q1, p2, q2 in winkel:
        if s in pk and q1 in pk and q2 in pk:
            sx, sy = pk[s]
            a1 = math.degrees(math.atan2(pk[q1][1] - sy, pk[q1][0] - sx))
            a2 = math.degrees(math.atan2(pk[q2][1] - sy, pk[q2][0] - sx))
            if (a2 - a1) % 360 > 180:
                a1, a2 = a2, a1
            a2 = a1 + (a2 - a1) % 360
            out.append(r'\draw[line width=0.5pt] (axis cs:%s,%s) ++(%s:0.55cm) arc (%s:%s:0.55cm);'
                       % (_g(sx), _g(sy), _g(a1), _g(a1), _g(a2)))
            out.append(r'\node[font=\small] at ($(axis cs:%s,%s)+(%s:0.85cm)$) {%s};'
                       % (_g(sx), _g(sy), _g((a1 + a2) / 2), tx(lab)))
    out.append(r'\end{axis}\end{tikzpicture}')
    return ''.join(out)


# --- Graphauswahl -------------------------------------------------------------
FORMEN = [   # Form in Worten -> Kurve im Einheitsquadrat (Entscheidung, Lauf C)
    (r'erst waagerecht.*Knick steigend', ('linie', [(0, .3), (.4, .3), (1, .9)])),
    (r'erst waagerecht.*Knick fallend', ('linie', [(0, .6), (.4, .6), (1, .15)])),
    (r'Gerade aus dem Ursprung', ('term', '0.85*x')),
    (r'Gerade mit positivem y-Achsenabschnitt, flach', ('term', '0.3+0.35*x')),
    (r'steigende Gerade ab positivem y-Achsenabschnitt|Gerade mit positivem y-Achsenabschnitt', ('term', '0.25+0.6*x')),
    (r'gekrümmte, immer steilere Kurve aus dem Ursprung', ('term', '0.88*x^2')),
    (r'gekrümmte, immer steilere Kurve ab positivem', ('term', '0.2*exp(1.45*x)')),
]


def abb_graphauswahl(d, D, iid):
    m = re.match(r'Graphauswahl:\s*(\w+) Achsenkreuze(?: ([A-Z])–([A-Z]))?(?:,? ([A-Z](?:, [A-Z])+))?\s*ohne Einteilung\s*(\(([^)]*)\))?(.*)$', d)
    if not m:
        return None
    klammer = m.group(6) or ''
    rest = m.group(7)
    gitter = 'mit Gitter' in rest
    passt = 'passt nicht' in rest
    rest = rest.split(':', 1)[1] if ':' in rest else ''
    fenster = re.match(r'x (-?[\d.]+)\.\.(-?[\d.]+); y (-?[\d.]+)\.\.(-?[\d.]+)', klammer)
    xn = yn = ''
    mn = re.match(r'x: ([^,]*), y: (.*)$', klammer)
    if mn:
        xn, yn = mn.group(1), mn.group(2)
    eintr = re.findall(r'(?:^|;)\s*([A-Z]|\d)\s+(.*?)(?=;\s*(?:[A-Z]|\d)\s|$)', rest.strip())
    if not eintr:
        return None
    bilder = []
    for name, form in eintr:
        form = form.strip()
        if fenster:
            fx0, fx1, fy0, fy1 = map(float, fenster.groups())
        else:
            fx0, fx1, fy0, fy1 = 0, 1, 0, 1
        zeich = None
        mt = re.match(r'(?:Gerade|Parabel)\s+([-\d.*x^+ ]+?)(?: für (-?[\d.]+)\.\.(-?[\d.]+))?$', form)
        ms = re.match(r'Streckenzug\s+(.*)$', form)
        mh = re.search(r'von \((-?[\d.]+)\|(-?[\d.]+)\) nach \((-?[\d.]+)\|(-?[\d.]+)\)', form)
        if mt:
            zeich = ('term', mt.group(1), mt.group(2), mt.group(3))
        elif ms:
            zeich = ('linie', [(float(a), float(b)) for a, b in re.findall(r'\((-?[\d.]+)\|(-?[\d.]+)\)', ms.group(1))])
        elif mh and 'Hyperbel' in form:
            ax_, ay_, bx_, by_ = map(float, mh.groups())
            kk = ax_ * ay_
            zeich = ('term', f'{kk:.4f}/x', str(ax_), str(bx_))
        else:
            for muster, z in FORMEN:
                if re.search(muster, form):
                    zeich = z if z[0] == 'linie' else ('term', z[1], None, None)
                    break
        if not zeich:
            return None
        z = [r'\begin{tikzpicture}\begin{axis}[width=3.9cm,height=3.4cm,scale only axis=false,axis lines=middle,'
             r'xtick=\empty,ytick=\empty,xmin=%s,xmax=%s,ymin=%s,ymax=%s,clip=true,'
             r'axis line style={-{Stealth[length=1.5mm]}}' % (_g(fx0), _g(fx1 + 0.08 * (fx1 - fx0)), _g(fy0), _g(fy1 + 0.08 * (fy1 - fy0)))]
        if gitter:
            z[0] += r',grid=both,minor tick num=0,xtick={%s},ytick={%s},xticklabels={},yticklabels={},grid style={mbgitter}' % (
                ','.join(_g(fx0 + i * (fx1 - fx0) / 5) for i in range(1, 6)), ','.join(_g(fy0 + i * (fy1 - fy0) / 5) for i in range(1, 6)))
        if xn:
            z[0] += r',xlabel={\tiny %s},ylabel={\tiny %s},x label style={anchor=north east,at={(1,0)},yshift=-2pt},y label style={anchor=south west,at={(0,1)},xshift=1pt}' % (tx(xn), tx(yn))
        z[0] += ']'
        if zeich[0] == 'term':
            lo = zeich[2] or _g(fx0)
            hi = zeich[3] or _g(fx1)
            z.append(r'\addplot[black,line width=0.9pt,domain=%s:%s,samples=80] {%s};' % (lo, hi, _pgf_p10(zeich[1])))
        else:
            z.append(r'\addplot[black,line width=0.9pt] coordinates {%s};' % ' '.join(f'({_g(a)},{_g(b)})' for a, b in zeich[1]))
        z.append(r'\end{axis}\end{tikzpicture}')
        unter = (r'\\[1pt]{\footnotesize $\square$ passt\quad $\square$ passt nicht}\\[2pt]\rule{3cm}{0.4pt}' if passt else '')
        bilder.append(r'\begin{tabular}[t]{@{}c@{}}{\small %s}\enspace$\square$\\%s%s\end{tabular}'
                      % (tx(name), ''.join(z), unter))
    zeilen = []
    for i in range(0, len(bilder), 4 if not passt else 3):
        zeilen.append(r'\hspace{0.4cm}'.join(bilder[i:i + (4 if not passt else 3)]))
    return r'\par\smallskip'.join(zeilen)


# --- Ankreuztabellen (Lauf C) ----------------------------------------------------
def abb_ankreuz(d, D, iid):
    """Gibt eine Kennung zurück, die echt_aufgabe auflöst: ANKREUZ{kopf|spalte|…}{zeilen|…}{art}.
    Art: opt (Zeilen = Optionen aus dem Text), fest (Zeilen aus der Beschreibung), liste (normale
    Ankreuzzeilen)."""
    rest = d.split(':', 1)[1].strip()
    if re.match(r'(zwei|drei|vier|fünf) Aussagen, je ein Ankreuzfeld', rest):
        return 'ANKREUZ{}{}{liste}'
    m = re.match(r'Zeilen (.*?); Spalten (.*)$', rest)
    if m:
        zeilen = [x.strip() for x in m.group(1).split(',')]
        spalten = [x.strip() for x in m.group(2).split('|')]
        return 'ANKREUZ{|%s}{%s}{fest}' % ('|'.join(spalten), '|'.join(zeilen))
    m = re.match(r'Spalten (.*?); (Zeile 1: .*)$', rest)
    if m:
        spalten = [x.strip() for x in m.group(1).split('|')]
        zeilen = [re.sub(r'^Zeile \d+:\s*', '', x.strip()) for x in m.group(2).split('; ')]
        return 'ANKREUZ{%s}{%s}{fest}' % ('|'.join(spalten), '|'.join(zeilen))
    m = re.match(r'(zwei|drei|vier|fünf) (Aussagen|Terme), Spalten ([^,]*)(, unter jeder Aussage eine Zeile Begründung)?$', rest)
    if m:
        spalten = [x.strip() for x in re.split(r'\s*[|/]\s*', m.group(3))]
        kopf = 'Term' if m.group(2) == 'Terme' else 'Aussage'
        return 'ANKREUZ{%s|%s}{}{opt%s}' % (kopf, '|'.join(spalten), '+begruendung' if m.group(4) else '')
    return None


# --- Abbildungstypen (Lauf C): Tabelle der bekannten Typen -----------------------
# zeichnen: Typ mit mindestens zwei Zeilen in den zehn P10-Wortlautdateien; rahmen: seltener Typ
TYPEN_RAHMEN = ('Kästchenfigur', 'Kreis mit Sektor', 'Ankreuznetze', 'leeres Karoraster', 'Tabellenauswahl',
                'leerer Streifen', 'Gefäße', 'Gefäß', 'Gewinnplan-Kasten')


def typ_von(d):
    """Typ einer Beschreibung: Text vor „:“, „(“ oder „,“, ohne „aus dem Vorspann“/„aus <Teil>“."""
    d = (d or '').strip()
    if not d:
        return ''
    t = re.split(r'[:(,;]', d, maxsplit=1)[0].strip()
    t = re.sub(r'\s+aus (dem Vorspann|\d?[a-z]\)?|\d[a-z])\b.*$', '', t)
    for g in ('Säulendiagramm', 'leerer Kreis', 'leeres Karoraster'):
        if t.startswith(g):
            return g
    return t


# ===========================================================================
# Geometrie-Skizzen (Lauf C): Dreieck, Viereck, Lageskizze, rechtwinkliges Dreieck
# Alle „nicht maßstabsgerecht“: Lage aus den Lagewörtern, Maße und Winkel nur als Beschriftung;
# wo Winkel oder Seiten die Form festlegen (Trapez), wird die Form daraus gerechnet.
# ===========================================================================
class Skizze:
    def __init__(self):
        self.P = {}            # Name -> (x, y)
        self.poly = []         # Hauptfigur
        self.seg = []          # (P, Q, stil)
        self.seite = {}        # frozenset(P, Q) -> Beschriftung
        self.winkel = []       # (S, P, Q, Beschriftung, recht)
        self.fuellung = ''     # grau | kariert | …
        self.flaechen = []     # ([Punkte], stil)
        self.punkte = []       # Punkte mit Marke (auf einer Seite)
        self.texte = []        # (x, y, Text, anker)
        self.nicht_mass = False
        self.namen = True      # Eckennamen zeigen
        self.auf = {}          # Punkt -> (P, Q): liegt auf Gerade PQ

    def strahlen(self, S):
        n = set()
        if S in self.poly:
            i = self.poly.index(S)
            n |= {self.poly[i - 1], self.poly[(i + 1) % len(self.poly)]}
        for p, q, _ in self.seg:
            if p == S:
                n.add(q)
            if q == S:
                n.add(p)
        return [x for x in n if x in self.P]

    def tex(self, breite=6.0):
        xs = [x for x, _ in self.P.values()]
        ys = [y for _, y in self.P.values()]
        w = max(xs) - min(xs) or 1
        h = max(ys) - min(ys) or 1
        s = min(breite / w, 4.2 / h, 1.6)
        cx = sum(x for x, _ in (self.P[p] for p in self.poly)) / max(1, len(self.poly)) if self.poly else 0
        cy = sum(y for _, y in (self.P[p] for p in self.poly)) / max(1, len(self.poly)) if self.poly else 0
        out = [r'\begin{tikzpicture}[x=%.3fcm,y=%.3fcm,line width=0.6pt,baseline=(current bounding box.north)]' % (s, s)]
        k = lambda p: '(%.3f,%.3f)' % self.P[p]
        for pts, stil in self.flaechen:
            if stil == 'schraffiert':
                out.append(r'\begin{scope}\clip %s -- cycle;\foreach \i in {-40,...,40}{\draw[line width=0.3pt] (\i*0.25-6,-6) -- ++(14,14);}\end{scope}'
                           % ' -- '.join(k(p) for p in pts))
            elif stil == 'kariert':
                out.append(r'\begin{scope}\clip %s -- cycle;\draw[black!45,line width=0.3pt,step=%.3f] (-10,-10) grid (20,20);\end{scope}'
                           % (' -- '.join(k(p) for p in pts), 0.3 / s))
            elif stil == 'gepunktet':
                out.append(r'\draw[dotted,line width=0.9pt] %s -- cycle;' % ' -- '.join(k(p) for p in pts))
            else:
                out.append(r'\fill[%s] %s -- cycle;' % (FUELL.get(stil, 'black!20'), ' -- '.join(k(p) for p in pts)))
        if self.poly:
            f = FUELL.get(self.fuellung)
            out.append(r'\draw%s %s -- cycle;' % (f'[fill={f}]' if f else '', ' -- '.join(k(p) for p in self.poly)))
        for p, q, stil in self.seg:
            out.append(r'\draw[%s] %s -- %s;' % (stil, k(p), k(q)))
        for S, p, q, lab, recht in self.winkel:
            if S not in self.P or p not in self.P or q not in self.P:
                continue
            sx, sy = self.P[S]
            a1 = math.degrees(math.atan2(self.P[p][1] - sy, self.P[p][0] - sx))
            a2 = math.degrees(math.atan2(self.P[q][1] - sy, self.P[q][0] - sx))
            d = (a2 - a1) % 360
            if d > 180:
                a1, a2, d = a2, a1, 360 - d
            a2 = a1 + d
            r = 0.42 / s * 1.0
            if recht:
                u = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
                v = (math.cos(math.radians(a2)), math.sin(math.radians(a2)))
                e = 0.28 / s
                out.append(r'\draw[line width=0.4pt] (%.3f,%.3f) -- (%.3f,%.3f) -- (%.3f,%.3f);'
                           % (sx + e * u[0], sy + e * u[1], sx + e * (u[0] + v[0]), sy + e * (u[1] + v[1]),
                              sx + e * v[0], sy + e * v[1]))
                out.append(r'\fill (%.3f,%.3f) circle (0.6pt);' % (sx + e * (u[0] + v[0]) / 2, sy + e * (u[1] + v[1]) / 2))
            else:
                if d < 35:
                    r = 0.75 / s
                out.append(r'\draw[line width=0.4pt] (%.3f,%.3f) arc (%.2f:%.2f:%.3f);'
                           % (sx + r * math.cos(math.radians(a1)), sy + r * math.sin(math.radians(a1)), a1, a2, r))
            if lab:
                m = math.radians((a1 + a2) / 2)
                rl = (r if not recht else 0.28 / s) + (0.32 if len(klar(lab)) <= 2 else 0.5) / s
                out.append(r'\node[font=\scriptsize,inner sep=0.5pt,fill=white] at (%.3f,%.3f) {%s};'
                           % (sx + rl * math.cos(m), sy + rl * math.sin(m), tx(lab)))
        for (p, q), lab in ((tuple(sorted(k_)), v) for k_, v in self.seite.items()):
            if p not in self.P or q not in self.P or not lab:
                continue
            (x1, y1), (x2, y2) = self.P[p], self.P[q]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            nx, ny = -(y2 - y1), x2 - x1
            ln = math.hypot(nx, ny) or 1
            nx, ny = nx / ln, ny / ln
            if (mx + nx - cx) ** 2 + (my + ny - cy) ** 2 < (mx - nx - cx) ** 2 + (my - ny - cy) ** 2:
                nx, ny = -nx, -ny
            # Seiten innerhalb der Figur (Diagonale, Höhe): Beschriftung neben der Linie
            anker = 'south' if ny > 0.7 else 'north' if ny < -0.7 else ('west' if nx > 0 else 'east')
            out.append(r'\node[font=\scriptsize,anchor=%s,inner sep=2pt] at (%.3f,%.3f) {%s};' % (anker, mx, my, tx(lab)))
        if self.namen:
            for p, (x, y) in self.P.items():
                if p.startswith('_'):
                    continue
                dx, dy = x - cx, y - cy
                ln = math.hypot(dx, dy) or 1
                dx, dy = dx / ln, dy / ln
                out.append(r'\node[font=\small,inner sep=1pt] at (%.3f,%.3f) {%s};'
                           % (x + 0.3 / s * dx, y + 0.3 / s * dy, tx(p) if len(p) > 1 else '$' + p + '$'))
        for p in self.punkte:
            out.append(r'\fill %s circle (1.4pt);' % k(p))
        for x, y, t, a in self.texte:
            out.append(r'\node[font=\scriptsize,anchor=%s] at (%.3f,%.3f) {%s};' % (a, x, y, tx(t)))
        if self.nicht_mass:
            out.append(r'\node[font=\scriptsize,mbgrau,anchor=north west] at ([yshift=-2pt]current bounding box.south west) {nicht maßstabsgerecht};')
        out.append(r'\end{tikzpicture}')
        return ''.join(out)


def klar(s):
    return re.sub(r'\$|\\[a-z]+|[{}_]', '', s)


POS = {'links unten': (0, 0), 'unten links': (0, 0), 'rechts unten': (6, 0), 'unten rechts': (6, 0),
       'links oben': (0, 3.5), 'oben links': (0, 3.5), 'rechts oben': (6, 3.5), 'oben rechts': (6, 3.5),
       'oben': (3, 3.5), 'unten': (3, 0), 'links': (0, None), 'rechts': (6, None),
       'oben links von der Mitte': (2, 3.5), 'weit links': (-2, None), 'weit links oben': (-2.5, 4.2)}


def _lage(wort, alle):
    x, y = POS[wort]
    if y is None:
        # „links“/„rechts“ ohne Höhe: auf halber Höhe nur, wenn gegenüber oben und unten je eine Ecke
        # steht (Dreieck F links, J oben rechts, R unten rechts); sonst auf der Grundlinie
        gegen = 'rechts' if 'links' in wort else 'links'
        mitte = (any('oben' in w and gegen in w for w in alle) and any('unten' in w and gegen in w for w in alle)) \
            or ('oben' in alle and 'unten' in alle)
        y = 1.75 if mitte else 0
    return (x, y)


def _proj(P, A, B):
    ax, ay = A; bx, by = B; px, py = P
    dx, dy = bx - ax, by - ay
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    return (ax + t * dx, ay + t * dy)


def _schnitt(A, B, C, D):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = A, B, C, D
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-9:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


LAGEWORT = r'(oben links von der Mitte|weit links oben|weit links|links unten|unten links|rechts unten|unten rechts|links oben|oben links|rechts oben|oben rechts|oben|unten|links|rechts)'
WINKELLAB = r'(\d+(?:,\d+)?°|[α-ω](?:_\{?\w+\}?)?|\$[^$]+\$)'


def skizze_benannt(d, art=''):
    """Figur mit benannten Ecken (A, B, C …) aus Lage-, Maß-, Winkel- und Linienangaben.
    Gibt (Skizze, [nicht verstandene Angaben]) zurück."""
    S = Skizze()
    rest = d.split(':', 1)[1] if ':' in d else d
    S.nicht_mass = 'nicht maßstabsgerecht' in rest
    rest = re.sub(r';?\s*nicht maßstabsgerecht', '', rest)
    teile = []
    for t in _oben_teile(rest, '; '):
        teile += _oben_teile(t, ', ')
    offen, lagen, rel, spaet = [], {}, [], []
    letzte = None
    for t in teile:
        t = t.strip().rstrip('.')
        m = re.match(r'^(?:Dreieck )?([A-Z])\s*(?:\(' + LAGEWORT + r'\)|' + LAGEWORT + r')$', t)
        if m:
            lagen[m.group(1)] = m.group(2) or m.group(3); letzte = m.group(1); continue
        m = re.match(r'^([A-Z]) ' + LAGEWORT + r' \(rechter Winkel\)$', t)
        if m:
            lagen[m.group(1)] = m.group(2); letzte = m.group(1)
            spaet.append(('recht', m.group(1))); continue
        m = re.match(r'^rechter Winkel bei ([A-Z]) \(' + LAGEWORT + r'\)$', t)
        if m:
            lagen[m.group(1)] = m.group(2); letzte = m.group(1)
            spaet.append(('recht', m.group(1))); continue
        m = re.match(r'^([A-Z]) senkrecht (über|unter) ([A-Z])$', t)
        if m:
            rel.append((m.group(1), 'auf' if m.group(2) == 'über' else 'ab', m.group(3))); letzte = m.group(1); continue
        m = re.match(r'^([A-Z]) senkrecht darunter(?: \(rechter Winkel\))?$', t)
        if m and letzte:
            rel.append((m.group(1), 'ab', letzte))
            if 'rechter Winkel' in t:
                spaet.append(('recht', m.group(1)))
            letzte = m.group(1); continue
        m = re.match(r'^([A-Z]) (rechts|links) von ([A-Z])$', t)
        if m:
            rel.append((m.group(1), m.group(2), m.group(3))); letzte = m.group(1); continue
        m = re.match(r'^(?:Punkt )?([A-Z]) auf ([A-Z])([A-Z])(?: nahe ([A-Z]))?$', t)
        if m:
            spaet.append(('auf', m.group(1), m.group(2), m.group(3), m.group(4))); continue
        m = re.match(r'^(\w+) auf ([A-Z])([A-Z])$', t)   # „Badestelle auf FR“
        if m:
            spaet.append(('auf', m.group(1), m.group(2), m.group(3), None)); continue
        m = re.match(r'^([A-Z]) bis (\w+) (\d.*)$', t) or re.match(r'^(\w+) bis ([A-Z]) (\d.*)$', t)
        if m:
            spaet.append(('mass', m.group(1), m.group(2), m.group(3))); continue
        m = re.match(r'^(?:Diagonale )?([A-Z])([A-Z]) = (\d[\d, ]*(?:,\d+)? ?\w*)( gestrichelt)?$', t)
        if m:
            spaet.append(('mass', m.group(1), m.group(2), m.group(3)))
            if t.startswith('Diagonale') or m.group(4):
                spaet.append(('seg', m.group(1), m.group(2), 'dashed' if m.group(4) else ''))
            continue
        m = re.match(r'^([a-z])(?:_\w+)? = (\d.*|[A-Z]{2})$', t)
        if m:
            spaet.append(('klein', m.group(1), m.group(2))); continue
        m = re.match(r'^(?:Winkel )?' + WINKELLAB + r' bei ([A-Z])(?: und bei ([A-Z]))?$', t)
        if m:
            spaet.append(('w', m.group(2), m.group(1)))
            if m.group(3):
                spaet.append(('w', m.group(3), m.group(1)))
            continue
        m = re.match(r'^' + WINKELLAB + r' und ' + WINKELLAB + r' bei ([A-Z])$', t)
        if m:
            spaet.append(('w2', m.group(3), m.group(1), m.group(2))); continue
        m = re.match(r'^(?:Winkel )?∠([A-Z])([A-Z])([A-Z]) = ' + WINKELLAB + r'(?: bei [A-Z])?$', t)
        if m:
            spaet.append(('wx', m.group(2), m.group(1), m.group(3), m.group(4))); continue
        m = re.match(r'^' + WINKELLAB + r' = ∠([A-Z])([A-Z])([A-Z])$', t)
        if m:
            spaet.append(('wx', m.group(3), m.group(2), m.group(4), m.group(1))); continue
        m = re.match(r'^bei ([A-Z]) ' + WINKELLAB + r' \((links|rechts)\) und ' + WINKELLAB + r' \((links|rechts)\)$', t)
        if m:
            spaet.append(('wlr', m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))); continue
        m = re.match(r'^' + WINKELLAB + r' bei ([A-Z]) zwischen ([A-Z])([A-Z]) und (?:([A-Z])([A-Z])|\$h_(\w)\$)$', t)
        if m:
            q2 = m.group(6) or ('_h' if m.group(7) else '')
            spaet.append(('wx', m.group(2), m.group(4), q2, m.group(1))); continue
        m = re.match(r'^rechter Winkel bei ([A-Z])$', t)
        if m:
            spaet.append(('recht', m.group(1))); continue
        m = re.match(r'^Diagonalen ([A-Z])([A-Z]) und ([A-Z])([A-Z]) mit (?:rechtem Winkel im )?Schnittpunkt ([A-Z])$', t)
        if m:
            spaet.append(('diag', m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))
            if 'rechtem Winkel' in t:
                spaet.append(('recht', m.group(5)))
            continue
        m = re.match(r'^(?:Diagonalen )?([A-Z])([A-Z]) (waagerecht|senkrecht)$', t)
        if m:
            spaet.append(('seg', m.group(1), m.group(2), '')); continue
        m = re.match(r'^Schnittpunkt ([A-Z]) mit rechtem Winkel$', t)
        if m:
            spaet.append(('diag2', m.group(1))); spaet.append(('recht', m.group(1))); continue
        m = re.match(r'^Höhe \$h_(\w)\$ gestrichelt von ([A-Z]) nach ([A-Z]) auf ([A-Z])([A-Z])$', t)
        if m:
            spaet.append(('lot', m.group(2), m.group(3), m.group(4), m.group(5), '$h_' + m.group(1) + '$')); continue
        m = re.match(r'^(\$?h\$?) gestrichelt von ([A-Z]) nach ([A-Z])$', t)
        if m:
            spaet.append(('lot', m.group(2), m.group(3), None, None, '$h$')); continue
        m = re.match(r'^([A-Z])([A-Z]) mit rechtem Winkel bei ([A-Z])$', t)
        if m:
            spaet.append(('lot', m.group(1) if m.group(2) == m.group(3) else m.group(2), m.group(3), None, None, '', '')); continue
        m = re.match(r'^([A-Z])([A-Z]) bis ([A-Z]) verlängert$', t)
        if m:
            spaet.append(('verl', m.group(1), m.group(2), m.group(3))); continue
        m = re.match(r'^([A-Z])([A-Z])(?: und ([A-Z])([A-Z]))? gestrichelt$', t)
        if m:
            spaet.append(('seg', m.group(1), m.group(2), 'dashed'))
            if m.group(3):
                spaet.append(('seg', m.group(3), m.group(4), 'dashed'))
            continue
        m = re.match(r'^Dreieck ([A-Z])([A-Z])([A-Z]) (schraffiert|grau)$', t)
        if m:
            spaet.append(('flaeche', [m.group(1), m.group(2), m.group(3)], m.group(4))); continue
        m = re.match(r'^([A-Z]) ' + LAGEWORT + r'$', t.replace(', verbunden mit', ''))
        m2 = re.match(r'^verbunden mit ([A-Z]) und ([A-Z])$', t)
        if m2 and letzte:
            spaet.append(('seg', letzte, m2.group(1), '')); spaet.append(('seg', letzte, m2.group(2), '')); continue
        m = re.match(r'^senkrechte (\w+) von ([A-Z]) auf ([A-Z])([A-Z]) \(nahe ([A-Z])\) bis zur Schräge ([A-Z])([A-Z])$', t)
        if m:
            spaet.append(('wand', m.group(2), m.group(3), m.group(4), m.group(5), m.group(6), m.group(7))); continue
        m = re.match(r'^(\d+(?:,\d+)? ?\w+) hoch$', t)
        if m:
            spaet.append(('wandmass', m.group(1))); continue
        if t in ('nach rechts geneigt',):
            spaet.append(('neig',)); continue
        offen.append(t)
    alle = list(lagen.values())
    reihe = []
    for t in teile:
        for p in re.findall(r'(?<![A-Za-z∠])([A-Z])(?![A-Za-z(])', t.split(' = ')[0] if '∠' not in t else ''):
            if p not in reihe and (p in lagen or any(p == r_[0] for r_ in rel)):
                reihe.append(p)
    for p, w in lagen.items():
        S.P[p] = _lage(w, alle)
    for _ in range(4):
        for p, w, q in rel:
            if q in S.P and p not in S.P:
                x, y = S.P[q]
                S.P[p] = {'auf': (x, y + 3.5), 'ab': (x, y - 3.5), 'rechts': (x + 6, y), 'links': (x - 6, y)}[w]
    # Hauptfigur: Dreieck = erste drei Ecken der Beschreibung, Viereck = ABCD (bzw. Reihenfolge der Nennung)
    eck = [p for p in reihe if p in S.P] + [p for p in S.P if len(p) == 1 and p not in reihe]
    if art == 'Viereck' and len(eck) >= 4:
        S.poly = sorted(eck)[:4]
    else:
        S.poly = eck[:3]
    for x in spaet:
        if x[0] == 'neig':
            for p in S.poly:
                if S.P[p][1] > 1.75:
                    S.P[p] = (S.P[p][0] + 2.4, S.P[p][1])
    # Punkte auf Seiten, Diagonalen, Lote
    wand = None
    for x in spaet:
        if x[0] == 'auf' and x[2] in S.P and x[3] in S.P:
            A, B = S.P[x[2]], S.P[x[3]]
            t = 0.2 if x[4] == x[2] else 0.8 if x[4] == x[3] else 0.5
            mm = [y for y in spaet if y[0] == 'mass' and x[1] in (y[1], y[2])]
            if len(mm) == 2:
                try:
                    a_ = _z(re.match(r'[\d,]+', mm[0][3]).group(0)) * (1000 if 'km' in mm[0][3] else 1)
                    b_ = _z(re.match(r'[\d,]+', mm[1][3]).group(0)) * (1000 if 'km' in mm[1][3] else 1)
                    t = a_ / (a_ + b_) if x[2] in (mm[0][1], mm[0][2]) else b_ / (a_ + b_)
                except Exception:
                    pass
            S.P[x[1]] = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
            S.auf[x[1]] = (x[2], x[3])
            S.punkte.append(x[1])
        elif x[0] == 'verl' and x[1] in S.P and x[2] in S.P:
            A, B = S.P[x[1]], S.P[x[2]]
            S.P[x[3]] = (B[0] + 0.35 * (B[0] - A[0]), B[1] + 0.35 * (B[1] - A[1]))
            S.auf[x[3]] = (x[1], x[2])
            S.seg.append((x[2], x[3], ''))
        elif x[0] == 'diag' and all(p in S.P for p in x[1:5]):
            S.P[x[5]] = _schnitt(S.P[x[1]], S.P[x[2]], S.P[x[3]], S.P[x[4]])
            S.seg += [(x[1], x[5], ''), (x[5], x[2], ''), (x[3], x[5], ''), (x[5], x[4], '')]
        elif x[0] == 'wand':
            wand = x
    for x in spaet:
        if x[0] == 'diag2':
            dg = [(y[1], y[2]) for y in spaet if y[0] == 'seg' and y[3] == '']
            if len(dg) >= 2 and all(p in S.P for p in dg[0] + dg[1]):
                S.P[x[1]] = _schnitt(S.P[dg[0][0]], S.P[dg[0][1]], S.P[dg[1][0]], S.P[dg[1][1]])
                for a, b in dg[:2]:
                    S.seg += [(a, x[1], ''), (x[1], b, '')]
                spaet = [y for y in spaet if not (y[0] == 'seg' and (y[1], y[2]) in dg[:2])]
        if x[0] == 'lot':
            von, fuss = x[1], x[2]
            if von not in S.P:
                continue
            if x[3]:
                S.P[fuss] = _proj(S.P[von], S.P[x[3]], S.P[x[4]])
                S.auf[fuss] = (x[3], x[4])
            elif fuss in S.auf:
                a, b = S.auf[fuss]
                S.P[fuss] = _proj(S.P[von], S.P[a], S.P[b])
            elif fuss in S.P:
                pass
            else:
                continue
            S.seg.append((von, fuss, 'dashed' if x[5] or len(x) == 6 else ''))
            if len(x) == 7:
                S.seg[-1] = (von, fuss, '')
            if x[5]:
                S.seite[frozenset((von, fuss))] = x[5]
            nb = S.auf.get(fuss, (None, None))[0]
            if nb and nb in S.P and abs(S.P[nb][0] - S.P[fuss][0]) + abs(S.P[nb][1] - S.P[fuss][1]) > 1e-6:
                S.winkel.append((fuss, von, nb, '', True))
            elif S.auf.get(fuss) and S.auf[fuss][1] in S.P:
                S.winkel.append((fuss, von, S.auf[fuss][1], '', True))
    if wand:
        _, p, a, b, nahe, c1, c2 = wand
        A, B = S.P.get(a), S.P.get(b)
        if A and B and c1 in S.P and c2 in S.P:
            t = 0.8 if nahe == b else 0.2
            S.P[p] = (A[0] + t * (B[0] - A[0]), A[1] + t * (B[1] - A[1]))
            q = _schnitt(S.P[p], (S.P[p][0], S.P[p][1] + 1), S.P[c1], S.P[c2])
            S.P['_w'] = q
            S.seg.append((p, '_w', 'line width=1.2pt'))
            S.winkel.append((p, '_w', a, '', True))
            for y in spaet:
                if y[0] == 'wandmass':
                    S.seite[frozenset((p, '_w'))] = y[1]
    for x in spaet:
        if x[0] == 'seg' and x[1] in S.P and x[2] in S.P:
            if not any({a, b} == {x[1], x[2]} for a, b, _ in S.seg):
                S.seg.append((x[1], x[2], x[3]))
        elif x[0] == 'mass' and x[1] in S.P and x[2] in S.P:
            S.seite[frozenset((x[1], x[2]))] = x[3]
        elif x[0] == 'klein':
            gr = x[1].upper()
            andere = [p for p in S.poly if p != gr]
            if len(S.poly) == 3 and gr in S.poly:
                S.seite[frozenset(andere)] = x[1] + (' = ' + x[2] if re.match(r'\d', x[2]) else '')
            else:
                offen.append('klein ' + x[1])
        elif x[0] == 'flaeche':
            S.flaechen.append((x[1], x[2]))
    for x in spaet:
        if x[0] == 'recht' and x[1] in S.P:
            st = S.strahlen(x[1])
            if len(st) >= 2:
                st = sorted(st, key=lambda q: math.atan2(S.P[q][1] - S.P[x[1]][1], S.P[q][0] - S.P[x[1]][0]))
                if not any(w[0] == x[1] and w[4] for w in S.winkel):
                    S.winkel.append((x[1], st[0], st[1], '', True))
        elif x[0] == 'w' and x[1] in S.P:
            st = S.strahlen(x[1])
            if x[1] in S.poly:
                i = S.poly.index(x[1])
                st = [S.poly[i - 1], S.poly[(i + 1) % len(S.poly)]]
            if len(st) >= 2:
                S.winkel.append((x[1], st[0], st[1], x[2], False))
            else:
                offen.append('Winkel bei ' + x[1])
        elif x[0] == 'wx':
            q2 = x[3]
            if q2 == '_h':
                q2 = next((b for a, b, s in S.seg if a == x[1] and s == 'dashed'), '')
            if x[1] in S.P and x[2] in S.P and q2 in S.P:
                S.winkel.append((x[1], x[2], q2, x[4], False))
            else:
                offen.append('Winkel ' + x[4])
        elif x[0] in ('w2', 'wlr') and x[1] in S.P:
            st = sorted(S.strahlen(x[1]), key=lambda q: math.atan2(S.P[q][1] - S.P[x[1]][1], S.P[q][0] - S.P[x[1]][0]))
            if len(st) < 3:
                offen.append('zwei Winkel bei ' + x[1]); continue
            # die drei Strahlen im Innern: zwei Teilwinkel nebeneinander
            sx, sy = S.P[x[1]]
            wl = lambda q: math.degrees(math.atan2(S.P[q][1] - sy, S.P[q][0] - sx)) % 360
            st = sorted(st, key=wl)
            paare = [(st[i], st[(i + 1) % len(st)]) for i in range(len(st))]
            paare = [p for p in paare if (wl(p[1]) - wl(p[0])) % 360 < 180][:2]
            paare.sort(key=lambda p: math.cos(math.radians(wl(p[0]) + ((wl(p[1]) - wl(p[0])) % 360) / 2)))   # links zuerst
            if x[0] == 'w2':
                labs = [x[2], x[3]]
            else:
                labs = [x[2], x[4]] if x[3] == 'links' else [x[4], x[2]]
            for (a, b), lab in zip(paare, labs):
                S.winkel.append((x[1], a, b, lab, False))
    return S, offen


def skizze_rechtwinklig(d):
    """Rechtwinkliges Dreieck ohne Eckennamen: Lage des rechten Winkels, Seiten nach Richtung."""
    rest = d.split(':', 1)[1]
    S = Skizze(); S.namen = False
    S.nicht_mass = 'nicht maßstabsgerecht' in rest
    rest = re.sub(r';?\s*nicht maßstabsgerecht', '', rest)
    teile = []
    for t in _oben_teile(rest, '; '):
        teile += _oben_teile(t, ', ')
    m = re.match(r'rechter Winkel (unten links|unten rechts|oben links|oben rechts|an der oberen Ecke)', teile[0])
    if not m:
        return None, teile
    lage = m.group(1)
    if lage == 'an der oberen Ecke':
        S.P = {'ul': (0, 0), 'ur': (6, 0), 'sp': (2.2, 2.65)}
        recht = 'sp'
    else:
        ecke = {'unten links': (0, 0), 'unten rechts': (6, 0), 'oben links': (0, 3.2), 'oben rechts': (6, 3.2)}[lage]
        x0, y0 = ecke
        S.P = {'r': ecke, 'w': (6 - x0, y0), 's': (x0, 3.2 - y0)}
        recht = 'r'
    S.poly = list(S.P)
    seiten = {}
    if recht == 'r':
        seiten = {'waagerecht': ('r', 'w'), 'senkrecht': ('r', 's'), 'hyp': ('w', 's')}
    else:
        seiten = {'hyp': ('ul', 'ur'), 'links': ('ul', 'sp'), 'rechts': ('sp', 'ur')}
    ecken = {'unten rechts': None, 'unten links': None}
    for P, (x, y) in S.P.items():
        lw = ('unten ' if y < 1 else 'oben ') + ('links' if x < 1 else 'rechts' if x > 5 else 'mitte')
        ecken[lw] = P
    S.winkel.append((recht, *[p for p in S.poly if p != recht], '', True))
    offen = []
    zw = re.search(r'zwischen (\S+) \((\w+)\) und (\S+) \((\w+)\)', teile[0])
    if zw:
        for lab, wo in ((zw.group(1), zw.group(2)), (zw.group(3), zw.group(4))):
            k = {'unten': 'waagerecht', 'oben': 'waagerecht', 'rechts': 'senkrecht', 'links': 'senkrecht'}[wo] \
                if recht == 'r' else wo
            seiten_lab(S, seiten[k], lab)
    for t in teile[1:]:
        t = t.strip()
        m = re.match(r'^(senkrechte|waagerechte) Kathete (\S+)(?: \((links|rechts)\))?$', t)
        if m:
            if m.group(2) != 'unbeschriftet':
                seiten_lab(S, seiten[m.group(1)[:-1]], m.group(2))
            continue
        m = re.match(r'^Kathete (\S+) (waagerecht|senkrecht)(?: (unten|oben|links|rechts))?$', t)
        if m:
            seiten_lab(S, seiten[m.group(2)], m.group(1)); continue
        m = re.match(r'^Hypotenuse (\S+)(?: (waagerecht unten|unten|links oben|rechts oben))?$', t)
        if m:
            seiten_lab(S, seiten['hyp'], m.group(1)); continue
        m = re.match(r'^Seite (\S+) von (?:links unten zur Spitze|der Spitze nach rechts unten)$', t)
        if m:
            seiten_lab(S, seiten['links' if 'links unten' in t else 'rechts'], m.group(1)); continue
        m = re.match(r'^(?:Winkel )?' + WINKELLAB + r' (unten links|unten rechts|an der oberen Ecke)(?: zwischen \S+ und \S+)?$', t)
        if m:
            wo = m.group(2)
            P = next((p for p, (x, y) in S.P.items() if (y > 1) == (wo == 'an der oberen Ecke')
                      and (wo == 'an der oberen Ecke' or (x < 1) == (wo == 'unten links'))), None)
            if not P or P == recht:
                offen.append(t); continue
            nb = [q for q in S.poly if q != P]
            S.winkel.append((P, nb[0], nb[1], m.group(1), False)); continue
        offen.append(t)
    return S, offen


def seiten_lab(S, paar, lab):
    S.seite[frozenset(paar)] = lab if lab.startswith('$') or not re.fullmatch(r'[a-z]', lab) else '$' + lab + '$'


def abb_trapez_u_a(d):
    """Vierecke ohne Eckennamen (Trapez, Parallelogramm, Quadrat, Rechteck, gleichschenkliges Trapez)."""
    m = re.match(r'Viereck \(([^)]*)\):\s*(.*)$', d)
    art, rest = m.group(1), m.group(2)
    S = Skizze(); S.namen = False
    S.nicht_mass = 'nicht maßstabsgerecht' in rest
    rest = re.sub(r';?\s*nicht maßstabsgerecht', '', rest)
    teile = []
    for t in _oben_teile(rest, '; '):
        teile += _oben_teile(t, ', ')
    tx_ = ' ; '.join(teile)
    offen = []
    E = lambda: S.P
    if art == 'Quadrat':
        S.P = {'ul': (0, 0), 'ur': (2.5, 0), 'or': (2.5, 2.5), 'ol': (0, 2.5)}
        S.poly = list(S.P)
        if 'grau' in tx_:
            S.fuellung = 'grau'
        return S, [t for t in teile if t != 'grau gefüllt']
    if art == 'Rechteck':
        S.P = {'ul': (0, 0), 'ur': (6, 0), 'or': (6, 3), 'ol': (0, 3)}
        S.poly = list(S.P)
        for t in teile:
            m = re.match(r'^(unten|oben|rechts|links) (\$?[a-z]\$?)(?: = (.*))?$', t) or \
                re.match(r'^Breite (\$?[a-z]\$?) (unten|oben)$', t)
            if t == 'liegend':
                continue
            if m and m.re.pattern.startswith('^Breite'):
                seiten_lab(S, ('ul', 'ur') if m.group(2) == 'unten' else ('ol', 'or'), m.group(1)); continue
            if m:
                wo = m.group(1)
                paar = {'unten': ('ul', 'ur'), 'oben': ('ol', 'or'), 'rechts': ('ur', 'or'), 'links': ('ul', 'ol')}[wo]
                seiten_lab(S, paar, m.group(2) if not m.group(3) else f'{m.group(2)} = {m.group(3)}'); continue
            if t == 'durch eine senkrechte Linie geteilt':
                S.P['mu'], S.P['mo'] = (2.6, 0), (2.6, 3)
                S.seg.append(('mu', 'mo', '')); continue
            mm = re.match(r'^(linker|rechter) Teil (grau|kariert) mit Breite (\$?[a-z]\$?)$', t)
            if mm and 'mu' in S.P:
                pts = ['ul', 'mu', 'mo', 'ol'] if mm.group(1) == 'linker' else ['mu', 'ur', 'or', 'mo']
                S.flaechen.append((pts, mm.group(2)))
                seiten_lab(S, (pts[0], pts[1]), mm.group(3)); continue
            mm = re.match(r'^gemeinsame Höhe (\$?[a-z]\$?) rechts$', t)
            if mm:
                seiten_lab(S, ('ur', 'or'), mm.group(1)); continue
            mm = re.match(r'^durch eine waagerechte Linie in einen oberen Streifen der Höhe (\w) und einen unteren Teil der Höhe (\w) geteilt \(\w, \w rechts\)$', t)
            if mm:
                S.P['ml'], S.P['mr'] = (0, 2.1), (6, 2.1)
                S.seg.append(('ml', 'mr', ''))
                seiten_lab(S, ('mr', 'or'), mm.group(1)); seiten_lab(S, ('ur', 'mr'), mm.group(2))
                S.seite.pop(frozenset(('ur', 'or')), None); continue
            offen.append(t)
        return S, offen
    if art == 'Parallelogramm':
        S.P = {'ul': (0, 0), 'ur': (5, 0), 'or': (6.4, 2.4), 'ol': (1.4, 2.4)}
        S.poly = list(S.P)
        for t in teile:
            if t in ('lange Seiten waagerecht', 'nach rechts geneigt'):
                continue
            m = re.match(r'^' + WINKELLAB + r' (unten links|unten rechts|oben links|oben rechts)$', t)
            if m:
                ecke = {'unten links': 'ul', 'unten rechts': 'ur', 'oben links': 'ol', 'oben rechts': 'or'}[m.group(2)]
                i = S.poly.index(ecke)
                S.winkel.append((ecke, S.poly[i - 1], S.poly[(i + 1) % 4], m.group(1), False)); continue
            offen.append(t)
        return S, offen
    if 'Trapez' in art:
        unten = oben = None
        h = 2.6
        wl = wr = None   # Innenwinkel unten links/rechts
        recht_unten = False
        hoehe_lab = ''
        for t in teile:
            m = re.match(r'^parallele Seiten (\S+ \w+) \(oben\) und (\S+ \w+) \(unten\)$', t)
            if m:
                oben, unten = m.group(1), m.group(2); continue
            m = re.match(r'^(unten|oben) (\d\S* \w+)$', t)
            if m:
                if m.group(1) == 'unten':
                    unten = m.group(2)
                else:
                    oben = m.group(2)
                continue
            m = re.match(r'^Grundseite (\S+ \w+) unten$', t)
            if m:
                unten = m.group(1); continue
        L = lambda s: _z(re.match(r'[\d,]+', s).group(0)) if s and re.match(r'[\d,]+', s) else None
        S.P = {}
        if art == 'Trapez' and re.search(r'rechte Winkel unten', tx_):
            # rechtwinkliges Trapez: Grundseite unten, linke und rechte Seite senkrecht
            S.P = {'ul': (0, 0), 'ur': (6, 0), 'or': (6, 3.6), 'ol': (0, 1.6)}
            S.poly = ['ul', 'ur', 'or', 'ol']
            for t in teile:
                m = re.match(r'^(linke|rechte) Seite (\S+ \w+)$', t)
                if m:
                    seiten_lab(S, ('ul', 'ol') if m.group(1) == 'linke' else ('ur', 'or'), m.group(2)); continue
                if re.match(r'^Grundseite', t):
                    seiten_lab(S, ('ul', 'ur'), unten); continue
                if t == 'rechte Winkel unten':
                    S.winkel += [('ul', 'ur', 'ol', '', True), ('ur', 'ul', 'or', '', True)]; continue
                if t == 'schräge Oberseite':
                    continue
                if t == 'gestrichelte Waagerechte von der linken oberen Ecke zur rechten Seite':
                    S.P['_g'] = (6, 1.6); S.seg.append(('ol', '_g', 'dashed')); continue
                m = re.match(r'^' + WINKELLAB + r' oben rechts$', t)
                if m:
                    S.winkel.append(('or', 'ol', 'ur', m.group(1), False)); continue
                offen.append(t)
            return S, offen
        # allgemeines Trapez: Form aus Längen und Winkeln
        lu, lo = L(unten), L(oben)
        winkel_lab = {}
        for t in teile:
            m = re.match(r'^(?:Innenwinkel )?(.*)$', t)
            for it in re.findall(WINKELLAB + r' (unten links und unten rechts|unten links|unten rechts|oben links|oben rechts)', t):
                lab, wo = it
                for w in (['unten links', 'unten rechts'] if 'und' in wo else [wo]):
                    winkel_lab[w] = lab
        for wo, lab in winkel_lab.items():
            if re.match(r'\d', lab):
                v = _z(lab.rstrip('°'))
                if wo == 'unten links': wl = v
                if wo == 'unten rechts': wr = v
                if wo == 'oben links': wl = 180 - v
                if wo == 'oben rechts': wr = 180 - v
        lang_oben = bool(re.search(r'lange Seite oben', tx_)) or (lu and lo and lo > lu)
        sym = 'symmetrisch' in tx_ or 'gleichschenklig' in art or (wl is None and wr is None)
        if lu and lo:
            k = 6.0 / max(lu, lo)
            bu, bo = lu * k, lo * k
            mh = re.search(r'Höhe (\d[\d,]*) ?\w+', tx_)
            if mh:
                h = L(mh.group(1)) * k
            elif re.search(r'Schenkel (\d[\d,]*)', tx_):
                sch = L(re.search(r'Schenkel (\d[\d,]*)', tx_).group(1)) * k
                h = math.sqrt(max(0.5, sch ** 2 - ((bu - bo) / 2) ** 2))
            dl = (bu - bo) / 2 if sym else (bu - bo) / 2
        else:
            bu, bo = (6.0, 3.2) if not lang_oben else (3.2, 6.0)
            if wl is not None and wr is not None:
                # Form aus den Winkeln: lange Seite 6, Höhe 2.4
                h = 2.4
                cl, cr = 1 / math.tan(math.radians(wl)), 1 / math.tan(math.radians(wr))
                if lang_oben:   # Winkel unten > 90°: Schenkel laufen nach außen
                    bo = 6.0
                    if bo + h * (cl + cr) < 2.6:
                        h = (bo - 2.6) / -(cl + cr)
                    bu = bo + h * (cl + cr)
                    dl = -h * cl
                else:
                    bu = 6.0; bo = bu - h * (cl + cr)
                    dl = h * cl
            dl = None if wl is None or wr is None else dl
            if dl is None:
                dl = (bu - bo) / 2
        if lang_oben:
            S.P = {'ul': (0, 0), 'ur': (bu, 0), 'or': (bo + (-dl if dl < 0 else 0) - (0 if dl < 0 else 0), h), 'ol': (0, h)}
            # obere Seite länger: unten eingerückt
            x0 = -dl if dl < 0 else (bo - bu) / 2
            S.P = {'ol': (0, h), 'or': (bo, h), 'ur': (x0 + bu, 0), 'ul': (x0, 0)}
        else:
            S.P = {'ul': (0, 0), 'ur': (bu, 0), 'or': (dl + bo, h), 'ol': (dl, h)}
        S.poly = ['ul', 'ur', 'or', 'ol']
        if 'grau' in tx_:
            S.fuellung = 'grau'
        for t in teile:
            if re.match(r'^(parallele Seiten|unten \d|oben \d|lange Seite|kurze Seite|symmetrisch|grau gefüllt)', t):
                if t.startswith('parallele Seiten') or re.match(r'^(unten|oben) \d', t):
                    if unten: seiten_lab(S, ('ul', 'ur'), unten)
                    if oben: seiten_lab(S, ('ol', 'or'), oben)
                continue
            m = re.match(r'^Höhe (\S+(?: \w+)?)(?: gestrichelt| mit rechten Winkeln)?$', t)
            if m:
                lab = m.group(1) if not re.fullmatch(r'[a-z]', m.group(1)) else '$' + m.group(1) + '$'
                fx = max(S.P['ol'][0], S.P['ul'][0])
                S.P['_hu'], S.P['_ho'] = (fx, 0), (fx, h)
                S.seg.append(('_ho', '_hu', 'dashed'))
                S.seite[frozenset(('_ho', '_hu'))] = lab
                S.winkel.append(('_hu', '_ho', 'ur', '', True))
                continue
            m = re.match(r'^Schenkel (\S+ \w+)$', t)
            if m:
                seiten_lab(S, ('ur', 'or'), m.group(1)); continue
            if re.search(WINKELLAB + r' (unten links|unten rechts|oben links|oben rechts)', t):
                continue
            offen.append(t)
        for wo, lab in winkel_lab.items():
            ecke = {'unten links': 'ul', 'unten rechts': 'ur', 'oben links': 'ol', 'oben rechts': 'or'}[wo]
            i = S.poly.index(ecke)
            S.winkel.append((ecke, S.poly[i - 1], S.poly[(i + 1) % 4], lab, False))
        return S, offen
    return None, teile


def abb_geometrie(d, D, iid, typ):
    try:
        if typ == 'rechtwinkliges Dreieck' and re.search(r'waagerechte Kathete \d', d):
            return abb_dreieck(d)   # Prozent-Fassung (byte-gleich)
        if typ == 'rechtwinkliges Dreieck' and re.match(r'rechtwinkliges Dreieck: rechter Winkel (unten|oben|an der)', d):
            S, offen = skizze_rechtwinklig(d)
        elif typ == 'Viereck' and not re.search(r'\b[A-D] (links|rechts|oben|unten|senkrecht)', d):
            S, offen = abb_trapez_u_a(d)
        else:
            S, offen = skizze_benannt(d, 'Viereck' if typ == 'Viereck' else '')
    except Exception as e:   # Beschreibung passt nicht ins Muster
        return None, [f'Fehler {type(e).__name__}: {e}']
    if S is None or len(S.poly) < 3 or offen:
        return None, offen
    return S.tex(), []


# ===========================================================================
# Körper (Schrägbild), Netze, zusammengesetzte Figur (Lauf C)
# Schrägbild: Kavalierperspektive (Tiefe 45°, halbe Länge); Rundkörper mit Ellipse.
# ===========================================================================
def _ellipse(cx, cy, rx, ry, vorn_voll=True, hinten='dashed'):
    return (r'\draw (%.2f,%.2f) arc (180:360:%.2f and %.2f);' % (cx - rx, cy, rx, ry) +
            r'\draw[%s] (%.2f,%.2f) arc (0:180:%.2f and %.2f);' % (hinten, cx + rx, cy, rx, ry))


def _mass(p, q, lab, seite='left'):
    return r'\path (%.2f,%.2f) -- node[font=\scriptsize,%s] {%s} (%.2f,%.2f);' % (p[0], p[1], seite, tx(lab), q[0], q[1])


def abb_schraegbild(d, D, iid):
    rest = d.split(':', 1)[1].strip()
    nm = 'nicht maßstabsgerecht' in rest
    rest = re.sub(r';?\s*nicht maßstabsgerecht\.?', '', rest)
    if '. Netz' in rest:
        return None   # Schrägbild und Netz in einer Zeile (2020-OS-K5a): Rahmen
    grau = 'grau' in rest
    out = [r'\begin{tikzpicture}[line width=0.6pt,baseline=(current bounding box.north)]']
    def labs(s):
        return dict(re.findall(r'\b(h|r|s|[a-z]) = (\d+(?:,\d+)? ?\w+)', s))
    L = labs(rest)
    if re.search(r'Zylinder', rest) and re.search(r'Kegel', rest):
        rx, ry, h, hk = 1.0, 0.3, 2.6, 1.3
        out.append(_ellipse(0, 0, rx, ry))
        out.append(r'\draw (-%s,0) -- (-%s,%s); \draw (%s,0) -- (%s,%s);' % (rx, rx, h, rx, rx, h))
        out.append(_ellipse(0, h, rx, ry))
        out.append(r'\draw (-%s,%s) -- (0,%s) -- (%s,%s);' % (rx, h, h + hk, rx, h))
        out.append(r'\draw[dashed] (0,%s) -- (%s,%s);' % (h, rx, h))
        hl = ('$h$ = ' + L['h']) if 'h' in L else '$h$'
        rl = ('$r$ = ' + L['r']) if 'r' in L else '$r$'
        sl = ('$s$ = ' + L['s']) if 's' in L else '$s$'
        out.append(r'\node[font=\scriptsize,right] at (%s,%s) {%s};' % (rx, h / 2, hl))
        out.append(r'\node[font=\scriptsize,below,fill=white,inner sep=1pt] at (%s,%s) {%s};' % (rx / 2, h - 0.08, rl))
        out.append(r'\node[font=\scriptsize,right] at (%s,%s) {%s};' % (rx / 2 + 0.05, h + hk / 2 + 0.1, sl))
    elif re.search(r'Zylinder', rest):
        rx, ry, h = 1.1, 0.33, 2.4
        liegend = False
        if grau:
            out.append(r'\fill[black!15] (-%s,0) arc (180:360:%s and %s) -- (%s,%s) arc (0:-180:%s and %s) -- cycle;'
                       % (rx, rx, ry, rx, h, rx, ry))
        out.append(_ellipse(0, 0, rx, ry))
        out.append(r'\draw (-%s,0) -- (-%s,%s); \draw (%s,0) -- (%s,%s);' % (rx, rx, h, rx, rx, h))
        out.append(r'\draw (0,%s) ellipse (%s and %s);' % (h, rx, ry))
        if 'Reifen' in rest:
            for y in (0.7, 1.7):
                out.append(r'\draw (-%s,%s) arc (180:360:%s and %s);' % (rx, y, rx, ry))
        if 'Stab' in rest:
            out.append(r'\draw[line width=1.6pt] (-%.2f,%.2f) -- (%.2f,%.2f);' % (rx * 0.9, -0.15, rx * 1.25, h + 0.75))
        if 'Maße' not in rest and 'ohne Maße' not in rest and ('h' in L or 'r' in L):
            pass
    elif re.search(r'Kegel', rest):
        rx, ry, h = 1.2, 0.36, 2.4
        if grau:
            out.append(r'\fill[black!15] (0,0) ellipse (%s and %s);' % (rx, ry))
        out.append(_ellipse(0, 0, rx, ry))
        out.append(r'\draw (-%s,0) -- (0,%s) -- (%s,0);' % (rx, h, rx))
        if 'Pfeil' in rest:
            mm = re.search(r'Pfeil „([^“]*)“', rest)
            out.append(r'\draw[-{Stealth[length=2mm]},line width=0.4pt] (1.9,1.9) node[right,font=\scriptsize] {%s} -- (0.5,1.4);'
                       % tx(mm.group(1) if mm else ''))
    elif re.search(r'Pyramide', rest):
        a, t = 2.4, 0.9
        P = [(0, 0), (a, 0), (a + t, t), (t, t)]
        sp = ((a + t) / 2, 2.6)
        out.append(r'\draw (0,0) -- (%s,0) -- (%s,%s);' % (a, a + t, t))
        out.append(r'\draw[dashed] (%s,%s) -- (%s,%s) -- (0,0); \draw[dashed] (%s,%s) -- (%s,%s);'
                   % (a + t, t, t, t, t, t, sp[0], sp[1]))
        for p in ((0, 0), (a, 0), (a + t, t)):
            out.append(r'\draw (%s,%s) -- (%s,%s);' % (p[0], p[1], sp[0], sp[1]))
    elif re.search(r'Quader', rest):
        b, h, t = 1.6, 2.8, 0.8
        out.append(r'\draw (0,0) rectangle (%s,%s); \draw (0,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,0);'
                   % (b, h, h, t, h + t, b + t, h + t, b, h, b))
        out.append(r'\draw (%s,%s) -- (%s,%s) -- (%s,0);' % (b + t, h + t, b + t, t, b))
        out.append(r'\draw[dashed] (0,0) -- (%s,%s) -- (%s,%s); \draw[dashed] (%s,%s) -- (%s,%s);'
                   % (t, t, b + t, t, t, t, t, h + t))
    elif re.search(r'prisma', rest, re.I):
        mm = re.search(r'Trapez oben (\d+), unten (\d+), Schenkel (\d+), Trapezhöhe (\w+); Prismenhöhe (\d+) \(Maße in (\w+)\)', rest)
        if mm:
            # stehendes Prisma, Trapez als Grund- und Deckfläche (Kavalier)
            o, u, s_, hl, H, e = mm.groups()
            k = 3.0 / max(int(o), int(u))
            bo, bu = int(o) * k, int(u) * k
            tq = 0.9
            def trapez(y):
                return [(-bo / 2, y + tq), (bo / 2, y + tq), (bu / 2, y), (-bu / 2, y)]
            Hh = 2.8
            G, Dk = trapez(0), trapez(Hh)
            out.append(r'\draw %s -- cycle;' % ' -- '.join('(%.2f,%.2f)' % p for p in Dk))
            out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);' % (*G[1], *G[2], *G[3], *G[0]))
            out.append(r'\draw[dashed] (%.2f,%.2f) -- (%.2f,%.2f);' % (*G[0], *G[1]))
            for i in range(4):
                out.append(r'\draw%s (%.2f,%.2f) -- (%.2f,%.2f);' % ('[dashed]' if i == 0 else '', *G[i], *Dk[i]))
            out.append(_mass(Dk[0], Dk[1], o, 'above'))
            out.append(_mass(G[3], G[2], u, 'below'))
            out.append(_mass(Dk[2], Dk[1], s_, 'right'))
            out.append(_mass(G[2], Dk[2], H, 'right'))
            out.append(r'\node[font=\scriptsize,mbgrau,anchor=north west] at (-2,-0.4) {Maße in %s};' % e)
        elif re.search(r'liegendes (dreiseitiges Prisma|Dreiecksprisma)', rest):
            A, B, C = (0, 0), (2.2, 0), (0.7, 1.6)
            t = (2.6, 1.0)
            T = lambda p: (p[0] + t[0], p[1] + t[1])
            if 'grau' in rest:
                out.append(r'\fill[black!15] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;' % (*A, *C, *T(C), *T(A)))
                out.append(r'\fill[black!15] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;' % (*B, *C, *T(C), *T(B)))
            out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;' % (*A, *B, *C))
            out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f); \draw[dashed] (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f);'
                       % (*T(C), *T(B), *B, *A, *T(A), *T(B)))
            out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f); \draw[dashed] (%.2f,%.2f) -- (%.2f,%.2f);' % (*C, *T(C), *T(A), *T(C)))
            if 'ABC' in rest:
                for n, p, a in (('A', A, 'south west'), ('B', B, 'north'), ('C', C, 'south east')):
                    out.append(r'\node[font=\small,anchor=%s] at (%.2f,%.2f) {$%s$};' % ('north east' if n == 'A' else a, *p, n))
            ml = re.search(r'Länge (\d+(?:,\d+)? ?\w+)', rest)
            if ml:
                out.append(_mass(B, T(B), ml.group(1), 'below right'))
        elif 'schräge Deckfläche' in rest:
            mm = re.search(r'Grundfläche (\S+) cm × (\S+) cm, vordere Kante (\S+) cm, hintere Kante (\S+) cm, schräge Deckfläche (\S+) cm', rest)
            return None if not mm else None
        else:
            return None
    else:
        return None
    if nm:
        out.append(r'\node[font=\scriptsize,mbgrau,anchor=north west] at ([yshift=-2pt]current bounding box.south west) {nicht maßstabsgerecht};')
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def abb_netz(d, D, iid):
    rest = d.split(':', 1)[1].strip()
    out = [r'\begin{tikzpicture}[line width=0.6pt,baseline=(current bounding box.north)]']
    if rest.startswith('Würfelnetz aus sechs Quadraten'):
        q = 0.8
        # senkrechte Reihe aus drei Quadraten (x=2), links an das mittlere weiß, links daran grau, rechts an das unterste
        felder = [(2, 2, ''), (2, 1, ''), (2, 0, ''), (1, 1, ''), (0, 1, 'grau'), (3, 0, '')]
        for x, y, f in felder:
            out.append(r'\draw%s (%.2f,%.2f) rectangle ++(%s,%s);' % ('[fill=black!30]' if f else '', x * q, y * q, q, q))
    elif rest.startswith('großes Dreieck'):
        A, B, C = (0, 0), (3.2, 0), (1.6, 2.77)
        M = lambda p, r: ((p[0] + r[0]) / 2, (p[1] + r[1]) / 2)
        out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;' % (*A, *B, *C))
        out.append(r'\draw (%.2f,%.2f) -- (%.2f,%.2f) -- (%.2f,%.2f) -- cycle;' % (*M(A, B), *M(B, C), *M(C, A)))
    elif d.startswith('Netz (begonnen) auf Karoraster'):
        m = re.search(r'zwei Rechtecke nebeneinander, je (\d+) Kästchen breit und (\d+) Kästchen hoch; unter dem rechten Rechteck ein gleichseitiges Dreieck mit (\d+) Kästchen Seitenlänge, Spitze nach unten, rechte Seite mit (\w) beschriftet', rest)
        if not m:
            return None
        b, h, s_, lab = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
        k = 0.4
        W, Hh = 2 * b + 2 * b + 2, h + 6 + 2
        out = [r'\begin{tikzpicture}[x=%scm,y=%scm,line width=0.6pt,baseline=(current bounding box.north)]' % (k, k),
               r'\draw[mbgitter,line width=0.3pt,step=1] (0,0) grid (%d,%d);' % (W + 4, Hh)]
        y0 = Hh - h - 1
        x0 = 2
        out.append(r'\draw (%d,%d) rectangle ++(%d,%d); \draw (%d,%d) rectangle ++(%d,%d);' % (x0, y0, b, h, x0 + b, y0, b, h))
        th = s_ * math.sqrt(3) / 2
        out.append(r'\draw (%d,%d) -- (%d,%d) -- (%.2f,%.2f) -- cycle;' % (x0 + b, y0, x0 + 2 * b, y0, x0 + b + s_ / 2, y0 - th))
        out.append(r'\node[font=\small,anchor=west] at (%.2f,%.2f) {$%s$};' % (x0 + b + s_ * 0.8, y0 - th / 2, lab))
    elif d.startswith('Netz (begonnen):'):
        m = re.search(r'zwei senkrechte Rechtecke nebeneinander, links schmal \(Breite (\w)\), rechts breiter \(Breite (\w) = ([^)]*)\), gemeinsame Höhe (\w)', rest)
        if not m:
            return None
        b, c, cw, dd = m.groups()
        W1, W2, H = 1.0, 2.2, 3.0
        out.append(r'\draw (0,0) rectangle (%s,%s); \draw (%s,0) rectangle (%s,%s);' % (W1, H, W1, W1 + W2, H))
        # Trapeze oben und unten am rechten Rechteck, kurze Seite am Rechteck
        out.append(r'\draw (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s);' % (W1, H, W1 - 0.45, H + 1.2, W1 + W2 + 0.45, H + 1.2, W1 + W2, H))
        out.append(r'\draw (%s,0) -- (%s,-1.2) -- (%s,-1.2) -- (%s,0);' % (W1, W1 - 0.45, W1 + W2 + 0.45, W1 + W2))
        out.append(r'\node[font=\scriptsize,below] at (%s,-1.2) {$%s$};' % (W1 + W2 / 2, 'a'))
        out.append(r'\node[font=\scriptsize,above] at (%s,%s) {$%s$};' % (W1 / 2, H, b))
        out.append(r'\node[font=\scriptsize] at (%s,%s) {$%s$ = %s};' % (W1 + W2 / 2, H / 2 + 0.3, c, tx(cw)))
        out.append(r'\node[font=\scriptsize,left] at (0,%s) {$%s$};' % (H / 2, dd))
        if 'Felder' in rest:
            out.append(r'\node[font=\small,anchor=west,align=left] at (%s,%s) {$a$ = \leerzelle\\[3pt] $b$ = \leerzelle\\[3pt] $c$ = %s\\[3pt] $d$ = \leerzelle};'
                       % (W1 + W2 + 1.2, H / 2, tx(cw)))
    else:
        return None
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


def abb_zusammengesetzt(d, D, iid):
    rest = d.split(':', 1)[1].strip()
    nm = 'nicht maßstabsgerecht' in rest
    out = [r'\begin{tikzpicture}[line width=0.6pt,baseline=(current bounding box.north)]']
    m = re.search(r'Stadionform.*?Breite (\w) = (\S+ \w+) links, gerades Stück (\w) = (\S+ \w+) unten', rest)
    if m:
        a, av, b, bv = m.groups()
        r, L = 0.9, 3.0
        pfad = r'(0,0) -- (%s,0) arc (-90:90:%s) -- (0,%s) arc (90:270:%s) -- cycle' % (L, r, 2 * r, r)
        out.append(r'\begin{scope}\clip %s;\foreach \i in {-30,...,30}{\draw[line width=0.3pt] (\i*0.2-3,-3) -- ++(7,7);}\end{scope}' % pfad)
        out.append(r'\draw %s;' % pfad)
        out.append(r'\draw[dashed] (0,0) -- (0,%s);' % (2 * r))
        out.append(r'\node[font=\scriptsize,left,fill=white,inner sep=1pt] at (-%s,%s) {$%s$ = %s};' % (r + 0.05, r, a, tx(av)))
        out.append(r'\node[font=\scriptsize,below] at (%s,0) {$%s$ = %s};' % (L / 2, b, tx(bv)))
    elif re.search(r'Rechteck \(gepunktet\) mit grauem Kreis darin', rest):
        out.append(r'\draw[dotted,line width=0.9pt] (0,0) rectangle (3.6,2.4);')
        out.append(r'\draw[fill=black!20] (1.8,1.2) circle (1.0);')
    else:
        return None
    if nm:
        out.append(r'\node[font=\scriptsize,mbgrau,anchor=north west] at ([yshift=-2pt]current bounding box.south west) {nicht maßstabsgerecht};')
    out.append(r'\end{tikzpicture}')
    return ''.join(out)


# ===========================================================================
# Verteiler (Lauf C)
# ===========================================================================
def _tabelle_leer(d):
    """„Tabelle:“ mit „leer“ (Eintragfeld) und einzeiligen Tabellen; Prozent-Tabellen haben kein
    „leer“ und gehen weiter durch abb_tabelle_zeilen (byte-gleich)."""
    teile = [t.strip() for t in d.split(':', 1)[1].split(';') if t.strip()]
    zeilen = [[z.strip() for z in t.split(' | ')] for t in teile]
    n = max(len(z) for z in zeilen)
    zeilen = [z + [''] * (n - len(z)) for z in zeilen]
    zelle = lambda z: r'\leerzelle' if z == 'leer' else tx(z)
    if len(zeilen) == 2 and len(zeilen[0]) > 3 and not any(re.search(r'[A-Za-zÄÖÜäöü]{4,}', z) for z in zeilen[0][1:]) \
            and len(zeilen[0][0]) > 0:
        # Wertetabelle quer: erste Spalte = Größe
        pass
    if n > 8 and len(zeilen) <= 4:
        # sehr breite Wertetabelle (2014-OS-K4: elf Spalten): gestürzt, Größen als Spaltenköpfe
        zeilen = [list(x) for x in zip(*zeilen)]
        n = len(zeilen[0])
    lang = any(len(klar(x)) > 30 for z in zeilen for x in z)
    if lang:
        # langer Text in einer Zelle: tabular mit Absatzspalte (\sachtabelle kennt nur l, c, r)
        erste = max(len(klar(z[0])) for z in zeilen)
        w0 = min(4.5, 0.2 * erste + 0.4)
        form = '|p{%.1fcm}|' % w0 + ''.join('p{%.1fcm}|' % ((13.0 - w0) / (n - 1) - 0.5) for _ in range(n - 1))
        return (r'\par\medskip\begingroup\centering\renewcommand{\arraystretch}{1.25}\begin{tabular}{%s}\hline %s \\ \hline %s \\ \hline\end{tabular}\par\endgroup\medskip'
                % (form, ' & '.join(zelle(x) for x in zeilen[0]),
                   r'\\ \hline '.join(' & '.join(zelle(x) for x in z) for z in zeilen[1:])))
    spalten = 'l' + ('c' * (n - 1))
    return r'\sachtabelle{%s}{%s}{%s}' % (spalten, ' & '.join(zelle(x) for x in zeilen[0]),
                                          r'\\ '.join(' & '.join(zelle(x) for x in z) for z in zeilen[1:]))


def _einzeln(d, D, iid, vorspann_abb):
    typ = typ_von(d)
    if re.search(r'\baus (dem Vorspann|\d?[a-z]\)|\d[a-z]\b)', d.split(':')[0].split(';')[0]):
        zus = re.search(r'aus dem Vorspann,? zusätzlich (.*)$', d)
        if zus and vorspann_abb:
            return vorspann_abb + r'\par{\footnotesize\color{mbgrau}zusätzlich: ' + tx(zus.group(1)) + '}'
        mm = re.search(r'\(mit (.*)\)$', d)
        if mm and vorspann_abb:
            return vorspann_abb + r'\par{\footnotesize\color{mbgrau}' + tx(mm.group(1)) + '}'
        if vorspann_abb:
            return vorspann_abb
        D.abb_verweis_leer = getattr(D, 'abb_verweis_leer', [])
        D.abb_verweis_leer.append(iid)
        return rahmen(d, D, iid, 'Verweis ohne Abbildung der Bezugszeile')
    if typ.startswith(TYPEN_RAHMEN):
        return rahmen(d, D, iid)
    if typ in ('Säulendiagramm', 'Balkendiagramm'):
        g = abb_diagramm(d, D, iid, liegend=typ == 'Balkendiagramm')
        return g if g else rahmen(d, D, iid, 'Werte nicht lesbar')
    if typ == 'Kreisdiagramm':
        return abb_kreisdiagramm(d, D, iid) or rahmen(d, D, iid, 'Sektoren nicht lesbar')
    if typ == 'Glücksrad':
        return abb_gluecksrad(d, D, iid) or rahmen(d, D, iid, 'Felder nicht lesbar')
    if typ == 'Zahlenscheiben':
        return abb_zahlenscheiben(d, D, iid) or rahmen(d, D, iid, 'Sektoren nicht lesbar')
    if typ == 'Würfelnetze':
        return abb_wuerfelnetze(d, D, iid) or rahmen(d, D, iid, 'Felder nicht lesbar')
    if typ == 'Baumdiagramm':
        b = abb_baum(d, D, iid)
        if b and 'darunter Ankreuztabelle' in d:
            return b + '\n' + (abb_ankreuz('Ankreuztabelle: ' + d.split('darunter Ankreuztabelle:', 1)[1], D, iid) or '')
        return b or rahmen(d, D, iid, 'Äste nicht lesbar')
    if typ == 'Achsenkreuz ohne Einteilung':
        return abb_achsenkreuz_leer(d, D, iid) or rahmen(d, D, iid, 'Rastermaße fehlen')
    if typ in ('Koordinatensystem', 'Graph'):
        g = abb_graph_p10(d, D, iid)
        if g:
            D.abb_gezeichnet = getattr(D, 'abb_gezeichnet', 0) + 1
            return g
        return rahmen(d, D, iid, 'Graph nicht lesbar')
    if typ == 'Graphauswahl':
        return abb_graphauswahl(d, D, iid) or rahmen(d, D, iid, 'Kurvenform nicht lesbar')
    if typ == 'Ankreuztabelle':
        return abb_ankreuz(d, D, iid) or rahmen(d, D, iid, 'Spalten nicht lesbar')
    if typ in ('Dreieck', 'Viereck', 'Lageskizze', 'rechtwinkliges Dreieck'):
        g, offen = abb_geometrie(d, D, iid, typ)
        if g:
            return g
        return rahmen(d, D, iid, 'nicht verstanden: ' + '; '.join(offen[:3]))
    if typ == 'Schrägbild':
        return abb_schraegbild(d, D, iid) or rahmen(d, D, iid, 'Körper nicht erkannt')
    if typ.startswith('Netz'):
        return abb_netz(d, D, iid) or rahmen(d, D, iid, 'Netzform nicht erkannt')
    if typ == 'zusammengesetzte Figur':
        return abb_zusammengesetzt(d, D, iid) or rahmen(d, D, iid, 'Figur nicht erkannt')
    if typ == 'leerer Kreis mit markiertem Mittelpunkt' or d.startswith('leerer Kreis'):
        mm = re.search(r'Durchmesser (\d+(?:,\d+)?) cm', d)
        if mm:
            return r'\kreisleer[%s]' % _g(_z(mm.group(1)) / 2)
        return None
    if typ == 'Tabelle' and d.startswith('Tabelle:') and (' leer' in d or re.search(r'\| leer\b|; leer\b', d)
                                                         or len([t for t in d.split(':', 1)[1].split(';') if t.strip()]) == 1):
        return _tabelle_leer(d)
    return None


def alte_form(d):
    """Formen, die das Programm vor Lauf C schon setzte (Prozent, Abitur): unverändert über
    _abbildung_alt, damit die Prozent-Hefte byte-gleich bleiben."""
    return (not d or d.startswith('keine') or 'wie im Text' in d
            or (d.startswith('Tabelle:') and not re.search(r'(^|[|;:])\s*leer\s*($|[|;])', d))
            or d.startswith(('Säulenraster', 'Tabelle (Spalten', 'Tabelle aus dem Vorspann', 'Graph aus dem Vorspann',
                             'leerer Kreis mit markiertem Mittelpunkt und', 'Ankreuztabelle: drei Terme'))
            or re.match(r'Skizze aus \d', d) is not None
            or re.match(r'Säulendiagramm(,| [A-Z]| \(Achse beginnt bei \d+\):)', d) is not None
            or (d.startswith('rechtwinkliges Dreieck') and re.search(r'waagerechte Kathete \d', d) is not None))


def abbildung(desc, D, iid, vorspann_abb=''):
    """Liefert LaTeX zur Beschreibung; '' wenn keine nötig. Ankreuztabellen als Kennung
    ANKREUZTABELLE (alt) bzw. ANKREUZ{Kopf}{Zeilen}{Art} (echt_aufgabe setzt sie mit dem Wortlaut);
    „ // “ trennt zwei Abbildungen (Lauf C)."""
    d = (desc or '').strip()
    if ' // ' in d:
        teile = [abbildung(t, D, iid, vorspann_abb) for t in d.split(' // ')]
        kreuz = [t for t in teile if t.startswith('ANKREUZ')]
        bild = [t for t in teile if t and t not in kreuz]
        return '\n\\par\\smallskip\\noindent '.join(bild) + (('\n' + kreuz[0]) if kreuz else '')
    if D.pr['ordner'] != 'abitur' and d.startswith('Tabelle:') and \
            max(len(t.split(' | ')) for t in d.split(':', 1)[1].split(';') if t.strip()) > 8:
        return _tabelle_leer(d)   # breite Tabelle gestürzt (Lauf C; Prozent hat keine)
    if D.pr['ordner'] == 'abitur' or alte_form(d):
        return _abbildung_alt(d, D, iid, vorspann_abb)
    t = _einzeln(d, D, iid, vorspann_abb)
    if t is not None:
        return t
    return _abbildung_alt(d, D, iid, vorspann_abb)


def _abbildung_alt(desc, D, iid, vorspann_abb=""):
    """Liefert (latex, ankreuztabelle?) zur Beschreibung; '' wenn keine nötig."""
    d = (desc or '').strip()
    if not d or d.startswith('keine'):
        return ''
    if d.startswith('Tabelle:'):
        return abb_tabelle_zeilen(d)
    if d.startswith('Säulenraster'):
        return abb_saeulenraster(d)
    if 'wie im Text' in d:
        return ''   # Werte stehen im Wortlaut; Entscheidung: keine zweite Darstellung
    if d.startswith('Tabelle aus dem Vorspann') or d.startswith('Graph aus dem Vorspann') \
            or re.match(r'Skizze aus \d', d):
        return vorspann_abb
    if d.startswith('Graph:') and re.search(r'; x -?[\d.]+\.\.', d):
        g = abb_graph_term(d, D, iid)
        if g:
            return g
    if re.match(r'(Graph|Skizze|Diagramm):', d):
        # Abitur (Lauf B2): Graphen liegen nur als Beschreibung vor, kein Funktionsterm zum Zeichnen –
        # gesetzt wird ein Rahmen mit der Beschreibung, damit Lehrer und Schüler wissen, welche
        # Abbildung zur Aufgabe gehört (Entscheidung; Datenbefund, Zählung D.abb_beschreibung)
        D.abb_beschreibung = getattr(D, 'abb_beschreibung', 0) + 1
        return (r'\fbox{\parbox{0.9\linewidth}{\footnotesize\color{mbgrau}Abbildung im Original: '
                + tx(d.split(':', 1)[1].strip()) + '}}')
    if d.startswith('Säulendiagramm'):
        return abb_saeulen(d, D, iid)
    if d.startswith('Tabelle (Spalten'):
        t = abb_tabelle_spalten(d, D, iid)
        if t is not None:
            return t
    if d.startswith('leerer Kreis'):
        return r'\kreisleer[2]'
    if d.startswith('rechtwinkliges Dreieck'):
        return abb_dreieck(d)
    if d.startswith('Ankreuztabelle'):
        return 'ANKREUZTABELLE'
    D.befund(f'{iid}: Abbildung „{d[:40]}…“ hat keinen bekannten Typ – nicht gesetzt')
    return ''





# ===========================================================================
# Typenliste (Lauf C, Teil 1): python3 werkzeuge/abbildung.py --typen
# ===========================================================================
def _typenliste(mn):
    import csv, collections, importlib.util
    hier = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location('pruefheft', os.path.join(hier, 'pruefheft.py'))
    ph = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ph)

    class _D:
        pr = {'ordner': 'msa'}
        befunde = []

        def befund(self, s):
            self.befunde.append(s)
    kap = ['prozent', 'dreiecke', 'flaechen', 'koerper', 'lineare', 'quadratische', 'gleichungssysteme',
           'wachstum', 'daten', 'wahrscheinlichkeit']
    st = collections.OrderedDict()
    for k in kap:
        for r in csv.DictReader(open(os.path.join(mn, 'msa', f'wortlaut-eigen-{k}.csv'), encoding='utf-8'),
                                delimiter=';'):
            d = (r['abbildung'] or '').replace("\\'", "'").strip()
            for teil in d.split(' // '):
                D = _D()
                typ = typ_von(teil) or '(keine)'
                verweis = re.search(r'\baus (dem Vorspann|\d?[a-z]\)|\d[a-z]\b)', teil.split(':')[0])
                n0 = getattr(D, 'abb_rahmen', 0)
                t = ph.abbildung(teil, D, r['id'], 'V') if teil else ''
                if not teil or teil.startswith('keine'):
                    art = 'nichts'
                elif verweis:
                    art = 'Verweis'
                elif getattr(D, 'abb_rahmen', 0) > n0 or t.startswith('\\fbox'):
                    art = 'Rahmen'
                elif not t:
                    art = 'unbekannt'
                else:
                    art = 'gezeichnet'
                st.setdefault(typ, collections.Counter())[art] += 1
    print('| Typ | Zeilen | gezeichnet | Rahmen | Verweis | nichts/unbekannt |')
    print('|---|---|---|---|---|---|')
    for typ, c in sorted(st.items(), key=lambda x: -sum(x[1].values())):
        print(f'| {typ} | {sum(c.values())} | {c["gezeichnet"]} | {c["Rahmen"]} | {c["Verweis"]} | '
              f'{c["nichts"] + c["unbekannt"]} |')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='Abbildungstypen der P10-Wortlautdateien')
    ap.add_argument('--typen', action='store_true')
    ap.add_argument('--mn', default=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), 'mathe-nachhilfe'))
    a = ap.parse_args()
    _typenliste(a.mn)

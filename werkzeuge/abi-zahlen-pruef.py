#!/usr/bin/env python3
"""Eine Zahlenwahl je Originalaufgabe (Abitur GK, mehr-abi-gk/*.csv).

Gruppiert alle Zeilen nach Aufgabe (eltern_id ohne Teilbuchstaben) und
vergleicht die benannten Festlegungen im wortlaut: Funktionsterme
(f(x) = …), Punkte (A(1|2|3)), Vektoren/Geraden (g: x = …) und
Wahrscheinlichkeiten (p = …, P(A) = …). Trägt derselbe Name in zwei
Teilen derselben Aufgabe verschiedene Werte, wird gemeldet.
Ohne Modell. Aufruf: python3 abi-zahlen-pruef.py [Ordner]
Ausgabe: je Konflikt eine Zeile, am Ende die Zahl; Rückgabe 1 bei > 0.
"""
import csv, glob, os, re, sys
from collections import defaultdict
import sympy as sp

ORDNER = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(__file__), '..', '..', 'mathe-nachhilfe', 'abitur',
    'mehr-abi-gk')


def aufgabe(eid):
    """2023-bebb-gk-B2.1g -> 2023-bebb-gk-B2.1; …Stochastik12-b -> …12"""
    return re.sub(r'(?<=\d)-?[a-z]+$', '', eid)


def norm(s):
    s = re.sub(r'\\(left|right|cdot|,|;|!|displaystyle)', '', s)
    s = s.replace('{,}', ',').replace('\\mid', '|').replace('·', '')
    s = re.sub(r'\\[dt]frac', r'\\frac', s)
    s = re.sub(r'\s+', '', s)
    return s.rstrip('.,;')


def klammer(s, i):
    """Inhalt der {…}-Klammer ab Index i (s[i] == '{'), Endindex."""
    tiefe = 0
    for j in range(i, len(s)):
        tiefe += {'{': 1, '}': -1}.get(s[j], 0)
        if tiefe == 0:
            return s[i + 1:j], j + 1
    raise ValueError(s)


def zu_python(s):
    """Grobe LaTeX->Python-Übersetzung für den Zahlenvergleich."""
    while '\\frac' in s:
        i = s.index('\\frac')
        a, j = klammer(s, i + 5)
        b, k = klammer(s, j)
        s = s[:i] + '((' + a + ')/(' + b + '))' + s[k:]
    while '\\sqrt' in s:
        i = s.index('\\sqrt')
        a, j = klammer(s, i + 5)
        s = s[:i] + 'Q(' + a + ')' + s[j:]
    s = re.sub(r'(?<![A-Za-z])e\^', 'E^', s)
    s = s.replace('{', '(').replace('}', ')').replace(',', '.')
    s = re.sub(r'(?<=[0-9A-Za-z)])(?=[A-Za-z(])', '*', s)
    s = s.replace('Q*(', 'Q(').replace('^', '**').replace('%', '/100')
    return s


def gleich(a, b):
    """a, b normierte Terme: gleich als Zahl/Funktion? (Stichproben)"""
    if a == b:
        return True
    try:
        ea, eb = (sp.sympify(zu_python(v), locals={'Q': sp.sqrt, 'E': sp.E})
                  for v in (a, b))
        frei = sorted(ea.free_symbols | eb.free_symbols, key=str)
        for w in (0.37, 1.3, -2.1):
            d = (ea - eb).subs({v: w for v in frei})
            if abs(complex(sp.N(d))) > 1e-9:
                return False
        return True
    except Exception:
        return False


def klassen(werte):
    """Fasst gleichwertige Terme zusammen."""
    k = []
    for w in sorted(werte):
        for g in k:
            if gleich(g[0], w):
                g.append(w)
                break
        else:
            k.append([w])
    return k


MATHE = re.compile(r'\$([^$]+)\$')
# f(x) = …, f_a(x) = …, h(t) = … (nicht f'(x), f(2), F(x) bleibt drin)
FUNK = re.compile(r"(?<![\w'\\])([a-zA-Z](?:_\{?\w+\}?)?)\(([a-z])\)\s*=\s*(.+)")
PUNKT = re.compile(r"(?<![\w\\])([A-Z](?:_\{?\w+\}?|'*)?)\s*(?:\\left)?\(\s*"
                   r"([^()|]*?(?:\\mid|\|)[^()]*?)\s*(?:\\right)?\)")
GERADE = re.compile(r"(?<![\w\\])([a-z](?:_\{?\w+\}?)?)\s*:\s*\\vec\s*\{?x\}?\s*=\s*(.+)")
WKT = re.compile(r"(?<![\w\\])(p|P\([^)]*\))\s*=\s*([0-9][0-9{},.%\\ ]*)")


def festlegungen(text):
    out, punkte = [], []
    for m in MATHE.finditer(text):
        t = m.group(1)
        for teil in re.split(r'\s(?:\\text\{\s*und\s*\}|und)\s|;', t):
            f = FUNK.match(teil.strip())
            if f:
                rhs = re.split(r'\s(?:mit|für)\s|\\quad|,\s*[a-z]\s*\\in|=',
                               f.group(3))[0]
                # allgemeine Ansätze wie c(f(x)+d) sind keine Zahlenwahl
                # f(x) = 0,4 ist eine Gleichung, keine Festlegung
                if not re.search(r'[a-zA-Z]\([a-z]\)', rhs) and \
                        re.search(f.group(2), rhs):
                    out.append(('Funktion ' + f.group(1), norm(rhs)))
            g = GERADE.search(teil)
            if g:
                out.append(('Gerade ' + g.group(1), norm(g.group(2))))
        for p in PUNKT.finditer(t):
            punkte.append(p)
        for w in WKT.finditer(t):
            out.append(('Wkt ' + norm(w.group(1)), norm(w.group(2))))
    # Punkte gehören zur ersten Funktion der Zeile: H von f und H von k
    # (anderer Teil, andere Funktion) sind verschiedene Punkte.
    zu = next((n.split()[1] for n, _ in out if n.startswith('Funktion')), '')
    for p in punkte:
        out.append((f'Punkt {p.group(1)}' + (f' (zu {zu})' if zu else ''),
                    norm(p.group(2))))
    return out


def main():
    werte = defaultdict(lambda: defaultdict(set))  # aufgabe -> name -> {(wert, id)}
    for fn in sorted(glob.glob(os.path.join(ORDNER, '*.csv'))):
        with open(fn, encoding='utf-8') as fh:
            for z in csv.DictReader(fh, delimiter=';'):
                eid = z.get('eltern_id') or z['id']
                a = aufgabe(eid)
                for name, w in festlegungen(z['wortlaut']):
                    werte[a][name].add((w, z['id'], os.path.basename(fn)))
    n = 0
    for a in sorted(werte):
        for name, s in sorted(werte[a].items()):
            k = klassen({w for w, _, _ in s})
            if len(k) > 1:
                n += 1
                print(f'{a}  {name}:')
                for g in k:
                    ids = sorted({f'{i} ({d})' for v, i, d in s if v in g})
                    print(f'    {g[0]}   <- {", ".join(ids)}')
    print(f'{n} Meldungen')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())

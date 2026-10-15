#!/usr/bin/env python3
"""bestellen.py – eine Bestellung „Name · Was · Zusatz“ in Lieferung übersetzen, ohne Modell (M4).

Anlass: plan.md § 10, 15.10.2026 (k), Bedienung Weg C: der Chat fragt nur, was fehlt, höchstens einmal; vor dem
Setzen eine Zeile „Du bekommst: …“; Freitext führt zum besten Treffer mit einer Zeile, was fehlt; Lösungen immer mit.
Alles aus Daten:
  Schüler, Prüfung, Papier   aufgabenbank-privat schueler.md (Tabelle „Schüler“)
  Prüfungen                  mathe-nachhilfe */gliederung/README.md, Block „## Bestellung“ (Anzeige, Sorte,
                             Schülerliste, Papier, Setzer- und Ablagepfade, Fehlt) – neue Prüfung = neuer Block
  Blätter, Lernfolge, Begriffe   */gliederung/*.md: Kennung, Ordner, Anzeigenamen, Kurzwort, Stufen (Anzeigename)
  Sorte                      erster Buchstabe der Kennung (P, A, L, F, S)
  Lernblatt (Sorte S)        bau/register.csv (Kennung S…); sonst Katalog mathe-nachhilfe katalog/*.md
                             („← Eingabe …“) -> Ausgabe „bauen“ (der Chat baut nach bau/bauauftrag.md)
  Lieferliste                eingang/gebaut.csv (werkzeuge/lieferung.py)

  python3 werkzeuge/bestellen.py "Lena ana"                 -> JSON {zeile, frage, befehle, dateien, hinweis, bauen}
  python3 werkzeuge/bestellen.py "Lena ana" --wahl 2        -> nach einer Rückfrage (1-basiert)
  python3 werkzeuge/bestellen.py "Lena PA30" --ausfuehren   -> setzt (oder nimmt die PDFs des Tages bei gleicher
                                                               Fassung), schreibt die Lieferzeile, gibt pdf aus
Weitere Schalter: --datum JJJJ-MM-TT (Tagesordner, Vorgabe heute).
Umgebung: MATHE_NACHHILFE, PRIVAT (Ordner der Geschwister-Repos).
"""
import argparse
import csv
import datetime
import glob
import json
import os
import re
import shlex
import subprocess
import sys
import time
import unicodedata

HIER = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.dirname(HIER)
MN = os.environ.get('MATHE_NACHHILFE') or os.path.join(os.path.dirname(BANK), 'mathe-nachhilfe')
PRIVAT = os.environ.get('PRIVAT') or os.path.join(os.path.dirname(BANK), 'aufgabenbank-privat')
KENN = re.compile(r'^([PALFS]\d*)([GASZB])(\d{2,3})(?:-(\d+))?$', re.I)

# Wörter der Bestellung (gleich für alle Prüfungen; gemeinsam.md „Bestellung“, plan.md § 10, 15.10. k)
W_MEHR = {'mehr'}
W_LOES = {'lösung', 'loesung', 'lösungen', 'loesungen'}
W_ORIG = {'original', 'originale', 'heft'}
W_NEU = {'neu'}
W_PROBE = {'probeprüfung', 'probepruefung', 'probe', 'prüfung', 'pruefung'}
W_KARTE = {'karte', 'bestellkarte'}
W_HAND = {'handreichung'}
W_GESAMT = {'gesamtheft'}
W_MAPPE = {'mappe'}
W_LISTE = {'liste'}
W_LERN = {'lernblatt'}
W_KLASSE = {'klasse', 'kl', 'kl.'}
W_NOCHMAL = {'nochmal', 'noch', 'mal', 'dasselbe', 'wieder', 'gleiche', 'blatt'}
W_LEICHT = {'leicht', 'leichter', 'leichteres', 'leichtere', 'einfach', 'einfacher', 'einfacheres', 'einfachere'}
W_SCHWER = {'schwer', 'schwerer', 'schwereres', 'schwerere', 'schwieriger', 'schwierigeres'}
STOPP = {'was', 'zu', 'zum', 'zur', 'mit', 'und', 'ein', 'eine', 'einen', 'etwas', 'bitte', 'für', 'fuer', 'die',
         'der', 'das', 'den', 'dem', 'von', 'im', 'in', 'aus', 'auf', 'an', 'ich', 'wir', 'brauche', 'möchte',
         'gib', 'mir', 'ihm', 'ihr', 'noch', 'nur', 'zu', 'über', 'ueber', 'thema', 'auch', 'bei', 'oder', 'mal'}
SCHLUESSEL = (W_MEHR | W_LOES | W_ORIG | W_NEU | W_PROBE | W_KARTE | W_HAND | W_GESAMT | W_MAPPE | W_LISTE |
              W_LERN | W_KLASSE)


def norm(s):
    s = s.lower().replace('ß', 'ss')
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]+', ' ', s).strip()


def stamm(w):
    w = norm(w)
    for e in ('innen', 'ungen', 'en', 'er', 'n', 's', 'e'):
        if len(w) > 4 and w.endswith(e):
            return w[:-len(e)]
    return w


# ---------------------------------------------------------------------------------------------- Daten lesen

def schueler():
    p = os.path.join(PRIVAT, 'schueler.md')
    if not os.path.exists(p):
        return []
    t = open(p, encoding='utf-8').read()
    a = t.find('\n## Schüler')
    teil = t[a:].split('\n## ', 2)[1] if a >= 0 else ''
    out = []
    kopf = None
    for z in teil.splitlines():
        if not z.startswith('|'):
            continue
        zellen = [c.strip() for c in z.strip().strip('|').split('|')]
        if kopf is None:
            kopf = zellen
            continue
        if set(''.join(zellen)) <= set('-: '):
            continue
        out.append(dict(zip(['nr', 'name', 'klasse', 'schule', 'kurs', 'pruefung', 'papier'], zellen)))
    return out


def schueler_eintragen(name, pruefung, kurs):
    """Neue Zeile in der Schülertabelle (Regel schueler.md: fehlt eine Angabe, einmal fragen und eintragen)."""
    p = os.path.join(PRIVAT, 'schueler.md')
    t = open(p, encoding='utf-8').read()
    a = t.find('\n## Schüler')
    e = t.find('\n## ', a + 3)
    teil = t[a:e]
    zeilen = teil.rstrip('\n').split('\n')
    nr = max([int(s['nr']) for s in schueler() if s['nr'].isdigit() and int(s['nr']) < 90] + [0]) + 1   # ab 90 Tests
    neu = f'| {nr} | {name} | ? | ? | {kurs or "?"} | {pruefung} | ? |'
    open(p, 'w', encoding='utf-8').write(t[:a] + '\n'.join(zeilen + [neu]) + '\n' + t[e:])
    return nr


def kopf_felder(t):
    kopf = t.split('\n## ')[0]
    einfach = {}
    paare = {}
    for k, v in re.findall(r'^([A-Za-zÄÖÜäöü ]+):\s*(.+)$', kopf, re.M):
        k = k.strip()
        einfach.setdefault(k, v.strip())
        for teil in v.split('|'):
            if '=' in teil:
                a, b = teil.rsplit('=', 1)
                paare.setdefault(k, {})[a.strip()] = b.strip()
    return einfach, paare


def stufen(t):
    out = []
    a = t.find('\n## Stufen')
    if a < 0:
        return out
    teil = t[a + 1:]
    e = teil.find('\n## ', 3)
    teil = teil if e < 0 else teil[:e]
    for b in re.split(r'^(?=### )', teil, flags=re.M)[1:]:
        name = b.splitlines()[0][4:].strip()
        zu = re.search(r'^- \*\*Zuschnitt:\*\*\s*(.*)$', b, re.M)
        an = re.search(r'^- \*\*Anzeigename:\*\*\s*(.*)$', b, re.M)
        out.append((name, zu.group(1).strip() if zu else '', an.group(1).strip() if an else name))
    return out


def pruefungen():
    """Je */gliederung/README.md mit Block „## Bestellung“ eine Prüfung mit ihren Blättern."""
    out = []
    for readme in sorted(glob.glob(os.path.join(MN, '*', 'gliederung', 'README.md'))):
        t = open(readme, encoding='utf-8').read()
        a = t.find('\n## Bestellung')
        if a < 0:
            continue
        block = t[a + 1:].split('\n## ', 1)[0]
        f = {k.strip(): v.strip() for k, v in re.findall(r'^- ([^:\n]+):\s*(.*)$', block, re.M)}
        ordner = os.path.basename(os.path.dirname(os.path.dirname(readme)))
        sorten = [(x.split('=')[0].strip(), x.split('=')[1].strip() if '=' in x else '')
                  for x in f.get('Sorte', '').split('|') if x.strip()]
        P = dict(ordner=ordner, felder=f, anzeige=f.get('Anzeige', ordner), sorten=sorten,
                 liste=[x.strip().lower() for x in f.get('Schülerliste', '').split('|') if x.strip()],
                 papiere=[x.strip() for x in f.get('Papier', '').split('|') if x.strip()],
                 blaetter=[], gebiete={})
        for g in sorted(glob.glob(os.path.join(os.path.dirname(readme), '*.md'))):
            if os.path.basename(g).lower() == 'readme.md':
                continue
            tg = open(g, encoding='utf-8').read()
            ein, paare = kopf_felder(tg)
            kw = [norm(x) for x in ein.get('Kurzwort', '').split('|') if x.strip()]
            gebiet = ein.get('Gebiet', '').replace(' + ', ' und ')
            if kw:
                P['gebiete'].setdefault(gebiet, set()).update(kw)
            st = stufen(tg)
            for einheit, kenn in paare.get('Kennung', {}).items():
                m = KENN.match(kenn)
                if not m:
                    continue
                P['blaetter'].append(dict(
                    kennung=kenn, sorte=m.group(1)[0].upper(), platz=int(m.group(3)), gebiet=gebiet,
                    kapitel=ein.get('Kapitel', ''), kapitelname=ein.get('Name', ''), einheit=einheit,
                    anzeige=paare.get('Anzeigenamen', {}).get(einheit, einheit),
                    ordner=paare.get('Ordner', {}).get(einheit, ''), kapitelfolge=int(re.sub(r'\D', '', ein.get(
                        'Folge', '')) or 99), stufen=[(n, an) for n, z, an in st if z == einheit]))
        folge = {}
        for b in P['blaetter']:
            folge[b['gebiet']] = min(folge.get(b['gebiet'], 99), b['kapitelfolge'])
        P['blaetter'].sort(key=lambda b: (folge[b['gebiet']], b['platz']))
        out.append(P)
    return out


def lieferliste(nummer):
    p = os.path.join(BANK, 'eingang', 'gebaut.csv')
    if not nummer or not os.path.exists(p):
        return []
    with open(p, encoding='utf-8', newline='') as f:
        return [z for z in csv.DictReader(f, delimiter=';') if z['nummer'] == nummer]


def katalog():
    out = []
    for f in sorted(glob.glob(os.path.join(MN, 'katalog', '*.md'))):
        stem = os.path.basename(f)[:-3]
        if stem.startswith('_') or stem == 'index':
            continue
        t = open(f, encoding='utf-8').read()
        titel = (re.search(r'^# (.+)$', t, re.M) or [None, stem])[1].strip()
        kl = re.search(r'Klasse\s+(\d+)', t)
        einheiten = []
        for m in re.finditer(r'^(\d+)\. (.+?) – .*?(?:← Eingabe (.*))?$', t, re.M):
            einheiten.append((int(m.group(1)), m.group(2).strip(), m.group(3) or ''))
        out.append(dict(eintrag=stem, titel=titel, klasse=int(kl.group(1)) if kl else None, einheiten=einheiten))
    return out


# ---------------------------------------------------------------------------------------------- Hilfen

def p(pfad):
    """Pfad aus einem Block „Bestellung“: „privat …“, „mn …“ oder aufgabenbank."""
    if pfad.startswith('privat '):
        return os.path.join(PRIVAT, pfad[7:].strip())
    if pfad.startswith('mn '):
        return os.path.join(MN, pfad[3:].strip())
    return os.path.join(BANK, pfad.strip())


def neuestes(vorlage):
    """Vorlage mit {datum}: die jüngste vorhandene Datei."""
    treffer = sorted(glob.glob(p(vorlage).replace('{datum}', '*')))
    return treffer[-1] if treffer else None


def hefte(P):
    v = P['felder'].get('Hefte')
    if not v:
        return []
    return sorted({os.path.basename(x)[:-4] for x in glob.glob(p(v).replace('{heft}', '*'))}, reverse=True)


def heft_zu_jahr(P, jahr, papier):
    jahr = int(jahr)
    jahr = jahr + 2000 if jahr < 100 else jahr
    kand = [h for h in hefte(P) if h.startswith(f'{jahr}-')]
    for h in kand:
        if papier and h.endswith('-' + papier.lower()):
            return h
    return kand[0] if kand else None


def jahre_offen(P, papier, geliefert):
    """Je Jahr ein Heft (Papier des Schülers vor), jüngstes zuerst; die nicht gelieferten vorn."""
    jahre = sorted({int(h[:4]) for h in hefte(P)}, reverse=True)
    hs = [heft_zu_jahr(P, j, papier) for j in jahre]
    return [h for h in hs if h not in geliefert] + [h for h in hs if h in geliefert]


def kurz_jahr(heft):
    return f'’{heft[2:4]}' + (f' {heft[5:].upper()}' if heft[5:] not in ('os',) else '')


def fassung(P, b):
    """Kennung mit Fassung ohne Satz (pruefheft.py --nur-fassung)."""
    v = P['felder'].get('Blatt')
    if not v:
        return b['kennung']
    cmd = [sys.executable] + shlex.split(v.format(kapitel=b['kapitel'], einheit=b['einheit'])) + [
        '--nur-fassung', '--mn', MN]
    cmd[1] = os.path.join(BANK, cmd[1])
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=BANK)
    m = re.search(r'^FASSUNG (\S+)', r.stdout, re.M)
    return m.group(1) if m else b['kennung']


def befehl(vorlage, **kw):
    teile = shlex.split(vorlage.format(**kw))
    return ' '.join(['python3'] + [shlex.quote(x) for x in teile] + ['--mn', shlex.quote(MN)])


class Frage(Exception):
    def __init__(self, text, optionen, werte):
        self.text, self.optionen, self.werte = text, optionen, werte


# ---------------------------------------------------------------------------------------------- Planung

class Bestellung:
    def __init__(self, eingabe, wahl=None, datum=None):
        self.eingabe = eingabe
        self.wahl = wahl
        self.wahl_verbraucht = False
        self.datum = datum or datetime.date.today().isoformat()
        self.P_alle = pruefungen()
        self.out = dict(zeile='', frage=None, befehle=[], dateien=[], hinweis=None, bauen=None)
        self.liefer = []          # (eintrag, ordner, kennung, zusaetze)
        self.schueler = None
        self.name = None

    # eine Rückfrage: bei --wahl die gewählte Option, sonst Frage; nach einer Antwort keine zweite (Vorschlag)
    def frage(self, text, optionen, werte):
        if self.wahl is not None and not self.wahl_verbraucht:
            self.wahl_verbraucht = True
            if not 1 <= self.wahl <= len(werte):
                raise SystemExit(f'--wahl {self.wahl}: erlaubt 1–{len(werte)}')
            return werte[self.wahl - 1]
        if self.wahl_verbraucht:
            return werte[0]
        raise Frage(text, optionen, werte)

    def pruefung_von(self, s):
        """Prüfung und Sorte aus der Schülerzeile (Spalten Prüfung, Kurs, Papier)."""
        txt = (s or {}).get('pruefung', '').lower()
        if s and re.search(r'\bkeine\b', txt) and not re.search(r'mathe-prüfung', txt.replace('keine mathe', '')):
            return None, None
        for P in self.P_alle:
            if s and any(x in txt for x in P['liste']):
                kurs = ((s.get('kurs') or '') + ' ' + (s.get('papier') or '')).upper()
                sorte = next((so for so, k in P['sorten'] if k and k in kurs), P['sorten'][0][0] if P['sorten'] else '')
                return P, sorte
        return None, None

    def vorgabe(self):
        P = next(P for P in self.P_alle if P['blaetter'])
        return P, P['sorten'][0][0]

    def plan(self):
        roh = [w for w in re.split(r'[\s·,]+', self.eingabe.strip()) if w]
        S = schueler()
        # Name
        # bekannter Name auch mitten im Freitext („was Leichteres zu Parabeln für Lena“, Probe 15.10.)
        if roh and not any(x['name'].lower() == roh[0].lower() for x in S):
            i = next((i for i, w in enumerate(roh) if any(x['name'].lower() == w.lower() for x in S)), None)
            if i is not None:
                vor = roh[i - 1].lower() if i else ''
                roh = [roh[i]] + roh[:i - 1 if vor in ('für', 'fuer', 'an', 'von') else i] + roh[i + 1:]
        if roh:
            w = roh[0]
            s = next((x for x in S if x['name'].lower() == w.lower()), None)
            if s:
                self.schueler, self.name, roh = s, s['name'], roh[1:]
            elif w[:1].isupper() and norm(w) not in {norm(x) for x in SCHLUESSEL | STOPP | W_LEICHT | W_SCHWER} \
                    and not KENN.match(w) and not self.ist_begriff(w):
                optionen, werte = [], []
                for P in self.P_alle:
                    for so, kurs in (P['sorten'] or [('', '')]):
                        optionen.append(f'{P["anzeige"]}{" " + kurs if kurs else ""}')
                        werte.append((P, so, kurs))
                optionen.append('keine Prüfung')
                werte.append((None, None, ''))
                P, so, kurs = self.frage(f'Welche Prüfung schreibt {w}?', optionen, werte)
                nr = schueler_eintragen(w, P['anzeige'] if P else 'keine', kurs)
                self.schueler = next(x for x in schueler() if x['nr'] == str(nr))
                self.name, roh = w, roh[1:]
        self.nummer = f'S{int(self.schueler["nr"]):02d}' if self.schueler and self.schueler['nr'].isdigit() else None
        P, sorte = self.pruefung_von(self.schueler) if self.schueler else self.vorgabe()
        self.ohne_pruefung = P is None
        if P is None:
            P, sorte = self.vorgabe()
        self.P, self.sorte = P, sorte
        papier = (self.schueler or {}).get('papier', '').upper()
        self.papier = papier if papier in P['papiere'] else (P['papiere'][0] if P['papiere'] else '')
        self.geliefert = lieferliste(self.nummer)
        w = [norm(x) for x in roh]
        ws = set(w)
        # Wörter ohne Blatt
        if ws & W_LISTE:
            return self.liste()
        if ws & W_KARTE:
            return self.datei('Karte', 'Bestellkarte')
        if ws & W_HAND:
            return self.datei('Handreichung', 'Handreichung')
        if ws & W_GESAMT:
            return self.datei('Gesamtheft', 'Gesamtheft')
        if ws & W_MAPPE:
            return self.datei('Mappe', 'Mappe (nur Lehrer)')
        if ws & W_LERN or (ws & W_KLASSE and any(x.isdigit() for x in w)):
            return self.lernblatt(w)
        if ws & {norm(x) for x in W_PROBE} and not ws & W_ORIG:
            return self.original(None, neu=True, probe=True)
        if ws & W_ORIG:
            jahr = next((x for x in w if x.isdigit()), None)
            return self.original(jahr, neu=bool(ws & W_NEU))
        loes = bool(ws & {norm(x) for x in W_LOES})
        mehr = bool(ws & W_MEHR)
        rest = [x for x in w if x not in {norm(y) for y in SCHLUESSEL | W_NOCHMAL}]
        # Kennung
        k = next((x for x in roh if KENN.match(x)), None)
        if k:
            b = self.blatt_zu_kennung(k)
            if not b:
                return self.fehlt(f'{k.upper()} gibt es nicht')
            return self.blatt(b, loes=loes, mehr=mehr)
        # Gebiet über Kurzwort
        for gebiet, kws in P['gebiete'].items():
            if rest and rest[0] in kws and len([x for x in rest if x not in STOPP]) == 1:
                if 'basis' in kws or gebiet.startswith('nur Basisteil'):
                    return self.basis()
                return self.gebiet(gebiet, loes=loes, mehr=mehr)
        if not rest:
            if self.ohne_blaetter():
                return self.fehlt(None)
            return self.fehlt('Was soll es sein? Gebiet (ana, geo, daten, basis), Begriff oder Kennung')
        return self.freitext(rest, loes=loes, mehr=mehr)

    # ---- Bausteine

    def kopf(self):
        teile = ([self.name] if self.name else []) + [self.P['anzeige'] + (
            f' {dict(self.P["sorten"]).get(self.sorte, "")}'.rstrip() if self.P['ordner'] != 'msa' else '')]
        return 'Du bekommst: ' + ' · '.join(teile)

    def ohne_blaetter(self):
        return not [b for b in self.P['blaetter'] if b['sorte'] == self.sorte]

    def fehlt(self, text):
        f = self.P['felder'].get('Fehlt')
        self.out['zeile'] = self.kopf() + ': nichts'
        self.out['hinweis'] = text or f or 'Dazu gibt es nichts.'
        if text and f and self.ohne_blaetter():
            self.out['hinweis'] = f
        return self.out

    def ist_begriff(self, w):
        s = stamm(w)
        for P in self.P_alle:
            for b in P['blaetter']:
                if any(s and s in {stamm(x) for x in norm(t).split()} for t in
                       [b['anzeige'], b['einheit']] + [a for _, a in b['stufen']]):
                    return True
        return False

    def blatt_zu_kennung(self, k):
        m = KENN.match(k)
        kern = (m.group(1) + m.group(2) + m.group(3)).upper()
        for P in self.P_alle:
            for b in P['blaetter']:
                if b['kennung'].upper() == kern:
                    if P is not self.P:
                        self.P, self.sorte = P, b['sorte']
                    return b
        return None

    def hatte(self, kennung):
        return any((z.get('kennung') or '').split('-')[0] == kennung and 'nur lösung' not in (z.get('zusaetze') or '')
                   for z in self.geliefert)

    def gebiet(self, gebiet, loes=False, mehr=False):
        bl = [b for b in self.P['blaetter'] if b['gebiet'] == gebiet and b['sorte'] == self.sorte]
        if not bl:
            return self.fehlt(None)
        letzte = max([i for i, b in enumerate(bl) if self.hatte(b['kennung'])], default=-1)
        offen = [b for b in bl[letzte + 1:] + bl[:letzte + 1] if not self.hatte(b['kennung'])]
        vorschlag = offen[0] if offen else bl[0]
        i = bl.index(vorschlag)
        andere = [bl[(i + j) % len(bl)] for j in range(1, len(bl))][:2]
        werte = [vorschlag] + andere
        opt = [f'{b["anzeige"]} ({b["kennung"]})' + (' – Vorschlag' if j == 0 else '') +
               (' – hatte schon' if self.hatte(b['kennung']) else '') for j, b in enumerate(werte)]
        b = self.frage(f'{gebiet}: welches Blatt?', opt, werte)
        return self.blatt(b, loes=loes, mehr=mehr)

    def blatt(self, b, loes=False, mehr=False, hinweis=None):
        P = self.P
        kf = fassung(P, b)
        ordner = p(P['felder']['Blattordner'].format(datum=self.datum, ordner=b['ordner']))
        pdf = os.path.join(ordner, 'pdf')
        tex = os.path.join(ordner, 'src', '2-blatt.tex')
        gleich = os.path.exists(tex) and re.search(re.escape(kf) + r'(?!\d)', open(tex, encoding='utf-8').read()) \
            and all(os.path.exists(os.path.join(pdf, n)) for n in ('1-uebersicht.pdf', '2-blatt.pdf', '3-loesungen.pdf'))
        if not gleich:
            self.out['befehle'].append(befehl(P['felder']['Blatt'], kapitel=b['kapitel'], einheit=b['einheit'])
                                       + f' --datum {self.datum} --aus {shlex.quote(ordner)}'
                                       + (f' --schueler {self.nummer}' if self.nummer else ''))
        name = f'{b["anzeige"]} ({kf})'
        if mehr:
            mo = os.path.join(ordner, 'mehr')
            if not all(os.path.exists(os.path.join(mo, 'pdf', n)) for n in ('mehr.pdf', 'mehr-loesung.pdf')) \
                    or not gleich:
                self.out['befehle'].append(befehl(P['felder']['Mehr'], kapitel=b['kapitel'], einheit=b['einheit'])
                                           + f' --datum {self.datum} --aus {shlex.quote(mo)} --ohne-register')
            self.out['dateien'] = [os.path.join(mo, 'pdf', 'mehr.pdf'), os.path.join(mo, 'pdf', 'mehr-loesung.pdf')]
            self.out['zeile'] = f'{self.kopf()} · {name}: Mehr (alle Seiten), Lösung'
            self.liefer.append((f'{b["kennung"]} {b["ordner"]} mehr', os.path.relpath(mo, BANK), kf, 'mehr'))
        elif loes:
            self.out['dateien'] = [os.path.join(pdf, '3-loesungen.pdf')]
            self.out['zeile'] = f'{self.kopf()} · {name}: Lösung'
            self.liefer.append((f'{b["kennung"]} {b["ordner"]}', os.path.relpath(os.path.join(pdf, '3-loesungen.pdf'),
                                                                                 BANK), kf, 'nur lösung'))
        else:
            self.out['dateien'] = [os.path.join(pdf, n) for n in ('1-uebersicht.pdf', '2-blatt.pdf', '3-loesungen.pdf')]
            self.out['zeile'] = f'{self.kopf()} · {name}: Übersicht, Blatt, Lösung'
            self.liefer.append((f'{b["kennung"]} {b["ordner"]}', os.path.relpath(ordner, BANK), kf, ''))
            if self.hatte(b['kennung']) and not hinweis:
                d = max(z['datum'] for z in self.geliefert if (z.get('kennung') or '').split('-')[0] == b['kennung'])
                hinweis = f'hatte {b["kennung"]} schon am {d}'
        if self.ohne_pruefung and not hinweis:
            hinweis = 'laut Schülerliste keine Prüfung; Blatt der ' + P['anzeige']
        self.out['hinweis'] = hinweis
        return self.out

    def basis(self):
        v = self.P['felder'].get('Basiszettel')
        if not v:
            return self.fehlt(None)
        alle = sorted(glob.glob(p(v).replace('{n}', '*')), key=lambda x: int(re.search(r'Z(\d+)\.pdf$', x).group(1)))
        kenn = lambda x: os.path.basename(x)[:-4]
        offen = [x for x in alle if not any((z.get('kennung') or '') == kenn(x) for z in self.geliefert)]
        werte = (offen or alle)[:3]
        opt = [kenn(x) + (' – Vorschlag' if i == 0 else '') for i, x in enumerate(werte)]
        x = self.frage('Basis: welcher Zettel?', opt, werte)
        self.out['dateien'] = [x]
        self.out['zeile'] = f'{self.kopf()} · Basiszettel {kenn(x)}: Zettel, Ergebnisse (Seite 2)'
        self.liefer.append((f'basis {kenn(x)}', os.path.relpath(os.path.dirname(x), BANK), kenn(x), 'basis'))
        return self.out

    def original(self, jahr, neu=False, probe=False):
        P = self.P
        if not P['felder'].get('Hefte'):
            return self.fehlt(None)
        geliefert = {z['eintrag'].split()[-1] for z in self.geliefert if z['eintrag'].startswith('original')}
        if jahr is None:
            werte = jahre_offen(P, self.papier, geliefert if neu else set())[:3]
            opt = [kurz_jahr(h) + (' – neuestes offenes' if i == 0 and h not in geliefert else '')
                   + (' – hatte schon' if h in geliefert else '') for i, h in enumerate(werte)]
            heft = self.frage('Welches Jahr?', opt, werte)
        else:
            heft = heft_zu_jahr(P, jahr, self.papier)
            if not heft:
                js = sorted({h[:4] for h in hefte(P)})
                return self.fehlt(f'’{int(jahr) % 100:02d} gibt es nicht; da sind {js[0]}–{js[-1]}')
        if neu:
            o = p(P['felder']['Original neu Ordner'].format(heft=heft))
            dat = [os.path.join(o, 'blatt.pdf'), os.path.join(o, 'loesung.pdf')]
            if not all(os.path.exists(x) for x in dat):
                self.out['befehle'].append(befehl(P['felder']['Original neu'], heft=heft).replace(
                    f' --mn {shlex.quote(MN)}', '') + f' --privat {shlex.quote(PRIVAT)}')
            self.out['dateien'] = dat
            art = 'Probeprüfung (Original neu ganz)' if probe else 'Original neu'
            self.out['zeile'] = f'{self.kopf()} · {art} {kurz_jahr(heft)}: Blatt, Lösung'
            self.liefer.append((f'original-neu {heft}', 'privat:' + os.path.relpath(o, PRIVAT), heft,
                                'probe' if probe else 'original neu'))
        else:
            x = p(P['felder']['Hefte'].format(heft=heft))
            self.out['dateien'] = [x]
            self.out['zeile'] = f'{self.kopf()} · Original {kurz_jahr(heft)}: Heftseiten (privat, nur Lehrer)'
            self.liefer.append((f'original {heft}', 'privat:' + os.path.relpath(x, PRIVAT), heft, 'original'))
        if self.ohne_pruefung:
            self.out['hinweis'] = 'laut Schülerliste keine Prüfung; Heft der ' + P['anzeige']
        return self.out

    def datei(self, feld, wort):
        v = self.P['felder'].get(feld)
        if not v:
            return self.fehlt(f'{wort} gibt es für {self.P["anzeige"]} noch nicht')
        kurs = dict(self.P['sorten']).get(self.sorte, '').lower()
        x = neuestes(v.replace('{kurs}', kurs))
        if not x:
            return self.fehlt(f'{wort} ist noch nicht gesetzt')
        self.out['dateien'] = [x]
        self.out['zeile'] = f'Du bekommst: {self.P["anzeige"]} · {wort}'
        return self.out

    def liste(self):
        self.out['zeile'] = f'Du bekommst: {self.name or "ohne Namen"} · Liste'
        if not self.nummer:
            self.out['hinweis'] = 'ohne Namen keine Liste'
            return self.out
        self.out['liste'] = [f'{z["datum"]} · {z["eintrag"]}' + (f' · {z["kennung"]}' if z.get('kennung') else '')
                             + (f' · {z["zusaetze"]}' if z.get('zusaetze') else '')
                             for z in sorted(self.geliefert, key=lambda z: z['datum'], reverse=True)]
        if not self.out['liste']:
            self.out['hinweis'] = 'noch keine Lieferung'
        return self.out

    def treffer(self, woerter):
        """Bester Treffer unter den Blättern der Prüfung: Anzeigename 3, Einheit und Kapitel 2, Stufe 1."""
        best, punkte, gefunden = None, 0, set()
        for b in self.P['blaetter']:
            if b['sorte'] != self.sorte:
                continue
            gew = [(b['anzeige'], 3), (b['einheit'], 2), (b['kapitelname'], 2)] + [(a, 1) for _, a in b['stufen']]
            pk, gf = 0, set()
            for w in woerter:
                s = stamm(w)
                for t, g in gew:
                    if s in {stamm(x) for x in norm(t).split()}:
                        pk += g
                        gf.add(w)
                        break
            if pk > punkte:
                best, punkte, gefunden = b, pk, gf
        return best, gefunden

    def freitext(self, woerter, loes=False, mehr=False):
        inhalt = [w for w in woerter if w not in STOPP]
        leicht = [w for w in inhalt if w in W_LEICHT]
        schwer = [w for w in inhalt if w in W_SCHWER]
        such = [w for w in inhalt if w not in W_LEICHT | W_SCHWER]
        if self.ohne_blaetter():
            return self.fehlt(None)
        b, gefunden = self.treffer(such)
        if not b:
            gb = ', '.join(sorted({x for kws in self.P['gebiete'].values() for x in list(kws)[:1]}))
            return self.fehlt(f'Dazu gibt es kein Prüfungsblatt („{" ".join(such)}“); Gebiete: {gb}')
        fehlt = []
        if leicht:
            fehlt.append('leichter gibt es noch nicht')
        if schwer:
            fehlt.append('schwerer gibt es noch nicht')
        rest = [w for w in such if w not in gefunden]
        if rest:
            fehlt.append(f'„{" ".join(rest)}“ passt zu keinem Blatt')
        return self.blatt(b, loes=loes, mehr=mehr, hinweis='; '.join(fehlt) + f' – das ist {b["anzeige"]}' if fehlt
                          else None)

    def lernblatt(self, w):
        klasse = next((int(x) for i, x in enumerate(w) if x.isdigit() and i and w[i - 1] in {norm(y) for y in W_KLASSE}),
                      None)
        if klasse is None and self.schueler:
            m = re.match(r'\d+', self.schueler.get('klasse', ''))
            klasse = int(m.group()) if m else None
        such = [x for x in w if x not in {norm(y) for y in SCHLUESSEL} and not x.isdigit() and x not in STOPP]
        roh = [x for x in re.split(r'[\s·,]+', self.eingabe) if norm(x) in such]
        thema = ' '.join(roh) or ' '.join(such)
        # Treffer in Sorte S: gesetzte Lernblätter mit Kennung S… (bau/register.csv)
        reg = os.path.join(BANK, 'bau', 'register.csv')
        if os.path.exists(reg) and such:
            with open(reg, encoding='utf-8', newline='') as f:
                for z in csv.DictReader(f, delimiter=';'):
                    if re.match(r'^S\d+[GASZ]\d', z['kennung']) and any(
                            stamm(s) in stamm(z['eintraege']) for s in such):
                        o = os.path.join(BANK, z['pfad'], 'pdf')
                        self.out['dateien'] = [os.path.join(o, n) for n in ('1-uebersicht.pdf', '2-blatt.pdf',
                                                                            '3-loesungen.pdf')]
                        self.out['zeile'] = (f'Du bekommst: {(self.name + " · ") if self.name else ""}Lernblatt '
                                             f'{z["eintraege"]} ({z["kennung"]}): Übersicht, Blatt, Lösung')
                        self.liefer.append((z['eintraege'], z['pfad'], z['kennung'], 'lernblatt'))
                        return self.out
        # sonst bauen: bester Katalogeintrag
        best, pk, einheit = None, 0, None
        for k in katalog():
            texte = [(k['titel'], 3), (k['eintrag'].replace('-', ' '), 3)] + [(n + ' ' + e, 1) for _, n, e in
                                                                               k['einheiten']]
            s = sum(g for x in such for t, g in texte if stamm(x) in {stamm(y) for y in norm(t).split()})
            # ganze Eingabe wie im Katalog („← Eingabe „brüche addieren““) zählt am meisten
            s += sum(10 for _, _, e in k['einheiten'] if such and ' '.join(such) in
                     [norm(x) for x in re.findall(r'„([^“]+)“', e)])
            if s > pk:
                best, pk = k, s
        if not best:
            self.out['zeile'] = f'Du bekommst: {(self.name + " · ") if self.name else ""}nichts'
            self.out['hinweis'] = f'Kein Katalogeintrag zu „{thema}“'
            return self.out
        # Einheit nur, wenn ein Wort über den Titel hinaus auf sie zeigt
        titel = {stamm(y) for y in norm(best['titel'] + ' ' + best['eintrag'].replace('-', ' ')).split()}
        eigen = [x for x in such if stamm(x) not in titel]
        treff = lambda e: sum(1 for x in eigen if stamm(x) in {stamm(y) for y in norm(e[1] + ' ' + e[2]).split()}) + (
            10 if ' '.join(such) in [norm(x) for x in re.findall(r'„([^“]+)“', e[2])] else 0)
        eh = max(best['einheiten'], key=treff, default=None)
        if eh and not treff(eh):
            eh = None
        self.out['bauen'] = dict(thema=best['titel'] + (f' – {eh[1]}' if eh else ''), eintrag=best['eintrag'],
                                 einheit=eh[0] if eh else None, klasse=klasse or best['klasse'])
        kl = klasse or best['klasse']
        self.out['zeile'] = (f'Du bekommst: {(self.name + " · ") if self.name else ""}Lernblatt '
                             f'{self.out["bauen"]["thema"]}' + (f' (Kl. {kl})' if kl else '') + ': wird gebaut, ≈ 20 min')
        self.out['hinweis'] = f'Lernblatt „{thema}“ gibt es noch nicht'
        return self.out


# ---------------------------------------------------------------------------------------------- Ausführen

def ausfuehren(B, out):
    t0 = time.time()
    for c in out['befehle']:
        r = subprocess.run(c, shell=True, capture_output=True, text=True, cwd=BANK)
        if r.returncode:
            out['fehler'] = f'{c[:120]} … Rückgabe {r.returncode}: {(r.stderr or r.stdout)[-600:]}'
            break
    out['pdf'] = [x for x in out['dateien'] if os.path.exists(x)]
    fehlen = [x for x in out['dateien'] if not os.path.exists(x)]
    if fehlen:
        out['fehler'] = (out.get('fehler', '') + ' fehlt: ' + ', '.join(fehlen)).strip()
    if B.nummer and B.liefer and not fehlen:
        msgs = []
        for eintrag, ordner, kennung, zus in B.liefer:
            r = subprocess.run([sys.executable, os.path.join(HIER, 'lieferung.py'), '--nummer', B.nummer,
                                '--eintrag', eintrag, '--ordner', ordner, '--kennung', kennung, '--zusaetze', zus,
                                '--datum', B.datum], capture_output=True, text=True, cwd=BANK)
            msgs.append(r.stdout.strip() or r.stderr.strip())
        out['lieferung'] = msgs
    out['laufzeit'] = round(time.time() - t0, 1)
    return out


def main():
    ap = argparse.ArgumentParser(description='Bestellung -> Lieferung (JSON)')
    ap.add_argument('eingabe')
    ap.add_argument('--wahl', type=int)
    ap.add_argument('--ausfuehren', action='store_true')
    ap.add_argument('--datum')
    a = ap.parse_args()
    B = Bestellung(a.eingabe, a.wahl, a.datum)
    try:
        out = B.plan()
    except Frage as f:
        out = B.out
        out['zeile'] = None
        out['frage'] = dict(text=f.text, optionen=f.optionen)
        out['befehle'], out['dateien'] = [], []
    if a.ausfuehren and not out['frage']:
        out = ausfuehren(B, out)
    print(json.dumps(out, ensure_ascii=False, indent=1))
    sys.exit(1 if out.get('fehler') else 0)


if __name__ == '__main__':
    main()

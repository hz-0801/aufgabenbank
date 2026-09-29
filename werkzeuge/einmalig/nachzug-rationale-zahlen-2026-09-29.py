"""Nachzug rationale-zahlen auf Katalog cebfd509 (Mappe 29.09.), bank.md
fünfte Fassung, Vorlage auftrag-eintrag.md 2026-09-29c.

Aufruf aus der Wurzel des Repos aufgabenbank:
    python3 werkzeuge/einmalig/nachzug-rationale-zahlen-2026-09-29.py <n>
schreibt bank/rationale-zahlen/e<n>.jsonl neu (ein Schreibvorgang) und
druckt übernommen/neu/umgeschrieben/entfallen.

Übernommen: aufgabe, antwort, loesung, pruef wortgleich; nachgezogen
nur id, sprosse, kette_nr, quelle, sprosse_text (bei zusammengelegter
Prüfungshöhe auch merkmal, weil es je Sprosse einheitlich sein muss).
"""
import copy
import json
import sys

B = 'bank/rationale-zahlen/'
E = 'rationale-zahlen'
# Katalogzeilen: alt (Stand 761321330) -> neu (cebfd509)
QMAP = {87: 84, 88: 85, 89: 86, 90: 87, 36: 35}
SERIE = ("Welche Ergebnisse können nicht stimmen? "
         "Begründe, ohne genau zu rechnen.")
P4 = ("Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. "
      "Begründe, ohne genau zu rechnen.")
GERUEST = "Vorzeichen: __ Betrag: __ Ergebnis: __"

PH = {
    1: ("Prüfungshöhe: eine Zahl angeben, die eine Bedingung mit negativer "
        "Grenze erfüllt, offene Antwort mit vielen richtigen Lösungen "
        "(P10-Form 2015-OS-B1b, Niveau I); daneben die aufsteigende Reihe "
        "aus negativem Bruch, negativer Dezimalzahl, Dezimalzahl und "
        "Wurzel (2014-OS-B1h, Niveau I – Typ und Original "
        "brueche-dezimalzahlen.md, hier nur der negative Teil)",
        "Prüfungsform: Zahl zu einer negativen Grenze angeben oder Zahlen "
        "mit negativem Bruch ordnen, Original verfremdet"),
    3: ("Prüfungshöhe: Termwert eines Bruchterms mit zwei negativen "
        "Einsetzungen ohne Taschenrechner, Ergebnis mit Vorzeichen und "
        "Komma (P10-Form 2021-OS-B1g, Niveau I); daneben derselbe Term mit "
        "ganzzahligem Ergebnis (2016-OS-B1i, Niveau I), das Produkt einer "
        "Vorzahl mit einer Klammerdifferenz (2026-FOR-B1g, Niveau I) und "
        "die Vorzeichenregel als Ankreuzaufgabe (2015-OS-B1g, Niveau I)",
        "Prüfungsform: Termwert mit negativen Einsetzungen oder "
        "Vorzeichenregel ohne Zahlen, Original verfremdet"),
    4: ("Prüfungshöhe: aus einer Preisliste mit Familienkarte, "
        "Gruppenticket und Altersgrenzen die günstigste Kombination für "
        "eine gegebene Gruppe ermitteln und gegen die Alternativen abwägen "
        "(P10-Form 2016-OS-K2d, Niveau III, Vorrat); daneben als "
        "Basismarke den Ausgangswert aus einer Angabe „so viel mehr als“ "
        "zurückrechnen (2017-OS-K2a, Niveau I)",
        "Prüfungsform: günstigste Preiskombination oder Ausgangswert aus "
        "„mehr als“, Original verfremdet"),
}


def lade(f):
    return [json.loads(z) for z in open(B + f + '.jsonl', encoding='utf-8')]


def nummeriere(rows):
    out = []
    for r in rows:
        r = copy.deepcopy(r)
        r['quelle'] = QMAP.get(r['quelle'], r['quelle'])
        out.append(r)
    return out


def kette(rows, k, s=None):
    return [copy.deepcopy(r) for r in rows
            if r['kette_nr'] == k and (s is None or r['sprosse'] == s)]


def um(r, **kw):
    r = copy.deepcopy(r)
    r['_um'] = True
    r.update(kw)
    return r


def verschiebe(rows, d):
    for r in rows:
        r['sprosse'] += d
    return rows


def pruefung_zusammen(rows, einheit, s):
    """alle Prüfungssprossen einer Kette zu einer Sprosse s."""
    text, merkmal = PH[einheit]
    for i, r in enumerate(rows, 1):
        r.update(sprosse=s, variante=i, sprosse_text=text, merkmal=merkmal)
    return rows


def pflicht(R, k, p):
    return [r for r in kette(R, k) if r.get('pflicht') == p]


def teile_pflicht(R, k):
    return (pflicht(R, k, 'fehler'), pflicht(R, k, 'begruenden'),
            pflicht(R, k, 'darstellung'), pflicht(R, k, 'anwendung'))


# ---------- Einheit 1 ----------
def e1(R):
    gf = kette(R, 1, 1)
    m = ("ganze Zahlen, auch negative, an der Zahlengeraden eintragen; "
         "$-5$ bleibt, die zweite Zahl wandert")
    pack = []
    for i, x in enumerate([3, -2, -8, 6, -9], 1):
        a, b = sorted([-5, x])
        pack.append(um(gf[0], variante=i, merkmal=m,
                       aufgabe=f"Trage die Zahlen $-5$ und ${x}$ an der "
                               "Zahlengeraden ein.",
                       loesung=f"von links: ${a}$; ${b}$"))
    F, Bg, D, A = teile_pflicht(R, 5)
    F[1] = um(F[1], aufgabe="Lena soll $-0{,}35$ und $-0{,}4$ vergleichen. "
              "Sie schreibt: $-0{,}4 < -0{,}35$. Prüfe, ob Lena richtig "
              "verglichen hat.",
              loesung="Richtig. Von zwei negativen Zahlen ist die mit dem "
              "größeren Betrag die kleinere: $0{,}4 > 0{,}35$, also "
              "$-0{,}4 < -0{,}35$.", pruef="")
    F[2] = um(F[2], aufgabe="Jonas hat jeweils die Zahl genau in der Mitte "
              f"zweier Zahlen bestimmt. {SERIE} \\\\ (1) Mitte von "
              "$-0{,}8$ und $-0{,}7$: $-0{,}85$ \\\\ (2) Mitte von $-4$ und "
              "$6$: $1$ \\\\ (3) Mitte von $-9$ und $-3$: $6$ \\\\ (4) Mitte "
              "von $-2{,}4$ und $-2{,}2$: $-2{,}3$",
              loesung="Nicht stimmen können (1) und (3). (1): $-0{,}85$ "
              "liegt links von beiden Zahlen, nicht zwischen ihnen. (3): "
              "Zwischen zwei negativen Zahlen liegt keine positive Zahl.",
              pruef="")
    Bg[1] = um(Bg[1], aufgabe=f"{P4} \\\\ (1) Jede negative Zahl ist kleiner "
               "als $0$. \\\\ (2) Von zwei negativen Zahlen ist immer die mit "
               "dem größeren Betrag die größere. \\\\ (3) Es gibt eine "
               "negative Zahl, deren Gegenzahl auch negativ ist.",
               loesung="(1) wahr, denn negative Zahlen liegen links der "
               "Null. (2) falsch, z. B. hat $-9$ den größeren Betrag als "
               "$-2$, ist aber kleiner. (3) falsch, denn die Gegenzahl "
               "einer negativen Zahl liegt rechts der Null, z. B. ist die "
               "Gegenzahl von $-3$ die $3$.")
    D[1] = um(D[1], aufgabe="Ein Konto hat den Kontostand $-45$ €. Schreibe "
              "in Worten, was dieser Kontostand bedeutet.")
    A[2] = um(A[2], aufgabe="Ein Impfstoff muss bei $-20$ °C oder kälter "
              "lagern. Im Gefrierschrank der Praxis sind es $-17$ °C. Ist "
              "es dort kalt genug?",
              loesung="Nein; vergleichen: $-17 > -20$, also ist es wärmer "
              "als $-20$ °C.", pruef="-17")
    ph = pruefung_zusammen(kette(R, 1, 6) + kette(R, 1, 7), 1, 6)
    return (kette(R, 1, 0) + pack
            + sum([kette(R, 1, s) for s in range(2, 6)], []) + ph
            + kette(R, 2) + kette(R, 3) + kette(R, 4)
            + F + Bg + D + A)


# ---------- Einheit 2 ----------
def e2(R):
    gf = kette(R, 3, 1)
    m = ("Start negativ, positive Zahl dazu oder weg; der Start $-7$ "
         "bleibt, die Änderung wandert")
    pack = []
    for i, d in enumerate([3, 9, -2, 7, -4], 1):
        op = f"+ {d}" if d > 0 else f"- {-d}"
        ri = "rechts" if d > 0 else "links"
        pack.append(um(gf[0], variante=i, merkmal=m,
                       aufgabe=f"Berechne: $-7 {op}$", antwort="__",
                       loesung=f"Start: $-7$; Pfeil: ${abs(d)}$ nach {ri}; "
                               f"Ergebnis: $-7 {op} = {-7 + d}$",
                       pruef=f"-7{op.replace(' ', '')}"))
    vz = []
    v = gf[0]
    for i, (a, b, erg, grund) in enumerate([
            (-13, 8, "kleiner als null",
             "Beträge vergleichen: $13 > 8$, die negative Zahl hat den "
             "größeren Betrag."),
            (-5, 14, "größer als null",
             "Beträge vergleichen: $14 > 5$, die positive Zahl hat den "
             "größeren Betrag."),
            (-17, 9, "kleiner als null",
             "Beträge vergleichen: $17 > 9$, die negative Zahl hat den "
             "größeren Betrag.")], 1):
        r = copy.deepcopy(v)
        r.update(sprosse=2, variante=i, hoehe='sprosse',
                 sprosse_text="nur das Vorzeichen: ist die Summe größer oder "
                 "kleiner als null? ankreuzen und mit den Beträgen begründen, "
                 "nicht ausrechnen",
                 merkmal="nur das Vorzeichen der Summe bestimmen, mit den "
                 "Beträgen begründen, nicht ausrechnen",
                 aufgabe=f"Rechne ${a} + {b}$ nicht aus. Ist die Summe "
                 "größer oder kleiner als null? Kreuze an und begründe mit "
                 "den Beträgen.\\\\ \\kreuz{größer als null} "
                 "\\kreuz{kleiner als null}",
                 form="ankreuzen", antwort="", loesung=f"{erg}; {grund}",
                 pruef="", grafik="", loesungsgrafik="")
        r['_neu'] = True
        vz.append(r)
    zz = kette(R, 3, 4)
    zz[0] = um(zz[0], antwort=GERUEST,
               loesung="Zeichen zusammenfassen: $3 - 8 - 4$; Vorzeichen: "
               "minus, weil $8 + 4$ mehr ist als $3$; Betrag: $12 - 3 = 9$; "
               "Ergebnis: $3 - 8 - 4 = -9$")
    zz[1] = um(zz[1], antwort=GERUEST,
               loesung="Zeichen zusammenfassen: $-5 + 2 + 6$; Vorzeichen: "
               "plus, weil $2 + 6$ mehr ist als $5$; Betrag: $8 - 5 = 3$; "
               "Ergebnis: $-5 + 2 + 6 = 3$")
    F, Bg, D, A = teile_pflicht(R, 7)
    F[1] = um(F[1], aufgabe="Ela soll $6 + (-2)$ berechnen. Sie rechnet so: "
              "$6 + (-2) = 6 - 2 = 4$. Prüfe, ob Ela richtig gerechnet hat.",
              loesung="Richtig. Plus und minus zusammen werden minus: aus "
              "$+ (-2)$ wird $- 2$.", pruef="")
    F[2] = um(F[2], aufgabe=f"Kai hat vier Aufgaben gerechnet. {SERIE} "
              "\\\\ (1) $-8 - 5 = -3$ \\\\ (2) $-4 + 9 = 5$ \\\\ (3) "
              "$7 - (-6) = 1$ \\\\ (4) $-12 + 3 = -9$",
              loesung="Nicht stimmen können (1) und (3). (1): Von $-8$ geht "
              "es weiter nach links, das Ergebnis muss kleiner als $-8$ "
              "sein. (3): Minus minus wird plus, das Ergebnis muss größer "
              "als $7$ sein.", pruef="")
    Bg[1] = um(Bg[1], aufgabe=f"{P4} \\\\ (1) Addiert man zu einer negativen "
               "Zahl eine positive, ist das Ergebnis immer positiv. \\\\ (2) "
               "Subtrahiert man eine negative Zahl, wird das Ergebnis immer "
               "größer. \\\\ (3) Die Summe zweier negativer Zahlen ist nie "
               "positiv.",
               loesung="(1) falsch, z. B. $-8 + 3 = -5$. (2) wahr, denn "
               "minus minus wird plus, der Pfeil geht nach rechts. (3) wahr, "
               "denn beide Pfeile gehen nach links, weg von der Null.")
    return (kette(R, 1) + kette(R, 2) + kette(R, 3, 0) + pack + vz
            + verschiebe(kette(R, 3, 2) + kette(R, 3, 3), 1)
            + verschiebe(zz, 1)
            + verschiebe(sum([kette(R, 3, s) for s in range(5, 9)], []), 1)
            + kette(R, 4) + kette(R, 5) + kette(R, 6)
            + F + Bg + D + A)


# ---------- Einheit 3 ----------
def e3(R):
    vs = kette(R, 1, 0)
    for r in vs:
        r['sprosse_text'] = ("„Wie viele Minuszeichen?“ – die negativen "
                             "Faktoren zählen und das Vorzeichen des "
                             "Ergebnisses ankreuzen; nichts rechnen")
    gf = kette(R, 1, 1)
    m = ("eine Zahl positiv, eine negativ: Ergebnis negativ; der Faktor "
         "$-6$ bleibt, der positive Faktor wandert")
    pack = []
    for i, x in enumerate([3, 5, 2, 9, 8], 1):
        pack.append(um(gf[0], variante=i, merkmal=m,
                       aufgabe=f"Berechne: ${x} \\cdot (-6)$",
                       antwort=GERUEST if i <= 2 else "__",
                       loesung=f"Vorzeichen: verschiedene Vorzeichen, also "
                       f"minus; Betrag: ${x} \\cdot 6 = {6 * x}$; Ergebnis: "
                       f"${x} \\cdot (-6) = {-6 * x}$",
                       pruef=f"{x}*(-6)"))
    df = kette(R, 1, 4)
    df[0] = um(df[0], loesung="Minuszeichen zählen: zwei, also plus; "
               "Teilprodukt: $(-2) \\cdot 5 = -10$; Ergebnis: "
               "$(-10) \\cdot (-3) = 30$")
    df[1] = um(df[1], loesung="Minuszeichen zählen: drei, also minus; "
               "Teilprodukt: $(-2) \\cdot (-3) = 6$; Ergebnis: "
               "$6 \\cdot (-5) = -30$")
    df[2] = um(df[2], loesung="Minuszeichen zählen: eins, also minus; "
               "Teilprodukt: $3 \\cdot (-2) = -6$; Ergebnis: "
               "$(-6) \\cdot 7 = -42$")
    F, Bg, _, A = teile_pflicht(R, 3)
    F[1] = um(F[1], aufgabe="Leo soll $(-18) : (-3)$ berechnen. Er rechnet "
              "so: $(-18) : (-3) = 6$. Prüfe, ob Leo richtig gerechnet hat.",
              loesung="Richtig. Minus durch minus ergibt plus, und "
              "$18 : 3 = 6$.", pruef="")
    F[2] = um(F[2], aufgabe=f"Eva hat vier Aufgaben gerechnet. {SERIE} "
              "\\\\ (1) $(-4) \\cdot 9 = 36$ \\\\ (2) $(-5) \\cdot (-8) = 40$ "
              "\\\\ (3) $-3^2 = 9$ \\\\ (4) $56 : (-7) = -8$",
              loesung="Nicht stimmen können (1) und (3). (1): Verschiedene "
              "Vorzeichen ergeben minus, das Ergebnis muss negativ sein. "
              "(3): Ohne Klammer gehört das Minus nicht zur Basis, das "
              "Ergebnis muss negativ sein.", pruef="")
    Bg[1] = um(Bg[1], aufgabe="Jana sagt: „Man teilt eine positive Zahl "
               "durch eine negative Zahl. Ob das Ergebnis positiv oder "
               "negativ ist, kann man nicht sagen, solange man die Zahlen "
               "nicht kennt.“ Begründe, ob Jana recht hat.",
               loesung="Nein; verschiedene Vorzeichen ergeben auch beim "
               "Teilen immer minus, die Zahlen bestimmen nur den Betrag.")
    Bg[2] = um(Bg[2], aufgabe=f"{P4} \\\\ (1) Ein Produkt aus vier Faktoren, "
               "von denen genau zwei negativ sind, ist nie negativ. \\\\ (2) "
               "Das Quadrat einer negativen Zahl ist immer negativ. \\\\ (3) "
               "Teilt man eine Zahl durch $-1$, erhält man immer ihre "
               "Gegenzahl.",
               loesung="(1) wahr, denn zwei Minuszeichen sind eine gerade "
               "Anzahl; das Produkt ist positiv oder, wenn ein Faktor null "
               "ist, null. (2) falsch, z. B. $(-3)^2 = 9$. (3) wahr, denn "
               "geteilt durch $-1$ dreht nur das Vorzeichen, z. B. "
               "$(-6) : (-1) = 6$.")
    ph = pruefung_zusammen(sum([kette(R, 1, s) for s in range(7, 11)], []),
                           3, 7)
    return (vs + pack + kette(R, 1, 2) + kette(R, 1, 3) + df
            + kette(R, 1, 5) + kette(R, 1, 6) + ph + kette(R, 2)
            + F + Bg + A)


# ---------- Einheit 4 ----------
def e4(R):
    gf = kette(R, 1, 1)
    m = ("Startwert plus eine Buchung; der Startwert $-60$ € bleibt, die "
         "Buchung wandert")
    pack = []
    for i, d in enumerate([25, 90, -40, 60, -15], 1):
        satz = (f"Dann werden ${d}$ € eingezahlt." if d > 0
                else f"Dann werden ${-d}$ € abgebucht.")
        op = f"+ {d}" if d > 0 else f"- {-d}"
        pack.append(um(gf[0], variante=i, merkmal=m,
                       aufgabe=f"Ein Konto steht bei $-60$ €. {satz} Wie "
                       "hoch ist der neue Kontostand?",
                       loesung=f"Startwert: $-60$ €; Änderung: "
                       f"${'+' if d > 0 else '-'}{abs(d)}$ €; rechnen: "
                       f"$-60 {op} = {-60 + d}$; Ergebnis: ${-60 + d}$ €",
                       pruef=f"-60{op.replace(' ', '')}"))
    F, Bg, _, A = teile_pflicht(R, 3)
    F[1] = um(F[1], aufgabe="Sina soll $-(4 - 17)$ berechnen. Sie rechnet "
              "so: \\rechnung{-(4 - 17) &= -4 + 17 \\\\ &= 13} Prüfe, ob "
              "Sina richtig gerechnet hat.",
              loesung="Richtig. Ein Minus vor der Klammer dreht alle Zeichen "
              "in der Klammer.", pruef="")
    F[2] = um(F[2], aufgabe=f"Malte hat Minusklammern aufgelöst. {SERIE} "
              "\\\\ (1) $20 - (5 - 8) = 17$ \\\\ (2) $15 - (9 + 4) = 2$ "
              "\\\\ (3) $-(6 - 11) = -5$ \\\\ (4) $40 - (-3 + 10) = 33$",
              loesung="Nicht stimmen können (1) und (3). (1): Die Klammer "
              "ist negativ; zieht man eine negative Zahl ab, muss das "
              "Ergebnis größer als $20$ sein. (3): Die Klammer ist negativ, "
              "das Minus davor macht das Ergebnis positiv.", pruef="")
    Bg[1] = um(Bg[1], aufgabe=f"{P4} \\\\ (1) Steht ein Minus vor einer "
               "Klammer, dreht man beim Auflösen immer alle Zeichen in der "
               "Klammer. \\\\ (2) Beim Addieren darf man die Summanden immer "
               "vertauschen. \\\\ (3) Beim Subtrahieren darf man die Zahlen "
               "immer vertauschen.",
               loesung="(1) wahr, denn man zieht die ganze Klammer ab, z. B. "
               "$10 - (4 - 1) = 10 - 4 + 1 = 7$. (2) wahr, denn für die "
               "Addition gilt das Kommutativgesetz, z. B. "
               "$-3 + 8 = 8 + (-3)$. (3) falsch, z. B. $5 - 2 = 3$, aber "
               "$2 - 5 = -3$.")
    Bg[2] = um(Bg[2], aufgabe="Finn sagt: „Von $-9$ °C bis $6$ °C sind es "
               "$3$ Grad Unterschied.“ Begründe, ob Finn recht hat.",
               loesung="Nein; von $-9$ bis $0$ sind es $9$ Grad, von $0$ bis "
               "$6$ noch $6$ Grad; Unterschied: $6 - (-9) = 15$ Grad.")
    ph = pruefung_zusammen(kette(R, 1, 6) + kette(R, 1, 7), 4, 6)
    return (kette(R, 1, 0) + pack
            + sum([kette(R, 1, s) for s in range(2, 6)], []) + ph
            + kette(R, 2) + F + Bg + A)


def schreibe(einheit, rows, alt):
    st = {'uebernommen': 0, 'neu': 0, 'umgeschrieben': 0}
    for r in rows:
        if r.pop('_neu', False):
            st['neu'] += 1
        elif r.pop('_um', False):
            st['umgeschrieben'] += 1
        else:
            st['uebernommen'] += 1
        r.pop('_um', None)
        r['id'] = (f"{E}-e{einheit}-k{r['kette_nr']}-s{r['sprosse']}"
                   f"-v{r['variante']}")
    st['entfallen'] = len(alt) - st['uebernommen'] - st['umgeschrieben']
    with open(B + f'e{einheit}.jsonl', 'w', encoding='utf-8',
              newline='\n') as h:
        for r in rows:
            h.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f'e{einheit}', len(rows), st)


if __name__ == '__main__':
    n = int(sys.argv[1])
    alt = lade(f'e{n}')
    schreibe(n, {1: e1, 2: e2, 3: e3, 4: e4}[n](nummeriere(alt)), alt)

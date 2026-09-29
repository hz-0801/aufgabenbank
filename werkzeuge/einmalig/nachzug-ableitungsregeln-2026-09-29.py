"""Nachzug bank/ableitungsregeln auf Katalog f56cace (Mappe 29.09.)
und bank.md fünfte Fassung. Einmalig; Aufruf aus der Repo-Wurzel:
    python3 werkzeuge/einmalig/nachzug-ableitungsregeln-2026-09-29.py e1|e2|e3
Schreibt die Datei ganz (erster Wurf). Übernommene Zeilen bleiben
wortgleich bis auf id, sprosse, kette_nr, quelle, sprosse_text."""
import json, sys, copy

B = 'bank/ableitungsregeln/'
E = 'ableitungsregeln'
QMAP = {97: 96, 98: 97, 99: 98, 38: 37}
KAT97_VOR = ("„Innen und außen?“ – zu Verkettungen ankreuzen, welcher Teil "
             "die innere Funktion ist (der Exponent, die Klammer) und was "
             "ihre Ableitung ist (eine Zahl, ein Vielfaches von x); "
             "nichts rechnen")
KAT97_VOR2 = ("innere und äußere Funktion hinschreiben, nicht ableiten: "
              "z = v(x) und u(z) als zwei Zeilen; rückwärts aus u und v "
              "die Verkettung bilden")

M_FEHLER = ("Fehler finden in drei Formen: Schülerrechnung mit Fehler, "
            "fehlerfreie Vorlage prüfen, Serie ohne genaue Rechnung")
M_BEGR = ("begründen in drei Formen: Warum-Frage, Aussagenserie, "
          "Personenaussage")


def lade(f):
    return [json.loads(l) for l in open(B + f + '.jsonl', encoding='utf-8')]


def schreibe(f, rows):
    with open(B + f + '.jsonl', 'w', encoding='utf-8', newline='\n') as h:
        for r in rows:
            r = {k: v for k, v in r.items() if not k.startswith('_')}
            h.write(json.dumps(r, ensure_ascii=False) + '\n')


def nachziehen(r):
    r['quelle'] = QMAP.get(r['quelle'], r['quelle'])
    r['id'] = (f"{E}-e{r['einheit']}-k{r['kette_nr']}-s{r['sprosse']}"
               f"-v{r['variante']}")
    return r


def setze(r, **kw):
    r = copy.deepcopy(r)
    r.update(kw)
    return r


def ersetze(rows, k, s, neu):
    aus, drin = [], False
    for r in rows:
        if r['kette_nr'] == k and r['sprosse'] == s:
            if not drin:
                aus.extend(neu)
                drin = True
        else:
            aus.append(r)
    return aus


def reihe(rows, k, s):
    return [r for r in rows if r['kette_nr'] == k and r['sprosse'] == s]


# ---------------- e1 ----------------
def e1():
    rows = lade('e1')
    v = reihe(rows, 2, 1)[0]
    m = ("ganze Koeffizienten, dritter Grad, einmal ableiten; 2x³ − 5x + 4 "
         "bleibt, der Koeffizient von x² wandert")
    gf = []
    for i, a in enumerate([3, -4, 6, 1, -2], 1):
        ta = {1: '+ x^2', -1: '- x^2'}.get(a, (f'+ {a}x^2' if a > 0
                                              else f'- {-a}x^2'))
        b = 2 * a
        tb = f'+ {b}x' if b > 0 else f'- {-b}x'
        aa = '' if abs(a) == 1 else str(abs(a))
        pa = (f'+ 2 \\cdot {aa}x' if a > 0 else f'- 2 \\cdot {aa}x')
        erg = f'6x^2 {tb} - 5'
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"$f(x) = 2x^3 {ta} - 5x + 4$ – $f'(x)$?",
            antwort="$f'(x) =$ __",
            loesung=(f"Summanden einzeln ableiten: $3 \\cdot 2x^2 {pa} - 5$; "
                     f"Konstante fällt weg: $4$ wird $0$; "
                     f"zusammenfassen: $6x^2 {tb} - 5$; "
                     f"Ergebnis: $f'(x) = {erg}$"),
            pruef="2*3"))
    rows = ersetze(rows, 2, 1, gf)
    f = reihe(rows, 4, 1)
    fe = [setze(f[0], merkmal=M_FEHLER),
          setze(f[1], merkmal=M_FEHLER,
                aufgabe=("Zu $g(x) = \\frac{1}{2}x^6 + 5x$ schreibt Ben "
                         "$g'(x) = 3x^5 + 5$. Prüfe, ob Ben richtig "
                         "gerechnet hat."),
                loesung=("Richtig. Nach der Faktor- und Potenzregel wird der "
                         "Vorfaktor $\\frac{1}{2}$ mit dem Exponenten $6$ "
                         "multipliziert, und $5x$ wird zu $5$."),
                pruef=""),
          setze(f[2], merkmal=M_FEHLER,
                aufgabe=("Zu $f(x) = 3x^4 - 5x^2 + 2x + 9$ haben vier "
                         "Schüler $f'(x)$ angegeben: (1) $12x^3 - 10x + 2$ "
                         "(2) $12x^4 - 10x^2 + 2$ (3) $12x^3 - 10x + 11$ "
                         "(4) $3x^3 - 5x + 2$. Welche Ergebnisse können "
                         "nicht stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) nicht: Der höchste Exponent muss um eins "
                         "kleiner werden, also $3$ sein; (3) nicht: Die "
                         "Konstante $9$ fällt weg, das Glied ohne $x$ kommt "
                         "nur von $2x$; (4) nicht: Der Vorfaktor $3$ wird "
                         "mit dem Exponenten $4$ multipliziert, vorn muss "
                         "$12$ stehen."),
                pruef="")]
    rows = ersetze(rows, 4, 1, fe)
    g = reihe(rows, 4, 2)
    be = [setze(g[0], merkmal=M_BEGR),
          setze(g[1], merkmal=M_BEGR,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe, ohne genau zu rechnen. "
                         "(1) Die Ableitung einer ganzrationalen Funktion "
                         "dritten Grades hat immer den Grad zwei. (2) Zwei "
                         "Funktionen mit derselben Ableitung sind immer "
                         "gleich. (3) Beim Ableiten fällt jede Zahl im "
                         "Term weg."),
                loesung=("(1) wahr, denn der höchste Exponent $3$ wird um "
                         "eins kleiner und sein Vorfaktor ist nicht null; "
                         "(2) falsch, z. B. haben $x^2 + 1$ und $x^2 + 6$ "
                         "beide die Ableitung $2x$; (3) falsch, z. B. wird "
                         "$5x$ zu $5$ – nur ein Summand ohne $x$ fällt "
                         "weg."),
                pruef=""),
          setze(g[2], merkmal=M_BEGR,
                aufgabe=("Für jede Zahl $k$ ist $f_k(x) = k \\cdot x^4$. "
                         "Jonas sagt: „Ich muss auch $k$ ableiten. Dabei "
                         "fällt $k$ weg, also ist $f_k'(x) = 4x^3$.“ "
                         "Begründe, ob Jonas recht hat."),
                loesung=("Nein; abgeleitet wird nach $x$, $k$ ist dabei "
                         "eine feste Zahl und bleibt nach der Faktorregel "
                         "als Vorfaktor stehen: $f_k'(x) = 4k \\cdot x^3$."),
                pruef="")]
    rows = ersetze(rows, 4, 2, be)
    return [nachziehen(r) for r in rows]


# ---------------- e2 ----------------
def kette_loes(fn, v, u, vs, us, zus, erg):
    return (f"innere Funktion: $v(x) = {v}$; äußere Funktion: $u(z) = {u}$; "
            f"innere Ableitung: $v'(x) = {vs}$; äußere Ableitung: "
            f"$u'(z) = {us}$; zusammensetzen: ${fn}'(x) = {zus}$; "
            f"Ergebnis: ${fn}'(x) = {erg}$")


def e2():
    rows = lade('e2')
    alt = reihe(rows, 1, 0)
    vor1 = [setze(r, sprosse=-1, sprosse_text=KAT97_VOR) for r in alt]
    muster = alt[0]
    mv = ("innere und äußere Funktion getrennt hinschreiben oder rückwärts "
          "zur Verkettung zusammensetzen, nicht ableiten")
    vor0 = []
    daten = [
        ("$f(x) = e^{6x}$ ist eine Verkettung. Schreibe die innere Funktion "
         "$z = v(x)$ und die äußere Funktion $u(z)$ in zwei Zeilen auf. "
         "Leite nicht ab.", "$z =$ __ \\\\ $u(z) =$ __",
         "innere Funktion: $z = 6x$; äußere Funktion: $u(z) = e^z$", "6"),
        ("$g(x) = (2x + 5)^4$ ist eine Verkettung. Schreibe die innere "
         "Funktion $z = v(x)$ und die äußere Funktion $u(z)$ in zwei Zeilen "
         "auf. Leite nicht ab.", "$z =$ __ \\\\ $u(z) =$ __",
         "innere Funktion: $z = 2x + 5$; äußere Funktion: $u(z) = z^4$",
         "2"),
        ("Die innere Funktion ist $v(x) = 3x - 2$, die äußere Funktion ist "
         "$u(z) = z^5$. Wie heißt die Verkettung $f(x) = u(v(x))$?",
         "$f(x) =$ __",
         "innere Funktion für $z$ einsetzen: $f(x) = (3x - 2)^5$", "3"),
        ("Die innere Funktion ist $v(x) = 2x^2 + 1$, die äußere Funktion ist "
         "$u(z) = e^z$. Wie heißt die Verkettung $f(x) = u(v(x))$?",
         "$f(x) =$ __",
         "innere Funktion für $z$ einsetzen: $f(x) = e^{2x^2 + 1}$", ""),
    ]
    for i, (a, an, l, p) in enumerate(daten, 1):
        vor0.append(setze(muster, sprosse=0, variante=i,
                          sprosse_text=KAT97_VOR2, merkmal=mv, aufgabe=a,
                          form="teil", antwort=an, loesung=l, pruef=p))
    rows = ersetze(rows, 1, 0, vor1 + vor0)
    v = reihe(rows, 1, 1)[0]
    m = ("e hoch k mal x, k ganz, auch negativ; f(x) = e^(kx) bleibt, "
         "k wandert")
    gf = []
    for i, k in enumerate([5, -2, 8, -5, 9], 1):
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"$f(x) = e^{{{k}x}}$ – $f'(x)$?",
            antwort="$f'(x) =$ __",
            loesung=kette_loes('f', f'{k}x', 'e^z', f'{k}', 'e^z',
                               f'e^{{{k}x}} \\cdot {k}' if k > 0 else
                               f'e^{{{k}x}} \\cdot ({k})',
                               f'{k} \\cdot e^{{{k}x}}'),
            pruef=str(k)))
    rows = ersetze(rows, 1, 1, gf)
    f = reihe(rows, 3, 1)
    fe = [setze(f[0], merkmal=M_FEHLER),
          setze(f[1], merkmal=M_FEHLER,
                aufgabe=("Zu $g(x) = (4x - 1)^3$ schreibt Lea "
                         "$g'(x) = 12 \\cdot (4x - 1)^2$. Prüfe, ob Lea "
                         "richtig gerechnet hat."),
                loesung=("Richtig. Nach der Kettenregel wird die äußere "
                         "Ableitung $u'(z) = 3z^2$ an der inneren Funktion "
                         "$v(x) = 4x - 1$ mit der inneren Ableitung "
                         "$v'(x) = 4$ multipliziert: "
                         "$3 \\cdot (4x - 1)^2 \\cdot 4 = 12 \\cdot "
                         "(4x - 1)^2$."),
                pruef=""),
          setze(f[2], merkmal=M_FEHLER,
                aufgabe=("Zu $f(x) = e^{-3x}$ haben vier Schüler $f'(x)$ "
                         "angegeben: (1) $-3 \\cdot e^{-3x}$ (2) $e^{-3x}$ "
                         "(3) $-3x \\cdot e^{-3x - 1}$ (4) "
                         "$3 \\cdot e^{-3x}$. Welche Ergebnisse können "
                         "nicht stimmen? Begründe, ohne genau zu rechnen."),
                loesung=("(2) nicht: Die innere Ableitung fehlt als Faktor; "
                         "(3) nicht: $e^{-3x}$ wird nicht wie eine Potenz "
                         "abgeleitet, der Exponent bleibt $-3x$; (4) nicht: "
                         "Der Graph fällt überall, die Ableitung muss "
                         "negativ sein."),
                pruef="")]
    rows = ersetze(rows, 3, 1, fe)
    g = reihe(rows, 3, 2)
    be = [setze(g[0], merkmal=M_BEGR),
          setze(g[1], merkmal=M_BEGR,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe, ohne genau zu rechnen. "
                         "(1) Die Ableitung von $e^{kx}$ hat immer denselben "
                         "Exponenten $kx$ wie die Funktion. (2) Jede "
                         "Funktion $e^{kx}$ ist ihre eigene Ableitung. "
                         "(3) Bei $(ax + b)^n$ hängt die innere Ableitung "
                         "nie von $x$ ab."),
                loesung=("(1) wahr, denn die äußere Ableitung von $e^z$ ist "
                         "wieder $e^z$, dazu kommt nur der Faktor $k$; "
                         "(2) falsch, z. B. hat $e^{2x}$ die Ableitung "
                         "$2 \\cdot e^{2x}$; (3) wahr, denn die innere "
                         "Funktion $ax + b$ hat die Ableitung $a$, eine "
                         "Zahl."),
                pruef=""),
          setze(g[2], merkmal=M_BEGR,
                aufgabe=("Max sagt: „Die Ableitung von "
                         "$f(x) = e^{x^2 - 3}$ ist wieder $e^{x^2 - 3}$, "
                         "denn die e-Funktion ist ihre eigene Ableitung.“ "
                         "Begründe, ob Max recht hat."),
                loesung=("Nein; nur $e^x$ ist seine eigene Ableitung. "
                         "Innere Funktion: $v(x) = x^2 - 3$; innere "
                         "Ableitung: $v'(x) = 2x$; Ergebnis: "
                         "$f'(x) = 2x \\cdot e^{x^2 - 3}$."),
                pruef="")]
    rows = ersetze(rows, 3, 2, be)
    return [nachziehen(r) for r in rows]


# ---------------- e3 ----------------
def e3():
    rows = lade('e3')
    v = reihe(rows, 1, 1)[0]
    m = ("x² mal e hoch x, e-Term ausklammern; x² · eˣ bleibt, der "
         "Vorfaktor wandert")
    gf = []
    for i, a in enumerate([3, 2, -4, 6, -1], 1):
        ax = {1: 'x^2', -1: '-x^2'}.get(a, f'{a}x^2')
        d = 2 * a
        ein = f'{d}x \\cdot e^x ' + (f'+ {ax} \\cdot e^x' if a > 0 else
                                     f'- {ax[1:]} \\cdot e^x')
        erg = f'({ax} ' + (f'+ {d}x' if d > 0 else f'- {-d}x') + ') \\cdot e^x'
        gf.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"$f(x) = {ax} \\cdot e^x$ – $f'(x)$, $e^x$ ausgeklammert?",
            antwort="$f'(x) =$ __",
            loesung=(f"Faktoren ableiten: $u(x) = {ax}$, $u'(x) = {d}x$, "
                     f"$v(x) = e^x$, $v'(x) = e^x$; Produktregel: "
                     f"$f'(x) = {ein}$; $e^x$ ausklammern: "
                     f"$f'(x) = {erg}$; Ergebnis: $f'(x) = {erg}$"),
            pruef=str(a) if abs(a) != 1 else str(d)))
    rows = ersetze(rows, 1, 1, gf)
    f = reihe(rows, 2, 1)
    fe = [setze(f[0], merkmal=M_FEHLER),
          setze(f[1], merkmal=M_FEHLER,
                aufgabe=("Zu $g(x) = 2x \\cdot e^{-3x}$ schreibt Sara "
                         "$g'(x) = (2 - 6x) \\cdot e^{-3x}$. Prüfe, ob Sara "
                         "richtig gerechnet hat."),
                loesung=("Richtig. Nach der Produktregel mit der inneren "
                         "Ableitung $-3$ im e-Faktor ist $g'(x) = 2 \\cdot "
                         "e^{-3x} + 2x \\cdot (-3) \\cdot e^{-3x} = "
                         "(2 - 6x) \\cdot e^{-3x}$."),
                pruef=""),
          setze(f[2], merkmal=M_FEHLER,
                aufgabe=("Zu $f(x) = (x^2 + 4) \\cdot e^x$ haben vier "
                         "Schüler $f'(x)$ angegeben: (1) $(x^2 + 2x + 4) "
                         "\\cdot e^x$ (2) $2x \\cdot e^x$ (3) $(x^2 + 2x) "
                         "\\cdot e^x$ (4) $(x^2 + 2x + 4) \\cdot e^{2x}$. "
                         "Welche Ergebnisse können nicht stimmen? Begründe, "
                         "ohne genau zu rechnen."),
                loesung=("(2) nicht: Nur die Faktoren einzeln abgeleitet, "
                         "der Summand $(x^2 + 4) \\cdot e^x$ fehlt; (3) "
                         "nicht: Aus $(x^2 + 4) \\cdot e^x$ bleibt das Glied "
                         "$4$ im Polynomfaktor; (4) nicht: $e^x$ bleibt beim "
                         "Ableiten $e^x$, der Exponent ändert sich nicht."),
                pruef="")]
    rows = ersetze(rows, 2, 1, fe)
    g = reihe(rows, 2, 2)
    be = [setze(g[0], merkmal=M_BEGR),
          setze(g[1], merkmal=M_BEGR,
                aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder "
                         "falsch ist. Begründe, ohne genau zu rechnen. "
                         "(1) Die Ableitung eines Produkts ist immer das "
                         "Produkt der Ableitungen. (2) Die Ableitung von "
                         "Polynom mal $e^x$ ist immer wieder ein Polynom mal "
                         "$e^x$. (3) Die Nullstellen von $(x^2 - 16) \\cdot "
                         "e^{3x}$ sind immer dieselben wie die von "
                         "$x^2 - 16$."),
                loesung=("(1) falsch, z. B. hat $x \\cdot e^x$ die "
                         "Ableitung $(x + 1) \\cdot e^x$, nicht "
                         "$1 \\cdot e^x$; (2) wahr, denn nach der "
                         "Produktregel kann man $e^x$ aus beiden Summanden "
                         "ausklammern; (3) wahr, denn der e-Term ist nie "
                         "null."),
                pruef=""),
          setze(g[2], merkmal=M_BEGR,
                aufgabe=("Emil sagt: „Die Ableitung von $f(x) = x \\cdot "
                         "e^{2x}$ ist $f'(x) = e^{2x} + x \\cdot e^{2x}$.“ "
                         "Begründe, ob Emil recht hat."),
                loesung=("Nein; beim zweiten Summanden fehlt die innere "
                         "Ableitung $2$ des e-Faktors, richtig ist "
                         "$f'(x) = e^{2x} + 2x \\cdot e^{2x} = (1 + 2x) "
                         "\\cdot e^{2x}$."),
                pruef="")]
    rows = ersetze(rows, 2, 2, be)
    return [nachziehen(r) for r in rows]


if __name__ == '__main__':
    for f in sys.argv[1:]:
        schreibe(f, {'e1': e1, 'e2': e2, 'e3': e3}[f]())

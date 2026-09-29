#!/usr/bin/env python3
"""Nachzug bank/pythagoras auf Katalog cebfd50 (Mappe 29.09.) und
Vorlage auftrag-eintrag.md 2026-09-29c.

Aufruf: python3 werkzeuge/einmalig/nachzug-pythagoras-2026-09-29.py e1|e2|e3
Schreibt die Datei der Einheit in einem Schreibvorgang und druckt die
Zahlen übernommen / neu / umgeschrieben / entfallen.

Änderungen am Katalog (Mappe alt 761321330 → neu cebfd50):
- Erkennungsschritte „Wo ist der rechte Winkel?“, „Lange oder kurze
  Seite gesucht?“, „Teildreieck nachfahren“ stehen jetzt als Vorstufe
  in der Kettenzeile (längerer Sprossentext); neu ist „Satz oder
  Umkehrung?“ vor Einheit 2.
- Zeilennummern: Erkennungsschritte 35–38, Kettenzeilen 87–89.
"""
import copy
import json
import math
import sys
from pathlib import Path

B = Path(__file__).resolve().parents[2] / "bank" / "pythagoras"
E = "pythagoras"

VORSTUFE = {
    1: "„Wo ist der rechte Winkel?“ – in Dreiecken verschiedener Lage die "
       "Rechtwinkelmarke einkreisen und die Seite gegenüber mit „H“ "
       "(Hypotenuse) beschriften; nichts rechnen",
    2: "„Lange oder kurze Seite gesucht?“ – zu Dreiecken mit zwei Maßen "
       "ankreuzen: Hypotenuse gesucht (plus) oder Kathete gesucht (minus); "
       "nichts rechnen",
    3: "„Teildreieck nachfahren“ – in einer Figur mit Höhe (gleichschenkliges "
       "Dreieck, Trapez, Parallelogramm) oder in Pyramide und Kegel das "
       "rechtwinklige Dreieck farbig nachfahren und seine Seiten beschriften; "
       "nichts rechnen",
}
# quelle alt → neu
QMAP = {36: 35, 38: 36, 40: 38, 89: 87, 90: 88, 91: 89}


def lade(f):
    return [json.loads(z) for z in (B / f"{f}.jsonl").read_text(
        encoding="utf-8").splitlines() if z.strip()]


def schreibe(f, rows):
    text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    (B / f"{f}.jsonl").write_text(text, encoding="utf-8")


def tsd(n):
    """Ganzzahl mit Tausender-\\, (LaTeX)."""
    s = f"{n:,}".replace(",", "\\,")
    return s


def neu_id(r):
    s = r["sprosse"]
    ss = f"s{s}" if s >= 0 else f"s{s}"
    return f"{E}-e{r['einheit']}-k{r['kette_nr']}-{ss}-v{r['variante']}"


def feste_felder(r):
    return {k: r[k] for k in ("aufgabe", "loesung", "pruef", "grafik",
                              "form", "antwort", "loesungsgrafik",
                              "original", "merkmal")}


def zaehle(alt, neu):
    """übernommen / neu / umgeschrieben / entfallen über (Einheit,
    alte id) – umgeschriebene Zeilen tragen _um, neue _neu."""
    ueb = sum(1 for r in neu if not r.get("_um") and not r.get("_neu"))
    um = sum(1 for r in neu if r.get("_um"))
    ne = sum(1 for r in neu if r.get("_neu"))
    ent = len(alt) - ueb - um
    return ueb, ne, um, ent


def setze(r, **kw):
    r = copy.deepcopy(r)
    r["_um"] = True
    r.update(kw)
    return r


def fertig(rows):
    out = []
    for r in rows:
        r = copy.deepcopy(r)
        if r["quelle"] in QMAP:
            r["quelle"] = QMAP[r["quelle"]]
        r["id"] = neu_id(r)
        out.append(r)
    return out


def reihe(rows, k, s):
    return [r for r in rows if r["kette_nr"] == k and r["sprosse"] == s]


def ersetze(rows, k, s, neue):
    """Zeilen (k, s) durch die Liste neue ersetzen, Stelle bleibt."""
    out, done = [], False
    for r in rows:
        if r["kette_nr"] == k and r["sprosse"] == s:
            if not done:
                out.extend(neue)
                done = True
            continue
        out.append(r)
    return out


def ersetze_variante(rows, k, s, v, neu):
    return [neu if (r["kette_nr"] == k and r["sprosse"] == s
                    and r["variante"] == v) else r for r in rows]


def lsg(r, k, s, v):
    return [x for x in r if x["kette_nr"] == k and x["sprosse"] == s
            and x["variante"] == v][0]


# ---------------------------------------------------------------- e1
def einheit1():
    alt = lade("e1")
    rows = copy.deepcopy(alt)
    # Vorstufe: Sprossentext länger, Aufgabe dieselbe (übernommen)
    for r in rows:
        if r["kette_nr"] == 2 and r["sprosse"] == 0:
            r["sprosse_text"] = VORSTUFE[1]
    # Grundfall als Päckchen: Kathete a = 36 cm bleibt, b wandert
    v = reihe(rows, 2, 1)[0]
    m = ("Hypotenuse gesucht, Wurzel geht auf; die Kathete a = 36 cm "
         "bleibt, die Kathete b wandert")
    neu = []
    for i, b in enumerate([15, 27, 48, 77, 105], 1):
        c2 = 36 ** 2 + b ** 2
        c = math.isqrt(c2)
        assert c * c == c2
        neu.append(setze(
            v, variante=i, merkmal=m,
            aufgabe=(f"In einem rechtwinkligen Dreieck sind die Katheten "
                     f"$a = 36$ cm und $b = {b}$ cm lang. Berechne die "
                     f"Länge der Hypotenuse $c$."),
            antwort="c² = __, c = __ cm",
            loesung=(f"Gleichung: $c^2 = 36^2 + {b}^2$; Zwischenergebnis: "
                     f"$c^2 = 1\\,296 + {tsd(b*b)} = {tsd(c2)}$; Wurzel: "
                     f"$c = \\sqrt{{{tsd(c2)}}} = {c}$ cm; Ergebnis: "
                     f"$c = {c}$ cm"),
            pruef=f"[{c2}, {c}]", grafik="", loesungsgrafik=""))
    rows = ersetze(rows, 2, 1, neu)
    # Pflicht fehler: v2 → P2 Mehrzahl, v3 → P1 Serie
    f2 = lsg(rows, 5, 1, 2)
    rows = ersetze_variante(rows, 5, 1, 2, setze(
        f2,
        aufgabe=("Nora hat vier Hypotenusen berechnet. Genau eine Rechnung "
                 "ist falsch. Finde sie und rechne sie richtig. \\\\ "
                 "(1) Katheten $16$ cm und $30$ cm: $c = \\sqrt{256 + 900} = "
                 "\\sqrt{1\\,156} = 34$ cm \\\\ "
                 "(2) Katheten $16$ cm und $63$ cm: $c = \\sqrt{256 + "
                 "3\\,969} = \\sqrt{4\\,225} = 65$ cm \\\\ "
                 "(3) Katheten $21$ cm und $28$ cm: $c = \\sqrt{21^2 + 28^2} "
                 "= 21 + 28 = 49$ cm \\\\ "
                 "(4) Katheten $28$ cm und $45$ cm: $c = \\sqrt{784 + "
                 "2\\,025} = \\sqrt{2\\,809} = 53$ cm"),
        loesung=("Rechnung 3 ist falsch: Nora hat die Wurzel aus jedem "
                 "Summanden einzeln gezogen. Zwischenergebnis: $c^2 = 441 + "
                 "784 = 1\\,225$; Wurzel: $c = \\sqrt{1\\,225} = 35$ cm; "
                 "Ergebnis: $c = 35$ cm"),
        pruef="[1225, 35]"))
    f3 = lsg(rows, 5, 1, 3)
    rows = ersetze_variante(rows, 5, 1, 3, setze(
        f3,
        aufgabe=("Tim hat vier Hypotenusen berechnet. Welche Ergebnisse "
                 "können nicht stimmen? Begründe, ohne genau zu rechnen. "
                 "\\\\ (1) Katheten $12$ m und $35$ m: $c = 37$ m \\\\ "
                 "(2) Katheten $11$ cm und $60$ cm: $c = 49$ cm \\\\ "
                 "(3) Katheten $18$ m und $80$ m: $c = 98$ m \\\\ "
                 "(4) Katheten $13$ cm und $84$ cm: $c = 85$ cm"),
        loesung=("Ergebnis 2 kann nicht stimmen: $49$ cm ist kürzer als die "
                 "Kathete $60$ cm, die Hypotenuse muss die längste Seite "
                 "sein. Ergebnis 3 kann nicht stimmen: $98$ m ist genau die "
                 "Summe der Katheten, die Hypotenuse ist aber immer kürzer "
                 "als beide Katheten zusammen."),
        pruef=""))
    # Pflicht begruenden: v3 → P4 Aussagenserie
    b3 = lsg(rows, 5, 2, 3)
    rows = ersetze_variante(rows, 5, 2, 3, setze(
        b3,
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe, ohne genau zu rechnen. \\\\ "
                 "a) Die Hypotenuse liegt immer dem rechten Winkel "
                 "gegenüber. \\\\ "
                 "b) Verdoppelt man nur eine Kathete, dann verdoppelt sich "
                 "immer auch die Hypotenuse. \\\\ "
                 "c) Es gibt ein rechtwinkliges Dreieck, dessen Hypotenuse "
                 "kürzer ist als eine Kathete."),
        loesung=("a) wahr, denn so ist die Hypotenuse festgelegt: die Seite "
                 "gegenüber dem rechten Winkel. b) falsch, z. B. Katheten "
                 "$7$ und $24$: Hypotenuse $25$; mit $14$ und $24$: "
                 "Hypotenuse $\\sqrt{772} \\approx 27{,}8$, nicht $50$. "
                 "c) falsch, denn das Hypotenusenquadrat ist die Summe "
                 "beider Kathetenquadrate und damit größer als jedes "
                 "einzelne."),
        pruef=""))
    # Pflicht anwendung: Urteil zuerst (P8, Urteilsfragen)
    a1 = lsg(rows, 5, 3, 1)
    rows = ersetze_variante(rows, 5, 3, 1, setze(
        a1,
        loesung=("Ja; Diagonale: $\\sqrt{111^2 + 62^2} = \\sqrt{16\\,165} "
                 "\\approx 127{,}1$ cm; in Zoll: $\\frac{127{,}1}{2{,}54} "
                 "\\approx 50$ Zoll; die Angabe stimmt.")))
    a2 = lsg(rows, 5, 3, 2)
    rows = ersetze_variante(rows, 5, 3, 2, setze(
        a2,
        loesung=("Nein; Diagonale der Tür: $\\sqrt{2{,}00^2 + 0{,}90^2} = "
                 "\\sqrt{4{,}81} \\approx 2{,}19$ m; Vergleich: $2{,}19$ m "
                 "ist weniger als $2{,}20$ m, die Platte passt nicht "
                 "hindurch.")))
    return alt, rows


# ---------------------------------------------------------------- e2
def einheit2():
    alt = lade("e2")
    rows = copy.deepcopy(alt)
    # kette_nr ab 2 um eins aufrücken (neuer Erkennungsschritt k2)
    for r in rows:
        if r["kette_nr"] >= 2:
            r["kette_nr"] += 1
    for r in rows:
        if r["kette_nr"] == 3 and r["sprosse"] == 0:
            r["sprosse_text"] = VORSTUFE[2]
    # neuer Erkennungsschritt „Satz oder Umkehrung?“ (Zeile 37)
    vorl = reihe(rows, 1, 0)[0]
    st = "Satz oder Umkehrung?"
    m = ("Wenn-dann-Satz umdrehen und entscheiden, ob die Umkehrung wahr "
         "ist; nichts rechnen")
    daten = [
        ("Der Satz heißt: „Wenn ein Tier ein Hund ist, dann hat es vier "
         "Beine.“ Schreibe die Umkehrung als Wenn-dann-Satz auf. Ist die "
         "Umkehrung wahr? \\janein",
         "nein; Umkehrung: Wenn ein Tier vier Beine hat, dann ist es ein "
         "Hund. Eine Katze hat auch vier Beine und ist kein Hund."),
        ("Der Satz heißt: „Wenn ein Viereck ein Rechteck ist, dann hat es "
         "vier rechte Winkel.“ Schreibe die Umkehrung als Wenn-dann-Satz "
         "auf. Ist die Umkehrung wahr? \\janein",
         "ja; Umkehrung: Wenn ein Viereck vier rechte Winkel hat, dann ist "
         "es ein Rechteck. Jedes solche Viereck ist ein Rechteck."),
        ("Der Satz heißt: „Wenn es regnet, dann ist die Straße nass.“ "
         "Schreibe die Umkehrung als Wenn-dann-Satz auf. Ist die Umkehrung "
         "wahr? \\janein",
         "nein; Umkehrung: Wenn die Straße nass ist, dann regnet es. Die "
         "Straße kann auch vom Gartenschlauch nass sein."),
        ("Der Satz des Pythagoras heißt: „Wenn ein Dreieck einen rechten "
         "Winkel hat, dann sind die beiden Kathetenquadrate zusammen so "
         "groß wie das Hypotenusenquadrat.“ Schreibe die Umkehrung als "
         "Wenn-dann-Satz daneben. Ist die Umkehrung wahr? \\janein",
         "ja; Umkehrung: Wenn in einem Dreieck die beiden kleineren "
         "Seitenquadrate zusammen so groß sind wie das Quadrat der längsten "
         "Seite, dann hat das Dreieck einen rechten Winkel. Das ist die "
         "Umkehrung des Satzes des Pythagoras, sie ist wahr."),
    ]
    neue = []
    for i, (auf, loe) in enumerate(daten, 1):
        r = copy.deepcopy(vorl)
        r.update(kette=st, kette_nr=2, sprosse=0, sprosse_text=st,
                 merkmal=m, hoehe="vorstufe", variante=i, aufgabe=auf,
                 form="ankreuzen", antwort="", loesung=loe, pruef="",
                 original=None, grafik="", loesungsgrafik="", quelle=37,
                 _neu=True)
        neue.append(r)
    k1 = [r for r in rows if r["kette_nr"] == 1]
    rest = [r for r in rows if r["kette_nr"] != 1]
    rows = k1 + neue + rest
    # Grundfall als Päckchen: Hypotenuse 85 cm bleibt, Kathete b wandert
    v = reihe(rows, 3, 1)[0]
    m = ("Kathete gesucht, Hypotenuse gegeben, Wurzel geht auf; die "
         "Hypotenuse c = 85 cm bleibt, die Kathete b wandert")
    neu = []
    for i, b in enumerate([13, 36, 40, 51, 77], 1):
        a2 = 85 ** 2 - b ** 2
        a = math.isqrt(a2)
        assert a * a == a2
        neu.append(setze(
            v, variante=i, merkmal=m,
            aufgabe=(f"In einem rechtwinkligen Dreieck ist die Hypotenuse "
                     f"$c = 85$ cm lang. Eine Kathete ist $b = {b}$ cm "
                     f"lang. Berechne die Länge der Kathete $a$."),
            antwort="a² = __, a = __ cm",
            loesung=(f"Gleichung umstellen: $a^2 = 85^2 - {b}^2$; "
                     f"Zwischenergebnis: $a^2 = 7\\,225 - {tsd(b*b)} = "
                     f"{tsd(a2)}$; Wurzel: $a = \\sqrt{{{tsd(a2)}}} = {a}$ "
                     f"cm; Ergebnis: $a = {a}$ cm"),
            pruef=f"[{a2}, {a}]", grafik="", loesungsgrafik=""))
    rows = ersetze(rows, 3, 1, neu)
    # Pflicht (jetzt k5): fehler v2 → P2 fehlerfrei, v3 → P1 Serie
    f2 = lsg(rows, 5, 1, 2)
    rows = ersetze_variante(rows, 5, 1, 2, setze(
        f2,
        aufgabe=("Ole soll prüfen, ob ein Dreieck mit den Seiten $3{,}3$ m, "
                 "$5{,}6$ m und $6{,}5$ m rechtwinklig ist. Er rechnet so: "
                 "\\rechnung{3{,}3^2 + 5{,}6^2 &= 10{,}89 + 31{,}36 = "
                 "42{,}25 \\\\ 6{,}5^2 &= 42{,}25 \\\\ &\\text{rechtwinklig}}"
                 " Prüfe, ob Ole richtig gerechnet hat. Wenn nicht, rechne "
                 "richtig."),
        loesung=("Richtig. Ole nimmt die längste Seite als Hypotenuse; "
                 "die beiden kleineren Quadrate sind zusammen so groß wie "
                 "das größte, also ist das Dreieck nach der Umkehrung des "
                 "Satzes des Pythagoras rechtwinklig."),
        pruef=""))
    f3 = lsg(rows, 5, 1, 3)
    rows = ersetze_variante(rows, 5, 1, 3, setze(
        f3,
        aufgabe=("Lena hat vier fehlende Katheten berechnet. Welche "
                 "Ergebnisse können nicht stimmen? Begründe, ohne genau zu "
                 "rechnen. \\\\ (1) Hypotenuse $61$ cm, Kathete $11$ cm: "
                 "andere Kathete $60$ cm \\\\ (2) Hypotenuse $26$ m, Kathete "
                 "$10$ m: andere Kathete $27{,}9$ m \\\\ (3) Hypotenuse "
                 "$45$ cm, Kathete $27$ cm: andere Kathete $36$ cm \\\\ "
                 "(4) Hypotenuse $37$ m, Kathete $35$ m: andere Kathete "
                 "$72$ m"),
        loesung=("Ergebnis 2 kann nicht stimmen: die Kathete $27{,}9$ m ist "
                 "länger als die Hypotenuse $26$ m; so ein Ergebnis "
                 "entsteht, wenn man die Quadrate addiert. Ergebnis 4 kann "
                 "nicht stimmen: $72$ m ist länger als die Hypotenuse "
                 "$37$ m, eine Kathete ist immer kürzer."),
        pruef=""))
    # begruenden: v1 → P6 Personenaussage, v3 → P4 Aussagenserie
    b1 = lsg(rows, 5, 2, 1)
    rows = ersetze_variante(rows, 5, 2, 1, setze(
        b1,
        aufgabe=("Mia sagt: „Beim Satz des Pythagoras wird immer addiert, "
                 "auch wenn eine Kathete gesucht ist.“ Begründe, ob Mia "
                 "recht hat."),
        loesung=("Nein; das Hypotenusenquadrat ist die Summe beider "
                 "Kathetenquadrate. Ist eine Kathete gesucht, bleibt ihr "
                 "Quadrat übrig, wenn man das bekannte Kathetenquadrat vom "
                 "Hypotenusenquadrat abzieht: Kathete gesucht heißt minus."),
        pruef=""))
    b3 = lsg(rows, 5, 2, 3)
    rows = ersetze_variante(rows, 5, 2, 3, setze(
        b3,
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe, ohne genau zu rechnen. \\\\ "
                 "a) Bei der Umkehrung nimmt man immer die längste Seite "
                 "als Hypotenuse. \\\\ "
                 "b) Jedes Dreieck, dessen Seitenlängen ganze Zahlen sind, "
                 "ist rechtwinklig. \\\\ "
                 "c) Bei einem sehr flachen rechtwinkligen Dreieck kann eine "
                 "Kathete länger sein als die Hypotenuse."),
        loesung=("a) wahr, denn nur die längste Seite kann dem rechten "
                 "Winkel gegenüberliegen. b) falsch, z. B. Seiten $2$ cm, "
                 "$3$ cm und $4$ cm: $4 + 9 = 13$, aber $4^2 = 16$, also "
                 "kein rechter Winkel. c) falsch, denn das "
                 "Hypotenusenquadrat ist die Summe beider "
                 "Kathetenquadrate und damit immer größer als jedes "
                 "einzelne, auch bei einem flachen Dreieck."),
        pruef=""))
    # anwendung: Urteil zuerst
    a1 = lsg(rows, 5, 3, 1)
    rows = ersetze_variante(rows, 5, 3, 1, setze(
        a1,
        loesung=("Ja; Leiterhöhe: $\\sqrt{30^2 - 14^2} = \\sqrt{704} "
                 "\\approx 26{,}5$ m; mit dem unteren Ende: $26{,}5 + 3 "
                 "\\approx 29{,}5$ m; das ist mehr als $28$ m, die Leiter "
                 "reicht.")))
    a2 = lsg(rows, 5, 3, 2)
    rows = ersetze_variante(rows, 5, 3, 2, setze(
        a2,
        loesung=("Ja; Höhe des Tablets: $\\sqrt{27{,}9^2 - 23{,}7^2} = "
                 "\\sqrt{216{,}72} \\approx 14{,}7$ cm; Vergleich: $23{,}7$ "
                 "cm ist weniger als $24$ cm und $14{,}7$ cm weniger als "
                 "$18$ cm, das Tablet passt.")))
    return alt, rows


# ---------------------------------------------------------------- e3
def dreieck_gs(g, h, einheit, schenkel):
    s = 4.5 / max(g, h)
    x, y = round(g * s, 2), round(h * s, 2)
    return (f"\\dreieck{{(0,0)}}{{({x:g},0)}}{{({x/2:g},{y:g})}}"
            f"{{{schenkel}\\text{{ {einheit}}}}}{{}}"
            f"{{{g}\\text{{ {einheit}}}}}{{}}{{}}{{}}")


def einheit3():
    alt = lade("e3")
    rows = copy.deepcopy(alt)
    # Vorstufe umgeschrieben: Figuren mit Höhe und Körper wie im Katalog
    v0 = reihe(rows, 2, 0)[0]
    m = ("Teildreieck in einer Figur mit Höhe oder in einem Körper "
         "farbig nachfahren und seine Seiten beschriften, nichts rechnen")
    daten = [
        ("Die Figur zeigt ein gleichschenkliges Trapez mit seiner Höhe. "
         "Fahre das rechtwinklige Dreieck aus Höhe, Schenkel und Überstand "
         "farbig nach. Schreibe dazu, welche Seiten Katheten sind und "
         "welche die Hypotenuse ist.",
         "\\trapez[hoehe=h]{5}{3}{2.5}",
         "Katheten: die Höhe und der Überstand; Hypotenuse: der Schenkel"),
        ("Die Figur zeigt ein Parallelogramm mit seiner Höhe. Fahre ein "
         "rechtwinkliges Dreieck mit der Höhe als Seite farbig nach. "
         "Schreibe dazu, welche Seiten Katheten sind und welche die "
         "Hypotenuse ist.",
         "\\parallelogramm[hoehe]{4}{2.5}{60}",
         "Katheten: die Höhe und das Stück der Grundseite bis zum "
         "Fußpunkt; Hypotenuse: die schräge Seite"),
        ("Die Figur zeigt eine Pyramide mit quadratischer Grundfläche. "
         "Fahre das rechtwinklige Dreieck aus Körperhöhe, Seitenhöhe und "
         "halber Grundkante farbig nach. Schreibe dazu, welche Seite die "
         "Hypotenuse ist.",
         "\\pyramide{4}{4}{3}{}{}{h}",
         "Katheten: die Körperhöhe und die halbe Grundkante; Hypotenuse: "
         "die Seitenhöhe"),
        ("Die Figur zeigt einen Kegel. Fahre das rechtwinklige Dreieck aus "
         "Höhe, Radius und Mantellinie farbig nach. Schreibe dazu, welche "
         "Seiten Katheten sind und welche die Hypotenuse ist.",
         "\\kegel{1.5}{3}{r}{h}{s}",
         "Katheten: die Höhe und der Radius; Hypotenuse: die Mantellinie"),
    ]
    neu = []
    for i, (auf, gr, loe) in enumerate(daten, 1):
        neu.append(setze(v0, variante=i, sprosse_text=VORSTUFE[3],
                         merkmal=m, aufgabe=auf, grafik=gr, loesung=loe,
                         pruef="", form="zeichnen", antwort="",
                         loesungsgrafik=""))
    rows = ersetze(rows, 2, 0, neu)
    # Grundfall als Päckchen: Schenkel 65 cm bleibt, Grundseite wandert
    v = reihe(rows, 2, 1)[0]
    m = ("Höhe im gleichschenkligen Dreieck, eine Kathete ist die halbe "
         "Grundseite; der Schenkel 65 cm bleibt, die Grundseite wandert")
    neu = []
    for i, g in enumerate([32, 66, 78, 104, 126], 1):
        hg = g // 2
        h2 = 65 ** 2 - hg ** 2
        h = math.isqrt(h2)
        assert h * h == h2
        neu.append(setze(
            v, variante=i, merkmal=m,
            aufgabe=(f"Die Figur zeigt ein gleichschenkliges Dreieck. Die "
                     f"Grundseite ist ${g}$ cm lang, die Schenkel sind je "
                     f"$65$ cm lang. Berechne die Höhe $h$."),
            antwort="h² = __, h = __ cm",
            loesung=(f"halbe Grundseite: $\\frac{{{g}}}{{2}} = {hg}$ cm; "
                     f"Gleichung umstellen: $h^2 = 65^2 - {hg}^2$; "
                     f"Zwischenergebnis: $h^2 = 4\\,225 - {tsd(hg*hg)} = "
                     f"{tsd(h2)}$; Wurzel: $h = \\sqrt{{{tsd(h2)}}} = {h}$ "
                     f"cm; Ergebnis: $h = {h}$ cm"),
            pruef=f"[{hg}, {h2}, {h}]",
            grafik=dreieck_gs(g, h, "cm", 65), loesungsgrafik=""))
    rows = ersetze(rows, 2, 1, neu)
    # Pflicht k4: fehler v2 → P2 Mehrzahl, v3 → P1 Serie
    f2 = lsg(rows, 4, 1, 2)
    rows = ersetze_variante(rows, 4, 1, 2, setze(
        f2,
        aufgabe=("Jonas hat vier Mantellinien von Kegeln berechnet. Genau "
                 "eine Rechnung ist falsch. Finde sie und rechne sie "
                 "richtig. \\\\ (1) Radius $7$ cm, Höhe $24$ cm: $s = "
                 "\\sqrt{49 + 576} = 25$ cm \\\\ (2) Durchmesser $96$ cm, "
                 "Höhe $55$ cm: $s = \\sqrt{96^2 + 55^2} \\approx 110{,}6$ cm "
                 "\\\\ (3) Radius $36$ cm, Höhe $15$ cm: $s = \\sqrt{1\\,296 "
                 "+ 225} = 39$ cm \\\\ (4) Durchmesser $24$ cm, Höhe $35$ "
                 "cm: $s = \\sqrt{12^2 + 35^2} = 37$ cm"),
        loesung=("Rechnung 2 ist falsch: Jonas hat den Durchmesser statt "
                 "des Radius genommen. Radius: $r = \\frac{96}{2} = 48$ cm; "
                 "Zwischenergebnis: $s^2 = 2\\,304 + 3\\,025 = 5\\,329$; "
                 "Wurzel: $s = \\sqrt{5\\,329} = 73$ cm; Ergebnis: $s = 73$ "
                 "cm"),
        pruef="[48, 5329, 73]"))
    f3 = lsg(rows, 4, 1, 3)
    rows = ersetze_variante(rows, 4, 1, 3, setze(
        f3,
        aufgabe=("Ella hat vier Höhen in gleichschenkligen Dreiecken "
                 "berechnet. Welche Ergebnisse können nicht stimmen? "
                 "Begründe, ohne genau zu rechnen. \\\\ (1) Schenkel $25$ "
                 "cm, Grundseite $14$ cm: Höhe $24$ cm \\\\ (2) Schenkel "
                 "$35$ m, Grundseite $42$ m: Höhe $40{,}8$ m \\\\ "
                 "(3) Schenkel $41$ cm, Grundseite $80$ cm: Höhe $9$ cm "
                 "\\\\ (4) Schenkel $6$ m, Grundseite $4$ m: Höhe $8$ m"),
        loesung=("Ergebnis 2 kann nicht stimmen: die Höhe $40{,}8$ m ist "
                 "länger als der Schenkel $35$ m, im Teildreieck ist der "
                 "Schenkel aber die Hypotenuse. Ergebnis 4 kann nicht "
                 "stimmen: die Höhe $8$ m ist länger als der Schenkel "
                 "$6$ m."),
        pruef=""))
    # begruenden: v1 → P6, v3 → P4
    b1 = lsg(rows, 4, 2, 1)
    rows = ersetze_variante(rows, 4, 2, 1, setze(
        b1,
        aufgabe=("Tom sagt: „Im gleichschenkligen Dreieck sind die "
                 "Grundseite und die Höhe die Katheten.“ Begründe, ob Tom "
                 "recht hat."),
        loesung=("Nein; die Höhe trifft die Grundseite in der Mitte, das "
                 "rechtwinklige Teildreieck hat darum nur die halbe "
                 "Grundseite als Kathete, der Schenkel ist die Hypotenuse."),
        pruef=""))
    b3 = lsg(rows, 4, 2, 3)
    rows = ersetze_variante(rows, 4, 2, 3, setze(
        b3,
        aufgabe=("Entscheide bei jeder Aussage, ob sie wahr oder falsch "
                 "ist. Begründe, ohne genau zu rechnen. \\\\ "
                 "a) Die Seitenhöhe einer Pyramide ist immer länger als "
                 "ihre Körperhöhe. \\\\ "
                 "b) Beim Kegel ist die Mantellinie immer kürzer als die "
                 "Höhe. \\\\ "
                 "c) Die Raumdiagonale eines Würfels ist immer länger als "
                 "die Diagonale einer Seitenfläche."),
        loesung=("a) wahr, denn im Stützdreieck ist die Seitenhöhe die "
                 "Hypotenuse und die Körperhöhe eine Kathete. b) falsch, "
                 "z. B. Radius $9$ cm und Höhe $40$ cm: Mantellinie $41$ cm, "
                 "länger als die Höhe. c) wahr, denn die Raumdiagonale ist "
                 "die Hypotenuse eines Dreiecks, in dem die "
                 "Flächendiagonale eine Kathete ist."),
        pruef=""))
    # anwendung: Urteil zuerst
    a = lsg(rows, 4, 3, 1)
    rows = ersetze_variante(rows, 4, 3, 1, setze(
        a,
        loesung=("Ja; Diagonale des Kofferbodens: $\\sqrt{55^2 + 35^2} = "
                 "\\sqrt{4\\,250} \\approx 65{,}2$ cm; das ist mehr als $62$ "
                 "cm, schräg passt der Schirm hinein.")))
    a = lsg(rows, 4, 3, 2)
    rows = ersetze_variante(rows, 4, 3, 2, setze(
        a,
        loesung=("Nein; längste Strecke im Becher: $\\sqrt{14^2 + 9^2} = "
                 "\\sqrt{277} \\approx 16{,}6$ cm; der Löffel ist $18$ cm "
                 "lang und ragt heraus.")))
    a = lsg(rows, 4, 3, 3)
    rows = ersetze_variante(rows, 4, 3, 3, setze(
        a,
        loesung=("Ja; Bodendiagonale: $d^2 = 1{,}1^2 + 0{,}9^2 = 2{,}02$; "
                 "Raumdiagonale: $2{,}02 + 0{,}5^2 = 2{,}27$; Wurzel: "
                 "$\\sqrt{2{,}27} \\approx 1{,}51$ m; das ist knapp mehr "
                 "als $1{,}5$ m, schräg passt die Angelrute.")))
    # darstellung v2 → rückwärts: von der Rechnung zur Figur (P7)
    d = lsg(rows, 4, 4, 2)
    rows = ersetze_variante(rows, 4, 4, 2, setze(
        d,
        aufgabe=("Zu einem gleichschenkligen Dreieck gehört die Rechnung "
                 "$h^2 = 7^2 - 3^2$. Zeichne eine passende Skizze. "
                 "Beschrifte den Schenkel, die halbe Grundseite und die "
                 "Höhe. Wie lang ist die ganze Grundseite?"),
        loesung=("Skizze: gleichschenkliges Dreieck mit Höhe $h$, Schenkel "
                 "$7$, halbe Grundseite $3$; Grundseite verdoppeln: "
                 "$2 \\cdot 3 = 6$"),
        pruef="6", form="zeichnen", grafik="\\rechenplatz[halb]{4}",
        loesungsgrafik=("\\dreieck{(0,0)}{(3.6,0)}{(1.8,3.79)}{7}{7}{6}"
                        "{}{}{}")))
    return alt, rows


def main():
    e = sys.argv[1]
    alt, rows = {"e1": einheit1, "e2": einheit2, "e3": einheit3}[e]()
    rows = fertig(rows)
    ueb, ne, um, ent = zaehle(alt, rows)
    for r in rows:
        r.pop("_um", None)
        r.pop("_neu", None)
    schreibe(e, rows)
    print(f"{e}: {len(rows)} Zeilen; übernommen {ueb}, neu {ne}, "
          f"umgeschrieben {um}, entfallen {ent}")


if __name__ == "__main__":
    main()

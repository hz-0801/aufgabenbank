#!/usr/bin/env python3
"""Baut neu-rg-duden9.jsonl (koerper, pyramide-kegel-kugel) aus Duden
WÜT Mathematik 9, Kap. 8, und rechnet jede Lösung mit sympy nach.
Vom Buch nur Typ und Stufung; Zahlen und Wortlaut eigen. Vorlage:
baue_neu_pyt.py. Kette, sprosse_text, merkmal, hoehe, quelle werden bei
vorhandenen Sprossen aus der Bank übernommen."""
import json, math
import sympy as sp

Q = "Duden WÜT Mathematik 9 (2017)"
B = "aufgabenbank/bank/"
pi = sp.pi
zeilen, _bank, _zaehl = [], {}, {}


def bank(E, e):
    if (E, e) not in _bank:
        _bank[(E, e)] = [json.loads(l) for l in open(f"{B}{E}/e{e}.jsonl")]
    return _bank[(E, e)]


def neu(E, e, k, s, aufgabe, form, antwort, loesung, pruef, herkunft,
        grafik="", neu_text=None, neu_merkmal=None):
    if neu_text is None:
        g = [r for r in bank(E, e) if r["kette_nr"] == k and r["sprosse"] == s]
        assert g, (E, e, k, s)
        v, n = g[0], len(g)
        kette, st, mk, h, q = v["kette"], v["sprosse_text"], v["merkmal"], v["hoehe"], v["quelle"]
    else:
        v = next(r for r in bank(E, e) if r["kette_nr"] == k)
        kette, st, mk, h, q, n = v["kette"], neu_text, neu_merkmal, "sprosse", v["quelle"], 0
    key = (E, e, k, s)
    _zaehl[key] = _zaehl.get(key, n) + 1
    var = _zaehl[key]
    zeilen.append({
        "id": f"{E}-e{e}-k{k}-s{s}-v{var}", "eintrag": E, "einheit": e,
        "kette": kette, "kette_nr": k, "sprosse": s, "sprosse_text": st,
        "merkmal": mk, "hoehe": h, "variante": var, "aufgabe": aufgabe,
        "form": form, "antwort": antwort, "loesung": loesung,
        "pruef": pruef, "original": None, "grafik": grafik,
        "loesungsgrafik": "", "quelle": q,
        "herkunft": f"{Q}, {herkunft}"})
    if neu_text is None and "pflicht" in v:
        zeilen[-1] = {**{kk: vv for kk, vv in zeilen[-1].items() if kk not in ("variante",)},}
        zz = zeilen[-1]; neu_z = {}
        for kk, vv in zz.items():
            neu_z[kk] = vv
            if kk == "hoehe":
                neu_z["pflicht"] = v["pflicht"]; neu_z["variante"] = var
        zeilen[-1] = neu_z


def P(*paare):
    """paare: (python-ausdruck, sympy-wert); prüft Gleichheit, gibt Liste-String."""
    for a, w in paare:
        x = eval(a, {"math": math})
        assert abs(x - float(sp.N(w, 30))) < 1e-7 * max(1, abs(x)), (a, x, sp.N(w))
    return "[" + ", ".join(a for a, _ in paare) + "]"


def z(w, st=1):
    x = round(float(sp.N(w, 30)) + 1e-12, st)
    s = f"{x:,.{st}f}".replace(",", "X").replace(".", "{,}").replace("X", "\\,")
    return s


K, PKK = "koerper", "pyramide-kegel-kugel"

# ---------- koerper e4 k2 NEU-zylinder-tabelle (S. 100 Nr. 1) ----------
H = "S. 100 Nr. 1 – Größentabelle zum Zylinder: je Zeile zwei Größen gegeben (r oder d, h, Grundfläche, Volumen), die übrigen berechnen"
ST = "Größentabelle: je Zeile zwei Größen gegeben (r oder d, h, G, V), die fehlenden berechnen"
MK = "die Formel wird je Zeile anders herum gebraucht; erst entscheiden, was fehlt"
for r1, h1, d2mm, h2, r3, h3 in [(4, 10, 60, 9, 4, 8), (5, 6, 80, 4, 3, 8)]:
    r2 = sp.Rational(d2mm, 20)
    V2 = pi * r2**2 * h2; G3 = pi * r3**2; V3 = G3 * h3
    G1 = pi * r1**2; M1 = 2 * pi * r1 * h1; O1 = 2 * G1 + M1; V1 = G1 * h1
    # Zeilen 2 und 3: aus gerundeten Angaben zurückrechnen
    V2g = round(float(V2), 1); G3g = round(float(G3), 1); V3g = round(float(V3), 1)
    h2b = V2g / float(pi * r2**2); h3b = V3g / G3g
    assert round(h2b, 1) == h2 and round(h3b, 1) == h3
    neu(K, 4, 2, "NEU-zylinder-tabelle",
        f"Ergänze die fehlenden Größen der drei Zylinder (auf eine Stelle nach dem Komma runden).\\\\ "
        f"Zylinder 1: $r = {r1}$ cm, $h = {h1}$ cm; gesucht $d$, $G$, $M$, $O$, $V$.\\\\ "
        f"Zylinder 2: $d = {d2mm}$ mm, $V = {z(V2g)}$ cm³; gesucht $r$ und $h$.\\\\ "
        f"Zylinder 3: $G = {z(G3g)}$ cm², $V = {z(V3g)}$ cm³; gesucht $h$ und $r$.",
        "teil", "Zylinder 1: d = __, G ≈ __, M ≈ __, O ≈ __, V ≈ __; Zylinder 2: r = __, h ≈ __; Zylinder 3: h ≈ __, r ≈ __",
        f"Zylinder 1: $d = {2*r1}$ cm, $G \\approx {z(G1)}$ cm², $M \\approx {z(M1)}$ cm², $O \\approx {z(O1)}$ cm², $V \\approx {z(V1)}$ cm³; "
        f"Zylinder 2: $r = {z(r2)}$ cm, $h = V : (\\pi \\cdot r^2) \\approx {z(h2)}$ cm; "
        f"Zylinder 3: $h = V : G \\approx {z(h3)}$ cm, $r = \\sqrt{{G : \\pi}} \\approx {z(r3)}$ cm",
        P((f"math.pi*{r1}**2", G1), (f"2*math.pi*{r1}*{h1}", M1), (f"2*math.pi*{r1}**2+2*math.pi*{r1}*{h1}", O1),
          (f"math.pi*{r1}**2*{h1}", V1), (f"{V2g}/(math.pi*{float(r2)}**2)", sp.nsimplify(V2g) / (pi * r2**2)),
          (f"{V3g}/{G3g}", sp.nsimplify(V3g) / sp.nsimplify(G3g)), (f"math.sqrt({G3g}/math.pi)", sp.sqrt(sp.nsimplify(G3g) / pi))),
        H, neu_text=ST, neu_merkmal=MK)

# ---------- koerper e3 k1 NEU-vieleck-grundflaeche (S. 99 Wissen, S. 100 Nr. 2b) ----------
H = "S. 100 Nr. 2b und S. 99 Wissen – Prisma mit Fünfeck- oder Sechseckgrundfläche: Grundfläche zerlegen, dann V und O"
ST = "Fünfeck- oder Sechseckgrundfläche: in Rechteck und Dreieck oder in sechs gleiche Dreiecke zerlegen"
MK = "die Grundfläche hat keine eigene Formel; sie wird erst zerlegt"
G = 6 * 4 + sp.Rational(6 * 2, 2); U = 6 + 4 + 4 + 2 * sp.Rational(36, 10)
neu(K, 3, 1, "NEU-vieleck-grundflaeche",
    "Ein Prisma ist $10$ cm lang. Seine Grundfläche sieht aus wie ein Haus: unten ein Rechteck, $6$ cm breit und $4$ cm hoch, "
    "darauf ein gleichschenkliges Dreieck mit der Höhe $2$ cm. Jede Dachkante ist $3{,}6$ cm lang. Berechne Volumen und Oberfläche.",
    "teil", "V = __ cm³, O ≈ __ cm²",
    f"$G = 6 \\cdot 4 + 6 \\cdot 2 : 2 = {G}$ cm²; $V = {G} \\cdot 10 = {G*10}$ cm³; Umfang $6 + 4 + 4 + 3{{,}}6 + 3{{,}}6 = {z(U)}$ cm; "
    f"$M = {z(U)} \\cdot 10 = {z(U*10,0)}$ cm²; $O = 2 \\cdot {G} + {z(U*10,0)} = {z(2*G+10*U,0)}$ cm²",
    P(("6*4+6*2/2", G), ("(6*4+6*2/2)*10", G * 10), ("(6+4+4+3.6+3.6)*10", U * 10), ("2*(6*4+6*2/2)+(6+4+4+3.6+3.6)*10", 2 * G + 10 * U)),
    H, neu_text=ST, neu_merkmal=MK)
ha = sp.sqrt(4**2 - 2**2); G = 6 * 4 * ha / 2
neu(K, 3, 1, "NEU-vieleck-grundflaeche",
    "Ein Bleistift ist ein gerades Prisma, seine Grundfläche ein regelmäßiges Sechseck mit der Seite $4$ mm. Er ist $120$ mm lang. "
    "Zerlege das Sechseck in sechs gleichseitige Dreiecke. Berechne die Höhe eines Dreiecks, die Grundfläche, das Volumen und die Oberfläche.",
    "teil", "h_a ≈ __ mm, G ≈ __ mm², V ≈ __ mm³, O ≈ __ mm²",
    f"$h_a = \\sqrt{{4^2 - 2^2}} \\approx {z(ha,2)}$ mm; $G = 6 \\cdot 4 \\cdot h_a : 2 \\approx {z(G)}$ mm²; "
    f"$V \\approx {z(G*120,0)}$ mm³; $M = 6 \\cdot 4 \\cdot 120 = 2\\,880$ mm²; $O = 2 \\cdot G + M \\approx {z(2*G+2880)}$ mm²",
    P(("math.sqrt(12)", ha), ("12*math.sqrt(12)", G), ("12*math.sqrt(12)*120", G * 120), ("6*4*120", 2880), ("24*math.sqrt(12)+2880", 2 * G + 2880)),
    H, neu_text=ST, neu_merkmal=MK)

# ---------- koerper e3 k2 s3 Sachaufgabe Deich (S. 100 Nr. 3) ----------
H = "S. 100 Nr. 3 – liegendes Trapezprisma (Damm): Volumen und ein Teil der Oberfläche in Hektar"
V = sp.Rational(20 + 6, 2) * 4 * 2000; A = (2 * sp.Rational(81, 10) + 6) * 2000
neu(K, 3, 2, 3,
    "Ein Deich ist $2$ km lang. Sein Querschnitt ist ein gleichschenkliges Trapez: unten $20$ m breit, oben $6$ m breit, $4$ m hoch; "
    "jede Böschung ist $8{,}1$ m lang. a) Wie viel m³ Erde stecken im Deich? b) Beide Böschungen und die Krone werden mit Gras eingesät. "
    "Wie viel Hektar sind das? ($1$ ha $= 10\\,000$ m²)",
    "teil", "a) __ m³  b) __ ha",
    f"a) $G = (20 + 6) : 2 \\cdot 4 = 52$ m²; $V = 52 \\cdot 2\\,000 = {z(V,0)}$ m³. b) Breite $8{{,}}1 + 6 + 8{{,}}1 = 22{{,}}2$ m; "
    f"$22{{,}}2 \\cdot 2\\,000 = {z(A,0)}$ m² $= {z(A/10000,2)}$ ha. Der Deich enthält $104\\,000$ m³ Erde; eingesät werden $4{{,}}44$ ha.",
    P(("(20+6)/2*4*2000", V), ("22.2*2000", A), ("22.2*2000/10000", A / 10000)), H)

# ---------- koerper e2 k1 NEU-masszahl-wuerfel (S. 100 Nr. 4) ----------
H = "S. 100 Nr. 4 – Würfel, bei dem die Maßzahlen von Oberfläche und Volumen gleich sind (Gleichung 6a² = a³)"
ST = "Maßzahlen von Oberfläche und Volumen vergleichen: 6 · a² = a³ (Vorrat)"
MK = "nicht rechnen, sondern eine Kante suchen, für die zwei Formeln dieselbe Zahl liefern"
a = sp.symbols("a", positive=True)
assert sp.solve(sp.Eq(6 * a**2, a**3), a) == [6]
neu(K, 2, 1, "NEU-masszahl-wuerfel",
    "Berechne für Würfel mit der Kante $2$ cm, $4$ cm, $6$ cm und $8$ cm jeweils die Oberfläche (in cm²) und das Volumen (in cm³). "
    "Bei welchem Würfel ist die Zahl vor cm² gleich der Zahl vor cm³? Begründe mit der Gleichung $6 \\cdot a^2 = a^3$, dass es nur diesen einen gibt.",
    "teil", "a = __ cm",
    "$a = 2$: $O = 24$, $V = 8$; $a = 4$: $O = 96$, $V = 64$; $a = 6$: $O = 216$, $V = 216$; $a = 8$: $O = 384$, $V = 512$. "
    "Gleich bei $a = 6$ cm; $6 \\cdot a^2 = a^3$ geteilt durch $a^2$ ergibt $a = 6$, also nur diese eine Kante.",
    P(("6*6**2", 216), ("6**3", 216)), H, neu_text=ST, neu_merkmal=MK)
assert sp.solve(sp.Eq(a**3, 2 * 6 * a**2), a) == [12]
neu(K, 2, 1, "NEU-masszahl-wuerfel",
    "Bei einem Würfel ist die Zahl vor cm³ (Volumen) doppelt so groß wie die Zahl vor cm² (Oberfläche). Stelle eine Gleichung auf und bestimme die Kante. Mache die Probe.",
    "teil", "a = __ cm",
    "$a^3 = 2 \\cdot 6 \\cdot a^2$, geteilt durch $a^2$: $a = 12$ cm. Probe: $V = 1\\,728$ cm³, $O = 864$ cm², $2 \\cdot 864 = 1\\,728$, beide gleich.",
    P(("2*6", 12), ("12**3", 1728), ("6*12**2", 864)), H, neu_text=ST, neu_merkmal=MK)

# ---------- koerper e4 k2 NEU-hohlzylinder (S. 100 Nr. 5) ----------
H = "S. 100 Nr. 5 – Hohlzylinder (Rohr): Außen- minus Innenzylinder, dann Masse aus der Dichte und urteilen"
ST = "Hohlzylinder (Rohr): Außenzylinder minus Innenzylinder, dann Masse aus der Dichte"
MK = "zwei Radien: das Volumen ist der Unterschied zweier Zylinder"
V = pi * (20**2 - 15**2) * 200; m = V * sp.Rational(24, 10)
neu(K, 4, 2, "NEU-hohlzylinder",
    "Ein Betonrohr ist $2$ m lang, außen $40$ cm und innen $30$ cm im Durchmesser. Beton wiegt $2{,}4$ g pro cm³. "
    "Berechne das Volumen des Betons und die Masse in kg. Können zwei Arbeiter, die zusammen höchstens $100$ kg tragen, das Rohr tragen?",
    "teil", "V ≈ __ cm³, m ≈ __ kg",
    f"$V = \\pi \\cdot (20^2 - 15^2) \\cdot 200 \\approx {z(V,0)}$ cm³; $m \\approx {z(V,0)} \\cdot 2{{,}}4 \\approx {z(m/1000)}$ kg. Nein; das Rohr wiegt rund $264$ kg.",
    P(("math.pi*(20**2-15**2)*200", V), ("math.pi*(20**2-15**2)*200*2.4/1000", m / 1000)), H, neu_text=ST, neu_merkmal=MK)
V = pi * (sp.Rational(11, 10)**2 - 1) * 300; m = V * sp.Rational(89, 10)
neu(K, 4, 2, "NEU-hohlzylinder",
    "Ein Kupferrohr ist $3$ m lang. Außen misst es $22$ mm im Durchmesser, die Wand ist $1$ mm dick. Kupfer wiegt $8{,}9$ g pro cm³. Wie schwer ist das Rohr?",
    "teil", "m ≈ __ kg",
    f"außen $r = 1{{,}}1$ cm, innen $r = 1{{,}}0$ cm; $V = \\pi \\cdot (1{{,}}1^2 - 1^2) \\cdot 300 \\approx {z(V)}$ cm³; "
    f"$m \\approx {z(m,0)}$ g $\\approx {z(m/1000,2)}$ kg. Das Rohr wiegt etwa $1{{,}}76$ kg.",
    P(("math.pi*(1.1**2-1)*300", V), ("math.pi*(1.1**2-1)*300*8.9", m), ("math.pi*(1.1**2-1)*300*8.9/1000", m / 1000)),
    H, neu_text=ST, neu_merkmal=MK)

# ---------- koerper e4 k2 s8 h aus V (S. 100 Nr. 6) ----------
H = "S. 100 Nr. 6 – Füllhöhe im Zylinder aus Litern und Innendurchmesser in mm"
h = sp.Integer(3000) / (pi * 10**2)
neu(K, 4, 2, 8,
    "Ein Kochtopf ist innen $200$ mm weit und $15$ cm hoch. Man gießt $3$ Liter Wasser hinein. Wie hoch steht das Wasser?",
    "teil", "h ≈ __ cm",
    f"$r = 10$ cm, $V = 3\\,000$ cm³; $h = 3\\,000 : (\\pi \\cdot 10^2) \\approx {z(h)}$ cm. Das Wasser steht etwa $9{{,}}5$ cm hoch.",
    P(("3000/(math.pi*10**2)", h)), H)

# ---------- koerper e4 k2 NEU-blatt-rollen (S. 100 Nr. 7) ----------
H = "S. 100 Nr. 7 – Rechteck zum Zylindermantel rollen: Umfang gegeben, r aus dem Umfang, beide Möglichkeiten vergleichen"
ST = "Rechteck zum Mantel rollen: r aus dem Umfang, zwei Möglichkeiten vergleichen"
MK = "der Radius ist nicht gegeben, sondern steckt im Umfang"
for (L, Bb, kr) in [(30, 20, 0), (24, 16, 1)]:
    u1, h1, u2, h2 = L - kr, Bb, Bb - kr, L
    V1 = u1**2 * h1 / (4 * pi); V2 = u2**2 * h2 / (4 * pi)
    r1 = u1 / (2 * pi); r2 = u2 / (2 * pi)
    kl = "" if kr == 0 else f" Zum Kleben überlappt der Rand $1$ cm."
    neu(K, 4, 2, "NEU-blatt-rollen",
        f"Ein Karton ist ${L}$ cm lang und ${Bb}$ cm breit. Er wird zu einer Röhre ohne Boden gerollt, einmal entlang der langen, einmal entlang der kurzen Seite.{kl} "
        "Berechne für beide Röhren Radius und Volumen. Welche fasst mehr?",
        "teil", "lang gerollt: r ≈ __ cm, V ≈ __ cm³; kurz gerollt: r ≈ __ cm, V ≈ __ cm³",
        f"lang gerollt: $u = {u1}$ cm, $h = {h1}$ cm, $r = {u1} : (2\\pi) \\approx {z(r1,2)}$ cm, $V \\approx {z(V1)}$ cm³; "
        f"kurz gerollt: $u = {u2}$ cm, $h = {h2}$ cm, $r \\approx {z(r2,2)}$ cm, $V \\approx {z(V2)}$ cm³. Die lang gerollte Röhre fasst mehr.",
        P((f"{u1}/(2*math.pi)", r1), (f"math.pi*({u1}/(2*math.pi))**2*{h1}", V1), (f"{u2}/(2*math.pi)", r2), (f"math.pi*({u2}/(2*math.pi))**2*{h2}", V2)),
        H, neu_text=ST, neu_merkmal=MK)

# ================= pyramide-kegel-kugel =================
H = "S. 102 Nr. 8 – Pyramide mit Rechteckgrundfläche, Höhe in einer anderen Einheit"
V = sp.Rational(1, 3) * sp.Rational(55, 10) * 4 * 12
neu(PKK, 1, 5, 3,
    "Eine Pyramide hat eine rechteckige Grundfläche mit den Seiten $5{,}5$ cm und $4{,}0$ cm. Sie ist $0{,}12$ m hoch. Berechne ihr Volumen in cm³.",
    "teil", "V = __ cm³", f"$h = 12$ cm; $V = \\frac{{1}}{{3}} \\cdot 5{{,}}5 \\cdot 4 \\cdot 12 = {z(V,0)}$ cm³",
    P(("1/3*5.5*4*12", V)), H)

H = "S. 102 Nr. 9 – Volumen der quadratischen Pyramide, wenn Höhe oder Grundkante verdoppelt wird"
ST = "Höhe oder Grundkante ändern: wie ändert sich das Volumen?"
MK = "nicht ein Volumen ausrechnen, sondern zwei vergleichen; die Kante zählt im Quadrat"
neu(PKK, 1, 5, "NEU-pyramide-verdoppeln",
    "Eine quadratische Pyramide hat $a = 3$ cm und $h = 4$ cm. a) Berechne ihr Volumen. b) Verdopple die Höhe und rechne neu. "
    "c) Verdopple statt dessen die Grundkante und rechne neu. Wie oft passt das alte Volumen jeweils hinein? Begründe.",
    "teil", "a) __ cm³  b) __ cm³, __-fach  c) __ cm³, __-fach",
    "a) $V = \\frac{1}{3} \\cdot 9 \\cdot 4 = 12$ cm³. b) $\\frac{1}{3} \\cdot 9 \\cdot 8 = 24$ cm³, doppelt. c) $\\frac{1}{3} \\cdot 36 \\cdot 4 = 48$ cm³, vierfach; "
    "die Grundkante steht in $a^2$, doppelte Kante gibt vierfache Grundfläche.",
    P(("1/3*3**2*4", 12), ("1/3*3**2*8", 24), ("1/3*6**2*4", 48)), H, neu_text=ST, neu_merkmal=MK)
neu(PKK, 1, 5, "NEU-pyramide-verdoppeln",
    "Bei einer quadratischen Pyramide wird die Grundkante halbiert und die Höhe verdreifacht. Wird das Volumen größer oder kleiner? "
    "Prüfe mit $a = 6$ cm und $h = 5$ cm und gib das neue Volumen als Bruchteil des alten an.",
    "teil", "alt __ cm³, neu __ cm³, Anteil __",
    "alt: $\\frac{1}{3} \\cdot 36 \\cdot 5 = 60$ cm³; neu: $\\frac{1}{3} \\cdot 9 \\cdot 15 = 45$ cm³; kleiner, $\\frac{45}{60} = \\frac{3}{4}$ "
    "(Grundfläche ein Viertel, Höhe dreifach).",
    P(("1/3*36*5", 60), ("1/3*9*15", 45), ("45/60", sp.Rational(3, 4))), H, neu_text=ST, neu_merkmal=MK)

H = "S. 102 Nr. 10 – Höhe der quadratischen Pyramide aus Volumen und Grundkante"
h = sp.Rational(6075, 100) * 3 / sp.Rational(45, 10)**2
neu(PKK, 1, 5, 12,
    "Eine quadratische Pyramide hat die Grundkante $4{,}5$ cm und das Volumen $60{,}75$ cm³. Wie hoch ist sie?",
    "teil", "h = __ cm", f"$G = 4{{,}}5^2 = 20{{,}}25$ cm²; $h = 3 \\cdot 60{{,}}75 : 20{{,}}25 = {z(h,0)}$ cm",
    P(("3*60.75/4.5**2", h)), H)

H = "S. 102 Nr. 11a und Wissen S. 102 – quadratische Pyramide aus Grundkante und Seitenkante: erst Seitenhöhe, dann Höhe, dann V und O"
ST = "aus Grundkante und Seitenkante: erst Seitenhöhe, dann Höhe, dann V und O"
MK = "zwei Stützdreiecke nacheinander; die Höhe ist nicht gegeben"
for aa, ss in [(6, 5), (10, 13)]:
    hs = sp.sqrt(ss**2 - (sp.Rational(aa, 2))**2); hh = sp.sqrt(hs**2 - sp.Rational(aa, 2)**2)
    V = sp.Rational(1, 3) * aa**2 * hh; M = 2 * aa * hs; O = aa**2 + M
    neu(PKK, 1, 5, "NEU-aus-seitenkante",
        f"Eine quadratische Pyramide hat die Grundkante $a = {aa}$ cm und die Seitenkante ${ss}$ cm. Berechne nacheinander die Seitenhöhe $h_s$, "
        "die Höhe $h$, das Volumen und die Oberfläche.",
        "teil", "h_s = __ cm, h ≈ __ cm, V ≈ __ cm³, O = __ cm²",
        f"$h_s = \\sqrt{{{ss}^2 - {aa//2}^2}} = {z(hs,0)}$ cm; $h = \\sqrt{{{z(hs,0)}^2 - {aa//2}^2}} \\approx {z(hh,2)}$ cm; "
        f"$V = \\frac{{1}}{{3}} \\cdot {aa**2} \\cdot h \\approx {z(V)}$ cm³; $M = 4 \\cdot {aa} \\cdot {z(hs,0)} : 2 = {z(M,0)}$ cm²; $O = {aa**2} + {z(M,0)} = {z(O,0)}$ cm²",
        P((f"math.sqrt({ss}**2-{aa/2}**2)", hs), (f"math.sqrt({ss}**2-2*{aa/2}**2)", hh), (f"1/3*{aa}**2*math.sqrt({ss}**2-2*{aa/2}**2)", V),
          (f"2*{aa}*math.sqrt({ss}**2-{aa/2}**2)", M), (f"{aa}**2+2*{aa}*math.sqrt({ss}**2-{aa/2}**2)", O)),
        H, grafik=f"\\pyramide{{3}}{{3}}{{3}}{{${aa}$ cm}}{{}}{{}}", neu_text=ST, neu_merkmal=MK)

H = "S. 102 Nr. 12b – Kegel aus Durchmesser und Mantellinie: Mantel, Oberfläche, Höhe, Volumen"
M = pi * 5 * 13; O = pi * 25 + M; hh = sp.sqrt(13**2 - 5**2); V = pi * 25 * hh / 3
neu(PKK, 2, 2, 8,
    "Ein Kegel hat den Durchmesser $10$ cm und die Mantellinie $s = 13$ cm. Berechne Mantel, Oberfläche, Höhe und Volumen.",
    "teil", "M ≈ __ cm², O ≈ __ cm², h = __ cm, V ≈ __ cm³",
    f"$r = 5$ cm; $M = \\pi \\cdot 5 \\cdot 13 \\approx {z(M)}$ cm²; $O = \\pi \\cdot 5^2 + M \\approx {z(O)}$ cm²; "
    f"$h = \\sqrt{{13^2 - 5^2}} = {z(hh,0)}$ cm; $V = \\frac{{1}}{{3}} \\cdot \\pi \\cdot 5^2 \\cdot 12 \\approx {z(V)}$ cm³",
    P(("math.pi*5*13", M), ("math.pi*25+math.pi*5*13", O), ("math.sqrt(13**2-5**2)", hh), ("math.pi*25*12/3", V)),
    H, grafik="\\kegel{1.2}{3}{}{}{$13$ cm}")

H = "S. 102 Nr. 13 – Kegelförmiger Haufen: r aus dem Umfang, Volumen, Masse, Zahl der Fahrten (aufrunden)"
r = sp.Rational(188, 10) / (2 * pi); V = pi * r**2 * 2 / 3; m = V * sp.Rational(16, 10)
assert 2 < m / 12 < 3
neu(PKK, 2, 3, 4,
    "Ein Kieshaufen hat die Form eines Kegels. Sein Umfang am Boden ist $18{,}8$ m, er ist $2$ m hoch. $1$ m³ Kies wiegt $1{,}6$ t. "
    "Ein Lkw lädt höchstens $12$ t. Wie oft muss er fahren?",
    "teil", "__ Fahrten",
    f"$r = 18{{,}}8 : (2\\pi) \\approx {z(r,2)}$ m; $V = \\frac{{1}}{{3}} \\cdot \\pi \\cdot r^2 \\cdot 2 \\approx {z(V)}$ m³; $m \\approx {z(m)}$ t; "
    f"${z(m)} : 12 \\approx {z(m/12,2)}$, also $3$ Fahrten.",
    P(("18.8/(2*math.pi)", r), ("math.pi*(18.8/(2*math.pi))**2*2/3", V), ("math.pi*(18.8/(2*math.pi))**2*2/3*1.6", m),
      ("math.pi*(18.8/(2*math.pi))**2*2/3*1.6/12", m / 12), ("3", 3)), H)

H = "S. 105 Nr. 14 – Kugelvolumen und -oberfläche aus r oder d in wechselnden Einheiten (mm bis km)"
r = sp.Rational(125, 100); V = sp.Rational(4, 3) * pi * r**3; O = 4 * pi * r**2
neu(PKK, 3, 1, 2,
    "Eine Murmel hat den Durchmesser $25$ mm. Berechne Volumen in cm³ und Oberfläche in cm².", "teil", "V ≈ __ cm³, O ≈ __ cm²",
    f"$r = 1{{,}}25$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot 1{{,}}25^3 \\approx {z(V,2)}$ cm³; $O = 4 \\cdot \\pi \\cdot 1{{,}}25^2 \\approx {z(O,2)}$ cm²",
    P(("4/3*math.pi*1.25**3", V), ("4*math.pi*1.25**2", O)), H)
r = sp.Rational(6, 10); V = sp.Rational(4, 3) * pi * r**3; O = 4 * pi * r**2
neu(PKK, 3, 1, 3,
    "Ein kugelförmiger Asteroid hat den Radius $0{,}6$ km. Berechne Volumen und Oberfläche; runde auf zwei Stellen nach dem Komma.",
    "teil", "V ≈ __ km³, O ≈ __ km²",
    f"$V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot 0{{,}}6^3 \\approx {z(V,2)}$ km³; $O = 4 \\cdot \\pi \\cdot 0{{,}}6^2 \\approx {z(O,2)}$ km²",
    P(("4/3*math.pi*0.6**3", V), ("4*math.pi*0.6**2", O)), H)

H = "S. 105 Nr. 15 und 17 – Masse der Kugel aus Durchmesser und Dichte, mit Urteil"
V = sp.Rational(4, 3) * pi * 2**3; m = V * sp.Rational(85, 10)
neu(PKK, 3, 1, 8,
    "Eine Kugel aus Messing hat den Durchmesser $4$ cm. Messing wiegt $8{,}5$ g pro cm³. Wie schwer ist die Kugel?",
    "teil", "m ≈ __ g",
    f"$r = 2$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot 2^3 \\approx {z(V,2)}$ cm³; $m \\approx {z(m)}$ g. Die Kugel wiegt etwa $285$ g.",
    P(("4/3*math.pi*2**3", V), ("4/3*math.pi*2**3*8.5", m)), H)
V = sp.Rational(4, 3) * pi * 30**3; m = V * sp.Rational(45, 100) / 1000
neu(PKK, 3, 1, 8,
    "Eine Kugel aus Fichtenholz hat den Durchmesser $0{,}6$ m. Fichte wiegt $0{,}45$ g pro cm³. Kann ein Kind, das $20$ kg heben kann, die Kugel anheben?",
    "teil", "m ≈ __ kg",
    f"$r = 30$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot 30^3 \\approx {z(V,0)}$ cm³; $m \\approx {z(m)}$ kg. Nein; die Kugel wiegt rund $51$ kg.",
    P(("4/3*math.pi*30**3", V), ("4/3*math.pi*30**3*0.45/1000", m)), H)

H = "S. 105 Nr. 16 und 18 – Radius aus dem Umfang des größten Kreises (Äquator), dann Volumen oder Oberfläche"
ST = "r aus dem Umfang des größten Kreises (Äquator), dann V oder O"
MK = "gegeben ist ein Umfang; der Radius kommt aus u = 2 · π · r"
r = sp.Integer(70) / (2 * pi); V = sp.Rational(4, 3) * pi * r**3
neu(PKK, 3, 1, "NEU-kugel-umfang",
    "Ein Fußball hat einen Umfang von $70$ cm (einmal ringsum gemessen). Berechne seinen Radius und sein Volumen in Litern.",
    "teil", "r ≈ __ cm, V ≈ __ l",
    f"$r = 70 : (2\\pi) \\approx {z(r,2)}$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot r^3 \\approx {z(V,0)}$ cm³ $\\approx {z(V/1000)}$ l",
    P(("70/(2*math.pi)", r), ("4/3*math.pi*(70/(2*math.pi))**3", V), ("4/3*math.pi*(70/(2*math.pi))**3/1000", V / 1000)),
    H, neu_text=ST, neu_merkmal=MK)
r = sp.Integer(10900) / (2 * pi); O = 4 * pi * r**2
neu(PKK, 3, 1, "NEU-kugel-umfang",
    "Der Mond ist fast eine Kugel; sein Äquator ist etwa $10\\,900$ km lang. Berechne den Radius und die Oberfläche des Mondes (in Millionen km², eine Stelle nach dem Komma).",
    "teil", "r ≈ __ km, O ≈ __ Mio. km²",
    f"$r = 10\\,900 : (2\\pi) \\approx {z(r,0)}$ km; $O = 4 \\cdot \\pi \\cdot r^2 \\approx {z(O/10**6)}$ Mio. km²",
    P(("10900/(2*math.pi)", r), ("4*math.pi*(10900/(2*math.pi))**2/1e6", O / 10**6)), H, neu_text=ST, neu_merkmal=MK)

H = "S. 105 Nr. 19 – Durchmesser im Verhältnis 1 : k, Verhältnis der Oberflächen und Volumen"
Oa, Ob, Va, Vb = 4 * pi * 4, 4 * pi * 36, sp.Rational(4, 3) * pi * 8, sp.Rational(4, 3) * pi * 216
neu(PKK, 3, 1, 12,
    "Kugel A hat den Radius $2$ cm, Kugel B den Radius $6$ cm. Berechne beide Oberflächen und beide Volumen. Wievielmal so groß ist jeweils der Wert von B? "
    "Begründe mit dem Faktor beim Radius.",
    "text", "",
    f"O: A $\\approx {z(Oa)}$ cm², B $\\approx {z(Ob)}$ cm²; V: A $\\approx {z(Va)}$ cm³, B $\\approx {z(Vb)}$ cm³; "
    "der Radius ist dreifach, die Oberfläche wächst mit $r^2$, das Volumen mit $r^3$: Oberfläche $3^2 = 9$-fach, Volumen $3^3 = 27$-fach",
    P(("4*math.pi*2**2", Oa), ("4*math.pi*6**2", Ob), ("4/3*math.pi*2**3", Va), ("4/3*math.pi*6**3", Vb), ("3**2", 9), ("3**3", 27)), H)

H = "S. 106 Wissen und Nr. 20 – Hohlkugel: Volumen außen minus innen, dann Masse"
ST = "Hohlkugel: Volumen außen minus innen, dann Masse aus der Dichte"
MK = "zwei Radien; der Innenradius kommt aus Außenradius minus Wanddicke"
V = sp.Rational(4, 3) * pi * (5**3 - 4**3); m = V * sp.Rational(78, 10)
neu(PKK, 3, 1, "NEU-hohlkugel",
    "Eine hohle Stahlkugel hat außen den Radius $5$ cm, ihre Wand ist $1$ cm dick. Stahl wiegt $7{,}8$ g pro cm³. Wie schwer ist die Kugel?",
    "teil", "m ≈ __ kg",
    f"innen $r = 4$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot (5^3 - 4^3) \\approx {z(V)}$ cm³; $m \\approx {z(m,0)}$ g $\\approx {z(m/1000,2)}$ kg",
    P(("4/3*math.pi*(5**3-4**3)", V), ("4/3*math.pi*(5**3-4**3)*7.8", m), ("4/3*math.pi*(5**3-4**3)*7.8/1000", m / 1000)),
    H, neu_text=ST, neu_merkmal=MK)
V = sp.Rational(4, 3) * pi * (4**3 - sp.Rational(39, 10)**3); m = V * sp.Rational(25, 10)
neu(PKK, 3, 1, "NEU-hohlkugel",
    "Eine Christbaumkugel aus Glas hat außen den Durchmesser $8$ cm, das Glas ist $1$ mm dick. Glas wiegt $2{,}5$ g pro cm³. Wie schwer ist die Kugel?",
    "teil", "m ≈ __ g",
    f"außen $r = 4$ cm, innen $r = 3{{,}}9$ cm; $V = \\frac{{4}}{{3}} \\cdot \\pi \\cdot (4^3 - 3{{,}}9^3) \\approx {z(V,2)}$ cm³; $m \\approx {z(m)}$ g",
    P(("4/3*math.pi*(4**3-3.9**3)", V), ("4/3*math.pi*(4**3-3.9**3)*2.5", m)), H, neu_text=ST, neu_merkmal=MK)

H = "S. 106 Nr. 21 – größte Kugel aus einem Würfel: Abfall in Prozent und Begründung, dass er nicht von der Größe abhängt"
Vk = sp.Rational(4, 3) * pi * 6**3; p = (1728 - Vk) / 1728 * 100
neu(PKK, 3, 1, 10,
    "Aus einem Holzwürfel mit der Kante $12$ cm wird die größte Kugel gedrechselt. a) Berechne das Volumen der Kugel. b) Wie viel Prozent des Holzes fallen ab? "
    "c) Begründe, dass bei jedem Würfel derselbe Anteil abfällt.",
    "teil", "a) __ cm³  b) __ %",
    f"a) $r = 6$ cm; $V \\approx {z(Vk)}$ cm³. b) Würfel $1\\,728$ cm³; Abfall $\\approx {z(1728-Vk)}$ cm³ $\\approx {z(p)}$ \\%. "
    "c) Mit Kante $a$ ist $r = a : 2$, die Kugel hat $\\frac{\\pi}{6} \\cdot a^3$; der Anteil $1 - \\frac{\\pi}{6}$ hängt nicht von $a$ ab.",
    P(("4/3*math.pi*6**3", Vk), ("1728-4/3*math.pi*6**3", 1728 - Vk), ("(1728-4/3*math.pi*6**3)/1728*100", p)), H)

H = "S. 106 Nr. 22 – Körper aus Halbkugel und Kegel (Querschnitt): Masse und Oberfläche"
Vg = sp.Rational(2, 3) * pi * 27 + pi * 9 * 5 / 3; m = Vg * sp.Rational(7, 10); s = sp.sqrt(34); O = 2 * pi * 9 + pi * 3 * s
neu(PKK, 3, 1, 11,
    "Ein Kreisel besteht aus einer Halbkugel mit dem Radius $3$ cm und einem Kegel mit demselben Radius und der Höhe $5$ cm, Spitze nach unten. "
    "Holz wiegt $0{,}7$ g pro cm³. Berechne die Masse des Kreisels und seine Oberfläche.",
    "teil", "m ≈ __ g, O ≈ __ cm²",
    f"$V = \\frac{{2}}{{3}} \\cdot \\pi \\cdot 3^3 + \\frac{{1}}{{3}} \\cdot \\pi \\cdot 3^2 \\cdot 5 \\approx {z(Vg)}$ cm³; $m \\approx {z(m)}$ g; "
    f"$s = \\sqrt{{3^2 + 5^2}} \\approx {z(s,2)}$ cm; $O = 2 \\cdot \\pi \\cdot 3^2 + \\pi \\cdot 3 \\cdot s \\approx {z(O)}$ cm²",
    P(("2/3*math.pi*27+math.pi*9*5/3", Vg), ("(2/3*math.pi*27+math.pi*9*5/3)*0.7", m), ("math.sqrt(34)", s), ("2*math.pi*9+math.pi*3*math.sqrt(34)", O)), H)

H = "S. 104 Wissen und S. 106 Nr. 23 – Kugelabschnitt: Höhe und Schnittradius bestimmen, Formel aus der Formelsammlung"
ST = "Kugelabschnitt mit der Formel aus der Formelsammlung (Vorrat, nur Gymnasium)"
MK = "nur ein Teil der Kugel; Kappenhöhe und Schnittradius erst über ein Stützdreieck"
for R, dd in [(10, 6), (13, 5)]:
    hk = R - dd; r2 = sp.sqrt(R**2 - dd**2); V = pi / 6 * hk * (3 * r2**2 + hk**2); O = pi * (2 * r2**2 + hk**2)
    neu(PKK, 3, 1, "NEU-kugelabschnitt",
        f"Von einer Kugel mit dem Radius ${R}$ cm wird ${dd}$ cm vom Mittelpunkt entfernt eine Kappe abgeschnitten. Bestimme die Höhe $h$ der Kappe und den Radius $r_2$ "
        "der Schnittfläche. Berechne mit $V = \\frac{\\pi}{6} \\cdot h \\cdot (3 r_2^2 + h^2)$ und $O = \\pi \\cdot (2 r_2^2 + h^2)$ Volumen und Oberfläche der Kappe.",
        "teil", "h = __ cm, r₂ = __ cm, V ≈ __ cm³, O ≈ __ cm²",
        f"$h = {R} - {dd} = {hk}$ cm; $r_2 = \\sqrt{{{R}^2 - {dd}^2}} = {z(r2,0)}$ cm; $V \\approx {z(V)}$ cm³; $O \\approx {z(O)}$ cm²",
        P((f"{R}-{dd}", hk), (f"math.sqrt({R}**2-{dd}**2)", r2), (f"math.pi/6*{hk}*(3*({R}**2-{dd}**2)+{hk}**2)", V), (f"math.pi*(2*({R}**2-{dd}**2)+{hk}**2)", O)),
        H, neu_text=ST, neu_merkmal=MK)

with open("neu-rg-duden9.jsonl", "w", encoding="utf-8", newline="\n") as fh:
    for zz in zeilen:
        fh.write(json.dumps(zz, ensure_ascii=False) + "\n")
from collections import Counter
print(len(zeilen), "Zeilen, Lösungen nachgerechnet")
for kk, n in Counter((zz["eintrag"], zz["einheit"], zz["kette_nr"], zz["sprosse"]) for zz in zeilen).items():
    print(kk, n)

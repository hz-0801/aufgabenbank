import json, sys, copy
B = '/tmp/bank-brueche-dezimalzahlen/bank/brueche-dezimalzahlen/'
E = 'brueche-dezimalzahlen'
QMAP = {111: 106, 112: 107, 113: 108, 114: 109, 115: 110, 116: 111, 45: 40}
def fr(z, n): return f"$\\frac{{{z}}}{{{n}}}$"
def dz(x): return "$" + x.replace(",", "{,}") + "$"

def lade(f):
    return [json.loads(l) for l in open(B + f + '.jsonl', encoding='utf-8')]

def reihe(rows, k, s):
    return [r for r in rows if r['kette_nr'] == k and r['sprosse'] == s]

def neu_zeile(vorlage, **kw):
    r = copy.deepcopy(vorlage)
    r.update(kw)
    return r

def setze(r, **kw):
    r = copy.deepcopy(r)
    r['_um'] = True
    r.update(kw)
    return r

# ---------- Päckchen ----------
def paeckchen_e1k1(rows):
    v = reihe(rows, 1, 1)[0]
    m = ("gleich große Teile: Nenner = alle Teile, Zähler = gefärbte Teile; "
         "der Streifen mit 9 Teilen bleibt, die Zahl der gefärbten Teile wandert")
    out = []
    for i, z in enumerate([2, 4, 5, 7, 8], 1):
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe="Der Streifen ist in gleich große Teile geteilt. Welcher Anteil des Streifens ist gefärbt? Gib ihn als Bruch an.",
            loesung=fr(z, 9), pruef=f"[{z}, 9]", grafik=f"\\bruchrechteck{{{z}}}{{9}}"))
    return out

def paeckchen_e1k2(rows):
    v = reihe(rows, 2, 1)[0]
    m = "Zähler 1: nur durch den Nenner teilen; das Ganze 48 bleibt, der Nenner wandert"
    out = []
    for i, n in enumerate([4, 2, 6, 3, 8], 1):
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Berechne $\\frac{{1}}{{{n}}}$ von $48$.",
            loesung=f"$48 : {n} = {48 // n}$", pruef=f"48/{n}"))
    return out

def paeckchen_e2(rows):
    v = reihe(rows, 1, 1)[0]
    m = "Zähler und Nenner mit derselben Zahl malnehmen; der Bruch 2/9 bleibt, die Erweiterungszahl wandert"
    out = []
    for i, k in enumerate([3, 2, 5, 4, 6], 1):
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Erweitere $\\frac{{2}}{{9}}$ mit ${k}$.",
            loesung=(f"Zähler mal {k}: $2 \\cdot {k} = {2*k}$; Nenner mal {k}: "
                     f"$9 \\cdot {k} = {9*k}$; Ergebnis: $\\frac{{2}}{{9}} = \\frac{{{2*k}}}{{{9*k}}}$"),
            pruef=f"[{2*k}, {9*k}]"))
    return out

def paeckchen_e3(rows):
    v = reihe(rows, 1, 1)[0]
    m = "gleiche Nenner: der größere Zähler gibt den größeren Bruch; 6/11 bleibt, der Zähler des zweiten Bruchs wandert"
    out = []
    for i, x in enumerate([9, 4, 10, 2, 7], 1):
        g, k = (x, 6) if x > 6 else (6, x)
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Welcher Bruch ist größer: $\\frac{{6}}{{11}}$ oder $\\frac{{{x}}}{{11}}$?",
            loesung=f"$\\frac{{{g}}}{{11}}$, denn ${g} > {k}$", pruef=f"[{g}, 11]"))
    return out

def paeckchen_e4(rows):
    v = reihe(rows, 1, 1)[0]
    m = "Hundertstel ohne Nullen; der Nenner 100 bleibt, der Zähler wandert"
    out = []
    for i, x in enumerate([23, 47, 29, 71, 96], 1):
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Schreibe $\\frac{{{x}}}{{100}}$ als Dezimalzahl.",
            loesung=f"$0{{,}}{x}$", pruef=f"0.{x}"))
    return out

def paeckchen_e5(rows):
    v = reihe(rows, 2, 1)[0]
    m = "gleich viele Stellen: Stelle für Stelle von links vergleichen; 0,64 bleibt, die zweite Zahl wandert"
    out = []
    for i, x in enumerate(["0,68", "0,61", "0,74", "0,46", "0,69"], 1):
        g = x if float(x.replace(",", ".")) > 0.64 else "0,64"
        out.append(setze(v, variante=i, merkmal=m,
            aufgabe=f"Welche Zahl ist größer: $0{{,}}64$ oder {dz(x)}?",
            loesung=dz(g), pruef=g.replace(",", ".")))
    return out

# ---------- Pflicht ----------
MF = "Rechnung prüfen: Fehler finden oder als richtig erkennen"
MB = "Behauptungen und Aussagen beurteilen, auch ohne Rechnung"
SERIE = "Welche Ergebnisse können nicht stimmen? Begründe, ohne genau zu rechnen."
P4 = "Entscheide bei jeder Aussage, ob sie wahr oder falsch ist. Begründe, ohne genau zu rechnen."

def pflicht(rows, k, einheit):
    f = reihe(rows, k, 1); b = reihe(rows, k, 2); d = reihe(rows, k, 3); a = reihe(rows, k, 4)
    F = [setze(x, merkmal=MF) for x in f]
    Bg = [setze(x, merkmal=MB) for x in b]
    D, A = list(d), list(a)
    if einheit == 1:
        F[1].update(aufgabe="Im Streifen sind $5$ Teile grau und $3$ Teile weiß. Lena schreibt: „Grau ist $\\frac{5}{8}$ des Streifens.“ Prüfe, ob Lena richtig gerechnet hat.",
                    loesung="Richtig. Der Nenner zählt alle Teile des Ganzen, grau und weiß zusammen: $5 + 3 = 8$.", pruef="")
        F[2].update(aufgabe=f"In einer Klasse sind $18$ Kinder, $8$ davon haben ein Haustier. Vier Kinder geben den Anteil der Kinder mit Haustier an. {SERIE} \\\\ (1) $\\frac{{8}}{{18}}$ \\\\ (2) $\\frac{{18}}{{8}}$ \\\\ (3) $\\frac{{8}}{{10}}$ \\\\ (4) $\\frac{{4}}{{9}}$",
                    loesung="Nicht stimmen können (2) und (3). (2): Der Anteil ist größer als ein Ganzes, gemeint ist aber nur ein Teil der Kinder. (3): Der Nenner muss die ganze Klasse oder ein gekürzter Nenner davon sein; $10$ teilt $18$ nicht – $10$ sind die Kinder ohne Haustier.", pruef="", form="text")
        Bg[0].update(aufgabe="Eine Pizza wird gerecht an $4$ Kinder verteilt. Eine gleich große Pizza wird gerecht an $6$ Kinder verteilt. Begründe, warum ein Stück der ersten Pizza größer ist.",
                     loesung="Gleiches Ganzes, weniger Teile: Wird dieselbe Pizza an weniger Kinder verteilt, ist jedes Teil größer, also ist $\\frac{1}{4}$ größer als $\\frac{1}{6}$.")
        Bg[2].update(aufgabe=f"{P4} \\\\ (1) Wenn mehr Kinder einen Kuchen gerecht teilen, wird jedes Stück kleiner. \\\\ (2) Ein Bruch mit größerem Nenner ist immer größer. \\\\ (3) Ein Achtel eines Kuchens ist nie größer als ein Viertel desselben Kuchens.",
                     loesung="(1) wahr, denn dasselbe Ganze wird in mehr gleich große Teile geteilt. (2) falsch, z. B. $\\frac{1}{9}$ ist kleiner als $\\frac{1}{3}$. (3) wahr, denn ein Viertel sind zwei Achtel.")
        A[1] = setze(A[1], antwort="", aufgabe="Du hast $650$ g Mehl. Ein Rezept für $4$ Personen braucht $800$ g Mehl. Du backst für $3$ Personen, also $\\frac{3}{4}$ des Rezepts. Reicht dein Mehl?",
                     loesung="Ja; Bruchteil berechnen: $800 : 4 \\cdot 3 = 600$ g; vergleichen: $600$ g sind weniger als $650$ g, es bleiben $50$ g übrig.", pruef="800/4*3")
    if einheit == 2:
        F[1].update(aufgabe="Tim soll $\\frac{6}{15}$ vollständig kürzen. Er kürzt mit $3$ und erhält $\\frac{2}{5}$. Prüfe, ob Tim richtig gerechnet hat.",
                    loesung="Richtig. $3$ teilt Zähler und Nenner, und $2$ und $5$ haben keinen gemeinsamen Teiler mehr.", pruef="")
        F[2].update(aufgabe=f"Ali hat Brüche erweitert oder gekürzt. {SERIE} \\\\ (1) $\\frac{{4}}{{9}} = \\frac{{8}}{{18}}$ \\\\ (2) $\\frac{{4}}{{9}} = \\frac{{4}}{{18}}$ \\\\ (3) $\\frac{{10}}{{14}} = \\frac{{5}}{{6}}$ \\\\ (4) $\\frac{{3}}{{7}} = \\frac{{12}}{{28}}$",
                    loesung="Nicht stimmen können (2) und (3). (2): Nur der Nenner ist verändert; Zähler und Nenner müssen mit derselben Zahl malgenommen werden. (3): Der Zähler ist halbiert, der Nenner nicht – die Hälfte von $14$ ist $7$.", pruef="")
        Bg[0].update(aufgabe="Man erweitert $\\frac{1}{2}$ mit $3$ und erhält $\\frac{3}{6}$. Begründe, warum der Bruch dadurch nicht größer wird.",
                     loesung="Erweitern verfeinert nur: Jedes Teil wird in $3$ gleiche Teile zerlegt, es gibt dreimal so viele, aber nur ein Drittel so große Teile – der Anteil bleibt gleich.")
        Bg[1].update(aufgabe=f"{P4} \\\\ (1) Beim Erweitern wird ein Bruch immer größer. \\\\ (2) Jeden Bruch kann man erweitern. \\\\ (3) Jeden Bruch kann man kürzen.",
                     loesung="(1) falsch, z. B. $\\frac{1}{2} = \\frac{2}{4}$, beide sind gleich groß. (2) wahr, denn man kann Zähler und Nenner immer mit derselben Zahl malnehmen. (3) falsch, z. B. $\\frac{3}{7}$: $3$ und $7$ haben keinen gemeinsamen Teiler außer $1$.")
        A[1] = setze(A[1], antwort="", aufgabe="Ein Film dauert $1\\frac{3}{4}$ Stunden. Im Parkhaus des Kinos sind die ersten $2$ Stunden kostenlos. Reicht die kostenlose Zeit für den Film?",
                     loesung="Ja; umrechnen: $1\\frac{3}{4}$ Stunden $= 60 + 45 = 105$ min; vergleichen: $105$ min sind weniger als $120$ min.", pruef="60+45")
    if einheit == 3:
        F[1].update(aufgabe="Nina vergleicht $\\frac{2}{5}$ und $\\frac{9}{20}$. Sie schreibt: $\\frac{2}{5} = \\frac{8}{20} < \\frac{9}{20}$. Prüfe, ob Nina richtig gerechnet hat.",
                    loesung="Richtig. Sie hat $\\frac{2}{5}$ mit $4$ auf Zwanzigstel erweitert; bei gleichem Nenner entscheidet der größere Zähler.", pruef="")
        F[2].update(aufgabe=f"Vier Kinder haben Brüche verglichen. {SERIE} \\\\ (1) $\\frac{{5}}{{6}} > \\frac{{5}}{{9}}$ \\\\ (2) $\\frac{{4}}{{5}} > \\frac{{11}}{{12}}$ \\\\ (3) $\\frac{{3}}{{11}} > \\frac{{3}}{{4}}$ \\\\ (4) $\\frac{{7}}{{8}} > \\frac{{3}}{{8}}$",
                    loesung="Nicht stimmen können (2) und (3). (2): Bei $\\frac{4}{5}$ fehlt ein Fünftel, bei $\\frac{11}{12}$ nur ein Zwölftel – es fehlt nicht gleich viel. (3): Gleicher Zähler, aber Elftel sind kleiner als Viertel.", pruef="")
        Bg[1].update(aufgabe="Max sagt: „$\\frac{2}{11}$ ist größer als $\\frac{2}{9}$, weil $11$ größer ist als $9$.“ Begründe, ob Max recht hat.",
                     loesung="Nein; bei gleichem Zähler gilt: größerer Nenner, kleinerer Bruch – Elftel sind kleiner als Neuntel.")
        Bg[2].update(aufgabe=f"{P4} \\\\ (1) Ein Bruch, dessen Zähler größer ist als der Nenner, ist immer größer als $1$. \\\\ (2) Von zwei Brüchen ist der mit dem größeren Nenner immer der größere. \\\\ (3) Es gibt einen Bruch, der größer als $\\frac{{1}}{{2}}$ und kleiner als $1$ ist.",
                     loesung="(1) wahr, denn dann sind mehr Teile gemeint, als das Ganze hat. (2) falsch, z. B. $\\frac{1}{9}$ ist kleiner als $\\frac{1}{4}$. (3) wahr, z. B. $\\frac{2}{3}$.")
        MD = "zwischen Zahlenstrahl, Bruch und Worten wechseln, in beide Richtungen"
        D = [setze(x, merkmal=MD) for x in d]
        D[2].update(aufgabe="Beschreibe in Worten, wo $\\frac{5}{4}$ am Zahlenstrahl liegt, ohne ihn zu zeichnen.",
                    loesung="$\\frac{5}{4} = 1\\frac{1}{4}$: ein Viertel rechts von der $1$, zwischen $1$ und $2$.",
                    pruef="[5, 4]", form="text", grafik="", loesungsgrafik="")
        A[0] = setze(A[0], antwort="", aufgabe="Ein Handy-Akku muss für einen Ausflug mindestens zu $\\frac{2}{3}$ geladen sein. Die Anzeige zeigt $\\frac{3}{4}$. Reicht die Ladung?",
                     loesung="Ja; gleichnamig machen: $\\frac{2}{3} = \\frac{8}{12}$ und $\\frac{3}{4} = \\frac{9}{12}$; vergleichen: $\\frac{9}{12}$ ist größer als $\\frac{8}{12}$.", pruef="[9, 12]")
    if einheit == 4:
        F[1].update(aufgabe="Omar soll $\\frac{3}{100}$ als Dezimalzahl schreiben. Er schreibt: $\\frac{3}{100} = 0{,}03$. Prüfe, ob Omar richtig gerechnet hat.",
                    loesung="Richtig. Hundertstel stehen an der zweiten Stelle nach dem Komma, die Zehntelstelle bekommt eine Null.", pruef="")
        F[2].update(aufgabe=f"Ida hat Zehnerbrüche als Dezimalzahlen geschrieben. {SERIE} \\\\ (1) $\\frac{{9}}{{1\\,000}} = 0{{,}}09$ \\\\ (2) $\\frac{{13}}{{100}} = 0{{,}}13$ \\\\ (3) $\\frac{{6}}{{10}} = 0{{,}}06$ \\\\ (4) $\\frac{{21}}{{1\\,000}} = 0{{,}}021$",
                    loesung="Nicht stimmen können (1) und (3). (1): Tausendstel brauchen drei Stellen nach dem Komma, das Ergebnis hat nur zwei. (3): Zehntel haben eine Stelle nach dem Komma, das Ergebnis hat zwei.", pruef="")
        Bg[1].update(aufgabe="Emil sagt: „$\\frac{6}{10}$ und $\\frac{60}{100}$ sind verschiedene Dezimalzahlen, denn $60$ ist mehr als $6$.“ Begründe, ob Emil recht hat.",
                     loesung="Nein; $\\frac{60}{100}$ ist $\\frac{6}{10}$ erweitert mit $10$, beide sind $0{,}6$ – eine angehängte Null ändert den Wert nicht.")
        Bg[2].update(aufgabe=f"{P4} \\\\ (1) Jeden Bruch kann man auf den Nenner $10$, $100$ oder $1\\,000$ erweitern. \\\\ (2) Eine Dezimalzahl mit zwei Stellen nach dem Komma ist immer eine Zahl von Hundertsteln. \\\\ (3) Hängt man hinten an die Stellen nach dem Komma eine Null an, ändert sich der Wert nie.",
                     loesung="(1) falsch, z. B. $\\frac{1}{3}$: $3$ teilt weder $10$ noch $100$ noch $1\\,000$. (2) wahr, denn die zweite Stelle zählt Hundertstel, z. B. $0{,}37 = \\frac{37}{100}$. (3) wahr, denn z. B. $0{,}4$ und $0{,}40$ sind beide $4$ Zehntel.")
        A[2] = setze(A[2], aufgabe="Lukas will heute mindestens $1{,}5$ km laufen. Eine Runde auf dem Sportplatz ist $\\frac{2}{5}$ km lang. Er läuft $4$ Runden. Reicht das?",
                     loesung="Ja; umwandeln: $\\frac{2}{5}$ km $= 0{,}4$ km; Strecke berechnen: $4 \\cdot 0{,}4 = 1{,}6$ km; vergleichen: $1{,}6$ km sind mehr als $1{,}5$ km.",
                     pruef="4*0.4", antwort="")
    if einheit == 5:
        F[1].update(aufgabe=f"Ben hat Quadrate von Dezimalzahlen berechnet. {SERIE} \\\\ (1) $0{{,}}3^2 = 0{{,}}6$ \\\\ (2) $0{{,}}2^2 = 0{{,}}04$ \\\\ (3) $0{{,}}5^2 = 2{{,}}5$ \\\\ (4) $0{{,}}1^2 = 0{{,}}01$",
                    loesung="Nicht stimmen können (1) und (3). (1): Das Quadrat einer Zahl zwischen $0$ und $1$ ist kleiner als die Zahl, $0{,}6$ ist aber größer als $0{,}3$. (3): Das Ergebnis ist sogar größer als $1$; außerdem hat das Quadrat von Zehnteln zwei Stellen nach dem Komma.", pruef="")
        F[2].update(aufgabe="Mona soll Zahlen von klein nach groß ordnen. Sie schreibt: $1{,}625$; $1{,}65$; $1{,}7$. Prüfe, ob Mona richtig geordnet hat.",
                    loesung="Richtig. Mit Nullen aufgefüllt gilt $1{,}625 < 1{,}650 < 1{,}700$; die Stellenwerte entscheiden, nicht die Länge der Zahl.", pruef="")
        Bg[1].update(aufgabe="Tim sagt: „$0{,}40$ ist größer als $0{,}4$, weil $40$ größer ist als $4$.“ Begründe, ob Tim recht hat.",
                     loesung="Nein; beide sind gleich: $40$ Hundertstel sind $4$ Zehntel, eine angehängte Null ändert den Wert nicht.")
        Bg[2].update(aufgabe=f"{P4} \\\\ (1) Eine Dezimalzahl mit mehr Stellen nach dem Komma ist immer größer. \\\\ (2) Das Quadrat einer Zahl zwischen $0$ und $1$ ist immer kleiner als die Zahl selbst. \\\\ (3) Zwischen zwei Dezimalzahlen liegt immer noch eine weitere.",
                     loesung="(1) falsch, z. B. $0{,}39$ ist kleiner als $0{,}4$. (2) wahr, denn man nimmt einen Teil der Zahl, z. B. $0{,}7^2 = 0{,}49$. (3) wahr, denn man hängt eine Stelle an, z. B. liegt $0{,}65$ zwischen $0{,}6$ und $0{,}7$.")
        A[1] = setze(A[1], antwort="", aufgabe="Auf der Klassenfahrt darf ein Koffer höchstens $15$ kg wiegen. Die Waage zeigt $14{,}98$ kg. Darf der Koffer mit?",
                     loesung="Ja; Nullen anhängen: $15$ kg $= 15{,}00$ kg; vergleichen: $14{,}98$ kg sind weniger als $15{,}00$ kg.", pruef="15")
    return F + Bg + D + A

# ---------- Zusammenbau ----------
def nummeriere(rows):
    out = []
    for r in rows:
        r = copy.deepcopy(r)
        if r['quelle'] in QMAP:
            r['quelle'] = QMAP[r['quelle']]
        out.append(r)
    return out

def ids(rows, einheit):
    for r in rows:
        r['id'] = f"{E}-e{einheit}-k{r['kette_nr']}-s{r['sprosse']}-v{r['variante']}"
    return rows

def kette(rows, k, s):
    return [copy.deepcopy(r) for r in reihe(rows, k, s)]

def schreibe(f, rows, einheit, alt):
    rows = ids(rows, einheit)
    altmap = {r['id']: r for r in alt}
    st = {'uebernommen': 0, 'neu': 0, 'umgeschrieben': 0}
    for r in rows:
        if r.pop('_neu', False):
            st['neu'] += 1
        elif r.pop('_um', False):
            st['umgeschrieben'] += 1
        else:
            st['uebernommen'] += 1
        r.pop('_um', None)
    st['entfallen'] = len(alt) - st['uebernommen'] - st['umgeschrieben']
    with open(B + f + '.jsonl', 'w', encoding='utf-8', newline='\n') as h:
        for r in rows:
            h.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f, len(rows), st)

def vorstufe_text(rows, k, text):
    return [setze(r, sprosse_text=text) for r in kette(rows, k, 0)]

def baue(einheit):
    alt = lade(f'e{einheit}')
    R = nummeriere(alt)
    if einheit == 1:
        rows = (kette(R, 1, 0) + paeckchen_e1k1(R) + sum([kette(R, 1, s) for s in range(2, 7)], [])
                + kette(R, 2, 0) + paeckchen_e1k2(R) + sum([kette(R, 2, s) for s in range(2, 7)], [])
                + kette(R, 3, 1) + pflicht(R, 4, 1))
    if einheit == 2:
        rows = (vorstufe_text(R, 1, "„Erweitert oder gekürzt – mit welcher Zahl?“") + paeckchen_e2(R)
                + sum([kette(R, 1, s) for s in range(2, 9)], []) + kette(R, 2, 1) + kette(R, 3, 1) + pflicht(R, 4, 2))
    if einheit == 3:
        rows = (vorstufe_text(R, 1, "„Welcher Vergleichsweg?“") + paeckchen_e3(R)
                + sum([kette(R, 1, s) for s in range(2, 8)], []) + kette(R, 2, 1) + pflicht(R, 3, 3))
    if einheit == 4:
        gf = paeckchen_e4(R)
        v = gf[0]
        neu = []
        for i, (txt, sol) in enumerate([
            ("Eine Zahl hat $4$ Einer, $2$ Zehntel und $6$ Hundertstel. Schreibe sie als Dezimalzahl.", "4,26"),
            ("Eine Zahl hat $5$ Einer, $0$ Zehntel und $7$ Hundertstel. Schreibe sie als Dezimalzahl.", "5,07"),
            ("Eine Zahl hat $0$ Einer, $9$ Zehntel, $0$ Hundertstel und $4$ Tausendstel. Schreibe sie als Dezimalzahl.", "0,904")], 1):
            r = neu_zeile(v, sprosse=2, variante=i, hoehe="sprosse",
                sprosse_text="Stellen einzeln gegeben → Dezimalzahl",
                merkmal="die Stellen stehen einzeln da und werden zu einer Dezimalzahl zusammengesetzt, auch mit einer Null-Stelle",
                aufgabe=txt, antwort="__", loesung=dz(sol), pruef=sol.replace(",", "."), grafik="", loesungsgrafik="")
            r.pop('_um', None); r['_neu'] = True
            neu.append(r)
        rest = []
        for s in range(2, 9):
            for r in kette(R, 1, s):
                r['sprosse'] = s + 1
                rest.append(r)
        rows = (vorstufe_text(R, 1, "„Wie viele Nachkommastellen?“") + gf + neu + rest
                + kette(R, 2, 1) + kette(R, 3, 1) + pflicht(R, 4, 4))
    if einheit == 5:
        gf = paeckchen_e5(R)
        v = gf[0]
        vs = []
        for i, (x, y, st) in enumerate([("3,52", "3,58", "an der Hundertstelstelle"),
                                        ("0,71", "0,81", "an der Zehntelstelle"),
                                        ("12,4", "13,4", "an der Einerstelle"),
                                        ("2,305", "2,309", "an der Tausendstelstelle")], 1):
            r = neu_zeile(v, sprosse=0, variante=i, hoehe="vorstufe",
                sprosse_text="„Wo entscheidet es sich?“",
                merkmal="nur die Stelle nennen, an der sich die Zahlen zuerst unterscheiden; kein Zeichen setzen",
                aufgabe=f"Die Zahlen {dz(x)} und {dz(y)} haben gleich viele Stellen. An welcher Stelle unterscheiden sie sich zuerst? Setze kein Vergleichszeichen.",
                antwort="__", loesung=st, pruef="")
            r.pop('_um', None); r['_neu'] = True
            vs.append(r)
        nullen = []
        for r in kette(R, 2, 0)[:3]:
            r['sprosse'] = 2; r['hoehe'] = 'sprosse'
            r['_um'] = True
            nullen.append(r)
        rest = []
        for s in range(2, 10):
            for r in kette(R, 2, s):
                r['sprosse'] = s + 1
                rest.append(r)
        rows = (kette(R, 1, 0) + vs + gf + nullen + rest
                + kette(R, 3, 1) + kette(R, 4, 1) + kette(R, 5, 1) + pflicht(R, 6, 5))
    schreibe(f'e{einheit}', rows, einheit, alt)

if __name__ == '__main__':
    baue(int(sys.argv[1]))

"""M2 Setzer (09.10.2026): Satzangaben des Hand-Satzes T6B in die Bank.

Liest die TikZ-Bilder aus bau/proben/2026-10-09/kathete-berechnen/2-blatt.tex
(in Blattfolge) und schreibt je Blattzeile von T6B das Feld grafik (TikZ
ganz; mehrere Bilder nacheinander, je Teil eins) und das Feld satz
(bank.md „Felder für den Lernweg“) in bank/pythagoras/e2.jsonl.
Einmalig; ein zweiter Lauf schreibt dasselbe noch einmal (idempotent).
"""
import json
import re
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
DATEI = WURZEL / "bank/pythagoras/e2.jsonl"
TEX = WURZEL / "bau/proben/2026-10-09/kathete-berechnen/2-blatt.tex"

bilder = re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}",
                    TEX.read_text(encoding="utf-8"), re.S)
assert len(bilder) == 12, len(bilder)
B = iter(bilder)


def nimm(n):
    return "\n".join(next(B) for _ in range(n))


KH = [["Hypotenuse"], ["Kathete"]]
SATZ = {
    # Nr. 1 – L2k-1
    "pythagoras-e2-k6-s2-v4": (nimm(1), {
        "form": "zwei",
        "text": "Die zwei kleinen Quadrate über den Katheten haben zusammen "
                "so viel Fläche wie das große Quadrat über der Hypotenuse. "
                "Hier fehlt eine Fläche.",
        "teile": [
            {"text": "Wie groß ist die Fläche des Quadrats mit dem "
                     "Fragezeichen?", "luecke": "cm$^2$"},
            {"text": "Wie lang ist die Seite dieses Quadrats?",
             "luecke": "cm"}],
        "fuss": ["64 cm²", "8 cm"],
        "loesung": [["$64$ cm$^2$", "$100 - 36 = 64$"],
                    ["$8$ cm", "$\\sqrt{64} = 8$"]]}),
    # Nr. 2 – L2k-2
    "pythagoras-e2-k3-s0-v5": (nimm(4), {
        "form": "reihe",
        "text": "Zwei Seiten sind gegeben. Ist die Seite mit dem "
                "Fragezeichen die Hypotenuse oder eine Kathete? Kreuze an.",
        "teile": [{"kreuz": KH}, {"kreuz": KH}, {"kreuz": KH},
                  {"kreuz": KH}],
        "fuss": ["H", "K", "K", "H"],
        "loesung": [["Hypotenuse", "gegenüber dem rechten Winkel"],
                    ["Kathete", "Hypotenuse ist die $17$-cm-Seite"],
                    ["Kathete", "Hypotenuse ist die $25$-cm-Seite"],
                    ["Hypotenuse", "gegenüber dem rechten Winkel"]]}),
    # Nr. 3 – L2k-3
    "pythagoras-e2-k6-s4-v4": (nimm(3), {
        "form": "reihe",
        "text": "Schreibe den Satz des Pythagoras für das Dreieck auf. "
                "Stelle die Gleichung dann so um, dass das Quadrat der "
                "gesuchten Seite allein steht.",
        "teile": [
            {"text": "gesucht: $u$", "grau": True,
             "zeilen": ["$w^2 = u^2 + v^2$",
                        "$\\Rightarrow\\ u^2 = w^2 - v^2$"]},
            {"text": "gesucht: $q$", "linien": 2},
            {"text": "gesucht: $\\overline{BC}$", "linien": 2}],
        "fuss": ["$q^2 = r^2 - p^2$", "$\\overline{BC}^2 = "
                "\\overline{AC}^2 - \\overline{AB}^2$"],
        "loesung": [
            ["$q^2 = r^2 - p^2$", "$r^2 = p^2 + q^2$, Hypotenuse $r$"],
            ["$\\overline{BC}^2 = \\overline{AC}^2 - \\overline{AB}^2$",
             "rechter Winkel bei $B$: $\\overline{AC}^2 = \\overline{AB}^2 "
             "+ \\overline{BC}^2$"]]}),
    # Nr. 4 – L2k-3 (Original ganz)
    "pythagoras-e2-k3-s5-v4": (nimm(1), {
        "form": "zwei", "marke": "P10 ’24",
        "text": "Im Dreieck sind $y$ und $z$ die Katheten, $x$ ist die "
                "Hypotenuse. Kreuze die Gleichung an, mit der man die Länge "
                "von $z$ berechnen kann.",
        "kreuz": [["$z = x^2 - y^2$", "$z = \\sqrt{x^2 + y^2}$"],
                  ["$z = x + y$", "$z = \\sqrt{x^2 - y^2}$"]],
        "fuss": "$z = \\sqrt{x^2 - y^2}$",
        "loesung": [["$z = \\sqrt{x^2 - y^2}$",
                     "$x^2 = y^2 + z^2$ \\ $\\Rightarrow$ \\ "
                     "$z^2 = x^2 - y^2$"]]}),
    # Nr. 5 – L2k-4
    "pythagoras-e2-k3-s1-v6": ("", {
        "form": "paeckchen",
        "text": "Die Hypotenuse und eine Kathete eines rechtwinkligen "
                "Dreiecks sind gegeben. Berechne die andere Kathete.",
        "teile": [
            {"text": "Hypotenuse $10$ cm, Kathete $6$ cm:", "grau": True,
             "zeilen": ["$a^2 = 10^2 - 6^2 = 100 - 36 = 64$", "$\\Rightarrow$",
                        "$a = \\sqrt{64} = 8$ cm"]},
            {"text": "Hypotenuse $13$ cm, Kathete $5$ cm", "karo": 3},
            {"text": "Hypotenuse $25$ cm, Kathete $7$ cm", "karo": 3}],
        "nach": "Prüfe dein Ergebnis: Die Kathete ist kürzer als die "
                "Hypotenuse.",
        "fuss": ["12 cm", "24 cm"],
        "loesung": [["$12$ cm", "$13^2 - 5^2 = 144$ \\ $\\Rightarrow$ "
                     "\\ $\\sqrt{144} = 12$; \\ $12 < 13$"],
                    ["$24$ cm", "$25^2 - 7^2 = 576$ \\ $\\Rightarrow$ "
                     "\\ $\\sqrt{576} = 24$"]]}),
    # Nr. 6 – L2k-5, zwei Zeilen auf einer Nummer (zweite: folgt)
    "pythagoras-e2-k3-s2-v3": ("", {
        "form": "paeckchen",
        "text": "Berechne die fehlende Kathete. Runde, wo nötig, auf eine "
                "Stelle nach dem Komma.",
        "teile": [{"text": "Hypotenuse $8$ cm, Kathete $3$ cm", "karo": 3}],
        "fuss": ["7,4 cm"],
        "loesung": [["$\\sqrt{55} \\approx 7{,}4$ cm",
                     "$8^2 - 3^2 = 55$ \\ $\\Rightarrow$ \\ "
                     "$\\sqrt{55} \\approx 7{,}416$"]]}),
    "pythagoras-e2-k3-s3-v4": ("", {
        "form": "paeckchen", "folgt": True,
        "teile": [{"text": "Hypotenuse $1{,}3$ m, Kathete $50$ cm",
                   "karo": 3}],
        "fuss": ["120 cm"],
        "loesung": [["$120$ cm $= 1{,}2$ m",
                     "$1{,}3$ m $= 130$ cm; \\ $130^2 - 50^2 = 14\\,400$"]]}),
    # Nr. 7–9 – L2k-6
    "pythagoras-e2-k3-s7-v4": (nimm(1), {
        "form": "zwei",
        "text": "Tim spannt ein Seil von der Spitze der Zeltstange bis zu "
                "einem Hering im Boden. Das Seil ist $3{,}4$ m lang. Reicht "
                "der Platz bis zum Zaun dafür?",
        "karo": 3, "kreuz": [["ja", "nein"]],
        "fuss": "nein, gebraucht werden 3 m",
        "loesung": [["nein", "Abstand des Herings: $\\sqrt{3{,}4^2 - "
                     "1{,}6^2} = \\sqrt{9} = 3$ m $> 2{,}8$ m"]]}),
    "pythagoras-e2-k3-s11-v4": (nimm(1), {
        "form": "zwei",
        "text": "Ein Boot fährt bei $A$ los und will genau gegenüber "
                "anlegen. Die Strömung treibt es ab. Es legt bei $B$ an, "
                "$90$ m flussabwärts. Wie lang war die Fahrt von $A$ nach "
                "$B$?",
        "karo": 3,
        "fuss": "150 m",
        "loesung": [["$150$ m", "Hypotenuse gesucht: $\\sqrt{120^2 + "
                     "90^2} = \\sqrt{22\\,500} = 150$"]]}),
    "pythagoras-e2-k6-s3-v3": ("", {
        "form": "frei",
        "nach": "Skizziere zuerst die Lage.",
        "karo": 4,
        "fuss": "53 m",
        "loesung": [["$53$ m", "$\\sqrt{65^2 - 39^2} = \\sqrt{2\\,704} "
                     "= 52$; \\ $52 + 1 = 53$"]]}),
    # Nr. 10 – L2k-7
    "pythagoras-e2-k3-s12-v7": (nimm(1), {
        "form": "zwei", "marke": "nach P10 ’24",
        "text": "Eine Seilbahn fährt von der Talstation $B$ zur Bergstation "
                "$A$. Das Seil $\\overline{AB}$ ist $384$ m lang. Der Punkt "
                "$F$ liegt senkrecht unter $A$. Die Strecke $\\overline{FA}$ "
                "ist der Höhenunterschied zwischen $B$ und $A$. Berechne "
                "diesen Höhenunterschied. Runde auf eine Stelle nach dem "
                "Komma.",
        "karo": 3,
        "fuss": "287,1 m",
        "loesung": [["$\\overline{FA} = \\sqrt{82\\,431} \\approx "
                     "287{,}1$ m", "$\\overline{FA}^2 = 384^2 - 255^2 = "
                     "82\\,431$ \\ $\\Rightarrow$ \\ $\\overline{FA} "
                     "\\approx 287{,}11$"]]}),
    # Zusatz L2k-4 (neue Zahlen, nicht auf T6B): Satz wie Nr. 5
    "pythagoras-e2-k3-s1-v7": ("", {
        "form": "paeckchen",
        "text": "Die Hypotenuse und eine Kathete eines rechtwinkligen "
                "Dreiecks sind gegeben. Berechne die andere Kathete.",
        "teile": [
            {"text": "Hypotenuse $17$ cm, Kathete $8$ cm", "karo": 3},
            {"text": "Hypotenuse $15$ cm, Kathete $9$ cm", "karo": 3},
            {"text": "Hypotenuse $26$ cm, Kathete $10$ cm", "karo": 3}],
        "nach": "Prüfe dein Ergebnis: Die Kathete ist kürzer als die "
                "Hypotenuse.",
        "fuss": ["15 cm", "12 cm", "24 cm"],
        "loesung": [["$15$ cm", "$17^2 - 8^2 = 225$ \\ $\\Rightarrow$ "
                     "\\ $\\sqrt{225} = 15$"],
                    ["$12$ cm", "$15^2 - 9^2 = 144$ \\ $\\Rightarrow$ "
                     "\\ $\\sqrt{144} = 12$"],
                    ["$24$ cm", "$26^2 - 10^2 = 576$ \\ $\\Rightarrow$ "
                     "\\ $\\sqrt{576} = 24$"]]}),
}
assert next(B, None) is None

zeilen = DATEI.read_text(encoding="utf-8").splitlines()
neu, gesetzt = [], set()
for z in zeilen:
    a = json.loads(z)
    if a["id"] in SATZ:
        grafik, satz = SATZ[a["id"]]
        a["grafik"] = grafik
        a["satz"] = satz
        gesetzt.add(a["id"])
    neu.append(json.dumps(a, ensure_ascii=False))
assert gesetzt == set(SATZ), set(SATZ) - gesetzt
DATEI.write_text("\n".join(neu) + "\n", encoding="utf-8")
print(f"{len(gesetzt)} Zeilen mit satz, {sum(1 for g, _ in SATZ.values() if g)} "
      f"mit grafik")

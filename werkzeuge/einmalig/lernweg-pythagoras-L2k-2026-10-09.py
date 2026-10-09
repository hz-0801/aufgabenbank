"""Bau M2 (09.10.2026): Lernweg „Kathete berechnen“ (pythagoras, Lerneinheit 2,
erster Teil, Blatt T6B) in bank/pythagoras/e2.jsonl zurücklegen.

Setzt die Lernweg-Felder (bank.md „Felder für den Lernweg“) an gewählten
Zeilen, fügt neue Zeilen hinter ihrer Sprosse ein und markiert schwächere
Zeilen desselben Schritts. Einmalig; zweiter Lauf ändert nichts (ids geprüft).
"""
import json
from pathlib import Path

DATEI = Path(__file__).resolve().parents[2] / "bank/pythagoras/e2.jsonl"
BLATT = ["T6B"]
HERKUNFT = "Bau M2 2026-10-09, Blatt T6B"

K3 = dict(eintrag="pythagoras", einheit=2, kette="Kathete", kette_nr=3,
          quelle=88, original=None, grafik="", loesungsgrafik="")
K6 = dict(eintrag="pythagoras", einheit=2, kette="Kathete", kette_nr=6,
          quelle=20, original=None, grafik="", loesungsgrafik="",
          hoehe="pflicht")
ST = {0: "„Lange oder kurze Seite gesucht?“ – zu Dreiecken mit zwei Maßen ankreuzen: Hypotenuse gesucht (plus) oder Kathete gesucht (minus); nichts rechnen",
      1: "Gleichung nach der gesuchten Kathete umstellen, dann Kathete mit aufgehender Wurzel",
      5: "Kathetengleichung unter vier Optionen ankreuzen (P10-Form)",
      7: "Kathete im Sachzusammenhang mit Skizze (Höhenunterschied, Abstand, Höhe eines Parallelogramms)",
      11: "Gemischt: Dreieck mit genannter Ecke des rechten Winkels, je Teilaufgabe Hypotenuse oder Kathete gesucht, Einheiten wechseln – erst die Hypotenuse bestimmen, dann plus oder minus wählen"}
ST6 = {2: "Begründen (warum bei gesuchter Kathete subtrahiert wird; warum die Zwölfknotenschnur mit den Abschnitten drei, vier, fünf einen rechten Winkel liefert)",
       4: "Gleichung nach einer Kathete umstellen (a² = c² − b², b² = c² − a²)"}
S12 = None  # sprosse_text der Prüfungshöhe wird aus der Datei übernommen


def lw(schritt, sache, darstellung, frage, antwortform):
    return dict(schritt=schritt, sache=sache, darstellung=darstellung,
                frage=frage, antwortform=antwortform, status="gut",
                blatt=BLATT)


NEU = [
    # L2k-1 Idee: Fläche abziehen
    dict(K6, id="pythagoras-e2-k6-s2-v4", sprosse=2, sprosse_text=ST6[2], pflicht="begruenden",
         merkmal="Idee: das fehlende Kathetenquadrat ist Hypotenusenquadrat minus anderes Kathetenquadrat",
         variante=4,
         aufgabe="Die zwei kleinen Quadrate über den Katheten haben zusammen so viel Fläche wie das große Quadrat über der Hypotenuse. Das große Quadrat hat $100$ cm$^2$, ein kleines $36$ cm$^2$. \\\\ a) Wie groß ist die Fläche des dritten Quadrats? \\\\ b) Wie lang ist die Seite dieses Quadrats?",
         form="teil", antwort="a) __ cm², b) __ cm",
         loesung="a) $100 - 36 = 64$ cm$^2$; b) $\\sqrt{64} = 8$ cm",
         pruef="[64, 8]", herkunft=HERKUNFT, **lw("L2k-1", "", "skizze-fertig", "laenge", "eintragen")),
    dict(K6, id="pythagoras-e2-k6-s2-v5", sprosse=2, sprosse_text=ST6[2], pflicht="begruenden",
         merkmal="Idee: das fehlende Kathetenquadrat ist Hypotenusenquadrat minus anderes Kathetenquadrat",
         variante=5,
         aufgabe="Die zwei kleinen Quadrate über den Katheten haben zusammen so viel Fläche wie das große Quadrat über der Hypotenuse. Das große Quadrat hat $169$ cm$^2$, ein kleines $25$ cm$^2$. \\\\ a) Wie groß ist die Fläche des dritten Quadrats? \\\\ b) Wie lang ist die Seite dieses Quadrats?",
         form="teil", antwort="a) __ cm², b) __ cm",
         loesung="a) $169 - 25 = 144$ cm$^2$; b) $\\sqrt{144} = 12$ cm",
         pruef="[144, 12]", herkunft=HERKUNFT,
         **dict(lw("L2k-1", "", "skizze-fertig", "laenge", "eintragen"), blatt=[])),
    # L2k-2 Hypotenuse oder Kathete gesucht, verschiedene Lagen
    dict(K3, id="pythagoras-e2-k3-s0-v5", sprosse=0, sprosse_text=ST[0], hoehe="vorstufe",
         merkmal="in vier Dreiecken verschiedener Lage entscheiden, ob die gesuchte Seite Hypotenuse oder Kathete ist",
         variante=5,
         aufgabe="Zwei Seiten sind gegeben. Ist die Seite mit dem Fragezeichen die Hypotenuse oder eine Kathete? \\\\ a) rechter Winkel unten links, Katheten $6$ cm und $8$ cm, ? gegenüber \\\\ b) rechter Winkel oben, waagerechte Seite $17$ cm, ? an der Spitze \\\\ c) rechter Winkel unten rechts, schräge Seite $25$ cm, ? unten \\\\ d) Dreieck gedreht, Katheten $12$ m und $34$ m, ? gegenüber",
         form="teil", antwort="",
         loesung="a) Hypotenuse; b) Kathete; c) Kathete; d) Hypotenuse",
         pruef="", herkunft=HERKUNFT, **lw("L2k-2", "", "skizze-fertig", "erkennen", "ankreuzen")),
    # L2k-3 Gleichung umstellen ohne Zahl
    dict(K6, id="pythagoras-e2-k6-s4-v4", sprosse=4, sprosse_text=ST6[4], pflicht="darstellung",
         merkmal="Gleichung zum beschrifteten Dreieck aufstellen und nach der gesuchten Seite umstellen, Buchstaben wechseln",
         variante=4,
         aufgabe="Schreibe den Satz des Pythagoras für das Dreieck auf. Stelle die Gleichung dann so um, dass das Quadrat der gesuchten Seite allein steht. \\\\ a) Hypotenuse $w$, gesucht $u$ \\\\ b) Hypotenuse $r$, gesucht $q$ \\\\ c) Dreieck $ABC$, rechter Winkel bei $B$, gesucht $\\overline{BC}$",
         form="teil", antwort="",
         loesung="a) $u^2 = w^2 - v^2$; b) $q^2 = r^2 - p^2$; c) $\\overline{BC}^2 = \\overline{AC}^2 - \\overline{AB}^2$",
         pruef="", herkunft=HERKUNFT, **lw("L2k-3", "", "skizze-fertig", "gleichung", "eintragen")),
    dict(K3, id="pythagoras-e2-k3-s5-v4", sprosse=5, sprosse_text=ST[5], hoehe="sprosse",
         merkmal="Kathetenformel mit Wurzel unter den Fallen des Originals wählen",
         variante=4,
         aufgabe="Im Dreieck sind $y$ und $z$ die Katheten, $x$ ist die Hypotenuse. Kreuze die Gleichung an, mit der man die Länge von $z$ berechnen kann. (P10 2024 OS) \\\\ \\kreuz{$z = x^2 - y^2$} \\\\ \\kreuz{$z = \\sqrt{x^2 + y^2}$} \\\\ \\kreuz{$z = x + y$} \\\\ \\kreuz{$z = \\sqrt{x^2 - y^2}$}",
         form="ankreuzen", antwort="",
         loesung="$z = \\sqrt{x^2 - y^2}$",
         pruef="", original={"id": "2024-OS-B1f", "jahr": 2024, "papier": "OS"},
         grafik="\\dreieckrw{4}{2.5}{$z$}{$y$}{$x$}",
         **lw("L2k-3", "", "skizze-fertig", "zuordnung", "ankreuzen")),
    # L2k-4 Rechnen glatt
    dict(K3, id="pythagoras-e2-k3-s1-v6", sprosse=1, sprosse_text=ST[1], hoehe="grundfall",
         merkmal="Kathete gesucht, Wurzel geht auf, Quadrate im Kopf; a) vorgerechnet",
         variante=6,
         aufgabe="Die Hypotenuse und eine Kathete eines rechtwinkligen Dreiecks sind gegeben. Berechne die andere Kathete. \\\\ a) Hypotenuse $10$ cm, Kathete $6$ cm (vorgerechnet) \\\\ b) Hypotenuse $13$ cm, Kathete $5$ cm \\\\ c) Hypotenuse $25$ cm, Kathete $7$ cm",
         form="teil", antwort="",
         loesung="a) $10^2 - 6^2 = 64$, $8$ cm; b) $13^2 - 5^2 = 144$, $12$ cm; c) $25^2 - 7^2 = 576$, $24$ cm",
         pruef="[64, 8, 144, 12, 576, 24]", herkunft=HERKUNFT,
         **lw("L2k-4", "", "term", "laenge", "rechnen")),
    dict(K3, id="pythagoras-e2-k3-s1-v7", sprosse=1, sprosse_text=ST[1], hoehe="grundfall",
         merkmal="Kathete gesucht, Wurzel geht auf, Quadrate im Kopf; neue Zahlen",
         variante=7,
         aufgabe="Die Hypotenuse und eine Kathete eines rechtwinkligen Dreiecks sind gegeben. Berechne die andere Kathete. \\\\ a) Hypotenuse $17$ cm, Kathete $8$ cm \\\\ b) Hypotenuse $15$ cm, Kathete $9$ cm \\\\ c) Hypotenuse $26$ cm, Kathete $10$ cm",
         form="teil", antwort="",
         loesung="a) $17^2 - 8^2 = 225$, $15$ cm; b) $15^2 - 9^2 = 144$, $12$ cm; c) $26^2 - 10^2 = 576$, $24$ cm",
         pruef="[225, 15, 144, 12, 576, 24]", herkunft=HERKUNFT,
         **dict(lw("L2k-4", "", "term", "laenge", "rechnen"), blatt=[])),
    # L2k-6 Sache
    dict(K3, id="pythagoras-e2-k3-s7-v4", sprosse=7, sprosse_text=ST[7], hoehe="sprosse",
         merkmal="Kathete in einer Sachsituation, Dreieck nicht gezeichnet, Entscheidung mit Antwort nein",
         variante=4,
         aufgabe="Tim spannt ein Seil von der Spitze der Zeltstange bis zu einem Hering im Boden. Die Stange ist $1{,}6$ m hoch, das Seil $3{,}4$ m lang. Der Zaun steht $2{,}8$ m von der Stange entfernt. Reicht der Platz bis zum Zaun dafür?",
         form="teil", antwort="",
         loesung="Nein; $\\sqrt{3{,}4^2 - 1{,}6^2} = \\sqrt{9} = 3$ m $> 2{,}8$ m",
         pruef="[9, 3]", bild="Zelt", herkunft=HERKUNFT,
         **lw("L2k-6", "Zeltseil", "bild", "entscheidung", "rechnen")),
    dict(K3, id="pythagoras-e2-k3-s11-v4", sprosse=11, sprosse_text=ST[11], hoehe="sprosse",
         merkmal="in einer Kathetenumgebung ist die Hypotenuse gesucht; Dreieck auf der Karte selbst finden",
         variante=4,
         aufgabe="Ein Boot fährt bei $A$ los und will genau gegenüber anlegen. Der Fluss ist $120$ m breit. Die Strömung treibt es ab. Es legt bei $B$ an, $90$ m flussabwärts. Wie lang war die Fahrt von $A$ nach $B$?",
         form="teil", antwort="",
         loesung="Hypotenuse gesucht: $\\sqrt{120^2 + 90^2} = \\sqrt{22\\,500} = 150$ m",
         pruef="[22500, 150]", bild="Fluss", herkunft=HERKUNFT,
         **lw("L2k-6", "Boot auf dem Fluss", "karte", "laenge", "rechnen")),
]

# Ziel L2k-7: Original 2024-OS-K6a nah am Wortlaut
NEU_S12 = dict(K3, id="pythagoras-e2-k3-s12-v7", sprosse=12, hoehe="pruefung",
               merkmal="Prüfungshöhe: Original 2024-OS-K6a nah am Wortlaut, Teil b und Punkt C weggelassen",
               variante=7,
               aufgabe="Eine Seilbahn fährt von der Talstation $B$ zur Bergstation $A$. Das Seil $\\overline{AB}$ ist $384$ m lang. Der Punkt $F$ liegt senkrecht unter $A$, $\\overline{FB}$ ist $255$ m lang. Die Strecke $\\overline{FA}$ ist der Höhenunterschied zwischen $B$ und $A$. Berechne diesen Höhenunterschied. Runde auf eine Stelle nach dem Komma. (P10 2024 OS)",
               form="teil", antwort="",
               loesung="$\\overline{FA} = \\sqrt{384^2 - 255^2} = \\sqrt{82\\,431} \\approx 287{,}1$ m",
               pruef="[82431, 82431**0.5]",
               original={"id": "2024-OS-K6a", "jahr": 2024, "papier": "OS"},
               bild="Seilbahn", **lw("L2k-7", "Seilbahn", "skizze-fertig", "laenge", "rechnen"))

GEWAEHLT = {  # Bankzeilen auf dem Blatt
    "pythagoras-e2-k3-s2-v3": lw("L2k-5", "", "term", "laenge", "rechnen"),
    "pythagoras-e2-k3-s3-v4": lw("L2k-5", "", "term", "laenge", "rechnen"),
    "pythagoras-e2-k6-s3-v3": lw("L2k-6", "Drachen", "text", "laenge", "rechnen"),
}
SCHWACH = {
    **{f"pythagoras-e2-k3-s1-v{v}": ("Grundfall mit vierstelligen Quadraten und vorgegebener Form a² = __ (Bauregel Antwortfeld)",
                                     "pythagoras-e2-k3-s1-v6") for v in range(1, 6)},
    "pythagoras-e2-k3-s7-v2": ("dieselbe Zeltsache mit fertiger Skizze und nur Längenfrage",
                               "pythagoras-e2-k3-s7-v4"),
}

zeilen = [json.loads(l) for l in DATEI.read_text(encoding="utf-8").splitlines() if l.strip()]
ids = {z["id"] for z in zeilen}
s12 = next(z for z in zeilen if z["id"] == "pythagoras-e2-k3-s12-v1")
NEU_S12["sprosse_text"] = s12["sprosse_text"]
for z in zeilen:
    if z["id"] in GEWAEHLT:
        z.update(GEWAEHLT[z["id"]])
    if z["id"] in SCHWACH:
        g, b = SCHWACH[z["id"]]
        z.update(status="schwach", status_grund=g, besser=b)
for n in NEU + [NEU_S12]:
    if n["id"] in ids:
        continue
    # merkmal je Sprosse einheitlich (bank-pruef); das eigene Merkmal steht im Lernweg
    n["merkmal"] = next(z["merkmal"] for z in zeilen
                        if z["kette_nr"] == n["kette_nr"] and z["sprosse"] == n["sprosse"])
    kette, sprosse = n["kette_nr"], n["sprosse"]
    pos = max(i for i, z in enumerate(zeilen)
              if z["kette_nr"] == kette and z["sprosse"] == sprosse)
    zeilen.insert(pos + 1, n)
    ids.add(n["id"])
DATEI.write_text("".join(json.dumps(z, ensure_ascii=False) + "\n" for z in zeilen),
                 encoding="utf-8")
print(len(zeilen), "Zeilen")

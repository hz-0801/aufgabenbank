# Bericht – GYW Seite oder Winkel mit sin, cos, tan (11.10.2026)

Dauer: 9 min (Bau-Agent, Start 22:10 UTC).
Seiten: Übersicht 1, Blatt 3, Lösungen 1. xelatex ohne Fehler.

## Aufgaben je Stufe (davon echte)
- Seitenverhältnis benennen: 3 (1)
- Winkel berechnen: 3 (2)
- Seite berechnen: 3 (2)
- erst entscheiden, dann rechnen: 2 (1)
Zusammen 11, davon 6 echte. Herausgelöste Fassungen neu: herausgeloest.csv (4 Zeilen).

## Was pruefung.md nicht beantwortet hat
- Schlussstufe ohne Hauptplätze: Stufenkopf „nicht geprüft“, obwohl 2025-OS-K4a (Nebenplatz) genau diese Entscheidung prüft – Nebenplätze zählen nicht; gesetzt nach Regel.
- „Am Ende die schwerste echte“ gegen Schlussstufe: die schwerste (2023-OS-K7b) steht am Ende von „Seite berechnen“, die Schlussstufe endet mit der leichteren 2025-OS-K4a.
- Längenregel: zwei zusätzliche echte (2022-OS-K5b, 2026-FOR-K4c) gestrichen, damit das Blatt bei 3 Seiten bleibt; welche wegfällt, sagt die Regel nicht (gewählt: die mit gleicher Figur/gleichem Weg wie eine andere).
- Marke bei ganzer Teilaufgabe mit eigenem Wortlaut (2025-OS-K4a ganz, 2025-OS-B1g wörtlich): „nach“ gesetzt wie im Muster P4Z; „ganz“ heißt in pruefung.md ganze Aufgabe.
- Bank-Lücke: keine Sprosse „Pythagoras oder sin, cos, tan entscheiden“ (nur Seiten → Pythagoras, Winkel dabei → Winkelfunktion); e3-k1-s14 ersetzt sie nur halb. Keine Bankzeile angelegt, weil die Sprosse im Katalog (trigonometrie.md) fehlt und jede Kette mit hoehe pruefung endet.
- Bank-Grundfall e2-k1-s1 aus Platzgründen weggelassen; die Mischsprosse s11 steht ohne Grundfall davor.

## Formmerkmale, die dem Setzer fehlen
- Winkelbogen mit Beschriftung in freien Skizzen (\mbwinkelbogen ist intern, Abstand fest 0,55/0,85 in Koordinaten, skaliert mit; bei kleinen Winkeln neben Rechtwinkelmarke von Hand gesetzt).
- Päckchen-Zeilen mit Text links, Karo rechts (\gzwei + \parbox von Hand wie in P4Z).
- Lückengleichung mit Linie innerhalb der Formel (Nr. 2: „sin __ = r/t“).
- Skizzen der echten (Parallelogramm, Teildreiecke) von Hand in TikZ; dieselbe Figur in zwei Aufgaben (Nr. 6/Nr. 8 Vorlage) müsste der Setzer aus einem Datensatz ziehen.

## Nachzug 12.10. (nach befund-kritiker-2026-10-11.md)

- Form aus T2U: Laufkopf „P10 · Prüfung“/Kennung je Seite, Titel „sin, cos, tan“, Stufenzeile, Seitenzahl n/N, Ausschnitt „Vorher: Pythagoras · ▸ sin, cos, tan · Weiter: Winkel · Sinussatz · Vierecke“; Übersicht mit Gruppen (Rechtwinklige Dreiecke / Alle Dreiecke und Vierecke); Stufenköpfe „letzte 5 Jahre: …“.
- Stufen (je eigener Handgriff, Kritiker mehr-dreiecke): Gleichung aufstellen · Winkel gesucht · Seite gesucht · Pythagoras oder sin, cos, tan? (Schlussstufe, pruefung.md § 5, Lehrer 11.10.). Namen nach dem Muster Pythagoras (gemeinsam.md „Namen“). 2020-OS-B1j (rechnet eine Seite) im Plan zu „Seite gesucht“ gezählt; in der Fundstellentabelle unverändert (Jahr 20: 1c 1j 5b).
- Je Stufe die Schülerfrage zuerst (Regel 5): Nr. 1a benennen (Hypotenuse, Gegenkathete, Ankathete), Nr. 4 Funktion zuordnen ohne Rechnen, Nr. 8 „x oben oder unten im Bruch“ ankreuzen (andere Zahlen als Nr. 9, damit Nr. 9 keine Abschrift ist), Nr. 12 sechs Mini-Fälle nur Werkzeug ankreuzen (Pythagoras · sin, cos, tan · Winkelsumme).
- Befunde umgesetzt: Nr. 2 untereinander, Gleichheitszeichen bündig, alte c) (Funktion fehlt) weg; Nr. 5 ohne „Wähle selbst …“, a) mit Skizze, b) ohne gemischte Einheiten (5 cm statt 50 mm); Nr. 9a mit Skizze; alte Nr. 10 (rechnen und mit Pythagoras prüfen) gestrichen.
- Andere Zahlen (msa/mehr-p10.csv): Nr. 6 262 m, 396 m → 48,6°; Nr. 7 38 cm, 16 cm → ε ≈ 65,1° („etwa 65°“); Nr. 10 7,3 m, 49° → 9,7 m; Nr. 11 128,9 cm, 58°, 45° → 91,1 cm, 172,0 cm; Nr. 13 200 cm, 17 cm → 200,7 cm, 4,9°. Nr. 3 ohne Zahlen. Alle Ergebnisse mit Python nachgerechnet.
- Stufenkopf Schlussstufe: Jahre der echten Aufgaben, die den Schritt enthalten (2026 · 2025 · 2024 · 2022), nach pruefung.md „Stufenkopf“.
- Aufgaben je Stufe (echte): Gleichung aufstellen 3 (1) · Winkel gesucht 4 (2) · Seite gesucht 4 (2) · Pythagoras oder sin, cos, tan? 2 (1) – 13 Nummern, 6 echte (vorher 11 / 6).
- Nicht umgesetzt: Blatt auf 3 Seiten – es sind 4 (eine Stufe je Seite; der Stufenkopf fordert 14 Zeilen Platz und schiebt jede Stufe auf eine neue Seite, obwohl Kopf + erste Aufgabe passen würden – Wunsch an den Setzer in bau/pruefung/nachzug-2026-10-12.md). Zweite echte in „Winkel gesucht“ und „Seite gesucht“ bleibt (Kern, andere Erscheinungsform: Sache / Parallelogramm, Teildreieck / zwei Teildreiecke).
- Seiten: Übersicht 1, Blatt 4, Lösung 2. herausgeloest.csv unverändert (Originalzahlen); die Blattzahlen stehen in mehr-p10.csv.

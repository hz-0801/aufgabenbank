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

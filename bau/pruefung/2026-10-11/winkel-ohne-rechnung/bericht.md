# Bericht – T2U Winkel ohne Rechnung bestimmen oder begründen

Dauer: 22:10–22:18 (date), etwa 8 min Wanduhr.
Seiten: Übersicht 1, Blatt 3, Lösungen 1.
Aufgaben je Stufe (davon echte): Eigenschaft 2 (1) · Winkelsumme 5 (3) · gleichschenklig 3 (2) · rechter Winkel 2 (1) – 12 Nummern, 7 echte.
Neue Bankzeilen: keine (keine Lücke). Herausgelöst: herausgeloest.csv (7 Zeilen; B1g, K7a, K2c als -h2, weil -h1 schon andere Fassungen sind).

## Was pruefung.md nicht beantwortet hat (selbst entschieden)
- Echte älter als fünf Jahre: 2018-OS-K4b steht auf dem Blatt, weil es die einzige echte seiner Sorte (Begründen über Nebenwinkel) und die schwerste des Handgriffs ist; pruefung.md sagt nicht, ob „schwerste echte“ auf die letzten fünf Jahre begrenzt ist.
- Sorte in „Winkelsumme“: Trapez ’23 und Parallelogramm ’26 als eine Sorte „Winkel im Viereck“ gezählt (nur andere Figur) → 2023-OS-K2a nur in der Tabelle, obwohl Kern eine zweite erlauben würde.
- Kürzen bei der letzten echten jeder Art („steht voll“): wie im Muster P4Z gekürzt, was nur andere Teilaufgaben brauchen (65°/131,5 cm bei 7a, Höhen bei 4b, 52°/14,1 m bei 5c); bei 7a bleibt 45° bei B, weil es im Original in der Skizze steht – die Aufgabe wird dadurch leicht.
- Marke „nach P10 ’23 · 1g“ auch bei ganzer, nur umformulierter Basisaufgabe (wie Muster), nicht „P10 ’23 · 1g“.
- Stufenkopf „geprüft 2026“ bei Eigenschaft erkennen zählt den Basisteil (B1c) als Hauptplatz.
- Ankreuzen in Nr. 2: drei Optionen zusammen ≈ 116 Zeichen (≤ 120 → laut gemeinsam.md eine Zeile), passen aber mit Buchstaben nicht in eine Zeile – untereinander gesetzt.
- Länge DF = 25 cm in Nr. 12 im Text statt in der Skizze, weil die Beschriftung auf der kurzen Strecke mit Linien und Bögen kollidierte.
- Bank-Wortlaut angepasst (s10-v2 ohne Satzanfang-Form und Prüfkennung; s8-v1 als Aussage + „Gib an“): Sprachregel vor Bankwortlaut.
- Fundstellentabelle: 2015-OS-K5b fällt aus dem Bereich 2026 … 2016 und steht nirgends.

## Formmerkmale, die dem Setzer fehlen
- Winkelbogen mit Beschriftung für freie Ecken (Bogen zwischen zwei Strecken, Label außen, Rechtwinkelmarke) – hier eigenes TikZ wie in den Bankgrafiken; kein Baustein `\winkelbei{V}{P}{Q}{Label}`.
- Grau gefülltes Teildreieck (2023-OS-K7a) und Peil-/Lageskizze mit Hilfslinien (2018-OS-K4b).
- Antwortlinie für kurze Antwort ohne Rechnung (Nr. 8) rechts in der Zeile: `\hfill\linie{30mm}`; im Setzer nicht als Form.
- Echte aus herausgeloest.csv mit Skizze: Feld abbildung ist Prosa, der Setzer braucht dafür Grafik-Code (wie Bankfeld grafik).
- Sternmarke bei FOR-Sternchenaufgaben (2025-OS-K2c) aus dem Original-Vermerk.

## Nachzug 11.10. (Durchsicht)

- Namen: Titel „Winkel“ (P10), Stufen wortgleich in Übersicht, Titelzeile, Stufenköpfen und Lösung: Eigenschaften kennen · Innenwinkelsumme: Dreieck · Viereck · gleichschenklig: zwei gleiche Winkel · rechter Winkel: begründen. Übersicht: Pythagoras · sin, cos, tan – im rechtwinkligen Dreieck · ▸ Winkel · Sinussatz – in jedem Dreieck (grau) · Symmetrie (grau); „Weiter: Flächeninhalt und Umfang“. Blattende „Weiter: Sinussatz – in jedem Dreieck“.
- Kopf: Seite 1 Titel, P10, rechts T2U, darunter graue Stufenzeile; Folgeseiten links „Winkel“, rechts T2U; Fuß mittig „n/3“, kopfüber-Ergebnisse unverändert.
- Stufenkopf: „letzte 5 Jahre: 2026“ · „2026 · 2023 · 2022“ · „2023“ · „2025“.
- Nummer und Buchstaben in zwei Spalten (Nr. 3 a–c; Lösung mit Buchstabenspalte).
- Ankreuzen untereinander (Nr. 1, 2, 8); Nr. 9 als Lückentext, zwei Zeilen, Gleichheitszeichen und Lücke untereinander.
- Skizzen: Nr. 1 kleine Raute; Nr. 3a Dreieck mit 52° und 71°; Nr. 8 (erste der Stufe gleichschenklig) Dreieck mit zwei 64°-Winkeln, dafür jetzt Ankreuzen „welche Seiten gleich lang“ statt Seite angeben (sonst Nr. 9 mit anderer Zahl); Nr. 4 ohne Skizze, Höhe im Text. Echte Aufgaben behalten ihre Skizze (Original hat eine: 5, 6, 7, 9, 10, 12; Nr. 2 ohne). Skizzen 7, 10, 12 verkleinert, damit das Blatt auf 3 Seiten bleibt.
- Päckchen Nr. 3: a) Dreieck mit Skizze → b) Viereck im Text → c) Viereck krumm (86,5°; 97,3°; 101,4° → 74,8°, eigen); kein Hinweis.
- Stern: geprüft gegen msa-katalog-kontext.csv/-basis.csv (Spalte stern) und gliederung/dreiecke.md. Nur 2025-OS-K2c (Nr. 12) ist Sternchenaufgabe – Stern stand schon. 2026-FOR-B1c und -B1i haben EBR-Zwillinge, also nicht nur im FOR-Heft: kein Stern. 2018-OS-K4b, 2022-OS-K5c, 2023-OS-B1g, 2023-OS-K7a: stern nein.
- Lösung: Stufenköpfe wortgleich als Zwischenüberschriften, Nummer- und Buchstabenspalte; 1 Seite.
- Umfang: Übersicht 1, Blatt 3, Lösung 1 Seite.
- mathblatt.sty 2026-10-11b neu: \pfstufenzeile{…}, \pflaufkopf{Name}{Kennung} (nach \pfheftstil; \pfkopfzeile war belegt), \pfseitevon (Seitenzahl „n/N“ mittig, lastpage), \pfteil{a)}{Text}, Umgebung pfloesungb mit \lzb{Nr}{Bst}{Ergebnis}{Weg}; alles zusätzlich, Bestehendes unverändert.

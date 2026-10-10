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

## Nachzug 11.10. (zweite Durchsicht)

- Dauer: 23:41–23:55 (date). Seiten: Übersicht 1, Blatt 3, Lösung 2 (Stufe 4 auf Seite 2).
- 1 Winkelbeziehungen: neue Stufe statt „Eigenschaften kennen“; Nr. 1 Markieren (Schülerfrage „gleich groß? zusammen 180°?“) an Kreuzung und Parallelen, Nr. 2 kleine Berechnung an denselben Figuren ohne neue Skizze; Kopf „letzte 5 Jahre: 2026 · 2022 · 2018“. Raute und 2026-FOR-B1c raus (→ Vierecke), B1c und die Raute-Fundstelle 2016-OS-B1e aus der Fundstellentabelle, B1c-Zeile aus herausgeloest.csv.
- 2 Innenwinkelsumme: Nr. 3 a) Dreieck mit Skizze, b) Viereck mit Skizzenfeld, c) gestrichen; Nr. 4 Winkel γ₁ statt ε, Skizzenfeld.
- 3 gleichschenklig: Nr. 8 neu – zwei Dreiecke (gleichschenklig mit 64°, gleichseitig), „Was unterscheidet die beiden? Trage alle Winkel ein.“; danach 2023-OS-B1g und -K7a wie bisher.
- 4 rechter Winkel: Nr. 11 neu mit dem Handgriff von 2025-OS-K2c (msa/wortlaut-eigen-dreiecke.csv: gleich lange Strecken am rechten Winkel → zwei gleichschenklig-rechtwinklige Teildreiecke, 45° + 45°), Längen in der Skizze, Hilfe „erst die Winkel eintragen“.
- 5 Skizzen: alle Winkelwerte und -namen innen im Bogen (\pfwinkel), Längen außen; Ausnahme: γ in Nr. 11 und 12 leicht neben der Mittellinie, weil die Teilungslinie durch den Bogen geht. Nr. 7 jetzt maßstäblich bis auf γ (10° statt 5°, sonst passt γ nicht in den Bogen; Original ist ohnehin nicht maßstabsgerecht).
- 6 Kopf: links „P10 · Prüfung“ (Folgeseiten „· Winkel“), rechts T2U auf jeder Seite, Titel „Winkel“, Stufenzeile; Fuß „n/N“ mittig. Gilt auch für Übersicht und Lösung.
- 7 Skizzenfeld bei Nr. 3b und Nr. 4.
- 8 Blattende: Fundstellentabelle, darunter grau „Vorher: Pythagoras · sin, cos, tan“, „▸ Winkel“, „Weiter: Sinussatz · Vierecke“.
- 9 Übersicht: Gruppen „Rechtwinklige Dreiecke“ (Pythagoras · sin, cos, tan) und „Alle Dreiecke und Vierecke“ (▸ Winkel mit Stufen, Sinussatz und Vierecke grau); „Weiter: Flächeninhalt und Umfang“. Gliederung dreiecke.md: Zeile „Gruppen:“, Eigenschaft erkennen → Zuschnitt „Vierecke: Symmetrie und Eigenschaften“ mit Hinweis.
- 10 Lösung: Stufenköpfe wortgleich, Nummer-/Buchstabenspalte, Markier-Aufgaben als „gleich: α = γ, β = δ; 180°: …“.
- Neue Makros (mathblatt.sty 2026-10-11c): \pflaufkopf[Sorte]{Name}{Kennung} (rückwärtskompatibel), \pfskizzenfeld[breite]{n}, \pfwinkel[r][f]{(x,y)}{von}{bis}{Wert} (Wert innen), \pfrw[r]{(x,y)}{Richtung}, \pfausschnitt{Vorher}{Name}{Weiter}; \geradenkreuzung, \parallelenpaar, \winkel, \mbwinkelbogen setzen Beschriftungen jetzt innen.
- Neue Bankzeilen: winkel-dreiecke-e2-k2-s0-v5, -e2-k2-s0-v6, -e2-k2-s3-v10, -e2-k2-s10-v9, -e3-k2-s0-v5, -e3-k2-s9-v8 (bank-pruef: 0 Abweichungen; neue Warnungen nur Mengen je Sprosse).
- Bankzeile e3-k2-s7-v7: ε → γ₁ (Sprachregel). Offen: Raute/B1c-Inhalt liegt jetzt beim Blatt Vierecke, das es noch nicht gibt.

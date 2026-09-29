# Mappe: lagebeziehungen

Eintrag: hz-0801/mathe-nachhilfe, katalog/lagebeziehungen.md
Katalog-Commit: 2a296e54827b16f81fd664c4430c6fcd84dd5719 (2026-09-28T22:05:53Z, „Katalog-Nachzug Teil 2: Sek II aus den Urteilen vom 28.09.“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-29 17:58 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Lagebeziehungen
  3
  4  ### Verortung
  5  Der Lagebefund: liegt ein Punkt in einer Ebene, auf welcher Seite liegt er, liegt eine Gerade in der Ebene, ist sie parallel oder schneidet sie – die Punktprobe an Koordinaten- und Parametergleichunge … (gekürzt, 2842 Zeichen)
  6  [GOST] Q3, 3. Kurshalbjahr „Analytische Geometrie“ (BB S. 29–30), Grund- und Leistungskursfach: L3-Zeile „Geraden und Ebenen analytisch beschreiben und Lagebeziehungen von Geraden und Ebenen untersuch … (gekürzt, 1729 Zeichen)
  7  [FOS] Kap. 4 Wahlthema 5 „Analytische Geometrie“ (S. 29): Thema „Punkt und Gerade im Raum“ mit „Lagebeziehung Punkt–Gerade und Gerade–Gerade“ (Zeilen 1209–1213 der Textfassung) – Ebenen und damit die Lagen dieses Eintrags kommen im RLP FOS nicht vor; Wahlstoff ohne Prüfungsbeleg, kein fhr-Bestand, keine fhr-Zeile in themen.csv.
  8  [LS-AA] Qualifikationsphase Kapitel VI „Geraden und Ebenen“: 8 Gegenseitige Lage von Ebenen und Geraden (Zeilen 337 und 1649 der Textfassung; 9 Gegenseitige Lage von Ebenen → ebenen.md und schnittmeng … (gekürzt, 648 Zeichen)
  9
 10  ### Lerneinheiten
 11  1. Punktprobe und Seitenlage – drin, drauf, auf welcher Seite: die Punktprobe an der Koordinatengleichung (einsetzen, Gleichung erfüllt oder nicht) und an der Parameterform (gleichsetzen, zwei Paramet … (gekürzt, 712 Zeichen)
 12    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
 13  2. Parameter aus der Lagebedingung – rückwärts eingesetzt: den freien Parameter einer Ebenengleichung aus einem Punkt bestimmen, der in der Ebene liegen soll (einsetzen, auflösen, Kontrolle; bei zwei freien Werten einen wählen – nicht beide null); den Punkt einer Ebene mit einer Koordinatenbedingung bestimmen (drei gleiche Koordinaten). (Q3, GK-Kern „Lagebeziehungen …“ rückwärts gelesen; Teil-A-Praxis des Pools) ← Eingabe „parameter ebenengleichung“, „k bestimmen ebene“, „punkt mit gleichen koordinaten“
 14    Marken: BE Q3 · BB Q3 · GK (BB nur LK) · Abitur LK
 15  3. Gerade und Ebene – enthalten, parallel, schneidend: die Lage über das Einsetzen des allgemeinen Geradenpunkts (Parameter fällt heraus und die Gleichung stimmt → Gerade liegt in der Ebene; fällt her … (gekürzt, 863 Zeichen)
 16    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
 17  4. Lagebefunde im Sachzusammenhang – Licht, Schatten, Bahnen: den Schattenpunkt als Durchstoßpunkt der Lichtgeraden durch die Wand- oder Bodenebene bestimmen oder aus einem vorgelegten Lösungsweg erläutern, und danach den Befund führen (liegt der Schatten auf der Wand – Koordinatenbereiche prüfen); Bahnen gegen Ebenen (Auftreffpunkt im Spielfeld, Berühren eines Netzes über die Höhe im Durchstoßpunkt). (Q3, GK-Kern; die Prüfungsform trägt Teil B mit Maßstab und Bereichsprüfung) ← Eingabe „schatten wand“, „trifft der ball“, „berührt das netz“, „lichtgerade“
 18    Marken: BE Q3 · BB Q3 · GK · keine Prüfungsaufgabe
 19  Warum vier: Die Plan-Zeile bündelt fünf Paarungen; zwei davon (Punkt–Gerade, Geraden) liegen bei geraden.md und eine (Ebenen) bei ebenen.md – übrig bleiben Punkt–Ebene (vorwärts als Probe, rückwärts a … (gekürzt, 711 Zeichen)
 20
 21  ### Typen je Lerneinheit
 22  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 23  Einheit 1: kein Berechnungstyp — Nachweis: Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (10) · Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen (1) · Punkt und Ebene: Lage eines Punktes zwischen zwei parallelen Ebenen über Einsetzen in die Koordinatengleichungen begründen (1) · Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen (1) — Deutung: Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren (1). Dazu: Fehler finden (nur den Stützpunkt eingesetzt; die dritte Gleichung der Parameterprobe nicht geprüft; eine fehlende Variable in der Gleichung als Fehler gedeutet; nur eine der beiden Ebenen geprüft) · Begründen (warum das Erfülltsein der Gleichung die Lage entscheidet; warum gleiche Vorzeichen beim Einsetzen dieselbe Seite bedeuten).
 24  Einheit 2: Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (7) · Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen (1) — kein Nachweistyp — kein Deutungstyp. Dazu: Fehler finden (den falschen Punkt eingesetzt; einen Punkt gewählt, an dem der Parameter herausfällt; beide freien Werte null gesetzt; den Parameter aus einem einzelnen Koeffizienten geraten) · Begründen (warum ein Punkt der Ebene eine Gleichung für den Parameter liefert; warum die triviale Lösung keine Ebenengleichung ergibt).
 25  Einheit 3: Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen (1) — Nachweis: Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (4) · Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden (4) · Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen (2) · Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen (1) · Gerade und Ebene: Parallelität einer Geraden zu einer Ebene über das Skalarprodukt von Richtungs- und Normalenvektor nachweisen (1; Ermessen, siehe Offene Punkte) · Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen (1) — kein Deutungstyp. Dazu: Fehler finden (nur den Stützpunkt geprüft und „liegt in der Ebene“ geschlossen; den Fall Parameter fällt heraus als „parallel“ abgeschlossen, ohne die Punktprobe zu führen; bei der Schar nur die Spitze geprüft und die Grundfläche vergessen) · Begründen (warum das Herausfallen des Parameters über enthalten oder parallel entscheidet; warum das Skalarprodukt mit dem Normalenvektor die drei Fälle trennt).
 26  Einheit 4: Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen (1) · Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen (1) · Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen (1) — kein Nachweistyp — Deutung: Gerade und Ebene: Länge eines Schattens auf einer Dachfläche über Schnitt von Lichtgerade und Ebene beschreiben (2; Ermessen, siehe Offene Punkte) · Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern (2). Dazu: Fehler finden (nur den Schnittpunkt berechnet und die Wandmaße nicht geprüft; nur die Zeit berechnet und die Lage nicht geprüft; den Schatten an der falschen Kante beginnen lassen; den zweiten Lösungsschritt falsch gedeutet) · Begründen (warum der Schatten der Durchstoßpunkt der Lichtgeraden ist; warum nach der Rechnung immer der Bereich zu prüfen bleibt).
 27  Zählung: 5 + 2 + 7 + 5 = 19 Haupttypen, 14 + 8 + 14 + 7 = 43 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27./28.09.2026: Heft 2017-be-gk, Pool 2017 grundlegend und erhöht Teil B, WTR und CAS).
 28
 29  ### Voraussetzungen (Blatt 0)
 30  Fertigkeiten (je Zeile: was, wofür):
 31  - Ebenengleichungen lesen (Koordinatenform, Normalenvektor ablesen, Parameterform) – die Prüfregeln aller Einheiten. Sek-II-Nachbarthema ebenen.md (dasselbe Kurshalbjahr; Klarstellung Geometrie: Fertigkeit aus dem Nachbarthema derselben Stufe). [GOST Q3 L3 „analytische Beschreibung von Geraden und Ebenen“; GOST-OHiMi 2.3 „Ebenen: Parameterform, Koordinaten- und Normalenform“]
 32  - Geradengleichungen lesen und den allgemeinen Geradenpunkt bilden (Stützpunkt plus Parameter mal Richtungsvektor) – das Einsetzen in Einheit 3 und 4. Sek-II-Nachbarthema geraden.md. [GOST Q3 L3 „Parameterform“; GOST-OHiMi 2.3 „Geraden: Parameterform“]
 33  - Skalarprodukt berechnen und Orthogonalität erkennen – die Merkregel in Einheit 3 und die Kreisbahn-Begründung. Sek-II-Nachbarthemen skalarprodukt-und-winkel.md, orthogonalitaet.md. [GOST Q3 L3 „Skalarprodukt in Koordinatenform“, „Orthogonalität von Vektoren“; GOST-OHiMi 2.3]
 34  - Gleichungen lösen: lineare Gleichungen nach einer Unbekannten oder einem Parameter, quadratische Gleichungen für Bahnkurven – Einheit 2 und 4. Sek-I-Themen lineare-gleichungen.md, quadratische-gleichungen.md. [GOST-OHiMi 2.1; GOST Eingangsvoraussetzung L1]
 35  - Terme mit einem Parameter umformen und Fallunterscheidungen führen – die Scharen in Einheit 3. Sek-I-Thema terme.md; Sek-II-Nachbarthema funktionsscharen-und-ortskurven.md (der Familiengedanke). [GOST Q3 LK „auch unter Verwendung von Parametern in den Koordinaten (Scharen)“]
 36  - Punkte im räumlichen Koordinatensystem lesen und Bereiche deuten (Koordinatenschranken, Wandmaße) – die Bereichsprüfungen in Einheit 4. Sek-II-Nachbarthema punkte-und-strecken-im-koordinatensystem.md. [GOST Q3 L3 „koordinatisieren“; GOST-OHiMi 2.3]
 37  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 38  - „Wer und wogegen?“ – zu Aufgabentexten ankreuzen, welche Objekte beteiligt sind (Punkt gegen Ebene, Gerade gegen Ebene) und welche Gleichung die Prüfregel ist; nichts rechnen. Vor Einheit 1 und 3. [GOST Q3 L3 „Lagebeziehungen zwischen: …“; Rohdatei: Klassen Punkt und Ebene, Gerade und Ebene]
 39
 40  ### Merkkasten
 41  Einheit 1 (Punktprobe und Seitenlage):
 42      Punktprobe an der Koordinatengleichung: die Koordinaten einsetzen – stimmt die Gleichung, liegt der Punkt in der Ebene; stimmt sie nicht, liegt er außerhalb. Eine fehlende Variable ist kein Fehler: ihre Koordinate darf beliebig sein.
 43        E: 3x − 2y = 0, Punkt (1 | 1,5 | 7): 3 − 3 = 0 – der Punkt liegt in E; die 7 kommt in der Gleichung nicht vor.
 44      Punktprobe an der Parameterform: gleichsetzen, zwei Parameter aus zwei Gleichungen bestimmen, die dritte Gleichung prüfen – erst wenn sie aufgeht, liegt der Punkt in der Ebene (wie bei ebenen.md, Kasten der Parameterform).
 45      Seite über das Vorzeichen: erfüllt ein Punkt die Gleichung nicht, sagt das Vorzeichen der Abweichung, auf welcher Seite er liegt – zwei Punkte mit gleichem Vorzeichen liegen auf derselben Seite; zwischen zwei parallelen Ebenen liegt, wer bei der einen darüber und bei der anderen darunter liegt.
 46      Auswendig (Teil A): „Punktprobe an der Koordinatengleichung“ und „… an der Parameterform“ – [GOST-OHiMi 2.3] „Lagebeziehungen zwischen Punkten, Geraden und Ebenen“ (Teil-A-Belege 2022MgrundlegendAAGLAA211-a, 2021MerhoehtAAGLAA211-a, 2018MerhoehtAAGLAA211-a, 2021-be-gk-A1.5a); „Seite über das Vorzeichen“ ist Begründungsfigur des Teils B (2023-bebb-gk-B3f).
 47      Formelsammlung: keine – die Punktprobe steht nicht in [FS-IQB 1.3] – [FS] offen
 48  Quelle: eigene Formulierung nach [GOST Q3 L3] „Lagebeziehungen zwischen: … Punkt und Ebene“ und [GOST-OHiMi 2.3]; Zahlenbeispiel aus dem Pool (2022MgrundlegendAAGLAA211-a, wörtlich; wortgleiche Dublette 2022-bebb-gk-A1.4a); [LS-AA QP VI 8].
 49
 50  Einheit 2 (Parameter aus der Lagebedingung):
 51      Der freie Parameter: soll ein Punkt in der Ebene liegen, wird er eingesetzt und die Gleichung nach dem Parameter aufgelöst; Kontrolle mit einem zweiten gegebenen Punkt, wenn es ihn gibt.
 52        Ebene 12x + 20y + tz = 60 durch C(0 | 0 | 4): 4t = 60, also t = 15.
 53      Den richtigen Punkt wählen: ein Punkt, an dem der Parameter herausfällt, liefert keine Gleichung – dann einen anderen gegebenen Punkt einsetzen.
 54      Zwei freie Werte: bei einer Form wie r · x₂ + s · x₃ = 0 einen Wert frei wählen und den anderen bestimmen – beide null ergibt keine Ebenengleichung.
 55      Punkt mit Koordinatenbedingung: drei gleiche Koordinaten heißt, denselben Buchstaben für alle drei einsetzen und auflösen.
 56      Auswendig (Teil A): „Der freie Parameter“ – dieselbe Anlagenzeile wie die Punktprobe, rückwärts gelesen (Teil-A-Belege 2023MgrundlegendAAGLAA22-a, 2026MerhoehtAAGLAA221-a, 2019MerhoehtAAGLAA22-a).
 57      Formelsammlung: keine – [FS] offen
 58  Quelle: eigene Formulierung nach [GOST Q3 L3] „Lagebeziehungen zwischen: … Punkt und Ebene“; Zahlenbeispiel aus dem Pool (2023MgrundlegendAAGLAA22-a, wörtlich); [LS-AA QP VI 8].
 59
 60  Einheit 3 (Gerade und Ebene):
 61      Einsetzen des allgemeinen Geradenpunkts: die Koordinaten der Geradengleichung in die Ebenengleichung einsetzen. Fällt der Parameter heraus und stimmt die Gleichung, liegt die ganze Gerade in der Ebene; fällt er heraus und stimmt sie nicht, ist die Gerade echt parallel; bleibt er stehen, gibt es genau einen Schnittpunkt (dessen Berechnung → schnittmengen.md).
 62        g: x = (0 | 1 | 1) + λ · (1 | 0 | −1), E: x + y + z = 2: λ + 1 + 1 − λ = 2 – wahr für jedes λ, g liegt in E.
 63      Merkregel über das Skalarprodukt: Richtungsvektor mal Normalenvektor gleich null → parallel oder enthalten (die Punktprobe des Stützpunkts entscheidet); ungleich null → genau ein Schnittpunkt.
 64      Parallel zur Koordinatenebene: die Gerade durch zwei Punkte ist genau dann parallel zur xy-Ebene, wenn beide Punkte dieselbe dritte Koordinate haben – ein Parameter in einer anderen Koordinate ändert daran nichts.
 65      Mit Scharparameter: die Merkregel liefert die Fallunterscheidung – für welche Parameterwerte ist das Skalarprodukt null, und was sagt dann die Punktprobe; die übrigen Werte geben den parameterabhängigen Schnittpunkt.
 66      Auswendig (Teil A): „Einsetzen des allgemeinen Geradenpunkts“ und „Merkregel über das Skalarprodukt“ – [GOST-OHiMi 2.3] „Lagebeziehungen zwischen Punkten, Geraden und Ebenen“, „Skalarprodukt in Koordinatenform“, „Orthogonalität von Vektoren“ (Teil-A-Belege 2023MerhoehtAAGLAA213-a, 2024MgrundlegendAAGLAA213-a); die Scharfälle sind LK-Stoff („auch Scharen“).
 67      Formelsammlung: keine – Lageregeln stehen nicht in der Formelsammlung – [FS] offen
 68  Quelle: eigene Formulierung nach [GOST Q3 L3] „Lagebeziehungen zwischen: … Gerade und Ebene“, LK-Zusatz „(Scharen)“ und [GOST-OHiMi 2.3]; Zahlenbeispiel aus dem Pool (2023MerhoehtAAGLAA213-a, wörtlich; wortgleiche Dublette 2023-bebb-lk-A1.5a); [LS-AA QP VI 8].
 69
 70  Einheit 4 (Lagebefunde im Sachzusammenhang):
 71      Licht und Schatten: der Schattenpunkt ist der Durchstoßpunkt der Lichtgeraden (durch den Punkt in Lichtrichtung, oder von der Lampe durch den Punkt) mit der Wand- oder Bodenebene – die feste Koordinate der Wand liefert den Parameter.
 72      Der Befund danach: der berechnete Punkt beantwortet die Frage erst, wenn seine Koordinaten gegen die Maße geprüft sind – liegt der Schatten auf der Wand, das Auftreffen im Spielfeld, der Durchstoßpunkt unterhalb der Netzkante?
 73      Bahnen: Auftreffen auf dem Boden heißt dritte Koordinate null (bei Bahnkurven eine quadratische Gleichung im Zeitparameter, die passende Lösung wählen); Berühren eines Netzes heißt, die Höhe im Durchstoßpunkt der Netzebene mit der Netzhöhe zu vergleichen.
 74      Auswendig (Teil A): keine – die Sachbefunde stellen die Kataloge in Teil B (Rechner, Maße); sitzen müssen Punktprobe und Einsetzregel (Kästen eins und drei).
 75      Formelsammlung: keine – [FS] offen
 76  Quelle: eigene Formulierung nach [GOST Q3 L3] „Lagebeziehungen …“ und der Poolpraxis der Rohdatei (Kulisse, Rollo, Hauswand, Beachvolleyball); ohne Zahlenbeispiel (Sacharbeit); [LS-AA QP VI 8 sinngemäß – die Sachformen haben keine eigene Lehrwerkseinheit].
 77
 78  ### Typische Fehler
 79  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 38 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Analytischen Geometrie, die Muster sind allein aus den Katalogzeilen belegt.
 80  - Punktprobe unvollständig oder falsch gelesen: nur den Stützpunkt eingesetzt, die dritte Gleichung der Parameterprobe nicht geprüft, eine fehlende Variable in der Gleichung als Fehler gedeutet oder eine nicht vorkommende Koordinate einsetzen wollen, den Richtungsvektor statt des Stützpunkts eingesetzt. [abi 2021-be-gk-A1.4b, 2021-be-gk-A1.5a, 2022-bebb-gk-A1.4a, 2023-bebb-lk-A1.5a, 2026-bb-ea-A1.8a; iqb 2022MgrundlegendAAGLAA211-a, 2021MerhoehtAAGLAA211-a, 2018MerhoehtAAGLAA211-a, 2023MerhoehtAAGLAA213-a, 2026MerhoehtAAGLAA221-a, 2026MerhoehtBAGLAA2MMS2-1d]
 81  - Seitenargument verkürzt: nur eine der beiden Ebenen geprüft und die Bedingung an die Koordinatenebenen vergessen; die Ebene nur an Eckpunkten geprüft statt mit dem Vorzeichenargument fürs Innere. [abi 2023-bebb-gk-B3f; iqb 2019MgrundlegendBAGLAA2WTR2-1c]
 82  - Gegenbeispiel falsch gebaut: einen Punkt mit gleichen Tauschkoordinaten gewählt (dann ändert der Tausch nichts) oder nicht geprüft, dass der Punkt wirklich innen liegt. [iqb 2026MerhoehtBAGLAA2MMS2-1c]
 83  - Parameterbestimmung verfehlt: den falschen Punkt eingesetzt, einen Punkt gewählt, an dem der Parameter herausfällt, beide freien Werte null gesetzt, den Parameter aus einem einzelnen Koeffizienten geraten. [abi 2022-bebb-lk-B3h; iqb 2022MerhoehtBAGLAA2WTR1-1e, 2023MgrundlegendAAGLAA22-a, 2023MgrundlegendBAGLAA2WTR1-1b, 2023MerhoehtBAGLAA2WTR1-1b, 2019MerhoehtAAGLAA22-a]
 84  - Lage von Gerade und Ebene verkürzt: nur den Stützpunkt geprüft und „liegt darin“ geschlossen; den Fall des herausfallenden Parameters als „parallel“ abgeschlossen, ohne die Punktprobe zu führen; einen Vorzeichenfehler beim Einsetzen des Scharparameters gemacht; die Parallelität zur Koordinatenebene am Parameter statt an den festen Koordinaten gesucht. [abi 2024-bebb-lk-A1.8a, 2024-bebb-gk-A1.2a; iqb 2024MgrundlegendAAGLAA213-a]
 85  - Orthogonalitätsbedingung verwechselt: für die Orthogonalität von Gerade und Ebene das Skalarprodukt von Richtungs- und Normalenvektor null erwartet (statt der Kollinearität), für orthogonale Ebenen ein Skalarprodukt ungleich null, für den Normalenvektor ein Skalarprodukt null mit sich selbst. [abi 2026-bb-gk-A1.2a, 2018-be-gk-B2.1b, 2025-bebb-gk-A1.5b; iqb 2026MgrundlegendAAGLAA211-a, 2025MgrundlegendAAGLAA213-b]
 86  - Schar unvollständig geprüft: nur die Spitze geprüft und die Grundfläche vergessen; nur eine Beispielebene genannt, wo unendlich viele zu begründen waren; die Kreisbahn behauptet, ohne zu prüfen, dass der Punkt in der Ebene liegt. [abi 2026-bb-ea-B3d; iqb 2020MerhoehtAAGLAA22-b, 2019MerhoehtAAGLAA22-b, 2026MerhoehtBAGLAA2WTR2-1d]
 87  - Sachbefund nicht geführt: nur den Schnittpunkt berechnet und die Wandmaße nicht geprüft; nur die Zeit berechnet und die Lage nicht geprüft; die Netzebene falsch angesetzt; den Schatten an der falschen Kante beginnen lassen; den zweiten Lösungsschritt falsch gedeutet; die Kante im vorgelegten Lösungsweg falsch benannt. [iqb 2020MerhoehtAAGLAA212, 2018MerhoehtBAGLAA2WTR3-1e, 2018MerhoehtBAGLAA2WTR3-1g, 2023MgrundlegendBAGLAA2WTR1-1g, 2024MgrundlegendBAGLAA2WTR1-1d, 2024MgrundlegendBAGLAA2WTR2-1d]
 88
 89  ### Für schwache Schüler
 90  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q3 Brandenburg und Berlin: die Lagebeziehungs-Zeile für Punkt–Ebene und Gerade–Ebene – Einheit 1 (Punktprobe an beiden Formen), Einheit 2 (der freie Parameter als Rückrichtung), Einheit 3 ohne die Scharen (Einsetzen und Merkregel), Einheit 4 als Teil-B-Anwendung. Ohne Hilfsmittel (Anlage OHiMi 2.3, Prüfungsteil A): „Lagebeziehungen zwischen Punkten, Geraden und Ebenen“ mit Skalarprodukt und Orthogonalität – die Kästen eins bis drei ohne das Seitenargument. LK-Zusatz: die Fallunterscheidungen an Scharen (Einheit 3; amtlich „auch Scharen“) – für GK-Schüler Vorrat. Weiterer Vorrat (Ermessen nach dem Niveau der Rohdatei): das Seitenargument fürs Innere (Einheit 1, Niveau III), die Existenzbegründung und die Kreisbahn (Einheit 3), die vollständigen Sachbefunde (Einheit 4, Niveau III). Niveaustufe H der E-Phase [RLP]: kein Posten – die Sek-I-Pläne kennen keine Ebenen; der nächste Anker ist die Gleichung als Punktmenge (lineare-funktionen.md), Blatt-0-Stoff der Grundvorstellung. RLP FOS (fhr): kein Bestand – das Wahlthema endet bei Punkt–Gerade und Gerade–Gerade. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Lagebeziehungen von Geraden und Ebenen – wenn das zutrifft, deckt es sich mit dem GK-Kern, kein zusätzlicher Posten.
 91  Grundvorstellung (Blatt 0) [GOST Q3 L3, MO]: Eine Ebenengleichung ist ein Türsteher – sie prüft jeden Punkt und sagt drinnen oder draußen, und bei draußen sogar, auf welcher Seite. „Hier ist eine Koordinatengleichung als Prüfregel und ein Stapel Punktkärtchen, keine Skizze. Sortiere die Kärtchen in drei Stapel: Gleichung erfüllt, linke Seite zu klein, linke Seite zu groß. Was haben die Punkte eines Stapels miteinander zu tun? Zwei Kärtchen liegen auf demselben Stapel – kann die Strecke zwischen ihren Punkten durch die Ebene hindurchführen? Und die Kärtchen des Erfüllt-Stapels: liegen ihre Punkte in der Mitte der Ebene oder am Rand – gibt es überhaupt einen Rand?“ Wer die Gleichung nur als Rechenaufgabe löst, ohne den Befund zu benennen, wer die Seite nicht am Vorzeichen abliest oder wer der Ebene einen Rand gibt, braucht das vor jeder Rechnung: Die Gleichung beschreibt alle Punkte der Ebene und teilt den Rest des Raums in zwei Seiten. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q3-Kern „Lagebeziehungen zwischen: … Punkt und Ebene“), liegt aber im Kurshalbjahr selbst, nicht in den Eingangsvoraussetzungen (Klarstellung Geometrie); die Aufgabenform ist Ermessen. [GOST Q3 L3; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „nur den Stützpunkt einsetzen“, abi 2023-bebb-lk-A1.5a; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
 92  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
 93  - Punktprobe und Seitenlage (Einheit 1): „Erfüllt, größer oder kleiner?“ – zu Punktproben ankreuzen, was das Einsetzen liefert und was es heißt (drin, diese Seite, jene Seite); nichts rechnen (Vorstufe, Grundvorstellung) → die Punktprobe an der Koordinatengleichung führen und den Befund benennen (Grundfall, viermal; abi 2022-bebb-gk-A1.4a, iqb 2022MgrundlegendAAGLAA211-a, 2021MerhoehtAAGLAA211-a, 2018MerhoehtAAGLAA211-a, Teil A) → die fehlende Variable richtig lesen (iqb 2022MgrundlegendAAGLAA211-a als Stolperstelle) → die Punktprobe an der Parameterform: zwei Parameter, dritte Gleichung (abi 2021-be-gk-A1.5a, Teil A) → die Probe im Sachaufbau: Punkt in der Fahrbahnebene (abi 2018-be-gk-B2.1b), Punkt in der Ebene samt Normalenvektor-Anschluss (abi 2025-bebb-gk-A1.5b, 2026-bb-gk-A1.2a; iqb 2025MgrundlegendAAGLAA213-b, 2026MgrundlegendAAGLAA211-a, Teil A) → die Aufgabenstellung aus einem vorgelegten Lösungsweg formulieren (iqb 2024MgrundlegendBAGLAA2WTR2-1d) → Seite gegen den Ursprung: den Punkt in die nach null umgestellte Gleichung einsetzen und das Vorzeichen mit dem des Ursprungs vergleichen → das Seitenargument: zwischen zwei parallelen Ebenen über die Vorzeichen (abi 2023-bebb-gk-B3f, Niveau III) und der Verlauf durchs Innere über Punktproben und Vorzeichen (iqb 2019MgrundlegendBAGLAA2WTR2-1c) → Prüfungshöhe: die Allaussage über das Innere mit einem Gegenbeispiel unter Koordinatentausch widerlegen (iqb 2026MerhoehtBAGLAA2MMS2-1c, Niveau II, MMS).
 94  - Parameter aus der Lagebedingung (Einheit 2): „Wer und wogegen?“ ankreuzen (Vorstufe) → den freien Parameter aus einem enthaltenen Punkt bestimmen (Grundfall, viermal; iqb 2023MgrundlegendAAGLAA22-a, Teil A; abi 2022-bebb-lk-B3h, iqb 2022MerhoehtBAGLAA2WTR1-1e mit Kontrollwert) → den richtigen Punkt wählen, wenn einer den Parameter herausfallen lässt (iqb 2023MgrundlegendAAGLAA22-a als Stolperstelle) → zwei freie Werte: einen wählen, den anderen bestimmen (iqb 2023MgrundlegendBAGLAA2WTR1-1b, 2023MerhoehtBAGLAA2WTR1-1b) → den Parameter aus dem gemeinsamen Punkt einer Geradenschar gewinnen (abi 2026-bb-ea-A1.8a, iqb 2026MerhoehtAAGLAA221-a, Teil A) → Prüfungshöhe: den Punkt der Ebene mit drei gleichen Koordinaten bestimmen (iqb 2019MerhoehtAAGLAA22-a, Niveau II, Teil A).
 95  - Gerade und Ebene (Einheit 3): „Fällt der Parameter heraus?“ – beim Einsetzen des allgemeinen Geradenpunkts ankreuzen, was gilt: fällt heraus und stimmt, dann liegt sie darin; fällt heraus und stimmt nicht, dann parallel; bleibt, dann ein Schnittpunkt; nichts rechnen (Vorstufe) → den allgemeinen Geradenpunkt einsetzen und „liegt in der Ebene“ nachweisen (Grundfall, viermal; abi 2023-bebb-lk-A1.5a, 2021-be-gk-A1.4b; iqb 2023MerhoehtAAGLAA213-a, 2026MerhoehtBAGLAA2MMS2-1d) → die Merkregel über das Skalarprodukt anwenden und die drei Fälle benennen → die Parallelität zur Koordinatenebene über die festen Koordinaten entscheiden (abi 2024-bebb-gk-A1.2a, iqb 2024MgrundlegendAAGLAA213-a, Teil A) → die Kreisbahn der Drehung als Kreis in der Ebene senkrecht zur Achse begründen (abi 2026-bb-ea-B3d, iqb 2026MerhoehtBAGLAA2WTR2-1d) → die Existenz unendlich vieler Ebenen ohne Punkt mit gleichen Koordinaten begründen (iqb 2019MerhoehtAAGLAA22-b, Niveau III, Teil A) → Prüfungshöhe: die Lage einer Geradenschar zur Ebene mit Fallunterscheidung untersuchen und den parameterabhängigen Schnittpunkt angeben, Kontrolle: den Schnittpunkt in die Ebenengleichung einsetzen, sie muss erfüllt sein (abi 2024-bebb-lk-A1.8a, Niveau II, Teil A, LK) und die Parameterwerte gemeinsamer Punkte der Pyramidenschar bestimmen (iqb 2020MerhoehtAAGLAA22-b, Niveau III, Teil A).
 96  - Lagebefunde im Sachzusammenhang (Einheit 4): „Rechnung fertig – Frage beantwortet?“ – zu Sachaufgaben ankreuzen, ob nach dem Durchstoßpunkt noch ein Bereich zu prüfen ist (Wandmaße, Feldgrenzen, Netzhöhe); nichts rechnen (Vorstufe) → den Schattenpunkt als Durchstoßpunkt bestimmen und die Wandmaße prüfen (Grundfall, viermal; iqb 2020MerhoehtAAGLAA212, Teil A) → den vorgelegten Lösungsweg zum Schatten erläutern: Spurpunkt, Bereich, Sachdeutung (iqb 2023MgrundlegendBAGLAA2WTR1-1g, 2024MgrundlegendBAGLAA2WTR1-1d, Niveau II bis III) → das Berühren des Netzes über die Höhe im Durchstoßpunkt untersuchen (iqb 2018MerhoehtBAGLAA2WTR3-1e) → Prüfungshöhe: den Auftreffpunkt der Bahnkurve berechnen und die Lage im Spielfeld prüfen – quadratische Gleichung, passende Lösung, Bereichsprüfung (iqb 2018MerhoehtBAGLAA2WTR3-1g, Niveau III).
 97
 98  ### Prüfungsform (fhr / abi / iqb)
 99  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; das Thema ist dort kein Stoff, themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 43 Zeilen mit 19 Haupttypen (abi 14 Zeilen, 8 Typen; iqb 29 Zeilen, 16 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; das Thema führt die Gegenstandsklassen „Punkt und Ebene“ und „Gerade und Ebene“ als Präfix vor dem Doppelpunkt – die Klassen „Geraden“ und „Ebenen“ liegen nach abitur-vokabular.md § 4 bei geraden.md und ebenen.md). Pool-Sachgebiet: Alternative A2 „Analytische Geometrie“ der Aufgabengruppe AG/LA [IQB-STR 1].
100  fhr: kein Bestand, keine Zeile – das Wahlthema 5 des RLP FOS 2019 endet bei den Lagen Punkt–Gerade und Gerade–Gerade; der fhr-Katalog führt kein Thema der Analytischen Geometrie.
101  abi (14 Zeilen, 8 Typen; Landeshefte be-gk, bebb-gk, bebb-lk, bb-gk, bb-ea 2017–2026) [abi-Katalog]: Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (5, E1) · Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (2, E3) · Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (2, E2) · je 1: Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen (E3) · Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen (E3) · Gerade und Ebene: Parallelität einer Geraden zu einer Ebene über das Skalarprodukt von Richtungs- und Normalenvektor nachweisen (E3) · Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden (E3) · Punkt und Ebene: Lage eines Punktes zwischen zwei parallelen Ebenen über Einsetzen in die Koordinatengleichungen begründen (E1). Muster: Das Thema ist der Teil-A-Klassiker der Landeshefte – 9 der 14 Zeilen stehen in Teil A (ein bis fünf Punkte): Punktproben an Koordinaten- und Parameterform (2021-be-gk-A1.5a, 2022-bebb-gk-A1.4a, 2025-bebb-gk-A1.5b, 2026-bb-gk-A1.2a), die Gerade in der Ebene (2021-be-gk-A1.4b, 2023-bebb-lk-A1.5a), die Parallelität zur xy-Ebene (2024-bebb-gk-A1.2a), der Scharparameter (2026-bb-ea-A1.8a) und die Geradenschar-Fallunterscheidung des Leistungskurses (2024-bebb-lk-A1.8a); Teil B trägt die Parallelität der neuen Flugbahn zur Wolkenuntergrenze über Richtungs- und Normalenvektor (2017-be-gk-B2.1d, vier Punkte, Niveau II; seit dem Nachzug 2026-09-28), die Punktprobe im Sachaufbau (2018-be-gk-B2.1b), den freien Parameter mit Kontrollwert (2022-bebb-lk-B3h), das Seitenargument fürs Innere (2023-bebb-gk-B3f, Niveau III) und die Kreisbahn der Drehung (2026-bb-ea-B3d). 8 der 14 Zeilen sind wortgleiche Pooldubletten (2022-bebb-gk-A1.4a, 2022-bebb-lk-B3h, 2023-bebb-lk-A1.5a, 2024-bebb-gk-A1.2a, 2025-bebb-gk-A1.5b, 2026-bb-gk-A1.2a, 2026-bb-ea-A1.8a, 2026-bb-ea-B3d); Landeszusätze sind die Berliner Zeilen 2017–2021 und die beiden Begründungen 2023–2024 (2023-bebb-gk-B3f, 2024-bebb-lk-A1.8a). Niveau I 5, II 8, III 1 (2023-bebb-gk-B3f).
102  iqb (29 Zeilen, 16 Typen; Pool 2017–2026, grundlegend 11 und erhöht 18 Zeilen, Teil A 13 und Teil B 16 Zeilen, davon 2 MMS und 1 CAS) [iqb-Katalog]: Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (5, E1) · Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (5, E2) · Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden (3, E3) · Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (2, E3) · Gerade und Ebene: Länge eines Schattens auf einer Dachfläche über Schnitt von Lichtgerade und Ebene beschreiben (2, E4) · Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern (2, E4) · je 1: Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen (E4) · Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen (E3) · Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen (E3) · Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen (E4) · Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren (E1) · Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen (E4) · Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen (E1) · Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen (E3) · Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen (E2) · Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen (E1). Muster: Teil A (13 Zeilen, ein bis fünf Punkte) prüft Punktproben (2018MerhoehtAAGLAA211-a, 2021MerhoehtAAGLAA211-a, 2022MgrundlegendAAGLAA211-a, 2025MgrundlegendAAGLAA213-b, 2026MgrundlegendAAGLAA211-a), Parameterbestimmungen (2023MgrundlegendAAGLAA22-a, 2026MerhoehtAAGLAA221-a, 2019MerhoehtAAGLAA22-a), die Gerade in der Ebene (2023MerhoehtAAGLAA213-a), die Parallelität zur xy-Ebene (2024MgrundlegendAAGLAA213-a), den Kulissenschatten (2020MerhoehtAAGLAA212), die Pyramidenschar (2020MerhoehtAAGLAA22-b) und die Existenzbegründung (2019MerhoehtAAGLAA22-b) – die beiden letzten tragen Anforderungsbereich III; Teil B stellt die Sachbefunde (Beachvolleyball 2018MerhoehtBAGLAA2WTR3-1e/1g, Haus mit Glasfassade 2019MgrundlegendBAGLAA2WTR2-1c, Rollo-Schatten 2023MgrundlegendBAGLAA2WTR1-1g, Hauswand 2024MgrundlegendBAGLAA2WTR1-1d, Kantenprobe 2024MgrundlegendBAGLAA2WTR2-1d), die Parameterbestimmungen (2022MerhoehtBAGLAA2WTR1-1e, 2023MgrundlegendBAGLAA2WTR1-1b, 2023MerhoehtBAGLAA2WTR1-1b) und die MMS-Zeilen (2026MerhoehtBAGLAA2MMS2-1c/1d) samt Kreisbahn (2026MerhoehtBAGLAA2WTR2-1d); seit dem Nachzug 2026-09-28 dazu der Jahrgang 2017 – die Parallelität der Geraden AB zur x1x2-Ebene über gleiche dritte Koordinaten auf beiden Niveaus (2017MgrundlegendBAGLAA2WTR2-1a, 2017MerhoehtBAGLAA2WTR2-1a, je zwei Punkte, Niveau I) und die beschriebene Berechnung der Schattenlänge auf der Dachfläche des Spielplatzturms (2017MerhoehtBAGLAA2WTR1-1e, wortgleich in der CAS-Fassung 2017MerhoehtBAGLAA2CAS1-1f, je vier Punkte, Niveau II). Amtlicher Anforderungsbereich in allen 29 Zeilen (höchster Bereich: I 9, II 16, III 4); Niveau I 9, II 16, III 4. Kontexte: Beachvolleyballfeld, Kulisse mit Lampe, Rollo und Hauswand im Sonnenlicht, Haus mit Glasfassade, Pyramidenzelt, Quader mit Trinkhalm, Spielplatzturm. 8 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste).
103  Zielmarke: Einheit 1 – abi: die Punktprobe an der Parameterform (2021-be-gk-A1.5a, Niveau I, Teil A) und das Seitenargument fürs Innere (2023-bebb-gk-B3f, Niveau III); iqb: die Punktprobe mit Normalenvektor-Anschluss (2025MgrundlegendAAGLAA213-b, 2026MgrundlegendAAGLAA211-a, Niveau II, Teil A) und das Koordinatentausch-Gegenbeispiel (2026MerhoehtBAGLAA2MMS2-1c, Niveau II). Einheit 2 – abi: der Parameter mit Kontrollwert am Quader (2022-bebb-lk-B3h, Niveau II); iqb: der Punkt mit drei gleichen Koordinaten (2019MerhoehtAAGLAA22-a, Niveau II, Teil A). Einheit 3 – abi: die Geradenschar-Fallunterscheidung (2024-bebb-lk-A1.8a, Niveau II, Teil A, LK) und die Kreisbahn (2026-bb-ea-B3d, Niveau II); iqb: die Pyramidenschar (2020MerhoehtAAGLAA22-b, Niveau III, Teil A) und die Existenzbegründung (2019MerhoehtAAGLAA22-b, Niveau III, Teil A). Einheit 4 – abi: keine (die Sachbefunde stellt nur der Pool); iqb: der Auftreffpunkt im Spielfeld (2018MerhoehtBAGLAA2WTR3-1g, Niveau III) und der erläuterte Rollo-Schatten (2023MgrundlegendBAGLAA2WTR1-1g, Niveau III).
````

## 2 Originale (42)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2021-be-gk-A1.5a (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: P(4 | 6 | 4); E: x = (1 | 2 | 3) + t · (0 | 2 | 1) + s · (3 | 0 | −1), t, s ∈ IR
- gesucht: Nachweis, dass P in E liegt
- verfahren: Gleichsetzen, t und s aus zwei Gleichungen, dritte prüfen
- fehlerquelle: die dritte Gleichung nicht prüfen

### 2022-bebb-gk-A1.4a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 1 · format Rechnung · antwort Text
- gegeben: E: 3x − 2y = 0; Punkt (1 | 1,5 | 7)
- gesucht: ob der Punkt in E liegt
- verfahren: Einsetzen
- fehlerquelle: fehlende z-Koordinate in der Gleichung als Fehler deuten

### 2025-bebb-gk-A1.5b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 3 · format Begründung · antwort Text
- gegeben: P(0; −1; 1), Q(2; 5; 3); E: x1 + 3x2 + x3 = 20
- gesucht: Nachweis, dass Q in E liegt|Nachweis, dass PQ ein Normalenvektor von E ist
- verfahren: Q in die Koordinatengleichung einsetzen; PQ = (2; 6; 2) = 2 · (1; 3; 1) mit dem Normalenvektor vergleichen
- fehlerquelle: für den Normalenvektor das Skalarprodukt PQ · (1; 3; 1) = 0 erwarten

### 2026-bb-gk-A1.2a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Ebene E: x1 − 3x2 + 2x3 = 11; Gerade g durch P(5; 0; 3) und Q(9; −12; 11)
- gesucht: Nachweis, dass P in E liegt|Begründung, dass g senkrecht zu E steht
- verfahren: P in die Koordinatengleichung einsetzen; Richtungsvektor PQ = (4; −12; 8) mit dem Normalenvektor (1; −3; 2) vergleichen: PQ = 4 · n, also kollinear
- fehlerquelle: für die Orthogonalität das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten

### 2021-be-gk-A1.4b (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: E: 2x + y + 4z = 6; Gerade s: x = (1 | −4 | 2) + r · (0 | 8 | −2), r ∈ IR, liegt in F
- gesucht: Nachweis, dass s auch in E liegt
- verfahren: Koordinaten von s in E einsetzen; r fällt heraus
- fehlerquelle: nur den Stützpunkt prüfen

### 2023-bebb-lk-A1.5a (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 2 · format Begründung · antwort Text
- gegeben: g: x = (0; 1; 1) + λ · (1; 0; −1), λ reell; Ebene x + y + z = 2
- gesucht: Nachweis, dass g in der Ebene liegt
- verfahren: allgemeinen Punkt von g einsetzen
- fehlerquelle: nur den Stützpunkt einsetzen

### 2024-bebb-gk-A1.2a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: P(2 | 0 | 23) und Q(6 | t | 20), t ∈ IR
- gesucht: ob es ein t gibt, für das die Gerade PQ parallel zur x-y-Ebene verläuft, mit Begründung
- verfahren: Richtungsvektor hat z-Komponente −3 unabhängig von t
- fehlerquelle: Parallelität über t in der y-Koordinate suchen

### 2026-bb-ea-A1.8a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 1 · format Rechnung · antwort Zahl
- gegeben: g_a: x = (1; −1; −3) + t · (1; a; −2a) für reelle a und t; E: 2x2 + x3 = c; jede Gerade g_a liegt in E
- gesucht: Wert von c
- verfahren: der gemeinsame Punkt (1; −1; −3) aller Geraden liegt in E: 2 · (−1) + (−3) = c
- fehlerquelle: den Richtungsvektor statt des Stützpunkts einsetzen

### 2024-bebb-lk-A1.8a (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-lk · punkte 5 · format Rechnung · antwort Term
- gegeben: E: −x + 2z = −3; Geradenschar g_a: x = (3a + 2; −3; a) + r · (−2; 2; −a), r ∈ IR, a ∈ IR
- gesucht: Lagebeziehung zwischen g_a und E in Abhängigkeit von a, gegebenenfalls Koordinaten des Schnittpunkts
- verfahren: Skalarprodukt n · u auswerten; Fall a = 1 mit Punktprobe; sonst Geradenpunkt in die Ebenengleichung einsetzen
- fehlerquelle: Fall a = 1 als „parallel“ ohne Punktprobe abschließen; Vorzeichenfehler beim Einsetzen des Parameters

### 2017-be-gk-B2.1d (abi-katalog.csv)

jahr 2017 · papier 2017-be-gk · punkte 4 · format Begründung|Rechnung · antwort Text|Zahl
- gegeben: Die untere Begrenzung einer dichten Wolkendecke liegt in der Ebene E: x − 20z = −1560. Die neue Flugbahn des Jets ist h: x = (1740 | 350 | 300) + s · (90 | 16,5 | 4,5); er überfliegt das Rathaus R(8040 | 1505 | 0) in 615 m Höhe. Der Bürgermeister schaut vom Rathaus in dem Moment nach oben, in dem der Jet genau darüber ist; 1 LE = 1 m.
- gesucht: Nachweis, dass die neue Flugbahn parallel zur Wolkenuntergrenze verläuft; Untersuchung, ob der Bürgermeister den Jet sehen kann oder nur die Wolkendecke
- verfahren: Normalenvektor n = (1 | 0 | −20) von E; r_neu · n = 90 − 90 = 0, also ist h parallel zu E (P10 erfüllt die Gleichung nicht, h liegt nicht in E). Über dem Rathaus x = 8040 in E einsetzen: 8040 − 20z = −1560 liefert die Höhe der Wolkenuntergrenze; mit der Flughöhe 615 m vergleichen.
- fehlerquelle: Richtungsvektor und Normalenvektor auf Kollinearität statt auf Orthogonalität prüfen oder die Wolkenhöhe über P10 statt über dem Rathaus berechnen

### 2018-be-gk-B2.1b (abi-katalog.csv)

jahr 2018 · papier 2018-be-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Ebene E: −10x + y = 0 und der Punkt D(4,8 | 48 | 9); die Fahrbahn liegt in der x-y-Ebene, 1 LE = 1 m.
- gesucht: Nachweis, dass D in E liegt; Nachweis, dass E orthogonal zur x-y-Ebene liegt
- verfahren: D in die Ebenengleichung einsetzen: −10 · 4,8 + 48 = 0, die Gleichung ist erfüllt. Für die Orthogonalität das Skalarprodukt der Normalenvektoren n_E = (−10 | 1 | 0) und n_xy = (0 | 0 | 1) bilden; es ist null, also stehen die Ebenen senkrecht aufeinander.
- fehlerquelle: für orthogonale Ebenen ein Skalarprodukt der Normalenvektoren ungleich null erwarten, weil die Bedingung mit der für orthogonale Geraden verwechselt wird

### 2022-bebb-lk-B3h (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Quader mit Ecken A und Q(1|1|3), Seitenflächen achsenparallel; BCD_k enthält die Quaderecken P und R; Kontrolle k = 4
- gesucht: dieser Wert von k
- verfahren: P(1|0|3) in L_k einsetzen
- fehlerquelle: Q statt P einsetzen (ergibt k = 6)

### 2023-bebb-gk-B3f (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-gk · punkte 3 · format Begründung · antwort Text
- gegeben: Körper ABCDEF: Die Eckpunkte A(4 | 0 | 0), B(0 | 4 | 0) und C(0 | 0 | 4) liegen in der Ebene L1: x + y + z = 4, die Eckpunkte D, E und F jeweils auf einer Koordinatenachse und in der Ebene L2: 2x + 2y + 2z = 5 (also D(2,5 | 0 | 0), E(0 | 2,5 | 0), F(0 | 0 | 2,5)). Die Oberfläche des Körpers besteht aus zwei Dreiecken (in L1 und L2) und drei Trapezen (in den Koordinatenebenen); T(1 | 1 | 1).
- gesucht: Begründung, dass T im Inneren des Körpers ABCDEF liegt
- verfahren: Der Körper ist der Teil des ersten Oktanten zwischen L2 und L1. T hat positive Koordinaten und liegt wegen 2 · 3 = 6 > 5 auf der vom Ursprung abgewandten Seite von L2 und wegen 3 < 4 auf der Ursprungsseite von L1.
- fehlerquelle: nur eine Ebene prüfen; die Bedingung an die Koordinatenebenen vergessen

### 2026-bb-ea-B3d (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Pyramide wird um die Gerade CD um 360° gedreht; Spitze S durchläuft einen Kreis; L: −2x + y + 4 = 0; H = CD ∩ L
- gesucht: Begründung, dass der Kreis in L liegt und H sein Mittelpunkt ist
- verfahren: L senkrecht zur Achse und durch S, Mittelpunkt auf der Achse
- fehlerquelle: S ∈ L nicht prüfen

### 2018MerhoehtAAGLAA211-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 1 · format Begründung · antwort Text
- gegeben: E: x2 − 3x3 = −19; S(−2 | −4 | 5)
- gesucht: Nachweis, dass S in E liegt
- verfahren: Einsetzen
- fehlerquelle: x1 = −2 mit einsetzen wollen (kommt nicht vor)

### 2021MerhoehtAAGLAA211-a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 1 · format Rechnung · antwort Text
- gegeben: P(−1; 7; 2), E: x1 + 3x2 = 0
- gesucht: Nachweis, dass P nicht in E liegt
- verfahren: einsetzen
- fehlerquelle: x3 = 2 einsetzen wollen (kommt nicht vor)

### 2022MgrundlegendAAGLAA211-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 1 · format Rechnung · antwort Text
- gegeben: E: 3 · x − 2 · y = 0; Punkt (1; 1,5; 7)
- gesucht: Prüfung, ob der Punkt in E liegt
- verfahren: einsetzen
- fehlerquelle: die dritte Koordinate 7 vermissen und deshalb zweifeln

### 2025MgrundlegendAAGLAA213-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: P(0; −1; 1), Q(2; 5; 3); E: x1 + 3x2 + x3 = 20
- gesucht: Nachweis, dass Q in E liegt|Nachweis, dass PQ ein Normalenvektor von E ist
- verfahren: Q in die Koordinatengleichung einsetzen; PQ = (2; 6; 2) = 2 · (1; 3; 1) mit dem Normalenvektor vergleichen
- fehlerquelle: für den Normalenvektor das Skalarprodukt PQ · (1; 3; 1) = 0 erwarten

### 2026MgrundlegendAAGLAA211-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Ebene E: x1 − 3x2 + 2x3 = 11; Gerade g durch P(5; 0; 3) und Q(9; −12; 11)
- gesucht: Nachweis, dass P in E liegt|Begründung, dass g senkrecht zu E steht
- verfahren: P in die Koordinatengleichung einsetzen; Richtungsvektor PQ = (4; −12; 8) mit dem Normalenvektor (1; −3; 2) vergleichen: PQ = 4 · n, also kollinear
- fehlerquelle: für die Orthogonalität das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten

### 2023MgrundlegendAAGLAA22-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 1 · format Rechnung · antwort Zahl
- gegeben: Dreieck ABC mit A(5; 0; 0), B(0; 3; 0), C(0; 0; 4) in der Abbildung; seine Ebene hat eine Gleichung der Form 12x + 20y + tz = 60
- gesucht: Wert von t
- verfahren: C einsetzen
- fehlerquelle: A oder B einsetzen, wo t herausfällt

### 2026MerhoehtAAGLAA221-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 1 · format Rechnung · antwort Zahl
- gegeben: g_a: x = (1; −1; −3) + t · (1; a; −2a) für reelle a und t; E: 2x2 + x3 = c; jede Gerade g_a liegt in E
- gesucht: Wert von c
- verfahren: der gemeinsame Punkt (1; −1; −3) aller Geraden liegt in E: 2 · (−1) + (−3) = c
- fehlerquelle: den Richtungsvektor statt des Stützpunkts einsetzen

### 2019MerhoehtAAGLAA22-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 2 · format Rechnung · antwort Zahl
- gegeben: E: 3x1 + 2x2 + 2x3 = 6 enthält einen Punkt mit drei übereinstimmenden Koordinaten
- gesucht: diese Koordinaten
- verfahren: a für alle drei Koordinaten einsetzen und lösen
- fehlerquelle: a = 6/3 aus dem ersten Koeffizienten

### 2023MerhoehtAAGLAA213-a (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: g: x = (0; 1; 1) + λ · (1; 0; −1), λ reell; Ebene x + y + z = 2
- gesucht: Nachweis, dass g in der Ebene liegt
- verfahren: allgemeinen Punkt von g einsetzen
- fehlerquelle: nur den Stützpunkt einsetzen

### 2024MgrundlegendAAGLAA213-a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: P(2; 0; 23) und Q_t(6; t; 20) mit reellem t
- gesucht: Entscheidung mit Begründung, ob es ein t gibt, für das die Gerade PQ_t parallel zur xy-Ebene verläuft
- verfahren: die Gerade ist genau dann parallel zur xy-Ebene, wenn P und Q_t dieselbe z-Koordinate haben; die z-Koordinaten hängen nicht von t ab
- fehlerquelle: t = 0 vorschlagen, weil dann die y-Koordinaten übereinstimmen

### 2020MerhoehtAAGLAA212 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 5 · format Rechnung · antwort Text
- gegeben: Kulisse 7 m breit, linke Wand in der xz-Ebene, rechte Wand parallel dazu (y = 7), Höhe 3, Tiefe 4; Lampe L(4; 0; 5), Spitze S(1; 6; 2)
- gesucht: rechnerische Untersuchung, ob der Schatten der Spitze auf der rechten Wand liegt
- verfahren: Gerade LS mit y = 7 schneiden, Koordinaten gegen die Wandmaße prüfen
- fehlerquelle: nur den Schnittpunkt berechnen, ohne die Wandmaße zu prüfen

### 2020MerhoehtAAGLAA22-b (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Pyramiden A B_t C_t D_t S_t mit A(0; 0; 0), B_t(t; 0; 0), C_t(t; t; 0), D_t(0; t; 0), S_t mit z = t/8; E: 3y + 4z = 24, enthält S_12
- gesucht: Werte von t, für die Pyramide und E gemeinsame Punkte haben
- verfahren: Spurgerade y = 8 in der Grundfläche, Lage von D_t und der übrigen Ecken zu E nach t unterscheiden
- fehlerquelle: nur die Spitze S_t prüfen (t ≥ 12) und die Grundfläche vergessen

### 2019MerhoehtAAGLAA22-b (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Aussage: Es gibt unendlich viele Ebenen, die keinen Punkt enthalten, dessen drei Koordinaten übereinstimmen
- gesucht: Begründung, dass die Aussage richtig ist
- verfahren: Punktmenge als Gerade durch den Ursprung mit Richtung (1; 1; 1) beschreiben, echt parallele Ebenen angeben
- fehlerquelle: nur eine Beispielebene nennen

### 2018MerhoehtBAGLAA2WTR3-1e (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Rechnung · antwort Text
- gegeben: Beachvolleyballfeld im Koordinatensystem (1 LE = 1 m, x1x2-Ebene ist der Sandboden): Spielfeld ABCD 8 m × 16 m, Netzoberkante zwischen E und F(−1 | 8 | 2,4) in 2,4 m Höhe; Tribüne als Viereck GHIJ mit G(−4 | 0 | 0), H(−4 | 16 | 0), I(−10 | 20 | 4), J(−10 | −4 | 4) in L: 2x1 + 3x3 = −8; Ball bewegt sich von (2 | 7,5 | 3) geradlinig in Richtung (0; 4; −3)
- gesucht: rechnerische Untersuchung, ob der Ball das Netz berührt
- verfahren: Weg bis x2 = 8 (0,5), zugehörige Abnahme der Höhe 0,375, Vergleich mit 2,4
- fehlerquelle: Netzebene x1 = const annehmen

### 2019MgrundlegendBAGLAA2WTR2-1c (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: Haus als Körper ABCDIJKL: Quader ABCDEFGH und Dachprisma EFGHIJKL; A(0 | 0 | 0), G(10 | 6 | 10), H(0 | 6 | 10), K(10 | 6 | 10,5), L(0 | 6 | 13); verglaste Fassade IEHL; 1 LE = 1 m; Ebenen S: 3x − 5y = 0 und T: 3x + 5y = 0
- gesucht: für jede Ebene, ob sie durch das Innere des Körpers verläuft
- verfahren: Punkte A und G in S einsetzen; für T das Vorzeichen von 3x + 5y im Körper betrachten
- fehlerquelle: T nur an den Eckpunkten prüfen

### 2023MgrundlegendBAGLAA2WTR1-1g (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 5 · format Begründung|Zeichnen · antwort Grafik
- gegeben: Rechnung (x₁; 0; x₃) = (0; 3; 3) + μ · (1; −1; −2) liefert μ = 3 und (3|0|−3); geschlossene Wand ABFE; vollständig herabgelassenes Rollo (Unterkante HG)
- gesucht: Bedeutung des Lösungsschritts; Zeichnung von Wand und Schatten in der x₁x₃-Ebene
- verfahren: Punkt als Spurpunkt der Lichtgeraden durch H in der Wandebene erkennen; Wand als Rechteck 5 × 4 zeichnen, Schattenkante durch die Spur des Lichts von G aus, Bereich schraffieren
- fehlerquelle: Schatten des Rollos an der Unterkante HG statt an der Oberkante EF beginnen lassen; S liegt außerhalb der Wand

### 2024MgrundlegendBAGLAA2WTR1-1d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Sonnenlicht in Richtung (−0,9; −1; −0,6); Hauswand in der xz-Ebene, 2,5 m hoch (−2,5 ≤ z ≤ 0); Schritte I: (x; 0; z) = (0; 2; 0) + λ · (−0,9; −1; −0,6) liefert λ = 2 und (−1,8 | 0 | −1,2); II: −1,8 < 0 und −2,5 < −1,2 < 0
- gesucht: Schlussfolgerungen aus beiden Schritten im Sachzusammenhang
- verfahren: Schritt I als Schattenpunkt, Schritt II als Lage auf der Wand deuten
- fehlerquelle: Schritt II als Nachweis eines Punkts auf der Überdachung deuten

### 2024MgrundlegendBAGLAA2WTR2-1d (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 2 · format Kurzantwort · antwort Text
- gegeben: Lösungsschritte (1) P(6 | 0 | r) mit 0 ≤ r ≤ 5, (2) 4 · 6 − 3 · 0 + 6 · r = 30
- gesucht: passende Aufgabenstellung
- verfahren: Kante AD und Ebene W erkennen
- fehlerquelle: Kante als CF oder AB benennen

### 2022MerhoehtBAGLAA2WTR1-1e (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Quader mit Ecken A und Q(1|1|3), Seitenflächen achsenparallel; BCD_k enthält die Quaderecken P und R; Kontrolle k = 4
- gesucht: dieser Wert von k
- verfahren: P(1|0|3) in L_k einsetzen
- fehlerquelle: Q statt P einsetzen (ergibt k = 6)

### 2023MgrundlegendBAGLAA2WTR1-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Ebene L durch A, B, G mit Gleichung r · x₂ + s · x₃ = 0
- gesucht: passende Werte für r und s
- verfahren: G in die Gleichung einsetzen, ein Wert frei wählen
- fehlerquelle: r = s = 0 als Lösung

### 2023MerhoehtBAGLAA2WTR1-1b (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ebene der grauen Werbefläche in der Form a · x₁ + a · x₂ = b
- gesucht: passende Werte für a und b
- verfahren: A (oder E) einsetzen
- fehlerquelle: a = b = 0 als Lösung

### 2026MerhoehtBAGLAA2MMS2-1c (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: E: x1 + x2 + 2x3 = 12; Aussage: für jeden Punkt P(u; v; w) im Innern des Dreiecks ABC liegt auch Q(u; w; v) im Innern von ABC
- gesucht: Begründung, dass die Aussage falsch ist
- verfahren: einen inneren Punkt mit v ≠ w wählen (Ebenengleichung erfüllt, alle Koordinaten positiv), den vertauschten Punkt in die Ebenengleichung einsetzen
- fehlerquelle: einen Punkt mit v = w wählen (dann ist Q = P); vergessen zu prüfen, dass P wirklich innen liegt

### 2026MerhoehtBAGLAA2WTR2-1d (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Begründung · antwort Text
- gegeben: Pyramide wird um die Gerade CD um 360° gedreht; Spitze S durchläuft einen Kreis; L: −2x + y + 4 = 0; H = CD ∩ L
- gesucht: Begründung, dass der Kreis in L liegt und H sein Mittelpunkt ist
- verfahren: L senkrecht zur Achse und durch S, Mittelpunkt auf der Achse
- fehlerquelle: S ∈ L nicht prüfen

### 2017MgrundlegendBAGLAA2WTR2-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Punkte A(0; 0; 1), B(2; 6; 1) und C(−4; 8; 5) in einem kartesischen Koordinatensystem
- gesucht: Begründung, dass die Gerade AB parallel zur x1x2-Ebene verläuft
- verfahren: Die x3-Koordinaten von A und B stimmen überein, also hat der Richtungsvektor die x3-Komponente 0
- fehlerquelle: mit dem Normalenvektor der Ebene statt mit dem Richtungsvektor argumentieren

### 2017MerhoehtBAGLAA2WTR2-1a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Viereck ABCD mit A(0; 0; 1), B(2; 6; 1), C(−4; 8; 5) und D(−6; 2; 5) in einem kartesischen Koordinatensystem; der Schnittpunkt der Diagonalen heißt M
- gesucht: Begründung, dass die Gerade AB parallel zur x1x2-Ebene verläuft
- verfahren: Die x3-Koordinaten von A und B stimmen überein, der Richtungsvektor hat die x3-Komponente 0
- fehlerquelle: mit dem Normalenvektor einer Ebene statt mit dem Richtungsvektor argumentieren

### 2017MerhoehtBAGLAA2WTR1-1e (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea · punkte 4 · format Kurzantwort · antwort Text
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; die Dachfläche EFS liegt in L: 5x1 − x2 + 13x3 = 65; an der Spitze S ist eine gerade Stange befestigt, deren oberer Endpunkt T ist; das Sonnenlicht fällt in parallelen Geraden mit dem Richtungsvektor v; der Schatten der Stange liegt vollständig auf der Dachfläche EFS
- gesucht: Beschreibung, wie man die Länge dieses Schattens berechnen kann, wenn die Koordinaten von T und v bekannt sind
- verfahren: Die Gerade durch T mit Richtung v mit L schneiden; der Schatten reicht von S bis zu diesem Schnittpunkt, seine Länge ist der Abstand der beiden Punkte
- fehlerquelle: den Schatten mit der x1x2-Ebene statt mit der Dachebene schneiden

### 2017MerhoehtBAGLAA2CAS1-1f (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ea-mms · punkte 4 · format Kurzantwort · antwort Text
- gegeben: Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m; die Dachfläche EFS liegt in L: 5x1 − x2 + 13x3 = 65; an der Spitze S ist eine gerade Stange befestigt, deren oberer Endpunkt T ist; das Sonnenlicht fällt in parallelen Geraden mit dem Richtungsvektor v; der Schatten der Stange liegt vollständig auf der Dachfläche EFS
- gesucht: Beschreibung, wie man die Länge dieses Schattens berechnen kann, wenn die Koordinaten von T und v bekannt sind
- verfahren: Die Gerade durch T mit Richtung v mit L schneiden; der Schatten reicht von S bis zu diesem Schnittpunkt, seine Länge ist der Abstand der beiden Punkte
- fehlerquelle: den Schatten mit der x1x2-Ebene statt mit der Dachebene schneiden

### 2018MerhoehtBAGLAA2WTR3-1g (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 4 · format Rechnung · antwort Text
- gegeben: Beachvolleyballfeld im Koordinatensystem (1 LE = 1 m, x1x2-Ebene ist der Sandboden): Spielfeld ABCD 8 m × 16 m, Netzoberkante zwischen E und F(−1 | 8 | 2,4) in 2,4 m Höhe; Tribüne als Viereck GHIJ mit G(−4 | 0 | 0), H(−4 | 16 | 0), I(−10 | 20 | 4), J(−10 | −4 | 4) in L: 2x1 + 3x3 = −8; Bahn des Balls nach dem Aufschlag: X_t(3 | 12t − 1 | −5t² + 4t + 2,8), t Zeit in Sekunden; der Ball überfliegt das Netz
- gesucht: ob der Ball innerhalb des Spielfelds auf dem Boden auftrifft
- verfahren: x3 = 0 nach t lösen, Auftreffpunkt mit den Feldgrenzen vergleichen
- fehlerquelle: nur die Zeit berechnen und die Lage nicht prüfen

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2026MerhoehtBAGLAA2MMS2-1d

## 3 Maßstab (unterrichtsblatt.md, wortgleich)

### 2.2

````text
2.2 Zone „kennst du schon" – die Voraussetzungen, eine Stufe
zurück. Zweck: ins Thema hineinführen, sehen, ob der Schüler so
weit ist, an Vergessenes erinnern. Die Zone lehrt nichts Neues
und nennt keinen Begriff des Themas. Sie ist auf der Zeitachse
die Zone hinter dem Schüler, kein eigenes Blatt; bereitgestellt
wird sie trotzdem zuerst als eigenes PDF (2.7). Untertitel auf
dem Blatt: „Das kennst du schon". Hängt der Schüler hier, ist
die Lücke älter als das Thema – das zeigt das Blatt durch die
Zone selbst, ohne Kennzeichnung.
- Je Fertigkeit des Abschnitts eine Hauptnummer mit eigener
  Anweisung; Titel ist die Fertigkeit als Ich-kann-Satz mit dem
  Wort, das die Klasse kennt („Ich kann die Nullstelle einer
  Geraden berechnen", nicht „wo eine Gerade die x-Achse
  schneidet"). Die Nummern der Zone sind die ersten Nummern des
  Blatts (1, 2, 3 …), keine eigene Zählung (Z1) und kein
  Neubeginn im Lernblatt; die Nummer ist die Adresse.
- Breite nach Bestellung (1.1): mit Wiederholung alle
  Fertigkeiten, die das Lernblatt braucht, dazu die Zweige des
  Themas, die die Zeitmarke vor die Eingabeklasse legt, als je
  eine Fertigkeit mit dem Grundfall des Zweigs; „wiederholung
  kurz" je Fertigkeit eine leichte und eine Fallstrick-
  Teilaufgabe; „nur das neue" keine Zone.
- Reihenfolge nach erster Verwendung im Lernblatt: die Angabe
  „– Einheit n" der Fertigkeitszeile, kleinste Einheit zuerst;
  bei gleicher Einheit die Lehrplanfolge der Voraussetzungs-
  themen; ohne Angabe die Reihenfolge des Eintrags. Innerhalb
  der Hauptnummer leicht → Fallstrick.
- Je Fertigkeit: zwei sehr leichte Teilaufgaben (im Kopf lösbar),
  eine mittlere (negative Zahl, Dezimalzahl, Bruch, Einheit) und
  je eine für jeden Fallstrick der Fertigkeit, an dem das
  Lernblatt hängt. Du planst rückwärts: erst die Stellen des
  Lernblatts, die die Fertigkeit brauchen, daraus die
  Fallstricke. Eine Fertigkeit, die das Lernblatt nirgends
  braucht, entfällt – auch eine, die nur ein abgewählter Zweig
  gebraucht hätte. Dazu einmal je Zone eine Fehler-finden-
  Aufgabe zum häufigsten Fallstrick, unmittelbar darauf als
  eigene Hauptnummer eine gleichartige zum selbst Rechnen – das
  Paar gibt es nur in der Zone (2.3 c).
- Schreibform aus dem Eintrag: Nennt die Fertigkeitszeile eine
  Form (Tabelle, Dreisatz, Streifen), setzt du sie; ein Dreisatz
  steht im zweispaltigen Schema mit den Operationen am Pfeil, nie
  als Zeile mit Doppelpunkt (3.2). Die Zahlen eines Dreisatzes
  der Zone sind so gewählt, dass beide Schritte im Kopf gehen:
  glatter Teiler, Produkt ohne Übertrag (4 Hefte 6 €; nicht 3 m
  7,50 €). Schriftliche Multiplikation ist keine Fertigkeit der
  Zone, sondern ein eigenes Thema.
- Kein Kasten, keine Stufenmarkierung, keine Prüfungshöhe: die
  Zone hat keine Decke.
- Lösungen in der Lösungsdatei (3.4), dazu die Zeile, welche
  Hauptnummer welchen Zweig trägt („1–2 → Einheit 1 und 2 ·
  3 → Einheit 3").
Beim Fokus trägt die Zone nur die Fertigkeiten, die der Typ
braucht, je zwei Teilaufgaben, als erste Seite des Fokus.
````

### 2.3 c

````text
c) Pflichtelemente je Zweig, aus den Typen des Zweigs: Fehler
   finden – Muster aus „Typische Fehler", eigene Zahlen, in der
   Schreibform des Verfahrens (bei Umformungen senkrecht mit
   `\rechnung`), Fehler benennen und korrigieren; Begründen
   oder Entscheiden ohne Rechnung; Darstellungswechsel in beide
   Richtungen, soweit die Typen es tragen; eine Anwendung, deren
   Mathematik vom Kontext getragen wird (realistische Größen, im
   Kontext sinnvolle Frage). Typen des Zweigs, die in keiner
   Kette stehen (Ordnen, Ergänzen, Aussagen prüfen, Umkehrung),
   bekommen eine eigene Hauptnummer. Gemischte Aufgaben, deren
   Punkt die Zuordnung ist („erst zuordnen, dann rechnen"),
   verraten das Verfahren nicht.

   Eine Hauptnummer, eine Fertigkeit, eine Antwortform: Nach
   „Ich finde den Fehler" folgt in derselben Nummer keine
   Rechenaufgabe; Ankreuzen und Begründen stehen nicht in
   derselben Nummer; wechselt die Anweisung so, dass eine andere
   Fertigkeit gefragt ist, beginnt eine neue Hauptnummer. Die
   Zone ist die Ausnahme mit ihrem Paar aus Fehler finden und
   gleichartiger Rechenaufgabe (2.2), und dort sind es zwei
   Nummern.
````

### 2.4 b–c

````text
b) Die Kette. Maßstab ist das strukturelle Merkmal, nicht die
   Stückzahl: Ein Merkmal ist ein Fall, der eine andere
   Entscheidung oder einen anderen Schritt verlangt – anderer
   gegebener Wert, andere Einheit, Dezimalzahl oder Bruch statt
   ganzer Zahl, negatives Vorzeichen, Sonderfall, typischer
   Fallstrick, Umkehrung des Verfahrens. Die Sprossen kommen aus
   dem Eintrag; fehlt zwischen zwei Sprossen ein Schritt, den die
   Prüfungshöhe verlangt, schließt du ihn mit einer Zwischen-
   sprosse und sagst es im Ausgabeblock. Zwei Teilaufgaben, die
   sich nur in den Zahlen unterscheiden, sind dieselbe Sprosse
   und kommen nur beim Grundfall vor. Aufwandsmerkmale (Rundung,
   krumme Zahlen) kommen nach allen Strukturmerkmalen, nie
   zwischen die glatten Fälle. Ein Schüler, der das Thema gerade
   beginnt, schafft die ersten sechs Teilaufgaben jeder
   Verfahrens-Hauptnummer, ohne die Sprossen ab der Mitte zu
   können. Ablesetypen zählen als Verfahrenstypen, die Grafik ist
   nur der Träger: mehrere Objekte je Grafik, höchstens zwei
   Grafiken je Hauptnummer. Aufwandsintensive Typen (Wertetabelle,
   Zeichnen, Konstruktion): mindestens drei Teilaufgaben, die
   erste sehr leicht. Konzept- und Kontexttypen (Begründen,
   Entscheiden, Fehler finden, Textaufgaben mit einer Situation):
   eine bis drei Teilaufgaben, gestuft wie in einer Prüfung –
   Vorbereitungsschritt, Rechnung, Deutung; bei Begründen erst der
   klare Fall, dann der subtile. Bei Entscheidungstypen mit
   Ja/Nein-Antwort liegen richtig und falsch etwa halbe-halbe in
   gemischter Reihenfolge.

c) Prüfungshöhe. Jede Verfahrens-Hauptnummer endet mit genau einer
   Teilaufgabe in Form und Anspruch der zentralen Prüfung nach 1.5
   (P10, Abitur Teil A oder B, FHR). Nennt der Eintrag für die
   Einheit ein Original, ist das die Teilaufgabe – verfremdet, mit
   Jahr (3.6); sie darf eingeführte Merkmale kombinieren, führt
   aber kein neues ein. Zerfällt die Einheit in mehrere Haupt-
   nummern, trägt die letzte das Original, die anderen enden auf
   ihrer höchsten Sprosse. Prüfungsniveau wird in einer Stunde
   nicht erreicht; die Aufgabe ist Zielmarke und bleibt stehen.
   Trägt der Zweig „keine P10-Aufgabe", ist die Decke die
   Prüfungsaufgabe, in der er gebraucht wird, sonst die
   Lehrwerk-Konvention (1.5).
````

### 3.6

````text
3.6 Zahlen, Verfremdung, Formulierung. Zahlenwerte so gewählt,
dass Ergebnisse endlich sind und leichte Aufgaben im Kopf
rechenbar; periodische Dezimalbrüche tragen einen Hinweis. Keine
Aufgabe erscheint doppelt. Keine ganze Gleichung, kein Term,
kein Zahlenpaar und keine Funktion aus Kasten, Beispiel oder
Original des Eintrags in einer Teilaufgabe (2.1). Verfremdetes
Original: gleiches Verfahren, gleiche Falle, gleiche Form
(Ankreuzen, Lückensatz, Rechnung mit Rundung), andere Zahlen,
anderer Kontext; am Ende des Aufgabentexts in Klammern Prüfung,
Jahr und Papier, wie der Eintrag es nennt: „(P10 2018 FOR)",
„(P10 2025 GYM)", „(Abitur 2022 GK)", „(FHR 2024)".
Formulierungen eindeutig. Buchstaben und Symbole, die im Aufgaben-
text nicht erklärt sind, werden nicht verwendet, auch nicht T für
Term oder L für Lösungsmenge. Ein Buchstabe steht auf einem Blatt
für genau eine Sache: Seitenlabels verschiedener Figuren und
Variablen in Textaufgaben überschneiden sich nicht.
````

# Mappe: orthogonalitaet

Eintrag: hz-0801/mathe-nachhilfe, katalog/orthogonalitaet.md
Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa (2026-09-26T14:47:30Z, „katalog: Sek-II-Einträge auf den CAS-Nachtrag“; ermittelt über GitHub-API)
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:10 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.
Kürzung: Katalogzeilen über 600 Zeichen enden nach 200 Zeichen mit „… (gekürzt, <n> Zeichen)“, außer in Merkkasten, Für schwache Schüler, Typen je Lerneinheit, Typische Fehler, Voraussetzungen, Prüfungsform, Zielmarke und Zeilen mit „[RLP]“ oder „LISUM“ (auch außerhalb dieser Abschnitte).

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Orthogonalität
  3
  4  ### Verortung
  5  Der Nachweis und die Konstruktion senkrechter Objekte: rechte Winkel an Dreiecken nachweisen (Skalarprodukt der Schenkelvektoren am Scheitel, mit Parametern identisch null, Nichtrechtwinkligkeit an al … (gekürzt, 2761 Zeichen)
  6  [GOST] Q3, 3. Kurshalbjahr „Analytische Geometrie“ (BB S. 29–30), Grund- und Leistungskursfach: L2-Zeile „Streckenlängen und Winkelgrößen im Raum auch mithilfe des Skalarprodukts bestimmen“ mit dem In … (gekürzt, 1551 Zeichen)
  7  [FOS] Kap. 4 Wahlthema 5 „Analytische Geometrie“ (S. 29): Thema „Vektoren“ mit „Winkelberechnung und Orthogonalität“ (Zeile 1205 der Textfassung) – Wahlstoff ohne Prüfungsbeleg, kein fhr-Bestand, keine fhr-Zeile in themen.csv; der rechte Winkel der fhr-Hefte ist ebene Geometrie (→ pythagoras.md, trigonometrie.md).
  8  [LS-AA] Qualifikationsphase Kapitel VI 4 „Zueinander orthogonale Vektoren – Skalarprodukt“ (Zeilen 329–330 der Textfassung), Kapitel VII 9 „Vektorielle Beweise“ (357). Zuordnung: Einheit 1 und 2 = QP VI 4; Einheit 3 = QP VI 4 mit den Ebenenformen aus VI 5 (→ ebenen.md); Einheit 4 = QP VII 9. Suchprotokoll `_suche_quelle.py --datei ../quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`: „orthogonale Vektoren“ 1 Treffer (329), „Vektorielle Beweise“ 1 (357); Nulltreffer: Mittelsenkrechte, Lot in den Kapitelüberschriften. Stundenangaben stehen nicht im Fahrplan.
  9
 10  ### Lerneinheiten
 11  1. Rechte Winkel an Dreiecken nachweisen – das Skalarprodukt am Scheitel: die beiden Schenkelvektoren vom behaupteten Scheitel aus bilden und das Skalarprodukt null zeigen; mit Parameterkoordinaten id … (gekürzt, 690 Zeichen)
 12    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
 13  2. Rechte Winkel rückwärts – Parameter und Punkte bestimmen: die Bedingung Skalarprodukt null als Gleichung lesen – Parameterwerte für rechte Winkel (linear oder quadratisch, Lösungen gegen den Bereic … (gekürzt, 748 Zeichen)
 14    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
 15  3. Senkrecht zu Geraden und Ebenen – die Paarregeln: die Gerade senkrecht zur Ebene über die Kollinearität ihres Richtungsvektors mit dem Normalenvektor (nicht über ein Skalarprodukt null – das häufig … (gekürzt, 880 Zeichen)
 16    Marken: BE Q3 · BB Q3 · GK · Abitur GK · Abitur LK
 17  4. Lot und Extremum – Orthogonalität als Argument: die kleinste Höhe und der kleinste Abstand über die Lotbedingung (Verbindungsvektor senkrecht zum Richtungsvektor der Geraden), der maximale Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe, Streckenverhältnisse an Lotfiguren über ähnliche rechtwinklige Dreiecke – Begründungsfiguren ohne und mit Parameter. (Q3, GK-Kern; Eingangsvoraussetzung L3 „Ähnlichkeit“ für die Lotfiguren) ← Eingabe „lotbedingung“, „kleinste höhe“, „maximaler winkel gleichschenklig“, „ähnliche dreiecke lot“
 18    Marken: BE Q3 · BB Q3 · GK · keine Prüfungsaufgabe
 19  Warum vier: Die Plan-Zeile nennt die Objektpaare, die Rohdatei trennt die Richtungen – nachweisen (Einheit 1), bestimmen (Einheit 2), die Paarregeln an Geraden und Ebenen (Einheit 3, mit sechzehn Zeil … (gekürzt, 919 Zeichen)
 20
 21  ### Typen je Lerneinheit
 22  Haupttypen der Rohdatei (Zeilenzahl in Klammern), je Einheit erst Berechnungs-, dann Nachweis-, dann Deutungstypen, innerhalb absteigend nach Zeilenzahl; Nebentypen der Rohdatei sind nicht zugeordnet.
 23  Einheit 1: kein Berechnungstyp — Nachweis: Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (5) · Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen (3) · Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen (3) · Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen (1) — kein Deutungstyp. Dazu: Fehler finden (den rechten Winkel an der falschen Ecke geprüft; das Skalarprodukt nur für ein Zahlenbeispiel des Parameters gerechnet; nur eine Ecke geprüft und aus einem Wert ungleich null auf das ganze Dreieck geschlossen; einen Schenkelvektor von der falschen Ecke aus gebildet) · Begründen (warum die Schenkelvektoren vom Scheitel ausgehen müssen; warum ein identisch verschwindendes Skalarprodukt für alle Parameterwerte trägt).
 24  Einheit 2: Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln (5) · Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen (2) · Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen (2) · Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen (2) · Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln (1) · Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen (1) · Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln (1) · Geraden und Ebenen: Parameter eines Punktes aus der Orthogonalität einer Strecke zu einer Geraden bestimmen (1; Ermessen, siehe Offene Punkte) — kein Nachweistyp — kein Deutungstyp. Dazu: Fehler finden (die Vektoren vom falschen Punkt aus angesetzt; eine Lösung außerhalb des Kantenbereichs nicht ausgeschlossen; die negative Höhe nicht verworfen; nur eine von zwei Lösungen angegeben; den Streckenparameter als Teilverhältnis ausgegeben; die Länge des konstruierten Vektors nicht angepasst) · Begründen (warum die Bedingung eine Gleichung liefert; warum quadratische Bedingungen zwei Kandidaten geben, die der Bereich siebt).
 25  Einheit 3: Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen (3) · Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen (2) · Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen (1) — Nachweis: Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (6) · Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen (3) — Deutung: Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben (1). Dazu: Fehler finden (für die Gerade senkrecht zur Ebene ein Skalarprodukt null mit dem Normalenvektor erwartet statt der Kollinearität; nur einen Spannvektor geprüft; die Normalenvektoren gleichgesetzt statt orthogonal angesetzt; den Normalenvektor aus den Koeffizienten falsch zugeordnet, wenn eine Variable fehlt; eine parallele statt einer senkrechten Ebene angegeben; die Mittelsenkrechte als Ebene aufgestellt) · Begründen (warum die Gerade senkrecht zur Ebene die Richtung des Normalenvektors hat; warum zwei Skalarprodukte für den Normalenvektor der Parameterform genügen).
 26  Einheit 4: Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln (1) — Nachweis: Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen (1) · Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen (1) — kein Deutungstyp. Dazu: Fehler finden (die Fläche über den Abstand zu einem Endpunkt statt über die Höhe angesetzt; das Maximum mit dem Rechner gesucht, ohne den Weg zu erläutern; mit Koordinaten gerechnet, wo keine gegeben sind) · Begründen (warum die kleinste Verbindung das Lot ist; warum der Spitzenwinkel wächst, wenn die Höhe schrumpft).
 27  Zählung: 4 + 8 + 6 + 3 = 21 Haupttypen, 12 + 15 + 16 + 3 = 46 Zeilen – alle Haupttypen der Rohdatei, jeder genau einmal (nachgezogen 2026-09-28 um die Katalogzeilen vom 27.09.2026: Pool 2017 grundlegend Teil A; nachgezogen 2026-09-29 um die Katalogzeile des CAS-Nachtrags (Pool 2018 erhöht Teil B CAS)).
 28
 29  ### Voraussetzungen (Blatt 0)
 30  Fertigkeiten (je Zeile: was, wofür):
 31  - Skalarprodukt berechnen und „null heißt senkrecht“ anwenden – die Prüfregel aller Einheiten. Sek-II-Nachbarthema skalarprodukt-und-winkel.md (dasselbe Bündel; Klarstellung Geometrie: Fertigkeit aus dem Nachbarthema derselben Stufe). [GOST Q3 L3 „Skalarprodukt in Koordinatenform“, „Orthogonalität von Vektoren“; GOST-OHiMi 2.3]
 32  - Kollinearität prüfen (Vielfaches) – die Regel „Gerade senkrecht Ebene“ in Einheit 3. Sek-II-Nachbarthema linearkombination-und-lineare-abhaengigkeit.md. [GOST Q3 L3 „Vektoren auf Kollinearität untersuchen“]
 33  - Normalenvektor aus der Koordinatengleichung ablesen, Spannvektoren aus der Parameterform lesen – die Bauteile der Einheit 3. Sek-II-Nachbarthema ebenen.md. [GOST Q3 L3 „Normalenvektor“, „Spannvektoren“; GOST-OHiMi 2.3]
 34  - Richtungsvektoren bilden und Beträge berechnen – Schenkel und Katheten in Einheit 1 und 2. Sek-II-Nachbarthemen geraden.md, vektoren-und-rechenoperationen.md. [GOST Q3 L3 „Richtungsvektor“; GOST-OHiMi 2.3 „Betrag eines Vektors“]
 35  - Lineare und quadratische Gleichungen sowie kleine Gleichungssysteme lösen, Lösungen gegen einen Bereich sieben – die Rückrichtung in Einheit 2. Sek-I-Themen quadratische-gleichungen.md, lineare-gleichungssysteme.md. [GOST-OHiMi 2.1; GOST Eingangsvoraussetzung L1]
 36  - Ähnlichkeit rechtwinkliger Dreiecke und Seitenverhältnisse – die Lotfiguren in Einheit 4. Sek-I-Themen strahlensaetze.md, winkel-dreiecke.md. [GOST Eingangsvoraussetzung L3 „Ähnlichkeit“]
 37  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 38  - „Welches Paar ist senkrecht – und welche Prüfregel gilt?“ – zu Aufgaben ankreuzen: zwei Richtungen → Skalarprodukt null; Gerade gegen Ebene → Kollinearität mit dem Normalenvektor; Ebene gegen Ebene → Skalarprodukt der Normalenvektoren; nichts rechnen. Vor Einheit 1 und 3. [GOST Q3 L2 „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“; Rohdatei-Fehlerquelle „Skalarprodukt null erwarten statt Kollinearität“, abi 2022-bebb-lk-A1.5a]
 39  - „Wo sitzt der rechte Winkel?“ – am Dreieck den behaupteten Scheitel markieren und beide Schenkelvektoren von dort ansetzen; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei-Fehlerquelle „den rechten Winkel bei A oder B prüfen statt bei O“; iqb 2026MgrundlegendAAGLAA111-a]
 40  - „Null zeigen oder null setzen?“ – ankreuzen, ob die Orthogonalität nachzuweisen (einsetzen, ausrechnen) oder aus ihr etwas zu bestimmen ist (Gleichung lösen); nichts rechnen. Vor Einheit 1 und 2. [Rohdatei: Typen „… nachweisen“ gegen „… ermitteln“; abi 2024-bebb-gk-A1.2b]
 41  - „Für alle oder für eins?“ – bei Parametern ankreuzen, ob das Skalarprodukt identisch null sein muss (jeder Wert) oder ein Wert gesucht ist; nichts rechnen. Vor Einheit 1 und 2. [Rohdatei-Fehlerquelle „nur für ein Zahlenbeispiel rechnen“; abi 2026-bb-ea-A1.7a]
 42
 43  ### Merkkasten
 44  Einheit 1 (Rechte Winkel an Dreiecken nachweisen):
 45      Am Scheitel: der rechte Winkel sitzt an einer Ecke – beide Schenkelvektoren von dort aus bilden und das Skalarprodukt null zeigen.
 46        A(0 | 0 | 0), B(6 | 2 | 3), C(t | −3t | 0): AB ∘ AC = 6t − 6t + 0 = 0 – rechter Winkel in A für jedes t.
 47      Mit Parameter heißt für alle: das Skalarprodukt muss identisch null sein – ein Zahlenbeispiel für den Parameter beweist nichts.
 48      Nicht rechtwinklig: alle drei Ecken prüfen – erst wenn keines der drei Skalarprodukte null ist, hat das Dreieck keinen rechten Winkel.
 49      Ohne Rechnung: liegt ein Schenkel in einer Koordinatenebene und der andere auf der dazu senkrechten Achse, ist der Winkel recht – die Achsenlage ersetzt das Skalarprodukt.
 50      Auswendig (Teil A): der ganze Kasten – [GOST-OHiMi 2.3] „Skalarprodukt in Koordinatenform“, „Orthogonalität von Vektoren“ (Teil-A-Belege 2026MgrundlegendAAGLAA112-a, 2026MerhoehtAAGLAA222-a, 2026MgrundlegendAAGLAA111-a, 2019MgrundlegendAAGLAA212-a).
 51      Formelsammlung: [FS-IQB 1.3] führt das Skalarprodukt; die Prüfregel „null heißt senkrecht“ steht nicht als Satz darin – [FS] offen
 52  Quelle: eigene Formulierung nach [GOST Q3 L3] „Orthogonalität von Vektoren“ und [GOST-OHiMi 2.3]; Zahlenbeispiel aus dem Pool (2026MgrundlegendAAGLAA112-a, wörtlich; wortgleiche Dublette 2026-bb-gk-A1.5a); [LS-AA QP VI 4].
 53
 54  Einheit 2 (Rechte Winkel rückwärts):
 55      Null setzen statt null zeigen: die unbekannte Größe (Parameter, Koordinate, Punkt) ansetzen, das Skalarprodukt der Schenkelvektoren null setzen und die Gleichung lösen.
 56        O, A(5 | 0 | a), B(2 | 4 | 5), rechter Winkel bei B: BO ∘ BA = 0 liefert 35 − 5a = 0, also a = 7.
 57      Quadratisch heißt sieben: liefert die Bedingung eine quadratische Gleichung, beide Lösungen bestimmen und gegen den Bereich prüfen (Kante, positives Vorzeichen) – unpassende Lösungen ausdrücklich verwerfen.
 58      Mit zweiter Bedingung: Orthogonalität und Ebenengleichung zusammen ergeben ein Gleichungssystem; Teilverhältnisse entstehen aus dem Streckenparameter (nicht der Parameter selbst ist das Verhältnis).
 59      Konstruieren: ein senkrechter Vektor mit Zusatzlage (Koordinatenebene) wird angesetzt und zuletzt auf die verlangte Länge gebracht.
 60      Auswendig (Teil A): „Null setzen statt null zeigen“ – dieselben Anlagenzeilen wie Kasten 1, rückwärts gelesen (Teil-A-Belege 2024MgrundlegendAAGLAA213-b, 2021MgrundlegendAAGLAA112-b, 2026MgrundlegendAAGLAA221); „Quadratisch heißt sieben“ und „Konstruieren“ sind Arbeitsregeln der Prüfungshöhe.
 61      Formelsammlung: [FS-IQB 1.1] „Quadratische Gleichung“ für die Rückrichtung; sonst keine – [FS] offen
 62  Quelle: eigene Formulierung nach [GOST Q3 L3] „Orthogonalität von Vektoren“; Zahlenbeispiel aus dem Pool (2021MgrundlegendAAGLAA112-b, wörtlich); [LS-AA QP VI 4].
 63
 64  Einheit 3 (Senkrecht zu Geraden und Ebenen):
 65      Gerade senkrecht zur Ebene: ihr Richtungsvektor ist ein Vielfaches des Normalenvektors – Kollinearität prüfen, nicht ein Skalarprodukt (Skalarprodukt null mit dem Normalenvektor hieße parallel zur Ebene!).
 66        g mit Richtungsvektor (3 | 0 | −1), E: 3x₁ − x₃ = −2: der Richtungsvektor ist selbst der Normalenvektor – g steht senkrecht auf E.
 67      Normalenvektor der Parameterform: senkrecht zur Ebene heißt senkrecht zu beiden Spannvektoren – zwei Skalarprodukte, beide null; einer allein genügt nicht.
 68      Paarregeln: zwei Geraden senkrecht → Skalarprodukt der Richtungsvektoren null (achsenparallele Geraden haben Einheitsvektoren); zwei Ebenen senkrecht → Skalarprodukt der Normalenvektoren null (nicht die Vektoren gleichsetzen); ein gerades Prisma → Kantenrichtung kollinear zum Normalenvektor der Grundfläche.
 69      Bauen: die Ebene senkrecht zu zwei Ebenen hat den Richtungsvektor ihrer Schnittgeraden als Normalenvektor; die Mittelsenkrechte geht durch den Mittelpunkt mit einem Richtungsvektor senkrecht zur Strecke – Zusatzbedingungen (parallel zur Koordinatenebene) legen ihn fest.
 70      Auswendig (Teil A): „Gerade senkrecht zur Ebene“, „Normalenvektor der Parameterform“ und die „Paarregeln“ – [GOST-OHiMi 2.3] „Orthogonalität von Vektoren“ mit den Ebenenformen (Teil-A-Belege 2022MerhoehtAAGLAA211-a, 2025MgrundlegendAAGLAA221-a, 2022MgrundlegendAAGLAA211-c, 2018MerhoehtAAGLAA211-b); „Bauen“ ist Prüfungshöhe (Teil-A-Belege 2021-be-gk-A1.4c, 2022MerhoehtAAGLAA213).
 71      Formelsammlung: [FS-IQB 1.3] führt Skalarprodukt und Ebenenformen; die Paarregeln stehen nicht darin – [FS] offen
 72  Quelle: eigene Formulierung nach [GOST Q3 L2] „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“ und [GOST-OHiMi 2.3]; Zahlenbeispiel aus dem Pool (2022MerhoehtAAGLAA211-a, wörtlich; wortgleiche Dublette 2022-bebb-lk-A1.5a); [LS-AA QP VI 4–5].
 73
 74  Einheit 4 (Lot und Extremum):
 75      Die kleinste Verbindung ist das Lot: unter allen Strecken von einem Punkt zu einer Geraden ist die senkrechte die kürzeste – als Gleichung: der Verbindungsvektor zum Laufpunkt hat mit dem Richtungsvektor das Skalarprodukt null.
 76      Extremwerte übersetzen: der kleinste Flächeninhalt eines Dreiecks mit fester Basis heißt kleinste Höhe, der größte Spitzenwinkel eines gleichschenkligen Dreiecks ebenso – beides führt auf die Lotbedingung statt auf Ableitungen.
 77      Ähnlichkeit am Lot: das Lot zerlegt rechtwinklige Figuren in ähnliche Dreiecke – Streckenverhältnisse folgen aus den Seitenverhältnissen, ganz ohne Koordinaten.
 78      Auswendig (Teil A): keine – die Lot-Argumente stellen die Kataloge als Begründungsfiguren der Prüfungshöhe (Teil A erhöht und Teil B); sitzen müssen die Prüfregeln der Kästen eins und drei.
 79      Formelsammlung: keine – Lotbedingung und Ähnlichkeitsargumente stehen nicht in der Formelsammlung – [FS] offen
 80  Quelle: eigene Formulierung nach [GOST Q3 L3] „Orthogonalität von Vektoren“ und [GOST Eingangsvoraussetzung L3] „Ähnlichkeit“; ohne Zahlenbeispiel (Begründungsfiguren); [LS-AA QP VII 9].
 81
 82  ### Typische Fehler
 83  Verdichtet aus den Spalten `verfahren` und `fehlerquelle` der 43 Zeilen des Themas in abitur/abi-katalog.csv und abitur/iqb-katalog.csv (Zuordnung über profil, leitidee und thema aus themen.csv, wie rohdatei-bau.py); Beleg ist die Original-id. [FD] nicht verwendet: das Quellenregister führt keine Didaktik der Analytischen Geometrie, die Muster sind allein aus den Katalogzeilen belegt.
 84  - Kollinearität und Skalarprodukt verwechselt: für die Gerade senkrecht zur Ebene ein Skalarprodukt null mit dem Normalenvektor erwartet statt der Kollinearität – das Kernfehlmuster des Themas. [abi 2022-bebb-lk-A1.5a, 2026-bb-ea-A1.3a; iqb 2022MerhoehtAAGLAA211-a, 2026MerhoehtAAGLAA211-a, 2020MgrundlegendAAGLAA211-a]
 85  - Falscher Scheitel oder falsche Vektoren: den rechten Winkel an der falschen Ecke geprüft oder vermutet; die Schenkelvektoren vom falschen Punkt aus angesetzt; einen Vektor falsch gebildet (Vorzeichen). [abi 2024-bebb-gk-A1.2b; iqb 2026MgrundlegendAAGLAA111-a, 2024MgrundlegendAAGLAA213-b, 2021MgrundlegendAAGLAA112-b, 2018MgrundlegendAAGLAA22-a, 2024MgrundlegendBAGLAA2WTR2-1f, 2024MerhoehtBAGLAA1WTR-2a, 2026MerhoehtBAGLAA1WTR-1b]
 86  - Am Beispiel statt für alle: das Skalarprodukt mit Parameter nur für einen Zahlenwert geprüft; mit Koordinaten gerechnet, wo koordinatenfrei zu begründen war; nur eine Ecke geprüft und aufs ganze Dreieck geschlossen; ein Quadrat einer Wurzel falsch ausgewertet. [abi 2026-bb-gk-A1.5a, 2026-bb-ea-A1.7a, 2018-bb-ea-B3.1b; iqb 2026MgrundlegendAAGLAA112-a, 2026MerhoehtAAGLAA222-a, 2022MerhoehtAAGLAA221-a, 2019MgrundlegendAAGLAA212-a]
 87  - Lösungen nicht gesiebt oder unvollständig: eine Lösung außerhalb des Kantenbereichs nicht ausgeschlossen; die negative Quaderhöhe nicht verworfen; nur eine von zwei Achsenlösungen angegeben; das Verhältnis als Parameterwert statt als Verhältnis der Abschnitte angegeben; die Vektorlänge der Konstruktion nicht angepasst. [abi 2023-bebb-lk-B3f; iqb 2023MerhoehtBAGLAA2WTR2-1f, 2026MerhoehtBAGLAA1MMS-1b, 2021MerhoehtAAGLAA112-b, 2021MerhoehtAAGLAA121-b, 2023MerhoehtAAGLAA221]
 88  - Paarregeln verfehlt: die Normalenvektoren gleichgesetzt statt orthogonal angesetzt (Parallelität geprüft); nur einen Spannvektor geprüft; den Normalenvektor bei fehlender Variable falsch zugeordnet; den Richtungsvektor der zweiten Geraden aus dem Schnittpunkt statt aus der Achsenrichtung abgelesen; eine parallele statt der senkrechten Ebene angegeben; die Mittelsenkrechte als Ebene aufgestellt; den Schnittpunkt aufwendig berechnet statt den gemeinsamen Stützpunkt zu sehen. [abi 2022-bebb-gk-A1.4c, 2025-bebb-gk-A1.8a, 2025-bebb-gk-A1.2b, 2021-be-gk-A1.4c; iqb 2022MgrundlegendAAGLAA211-c, 2025MgrundlegendAAGLAA221-a, 2018MerhoehtAAGLAA211-b, 2025MgrundlegendAAGLAA211-b, 2022MerhoehtAAGLAA213, 2018MerhoehtAAGLAA212-a]
 89  - Anhang verfehlt: beim Oberflächenanhang Seitenflächen vergessen oder eine Kantenlänge geraten; die Konstante der Ebenengleichung mit dem falschen Punkt bestimmt; die Ebenenbedingung als Gerade missdeutet oder eine Konstante im Skalarprodukt vergessen. [abi 2021-be-gk-B3a, 2022-bebb-gk-B3c, 2026-bb-gk-A1.8a; iqb 2021MgrundlegendBAGLAA2WTR1-1a, 2026MgrundlegendAAGLAA221]
 90  - Lot-Argument verfehlt: die Fläche über den Abstand zu einem Streckenende statt über die Höhe angesetzt; das Maximum mit dem Rechner gesucht, ohne den Weg zu erläutern. [iqb 2020MgrundlegendBAGLAA2WTR-2, 2025MerhoehtBAGLAA2MMS-1e]
 91
 92  ### Für schwache Schüler
 93  Mindeststoff (GK-Kern Q3 / Niveaustufe H / RLP FOS) [GOST, GOST-OHiMi, FOS]: GK-Kern Q3 Brandenburg und Berlin, Grund- und Leistungskursfach ohne LK-Zusatz: Einheit 1 und 2 „Orthogonalität von Vektoren“ (vorwärts und rückwärts); Einheit 3 „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“; Einheit 4 als Begründungsanwendung derselben Zeilen. Ohne Hilfsmittel (Anlage OHiMi 2.3, Prüfungsteil A): Skalarprodukt und Orthogonalität – die Prüfregeln der Kästen eins bis drei; die Lot-Argumente und die Anhänge (Oberfläche, Volumen) sind Teil-B-Arbeit. LK-Zusatz: keiner. Vorrat, weil der Plan keine Grenze zieht (Ermessen nach dem Niveau der Rohdatei): die Konstruktionen (Kathetenpunkt, Mittelsenkrechte, Ebene senkrecht zu zwei Ebenen), die koordinatenfreien Begründungen und die Lot-Extremal-Argumente der Einheit 4. Niveaustufe H der E-Phase [RLP]: der rechte Winkel als Figureigenschaft ist Sek-I-Bestand (winkel-dreiecke.md, pythagoras.md) – Blatt-0-Stoff; die Vektorprüfungen sind Q3-Stoff. RLP FOS (fhr): Wahlstoff ohne Prüfungsbeleg – kein Bestand, keine Zeile. COSH [COSH, nachrangig, aus dem Gedächtnis, nicht am Text geprüft]: der Mindestanforderungskatalog führt nach Erinnerung Orthogonalität über das Skalarprodukt – wenn das zutrifft, deckt es sich mit dem GK-Kern, kein zusätzlicher Posten.
 94  Grundvorstellung (Blatt 0) [GOST Q3 L2, MO]: Senkrecht zu einer Ebene heißt senkrecht zu allen ihren Richtungen – deshalb prüft man gegen die Ebene anders als gegen eine einzelne Linie. „Hier ist eine Tischplatte als Ebene und ein Stab, kein Term. Stelle den Stab senkrecht auf die Platte: auf wie vielen Linien der Platte steht er jetzt senkrecht – auf einer, auf zweien, auf allen? Kippe ihn ein wenig: findest du immer noch eine Linie der Platte, auf der er senkrecht steht? Warum reicht ‚senkrecht zu einer Linie‘ also nicht für ‚senkrecht zur Platte‘ – und zu wie vielen verschiedenen Richtungen musst du mindestens prüfen?“ Wer dem gekippten Stab die Senkrechte abspricht, weil er „schief aussieht“, oder wer sie ihm zuspricht, weil eine Linie passt, braucht das vor jeder Prüfregel: Gegen eine Richtung genügt ein Skalarprodukt, gegen eine Ebene braucht es zwei – oder gleich die Richtung des Normalenvektors. Verständnis, nicht Verfahren; die Vorstellung ist amtlich (Q3-Kern „Orthogonalität von Geraden, Ebenen, Geraden und Ebenen“), liegt aber im Kurshalbjahr selbst, nicht in den Eingangsvoraussetzungen (Klarstellung Geometrie); die Aufgabenform ist Ermessen. [GOST Q3 L2; MO-Logik: Vorstellung vor Verfahren; Rohdatei-Fehlerquelle „nur einen Spannvektor prüfen“, abi 2025-bebb-gk-A1.8a; BASICS nur als Strukturvorbild Diagnose → Förderung → Nachtest, keine Inhalte]
 95  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, Rohdatei; Sprossenfolge Ermessen, wo Lehrwerk und Rohdatei keine Reihenfolge vorgeben]:
 96  - Rechte Winkel nachweisen (Einheit 1): „Wo sitzt der rechte Winkel?“ ankreuzen (Vorstufe) → die Schenkelvektoren vom Scheitel bilden und das Skalarprodukt null zeigen (Grundfall, viermal) → mit Kathetenlängen anschließen (iqb 2026MgrundlegendAAGLAA111-a, Teil A; abi 2021-be-gk-B3a und iqb 2021MgrundlegendBAGLAA2WTR1-1a mit Oberflächenanhang) → mit Parameter identisch null führen (abi 2026-bb-gk-A1.5a, 2026-bb-ea-A1.7a; iqb 2026MgrundlegendAAGLAA112-a, 2026MerhoehtAAGLAA222-a, 2018MgrundlegendAAGLAA22-a, Teil A) → ohne Rechnung aus der Achsenlage begründen (iqb 2024MerhoehtBAGLAA1WTR-2a) → Prüfungshöhe: die Nichtrechtwinkligkeit an allen drei Ecken nachweisen (abi 2018-bb-ea-B3.1b, Niveau I; iqb 2019MgrundlegendAAGLAA212-a, Teil A).
 97  - Rechte Winkel rückwärts (Einheit 2): „Null zeigen oder null setzen?“ und „Für alle oder für eins?“ ankreuzen (Vorstufe) → den Parameter für den rechten Winkel über eine lineare Gleichung bestimmen (Grundfall, viermal; iqb 2021MgrundlegendAAGLAA112-b, Teil A) → quadratische Bedingungen lösen und die Lösungen sieben (abi 2024-bebb-gk-A1.2b, iqb 2024MgrundlegendAAGLAA213-b, Teil A; iqb 2021MerhoehtAAGLAA112-b mit zwei Achsenpunkten, 2024MgrundlegendBAGLAA2WTR2-1f) → die Koordinate auf der Kante bestimmen und den Bereich prüfen (abi 2023-bebb-lk-B3f, iqb 2023MerhoehtBAGLAA2WTR2-1f) → die Quaderhöhe aus senkrechten Raumdiagonalen samt Volumen oder Oberfläche (iqb 2026MerhoehtBAGLAA1WTR-1b, 2026MerhoehtBAGLAA1MMS-1b) → den Punkt aus Orthogonalitäts- und Ebenenbedingung über das Gleichungssystem (abi 2026-bb-gk-A1.8a, iqb 2026MgrundlegendAAGLAA221, Niveau III, Teil A) → das Teilverhältnis aus dem rechten Winkel (iqb 2021MerhoehtAAGLAA121-b, Niveau III, Teil A) → Prüfungshöhe: den Eckpunkt des gleichschenklig-rechtwinkligen Dreiecks konstruieren – Orthogonalität, Koordinatenebene, Länge anpassen (iqb 2023MerhoehtAAGLAA221, Niveau III, Teil A).
 98  - Senkrecht zu Geraden und Ebenen (Einheit 3): „Welches Paar ist senkrecht – und welche Prüfregel gilt?“ ankreuzen (Vorstufe, Grundvorstellung) → die Gerade senkrecht zur Ebene über die Kollinearität mit dem Normalenvektor begründen (Grundfall, viermal; abi 2022-bebb-lk-A1.5a, 2026-bb-ea-A1.3a; iqb 2022MerhoehtAAGLAA211-a, 2026MerhoehtAAGLAA211-a, 2018MerhoehtAAGLAA211-b, Teil A) → das gerade Prisma über die Kantenrichtung (iqb 2020MgrundlegendAAGLAA211-a, Teil A) → den Normalenvektor der Parameterform über zwei Skalarprodukte nachweisen (abi 2025-bebb-gk-A1.8a, 2022-bebb-gk-B3c; iqb 2025MgrundlegendAAGLAA221-a, Teil A) → senkrechte Geradenpaare prüfen, auch mit achsenparallelen Einheitsvektoren (abi 2025-bebb-gk-A1.2b; iqb 2025MgrundlegendAAGLAA211-b, 2018MerhoehtAAGLAA212-a, Teil A) → den Parameter für senkrechte Ebenen bestimmen (abi 2022-bebb-gk-A1.4c, iqb 2022MgrundlegendAAGLAA211-c, Teil A) → Prüfungshöhe: die Ebene senkrecht zu zwei Ebenen über die Schnittgerade angeben (abi 2021-be-gk-A1.4c, Niveau II, Teil A) und die Mittelsenkrechte mit Zusatzbedingung aufstellen (iqb 2022MerhoehtAAGLAA213, Niveau II, Teil A).
 99  - Lot und Extremum (Einheit 4): „Welches Paar ist senkrecht?“ auf die Lotfigur anwenden (Vorstufe) → die Lotbedingung als kleinste Verbindung aufstellen (Grundfall, viermal) → den maximalen Spitzenwinkel über die minimale Höhe und die Lotbedingung ermitteln und den Weg erläutern (iqb 2025MerhoehtBAGLAA2MMS-1e, Niveau III, MMS) → Prüfungshöhe: das Streckenverhältnis am Lot im Quadrat über ähnliche rechtwinklige Dreiecke koordinatenfrei begründen (iqb 2022MerhoehtAAGLAA221-a, Niveau III, Teil A); die Flächengleichung des flächenkleinsten gleichschenkligen Dreiecks steht als Begründungsaufgabe in Teil B (siehe Zielmarke).
100
101  ### Prüfungsform (fhr / abi / iqb)
102  Geltung [konzept.md § 4 Entscheidung 35]: Der IQB-Pool ist für das Profil abi voll maßgeblich – Brandenburg entnimmt seit 2017 Poolaufgaben, seit der KMK-Ländervereinbarung 2020 unverändert, und der Pool wirkt normierend auf Landesaufgaben und Oberstufenklausuren; die Auswahl-Einschränkung steht allein in den Geltungsdateien abi-*-geltung.md, die das Thema für alle vier Zielprüfungen mit „ja“ führen. Für fhr ist der Pool keine Vorgabe; das Thema ist dort Wahlstoff ohne Prüfungsbeleg, themen.csv führt keine fhr-Zeile. Die Rohdatei zählt 46 Zeilen mit 21 Haupttypen (abi 14 Zeilen, 11 Typen; iqb 32 Zeilen, 20 Typen), Jahre 2017–2026. Der Eintrag setzt keine Decke; Häufigkeit ist Auskunft, ein einziges Vorkommen ein vollwertiger Typ. Typnamen wörtlich aus abitur/abitur-typen.csv (gemeinsame Liste abi/iqb; das Thema führt die Gegenstandsklassen „Dreieck“ und „Geraden und Ebenen“ als Präfix vor dem Doppelpunkt). Pool-Sachgebiet: Alternative A2 „Analytische Geometrie“ der Aufgabengruppe AG/LA [IQB-STR 1], die abstrakten Aufgaben in der Gruppe AG/LA 1.
103  fhr: kein Bestand, keine Zeile – das Wahlthema 5 des RLP FOS 2019 nennt „Winkelberechnung und Orthogonalität“, die zentralen FHR-Prüfungen stellen es nicht; der fhr-Katalog führt kein Thema der Analytischen Geometrie.
104  abi (14 Zeilen, 11 Typen; Landeshefte bb-ea, be-gk, bebb-gk, bebb-lk, bb-gk 2018–2026) [abi-Katalog]: Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (2, E1) · Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen (2, E3) · Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (2, E3) · je 1: Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen (E2) · Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen (E1) · Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln (E2) · Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen (E1) · Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben (E3) · Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen (E3) · Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen (E3) · Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen (E2). Muster: Das Thema ist neben den Lagebeziehungen der zweite Teil-A-Klassiker – 10 der 14 Zeilen stehen in Teil A (ein bis fünf Punkte): die Parameterdreiecke (2026-bb-gk-A1.5a, 2026-bb-ea-A1.7a), die Rückrichtungen (2024-bebb-gk-A1.2b, 2026-bb-gk-A1.8a), die Kollinearitätsregel (2022-bebb-lk-A1.5a, 2026-bb-ea-A1.3a), die Spannvektor-Nachweise (2025-bebb-gk-A1.8a), die Geraden- und Ebenenpaare (2025-bebb-gk-A1.2b, 2022-bebb-gk-A1.4c) und die Ebene senkrecht zu zwei Ebenen (2021-be-gk-A1.4c); Teil B trägt die Nachweise am Körper mit Anhängen (Holzkörper mit Oberfläche 2021-be-gk-B3a, Kirchturmdach 2022-bebb-gk-B3c, Museum 2018-bb-ea-B3.1b) und die Kantenkoordinate 2023-bebb-lk-B3f. 12 der 14 Zeilen sind wortgleiche Pooldubletten (2021-be-gk-B3a, 2022-bebb-gk-A1.4c, 2022-bebb-lk-A1.5a, 2023-bebb-lk-B3f, 2024-bebb-gk-A1.2b, 2025-bebb-gk-A1.2b, 2025-bebb-gk-A1.8a, 2026-bb-gk-A1.5a, 2026-bb-gk-A1.8a, 2026-bb-ea-A1.3a, 2026-bb-ea-A1.7a; seit dem Abgleichlauf 27 auch die Museumszeile 2018-bb-ea-B3.1b als Dublette der CAS-Fassung des Pools 2018 erhöht, Niveau nach dem amtlichen Bereich I statt II) – die höchste Dublettenquote des Bündels; Landeszusätze sind die Kirchturmzeile und die Ebene senkrecht zu zwei Ebenen. Niveau I 5, II 8, III 1 (2026-bb-gk-A1.8a).
105  iqb (32 Zeilen, 20 Typen; Pool 2017–2026, grundlegend 16 und erhöht 16 Zeilen, Teil A 23 und Teil B 9 Zeilen, davon 1 CAS und 2 MMS) [iqb-Katalog]: Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln (4, E2) · Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (4, E3) · Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (3, E1) · Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen (2, E1) · Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen (2, E1) · Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen (2, E2) · Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen (2, E3) · je 1: Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln (E2) · Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen (E4) · Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen (E2) · Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln (E4) · Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen (E2) · Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen (E1) · Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen (E4) · Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln (E2) · Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen (E3) · Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen (E3) · Geraden und Ebenen: Parameter eines Punktes aus der Orthogonalität einer Strecke zu einer Geraden bestimmen (E2) · Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen (E3) · Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen (E2). Muster: Teil A trägt 23 der 31 Zeilen (ein bis fünf Punkte) – das Thema ist der größte Teil-A-Posten des Sachgebiets: Parameterdreiecke und Rückrichtungen in fast jedem Jahrgang (2017MgrundlegendAAGLAA211-b, 2018MgrundlegendAAGLAA22-a, 2019MgrundlegendAAGLAA212-a, 2021MgrundlegendAAGLAA112-b, 2021MerhoehtAAGLAA112-b, 2021MerhoehtAAGLAA121-b, 2024MgrundlegendAAGLAA213-b, 2026MgrundlegendAAGLAA111-a, 2026MgrundlegendAAGLAA112-a, 2026MerhoehtAAGLAA222-a; seit dem Nachzug 2026-09-28 dazu der Parameter eines Punktes, dessen Verbindungsstrecke zu einem Geradenpunkt senkrecht auf der Geraden steht, 2017MgrundlegendAAGLAA22-a, zwei Punkte, Niveau II), die Paarregeln (2018MerhoehtAAGLAA211-b, 2018MerhoehtAAGLAA212-a, 2020MgrundlegendAAGLAA211-a, 2022MerhoehtAAGLAA211-a, 2022MgrundlegendAAGLAA211-c, 2025MgrundlegendAAGLAA211-b, 2025MgrundlegendAAGLAA221-a, 2026MerhoehtAAGLAA211-a) und die Konstruktionen auf Anforderungsbereich III (2023MerhoehtAAGLAA221, 2022MerhoehtAAGLAA221-a, 2022MerhoehtAAGLAA213, 2026MgrundlegendAAGLAA221); Teil B stellt die Nachweise am Körper (2021MgrundlegendBAGLAA2WTR1-1a, 2024MgrundlegendBAGLAA2WTR2-1f, 2023MerhoehtBAGLAA2WTR2-1f, 2024MerhoehtBAGLAA1WTR-2a; seit dem Nachzug 2026-09-29 dazu die Nichtrechtwinkligkeit der Bodenfläche am Museum in der CAS-Fassung 2018MerhoehtBAGLAA2CAS1-1b, drei Punkte, Niveau I, wortgleich im Landesheft 2018-bb-ea-B3.1b), die Quaderdiagonalen in WTR- und MMS-Fassung (2026MerhoehtBAGLAA1WTR-1b, 2026MerhoehtBAGLAA1MMS-1b) und die Lot-Argumente (2020MgrundlegendBAGLAA2WTR-2, 2025MerhoehtBAGLAA2MMS-1e). Amtlicher Anforderungsbereich in allen 32 Zeilen (höchster Bereich: I 9, II 17, III 6); Niveau I 10, II 16, III 6. Kontexte: Holzkörper, Glasdach mit Rollo, E-Scooter-Quader, Zeltkanten, Museum – überwiegend abstrakte Teil-A-Aufgaben. 12 Poolzeilen kehren wortgleich in Landesheften wieder (Dubletten der abi-Liste).
106  Zielmarke: Einheit 1 – abi: das Parameterdreieck in Teil A (2026-bb-gk-A1.5a, 2026-bb-ea-A1.7a, Niveau I bis II) und die Nichtrechtwinkligkeit am Museum (2018-bb-ea-B3.1b, Niveau I); iqb: der Nachweis mit Kathetenlängen (2026MgrundlegendAAGLAA111-a, Niveau I, Teil A) und die Achsenlage-Begründung (2024MerhoehtBAGLAA1WTR-2a, Niveau I). Einheit 2 – abi: der Punkt aus Orthogonalitäts- und Ebenenbedingung (2026-bb-gk-A1.8a, Niveau III, Teil A) und die Kantenkoordinate (2023-bebb-lk-B3f, Niveau II); iqb: die Konstruktion des Kathetenpunkts (2023MerhoehtAAGLAA221, Niveau III, Teil A) und das Teilverhältnis aus dem rechten Winkel (2021MerhoehtAAGLAA121-b, Niveau III, Teil A). Einheit 3 – abi: die Ebene senkrecht zu zwei Ebenen (2021-be-gk-A1.4c, Niveau II, Teil A) und der Spannvektor-Nachweis am Kirchturmdach (2022-bebb-gk-B3c, Niveau II); iqb: die Mittelsenkrechte mit Zusatzbedingung (2022MerhoehtAAGLAA213, Niveau II, Teil A) und das gerade Prisma (2020MgrundlegendAAGLAA211-a, Niveau II, Teil A). Einheit 4 – abi: keine (die Lot-Argumente stellt nur der Pool); iqb: die Flächengleichung des flächenkleinsten Dreiecks begründen (2020MgrundlegendBAGLAA2WTR-2, Niveau III), der maximale Spitzenwinkel (2025MerhoehtBAGLAA2MMS-1e, Niveau III) und das Ähnlichkeitsargument am Lot (2022MerhoehtAAGLAA221-a, Niveau III, Teil A).
````

## 2 Originale (46)

Kennungen aus „Prüfungsform“, „Für schwache Schüler“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2026-bb-gk-A1.5a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: Dreieck ABC mit A(0; 0; 0), B(6; 2; 3) und C(t; −3t; 0), t positiv reell
- gesucht: Nachweis, dass das Dreieck in A einen rechten Winkel hat
- verfahren: Skalarprodukt AB · AC = 6t − 6t + 0 = 0 für jedes t
- fehlerquelle: das Skalarprodukt nur für einen Zahlenwert von t prüfen

### 2026-bb-ea-A1.7a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Dreiecke AB_sC_t mit A(0; 0; 0), B_s(4s; 3s; 0) und C_t(0; 0; t), s und t positiv reell
- gesucht: Begründung, dass jedes Dreieck AB_sC_t in A rechtwinklig ist
- verfahren: die Seite AB_s liegt in der xy-Ebene, die Seite AC_t auf der z-Achse, die auf dieser Ebene senkrecht steht; rechnerisch ist (4s; 3s; 0) · (0; 0; t) = 0
- fehlerquelle: nur für ein Zahlenbeispiel von s und t rechnen

### 2024-bebb-gk-A1.2b (abi-katalog.csv)

jahr 2024 · papier 2024-bebb-gk · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ursprung O, P(2 | 0 | 23), Q(6 | t | 20) bilden ein Dreieck
- gesucht: Werte von t, für die das Dreieck in Q einen rechten Winkel hat
- verfahren: QO · QP = 0 nach t lösen
- fehlerquelle: Skalarprodukt OP · OQ (rechter Winkel bei O) ansetzen

### 2026-bb-gk-A1.8a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-gk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: A(2; −3; −1) und B(10; −5; 3); für C gilt: die z-Koordinate von C ist 6; die Geraden AB und AC verlaufen senkrecht zueinander; C liegt in der Ebene x + 2y = 0
- gesucht: Koordinaten von C
- verfahren: C(x; y; 6) ansetzen; AB · AC = 8(x − 2) − 2(y + 3) + 4 · 7 = 8x − 2y + 6 = 0 und x + 2y = 0 als Gleichungssystem lösen
- fehlerquelle: die Ebenengleichung x + 2y = 0 als Gerade in der Ebene missdeuten oder beim Skalarprodukt die Konstante 28 vergessen

### 2022-bebb-lk-A1.5a (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-lk · punkte 1 · format Begründung · antwort Text
- gegeben: g: x = (7; 3; 3) + r · (3; 0; −1); E: 3x1 − x3 = −2
- gesucht: Begründung, dass g senkrecht zu E steht
- verfahren: Richtungsvektor mit dem Normalenvektor vergleichen
- fehlerquelle: Skalarprodukt null erwarten statt Kollinearität

### 2026-bb-ea-A1.3a (abi-katalog.csv)

jahr 2026 · papier 2026-bb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: g: x = (−4; 2; −2) + t · (−2; −1; 2), t reell; E: −2x1 − x2 + 2x3 − 2 = 0; P(−4; 2; −2)
- gesucht: Begründung, dass g senkrecht zu E steht|Nachweis, dass P in E liegt
- verfahren: der Richtungsvektor (−2; −1; 2) von g ist zugleich Normalenvektor von E; P einsetzen: −2 · (−4) − 2 + 2 · (−2) − 2 = 0
- fehlerquelle: das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten

### 2025-bebb-gk-A1.8a (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 2 · format Begründung · antwort Text
- gegeben: E: x = (1; −3; 0) + r · (−3; 4; 1) + s · (3; −4; 0), r und s reell; Vektor (4; 3; 0)
- gesucht: Nachweis, dass (4; 3; 0) senkrecht zu E steht
- verfahren: Skalarprodukte mit beiden Spannvektoren bilden
- fehlerquelle: nur einen Spannvektor prüfen

### 2025-bebb-gk-A1.2b (abi-katalog.csv)

jahr 2025 · papier 2025-bebb-gk · punkte 2 · format Rechnung · antwort Text
- gegeben: g: x = (8; 3; −3) + s · (−4; 0; 3); die Gerade h verläuft parallel zur y-Achse und schneidet g im Punkt (8; 3; −3)
- gesucht: Untersuchung, ob g und h senkrecht zueinander verlaufen
- verfahren: Richtungsvektor (0; 1; 0) von h mit dem Richtungsvektor von g skalar multiplizieren
- fehlerquelle: den Richtungsvektor von h aus dem Schnittpunkt ablesen

### 2022-bebb-gk-A1.4c (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 2 · format Rechnung · antwort Zahl
- gegeben: E: 3x − 2y = 0; F: 2x + sy + z = 4
- gesucht: s, für das F senkrecht zu E steht
- verfahren: Skalarprodukt der Normalenvektoren null
- fehlerquelle: Normalenvektoren gleichsetzen statt orthogonal

### 2021-be-gk-A1.4c (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 2 · format Kurzantwort · antwort Term
- gegeben: E: 2x + y + 4z = 6, F: −5x + 2y + 8z = 35, Schnittgerade s mit Richtungsvektor (0 | 8 | −2)
- gesucht: Gleichung einer Ebene H senkrecht zu E und F
- verfahren: Normalenvektor von H = Richtungsvektor von s, beliebiger Stützpunkt
- fehlerquelle: eine zu E parallele Ebene angeben

### 2021-be-gk-B3a (abi-katalog.csv)

jahr 2021 · papier 2021-be-gk · punkte 5 · format Rechnung · antwort Text|Zahl
- gegeben: Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD mit Spitze E senkrecht über D); B, D, E liegen in der Symmetrieebene; 1 LE = 1 cm
- gesucht: Nachweis, dass BCE rechtwinklig ist; Inhalt der Gesamtoberfläche
- verfahren: Skalarprodukt BC · CE = 0; Oberfläche aus Quadrat, zwei Dreiecken BCE/ABE (symmetrisch) und zwei Dreiecken CDE/ADE
- fehlerquelle: die Dreiecke ABE und ADE vergessen (nur drei Flächen zählen)

### 2022-bebb-gk-B3c (abi-katalog.csv)

jahr 2022 · papier 2022-bebb-gk · punkte 3 · format Rechnung · antwort Text|Term
- gegeben: Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; L durch C, G, F; N parallel zu L durch B; n = (3; 3; 2)
- gesucht: Nachweis, dass n Normalenvektor von N ist; Koordinatengleichung von N
- verfahren: Skalarprodukte mit CG und CF; 3x + 3y + 2z = d mit B
- fehlerquelle: d mit einem Punkt von L (statt B) bestimmen

### 2018-bb-ea-B3.1b (abi-katalog.csv)

jahr 2018 · papier 2018-bb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt. Die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist. Das Dreieck ABC liegt in der x-y-Ebene, das Dreieck DEF parallel dazu. Im kartesischen Koordinatensystem gilt A(−5 | 5 | 0), B(−5 | 25 | 0), D(0 | 0 | 15), E(0 | 30 | 15), F(−25 | 5 | 15) und G(−10 | 10 | 35). Eine Längeneinheit entspricht 1 m in der Realität. Die Bodenfläche der oberen Etage ist das Dreieck DEF.
- gesucht: Nachweis, dass das Dreieck DEF nicht rechtwinklig ist
- verfahren: Die sechs Verbindungsvektoren bilden und für jede der drei Ecken das Skalarprodukt der beiden anliegenden Seitenvektoren berechnen. Ist keines davon null, gibt es keinen rechten Winkel.
- fehlerquelle: nur ein Skalarprodukt prüfen und aus dem einen Wert ungleich null auf das ganze Dreieck schließen

### 2023-bebb-lk-B3f (abi-katalog.csv)

jahr 2023 · papier 2023-bebb-lk · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Q auf AD, R(0|6|2) auf BE; Dreieck FQR mit rechtem Winkel bei Q
- gesucht: x₃-Koordinate von Q
- verfahren: Q(6|3|q) ansetzen, QR · QF = 0 lösen, Lösung im Kantenbereich wählen
- fehlerquelle: Lösung 11 nicht ausschließen

### 2017MgrundlegendAAGLAA211-b (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Punkte A(−2 | 1 | −2), B(1 | 2 | −1), C(1 | 1 | 4) und für eine reelle Zahl d der Punkt D(d | 1 | 4); das Dreieck ABD ist im Punkt B rechtwinklig
- gesucht: Wert von d
- verfahren: Skalarprodukt der Schenkelvektoren in B mit d ansetzen und gleich null setzen
- fehlerquelle: die Schenkel am falschen Eckpunkt nehmen (etwa AB · AD)

### 2018MgrundlegendAAGLAA22-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: A(7 | 3 | 0), B(5 | 3 | 4), C_t(5 + 2t | 3 | 4 + t) mit t ≠ 0
- gesucht: Nachweis, dass jedes Dreieck ABC_t bei B einen rechten Winkel hat
- verfahren: Skalarprodukt der Schenkelvektoren bei B
- fehlerquelle: Vektor AC statt BC ansetzen

### 2019MgrundlegendAAGLAA212-a (iqb-katalog.csv)

jahr 2019 · papier 2019-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: gerades Prisma ABCDEF mit Grundfläche A(0 | −4 | 0), B(√20 | 0 | 0), C(0 | 4 | 0)
- gesucht: Nachweis, dass das Dreieck ABC bei B nicht rechtwinklig ist
- verfahren: Skalarprodukt der Schenkelvektoren bei B
- fehlerquelle: (√20)² = 20 falsch berechnen

### 2021MgrundlegendAAGLAA112-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: O Ursprung, A(5; 0; a), B(2; 4; 5)
- gesucht: Wert von a, für den das Dreieck OAB bei B rechtwinklig ist
- verfahren: Skalarprodukt BO · BA null setzen
- fehlerquelle: Skalarprodukt OA · OB ansetzen (rechter Winkel bei O)

### 2021MerhoehtAAGLAA112-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: A(2; −3; 1), B(2; 3; 1); C auf der y-Achse; Gerade AC senkrecht zu Gerade BC
- gesucht: Koordinaten aller möglichen Punkte C
- verfahren: C(0; c; 0), Skalarprodukt CA · CB = 0 lösen
- fehlerquelle: nur c = 2 angeben

### 2021MerhoehtAAGLAA121-b (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: A, B, C wie in a; T auf der Strecke AC; Dreieck ABT bei B rechtwinklig
- gesucht: Verhältnis |AT| : |CT|
- verfahren: T als λ · AC ansetzen, Skalarprodukt AB · TB = 0 lösen, Verhältnis λ : (1 − λ)
- fehlerquelle: Verhältnis als 13 : 17 angeben (λ statt λ : (1 − λ))

### 2024MgrundlegendAAGLAA213-b (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Ursprung O, P(2; 0; 23), Q_t(6; t; 20) bilden ein Dreieck
- gesucht: Werte von t, für die das Dreieck in Q_t einen rechten Winkel hat
- verfahren: Skalarprodukt der Vektoren Q_tO und Q_tP gleich null setzen
- fehlerquelle: die Vektoren OP und OQ_t verwenden (rechter Winkel in O)

### 2026MgrundlegendAAGLAA111-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 3 · format Begründung · antwort Text
- gegeben: gleichschenkliges Dreieck OAB mit O(0; 0; 0), A(8; 6; 0) und B(0; 0; 10)
- gesucht: Nachweis, dass OAB in O rechtwinklig ist und die Katheten die Länge 10 haben
- verfahren: Skalarprodukt OA · OB = 0 zeigen; |OB| = 10 berechnen und aus der Gleichschenkligkeit im rechten Winkel |OA| = |OB| folgern oder |OA| = √(64 + 36) = 10 direkt rechnen
- fehlerquelle: den rechten Winkel bei A oder B prüfen statt bei O

### 2026MgrundlegendAAGLAA112-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Dreieck ABC mit A(0; 0; 0), B(6; 2; 3) und C(t; −3t; 0), t positiv reell
- gesucht: Nachweis, dass das Dreieck in A einen rechten Winkel hat
- verfahren: Skalarprodukt AB · AC = 6t − 6t + 0 = 0 für jedes t
- fehlerquelle: das Skalarprodukt nur für einen Zahlenwert von t prüfen

### 2026MerhoehtAAGLAA222-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: Dreiecke AB_sC_t mit A(0; 0; 0), B_s(4s; 3s; 0) und C_t(0; 0; t), s und t positiv reell
- gesucht: Begründung, dass jedes Dreieck AB_sC_t in A rechtwinklig ist
- verfahren: die Seite AB_s liegt in der xy-Ebene, die Seite AC_t auf der z-Achse, die auf dieser Ebene senkrecht steht; rechnerisch ist (4s; 3s; 0) · (0; 0; t) = 0
- fehlerquelle: nur für ein Zahlenbeispiel von s und t rechnen

### 2017MgrundlegendAAGLAA22-a (iqb-katalog.csv)

jahr 2017 · papier 2017-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Punkt P(−3 | 2 | 1), Gerade g: x = OP + r · (1; 3; 0), r ∈ IR, und für eine reelle Zahl a der Punkt Q(0 | a | 0); die Strecke PQ steht senkrecht zu g
- gesucht: Wert von a
- verfahren: Skalarprodukt von PQ mit dem Richtungsvektor von g gleich null setzen
- fehlerquelle: den Ortsvektor von Q statt des Verbindungsvektors PQ mit dem Richtungsvektor multiplizieren

### 2018MerhoehtAAGLAA211-b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: E: x2 − 3x3 = −19; P(1 | 2 | 2), Q(1 | −1 | 11)
- gesucht: Nachweis, dass die Gerade PQ senkrecht zu E steht
- verfahren: PQ als Vielfaches des Normalenvektors zeigen
- fehlerquelle: Normalenvektor (1; −3; 0) aus den Koeffizienten falsch zuordnen (x1 fehlt)

### 2018MerhoehtAAGLAA212-a (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea · punkte 2 · format Kurzantwort|Begründung · antwort Text
- gegeben: g: x = (3; −3; 3) + r · (3; 0; −1), h: x = (3; −3; 3) + s · (1; 0; 3)
- gesucht: Schnittpunkt von g und h und Nachweis der Orthogonalität
- verfahren: Stützpunkt ablesen, Skalarprodukt
- fehlerquelle: Schnittpunkt über ein Gleichungssystem berechnen statt den gemeinsamen Stützpunkt zu sehen

### 2020MgrundlegendAAGLAA211-a (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: Prisma ABCDEF mit A(3; 3; 6), B(−1; 5; 2), C(7; 4; 1), E(2; 23; 8); A, B, C in L: x + 6y + 2z = 33
- gesucht: Begründung, dass das Prisma gerade ist
- verfahren: BE mit dem Normalenvektor von L vergleichen
- fehlerquelle: Skalarprodukt BE · n = 0 erwarten

### 2022MerhoehtAAGLAA211-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 1 · format Begründung · antwort Text
- gegeben: g: x = (7; 3; 3) + r · (3; 0; −1); E: 3x1 − x3 = −2
- gesucht: Begründung, dass g senkrecht zu E steht
- verfahren: Richtungsvektor mit dem Normalenvektor vergleichen
- fehlerquelle: Skalarprodukt null erwarten statt Kollinearität

### 2022MgrundlegendAAGLAA211-c (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ga · punkte 2 · format Rechnung · antwort Zahl
- gegeben: E: 3 · x − 2 · y = 0; F: 2 · x + s · y + z = 4
- gesucht: Wert von s, für den F senkrecht zu E steht
- verfahren: Skalarprodukt der Normalenvektoren null setzen
- fehlerquelle: Normalenvektoren als kollinear ansetzen (Parallelität statt Orthogonalität)

### 2025MgrundlegendAAGLAA211-b (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 2 · format Rechnung · antwort Text
- gegeben: g: x = (8; 3; −3) + s · (−4; 0; 3); die Gerade h verläuft parallel zur y-Achse und schneidet g im Punkt (8; 3; −3)
- gesucht: Untersuchung, ob g und h senkrecht zueinander verlaufen
- verfahren: Richtungsvektor (0; 1; 0) von h mit dem Richtungsvektor von g skalar multiplizieren
- fehlerquelle: den Richtungsvektor von h aus dem Schnittpunkt ablesen

### 2025MgrundlegendAAGLAA221-a (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ga · punkte 2 · format Begründung · antwort Text
- gegeben: E: x = (1; −3; 0) + r · (−3; 4; 1) + s · (3; −4; 0), r und s reell; Vektor (4; 3; 0)
- gesucht: Nachweis, dass (4; 3; 0) senkrecht zu E steht
- verfahren: Skalarprodukte mit beiden Spannvektoren bilden
- fehlerquelle: nur einen Spannvektor prüfen

### 2026MerhoehtAAGLAA211-a (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: g: x = (−4; 2; −2) + t · (−2; −1; 2), t reell; E: −2x1 − x2 + 2x3 − 2 = 0; P(−4; 2; −2)
- gesucht: Begründung, dass g senkrecht zu E steht|Nachweis, dass P in E liegt
- verfahren: der Richtungsvektor (−2; −1; 2) von g ist zugleich Normalenvektor von E; P einsetzen: −2 · (−4) − 2 + 2 · (−2) − 2 = 0
- fehlerquelle: das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten

### 2023MerhoehtAAGLAA221 (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Dreieck ABC mit A(0; 0; 0), B(3; 5; −4), gleichschenklig und rechtwinklig, AB Kathete, zweite Kathete in der x1x3-Ebene
- gesucht: Koordinaten eines möglichen Punktes C
- verfahren: rechter Winkel in A: Richtung (4; 0; 3) liegt in der x1x3-Ebene und ist senkrecht zu AB; auf die Länge |AB| bringen
- fehlerquelle: die Länge des Richtungsvektors nicht an |AB| anpassen

### 2022MerhoehtAAGLAA221-a (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 3 · format Begründung · antwort Text
- gegeben: Quadrat ABCD; g durch B und den Mittelpunkt M von AD mit Richtungsvektor v; F Lotfußpunkt von A auf g
- gesucht: Begründung, dass |BF| = 2 · |AF| gilt
- verfahren: Dreiecke ABM und ABF als ähnlich erkennen und Seitenverhältnisse übertragen
- fehlerquelle: mit Koordinaten rechnen wollen, obwohl keine gegeben sind

### 2022MerhoehtAAGLAA213 (iqb-katalog.csv)

jahr 2022 · papier 2022-iqb-ea · punkte 5 · format Rechnung · antwort Zahl|Term
- gegeben: A(−5; 5; −3), B(−1; 1; −1)
- gesucht: Mittelpunkt von AB; Gleichung der Mittelsenkrechten von AB, die parallel zur x1x3-Ebene verläuft
- verfahren: Mittelpunkt als Stützpunkt, Richtungsvektor (a; 0; b) senkrecht zu AB
- fehlerquelle: Mittelsenkrechte als Ebene aufstellen

### 2026MgrundlegendAAGLAA221 (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ga · punkte 5 · format Rechnung · antwort Zahl
- gegeben: A(2; −3; −1) und B(10; −5; 3); für C gilt: die z-Koordinate von C ist 6; die Geraden AB und AC verlaufen senkrecht zueinander; C liegt in der Ebene x + 2y = 0
- gesucht: Koordinaten von C
- verfahren: C(x; y; 6) ansetzen; AB · AC = 8(x − 2) − 2(y + 3) + 4 · 7 = 8x − 2y + 6 = 0 und x + 2y = 0 als Gleichungssystem lösen
- fehlerquelle: die Ebenengleichung x + 2y = 0 als Gerade in der Ebene missdeuten oder beim Skalarprodukt die Konstante 28 vergessen

### 2021MgrundlegendBAGLAA2WTR1-1a (iqb-katalog.csv)

jahr 2021 · papier 2021-iqb-ga · punkte 5 · format Rechnung · antwort Text|Zahl
- gegeben: Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD, Spitze E senkrecht über D); B, D und E liegen in der Symmetrieebene des Körpers; 1 LE = 1 cm
- gesucht: Nachweis, dass BCE rechtwinklig ist; Inhalt der Oberfläche des Körpers
- verfahren: Skalarprodukt CB · CE; Oberfläche aus Quadrat und vier Dreiecken
- fehlerquelle: Dreieck ADE oder BCE vergessen; |CE| als 10 annehmen

### 2024MgrundlegendBAGLAA2WTR2-1f (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ga · punkte 3 · format Rechnung · antwort Zahl
- gegeben: Dreieck MFS_t mit M(3 | 4 | 5), F(0 | 0 | 5), S_t(t | 0 | 0)
- gesucht: t für einen rechten Winkel in M
- verfahren: Skalarprodukt der Schenkel null setzen
- fehlerquelle: Vektoren von F statt von M aus

### 2023MerhoehtBAGLAA2WTR2-1f (iqb-katalog.csv)

jahr 2023 · papier 2023-iqb-ea · punkte 5 · format Rechnung · antwort Zahl
- gegeben: Q auf AD, R(0|6|2) auf BE; Dreieck FQR mit rechtem Winkel bei Q
- gesucht: x₃-Koordinate von Q
- verfahren: Q(6|3|q) ansetzen, QR · QF = 0 lösen, Lösung im Kantenbereich wählen
- fehlerquelle: Lösung 11 nicht ausschließen

### 2024MerhoehtBAGLAA1WTR-2a (iqb-katalog.csv)

jahr 2024 · papier 2024-iqb-ea · punkte 2 · format Begründung · antwort Text
- gegeben: A(0 | 0 | 0), B(−3 | −4 | 0), C(0 | 0 | 12); Umfang 30
- gesucht: Begründung, dass ABC rechtwinklig ist
- verfahren: Lage von AB und AC zu den Achsen
- fehlerquelle: rechten Winkel bei B vermuten

### 2018MerhoehtBAGLAA2CAS1-1b (iqb-katalog.csv)

jahr 2018 · papier 2018-iqb-ea-mms · punkte 3 · format Begründung · antwort Text
- gegeben: Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt; die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist; die Ebene, in der das Dreieck ABC liegt, beschreibt die Horizontale, das Dreieck DEF liegt parallel zu dieser Ebene; A(−5; 5; 0), B(−5; 25; 0), D(0; 0; 15), E(0; 30; 15), F(−25; 5; 15), G(−10; 10; 35); 1 LE = 1 m; die Bodenfläche der oberen Etage ist das Dreieck DEF
- gesucht: Nachweis, dass die Bodenfläche der oberen Etage nicht rechtwinklig ist
- verfahren: Für jede der drei Ecken das Skalarprodukt zweier Seitenvektoren berechnen; keines ist null, also hat das Dreieck keinen rechten Winkel
- fehlerquelle: nur ein Skalarprodukt prüfen und daraus auf das ganze Dreieck schließen

### 2026MerhoehtBAGLAA1WTR-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea · punkte 4 · format Rechnung · antwort Zahl
- gegeben: A(6 | 0 | 0), B(6 | 8 | 0), C(0 | 8 | 0), E(6 | 0 | h), h > 0; Raumdiagonalen AG und CE senkrecht
- gesucht: h und Volumen des Quaders
- verfahren: Skalarprodukt der Diagonalen null setzen, Volumen aus den Kanten
- fehlerquelle: Vorzeichen in CE

### 2026MerhoehtBAGLAA1MMS-1b (iqb-katalog.csv)

jahr 2026 · papier 2026-iqb-ea-mms · punkte 4 · format Rechnung · antwort Zahl
- gegeben: A(6; 0; 0), B(6; 8; 0), C(0; 8; 0), E(6; 0; h) mit h > 0; die Raumdiagonalen AG und CE schneiden sich senkrecht
- gesucht: h und der Inhalt der Oberfläche des Quaders
- verfahren: G(0; 8; h) ergänzen, Skalarprodukt der Diagonalenvektoren null setzen, h > 0 wählen; Oberfläche aus den drei Kantenlängen 6, 8, 10
- fehlerquelle: h = −10 nicht ausschließen; nur drei Seitenflächen addieren

### 2020MgrundlegendBAGLAA2WTR-2 (iqb-katalog.csv)

jahr 2020 · papier 2020-iqb-ga · punkte 4 · format Begründung · antwort Text
- gegeben: Gerade t: x = (−2; 3; −1) + λ · (−1; 0; 3), λ ∈ IR, die die Gerade durch R(−1 | 2 | 3) und S(−1 | 4 | 3) nicht schneidet; zu jedem λ gehört der Punkt T_λ von t, jeder Punkt T_λ hat von R und S den gleichen Abstand; unter den Dreiecken RST_λ hat eines den kleinsten Flächeninhalt; Behauptung: der zugehörige Wert von λ löst (−1 − λ; 0; −4 + 3λ) · (−1; 0; 3) = 0
- gesucht: Begründung der Gleichung
- verfahren: Flächeninhalt als 1/2 · |RS| · |MT_λ| schreiben, Minimum bei minimalem |MT_λ|, d. h. MT_λ senkrecht zu t
- fehlerquelle: die Fläche über den Abstand T_λ zu R statt über die Höhe ansetzen

### 2025MerhoehtBAGLAA2MMS-1e (iqb-katalog.csv)

jahr 2025 · papier 2025-iqb-ea-mms · punkte 6 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Punkte A(2 | 0 | 0), B(−2 | 0 | 0), C(−2 | 0 | 3), D(2 | 0 | 3), S(0 | −5 | 0), E_k(0 | k | 0), F_k(0 | k | 30 − 3k) mit 0 < k ≤ 10; zusammengesetzter Körper aus der Pyramide ABCDS und dem Körper ABCDE_kF_k; ABCD ist ein Rechteck; Innenwinkel des Dreiecks DF_kC bei F_k
- gesucht: Wert von k, für den dieser Winkel maximal ist, mit Erläuterung des Lösungswegs
- verfahren: Winkelmaximum in die minimale Höhe MF_k übersetzen, Lotbedingung MF_k · (0; 1; −3) = 0 lösen
- fehlerquelle: den Winkel als Funktion von k mit dem Rechner maximieren, ohne den Weg zu erläutern

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

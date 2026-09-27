# Gegenlese: punkte-und-strecken-im-koordinatensystem

Datum: Sun Sep 27 21:40:59 UTC 2026
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 255
Korrekturen: 2

## Punkt 1 – Lösung und pruef
- punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s4-v3: „ein Drittel ihrer Länge von vorn“ stimmt nicht. Die Deckkante mit $x_1 = 5$ bzw. $x_1 = 3$ liegt ganz vorn und läuft in $x_2$-Richtung, $P$ liegt bei $x_2 = 2$ von $6$ – Vorschlag: „ein Drittel ihrer Länge von der $x_1x_3$-Ebene aus (bei $x_2 = 2$)“.
- punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v7: korrigiert: „Für jedes $s$ ein Dreieck … Außerhalb ist das Dreieck niedriger.“ → „Für $2 \le s \le 5$ ein Dreieck (drei Ecken) … Für $1 < s < 2$ und $5 < s < 7$ ein Trapez (vier Ecken): Die Dreiecksflächen $ABP$ bzw. $CDQ$ schneiden die Spitze ab.“ Nachgerechnet: Bei $s = 1{,}5$ ist der Schnitt das Trapez $(2|0)$, $(6|0)$, $(5|1{,}5)$, $(3|1{,}5)$ in der $x_1x_3$-Sicht. Flächeninhalt $6$ und pruef bleiben unverändert – keine weitere Änderung nötig.
- punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v8: korrigiert: dieselbe Stelle, „Für jedes $s$ ein Dreieck … niedriger.“ → „Für $3 \le s \le 6$ ein Dreieck (drei Ecken) … Für $1 < s < 3$ und $6 < s < 9$ ein Trapez (vier Ecken): …“. Nachgerechnet: Bei $s = 2$ ist der Schnitt das Trapez $(0|0)$, $(6|0)$, $(4{,}5|2)$, $(1{,}5|2)$. Flächeninhalt $12$ und pruef bleiben unverändert – keine weitere Änderung nötig.

## Punkt 2 – Eindeutigkeit und Angaben
- punkte-und-strecken-im-koordinatensystem-e1-k1-s2-v1, punkte-und-strecken-im-koordinatensystem-e1-k1-s2-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s2-v3: Die vier Punkte liegen nicht in einer Ebene (Spatprodukt $4$, $6$, $-6$). „Das Viereck“ wäre also ein windschiefes Viereck, anders als im Original, wo 2019-be-gk-B3.2b dasselbe Viereck als Trapez nachweist – Vorschlag: $S$ auf seiner Kante so verschieben, dass die Punkte in einer Ebene liegen: v1 $S(2{,}5 | 0 | 4)$, v2 $S(0 | 0 | 0{,}5)$, v3 $S(2 | 0 | 4)$. Alle drei ergeben ein konvexes Viereck; Lösungsgrafik mitändern.
- punkte-und-strecken-im-koordinatensystem-e1-k1-s6-v2, punkte-und-strecken-im-koordinatensystem-e1-k1-s6-v3: Grammatikfehler im Aufgabentext: „Der Beet ist …“ bzw. „Der Bodenplatte ist …“ – Vorschlag: „Das Beet ist …“ bzw. „Die Bodenplatte ist …“.
- punkte-und-strecken-im-koordinatensystem-e3-k1-s3-v3: „für jedes $p$ gleichschenklig“ stimmt für $p = 2$ nicht. Dann ist $C(1 | 2 | 0)$ der Mittelpunkt von $AB$ und das Dreieck entartet – Vorschlag: „für jedes $p \ne 2$“ (wie in v2 mit „$p \ne 3$“).
- punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v2, punkte-und-strecken-im-koordinatensystem-e3-k1-s9-v3: „Gib einen Punkt $T$ an“ hat unendlich viele Lösungen, z. B. auch das Bild von $P$ bei einer Drehung um die Gerade $OQ$. Die loesung nennt aber nur $T = Q - P$ ohne „z. B.“, und antwort/pruef erwarten genau diesen Punkt – Vorschlag: loesung mit „Z. B.“ beginnen und die Bedingung für andere richtige Antworten nennen ($|OT| = |PQ|$, $|TQ| = |OP|$ oder $|OT| = |OP|$, $|TQ| = |PQ|$).
- punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v1, punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v2: Im Raum ist $D$ durch $|DA| = |DB| = |CA|$ nicht eindeutig bestimmt. Die Lösungen bilden einen Kreis um $M$ in der Mittelebene von $AB$ (Radius $\sqrt{8}$ bzw. $3$), die Frage „Koordinaten von $D$?“ hat also unendlich viele Antworten – Vorschlag: „Gesucht ist der Punkt $D$, für den $ADBC$ eine Raute ist“ oder „$D$ liegt in der Ebene von $A$, $B$, $C$“.
- punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v3, punkte-und-strecken-im-koordinatensystem-e3-k1-s10-v4: „Gib zwei Punkte $B$ und $C$ an“ ist offen: $B$ muss nicht der Gegenpunkt sein, und für $C$ gibt es unendlich viele Möglichkeiten. Die loesung stellt aber eine Wahl ohne „z. B.“ dar – Vorschlag: „Z. B.“ voranstellen und die Bedingungen nennen: $|MB| = |MC| = 3$ und zwei gleich lange Seiten.
- punkte-und-strecken-im-koordinatensystem-e4-k1-s9-v1, punkte-und-strecken-im-koordinatensystem-e4-k1-s9-v2: „Gib eine weitere Ecke an“ hat vier richtige Antworten, die loesung nennt nur die zwei an $P$ – Vorschlag: die Ecken an $Q$ ergänzen: v1 $(6 | -2 | 5)$, $(-2 | 4 | 5)$; v2 $(6 | 6 | 8)$, $(0 | 6 | 0)$.
- punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v3: Zwei Drehungen legen $D$ und $E$ in die $x_1x_2$-Ebene (um $+90°$ oder $-90°$). Bei der einen kommt $C^*$ unter die Ebene ($S - |\overrightarrow{SC}| \cdot (0 | 0 | 1)$), die loesung behauptet aber ohne Begründung „senkrecht über“ – Vorschlag: im Text „gekippt (der Körper bleibt über der $x_1x_2$-Ebene)“ wie in v4, oder die Wahl des Vorzeichens in der loesung begründen.

## Punkt 3 – Sprosse und Merkmal
- punkte-und-strecken-im-koordinatensystem-e1-k1-s8-v3, punkte-und-strecken-im-koordinatensystem-e1-k1-s8-v4: Das Merkmal „Projektion und Punktspiegelung kombinieren“ passt nicht. Diese Varianten haben keine Punktspiegelung, sondern entscheiden über den Höhenfußpunkt (zweites Original der Sprosse) – Vorschlag: Merkmal der ganzen Sprosse allgemeiner fassen, z. B. „Projektion in die $x_1x_2$-Ebene als Werkzeug: Ecke spiegeln oder Höhenfußpunkt beurteilen“.
- punkte-und-strecken-im-koordinatensystem-e5-k1-s2-v2, punkte-und-strecken-im-koordinatensystem-e5-k1-s2-v3: Das Merkmal „Lage selbst festlegen“ wird nicht geübt, weil der Text die Lage vorgibt („eine Bodenecke im Ursprung, zwei Bodenkanten auf den positiven Achsen“ bzw. „$A$ im Ursprung, $B$ auf der $x_1$-Achse, $D$ auf der $x_2$-Achse“). Es bleibt Ablesen wie in s1 – Vorschlag: wie v1 nur „Wähle geeignete Koordinaten“ verlangen und die loesung mit „Z. B.“ geben.

## Punkt 4 – Schreibform
- punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v5, punkte-und-strecken-im-koordinatensystem-e5-k1-s8-v6: Die Begründung benutzt Koordinatengleichungen der Seitenflächen ($3x_1 + 2x_3 = 12$ bzw. $2x_1 + x_3 = 6$). Ebenengleichungen führt dieser Eintrag nicht ein – Vorschlag: mit dem Querschnitt begründen: In der Höhe $z$ ist der Pyramidenquerschnitt das Quadrat mit der Seite $4 - \frac{2}{3}z$ bzw. $3 - \frac{1}{2}z$. Für $z \le k$ ist diese Seite $\ge k$, also enthält es den Würfelquerschnitt mit der Seite $k$.

## Punkt 5 – Ankreuzen
- punkte-und-strecken-im-koordinatensystem-zone-f7-v2: „Welches Dreieck hat zwei gleich lange Seiten?“ – der Distraktor „gleichseitig“ trifft auch zu, denn ein gleichseitiges Dreieck hat ebenfalls zwei gleich lange Seiten. Damit sind zwei Optionen richtig – Vorschlag: „genau zwei gleich lange Seiten“.

## Punkt 6 – Fehler finden
keine

## Entscheidungen
- Grammatikfehler im Aufgabentext (e1-k1-s6-v2, v3) stehen unter Punkt 2, weil kein eigener Abschnitt dafür vorgesehen ist.
- Offene Aufgaben („Gib einen Punkt an“), deren loesung eine Wahl als einzige Antwort darstellt, stehen unter Punkt 2 (Eindeutigkeit) und sind nicht korrigiert, weil die Rechnung der genannten Wahl stimmt.
- e1-k1-s4-v1, v3: Der Richtungsfehler steht in einem beschreibenden Satz der loesung und ist nicht rechnerisch, deshalb Befund statt Korrektur.
- e5-k1-s8-v7, v8: Die falsche Eckenzahl („für jedes $s$ ein Dreieck“) ist ein Rechenergebnis mit eindeutiger Korrektur, deshalb ist die loesung korrigiert (nur dieser Satz, Flächeninhalt und pruef unverändert).
- Prüfkennung im Text bei original null (e4-k1-s10-v7, v8; e5-k1-s3-v1 bis v3) ist kein Befund: stand.md führt das als bewusste Entscheidung, und e4 s10 gehört zur vorbestehenden Warnung.

Sauber: 228 Zeilen ohne Befund

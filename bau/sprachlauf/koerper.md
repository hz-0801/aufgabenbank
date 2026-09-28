# Sprachlauf koerper

Stand 2026-09-28 (Gruppe 4). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 750cb05. Nur das Feld aufgabe ist
geändert; `python3 werkzeuge/bank-pruef.py koerper`: Abweichungen: 0, Warnungen: 0

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 50 | 2 | 52 |
| e2.jsonl | 47 | 9 | 56 |
| e3.jsonl | 47 | 0 | 47 |
| e4.jsonl | 56 | 1 | 57 |
| e5.jsonl | 46 | 4 | 50 |
| zone.jsonl | 26 | 2 | 28 |
| gesamt | 272 | 18 | 290 |

Geänderte Sprossen: 101. Die Beispiele sind je Sprosse
die erste geänderte Zeile, gleichmäßig über die Sprossen verteilt.

## Entscheidungen

- „Ein Zelt hat diese Form.“ wird „… hat die Form im Bild.“, „Lässt sich dieses
  Netz …“ wird „Das Bild zeigt ein Netz. Kann man daraus …“ (Regel 5: die
  Darstellung wird im Satz genannt).
- Stichwortzeilen „Quader: Länge …, Breite … – Volumen?“ sind Sachsätze mit
  Aufforderung: „Ein Quader ist … lang, … breit und … hoch. Berechne das
  Volumen des Quaders.“
- „auf eine Stelle“ bzw. „(auf eine Stelle)“ wird überall ein eigener Satz
  „Runde auf eine Stelle nach dem Komma.“; in Originalen steht er vor der
  Prüfkennung.
- Fehler finden mit Rechnung: „<Name> soll … berechnen. Er/Sie rechnet so:
  \rechnung{…} Finde den Fehler und rechne richtig.“; bei einer Aussage
  „… und schreibe die Aussage richtig.“, bei Emmas Karton „… und gib einen
  passenden Karton an.“, bei Jonas' Würfelfläche „… und gib die richtige
  Fläche an.“
- Division: „$\sqrt{98 : 2}$“ (zone-f5-v5) steht als Bruch, ebenso der
  Dreiecksteil in Toms Rechnung e5-k4-s1-v3 ($\frac{7 \cdot 2{,}5}{2}$).
  In den Ankreuz-Termen e5-k1-s4-v2 bleibt „$5 \cdot 2 : 2$“, weil die
  Optionen wortgleich übernommen werden (die Option ist der zu prüfende Term).
- „Füllstand in Prozent?“ wird „Zu wie viel Prozent ist … gefüllt?“ (Frage
  mit Bezug, Regel 2).
- „Wievielmal so groß“ wird „Wie viel Mal so groß ist das Volumen von B wie
  das von A?“.
- Fachwörter Prisma, Grundfläche, Mantel, Oberfläche, Schrägbild, Netz,
  Radius, Durchmesser bleiben, weil die Sprossen sie üben.

## 10 Beispiele

1. `koerper-e1-k1-s0-v1` – Körper ankreuzen

   vorher: Ein Zelt hat diese Form. Kreuze an, welcher Körper es ist (P10 2017 OS). \\ \kreuz{Pyramide} \\ \kreuz{Prisma} \\ \kreuz{Quader}

   nachher: Ein Zelt hat die Form im Bild. Kreuze an, welcher Körper es ist (P10 2017 OS). \\ \kreuz{Pyramide} \\ \kreuz{Prisma} \\ \kreuz{Quader}

2. `koerper-e1-k4-s1-v1` – Körper in ein Schrägbild einzeichnen (Kegel im Quader)

   vorher: Ein Kegel aus Beton (Radius $25$ cm, Höhe $70$ cm) wird in einem quaderförmigen Karton verschickt, der so klein wie möglich ist. Skizziere den Kegel in das Schrägbild des Kartons (P10 2024 OS).

   nachher: Ein Kegel aus Beton hat die Form eines Kegels mit Radius $25$ cm und Höhe $70$ cm. Er wird in einem quaderförmigen Karton verschickt, der so klein wie möglich ist. Skizziere den Kegel in das Schrägbild des Kartons (P10 2024 OS).

3. `koerper-e2-k1-s6-v1` – Kante aus V

   vorher: Quader: Volumen $90$ cm³, Länge $5$ cm, Breite $3$ cm – Höhe?

   nachher: Ein Quader hat das Volumen $90$ cm³. Er ist $5$ cm lang und $3$ cm breit. Wie hoch ist der Quader?

4. `koerper-e3-k1-s2-v1` – Rechteckgrundfläche

   vorher: Prisma mit rechteckiger Grundfläche $7$ cm × $3$ cm, Höhe $5$ cm – Volumen?

   nachher: Die Grundfläche eines Prismas ist ein Rechteck mit $7$ cm × $3$ cm. Das Prisma ist $5$ cm hoch. Berechne sein Volumen.

5. `koerper-e3-k2-s3-v1` – Sachaufgabe (Dach, Vitrine, Werbeprisma, Zelt, Schokoladenverpackung)

   vorher: Ein Dachboden hat die Form eines liegenden Dreiecksprismas: $9$ m breit, $3{,}5$ m hoch und $11$ m lang. Ein Heizgerät reicht für Räume bis $180$ m³. Reicht es für den ausgebauten Dachboden?

   nachher: Ein Dachboden hat die Form eines liegenden Dreiecksprismas. Er ist $9$ m breit, $3{,}5$ m hoch und $11$ m lang. Ein Heizgerät reicht für Räume bis $180$ m³. Reicht es für den ausgebauten Dachboden?

6. `koerper-e4-k2-s9-v1` – r aus V

   vorher: Ein größerer Becher soll bei $9$ cm Höhe $600$ cm³ fassen. Berechne den Radius auf eine Stelle (P10 2022 OS).

   nachher: Ein größerer Becher soll bei $9$ cm Höhe $600$ cm³ fassen. Berechne den Radius. Runde auf eine Stelle nach dem Komma. (P10 2022 OS)

7. `koerper-e5-k1-s3-v1` – Quader und Halbzylinder

   vorher: Ein Pool: Rechteck $8$ m × $4$ m, an der $4$-m-Seite ein Halbkreis mit $2$ m Radius; überall $1{,}4$ m tief – Wasservolumen auf eine Stelle?

   nachher: Ein Pool hat als Grundfläche ein Rechteck mit $8$ m × $4$ m. An der $4$-m-Seite schließt ein Halbkreis mit $2$ m Radius an. Der Pool ist überall $1{,}4$ m tief. Wie viel Wasser passt hinein? Runde auf eine Stelle nach dem Komma.

8. `koerper-e5-k4-s3-v1` – Haus = Quader + Dreiecksprisma; Pool = Quader + Halbzylinder

   vorher: Ein Pool: Rechteck $9$ m × $4$ m, an der $4$-m-Seite ein Halbkreis mit $2$ m Radius, überall $1{,}4$ m tief. Der Schlauch liefert $1\,800$ l pro Stunde. Ist der Pool am Sonntag um $14$ Uhr voll, wenn man am Freitag um $18$ Uhr anfängt?

   nachher: Ein Pool hat als Grundfläche ein Rechteck mit $9$ m × $4$ m. An der $4$-m-Seite schließt ein Halbkreis mit $2$ m Radius an. Der Pool ist überall $1{,}4$ m tief. Der Schlauch liefert $1\,800$ l pro Stunde. Man fängt am Freitag um $18$ Uhr an. Ist der Pool am Sonntag um $14$ Uhr voll?

9. `koerper-zone-f3-v3` – Längen- und Volumeneinheiten, Kubikdezimeter als Liter, Kubikzentimete

   vorher: $2{,}35$ m – wie viel cm?

   nachher: Rechne $2{,}35$ m in cm um.

10. `koerper-zone-f6-v4` – Prozentwert berechnen (zehn Prozent von einem Volumen mit Komma)

   vorher: Ein Eimer wiegt leer $2$ kg und fasst $8$ l Wasser; $1$ l Wasser wiegt $1$ kg. Er ist zu $25\,\%$ gefüllt. Wie schwer ist der Eimer jetzt?

   nachher: Ein Eimer wiegt leer $2$ kg und fasst $8$ l Wasser. $1$ l Wasser wiegt $1$ kg. Der Eimer ist zu $25\,\%$ gefüllt. Wie schwer ist der Eimer jetzt?

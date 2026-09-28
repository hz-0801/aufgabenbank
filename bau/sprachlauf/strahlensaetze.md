# Sprachlauf strahlensaetze

Stand 2026-09-28 (Sprachlauf Gruppe 3). Regeln: bau/sprachlauf/regeln.md.
Vergleich gegen den Bankstand 5e58c41. Nur das Feld aufgabe ist geändert;
`python3 werkzeuge/bank-pruef.py strahlensaetze`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 66 | 16 | 82 |
| e2.jsonl | 51 | 3 | 54 |
| e3.jsonl | 35 | 16 | 51 |
| zone.jsonl | 27 | 12 | 39 |
| gesamt | 179 | 47 | 226 |

Geänderte Sprossen: 71. Die 10 Beispiele sind je Sprosse die erste
geänderte Zeile, gleichmäßig über die Sprossen verteilt (Zone zuerst).

## 10 Beispiele vorher/nachher

1. `strahlensaetze-zone-f1-v1` – Dezimalzahlen und ganze Zahlen mal und geteilt durch eine Za

   vorher: $3{,}4 \cdot 100$ – wie viel?

   nachher: Berechne $3{,}4 \cdot 100$.

2. `strahlensaetze-zone-f3-v1` – Vielfache und Teiler, „doppelt“, „halb“, „dreifach“, „ein Dr

   vorher: Das Doppelte von $35$ – wie viel?

   nachher: Berechne das Doppelte von $35$.

3. `strahlensaetze-zone-f8-v1` – Gleichung mit einer Variablen und Verhältnisgleichung nach x

   vorher: $x : 4 = 3$ – wie groß ist $x$?

   nachher: Löse die Gleichung. $\frac{x}{4} = 3$

4. `strahlensaetze-e1-k2-s1-v1` – Maßstab lesen und in Worten sagen: ein Zentimeter auf dem Pl

   vorher: Maßstab $1 : 20$ – wie viel ist $1\,\text{cm}$ auf dem Plan in Wirklichkeit?

   nachher: Ein Plan hat den Maßstab $1 : 20$. Wie lang ist $1\,\text{cm}$ auf dem Plan in Wirklichkeit?

5. `strahlensaetze-e1-k3-s0-v1` – „passt es ins Feld“ ankreuzen (Vorstufe)

   vorher: Ein Beet ist $4\,\text{m}$ lang und $2\,\text{m}$ breit. Das Zeichenfeld ist $15\,\text{cm}$ breit und $9\,\text{cm}$ hoch. Welcher Maßstab passt? \kreuz{$1 : 20$} \\ \kreuz{$1 : 40$} \\ \kreuz{$1 : 1\,000$}

   nachher: Ein Beet ist $4\,\text{m}$ lang und $2\,\text{m}$ breit. Das Zeichenfeld ist $15\,\text{cm}$ breit und $9\,\text{cm}$ hoch. Das Beet soll möglichst groß in das Feld passen. Kreuze den passenden Maßstab an. \kreuz{$1 : 20$} \\ \kreuz{$1 : 40$} \\ \kreuz{$1 : 1\,000$}

6. `strahlensaetze-e1-k3-s9-v1` – Prüfungshöhe: Draufsicht einer Tonne auf einer Platte als Kr

   vorher: Eine zylinderförmige Futtertonne ist $90\,\text{cm}$ hoch und hat den Radius $33\,\text{cm}$. Sie soll mit einer rechteckigen Holzplatte abgedeckt werden, die $60\,\text{cm}$ breit und $85\,\text{cm}$ lang ist. Zeichne die Draufsicht von Tonne und Platte in einem passenden Maßstab in das Karofeld, gib den Maßstab an und beschrifte. Entscheide, ob die Platte die Tonne vollständig abdeckt. (P10 2021 OS)

   nachher: Eine zylinderförmige Futtertonne ist $90\,\text{cm}$ hoch und hat den Radius $33\,\text{cm}$. Sie soll mit einer rechteckigen Holzplatte abgedeckt werden. Die Platte ist $60\,\text{cm}$ breit und $85\,\text{cm}$ lang. Zeichne die Draufsicht von Tonne und Platte in das Karofeld. Wähle dazu einen passenden Maßstab und gib ihn an. Beschrifte die Zeichnung. Entscheide, ob die Platte die Tonne vollständig abdeckt. (P10 2021 OS)

7. `strahlensaetze-e2-k1-s4-v1` – Streckfaktor aus Original- und Bildstrecke berechnen

   vorher: $\overline{AB} = 5\,\text{cm}$, die Bildstrecke $\overline{A'B'} = 15\,\text{cm}$ – wie groß ist der Streckfaktor $k$?

   nachher: Die Strecke $\overline{AB}$ ist $5\,\text{cm}$ lang. Sie wird zentrisch gestreckt. Die Bildstrecke $\overline{A'B'}$ ist $15\,\text{cm}$ lang. Wie groß ist der Streckfaktor $k$?

8. `strahlensaetze-e2-k1-s12-v1` – Prüfungshöhe: kein P10-Original; Zielmarke nach RLP E: zu Fi

   vorher: Ein Foto ist $9\,\text{cm}$ breit und $13\,\text{cm}$ hoch. Poster A ist $27\,\text{cm}$ breit und $39\,\text{cm}$ hoch, Poster B $30\,\text{cm}$ breit und $40\,\text{cm}$ hoch. Welches Poster ist zum Foto ähnlich? Gib den Streckfaktor an. Ein Baum ist auf dem Foto $2{,}4\,\text{cm}$ hoch – wie hoch ist er auf diesem Poster?

   nachher: Ein Foto ist $9\,\text{cm}$ breit und $13\,\text{cm}$ hoch. Poster A ist $27\,\text{cm}$ breit und $39\,\text{cm}$ hoch. Poster B ist $30\,\text{cm}$ breit und $40\,\text{cm}$ hoch. Welches Poster ist zum Foto ähnlich? Gib den Streckfaktor an. Auf dem Foto ist ein Baum $2{,}4\,\text{cm}$ hoch. Wie hoch ist der Baum auf diesem Poster?

9. `strahlensaetze-e3-k1-s7-v1` – Sachaufgabe, bei der die Skizze selbst gezeichnet wird: Flus

   vorher: Zwei Bäume am anderen Ufer eines Flusses stehen $24\,\text{m}$ auseinander. Von einem Punkt $Z$ aus werden sie angepeilt; die zwei Peillinien treffen das eigene Ufer $8\,\text{m}$ auseinander. $Z$ ist $5\,\text{m}$ vom eigenen Ufer entfernt, beide Ufer sind parallel. Fertige eine Skizze an und berechne die Breite des Flusses.

   nachher: Zwei Bäume stehen am anderen Ufer eines Flusses. Sie sind $24\,\text{m}$ voneinander entfernt. Von einem Punkt $Z$ aus schaut man zu beiden Bäumen. Die zwei Blicklinien kreuzen das eigene Ufer $8\,\text{m}$ voneinander entfernt. $Z$ ist $5\,\text{m}$ vom eigenen Ufer entfernt. Beide Ufer sind parallel. Fertige eine Skizze an und berechne die Breite des Flusses.

10. `strahlensaetze-e3-k4-s4-v1` – Verhältnisgleichung aufstellen, gesuchte Strecke allein auf

   vorher: In der V-Figur sind $AB$ und $A'B'$ parallel. Welche Gleichung passt? \kreuz{$\overline{ZA} : \overline{ZA'} = \overline{ZB} : \overline{ZB'}$} \\ \kreuz{$\overline{ZA} : \overline{AA'} = \overline{ZB'} : \overline{ZB}$} \\ \kreuz{$\overline{AB} : \overline{A'B'} = \overline{ZA} : \overline{AA'}$}

   nachher: In der V-Figur sind $AB$ und $A'B'$ parallel. Kreuze die Gleichung an, die zur Figur passt. \kreuz{$\overline{ZA} : \overline{ZA'} = \overline{ZB} : \overline{ZB'}$} \\ \kreuz{$\overline{ZA} : \overline{AA'} = \overline{ZB'} : \overline{ZB}$} \\ \kreuz{$\overline{AB} : \overline{A'B'} = \overline{ZA} : \overline{AA'}$}

## Fälle, in denen die Regeln nicht reichten

1. „:“ als Division oder als Verhältnis (e1-k4-s1-v3, e3-k4-s1-v3,
   e2-k3-s1-v2, zone-f8-v1). Entscheidung: Wo „:“ ein Verhältnis von
   Längen ist (Maßstab $1 : n$, Streckfaktor $k = 4{,}5 : 6$,
   Verhältnisgleichung $\overline{ZB'} : 5 = 8 : 2$), bleibt es. Reine
   Rechenschritte wurden Brüche: Leas $\frac{180}{20} = 9$, Leos
   falsch umgestellte Rechnung $\frac{5}{8} \cdot 2$ (vorher
   „$5 : 8 \cdot 2$“, für Schüler doppeldeutig), zone-f1
   $\frac{56}{100}$, $\frac{18}{60}$ und zone-f8-v1 $\frac{x}{4} = 3$
   (passt zu f8-v3/v4). In den loesung-Feldern steht weiter „:“ –
   nicht angefasst, weil nur aufgabe geändert werden darf.
2. Gleichungen in zone-f8: loesung steht als „$x = 12$“, nicht als
   Lösungsmenge. Daher „Löse die Gleichung.“ ohne 𝕃 (alle vier Zeilen
   f8-v1 bis v4).
3. e3-k4-s3-v3 (Taschenlampe): „Wand $2\,\text{m}$ hinter der Lampe“
   ist räumlich falsch (die Lösung rechnet mit $200\,\text{cm}$ Abstand
   Lampe–Wand, die Wand liegt vor der Lampe hinter der Figur). Neu:
   „Die Wand ist $2\,\text{m}$ von der Lampe entfernt.“ – Lösung
   unverändert. Ähnlich e1-k3-s3-v2/v3 und e1-k3-s4-v3: falsches
   Pronomen („Zeichne es“ für Balkon/Garage, „ihn“ für Beet)
   berichtigt. Bei e3-k1-s7-v2 (Förster) „Kathete“ durch „Seite am
   rechten Winkel“ ersetzt, weil die Sprosse das Wort nicht übt; in
   e2-k1-s9 (Übergabe an Trigonometrie) bleiben „Kathete“ und
   „Hypotenuse“.

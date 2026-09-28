# Sprachlauf zinsrechnung

Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Vergleich gegen den Bankstand ecde001. Nur das Feld aufgabe ist geändert (Skriptprobe: alle anderen Felder gleich, keine Zahl verloren, keine neue Zahl). `python3 werkzeuge/bank-pruef.py zinsrechnung`: 0 Abweichungen, 0 Warnungen.

## Zählung

| Datei | geändert | unverändert | Zeilen |
| --- | --: | --: | --: |
| e1.jsonl | 55 | 20 | 75 |
| e2.jsonl | 52 | 3 | 55 |
| zone.jsonl | 34 | 1 | 35 |
| gesamt | 141 | 24 | 165 |

## 10 Beispiele

1. `zinsrechnung-e1-k1-s0-v1` – „was ist was“ und „Zinsen oder Guthaben“ ankreuzen

   vorher: Lena legt 850\,€ für ein Jahr auf ein Sparbuch, die Bank zahlt 2\,\% Zinsen. Wie viel Euro Zinsen bekommt sie? Was ist gesucht? Kreuze an, rechne nicht. \\ \kreuz{das Kapital (Grundwert)} \\ \kreuz{der Zinssatz (Prozentsatz)} \\ \kreuz{die Zinsen (Prozentwert)}

   nachher: Lena legt 850\,€ für ein Jahr auf ein Sparbuch. Die Bank zahlt 2\,\% Zinsen. Die Frage lautet: „Wie viel Euro Zinsen bekommt Lena?“ Kreuze an, was gesucht ist. Rechne nicht. \\ \kreuz{das Kapital (Grundwert)} \\ \kreuz{der Zinssatz (Prozentsatz)} \\ \kreuz{die Zinsen (Prozentwert)}

2. `zinsrechnung-e2-k1-s0-v1` – „vom Start oder vom neuen Guthaben“ und „plus oder mal“ ankreuzen

   vorher: Auf einem Konto liegen am Anfang 600\,€, nach einem Jahr mit Zinsen 612\,€. Von welchem Betrag werden die Zinsen im zweiten Jahr berechnet? Kreuze an, rechne nicht. \\ \kreuz{vom neuen Guthaben 612\,€} \\ \kreuz{vom Startguthaben 600\,€}

   nachher: Auf einem Konto liegen am Anfang 600\,€. Nach einem Jahr sind es mit Zinsen 612\,€. Kreuze an, von welchem Betrag die Zinsen im zweiten Jahr berechnet werden. Rechne nicht. \\ \kreuz{vom neuen Guthaben 612\,€} \\ \kreuz{vom Startguthaben 600\,€}

3. `zinsrechnung-zone-f1-v1` – Prozentwert berechnen

   vorher: 20\,\% von 40\,€ – wie viel Euro?

   nachher: Berechne 20\,\% von 40\,€.

4. `zinsrechnung-e1-k1-s11-v5` – Jahreszinsen aus Kapital und Zinssatz als Kurzantwort (P10-Form 2015-O

   vorher: Auf ein Sparbuch werden jedes Jahr 250\,€ eingezahlt. Weise nach, dass die Bank 3\,\% Zinsen pro Jahr zahlt. (P10 2014 OS)

   nachher: Auf ein Sparbuch werden jedes Jahr 250\,€ eingezahlt. Die Tabelle zeigt das Guthaben. Weise nach, dass die Bank 3\,\% Zinsen pro Jahr zahlt. (P10 2014 OS)

5. `zinsrechnung-e2-k1-s8-v1` – Zinsen insgesamt: Endkapital minus Startkapital

   vorher: 3\,000\,€ zu 2\,\% mit Zinseszins, 5 Jahre – wie viel Euro Zinsen insgesamt?

   nachher: Auf einem Konto liegen 3\,000\,€ für 5 Jahre. Die Bank zahlt 2\,\% Zinsen mit Zinseszins. Wie viel Euro Zinsen gibt es insgesamt?

6. `zinsrechnung-zone-f2-v1` – Prozentsatz berechnen

   vorher: 5\,€ von 20\,€ – wie viel Prozent?

   nachher: Wie viel Prozent von 20\,€ sind 5\,€?

7. `zinsrechnung-e1-k4-s3-v1` – Kredit: Zinsen als Kosten, Rückzahlung = Kreditsumme plus Zinsen

   vorher: Frau Demir leiht sich 4\,000\,€ für ein Jahr zu 6\,\%. Sie kann jeden Monat 350\,€ zurücklegen. Reicht das Gesparte nach einem Jahr für die Rückzahlung?

   nachher: Frau Demir leiht sich 4\,000\,€ für ein Jahr. Sie zahlt dafür 6\,\% Zinsen. Sie kann jeden Monat 350\,€ sparen. Reicht das Gesparte nach einem Jahr, um alles zurückzuzahlen?

8. `zinsrechnung-e2-k4-s4-v1` – Wachstumsfaktor: „plus 2 %“ ist „mal 1,02“, q = 1 + p/100

   vorher: Die Tabelle zeigt ein Guthaben mit Zinseszins. Welcher Zinssatz?

   nachher: Die Tabelle zeigt ein Guthaben mit Zinseszins. Wie hoch ist der Zinssatz?

9. `zinsrechnung-zone-f5-v1` – Dreisatz und fester Faktor („pro Monat“, „pro Tag“)

   vorher: 3 Monate kosten 21\,€ – wie viel kosten 5 Monate?

   nachher: Ein Abo kostet für 3 Monate 21\,€. Wie viel Euro kostet es für 5 Monate?

10. `zinsrechnung-e1-k2-s1-v1` – Jahreszinsen zuerst, dann durch zwölf, mal Anzahl der Monate

   vorher: 2\,400\,€ zu 2\,\% für 5 Monate – wie viel Euro Zinsen?

   nachher: Auf einem Konto liegen 2\,400\,€ für 5 Monate. Die Bank zahlt 2\,\% Zinsen im Jahr. Wie viel Euro Zinsen gibt es für die 5 Monate?

## Wo die Regeln nicht reichten

# Wo die Regeln nicht reichten (zinsrechnung)

- zinsrechnung-e1-k2-s0-v1 bis -v4: Die Ankreuzoptionen enthalten selbst einen Gedankenstrich („ein Jahr – nicht teilen“), und die loesung nennt die Option wortgleich. Ändern der Option hätte die Lösung gebrochen, ein neuer Stamm mit unverändertem \kreuz scheitert an der Gedankenstrich-Sperre in apply.py. Entscheidung: die vier Zeilen ganz unverändert gelassen; der Stamm „Welche Laufzeit? Kreuze an, rechne nicht.“ bleibt Stichwortsprache. Braucht eine Änderung an loesung und Optionen zusammen.
- zinsrechnung-e1-k1-s0-v1 bis -v4 (und ähnlich e2-k1-s0): Die Sprosse übt, die gestellte Frage einzuordnen („Was ist gesucht?“). Die Frage an die Sachlage steht deshalb als wörtliche Rede („Die Frage lautet: „Wie hoch ist der Zinssatz?““), danach ein Auftrag „Kreuze an, was gesucht ist. Rechne nicht.“; die Fachwörter in den Optionen (Kapital, Grundwert …) sind unverändert.
- Fachwörter Kapital, Zinssatz, Guthaben, Zinseszins, Wachstumsfaktor, Bankjahr: behalten, weil die Sprossen sie üben; kein Alltagswort in Klammern ergänzt, wo es eine Zahl gebraucht hätte (Bankjahr = 360 Tage wäre eine neue Zahl).
- Kurzformen „zu 2 %“ in guten Zeilen (e1-k1-s3, e1-k2-s5, e2-k4-s3-v1/v2) gelassen; in umgeschriebenen Zeilen als „Die Bank zahlt 2 % Zinsen im Jahr“ ausgeschrieben. Zahlen ohne $…$ wie in der Bank belassen (die Zeilen dieses Eintrags setzen Zahlen im Fließtext ohne Mathemodus).
- Begründungszeilen ohne Behauptung (e1-k4-s2-v3, e2-k4-s2-v2): in die feste Form „<Name> sagt: „…“ Begründe, ob <Name> recht hat.“ gebracht (Namen Tim, Lea neu); „Warum …? Begründe.“ (e1-k4-s2-v1/v2, e2-k4-s2-v1) in „Erkläre, warum …“.

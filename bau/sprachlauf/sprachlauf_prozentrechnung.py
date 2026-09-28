#!/usr/bin/env python3
"""Sprachlauf prozentrechnung (2026-09-28): schreibt das Feld aufgabe der
Bankzeilen in bank/prozentrechnung/*.jsonl nach bau/sprachlauf/regeln.md um.

Aufruf aus der Repo-Wurzel:
    python3 bau/sprachlauf/sprachlauf_prozentrechnung.py [--bericht]

Nur das Feld aufgabe wird geändert, alle anderen Felder bleiben byte-gleich.
Jede Zeile in NEU trägt den neuen Text; Zeilen, die nicht in NEU stehen,
bleiben unverändert. Probe: jede Zahl der alten aufgabe steht auch in der
neuen (Multimenge), und keine neue Zahl kommt hinzu (eine Zahl der alten
aufgabe darf im Fragesatz wiederholt werden).
--bericht schreibt bau/sprachlauf/prozentrechnung.md (Zählung und
25 Beispiele) aus dem Stand vor dem Lauf (git HEAD) und dem neuen Stand.
"""

import collections
import json
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
BANK = WURZEL / "bank" / "prozentrechnung"
P = "prozentrechnung-"
RUNDE = "Runde auf eine Stelle nach dem Komma."
STREIFEN_P = "Wie viel Prozent des ganzen Streifens sind grau?"
FEHLER = "Finde den Fehler und rechne richtig."

NEU = {
    # --- e1 Umwandeln -------------------------------------------------
    "e1-k1-s1-v1": "Der Streifen zeigt ein Ganzes. Ein Teil davon ist grau. " + STREIFEN_P,
    "e1-k1-s1-v2": "Der Streifen zeigt ein Ganzes. Ein Teil davon ist grau. " + STREIFEN_P,
    "e1-k1-s1-v3": "Der Streifen zeigt ein Ganzes. Ein Teil davon ist grau. " + STREIFEN_P,
    "e1-k1-s1-v4": "Der Streifen zeigt ein Ganzes. Ein Teil davon ist grau. " + STREIFEN_P,
    "e1-k1-s1-v5": "Der Streifen zeigt ein Ganzes. Ein Teil davon ist grau. " + STREIFEN_P,
    "e1-k1-s2-v1": r"Schreibe den Bruch $\frac{37}{100}$ in Prozent.",
    "e1-k1-s2-v2": r"Schreibe den Bruch $\frac{9}{100}$ in Prozent.",
    "e1-k1-s2-v3": r"Schreibe den Bruch $\frac{60}{100}$ in Prozent.",
    "e1-k1-s3-v1": r"Schreibe den Bruch $\frac{11}{20}$ in Prozent.",
    "e1-k1-s3-v2": r"Schreibe den Bruch $\frac{4}{25}$ in Prozent.",
    "e1-k1-s3-v3": r"Schreibe den Bruch $\frac{4}{5}$ in Prozent.",
    "e1-k1-s4-v1": r"Schreibe die Dezimalzahl $0{,}64$ in Prozent.",
    "e1-k1-s4-v2": r"Schreibe $12\,\%$ als Dezimalzahl.",
    "e1-k1-s4-v3": r"Schreibe die Dezimalzahl $0{,}3$ in Prozent.",
    "e1-k1-s5-v1": "Jeder hundertste Besucher bekommt einen Preis. Wie viel "
                   "Prozent der Besucher bekommen einen Preis?",
    "e1-k1-s5-v2": "Jede zweite Wohnung hat einen Balkon. Wie viel Prozent der "
                   "Wohnungen haben einen Balkon?",
    "e1-k1-s5-v3": "Jedes zehnte Los gewinnt. Wie viel Prozent der Lose "
                   "gewinnen?",
    "e1-k1-s6-v1": r"$35\,\%$ der Kinder fahren mit dem Rad zur Schule. Die "
                   r"anderen Kinder gehen zu Fuß. Wie viel Prozent der Kinder "
                   r"gehen zu Fuß?",
    "e1-k1-s6-v2": r"Bei einer Wahl bekommt A $42\,\%$ der Stimmen. B bekommt "
                   r"$31\,\%$. Den Rest bekommt C. Wie viel Prozent der Stimmen "
                   r"bekommt C?",
    "e1-k1-s6-v3": r"Ein Müsli besteht zu $45\,\%$ aus Haferflocken. $30\,\%$ "
                   r"sind Obst und $15\,\%$ sind Nüsse. Der Rest sind Kerne. "
                   r"Wie viel Prozent des Müslis sind Kerne?",
    "e1-k1-s7-v1": r"$5\,\%$ der Pakete kommen zu spät. Kreuze die Aussage an, "
                   r"die dazu passt. (P10 2020 OS)\\ \kreuz{$5$ von $10$ Paketen "
                   r"kommen zu spät.}\\ \kreuz{Jedes 5. Paket kommt zu spät.}\\ "
                   r"\kreuz{$5$ von $100$ Paketen kommen zu spät.}",
    "e1-k1-s7-v2": r"$8\,\%$ der Gäste bestellen Tee. Kreuze die Aussage an, die "
                   r"dazu passt. (P10 2020 OS)\\ \kreuz{Jeder 8. Gast bestellt "
                   r"Tee.}\\ \kreuz{$8$ von $100$ Gästen bestellen Tee.}\\ "
                   r"\kreuz{$8$ von $10$ Gästen bestellen Tee.}",
    "e1-k1-s7-v3": r"Jeder vierte Besucher kauft ein Programmheft. Kreuze an, "
                   r"wie viel Prozent der Besucher das sind. (P10 2022 OS)\\ "
                   r"\kreuz{$4\,\%$}\\ \kreuz{$25\,\%$}\\ \kreuz{$40\,\%$}\\ "
                   r"\kreuz{$75\,\%$}",
    "e1-k1-s7-v4": r"Jedes zwanzigste Ei einer Lieferung ist zerbrochen. Kreuze "
                   r"an, wie viel Prozent der Eier das sind. (P10 2022 OS)\\ "
                   r"\kreuz{$2\,\%$}\\ \kreuz{$5\,\%$}\\ \kreuz{$20\,\%$}\\ "
                   r"\kreuz{$80\,\%$}",
    "e1-k1-s8-v1": r"Die Tabelle zeigt den Schulweg der Kinder einer Schule. "
                   r"Genau eine Aussage ist falsch. Kreuze sie an und schreibe "
                   r"sie richtig. (P10 2023 OS)\\ \kreuz{Aussage 1: Ein Viertel "
                   r"der Kinder fährt mit dem Bus.}\\ \kreuz{Aussage 2: Die Hälfte "
                   r"der Kinder fährt mit dem Rad.}",
    "e1-k1-s8-v2": r"Die Tabelle zeigt die Mitglieder eines Sportvereins. Genau "
                   r"eine Aussage ist falsch. Kreuze sie an und schreibe sie "
                   r"richtig. (P10 2023 OS)\\ \kreuz{Aussage 1: Jedes fünfte "
                   r"Mitglied ist ein Kind.}\\ \kreuz{Aussage 2: Die Hälfte der "
                   r"Mitglieder sind Erwachsene.}",
    "e1-k1-s8-v3": r"Befragte in der Stadt und auf dem Land sagen, was sie in der "
                   r"Freizeit machen. Die Tabelle zeigt die Anteile. Genau eine "
                   r"Aussage ist falsch. Kreuze sie an und schreibe sie richtig. "
                   r"(P10 2019 OS)\\ \kreuz{Aussage 1: Ein Viertel der Befragten "
                   r"auf dem Land geht in die Bibliothek.}\\ \kreuz{Aussage 2: "
                   r"Mehr als die Hälfte der Befragten auf dem Land treibt Sport "
                   r"im Verein.}",
    "e1-k1-s8-v4": r"Kinder der Grundschule und der Oberschule sagen, wie oft sie "
                   r"zu Hause frühstücken. Die Tabelle zeigt die Anteile. Genau "
                   r"eine Aussage ist falsch. Kreuze sie an und schreibe sie "
                   r"richtig. (P10 2019 OS)\\ \kreuz{Aussage 1: Drei von fünf "
                   r"Oberschülern frühstücken immer zu Hause.}\\ \kreuz{Aussage 2: "
                   r"Jeder zehnte Grundschüler frühstückt nie zu Hause.}",
    "e1-k1-s8-v5": r"Die Tabelle zeigt, wie oft Jugendliche Sport treiben. Jemand "
                   r"behauptet: „Mehr als die Hälfte der Jugendlichen treibt "
                   r"mindestens zweimal pro Woche Sport.“ Begründe mit den Werten "
                   r"der Tabelle, ob das stimmt. (P10 2017 OS)",
    "e1-k1-s8-v6": r"Die Tabelle zeigt, wie viele Autos die Haushalte haben. "
                   r"Jemand behauptet: „Mehr als $70\,\%$ der Haushalte haben "
                   r"mindestens ein Auto.“ Begründe mit den Werten der Tabelle, "
                   r"ob das stimmt. (P10 2017 OS)",
    "e1-k1-s9-v1": "Die Tabelle zeigt, woher der Strom einer Gemeinde kommt. Ein "
                   "Anteil fehlt. Trage den fehlenden Anteil in die Tabelle ein. "
                   "(P10 2021 OS)",
    "e1-k1-s9-v2": "Die Tabelle zeigt, wie die Fläche eines Landkreises genutzt "
                   "wird. Ein Anteil fehlt. Trage den fehlenden Anteil in die "
                   "Tabelle ein. (P10 2021 OS)",
    "e1-k2-s1-v1": r"Ordne die Zahlen der Größe nach, die kleinste zuerst. "
                   r"$0{,}4$; $\frac{1}{4}$; $35\,\%$; $\frac{3}{10}$",
    "e1-k2-s1-v2": r"Ordne die Zahlen der Größe nach, die kleinste zuerst. "
                   r"$0{,}07$; $\frac{1}{20}$; $6\,\%$; $\frac{1}{10}$",
    "e1-k2-s1-v3": r"Ordne die Zahlen der Größe nach, die kleinste zuerst. "
                   r"$\frac{3}{5}$; $0{,}55$; $58\,\%$; $\frac{1}{2}$",
    "e1-k3-s1-v1": r"Tom sagt: „Jede fünfundzwanzigste Schraube ist fehlerhaft, "
                   r"das sind $25\,\%$.“ Finde den Fehler und schreibe die "
                   r"Aussage richtig.",
    "e1-k3-s1-v2": r"Mia schreibt: $\frac{2}{5} = 25\,\%$. Finde den Fehler und "
                   r"schreibe es richtig.",
    "e1-k3-s1-v3": r"Ben sagt: „$2\,\%$ heißt: jeder Zweite.“ Finde den Fehler "
                   r"und schreibe die Aussage richtig.",
    "e1-k3-s2-v1": r"Erkläre, warum $\frac{1}{4}$ dasselbe ist wie $25\,\%$.",
    "e1-k3-s2-v2": r"Erkläre, warum $\frac{3}{20}$ und $15\,\%$ gleich viel "
                   r"sind.",
    "e1-k3-s2-v3": r"Sara sagt: „$\frac{1}{2}$ und $2\,\%$ sind gleich viel.“ "
                   r"Begründe, ob Sara recht hat.",
    "e1-k3-s4-v1": r"Die Klassen 7a und 7b stimmen über den Wandertag ab. In der "
                   r"7a sind $18$ von $25$ Kindern für den Zoo. In der 7b sind "
                   r"$21$ von $30$ Kindern für den Zoo. In welcher Klasse ist der "
                   r"Anteil für den Zoo größer?",
    "e1-k3-s4-v2": r"Nele und Jonas werfen beim Basketball Freiwürfe. Nele trifft "
                   r"$17$ von $20$ Würfen. Jonas trifft $22$ von $25$ Würfen. Wer "
                   r"hat den größeren Anteil an Treffern?",
    # --- e2 Prozentsatz -----------------------------------------------
    "e2-k1-s0-v1": r"In der Klasse sind $28$ Kinder. $7$ davon haben einen Hund. "
                   r"Welche Zahl ist hier das Ganze?",
    "e2-k1-s0-v2": r"Von $600$ Losen sind $90$ Gewinne. Welche Zahl ist hier das "
                   r"Ganze?",
    "e2-k1-s0-v3": r"$45$ Gäste essen vegetarisch. Eingeladen sind $150$ Gäste. "
                   r"Welche Zahl ist hier das Ganze?",
    "e2-k1-s0-v4": r"Ein Pullover kostete $60\,€$. Jetzt kostet er $45\,€$. "
                   r"Welcher Preis ist hier das Ganze?",
    "e2-k2-s0-v1": r"Teile den Streifen in gleiche Teile ein. Jeder Teil soll "
                   r"$10\,\%$ sein.",
    "e2-k2-s0-v2": r"Teile den Streifen in gleiche Teile ein. Jeder Teil soll "
                   r"$25\,\%$ sein.",
    "e2-k2-s0-v3": r"Teile den Streifen in gleiche Teile ein. Jeder Teil soll "
                   r"$20\,\%$ sein.",
    "e2-k2-s0-v4": r"Teile den Streifen in gleiche Teile ein. Jeder Teil soll "
                   r"$5\,\%$ sein.",
    "e2-k3-s0-v1": r"Der ganze Streifen steht für $50$ Kinder. Der graue Teil "
                   r"steht für $10$ Kinder. " + STREIFEN_P,
    "e2-k3-s0-v2": r"Der ganze Streifen steht für $40$ kg. Der graue Teil steht "
                   r"für $30$ kg. " + STREIFEN_P,
    "e2-k3-s0-v3": r"Der ganze Streifen steht für $200$ m. Der graue Teil steht "
                   r"für $140$ m. " + STREIFEN_P,
    "e2-k3-s0-v4": r"Der ganze Streifen steht für $80\,€$. Der graue Teil steht "
                   r"für $40\,€$. " + STREIFEN_P,
    "e2-k3-s1-v1": r"$17$ von $100$ Schülern spielen ein Instrument. Wie viel "
                   r"Prozent der Schüler spielen ein Instrument?",
    "e2-k3-s1-v2": r"$68$ von $100$ Losen sind Nieten. Wie viel Prozent der Lose "
                   r"sind Nieten?",
    "e2-k3-s1-v3": r"$3$ von $100$ Äpfeln sind faul. Wie viel Prozent der Äpfel "
                   r"sind faul?",
    "e2-k3-s1-v4": r"$45$ von $100$ Befragten fahren Rad. Wie viel Prozent der "
                   r"Befragten fahren Rad?",
    "e2-k3-s1-v5": r"Zu einem Fest kommen $100$ Gäste. $81$ davon bleiben zum "
                   r"Essen. Wie viel Prozent der Gäste bleiben zum Essen?",
    "e2-k3-s2-v1": r"$19$ von $50$ Kindern haben ein Haustier. Wie viel Prozent "
                   r"der Kinder haben ein Haustier?",
    "e2-k3-s2-v2": r"Lea beantwortet $7$ von $25$ Fragen richtig. Wie viel "
                   r"Prozent der Fragen hat sie richtig?",
    "e2-k3-s2-v3": r"Im Bus sind $13$ von $20$ Plätzen belegt. Wie viel Prozent "
                   r"der Plätze sind belegt?",
    "e2-k3-s3-v1": r"Ein Training dauert $60$ Minuten. $27$ Minuten davon wird "
                   r"gelaufen. Wie viel Prozent der Zeit wird gelaufen?",
    "e2-k3-s3-v2": r"$153$ von $360$ Schülern kommen mit dem Bus. Wie viel "
                   r"Prozent der Schüler kommen mit dem Bus?",
    "e2-k3-s3-v3": r"$91$ von $140$ Zuschauern sind Kinder. Wie viel Prozent der "
                   r"Zuschauer sind Kinder?",
    "e2-k3-s4-v1": r"$17$ von $24$ Kindern waren im Schwimmbad. Wie viel Prozent "
                   r"der Kinder waren im Schwimmbad? " + RUNDE,
    "e2-k3-s4-v2": r"Ein Team hat $5$ von $7$ Spielen gewonnen. Wie viel Prozent "
                   r"der Spiele hat es gewonnen? " + RUNDE,
    "e2-k3-s4-v3": r"In einem Wald sind $38$ von $55$ Bäumen Kiefern. Wie viel "
                   r"Prozent der Bäume sind Kiefern? " + RUNDE,
    "e2-k3-s5-v1": r"Im Chor singen $14$ Mädchen und $6$ Jungen. Wie viel "
                   r"Prozent der Kinder im Chor sind Jungen?",
    "e2-k3-s5-v2": r"Eine Mannschaft hat $18$ Siege, $4$ Unentschieden und $3$ "
                   r"Niederlagen. Wie viel Prozent der Spiele waren Siege?",
    "e2-k3-s5-v3": r"Eine Bäckerei verkauft $72$ Brote mit Körnern und $48$ Brote "
                   r"ohne Körner. Wie viel Prozent der Brote haben Körner?",
    "e2-k3-s6-v1": r"Eine Jacke kostete vorher $80\,€$. Jetzt kostet sie $60\,€$. "
                   r"Wie viel Prozent Rabatt gibt es auf den alten Preis?",
    "e2-k3-s6-v2": r"Ein Fahrradhelm kostete vorher $45\,€$. Jetzt kostet er "
                   r"$36\,€$. Wie viel Prozent Rabatt gibt es auf den alten Preis?",
    "e2-k3-s6-v3": r"Eine Spielkonsole kostete vorher $360\,€$. Jetzt kostet sie "
                   r"$306\,€$. Wie viel Prozent Rabatt gibt es auf den alten "
                   r"Preis?",
    "e2-k3-s7-v2": r"Auf dem Blech liegen $11$ Muffins mit Blaubeeren und $4$ mit "
                   r"Kirschen. Wie viel Prozent der Muffins sind mit Kirschen? "
                   + RUNDE + " (P10 2018 OS)",
    "e2-k3-s7-v3": r"Eine Stadt hat $480\,000$ Einwohner. Davon sind $72\,000$ "
                   r"Kinder, $57\,000$ Jugendliche, $264\,000$ Erwachsene und "
                   r"$87\,000$ Senioren. Wie viel Prozent der Einwohner sind "
                   r"Jugendliche? " + RUNDE + " (P10 2023 OS)",
    "e2-k3-s7-v4": r"Ein Haushalt braucht pro Tag $380$ l Wasser. Für die "
                   r"Toilette sind es $102$ l, zum Duschen $136$ l und für die "
                   r"Wäsche $46$ l. Der Rest sind $96$ l. Wie viel Prozent des "
                   r"Wassers braucht der Haushalt zum Duschen? " + RUNDE
                   + " (P10 2023 OS)",
    "e2-k3-s7-v5": r"Von $64$ Bewerbungen wurden $47$ angenommen. Wie viel "
                   r"Prozent der Bewerbungen wurden abgelehnt? " + RUNDE
                   + " (P10 2015 OS)",
    "e2-k3-s7-v6": r"Ein Zug fuhr an $92$ Tagen. An $79$ Tagen war er pünktlich. "
                   r"An wie viel Prozent der Tage war er verspätet? " + RUNDE
                   + " (P10 2015 OS)",
    "e2-k3-s8-v1": r"Eine Stadt hat $40\,000$ Einwohner. In diesem Jahr sind "
                   r"$1\,080$ Menschen zugezogen. Wie viel Prozent der "
                   r"Einwohnerzahl sind das? (P10 2014 OS)",
    "e2-k3-s8-v2": r"Von $12\,500$ verkauften Konzertkarten wurden $175$ "
                   r"zurückgegeben. Wie viel Prozent der Karten wurden "
                   r"zurückgegeben? (P10 2014 OS)",
    "e2-k3-s9-v1": r"Eine Mannschaft hat $13$ Spieler. Ihre Körpergrößen in cm "
                   r"sind: $172$, $185$, $169$, $190$, $178$, $181$, $166$, "
                   r"$188$, $175$, $183$, $170$, $192$, $177$. Wie viel Prozent "
                   r"der Spieler sind größer als $180$ cm? " + RUNDE
                   + " (P10 2025 OS)",
    "e2-k3-s9-v2": r"In einer Praxis warten $9$ Patienten. Ihre Wartezeiten in "
                   r"Minuten sind: $12$, $35$, $8$, $22$, $41$, $17$, $30$, $5$, "
                   r"$26$. Wie viel Prozent der Patienten warteten länger als "
                   r"$20$ Minuten? " + RUNDE + " (P10 2025 OS)",
    "e2-k4-s1-v1": r"Der Teil soll $30\,\%$ vom Ganzen sein. Gib dafür ein "
                   r"Beispiel mit Teil und Ganzem an.",
    "e2-k4-s1-v2": r"Der Teil soll $25\,\%$ vom Ganzen sein. Gib dafür ein "
                   r"Beispiel mit Teil und Ganzem an.",
    "e2-k4-s1-v3": r"Der Teil soll $12{,}5\,\%$ vom Ganzen sein. Gib dafür ein "
                   r"Beispiel mit Teil und Ganzem an.",
    "e2-k5-s1-v1": r"Kim soll ausrechnen, wie viel Prozent $12$ von $48$ Kindern "
                   r"sind. Kim rechnet so: \rechnung{\frac{48}{12} &= 4 = "
                   r"400\,\%} " + FEHLER,
    "e2-k5-s1-v2": r"Paul soll ausrechnen, wie viel Prozent $18$ von $45$ Äpfeln "
                   r"sind. Paul rechnet so: \rechnung{\frac{45}{18} &= 2{,}5 = "
                   r"2{,}5\,\%} " + FEHLER,
    "e2-k5-s1-v3": r"Im Korb liegen $6$ Birnen und $18$ Äpfel. Lea berechnet den "
                   r"Anteil der Birnen so: \rechnung{\frac{6}{18} &\approx "
                   r"0{,}333 = 33{,}3\,\%} " + FEHLER,
    "e2-k5-s2-v1": "Beim Prozentsatz teilt man durch das Ganze, nicht durch den "
                   "Teil. Erkläre, warum.",
    "e2-k5-s2-v2": r"Ali sagt: „$30$ von $60$ und $15$ von $30$ sind derselbe "
                   r"Prozentsatz.“ Begründe, ob Ali recht hat.",
    "e2-k5-s2-v3": r"Begründe, ob ein Teil mehr als $100\,\%$ von seinem Ganzen "
                   r"sein kann.",
    "e2-k5-s3-v1": r"Das Ganze sind $40$ kg. Der Teil sind $10$ kg. Zeichne den "
                   r"Teil in den Streifen ein und lies ab, wie viel Prozent das "
                   r"sind.",
    "e2-k5-s3-v2": r"Das Ganze sind $30$ m. Der Teil sind $21$ m. Zeichne den "
                   r"Teil in den Streifen ein und lies ab, wie viel Prozent das "
                   r"sind.",
    "e2-k5-s3-v3": r"Von $120$ Teilnehmern sind $54$ Frauen. Berechne mit der "
                   r"Tabelle, wie viel Prozent der Teilnehmer Frauen sind.",
    "e2-k5-s4-v1": r"Ein Handyvertrag hat $20$ GB im Monat. Am 20. Tag sind $17$ "
                   r"GB verbraucht. Wie viel Prozent der $20$ GB sind noch übrig? "
                   r"Reicht der Rest bei gleichem Verbrauch für die letzten $10$ "
                   r"Tage?",
    "e2-k5-s4-v2": r"In der 7c wird ein Klassensprecher gewählt. Emma bekommt "
                   r"$12$ Stimmen, Noah bekommt $9$. $6$ Stimmen sind ungültig. "
                   r"Emma sagt: „Ich habe die Mehrheit aller Stimmen.“ Berechne "
                   r"Emmas Anteil in Prozent und prüfe, ob sie recht hat. " + RUNDE,
    "e2-k5-s4-v3": r"Eine Bäckerei wirft abends Brötchen weg. Am Montag sind es "
                   r"$36$ von $240$ Brötchen. Am Dienstag sind es $27$ von $150$ "
                   r"Brötchen. An welchem Tag war der Anteil weggeworfener "
                   r"Brötchen größer?",
    # --- e3 Prozentwert -----------------------------------------------
    "e3-k1-s1-v1": r"Der ganze Streifen steht für $80\,€$. Wie viel Euro sind "
                   r"$50\,\%$ davon?",
    "e3-k1-s1-v2": r"Der ganze Streifen steht für $60$ kg. Wie viel kg sind "
                   r"$25\,\%$ davon?",
    "e3-k1-s1-v3": r"Der ganze Streifen steht für $300$ m. Wie viele Meter sind "
                   r"$10\,\%$ davon?",
    "e3-k1-s1-v4": r"Der ganze Streifen steht für $14$ l. Wie viele Liter sind "
                   r"$50\,\%$ davon?",
    "e3-k1-s1-v5": r"Der ganze Streifen steht für $90\,€$. Wie viel Euro sind "
                   r"$10\,\%$ davon?",
    "e3-k1-s2-v1": r"Berechne $6\,\%$ von $400$ kg.",
    "e3-k1-s2-v2": r"Berechne $9\,\%$ von $700\,€$.",
    "e3-k1-s2-v3": r"Berechne $11\,\%$ von $200$ m.",
    "e3-k1-s3-v1": r"Berechne $30\,\%$ von $90\,€$.",
    "e3-k1-s3-v2": r"Berechne $15\,\%$ von $60\,€$.",
    "e3-k1-s3-v3": r"Berechne $5\,\%$ von $140$ kg.",
    "e3-k1-s4-v1": r"Schreibe $45\,\%$ als Dezimalzahl und berechne damit "
                   r"$45\,\%$ von $80$ kg.",
    "e3-k1-s4-v2": r"Schreibe $64\,\%$ als Dezimalzahl und berechne damit "
                   r"$64\,\%$ von $150$ Personen.",
    "e3-k1-s4-v3": r"Schreibe $4\,\%$ als Dezimalzahl und berechne damit "
                   r"$4\,\%$ von $350\,€$.",
    "e3-k1-s5-v1": r"Berechne $20\,\%$ von $4{,}50\,€$.",
    "e3-k1-s5-v2": r"Berechne $30\,\%$ von $12{,}40\,€$.",
    "e3-k1-s5-v3": r"Berechne $15\,\%$ von $8{,}60$ m.",
    "e3-k1-s6-v1": r"Schuhe kosten $70\,€$. Es gibt $20\,\%$ Rabatt. Wie viel "
                   r"Euro spart man?",
    "e3-k1-s6-v2": r"Kopfhörer kosten $90\,€$. Es gibt $30\,\%$ Rabatt. Wie viel "
                   r"kosten die Kopfhörer jetzt?",
    "e3-k1-s6-v3": r"Eine Tischlampe kostet $64\,€$. Es gibt $25\,\%$ Rabatt. "
                   r"Wie viel kostet die Lampe jetzt?",
    "e3-k1-s7-v1": r"Berechne $150\,\%$ von $40$ kg.",
    "e3-k1-s7-v2": r"Berechne $120\,\%$ von $35\,€$.",
    "e3-k1-s7-v3": r"Berechne $200\,\%$ von $17$ m.",
    "e3-k1-s8-v1": r"Ein Fernseher kostet $480\,€$. Bei Barzahlung gibt es "
                   r"$15\,\%$ Rabatt. Kreuze an, wie viel Euro man spart. "
                   r"(P10 2021 OS)\\ \kreuz{$32\,€$}\\ \kreuz{$408\,€$}\\ "
                   r"\kreuz{$72\,€$}\\ \kreuz{$552\,€$}",
    "e3-k1-s8-v2": r"Eine Waschmaschine kostet $650\,€$. Im Angebot gibt es "
                   r"$30\,\%$ Rabatt. Kreuze an, wie viel Euro man spart. "
                   r"(P10 2021 OS)\\ \kreuz{$455\,€$}\\ \kreuz{$65\,€$}\\ "
                   r"\kreuz{$845\,€$}\\ \kreuz{$195\,€$}",
    "e3-k1-s9-v1": r"Berechne $17\,\%$ von $60\,€$. (P10 2014 OS)",
    "e3-k1-s9-v2": r"Berechne $19\,\%$ von $40\,€$. (P10 2014 OS)",
    "e3-k1-s9-v3": r"Berechne $40\,\%$ von $85\,€$. (P10 2026 FOR)",
    "e3-k1-s9-v4": r"Berechne $60\,\%$ von $45\,€$. (P10 2026 FOR)",
    "e3-k1-s10-v1": r"Bei einer Umfrage wurden $800$ Haushalte befragt. $35\,\%$ "
                    r"hatten ein E-Bike, sechs Jahre später $52\,\%$. Um wie "
                    r"viele Haushalte hat die Zahl zugenommen? (P10 2019 OS)",
    "e3-k2-s1-v1": r"Eine Reparatur kostet ohne Mehrwertsteuer $300\,€$. Dazu "
                   r"kommen $19\,\%$ Mehrwertsteuer. Wie viel Euro "
                   r"Mehrwertsteuer sind das?",
    "e3-k2-s1-v2": r"Bücher kosten ohne Mehrwertsteuer $40\,€$. Dazu kommen "
                   r"$7\,\%$ Mehrwertsteuer. Wie viel Euro Mehrwertsteuer sind "
                   r"das?",
    "e3-k2-s1-v3": r"Ein Laptop kostet ohne Mehrwertsteuer $800\,€$. Dazu kommen "
                   r"$19\,\%$ Mehrwertsteuer. Wie viel Euro Mehrwertsteuer sind "
                   r"das?",
    "e3-k3-s1-v1": r"Jonas soll $60\,\%$ von $35\,€$ berechnen. Er rechnet so: "
                   r"\rechnung{0{,}06 \cdot 35 &= 2{,}10\,€} " + FEHLER,
    "e3-k3-s1-v2": r"Aylin soll $20\,\%$ von $85\,€$ berechnen. Sie rechnet so: "
                   r"\rechnung{\frac{85}{20} &= 4{,}25\,€} " + FEHLER,
    "e3-k3-s1-v3": r"Ein Mantel kostet $140\,€$. Es gibt $30\,\%$ Rabatt. Tim "
                   r"soll ausrechnen, wie viel man spart. Er rechnet so: "
                   r"\rechnung{0{,}3 \cdot 140 &= 42 \\ 140 - 42 &= 98} Dann "
                   r"sagt er: „Man spart $98\,€$.“ " + FEHLER,
    "e3-k3-s2-v1": r"$1\,\%$ von $500\,€$ sind $5\,€$. Erkläre, warum.",
    "e3-k3-s2-v2": r"Erkläre, warum $6\,\%$ von $300$ genau sechsmal so viel ist "
                   r"wie $1\,\%$ von $300$.",
    "e3-k3-s2-v3": r"Ole sagt: „$20\,\%$, ein Fünftel und $\frac{20}{100}$ von "
                   r"$45\,€$ sind jedes Mal dasselbe.“ Begründe, ob Ole recht "
                   r"hat.",
    "e3-k3-s3-v1": r"Der ganze Streifen steht für $60\,€$. Zeichne $30\,\%$ im "
                   r"Streifen ein und lies ab, wie viel Euro das sind.",
    "e3-k3-s3-v2": r"Der ganze Streifen steht für $36$ kg. Zeichne $75\,\%$ im "
                   r"Streifen ein und lies ab, wie viel kg das sind.",
    "e3-k3-s3-v3": r"Der ganze Streifen steht für $500$ m. Zeichne $40\,\%$ im "
                   r"Streifen ein und lies ab, wie viele Meter das sind.",
    "e3-k3-s4-v1": r"Dieselbe Jacke kostet in Laden A $95\,€$. Dort gibt es "
                   r"$20\,\%$ Rabatt. In Laden B kostet sie $85\,€$ mit $10\,\%$ "
                   r"Rabatt. In welchem Laden ist die Jacke billiger?",
    "e3-k3-s4-v2": r"Ein Handwerker berechnet ohne Mehrwertsteuer $1\,250\,€$. "
                   r"Dazu kommen $19\,\%$ Mehrwertsteuer. Familie Kaya hat "
                   r"$1\,500\,€$ zurückgelegt. Reicht das Geld der Familie?",
    "e3-k3-s4-v3": r"Eine Schule hat $840$ Schüler. Bei einer Grippewelle fehlen "
                   r"$15\,\%$ der Schüler. Die Mensa hat $700$ Essen bestellt. "
                   r"Reicht das, wenn alle anwesenden Schüler essen?",
    # --- e4 Grundwert -------------------------------------------------
    "e4-k1-s0-v1": r"In einer Aufgabe steht: „$30\,\%$ der Klasse sind $9$ "
                   r"Kinder. Wie viele Kinder hat die Klasse?“ Kreuze an, was "
                   r"gesucht ist.\\ \kreuz{Prozentwert}\\ \kreuz{Prozentsatz}\\ "
                   r"\kreuz{Grundwert}",
    "e4-k1-s0-v2": r"In einer Aufgabe steht: „Ein Handy kostet $300\,€$, es gibt "
                   r"$12\,\%$ Rabatt. Wie viel Euro spart man?“ Kreuze an, was "
                   r"gesucht ist.\\ \kreuz{Prozentwert}\\ \kreuz{Prozentsatz}\\ "
                   r"\kreuz{Grundwert}",
    "e4-k1-s0-v3": r"In einer Aufgabe steht: „Von $240$ Befragten sagen $60$ ja. "
                   r"Wie viel Prozent sind das?“ Kreuze an, was gesucht ist.\\ "
                   r"\kreuz{Prozentwert}\\ \kreuz{Prozentsatz}\\ "
                   r"\kreuz{Grundwert}",
    "e4-k1-s0-v4": r"In einer Aufgabe steht: „$18\,€$ Rabatt sind $15\,\%$ des "
                   r"alten Preises. Wie hoch war der alte Preis?“ Kreuze an, was "
                   r"gesucht ist.\\ \kreuz{Prozentwert}\\ \kreuz{Prozentsatz}\\ "
                   r"\kreuz{Grundwert}",
    "e4-k2-s0-v1": r"Der graue Teil des Streifens ist $30\,\%$. Er hat $6$ "
                   r"Kästchen. Wie viele Kästchen hat der ganze Streifen?",
    "e4-k2-s0-v2": r"Der graue Teil des Streifens ist $50\,\%$. Er hat $7$ "
                   r"Kästchen. Wie viele Kästchen hat der ganze Streifen?",
    "e4-k2-s0-v3": r"Der graue Teil des Streifens ist $25\,\%$. Er hat $3$ "
                   r"Kästchen. Wie viele Kästchen hat der ganze Streifen?",
    "e4-k2-s0-v4": r"Der graue Teil des Streifens ist $60\,\%$. Er hat $9$ "
                   r"Kästchen. Wie viele Kästchen hat der ganze Streifen?",
    "e4-k2-s1-v1": r"$50\,\%$ einer Menge sind $35$ kg. Wie viel kg ist die ganze "
                   r"Menge?",
    "e4-k2-s1-v2": r"$25\,\%$ eines Betrags sind $12\,€$. Wie viel Euro ist der "
                   r"ganze Betrag?",
    "e4-k2-s1-v3": r"$20\,\%$ einer Strecke sind $9$ m. Wie lang ist die ganze "
                   r"Strecke?",
    "e4-k2-s1-v4": r"$10\,\%$ einer Menge sind $16$ l. Wie viele Liter sind die "
                   r"ganze Menge?",
    "e4-k2-s1-v5": r"$25\,\%$ einer Gruppe sind $30$ Kinder. Wie viele Kinder "
                   r"sind in der ganzen Gruppe?",
    "e4-k2-s2-v1": r"$3\,\%$ einer Menge sind $12$ kg. Wie viel kg ist die ganze "
                   r"Menge?",
    "e4-k2-s2-v2": r"$7\,\%$ eines Betrags sind $56\,€$. Wie viel Euro ist der "
                   r"ganze Betrag?",
    "e4-k2-s2-v3": r"$15\,\%$ einer Strecke sind $45$ m. Wie lang ist die ganze "
                   r"Strecke?",
    "e4-k2-s3-v1": r"$36\,\%$ einer Menge sind $81$ kg. Wie viel kg ist die "
                   r"ganze Menge?",
    "e4-k2-s3-v2": r"$64\,\%$ einer Strecke sind $52$ m. Wie lang ist die ganze "
                   r"Strecke?",
    "e4-k2-s3-v3": r"$12{,}5\,\%$ eines Betrags sind $17\,€$. Wie viel Euro ist "
                   r"der ganze Betrag?",
    "e4-k2-s4-v1": r"$21$ Kinder fahren mit dem Rad. Das sind $75\,\%$ der "
                   r"Klasse. Wie viele Kinder hat die Klasse?",
    "e4-k2-s4-v2": r"Im Tank sind noch $12$ l. Das sind $20\,\%$ der "
                   r"Tankfüllung. Wie viele Liter passen in den Tank?",
    "e4-k2-s4-v3": r"Ein Verein hat $54$ Jugendliche. Das sind $45\,\%$ aller "
                   r"Mitglieder. Wie viele Mitglieder hat der Verein?",
    "e4-k2-s5-v1": r"$40\,\%$ von $65$ Kindern gehen in die AG. Wie viele Kinder "
                   r"gehen in die AG?",
    "e4-k2-s5-v2": r"$14$ von $56$ Plätzen sind frei. Wie viel Prozent der Plätze "
                   r"sind frei?",
    "e4-k2-s5-v3": r"$33$ Gäste sind $55\,\%$ der Eingeladenen. Wie viele Gäste "
                   r"sind eingeladen?",
    "e4-k3-s1-v1": r"$30\,\%$ einer Menge sind $12$ kg. Sven soll die ganze Menge "
                   r"berechnen. Er rechnet so: \rechnung{0{,}3 \cdot 12 &= "
                   r"3{,}6\text{ kg}} " + FEHLER,
    "e4-k3-s1-v2": r"$50\,\%$ eines Betrags sind $24\,€$. Nora soll den ganzen "
                   r"Betrag berechnen. Sie rechnet so: \rechnung{0{,}5 \cdot 24 "
                   r"&= 12\,€} " + FEHLER,
    "e4-k3-s1-v3": r"$5\,\%$ einer Strecke sind $7$ m. Emil soll die ganze "
                   r"Strecke berechnen. Er rechnet so: \rechnung{7 \cdot 0{,}05 "
                   r"&= 0{,}35\text{ m}} " + FEHLER,
    "e4-k3-s2-v1": r"Wenn man das Ganze berechnet, rechnet man am Ende mal "
                   r"$100$. Erkläre, warum.",
    "e4-k3-s2-v2": r"$20\,\%$ sind $7\,€$. Erkläre, warum das Ganze fünfmal so "
                   r"viel ist.",
    "e4-k3-s2-v3": r"Mo sagt: „Das Ganze ist immer größer als der Prozentwert.“ "
                   r"Begründe, ob Mo recht hat.",
    "e4-k3-s3-v1": r"Der graue Teil des Streifens ist $40\,\%$. Das sind $18$ kg. "
                   r"Trage die Werte am Streifen ein und lies das Ganze ab.",
    "e4-k3-s3-v2": r"Der graue Teil des Streifens ist $75\,\%$. Das sind $60\,€$. "
                   r"Trage die Werte am Streifen ein und lies das Ganze ab.",
    "e4-k3-s3-v3": r"Der graue Teil des Streifens ist $60\,\%$. Das sind $42$ m. "
                   r"Trage die Werte am Streifen ein und lies das Ganze ab.",
    "e4-k3-s4-v1": r"Tims Handy zeigt $35\,\%$ Akku. Laut Anzeige reicht das noch "
                   r"für $7$ Stunden Musik. Wie lange hält ein voller Akku? "
                   r"Reicht er für eine Busfahrt von $18$ Stunden?",
    "e4-k3-s4-v2": r"Die Klassenfahrt ist zu $70\,\%$ bezahlt. Das sind "
                   r"$4\,200\,€$. Wie teuer ist die Klassenfahrt insgesamt? Wie "
                   r"viel Geld fehlt noch?",
    "e4-k3-s4-v3": r"Nach einem trockenen Sommer sind in einem Stausee noch $18$ "
                   r"Mio.\,m$^3$ Wasser. Das sind $45\,\%$ der Füllmenge. Wie "
                   r"viel Wasser fasst der See? Wie viel fehlt noch, bis er voll "
                   r"ist?",
    # --- e5 Veränderung -----------------------------------------------
    "e5-k1-s0-v1": r"Der Preis stieg von $2{,}40\,€$ auf $2{,}70\,€$. Welcher "
                   r"Preis ist der alte Preis?",
    "e5-k1-s0-v2": r"Jetzt hat der Verein $150$ Mitglieder. Im letzten Jahr waren "
                   r"es $120$. Welche Zahl ist der alte Wert?",
    "e5-k1-s0-v3": r"Die Miete wurde auf $690\,€$ erhöht. Vorher zahlte Familie "
                   r"Berg $600\,€$. Welcher Betrag ist der alte Wert?",
    "e5-k1-s0-v4": r"Nach dem Rabatt kostet das Rad $340\,€$. Vorher kostete es "
                   r"$425\,€$. Welcher Preis ist der alte Preis?",
    "e5-k2-s0-v1": r"Ein Preis wird um $20\,\%$ gesenkt. Kreuze an, was dasselbe "
                   r"bedeutet.\\ \kreuz{auf $20\,\%$ gesenkt}\\ \kreuz{auf "
                   r"$80\,\%$ gesenkt}\\ \kreuz{um $80\,\%$ gesenkt}",
    "e5-k2-s0-v2": r"Ein Preis wird auf $60\,\%$ gesenkt. Kreuze an, was dasselbe "
                   r"bedeutet.\\ \kreuz{um $60\,\%$ gesenkt}\\ \kreuz{um "
                   r"$40\,\%$ gesenkt}\\ \kreuz{auf $40\,\%$ gesenkt}",
    "e5-k2-s0-v3": r"Ein Preis wird um $15\,\%$ erhöht. Kreuze an, was dasselbe "
                   r"bedeutet.\\ \kreuz{auf $115\,\%$ erhöht}\\ \kreuz{auf "
                   r"$15\,\%$ erhöht}\\ \kreuz{auf $85\,\%$ erhöht}",
    "e5-k2-s0-v4": r"Ein Preis wird auf $125\,\%$ erhöht. Kreuze an, was dasselbe "
                   r"bedeutet.\\ \kreuz{um $125\,\%$ erhöht}\\ \kreuz{um "
                   r"$75\,\%$ erhöht}\\ \kreuz{um $25\,\%$ erhöht}",
    "e5-k2-s1-v1": r"Ein Preis von $80\,€$ wird um $10\,\%$ erhöht. Wie hoch ist "
                   r"der neue Preis?",
    "e5-k2-s1-v2": r"Ein Gewicht von $60$ kg wird um $25\,\%$ kleiner. Wie groß "
                   r"ist das neue Gewicht?",
    "e5-k2-s1-v3": r"Ein Dorf hat $400$ Einwohner. Es werden $5\,\%$ mehr. Wie "
                   r"viele Einwohner hat das Dorf jetzt?",
    "e5-k2-s1-v4": r"Ein Preis von $50\,€$ wird um $20\,\%$ gesenkt. Wie hoch ist "
                   r"der neue Preis?",
    "e5-k2-s1-v5": r"Ein Band ist $90$ cm lang. Es wird um $50\,\%$ verlängert. "
                   r"Wie lang ist das Band jetzt?",
    "e5-k2-s2-v1": r"Ein Preis von $45\,€$ wird um $20\,\%$ erhöht. Berechne den "
                   r"neuen Preis in einem Schritt mit einem Faktor.",
    "e5-k2-s2-v2": r"Ein Gewicht von $70$ kg wird um $20\,\%$ kleiner. Berechne "
                   r"das neue Gewicht in einem Schritt mit einem Faktor.",
    "e5-k2-s2-v3": r"Ein Preis von $260\,€$ wird um $15\,\%$ gesenkt. Berechne "
                   r"den neuen Preis in einem Schritt mit einem Faktor.",
    "e5-k2-s3-v1": r"In einer AG steigt die Zahl der Kinder von $40$ auf $50$. Um "
                   r"wie viel Prozent ist die Zahl gestiegen?",
    "e5-k2-s3-v2": r"Ein Preis sinkt von $80\,€$ auf $68\,€$. Um wie viel Prozent "
                   r"ist der Preis gesunken?",
    "e5-k2-s3-v3": r"Ein Verein wächst von $150$ auf $174$ Mitglieder. Um wie "
                   r"viel Prozent ist die Zahl der Mitglieder gestiegen?",
    "e5-k2-s4-v1": r"Nach $20\,\%$ Rabatt kostet ein Rad $360\,€$. Wie hoch war "
                   r"der alte Preis?",
    "e5-k2-s4-v2": r"Die Monatskarte wird um $10\,\%$ teurer. Jetzt kostet sie "
                   r"$66\,€$. Wie hoch war der alte Preis?",
    "e5-k2-s4-v3": r"Nach $25\,\%$ Rabatt kostet ein Mantel $105\,€$. Wie hoch "
                   r"war der alte Preis?",
    "e5-k2-s5-v1": r"Ein Gerät kostet ohne Mehrwertsteuer (netto) $200\,€$. Dazu "
                   r"kommen $19\,\%$ Mehrwertsteuer. Wie viel kostet das Gerät "
                   r"mit Mehrwertsteuer (brutto)?",
    "e5-k2-s5-v2": r"Ein Buch kostet mit $7\,\%$ Mehrwertsteuer (brutto) "
                   r"$53{,}50\,€$. Wie viel kostet es ohne Mehrwertsteuer "
                   r"(netto)?",
    "e5-k2-s5-v3": r"Ein Fahrrad kostet mit $19\,\%$ Mehrwertsteuer (brutto) "
                   r"$714\,€$. Wie viel kostet es ohne Mehrwertsteuer (netto)?",
    "e5-k2-s6-v1": r"Die Wahlbeteiligung war $58\,\%$. Später war sie $64\,\%$. "
                   r"Um wie viele Prozentpunkte ist sie gestiegen? Um wie viel "
                   r"Prozent ist sie gestiegen? " + RUNDE,
    "e5-k2-s6-v2": r"Die Arbeitslosenquote sinkt von $6\,\%$ auf $4{,}5\,\%$. Um "
                   r"wie viele Prozentpunkte ist sie gesunken? Um wie viel "
                   r"Prozent ist sie gesunken?",
    "e5-k2-s6-v3": r"Ein Zinssatz steigt von $2\,\%$ auf $3\,\%$. Um wie viele "
                   r"Prozentpunkte ist er gestiegen? Um wie viel Prozent ist er "
                   r"gestiegen?",
    "e5-k2-s7-v1": r"Eine Straße steigt auf $200$ m waagerechter Strecke um $14$ "
                   r"m. Wie groß ist die Steigung in Prozent?",
    "e5-k2-s7-v2": r"Ein Weg steigt auf $40$ m waagerechter Strecke um $3$ m. Wie "
                   r"groß ist die Steigung in Prozent?",
    "e5-k2-s7-v3": r"Eine Skipiste hat $12\,\%$ Steigung. Wie viele Meter steigt "
                   r"sie auf $250$ m waagerechter Strecke an?",
    "e5-k2-s8-v1": r"Ein Liter Milch kostete $1{,}15\,€$, jetzt kostet er "
                   r"$1{,}29\,€$. Um wie viel Prozent ist der Preis gestiegen? "
                   + RUNDE + " (P10 2026 FOR)",
    "e5-k2-s8-v2": r"Eine Kugel Eis kostete $1{,}70\,€$, jetzt kostet sie "
                   r"$1{,}90\,€$. Um wie viel Prozent ist der Preis gestiegen? "
                   + RUNDE + " (P10 2026 FOR)",
    "e5-k2-s8-v3": r"Ein Kino hatte im Mai $1\,340$ Besucher, im Juni $1\,120$. "
                   r"Um wie viel Prozent ist die Zahl gesunken? " + RUNDE
                   + " (P10 2022 OS)",
    "e5-k2-s8-v4": r"Eine Bücherei verlieh im März $860$ Bücher, im April $780$. "
                   r"Um wie viel Prozent ist die Zahl gesunken? " + RUNDE
                   + " (P10 2022 OS)",
    "e5-k2-s10-v1": r"In einer Kletterhalle zahlen Erwachsene $14\,€$ und "
                    r"Jugendliche bis $17$ Jahre $9\,€$. Familie Demir kommt mit "
                    r"Mutter, Vater, Tochter ($15$ Jahre) und Sohn ($12$ Jahre). "
                    r"Montags gibt es $15\,\%$ Rabatt. Wie viel zahlt die Familie "
                    r"am Montag? (P10 2015 OS)",
    "e5-k2-s10-v2": r"Im Theater zahlen Erwachsene $22\,€$ und Schüler $13\,€$. Es "
                    r"kommen Oma, Mutter, Vater und ein Schüler. Mit der "
                    r"Familienkarte gibt es $25\,\%$ Rabatt. Wie viel zahlen sie "
                    r"zusammen? (P10 2015 OS)",
    "e5-k2-s11-v1": r"Ein Radweg darf höchstens $5\,\%$ Steigung haben. Ergänze "
                    r"den Satz: „$5\,\%$ Steigung heißt: auf \leerfeld[m] "
                    r"waagerechter Strecke \leerfeld[m] Höhenunterschied.“ Herr "
                    r"Lenz sagt: „Ein Radweg, der auf $240$ m waagerechter "
                    r"Strecke um $15$ m ansteigt, ist zu steil.“ Prüfe mit einer "
                    r"Rechnung, ob er recht hat. (P10 2025 OS)",
    "e5-k2-s11-v2": r"Eine Garagenzufahrt darf höchstens $15\,\%$ Steigung haben. "
                    r"Ergänze den Satz: „$15\,\%$ Steigung heißt: auf $100$ m "
                    r"waagerechter Strecke \leerfeld[m] Höhenunterschied.“ Eine "
                    r"Zufahrt steigt auf $8$ m waagerechter Strecke um $1{,}1$ m "
                    r"an. Frau Roth sagt, sie sei zu steil. Prüfe mit einer "
                    r"Rechnung, ob sie recht hat. (P10 2025 OS)",
    "e5-k3-s1-v1": r"Ein Preis steigt von $60\,€$ auf $75\,€$. Ida berechnet die "
                   r"Steigerung in Prozent so: \rechnung{\frac{15}{75} &= 0{,}2 "
                   r"= 20\,\%} " + FEHLER,
    "e5-k3-s1-v2": r"Die Zahl der Besucher sinkt von $500$ auf $400$. Finn "
                   r"berechnet die Abnahme in Prozent so: "
                   r"\rechnung{\frac{100}{400} &= 0{,}25 = 25\,\%} " + FEHLER,
    "e5-k3-s1-v3": r"Ein Hund wog $20$ kg, jetzt wiegt er $23$ kg. Zoe berechnet "
                   r"die Zunahme in Prozent so: \rechnung{\frac{3}{23} &\approx "
                   r"0{,}130 = 13{,}0\,\%} " + FEHLER,
    "e5-k3-s2-v1": "Eine Preiserhöhung rechnet man immer vom alten Preis aus. "
                   "Erkläre, warum.",
    "e5-k3-s2-v2": r"Ein Preis steigt um $10\,\%$. Danach sinkt er um $10\,\%$. "
                   r"Begründe, ob er dann wieder so hoch ist wie am Anfang.",
    "e5-k3-s2-v3": r"Lara sagt: „Von $50$ auf $100$ sind $100\,\%$ mehr, also "
                   r"sind von $100$ auf $50$ auch $100\,\%$ weniger.“ Begründe, "
                   r"ob Lara recht hat.",
    "e5-k3-s3-v1": r"Ein Fahrrad kostet $600\,€$. Bei Angebot A gibt es $10\,\%$ "
                   r"Rabatt. Auf den neuen Preis gibt es noch einmal $10\,\%$. "
                   r"Bei Angebot B gibt es einmal $20\,\%$ Rabatt. Welches "
                   r"Angebot ist günstiger?",
    "e5-k3-s3-v2": r"Frau Öz verdient $2\,400\,€$ im Monat. Bei Angebot 1 bekommt "
                   r"sie $4\,\%$ mehr Lohn. Bei Angebot 2 bekommt sie $90\,€$ "
                   r"mehr im Monat. Welches Angebot ist für sie besser? Ab "
                   r"welchem Lohn wären beide gleich gut?",
    "e5-k3-s3-v3": r"Eine Jeans kostet $80\,€$. Laden A erhöht den Preis um "
                   r"$25\,\%$. Dann gibt Laden A $20\,\%$ Rabatt auf den neuen "
                   r"Preis. Laden B lässt den Preis gleich. In welchem Laden ist "
                   r"die Jeans billiger?",
    # --- Zone ---------------------------------------------------------
    "zone-f1-v1": r"In einer Tüte sind $10$ Bonbons. $6$ davon sind rot. "
                  r"Schreibe den Anteil der roten Bonbons als Bruch und kürze "
                  r"ihn.",
    "zone-f1-v2": r"Erweitere den Bruch $\frac{7}{10}$ auf den Nenner $100$.",
    "zone-f1-v3": r"$6$ von $15$ Plätzen sind besetzt. Schreibe den Anteil der "
                  r"besetzten Plätze als Bruch, kürze ihn und erweitere auf "
                  r"Hundertstel.",
    "zone-f1-v4": r"Im Korb liegen $3$ grüne und $9$ rote Äpfel. Schreibe den "
                  r"Anteil der grünen Äpfel als Bruch und kürze ihn.",
    "zone-f1-v5": r"Erweitere den Bruch $\frac{9}{20}$ auf den Nenner $100$.",
    "zone-f2-v1": r"Schreibe $\frac{1}{2}$ als Dezimalzahl.",
    "zone-f2-v2": r"Schreibe $0{,}9$ als Bruch.",
    "zone-f2-v3": r"Schreibe $\frac{3}{25}$ als Dezimalzahl.",
    "zone-f2-v4": r"Schreibe $\frac{7}{100}$ als Dezimalzahl.",
    "zone-f2-v5": r"Schreibe $0{,}4$ als Bruch und kürze ihn.",
    "zone-f3-v1": r"Berechne. $\frac{600}{100}$",
    "zone-f3-v2": r"Berechne. $0{,}1 \cdot 70$",
    "zone-f3-v3": r"Berechne. $0{,}15 \cdot 60$",
    "zone-f3-v4": r"Berechne. $\frac{45}{100}$",
    "zone-f3-v5": r"Berechne. $0{,}06 \cdot 50$",
    "zone-f4-v1": r"$2$ Kinokarten kosten $18\,€$. Berechne mit der Tabelle, wie "
                  r"viel $5$ Kinokarten kosten.",
    "zone-f4-v2": r"$4$ kg Äpfel kosten $12\,€$. Berechne mit der Tabelle, wie "
                  r"viel $3$ kg Äpfel kosten.",
    "zone-f4-v3": r"$5$ Brötchen kosten $2\,€$. Berechne mit der Tabelle, wie "
                  r"viel $3$ Brötchen kosten.",
    "zone-f4-v4": r"$100$ Schrauben wiegen $400$ g. Berechne mit der Tabelle, wie "
                  r"viel $7$ Schrauben wiegen.",
    "zone-f4-v5": r"$3$ kg Kartoffeln kosten $6\,€$. Berechne mit der Tabelle, "
                  r"wie viel kg Kartoffeln man für $10\,€$ bekommt.",
    "zone-f5-v1": r"Runde $4{,}73$ auf eine Stelle nach dem Komma.",
    "zone-f5-v2": r"Runde $8{,}26$ auf eine Stelle nach dem Komma.",
    "zone-f5-v3": r"Runde $18{,}456$ kg auf eine Stelle nach dem Komma.",
    "zone-f5-v4": r"Runde $6{,}97$ auf eine Stelle nach dem Komma.",
    "zone-f5-v5": r"Runde $2{,}349$ auf eine Stelle nach dem Komma.",
    "zone-f6-v1": r"Berechne $\frac{1}{4}$ von $20\,€$.",
    "zone-f6-v2": r"Berechne $\frac{1}{2}$ von $36$ kg.",
    "zone-f6-v3": r"Berechne $\frac{3}{5}$ von $45$ m.",
    "zone-f6-v4": r"Von $48\,€$ ist ein Viertel ausgegeben. Wie viel Euro sind "
                  r"noch übrig?",
    "zone-f6-v5": r"Berechne $\frac{1}{5}$ von $6{,}50\,€$.",
    "zone-f6-v6": r"Von $40\,€$ ist ein Fünftel ausgegeben. Ben soll ausrechnen, "
                  r"wie viel Euro übrig sind. Er rechnet: $\frac{40}{5} = 8$. "
                  r"Dann sagt er: „Übrig sind $8\,€$.“ " + FEHLER,
    "zone-f6-v7": r"Im Tank sind $30$ Liter. Ein Drittel davon ist verbraucht. "
                  r"Wie viele Liter sind noch übrig?",
}

ZAHL = re.compile(r"\d+(?:\{,\}\d+)?")


def zahlen(t):
    """Zahlen einer aufgabe als Multimenge; Tausenderabstand „\\,“ zwischen
    Ziffern wird zusammengezogen, Bausteinnamen und Befehle zählen nicht."""
    t = re.sub(r"(\d)\\,(\d)", r"\1\2", t)
    t = re.sub(r"\\[A-Za-z]+", " ", t)
    return collections.Counter(ZAHL.findall(t))


def lauf():
    geaendert, fehler = {}, []
    gefunden = set()
    for p in sorted(BANK.glob("*.jsonl")):
        zeilen = p.read_text(encoding="utf-8").splitlines()
        aus = []
        for l in zeilen:
            z = json.loads(l)
            k = z["id"][len(P):]
            if k in NEU:
                gefunden.add(k)
                neu = NEU[k]
                za, zn = zahlen(z["aufgabe"]), zahlen(neu)
                if (za - zn) or (set(zn) - set(za)):
                    fehler.append(f"{k}: Zahlen alt {dict(zahlen(z['aufgabe']))}"
                                  f" neu {dict(zahlen(neu))}")
                if neu != z["aufgabe"]:
                    geaendert.setdefault(p.name, []).append(k)
                    z["aufgabe"] = neu
            aus.append(json.dumps(z, ensure_ascii=False))
        p.write_text("\n".join(aus) + "\n", encoding="utf-8")
    fehlt = set(NEU) - gefunden
    if fehlt:
        fehler.append("nicht in der Bank: " + ", ".join(sorted(fehlt)))
    for f in fehler:
        print("FEHLER", f)
    for n, ks in sorted(geaendert.items()):
        print(f"{n}: {len(ks)} geändert")
    return 1 if fehler else 0


if __name__ == "__main__" and "--bericht" not in sys.argv:
    sys.exit(lauf())


BASIS = "d86851d"   # Bankstand vor dem Sprachlauf


def bericht():
    """bau/sprachlauf/prozentrechnung.md: Zählung je Datei und 25 Beispiele
    (je Sprosse die erste geänderte Zeile, gleichmäßig über alle Sprossen)."""
    zaehl, sprossen = [], {}
    for p in sorted(BANK.glob("*.jsonl")):
        rel = p.relative_to(WURZEL).as_posix()
        alt = subprocess.run(["git", "show", f"{BASIS}:{rel}"], cwd=WURZEL,
                             capture_output=True, text=True,
                             check=True).stdout.splitlines()
        neu = p.read_text(encoding="utf-8").splitlines()
        g = 0
        for a, n in zip(alt, neu):
            a, n = json.loads(a), json.loads(n)
            if a["aufgabe"] != n["aufgabe"]:
                g += 1
                k = (p.name, a["kette_nr"], a["sprosse"])
                sprossen.setdefault(k, (a, n))
        zaehl.append((p.name, g, len(neu) - g, len(neu)))
    keys = sorted(sprossen, key=lambda k: (k[0] != "zone.jsonl", k))
    n = 25
    wahl = [keys[round(i * (len(keys) - 1) / (n - 1))] for i in range(n)]
    z = ["# Sprachlauf prozentrechnung",
         "",
         f"Stand 2026-09-28. Regeln: bau/sprachlauf/regeln.md. Skript:",
         "bau/sprachlauf/sprachlauf_prozentrechnung.py (alle neuen Texte",
         f"stehen dort). Vergleich gegen den Bankstand {BASIS}. Nur das Feld",
         "aufgabe ist geändert; `python3 werkzeuge/bank-pruef.py",
         "prozentrechnung`: 0 Abweichungen, 0 Warnungen.",
         "",
         "## Zählung",
         "",
         "| Datei | geändert | unverändert | Zeilen |",
         "| --- | --: | --: | --: |"]
    for name, g, u, s in zaehl:
        z.append(f"| {name} | {g} | {u} | {s} |")
    z.append(f"| gesamt | {sum(x[1] for x in zaehl)} | "
             f"{sum(x[2] for x in zaehl)} | {sum(x[3] for x in zaehl)} |")
    z += ["", f"Geänderte Sprossen: {len(sprossen)}. Die 25 Beispiele sind je",
          "Sprosse die erste geänderte Zeile, gleichmäßig über die Sprossen",
          "verteilt (Zone zuerst, dann e1–e5).", "", "## 25 Beispiele", ""]
    for i, k in enumerate(wahl, 1):
        a, nn = sprossen[k]
        z += [f"{i}. `{a['id']}` – {a['sprosse_text'][:60].rstrip()}",
              "", f"   vorher: {a['aufgabe']}", "",
              f"   nachher: {nn['aufgabe']}", ""]
    (WURZEL / "bau" / "sprachlauf" / "prozentrechnung.md").write_text(
        "\n".join(z).rstrip() + "\n", encoding="utf-8")
    print("bau/sprachlauf/prozentrechnung.md geschrieben")


if __name__ == "__main__" and "--bericht" in sys.argv:
    bericht()

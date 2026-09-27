# Gegenlese: lineare-gleichungen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung)
Geprüfte Zeilen: 199 (zone 28, e1 48, e2 47, e3 36, e4 40)
Korrekturen: 0
Grundlage: Aufgaben selbst nachgerechnet (Python/sympy); bank.md für die Felder; mappen/lineare-gleichungen.md für Sprossenfolge, Schreibform und Typische Fehler.

## Befunde

### 1 Lösung und pruef
lineare-gleichungen-e2-k4-s4-v3: Die Lösung sagt, beim Malnehmen mit 0 „verliert die Gleichung ihre Lösung“. Das ist schief: Die alte Lösung erfüllt 0 = 0 weiterhin, nur ist jetzt jede Zahl Lösung, die Lösungsmenge ändert sich also – Vorschlag: „Dann steht 0 = 0 da, und das ist für jede Zahl wahr. Die neue Gleichung hat andere Lösungen als die alte, die Umformung ändert die Lösung.“
### 2 Eindeutigkeit und Angaben
lineare-gleichungen-e2-k1-s0-v2: Bei $\frac{x}{3} = 7$ ist auf „was steht bei x?“ auch $\frac{1}{3}$ eine richtige Antwort (die Kette nennt die Sprosse selbst „Vorzahl als Bruch“), die Lösung lässt nur $:3$ gelten – Vorschlag: loesung „$:3$ (x wird durch 3 geteilt; auch $\frac{1}{3}$ richtig)“.
lineare-gleichungen-e4-k2-s1-v1: a und b werden nicht erklärt (anders als G, h, V in v2 und s, v, t in v3) – Vorschlag: „Flächeninhalt $A$ eines Rechtecks mit den Seitenlängen $a$ und $b$: …“.
### 3 Sprosse und Merkmal
lineare-gleichungen-e2-k3-s7-v3: Die Aufgabe verlangt nur eine Gleichung mit einer Mal-Rechnung (einschrittig), v1 und v2 dagegen eine zweischrittige. Die Variante ändert damit die Struktur und nicht nur die Zahlen – Vorschlag: „Eine zweischrittige Gleichung mit der Lösung 10?“ (etwa $3x - 4 = 26$).
lineare-gleichungen-e2-k4-s4-v2: Die Frage betrifft die Reihenfolge der Umformungen (erst −3, dann :5). Das Merkmal verlangt aber die Begründung, warum dieselbe Umformung auf beiden Seiten die Lösung nicht ändert – Vorschlag: Begründungsfrage zum Merkmal, etwa „Warum darf man bei $3x = 21$ beide Seiten durch 3 teilen?“.
lineare-gleichungen-e3-k2-s1-v1: $0{,}5x + 1{,}2 = 3{,}7$ hat x nur links, v2 und v3 dagegen x auf beiden Seiten. Die Varianten unterscheiden sich damit in der Struktur – Vorschlag: auch v1 mit x beidseitig (etwa $0{,}8x + 1{,}5 = 0{,}3x + 4$).
lineare-gleichungen-e4-k1-s6-v5, lineare-gleichungen-e4-k1-s6-v6, lineare-gleichungen-e4-k1-s6-v7, lineare-gleichungen-e4-k1-s6-v8: Das Merkmal sagt „… und lösen“. Die Originale 2016-OS-B1b und 2021-OS-B1e verlangen aber nur das Angeben bzw. Ankreuzen der Gleichung, ohne Lösen und ohne Klammer. Ihr Anspruch liegt auf Höhe von Sprosse 1 bzw. 3 und damit unter den Sprossen 4–5 – Vorschlag: das Merkmal für diese Zeilen ohne „und lösen“ fassen oder in stand.md als Katalogfolge vermerken (vier Originale an einer Prüfungshöhe, zwei davon mit dem Typ „Term zu Sachtext angeben“ aus terme.md).
### 4 Schreibform
lineare-gleichungen-e4-k1-s5-v1, lineare-gleichungen-e4-k1-s5-v2, lineare-gleichungen-e4-k1-s5-v3: Die Aufgabe verlangt „gegeben, gesucht, Formel, Rechnung“, die Lösung zeigt nur die Rechnung – Vorschlag: in der loesung die Formelzeile ergänzen ($U = 2 \cdot (a + b)$; $\alpha + \beta + \gamma = 180^\circ$; Umfang = Basis + 2 · Schenkel), dazu kurz gegeben/gesucht.
### 5 Ankreuzen
keine
### 6 Fehler finden
lineare-gleichungen-e1-k4-s2-v1: Die Aufgabe verrät den Fehler selbst („Eine Probe macht sie nicht.“), zu finden bleibt nichts. Eine Rechnung in der Schreibform des Verfahrens fehlt – Vorschlag: den Hinweissatz streichen und Miras Ergebnis als Zeile zeigen („Mira: Lösung von $4x + 6 = 30$ ist $x = 9$.“), Auftrag „Finde den Fehler und prüfe“.

## Entscheidungen

- pruef bei Ankreuzen mit Gleichungen als Optionen (e1-k2-s5-v1/v2, e4-k1-s1-v1–v5, e4-k1-s6-v7/v8): bank.md verlangt dort "", die Zeilen tragen eine Zahl aus der Lösung. Das ist harmlos, bank-pruef lässt es zu, und kein Leser des Blatts sieht es. Ebenso tragen die Terme der Zone (z. B. $5x + 4$) und die Sonderfälle in e3 als pruef nur die erste Zahl an der Ergebnisstelle, e4-k1-s6-v3/v4 nur die erste von zwei gefragten Anzahlen (32 statt [32, 128], 40 statt [40, 200]). Beides nicht als Befund gezählt: Die Werte stimmen, bank-pruef folgt dieser Übung.
- e1-k2-s5-v3/v4 (Original 2022-OS-B1c): Die richtige Lösung ist positiv (7 bzw. 6), die Sprosse heißt „mit negativer Zahl“. Die negativen Zahlen stecken in den Seitenwerten (−17, −15) und im Distraktor −7, wie im Original. Kein Befund.
- e2-k3-s8 (Prüfungshöhe mit Klammer und bei v5/v6 mit Dezimalzahl): Klammer und Dezimalzahl kommen in der Kette von Einheit 2 vorher nicht vor. Die Zielmarke des Katalogs verlangt aber ausdrücklich die Klammer (2020-OS-B1e, 2023-OS-B1e, 2024-OS-B1d), und die Klammer wird als Block behandelt. Kein Befund.
- Varianten mit anderem Format an einer Prüfungshöhe (zwei Originale je Sprosse, je 2 Zeilen) sind Absicht von bank.md („2 je Original“) und zählen nicht als Merkmalsbruch. Befund 3 zu e4-k1-s6 betrifft nur das Merkmal „und lösen“.
- x als Unbekannte in vielen Aufgaben einer Einheit: Jede Aufgabe erklärt x („$x$: …“) bzw. es ist die Unbekannte der Gleichung. Nicht als Verstoß gegen „ein Buchstabe je Einheit für eine Sache“ gewertet.

Sauber: 185 Zeilen ohne Befund

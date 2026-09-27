# Gegenlese: grenzwerte-und-verhalten-im-unendlichen

Datum: 2026-09-27
Modell: Claude (Claude Code, Web-Sitzung), unabhängige Gegenlese
Geprüfte Zeilen: 136 (zone 31, e1 36, e2 42, e3 27)
Korrekturen: 0

Alle Grenzwerte, Vorzeichen, Annäherungsseiten, Nullstellen,
Funktionswerte und Ableitungen mit Python/sympy aus der Aufgabe
nachgerechnet; bank-pruef.py: 0 Abweichungen.

## Entscheidungen

- Korrigiert wird nur eine falsche Zahl mit eindeutiger Korrektur;
  Widersprüche zwischen Kontext und Deutung stehen unter Punkt 2.

## Befunde

### Punkt 1 – Lösung rechnerisch richtig

keine

### Punkt 2 – eindeutig lösbar

- grenzwerte-und-verhalten-im-unendlichen-e2-k1-s5-v3: Kontext „Nach dem Einschalten einer Heizung“ widerspricht der Deutung „das Rohr kühlt auf Dauer auf 18 °C ab“ – Kontext ändern, etwa „Nach einem kurzen Heizstoß …“.
- grenzwerte-und-verhalten-im-unendlichen-e3-k2-s3-v3: „Welche Geschwindigkeit erreicht er höchstens?“ setzt ein Maximum voraus, die Lösung sagt „wird nie ganz erreicht“ – „Welcher Geschwindigkeit nähert er sich auf Dauer, und was bedeutet das?“.

### Punkt 3 – passt zu sprosse_text und merkmal

- grenzwerte-und-verhalten-im-unendlichen-zone-f1-v5: keine negative Basis ($x = 10$), die Fertigkeit ist „Potenzen … bei negativer Basis“ – $x = -10$ einsetzen lassen ($(-10)^4 = 10\,000$, $50 \cdot (-10)^2 = 5000$) oder einen Fallstrick dieser Fertigkeit nehmen.
- grenzwerte-und-verhalten-im-unendlichen-e2-k1-s4-v3: fragt nur $x \to -\infty$ (Seite, auf der $e^{x}$ verschwindet), das Merkmal verlangt das Vorzeichen auf der wachsenden Seite; zudem form text statt teil wie v1/v2 – wie v1/v2 beide Richtungen fragen ($x \to +\infty$: $f(x) \to -\infty$).

### Punkt 4 – Schreibform

- grenzwerte-und-verhalten-im-unendlichen-e1-k1-s0-v3: verlangt in Einheit 1 (ganzrationale Funktionen), dass $e^{-x}$ gegen $x^2 + 1$ gewinnt – das kommt erst in e2 – durch ein ganzrationales Beispiel ersetzen (etwa $100x^2 - x^3$) oder nach e2 verschieben.

### Punkt 5 – Ankreuzen

keine

### Punkt 6 – Fehler finden

keine

Sauber: 131 Zeilen ohne Befund

# Gegenlese: ableitungsregeln

Datum: 2026-09-27  
Modell: Claude in Claude Code (Web-Sitzung); die genaue Modellkennung darf laut Sitzungsvorgabe nicht ins Repo, sie steht im Chatbericht  
Geprüfte Zeilen: 138  
Korrekturen: 0

## Festlegungen dieser Gegenlese

- Jede Zeile einzeln nachgerechnet (Python mit sympy/scipy), aus dem Aufgabentext; bank.md nur für die Felder, stand.md nicht gelesen.
- Korrigiert wird nur, wenn loesung selbst rechnerisch falsch ist und die Korrektur eindeutig in loesung/pruef liegt. Ein unvollständiges pruef bei richtiger loesung ist ein Befund unter Punkt 1, keine Korrektur.
- Widerspricht die Lösung einer Grafik oder dem Aufgabentext und ließe sich das an Aufgabe, Grafik oder Lösung beheben, ist die Korrektur nicht eindeutig: Befund, keine Änderung.
- Korrigierte Zeilen stehen unter Punkt 1 mit „korrigiert“ und zählen nicht als sauber. Eine Zeile mit mehreren Befunden steht unter jedem Punkt einmal.

## Befunde

### 1 Lösung und pruef

- keine

### 2 Eindeutig lösbar

- ableitungsregeln-e3-k2-s2-v3: f, g und a werden im Text nicht eingeführt; der Term g'(a) erscheint ohne Herkunft – Voranstellen: „Für differenzierbares f ist g(x) = f(x) · e^x, also g'(x) = (f'(x) + f(x)) · e^x.“

### 3 Sprosse und Merkmal

- ableitungsregeln-e2-k1-s4-v3: Anders als v1/v2 muss erst f aus f' und f(1) rekonstruiert werden (Aufleiten von e^(6x)); dieser Schritt steht weder im Merkmal noch in der Kette – f direkt angeben wie in v1/v2, oder die Rekonstruktion als eigene Sprosse bzw. im Merkmal führen
- ableitungsregeln-e3-k1-s3-v3: Zusätzlich zum Nachweis wird der Extrempunkt berechnet; v1/v2 und das Merkmal verlangen nur den Nachweis der vorgegebenen Form – Extrempunkt ins Merkmal aufnehmen oder in allen Varianten verlangen bzw. hier streichen

### 4 Schreibform

- ableitungsregeln-e1-k2-s9-v2: Wegen f'(2) = 0 braucht der Nachweis des Tiefpunkts das f''-Kriterium; die Sprosse prüft laut Katalog und Original nur über f'(x₀) – Zahlen so wählen, dass f'(x₀) ≠ 0 ist (wie Original 2024-B-1d), oder nur fragen, ob P als Extrempunkt in Frage kommt

### 5 Ankreuzen

- keine

### 6 Fehler finden

- ableitungsregeln-e2-k3-s1-v3: Kims Fehler (Potenzregel auf e^(5x) angewandt) ist keines der genannten Muster; „als wäre der Exponent ein Vorfaktor“ beschreibt ihn unzutreffend – Fehlerbenennung präzisieren: Exponent 5x vorgezogen und um 1 verringert wie bei x^n; oder Fehler passend zu einem Katalogmuster wählen

Sauber: 133 Zeilen ohne Befund

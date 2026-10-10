# Plan: Winkel berechnen (Trigonometrie, Lerneinheit 2)

Bau 10.10.2026 nach `bau/bauauftrag.md`, Kennung LT3, Standardlage:
Klasse 10 (OS), sicher ist Lerneinheit 1 (Seiten vom Winkel aus
benennen, sin, cos, tan aufstellen, Seite mit mal oder geteilt),
unsicher bei Neuem, allein, Ziel P10.

## 1 Rückwärts von den Zielaufgaben (P10)

| Zielaufgabe (Katalog, Prüfungsform) | braucht |
|---|---|
| Seilbahn: cos β1 = 255 : 384 (2024-OS-K6b) | Seil = Hypotenuse, Bodenstrecke = Ankathete; Umkehrtaste (A, B) |
| Nachweis cos α = 4/9, „also rund 64°“ (2019-OS-K3b) | Antwortsatz beim Nachweis (C, T) |
| Winkel im Teildreieck mit der Höhe (2022-OS-K5b) | Teildreieck finden, Höhe als Kathete (C, T) |
| Winkel im Parallelogramm (2026-FOR-K4b) | Höhe zeichnet das Dreieck, cos⁻¹ (C) |
| Rampe: erst Seite, dann tan α (2025-OS-K4a) | Seite oder Winkel gesucht? (D, T) |

Darunter: rechter Winkel → H; vom gesuchten Winkel aus G und A → die
zwei bekannten Seiten wählen die Funktion → Bruch → Umkehrtaste →
runden, Grad. Neu gegenüber 1 ist nur die Umkehrtaste; schwer ist die
Entscheidung, ob umgestellt oder umgekehrt wird.

## 2 Lernweg (Folge im Heft)

| Kennung | Abschnitt | Grund für die Stelle |
|---|---|---|
| A | Winkel aus zwei Seiten | sin⁻¹ → cos⁻¹ → tan⁻¹ → andere Lage (Falle: Katheten beim Tangens vertauscht) |
| B | Steigungswinkel in Sachen | schräg = Hypotenuse, waagerecht = Ankathete; zweiter Winkel 90° − α |
| C | Winkel in Figuren und Nachweis | Höhe, Koordinatensystem, Parallelogramm; „rund …“ |
| D | Seite oder Winkel? | mischt, was 1 getrennt übte (mal, geteilt), mit der Umkehrtaste |
| T | Probetest | je Rechenart: cos⁻¹ ankreuzen (A), sin⁻¹ Seilbahn (B), Höhe mal + Nachweis (C, D), tan⁻¹ und geteilt (D) |

Ziele (Modell selbst finden, Antwortform wechselt): A Steht die Leiter
sicher (Bereich)? B Welche Straße ist steiler, um wie viel? C Hat Mia
recht (Behauptung prüfen)? D Wie lang mindestens, ist der Winkel
erlaubt? T Um wie viel ist der Schatten länger?

## 3 Änderungen gegenüber dem Katalog

- **Gestrichen fürs Blatt:** Vorstufe „Seite oder Winkel ankreuzen,
  nichts rechnen“ (D1 erkennt und rechnet zugleich), Umkehrtaste als
  eigene Stufe (Formel A), Fehler finden, Begründen (Lehrer 09.10.).
- **Winkel im Teildreieck und Nachweis** in Lerneinheit 2 (Katalog
  Typen Einheit 2), nicht erst in 3.
- **„Seite oder Winkel?“ als eigener Abschnitt** D vor dem Probetest
  (Thema-Weg ergänzt).
- Formelkasten S. 1 ohne die Regel aus D; jeder Hinweis steht einmal
  (SHIFT nur in A, DEG nur bei den Fehlern, 90° − α nur in B).

## 4 Feste Zahlen (sympy, `pruef` in der Bank)

A: 5/8 → 38,7°; 3/6 → 30°; cos 7/10 → 45,6°; tan 4/7 → 29,7°;
tan 9/6 → 56,3°; Leiter cos 1,2/4 → 72,5° (zwischen 65° und 75°).
B: 1,20/2,50 → 28,7°; Treppe 17/29 → 30,4°; Seilbahn 320/450 → 44,7°;
Mast 9/12 → 48,6°, 41,4°; Straßen 5,1° gegen 5,7° → 0,6°.
C: 4/7 → 34,8°; tan 5/4 → 51,3°; Koordinaten 4/6 → 33,7°;
cos 2,5/6,5 → 67,4°; Rechteck 22,6° und 67,4°.
D: 9 sin 40° ≈ 5,8; sin⁻¹(4/9) ≈ 26,4°; 10 cos 35° ≈ 8,2; tan 5/8 →
32,0°; 6 : sin 50° ≈ 7,8; cos⁻¹(5/8) ≈ 51,3°; 8 cos 50° ≈ 5,1;
5 : tan 32° ≈ 8,0; Rampe 0,40 : sin 6° ≈ 3,83 m, tan 0,40/3,50 → 6,5°.
T: cos⁻¹(s/t); 230/410 → 34,1°; h = 6 sin 53° ≈ 4,79, β ≈ 32,2°;
Schatten 36,9°, 1,80 : tan 25° ≈ 3,86 m, 1,46 m länger.

## 5 Form

Gesetzt mit `werkzeuge/setzer.py trigonometrie 2` aus dem Lernweg-Block
LT3 (Katalog, Form abschnitte), Sorten selbst und tisch-alt. Skizzen aus
einem Skript (Maße aus den Zahlen, Beschriftung neben der Linie).

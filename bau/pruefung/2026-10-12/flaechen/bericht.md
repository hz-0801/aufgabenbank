# Blatt P Flächen aus Daten (12.10.2026) – Kennung H37
Bau: `python3 werkzeuge/pruefheft.py --kapitel flaechen --art p --einheit
"Flächeninhalt und Umfang" --datum 2026-10-12`; PDFs unter pdf/. Blatt
2 Seiten (Karo 0,5), Lösung 2, Übersicht 1; kein „SETZER: fehlt“, keine
LaTeX-Fehler; jede Lösung mit Python nachgerechnet (Anzeige „Fläche und
Umfang“). Je Stufe Schülerfrage + Einstieg + echte (echte in Klammern):
- Formel zur Figur: 1 + 1 + 1 (2025-1i Gleichung ankreuzen)
- Fläche oder Umfang berechnen: 1 + 1 + 2 (2026-1h Rechteck, 2024-4a Kreis)
- Seite aus Fläche oder Umfang: 1 + 1 + 1 (2023-1c Rechteckseite)
- Figur erst zerlegen: 1 + 1 + 1 (2023-2c Trapezumfang über sin, Stern)
- Anteil in Prozent: 1 + 0 + 1 (2025-1e Kreissektor); Einstieg entfällt
Zusammen 15 Aufgaben, 6 echte; 19 weitere Originale im Mehr-Block.
Ergänzte Daten: gliederung/flaechen.md Anzeigenamen, je Stufe Anzeigename,
Schülerfrage, -Fälle, -Form, -Weg (Format wie koerper.md);
zuordnung-flaechen.csv neu erzeugt (2025-OS-B1e nach „Anteil in Prozent“
wie die Gliederung seit 10.10.); mehr-p10.csv Zeilen flaechen: grafik für
8 Originale (TikZ zu den neuen Zahlen), form, auf_blatt = ja für 6,
2025-OS-B1e Stufe nachgezogen, drei Lösungen in Setzerform.
Setzer (Art p, Nachzug): Einstieg nur aus der ersten Sprosse, entfällt auf
Prüfungshöhe; form linie; Ankreuzen neben Skizze zeilenweise; Antwortfeld
des Einstiegs ungeteilt; Lösungs-Parser (Klammer-Term, Geteiltzeichen).
Offen (bau/befunde-M3.md): Einstieg für „Anteil in Prozent“; Reihenfolge
bei gleicher Schwere; Gruppenzeile bei einer Einheit; wegen Länge im
Mehr-Block: 2022-1e, 2025-2b, 2020-7b, 2018-6a. mehr-pruef.py meldet
2022-OS-K2a-m1 (koerper, fremde Zeile): Teilergebnisse 2 pruef / 3 loesung.

# Runde 13.10. Schritt B – Wachstum (Exponentielles Wachstum, 74A)

Einheit Exponentielles Wachstum: Blatt aus Daten, 2 Seiten, Setzer meldet
nichts als fehlend; endet mit der schwersten echten (’26 · 7b, Niveau III).
- Blatt: alle fünf Originale 2022–2026 (’26 · 7a, 7b, 7c; ’25 · 7a, 7b) mit
  den neuen Zahlen aus mehr-p10 (590 €, 2,3 %; 70 Bakterien, Faktor 1,3),
  auf_blatt = ja. Vorher lagen alle auf nein, der Setzer zog 19 ältere aufs
  Blatt (5 Seiten). Die älteren bleiben im Mehr-Block.
- Stufen nach dem Gesuchten: Tabelle ergänzen · Graph zeichnen · Faktor und
  Gleichung gesucht · Graph zuordnen (Anzeigenamen; Stufennamen der Zuordnung
  unverändert). Buchstufen Faktor / Gleichung / Wert nach n Jahren bleiben
  eine Stufe, weil die Originale sie in einer Teilaufgabe fragen.
- Tabellen, Koordinatensystem (Bakterien, 0–5 h, 0–250) und die drei
  Graphen A/B/C als TikZ in der Spalte grafik; Antwortfelder per form.
Heranführungen (neu, zwei; Stolperstein pruefung.md § 2):
- vor Tabelle ergänzen: Prozentsatz → Faktor (5 % → 1,05; 2,3 % → 1,023).
  Der Schüler übt, dass 2,3 % nicht 1,23 wird, bevor er die Miete fortschreibt.
- vor Faktor und Gleichung: Quotient (200 → 210: Faktor 1,05, 5 %), damit er
  in ’25 · 7b „zeige, dass der Faktor 1,3 ist“ als Teilen erkennt.
- Graph zeichnen und Graph zuordnen ohne Heranführung.
Gerechnet mit sympy: 590 · 1,023^k (603,57; 617,45; 631,65), 590 · 1,023^14
≈ 811,17; 70 · 1,3^24 ≈ 37996; Quotienten 1,297–1,305.
Wünsche an den Setzer:
- Bei Tabelle mit Leerzelle (form einzeichnen+karo) kommt das Karo voll
  (4 Zeilen); für zwei Lücken reichen die Zellen, Karo ist überflüssig.
- Koordinatensystem neben einer Tabelle geht nur über minipage im grafik-
  Feld; ein Baustein „Tabelle links, ksys rechts“ wäre sauberer.
- Overfull 5 im Blatt (vermutlich Tabellenbreite); nicht sichtbar.
Offen an den Lehrer:
- „Zeit bis Verdopplung oder Schwelle“ (2016, 2018, 2020) hat keine Stufe im
  Zuschnitt; in fünf Jahren kein Original – so lassen?
- „Wachstumsart begründen“ (2016-K4d, 2018-K2b) steht nur als Hauptplatz in
  der Tabelle, ohne Zeile im Mehr-Block.

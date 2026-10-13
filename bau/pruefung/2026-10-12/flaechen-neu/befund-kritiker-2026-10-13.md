# Kritiker: Fläche und Umfang (Y5D2), Runde 6, 13.10.2026
Grundlage: bericht.md, src/*.tex, pdf/ (alle Seiten gesehen), pruefung.md § 5, gemeinsam.md
„Satz“, „Zahlen“, „Lösungen“; Originalwerte aus msa-katalog-*.csv, Plätze aus handgriffe-p10.csv.

## 1 Fachliche Fehler: 0
Mit sympy nachgerechnet, alles stimmt: ½ · 56 · 96 = 2688 cm²; 625π ≈ 1963,5 cm²;
(24,20 + 16,20) : 2 · 7,50 = 151,5 m²; DB = 7,3 : tan 49° ≈ 6,35 m, A ≈ 63,3 m²; 2 · 7 = 14 cm;
Schenkel 8,49 m (sin) bzw. genau 8,50 m (Pythagoras 4,00 und 7,50), u ≈ 57,4 m; 38 500 : 350 = 110;
125 : 360 ≈ 34,7 %; 14 Deckel, Abfall 700 − 171,5π ≈ 161,2 cm² ≈ 23,0 % ≤ 24 %. Alle Zahlen weichen
vom Original ab, gleicher Typ und gleiche Schwere (Deckel: wieder abrunden, 100 : 7). Figuren passen:
Trapez gezeichnet 61°, Dreieck β 49°, Verhältnisse nirgends umgekehrt, Sektor wirklich 125°.

## 2 Schwere Befunde: 2
- Nr. 11 trägt „Basis · ohne TR“, aber 125 : 360 ≈ 34,7 % rechnet niemand im Kopf. Der Schüler
  übt so, an der Aufgabe zu scheitern, die er in der Prüfung ohne Rechner glatt lösen muss
  (pruefung.md „Neue Zahlen der Basis gehen im Kopf“). Ein Winkel wie 144° (40 %) oder 126° (35 %)
  hält Typ und Schwere des Originals (145°). Platz: neutral. (Daten: msa/mehr-p10.csv, Zeile
  2025-OS-B1e-m1: wortlaut, grafik, loesung, pruef)
- Zweitthema nicht ausgeblendet: Nr. 7 verlangt erst DB = h : tan 49°, Nr. 9 erst den Schenkel mit
  sin 62° – beides ist Dreiecke-Handwerk (handgriffe-p10.csv: Zwischenschritt dreiecke:Seite
  berechnen). Wer am Tangens hängt, übt auf dem Flächenblatt keine Fläche; die Regel will genau das
  trennen und die ganze Mischung aufs Gemischt-Blatt Geometrie legen. Die herausgelöste Fassung
  2022-OS-K5e-h2 liegt bereit, der Setzer nahm trotzdem m1 – und h2 trägt noch die Originalzahlen
  (h 7,4 m, c 17,8 m), müsste also die Zahlen von m1 bekommen (c ≈ 17,35 m, h 7,3 m). Für 9 fehlt
  eine Fassung mit „Schenkel 8,50 m“. Folge: 7 und 9 sinken auf Stufe I; das Blatt endet weiter mit
  Nr. 12 auf Prüfungshöhe. Gegenstimme: gliederung/flaechen.md nennt bei „Umfang gesucht“ bewusst
  „eine Seite, die erst berechnet wird“ – das widerspricht der Regel; der Lehrer sollte das einmal
  entscheiden. Platz: spart (Karo 3 → 2 zweimal, rund 2 cm). (Daten: msa/herausgeloest-p10.csv,
  gliederung/flaechen.md; Setzer: Wahl m1 statt h2 in werkzeuge/pruefheft.py)

## 3 Leichte Befunde: 7
- Lösung Nr. 1 nennt links „u = 3 · a“ statt des Buchstabens C; bei Nr. 2 steht „C“. Der Lehrer
  prüft Ankreuzen am Buchstaben (gemeinsam.md „Buchstaben vor Optionen“). Platz: neutral. (Daten:
  mehr-p10.csv loesung 2024-OS-B1c-m1)
- Rechte Lösungsspalte wiederholt bei 1, 3 und 8 nur das Ergebnis. Der Schüler, der falsch lag,
  braucht den Ansatz: „drei gleiche Seiten: a + a + a“, „Katheten d und e: d · e : 2“,
  „2 · (4,5 + 2,5)“. Bei 9 fehlt der Überstand (24,20 − 16,20) : 2 = 4,00 – der Schritt, an dem
  er hängt. Platz: neutral. (Daten: mehr-p10.csv loesung)
- Lösung links nicht in der Form der Frage: Nr. 7 fragt nur A, links steht auch DB; Nr. 12 fragt
  „überprüfe“, links gehört das Urteil „Ja, eingehalten (≈ 23,0 % ≤ 24 %)“. Bei 12 bricht zudem
  „%“ allein in die nächste Zeile. Platz: neutral. (Daten: mehr-p10.csv; Umbruch: Setzer)
- „Anteil in Prozent“ steht als „oft · 25 · 23“, der Deckel ’23 · 5c hat seinen Hauptplatz aber
  im Kapitel Prozent; gezählt werden nur Hauptplätze, also „selten · 25“. Sonst glaubt der Schüler,
  die Kreisanteile kämen jedes zweite Jahr. Platz: neutral. (Setzer: pruefheft.py, Jahre im Kopf)
- Nr. 10: Skizzenfeld und 2 cm Karo für eine Kopfrechnung in einem Schritt (Rechteck, Breite
  gegeben). Zu skizzieren ist kaum etwas (gemeinsam.md „Skizzenfeld“, Grenze); eine Antwortzeile
  reicht. Bei Nr. 8 hat die Skizze ein Warum (vier Seiten sehen statt a + b), dort bleibt sie.
  Ein kürzeres Nr. 10 passt auf Seite 2, die jetzt ein Viertel leer endet. Platz: spart ~2 cm.
  (Daten: mehr-p10.csv form 2023-OS-B1c-m1)
- Anstoß „Formeln umstellen“ ist fast wörtlich das Beispiel der Regel und nimmt dem einzigen
  Original den ganzen Handgriff ab – danach bleibt nur Einsetzen. Besser fragt er nach dem Weg
  („Welche Rechnung macht aus der Fläche wieder eine Seite?“), ohne a = vorzugeben. Platz: neutral.
  (Daten: gliederung/flaechen.md, Frage)
- Figuren tragen die Maße nicht: Trapez 6/9 ohne 24,20, 16,20, 7,50; Dreieck 7 zeigt 11,0 m, aber
  nicht h_c. Der Schüler rechnet an der Figur (Skizze in Geometrie); stehen die Längen dort, kann der
  Text kürzer werden. Platz: neutral bis spart. (Daten: mehr-p10.csv grafik)

## 4 Stufen
Fünf Stufen nach dem Gesuchten, jede mit eigenem ersten Schritt: Formel erkennen · Formel aus der
Sammlung, einsetzen · Seiten zusammenzählen · Formel rückwärts · Teil durch Ganzes. Mehr als ein
Original hat jede im Bestand; auf dem Blatt hat „Formeln umstellen“ nur eins (’23 · B1c), die
übrigen liegen zu Recht im Mehr-Block. „Anteil in Prozent“ trägt nur ein Original mit Hauptplatz;
sie lebt vom Deckel als Nebenplatz – vertretbar, solange der Kopf das ehrlich zählt (Befund oben).
Leicht → schwer in jeder Stufe (4–7: I, I, I, II; 8–9: I, II; 11–12: I, III); die Rücksprünge auf
I sind die Basisaufgaben am Platz ihrer Stufe, so gewollt. Das Blatt endet mit Nr. 12 (III) auf
Prüfungshöhe. Formelsammlungs-Anstoß bei „Fläche gesucht“ statt „Formeln“ ist richtig begründet
(Basis ohne Formelsammlung); der Teil-Ganzes-Anstoß passt zu 11, für 12 liegt die Stolperstelle
eher beim Abrunden der Deckelzahl – kein Befund, solange er kurz bleibt.

## 5 Gesamturteil: Note 2
Fachlich sauber, Figuren stimmen, alle zwölf jungen Originale mit neuen Zahlen und klarer
Stufenfolge; das Blatt ist als Prüfungstraining brauchbar. Zu beheben vor dem Lehrer: Nr. 11 mit
kopfrechenbarem Winkel und die Entscheidung über das Zweitthema in 7 und 9. Länge: Alle Behebungen
zusammen sparen etwa 4 cm (Zweitthema ~2 cm, Nr. 10 ~2 cm), aus 2,4 werden rund 2,2 Textseiten –
das Blatt bleibt bei 3 Seiten; Seite 3 trüge dann nur noch „Anteil in Prozent“ und die Fundstellen.

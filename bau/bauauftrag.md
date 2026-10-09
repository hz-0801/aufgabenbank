# Bauauftrag – eine Lerneinheit von oben bauen

Stand 09.10.2026 (plan.md Linie 2). Für jeden Agenten oder Chat, der eine
Lerneinheit baut. Handwerk (Satz, Zahlen, Lösungen, Sprache): `bau/bauregeln.md`.
Zeilenform der Bank: `bank.md`. Wörter: `mathe-nachhilfe/begriffe.md`.
Muster eines gelungenen Baus: `bau/proben/2026-10-08/hypotenuse-berechnen/`
(K4W, Lehrer 09.10. „besser“).

## Zweck

Der Schüler soll nach dem Blatt die Aufgaben der Lerneinheit bis
Prüfungshöhe lösen können; der Lehrer sitzt daneben. Gebaut wird wie ein
erfahrener Mathelehrer und Didaktiker: erst der Weg, dann die Aufgaben.
Das Ergebnis wird zerlegt zurückgelegt (Lernweg in den Katalog, Aufgaben in
die Bank), damit spätere Blätter ohne Modell gesetzt werden.

## Für wen du baust

Für einen Schüler der Klasse, die der Katalog an der Einheit nennt. Er kann
die Voraussetzungen aus dem Katalog, ist bei Neuem unsicher und will am Ende
die Zielaufgabe schaffen – sie ist sein Test. Daraus folgt: anfangen mit
etwas, das er kann; wenig Text, ein klarer Satz je Schritt; erst Erfolg,
dann Stolperstelle; der Weg führt sichtbar zur Zielaufgabe. Ob er allein
arbeitet (Selbstlernheft) oder mit dem Lehrer am Tisch (Blatt), entscheidet
erst die Sorte beim Setzen; der Bau legt für beides an (Lehrer 09.10., aus
dem Befund Selbstlernheft Geraden: `mathe-nachhilfe/befund-selbstlernheft-2026-10-09.md`).

## Eingaben – sparsam lesen

Lies nur, was der Bau braucht, nie ganze große Dateien:
- Katalogeintrag `mathe-nachhilfe/katalog/<eintrag>.md`: die Zeile der
  Lerneinheit unter „Lerneinheiten“, ihre Zeile unter „Typen je
  Lerneinheit“, „Typische Fehler“, ihre Kette unter „Sprossen je
  Verfahrenstyp“, „Prüfungsform“ (mit grep/awk herausschneiden).
- Bankzeilen der Einheit `bank/<eintrag>/e<n>.jsonl` mit einem kurzen
  Python-Filter: je Zeile nur id, sprosse_text, aufgabe (gekürzt), original,
  sache/darstellung, falls gesetzt. Nicht die ganze Datei ausgeben.
- Originale: Gliederung `mathe-nachhilfe/msa/gliederung/` (bzw. abitur/) für
  die Stufen und Originale der Einheit; Wortlaut nur der gewählten Originale.
- Nicht lesen: `quellen/`, Mappen (sie dienen dem Füllen der Bank, nicht
  dem Bau), alte Prompts, Archiv.

## Ablauf

1. **Uhr:** Startzeit mit `date` notieren.
2. **Lernweg (5–7 Schritte).** Rückwärts von der Zielaufgabe planen: Welche
   Prüfungsaufgabe (Original) ist die Decke, welche Merkmale hat sie, und
   welcher Schritt bereitet jedes Merkmal vor? Je Schritt: was der Schüler
   begreift, wo er stolpert (aus „Typische Fehler“). Folge nach der Sache,
   nicht nach der Bank-Kette (die ist teils falsch geordnet).
3. **Aufgaben je Schritt.** Erst in der Bank suchen; die beste nehmen, wenn
   sie dem Schritt dient. Sonst neu schreiben. Je Schritt die Aufgaben für das Blatt
   und zusätzlich, nur für die Bank (Lehrer 09.10.: „unbedingt, gerne auch
   mehr“): mindestens eine leichtere Aufgabe (Einstieg unten: Vorstufe,
   kleinere Zahlen, mehr aufgedeckt) und mindestens zwei gleichwertige mit
   anderen Zahlen oder anderer Sache; bei Rechenschritten und Päckchen
   mehr. Sie werden mitgeprüft und in den Lernweg-Block eingetragen.
   Zusätzlich je Schritt: die Formel oder der Merksatz in einer Zeile und
   ein kurzes vorgerechnetes Beispiel (eine Bankzeile); beides druckt nur
   das Selbstlernheft. In Päckchen „die fehlende Seite“ statt der Größe,
   die die Überschrift schon nennt; wo zwei Verfahren getrennt geübt wurden,
   mischt die folgende Einheit sie.
4. **Blatt setzen.** Mit `werkzeuge/setzer.py`, sobald es ihn gibt; bis
   dahin von Hand nach dem Muster K4W mit `mathblatt.sty` (Raw-URL
   https://raw.githubusercontent.com/hz-0801/blattbau/main/mathblatt.sty). Drei
   PDFs: Übersicht, Blatt, Lösungen. Bilder der Seiten einmal ansehen.
5. **Prüfen.** Jede Zahl mit sympy; neue Bankzeilen mit
   `werkzeuge/bank-pruef.py <eintrag>`; Dubletten mit `werkzeuge/duplikate.py`.
6. **Kritiker.** Ein zweiter Agent (Fable) ohne diese Datei, nur mit dem
   Zweck oben und den PDFs; höchstens 400 Wörter, die drei wichtigsten
   Änderungen. Übernehmen, was dem Zweck dient; Abweichungen begründen.
7. **Zerlegen.** Fehlt im Katalogeintrag der Abschnitt „Thema-Weg“, lege
   ihn beim ersten Bau des Themas an: Folge der Lerneinheiten mit Grund für
   die Stelle, Vorher-Check (Voraussetzungen, Zone-ids), Probetest (ids von
   Originalen, gemischt, schwerste zuletzt); spätere Baue ergänzen ihn.
   Lernweg als Block in den Abschnitt „Lernweg“ des
   Katalogeintrags (Form: `katalog/_vorlage.md`). Gewählte und neue Aufgaben
   vollständig in die Bank: Text, Skizze als TikZ im Feld grafik (ganz, nicht
   nur ein Name), Lösung, pruef – so, dass der Setzer das Blatt ohne die
   .tex-Datei wieder setzen kann; dazu die Lernweg-Felder (`bank.md`, „Felder für den
   Lernweg“), status gut; schwächere Zeilen desselben Schritts schwach mit
   Grund und besser. Kennung und ids ins Register `bau/register.csv`.
8. **Uhr und Bericht.** Endzeit mit `date`; Bericht (unten). Befunde, die
   über diese Einheit hinausgehen, in `bau/befunde-M<n>.md`, nicht in eine
   Regel.

## Was ein guter Lernweg tut

- Jede Stufe ändert gegenüber der vorigen genau ein Merkmal (Zahl,
  Darstellung, Fragerichtung, Sache); reine Zahlwechsel kommen ins Päckchen.
- Erkennen und Aufstellen vor dem Rechnen, ohne Zahl als Ergebnis.
- Jede Nummer beginnt beim einfachsten Fall ihrer Art.
- Ein neuer Schritt darf in a) grau vorgerechnet stehen; b) rechnet der
  Schüler.
- Runden, krumme Zahlen, Einheiten erst nach allen Denkschritten.
- Die Idee sichtbar machen, wo der häufigste Fehler sonst unerklärt bleibt
  (Beispiel: Kästchenbild gegen c = a + b).
- Sache: Sie trägt die Mathematik. Über die ganze Einheit nie zweimal
  dasselbe Modell und nie dreimal dieselbe Darstellung; die Sachaufgaben
  steigern, wie viel der Schüler selbst sehen muss (fertige Skizze → Bild
  ohne Figur → Karte → nur Text).
- Antwortform und Fragerichtung wechseln (Länge, Unterschied, Entscheidung);
  bei Ja/Nein beide Antworten vorkommen lassen.
- Verfremdetes Original behält die Falle des Originals.
- Prüfungsblatt: am Ende ein echtes Original ganz. Lernblatt: Originale
  nur, wo sie die beste Aufgabe sind, ohne Sätze, die nur der Prüfung
  dienen.
- Kurz: so lang, wie der Weg es braucht.

Nicht: Fehleraufgabe als Pflicht, Vollständigkeit vor Lernweg, Original am
Ende jeder Nummer, vorgegebene Antwortform („c² = __“), Grundfall vier- bis
fünfmal, Merkkasten, feste Stückzahlen, „im Zweifel voller“.

## Bericht (höchstens 250 Wörter)

Modell · Start/Ende (date) · Lernweg in Schritten (je eine Zeile) · Zahl der
Aufgaben aus der Bank / neu / als schwach markiert · Prüfskripte (Meldungen)
· Kritiker: übernommen / nicht übernommen mit Grund · Kennung · Commits.

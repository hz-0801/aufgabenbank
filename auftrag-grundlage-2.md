# Auftrag: bank.md nachziehen, Prüfskript schärfen, Mappen bauen

Modell: Opus. Web-Sitzung, Repo aufgabenbank. Kurz, eine Sitzung,
vier Commits. Grund: Der Prüfstein prozentrechnung (bank/
prozentrechnung/stand.md, 17 Entscheidungen) hat gezeigt, was
bank.md nicht regelt, und die Sitzung hat drei Viertel ihrer
Kosten mit dem Lesen der Quellen verbraucht. Die nächsten
Sitzungen sollen je Eintrag nur eine Mappe lesen.

## Teil 1: bank.md nachziehen (Commit „bank: Regeln nach Prüfstein")

In bank.md ergänzen, in den Worten von stand.md, ohne Neues:
- Abschnitt „Mengen je Kette": Erkennungsschritt 4 Zeilen (eigene
  Kette, nur Sprosse 0, einmal in der ersten Einheit seines
  Bereichs); Typ ohne Kette 3 Zeilen als eine Sprosse mit hoehe
  sprosse; je Zone ein Paar aus Fehler finden und gleichartiger
  Rechenaufgabe (2 Zeilen, hoehe pflicht, pflicht fehler bzw.
  sprosse) zum häufigsten Fallstrick.
- Abschnitt „Reihenfolge je Datei": Erkennungsschritte →
  Verfahrenskette des Katalogs → Typen ohne Kette →
  Pflichtelemente als eigene Kette mit dem Namen der
  Verfahrenskette. kette_nr zählt in dieser Folge.
- Abschnitt „Felder": Entscheidungen 9 bis 14 von stand.md als
  Regeln (pflicht nur bei hoehe pflicht; loesung LaTeX-fähig;
  pruef ungerundet, Brüche als Liste; form streifenfeld/
  streifenleer; antwort trägt das Gerüst; Prüfkennung vor den
  Ankreuzoptionen).
- Neuer Abschnitt „Quellen je Sitzung": Eine Sitzung liest nur
  mappen/<eintrag>.md (Teil 3) und bank.md; Katalog, Anleitung,
  Prompt und CSV liest sie nicht selbst. Grund: Kosten.
- Neuer Abschnitt „Befunde": Was eine Sitzung am Katalog, an
  bank.md oder am Prüfskript für falsch hält, steht in stand.md
  unter „Befunde"; sie ändert es nicht.
- Aus bank/quadratische-funktionen/stand.md: Sperre mit Ausnahme –
  frei sind der Gegenstand der Kette und die Form, die der
  Sprossentext selbst nennt (x², 2x², (x − d)² + e als Form);
  gesperrt bleiben konkrete Zahlbelegungen aus Kasten und
  Original (etwa (x − 3)² + 1), Zahlenpaare und Ergebnisse.
  Neues Feld loesungsgrafik ("" oder Bausteinaufruf) für
  Skizzieraufgaben, deren Lösung nicht durch zwei bis drei
  Punkte beschreibbar ist. Feld papier kommt aus der Spalte
  papier der Prüfungsdatei; das Beispiel in bank.md („FOR" zu
  einer OS-Kennung) berichtigen.

## Teil 2: Prüfskript schärfen (Commit „werkzeuge: bank-pruef v0.2")

werkzeuge/bank-pruef.py:
- Zahlenvergleich: jede pruef-Zahl muss einer Zahl der Lösung
  entsprechen, die an der Ergebnisstelle steht – Lösungen tragen
  das Ergebnis als erste Zahl oder nach „=" bzw. „≈"; eine
  Übereinstimmung mit irgendeiner Zahl im Text genügt nicht.
  Nach Rundung auf die Stellen der Lösung, Toleranz 0,005.
- Ankreuzaufgaben (form ankreuzen): die Lösungszahl muss unter
  den \kreuz-Optionen der Aufgabe stehen, genau einmal.
- Mengen aus bank.md je Kette prüfen (Vorstufe 4, Grundfall 5,
  Sprosse 3, Prüfungshöhe 2 je Original, Erkennungsschritt 4,
  Typ ohne Kette 3, Zone-Paar 2); Abweichung ist ein Befund
  (Warnung), kein Fehler.
- Bausteinprobe aus der Sitzung prozentrechnung ins Skript:
  jeder \Baustein in aufgabe, loesung, grafik, loesungsgrafik
  steht in mappen/_bausteine.md (Teil 3) mit passender
  Argumentzahl.
- Grafikprobe (Befund quadratische-funktionen): bei ksys-Grafiken
  liegt jeder Punkt, den loesung oder pruef als Zahlenpaar nennt,
  und jeder Scheitel einer \parabel innerhalb von xmin..xmax und
  ymin..ymax; Zeilen mit form zeichnen oder dem Wort „Graph" in
  aufgabe haben ein nichtleeres grafik.
- Doppelprüfung über aufgabe und grafik zusammen (falls noch nicht
  so).
- Sperrprobe ins Skript: kein Zahlenpaar und keine Gleichung aus
  den Abschnitten Merkkasten, Typische Fehler und den Originalen
  der Mappe in aufgabe.
Gegenprobe: `python3 werkzeuge/bank-pruef.py prozentrechnung`
und `… quadratische-funktionen` – Zahl der Abweichungen und
Warnungen je Datei in den Bericht; die jsonl werden nicht
geändert (Befund, kein Eingriff).

## Teil 3: Mappen bauen (Commit „werkzeuge: mappe.py, Mappen")

werkzeuge/mappe.py <eintrag> baut mappen/<eintrag>.md aus dem Netz
(Raw-URLs hz-0801/mathe-nachhilfe und hz-0801/blattbau, main):
1. Kopf: Eintrag, Katalog-Commit (GitHub-API, letzter Commit auf
   der Datei), Datum.
2. Der Katalogeintrag vollständig, mit Zeilennummern am
   Zeilenanfang (für das Feld quelle), ohne die Abschnitte
   „Status", „Offene Punkte" und „Prüfliste".
3. Originale: aus msa/msa-katalog-kontext.csv, -basis.csv,
   -gym.csv (und fhr/fhr-katalog.csv, abitur/abi-katalog.csv,
   abitur/iqb-katalog.csv, wenn der Eintrag Kennungen daraus
   nennt) je Kennung, die im Eintrag unter „Prüfungsform" oder
   „Zielmarke" steht, die Spalten id, jahr, papier, punkte,
   gegeben, gesucht, verfahren, fehlerquelle, format, antwort –
   nur diese Zeilen.
4. Maßstab: aus unterrichtsblatt.md die Abschnitte 2.2, 2.3 c,
   2.4 b–c, 3.6 wortgleich.
Dazu einmal mappen/_bausteine.md: aus Anleitung_mathblatt.md alle
Zeilen, die mit `\` oder `\begin{` beginnen (die Kurzreferenz,
etwa 150 Zeilen), plus die Absätze zu \anweisung, \rechenplatz,
beispiel, \streifenfeld, \swz. Mappen bauen für:
lineare-funktionen, quadratische-gleichungen, lineare-gleichungen,
terme, bruchrechnung, pythagoras. Zahl der Zeilen je Mappe in
den Bericht.

## Teil 4: Eintragsauftrag als Datei (Commit „auftrag: Vorlage")

auftrag-eintrag.md in der Wurzel: der Auftrag prozentrechnung
(archiv, falls dort; sonst aus stand.md rekonstruiert), umgestellt
auf: Quellen nur mappen/<eintrag>.md, mappen/_bausteine.md,
bank.md; Vergleichsblätter entfallen; Schritte: Mappe lesen,
Zone, Einheiten nacheinander, je Einheit eine Datei in einem
Schreibvorgang, Prüfskript, Commit, Push; stand.md mit Zahlen,
Entscheidungen, Befunden; Bericht wie beim Prüfstein. Platzhalter
<eintrag>. Regeln: keine Rückfrage, nur unter bank/<eintrag>/
schreiben, `git pull --rebase` vor jedem Push.

## Bericht

Im Chat: Modell; je Teil eine Zeile; Prüfskript-Ergebnis für die
zwei vorhandenen Einträge (Abweichungen, Warnungen, je Datei);
Zeilen je Mappe; letzte Zeile „gepusht auf main, Commit <hash>".

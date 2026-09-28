# Prüfungshefte nach Themen

Stand: siehe Commit „bau/hefte: elf Prüfungshefte“. Rezept H (werkzeuge/zusammenbau.py v0.4, `--heft`, `--nur-basis`), Vorlage mathblatt.sty aus hz-0801/blattbau, gerendert mit bau/hefte/render.py (xelatex, je Dokument zwei Läufe, höchstens 3 Versuche je Heft). Diese Datei baut bau/hefte/bericht.py.

## Übersicht

HN Hauptnummern; Anlauf und Prüfungshöhe in Teilaufgaben; Seiten des Hefts und der Lösungen (pdfinfo); Originale: verschiedene Originalkennungen hinter den Prüfungshöhen; Punkte: Summe der Katalogpunkte dieser Originale (in Klammern, wie viele Punkte tragen) – jedes Original steht in der Bank verfremdet meist zweimal, die Summe zählt es einmal; ⋆ Teilaufgaben mit Sternchen (OS-Original mit stern = ja, nur FOR).

| Heft | Kennung | Einträge | HN | Anlauf | Prüfungshöhe | Seiten | Lösungen | Originale | Punkte | ⋆ | ausgelassen |
| --- | --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| msa-funktionen | LIN-H1 | 6 | 55 | 77 | 180 | 34 | 5 | 82 | 206 (82) | 76 | 3 |
| msa-geometrie | FLA-H1 | 9 | 67 | 90 | 176 | 44 | 7 | 89 | 189 (89) | 35 | 0 |
| msa-daten | DAT-H1 | 2 | 17 | 19 | 50 | 11 | 4 | 43 | 88 (43) | 15 | 1 |
| msa-zahlen | BRU-H1 | 10 | 72 | 95 | 236 | 31 | 6 | 107 | 174 (107) | 30 | 4 |
| basis-zahlen | BRU-H2 | 9 | 27 | 0 | 139 | 14 | 3 | 60 | 61 (60) | 2 | 4 |
| basis-geometrie | FLA-H2 | 6 | 14 | 0 | 46 | 13 | 1 | 27 | 29 (27) | 0 | 0 |
| basis-rest | LIN-H2 | 4 | 7 | 0 | 19 | 6 | 1 | 13 | 13 (13) | 0 | 2 |
| abi-gk-analysis-1 | AEN-H1 | 7 | 65 | 72 | 153 | 29 | 9 | 108 | 414 (108) | 0 | 0 |
| abi-gk-analysis-2 | STA-H1 | 5 | 39 | 42 | 104 | 17 | 5 | 62 | 257 (62) | 0 | 0 |
| abi-gk-stochastik | ZUF-H1 | 7 | 58 | 71 | 95 | 23 | 6 | 61 | 192 (61) | 0 | 1 |
| abi-gk-geometrie | PUN-H1 | 10 | 99 | 107 | 336 | 44 | 22 | 206 | 643 (206) | 0 | 0 |

## Je Heft

### msa-funktionen (LIN-H1)

Aufruf: `zusammenbau.py lineare-funktionen quadratische-funktionen quadratische-gleichungen lineare-gleichungssysteme potenz-exponentialfunktionen zuordnungen --heft msa`

Versuche: 2, Fehlerstellen je Versuch [3, 0]; fehlende Zeichen im PDF: 13 (ä ≈).

Ausgelassen:
- Nr. 39a potenz-exponentialfunktionen-e2-k2-s0-v1 – LaTeX Error: There's no line here to
- Nr. 12b quadratische-funktionen-e1-k1-s10-v2 – LaTeX Error: There's no line here to end.
- Nr. 12a quadratische-funktionen-e1-k1-s10-v1 – LaTeX Error: There's no line here to end.

### msa-geometrie (FLA-H1)

Aufruf: `zusammenbau.py flaechen koerper pyramide-kegel-kugel pythagoras trigonometrie kreis winkel-dreiecke strahlensaetze symmetrie-abbildungen --heft msa`

Versuche: 1, Fehlerstellen je Versuch [0]; fehlende Zeichen im PDF: 85 (α β γ δ ₁ ≈).

### msa-daten (DAT-H1)

Aufruf: `zusammenbau.py daten wahrscheinlichkeit --heft msa`

Versuche: 2, Fehlerstellen je Versuch [1, 0]; fehlende Zeichen im PDF: 27 (ß ö ü).

Ausgelassen:
- Nr. 5b daten-e2-k2-s11-v2 – Dimension too large.

### msa-zahlen (BRU-H1)

Aufruf: `zusammenbau.py bruchrechnung brueche-dezimalzahlen prozentrechnung zinsrechnung rationale-zahlen potenzen-wurzeln einheiten terme lineare-gleichungen binomische-formeln --heft msa`

Versuche: 2, Fehlerstellen je Versuch [6, 0]; fehlende Zeichen im PDF: 0.

Ausgelassen:
- Nr. 22h brueche-dezimalzahlen-e5-k2-s9-v8 – LaTeX Error: Command \item invalid in math m
- Nr. 22g brueche-dezimalzahlen-e5-k2-s9-v7 – Missing $ inserted.
- Nr. 20d brueche-dezimalzahlen-e4-k1-s8-v4 – LaTeX Error: Command \item invalid in math m
- Nr. 20c brueche-dezimalzahlen-e4-k1-s8-v3 – Missing $ inserted.

Folgefehler, Teilaufgabe allein fehlerfrei, bleibt: brueche-dezimalzahlen_a.tex Nr. 22i.

### basis-zahlen (BRU-H2)

Aufruf: `zusammenbau.py bruchrechnung brueche-dezimalzahlen prozentrechnung zinsrechnung rationale-zahlen potenzen-wurzeln einheiten terme lineare-gleichungen binomische-formeln --heft msa --nur-basis`

Ohne Prüfungshöhe im Profil, daher nicht im Heft: binomische-formeln.
Versuche: 2, Fehlerstellen je Versuch [6, 0]; fehlende Zeichen im PDF: 0.

Ausgelassen:
- Nr. 9h brueche-dezimalzahlen-e5-k2-s9-v8 – LaTeX Error: Command \item invalid in math m
- Nr. 9g brueche-dezimalzahlen-e5-k2-s9-v7 – Missing $ inserted.
- Nr. 8d brueche-dezimalzahlen-e4-k1-s8-v4 – LaTeX Error: Command \item invalid in math m
- Nr. 8c brueche-dezimalzahlen-e4-k1-s8-v3 – Missing $ inserted.

Folgefehler, Teilaufgabe allein fehlerfrei, bleibt: brueche-dezimalzahlen_a.tex Nr. 9i.

### basis-geometrie (FLA-H2)

Aufruf: `zusammenbau.py flaechen koerper pyramide-kegel-kugel pythagoras trigonometrie kreis winkel-dreiecke strahlensaetze symmetrie-abbildungen --heft msa --nur-basis`

Ohne Prüfungshöhe im Profil, daher nicht im Heft: pyramide-kegel-kugel, pythagoras, strahlensaetze.
Versuche: 1, Fehlerstellen je Versuch [0]; fehlende Zeichen im PDF: 22 (α β γ ≈).

### basis-rest (LIN-H2)

Aufruf: `zusammenbau.py lineare-funktionen quadratische-funktionen quadratische-gleichungen lineare-gleichungssysteme potenz-exponentialfunktionen zuordnungen daten wahrscheinlichkeit --heft msa --nur-basis`

Ohne Prüfungshöhe im Profil, daher nicht im Heft: lineare-gleichungssysteme, potenz-exponentialfunktionen, zuordnungen, daten.
Versuche: 2, Fehlerstellen je Versuch [2, 0]; fehlende Zeichen im PDF: 0.

Ausgelassen:
- Nr. 3b quadratische-funktionen-e1-k1-s10-v2 – LaTeX Error: There's no line here to end.
- Nr. 3a quadratische-funktionen-e1-k1-s10-v1 – LaTeX Error: There's no line here to end.

### abi-gk-analysis-1 (AEN-H1)

Aufruf: `zusammenbau.py ableitung-und-aenderungsrate ableitungsregeln kurvenuntersuchung tangente-normale-schnittwinkel funktionsklassen-und-eigenschaften grenzwerte-und-verhalten-im-unendlichen extremalprobleme --heft abitur-gk`

Versuche: 1, Fehlerstellen je Versuch [0]; fehlende Zeichen im PDF: 0.

### abi-gk-analysis-2 (STA-H1)

Aufruf: `zusammenbau.py stammfunktion-und-hauptsatz integrationsregeln flaecheninhalt-durch-integration rekonstruktion-von-funktionsgleichungen rekonstruktion-von-bestaenden gleichungen-loesen rotationsvolumen --heft abitur-gk`

Ohne Prüfungshöhe im Profil, daher nicht im Heft: integrationsregeln, rotationsvolumen.
Versuche: 1, Fehlerstellen je Versuch [0]; fehlende Zeichen im PDF: 9 (∫ ≈).

### abi-gk-stochastik (ZUF-H1)

Aufruf: `zusammenbau.py zufallsexperimente-und-pfadregeln bedingte-wahrscheinlichkeit-und-bayes vierfeldertafel unabhaengigkeit zufallsgroessen-und-verteilungen kenngroessen-von-verteilungen binomialverteilung hypothesentests --heft abitur-gk`

Ohne Prüfungshöhe im Profil, daher nicht im Heft: hypothesentests.
Versuche: 2, Fehlerstellen je Versuch [6, 0]; fehlende Zeichen im PDF: 0.

Ausgelassen:
- Nr. 56b binomialverteilung-e5-k1-s1-v1 – Extra }, or forgotten $.

Folgefehler, Teilaufgabe allein fehlerfrei, bleibt: binomialverteilung_a.tex Nr. 56c.

### abi-gk-geometrie (PUN-H1)

Aufruf: `zusammenbau.py punkte-und-strecken-im-koordinatensystem vektoren-und-rechenoperationen geraden ebenen lagebeziehungen schnittmengen abstaende skalarprodukt-und-winkel orthogonalitaet flaecheninhalt-und-volumen-im-raum --heft abitur-gk`

Versuche: 1, Fehlerstellen je Versuch [0]; fehlende Zeichen im PDF: 1 (≈).

## Die häufigsten Fehler nach Baustein

Gezählt je ausgelassener Teilaufgabe und Heft (eine Bankzeile in zwei Heften zählt zweimal; in Klammern die Zahl verschiedener Bankzeilen). Der Baustein ist der erste Vorlagenbaustein der Zeile (Grafik vor Text) oder der Lückensatz.

1. Lückensatz: __ im Aufgabentext (Unterstrich außerhalb Mathe): 8× (4 Bankzeilen: brueche-dezimalzahlen-e4-k1-s8-v3, brueche-dezimalzahlen-e4-k1-s8-v4, brueche-dezimalzahlen-e5-k2-s9-v7, brueche-dezimalzahlen-e5-k2-s9-v8; Meldung: LaTeX Error: Command \item invalid in math m / Missing $ inserted)
2. \wertetabelle (form ankreuzen): 5× (3 Bankzeilen: potenz-exponentialfunktionen-e2-k2-s0-v1, quadratische-funktionen-e1-k1-s10-v1, quadratische-funktionen-e1-k1-s10-v2; Meldung: LaTeX Error: There's no line here to / LaTeX Error: There's no line here to end)
3. \saeulenab (form zeichnen): 1× (1 Bankzeilen: daten-e2-k2-s11-v2; Meldung: Dimension too large)
4. \saeulenab (form teil): 1× (1 Bankzeilen: binomialverteilung-e5-k1-s1-v1; Meldung: Extra }, or forgotten $)

## Entscheidungen dieses Laufs

1. Prüfungshöhe = jede Bankzeile, deren Original (sonst die Prüfkennung
   im Text) zum Profil des Hefts gehört, gleich welche hoehe. Grund: in
   Sek II stehen die meisten Originale an Sprossen mitten in der Kette
   (GK: 170 Zeilen hoehe pruefung, 535 an grundfall/sprosse). Zeilen
   hoehe pruefung ohne Original und ohne Prüfkennung (Zielmarken) sind
   nicht im Heft, weil sie keine Prüfkennung tragen.
2. Profile: msa = Papier OS, FOR, EBR, GYM („(P10 Jahr Papier)“);
   abitur-gk = Papier mit -ga oder -gk (iqb grundlegend auch MMS, be-gk,
   bebb-gk, bb-gk; „(Abitur Jahr GK)“). FHR und LK bleiben draußen.
3. Anlauf je Kette: Vorstufe, Grundfall und eine Sprosse, je kleinste
   Variante ohne Original; Prüfkennung entfernt. Die Bank zählt
   Fallstricke nicht nach Häufigkeit; genommen wird die erste Sprosse
   nach dem Grundfall, deren Merkmal einen Fallstrick nennt (Fallstrick,
   Falle, Fehler, verwechseln, vertauschen, Vorzeichen, Klammer,
   Sonderfall, negativ, Null), sonst die erste Sprosse nach dem
   Grundfall. Die Wahl steht je Kette in der zusammenbau.log (AUSWAHL).
4. Ketten ohne Prüfungshöhe im Profil fehlen ganz (auch ohne Anlauf);
   Einträge ganz ohne stehen oben je Heft. Die Pflichtkette zählt zur
   gleichnamigen Verfahrenskette.
5. Sternchen: \steil bzw. \sgl, wenn das Original im Katalog stern = ja
   trägt (OS-Hefte bis 2025, nur FOR); Legende in der Fußzeile. Abitur
   und GYM tragen keine Sternchen.
6. Basis (5–7): Original mit Papier OS, FOR oder EBR und Kennung
   -<Papier>-B<n> (Basisteil), ohne Anlauf.
7. Kennung H<n> über bau/register.csv (Rezept H aus v0.3); die
   Registerzeilen sind die einzige Schreibstelle außerhalb von
   bau/hefte/ und werkzeuge/.
8. Satz: Eine Gleichung ohne $ im gleichungsraster wird als Mathe
   gesetzt, ein Text im gleichungsraster als Teilaufgabe (\teil) – sonst
   Kompilierfehler bzw. Text über die Spalte hinaus (nur im Heft).
9. Ausgelassene Teilaufgaben stehen als „(ausgelassen)“ mit ihrem
   Buchstaben da, die Lösung ebenso; der alte Quelltext bleibt als
   Kommentar mit Grund. Folgefehler werden durch ein Kleinstdokument je
   Teilaufgabe von der Ursache getrennt.
10. daten liegt nur mit e1, e2 und zone in bank/ (eine andere Sitzung
    baut den Eintrag); das Heft msa-daten nimmt den Stand beim Bau.

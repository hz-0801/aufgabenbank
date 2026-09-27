# Lösungswege je Eintrag – Vorschlag für bank.md

Stand 2026-09-27, nach dem Prüfstein an lineare-gleichungen und
quadratische-funktionen (bank/<eintrag>/weg.jsonl). Vorschlag, nicht
beschlossen; bank.md, bank-pruef.py, duplikate.py und zusammenbau.py
sind unverändert.

## Zuerst: zwei Werkzeuge stolpern über weg.jsonl

1. `bank-pruef.py` (v0.5) liest `bank/<eintrag>/*.jsonl` und meldet
   `weg.jsonl` als „ABWEICHUNG weg.jsonl: Dateiname“. Beide Einträge
   stehen dadurch bei 1 Abweichung statt 0; die Bankzeilen selbst sind
   unverändert bei 0. Nach bank.md („Erst bei null Abweichungen wird
   committet“) blockiert das jeden weiteren Commit an diesen Einträgen.
   Abhilfe: in `pruefe_eintrag` nur `zone.jsonl` und `e<n>.jsonl`
   lesen (wie `zusammenbau.py` schon) und `weg.jsonl` eigens prüfen
   (unten, „Prüfung“).
2. `duplikate.py` liest `bank/*/*.jsonl` und bricht bei der ersten
   Wegzeile mit `KeyError: 'eintrag'` ab. Abhilfe: dieselbe Auswahl
   der Dateien.

`zusammenbau.py` liest nur `e*.jsonl` und `zone.jsonl` und ist nicht
betroffen.

## Was der Prüfstein zeigt

| Eintrag | Wege | Schritte | Schnitt | raster / rechnung | fehlerstelle null | Abweichung zu loesung |
| --- | --- | --- | --- | --- | --- | --- |
| lineare-gleichungen | 59 | 190 | 3,2 | 19 / 40 | 24 | 0 |
| quadratische-funktionen | 58 | 186 | 3,2 | 19 / 39 | 7 | 0 |

Jeder Weg endet mit dem Ergebnis aus loesung. Nachgerechnet (Skript im
Scratchpad, nicht im Repo): 285 Gleichheiten in den Rechenzeilen,
jede pruef-Zahl steht im Weg, fehlerstelle.muster steht wortgleich
unter „Typische Fehler“ der Mappe, form passt zu form der Bankzeile.

fehlerstelle null trifft vor allem die Zone (17 von 26 Zonenwegen) und
Stellen, für die „Typische Fehler“ kein Muster führt (siehe Befunde).

## Vorschlag für bank.md

Unter „Ablage“:

    bank/<eintrag>/weg.jsonl      Lösungswege zu Grundfall und Prüfungshöhe

Neuer Abschnitt „Lösungswege“:

    id            wie die Bankzeile; Reihenfolge wie in der Bank
                  (zone, e1, e2 …)
    schritte      Liste; je Schritt ein Objekt:
                    tun       ein Satz in Schülersprache, Du-Form
                    rechnung  eine Zeile im Inhalt von \rechnung:
                              & vor dem Gleichheitszeichen,
                              &&\mid vor der Umformung, && vor einem
                              Kommentar; kein $, kein \\
                    warum     ein Halbsatz, klein, ohne Punkt
    fehlerstelle  null oder {"schritt": n, "muster": "<Zeile aus
                  Typische Fehler, wortgleich, ohne Quellenklammer>"}
    form          "raster" bei form gleichungsraster der Bankzeile,
                  sonst "rechnung"

Regeln:

- Ein Schritt ist eine Zeile der Schreibform des Verfahrens. Bei
  Umformungen steht die Ausgangsgleichung in Schritt 1, der Vermerk
  hinter dem Strich in derselben Zeile; tun erklärt den Vermerk. Das
  Auflösen einer Klammer ist ein eigener Schritt ohne Vermerk.
- Der letzte Schritt trägt das Ergebnis der loesung. Mit Probe: die
  Probezeile und dahinter „x = … ist Lösung“, wie im `\beispiel` der
  Anleitung (`&& \text{(wA)}\quad x = 3 \text{ ist Lösung}`).
- Der Weg rechnet die loesung nach, er ändert sie nicht. Ein anderes
  Ergebnis steht in stand.md unter „Befunde“.
- fehlerstelle nur mit einem Muster aus „Typische Fehler“ des
  Eintrags. Passt keins, null – kein Muster wird zurechtgebogen.
- Offene Aufgaben („z. B.“) folgen dem Beispiel der loesung.

Mengen: siehe nächster Abschnitt; Empfehlung ist „grundfall und
pruefung, ohne Zone“.

Prüfung (als Zusatz für bank-pruef.py): ids und Reihenfolge wie die
Bankzeilen der gewählten Menge; Felder vollständig; form passend;
fehlerstelle.muster wortgleich in der Mappe, schritt im Bereich;
jede pruef-Zahl der Bankzeile steht in einer Rechenzeile; jede
Gleichheitskette aus Zahlen stimmt (Toleranz wie bei pruef); Zeilen
mit x stimmen für die x-Werte, die der Weg selbst nennt; Bausteine in
rechnung wie in aufgabe.

## Mengen und Kosten je Eintrag

Kosten in Zeilen von weg.jsonl (eine Zeile je Weg), dazu Schritte.
Zahlen der Mengen A und B gezählt, C und D geschätzt mit 3,2 Schritten
je Weg (Schnitt des Prüfsteins).

| Menge | lineare-gleichungen | quadratische-funktionen |
| --- | --- | --- |
| A grundfall + pruefung (Prüfstein) | 59 Zeilen, 190 Schritte | 58 Zeilen, 186 Schritte |
| B wie A, ohne Zone (Empfehlung) | 49 Zeilen, 170 Schritte | 42 Zeilen, 144 Schritte |
| C B + je Sprosse und Vorstufe Variante 1 | 77 Zeilen, ~260 Schritte | 83 Zeilen, ~275 Schritte |
| D alle Zeilen außer begruenden | 187 Zeilen, ~600 Schritte | 245 Zeilen, ~785 Schritte |

Empfehlung B. Gründe:

- Die Lösungsseite braucht den Weg dort, wo das Verfahren gelernt wird
  (Grundfall) und wo es am schwersten ist (Prüfungshöhe). Eine Sprosse
  dazwischen ändert genau ein Merkmal (bank.md, „Regeln für den
  Inhalt“); ihr Weg ist der Grundfallweg plus ein Schritt.
- Form schwach setzt den Grundfall als Päckchen mit allen Varianten
  (zusammenbau.md, Offen 7) – genau die Menge von B.
- Zone: Die Wege sind zwei Zeilen lang („6² = 6 · 6 = 36“), und 17
  von 26 haben keine fehlerstelle, weil „Typische Fehler“ die
  Fallstricke der Voraussetzungen nicht führt. Der Gewinn ist klein.
  Dagegen spricht nur, dass schwach auch in der Zone gilt (Offen 7).

## Was der Zusammenbau daraus setzt

- **Lösungsdatei, Begleitteil.** `\erg` bleibt mit loesung. Unter der
  Hauptnummer folgt für Variante 1 des Grundfalls und für die
  Prüfungshöhe der Weg als `\rechnung{…}`: die rechnung-Zeilen mit
  ` \\ ` verbunden. Das ist die Verwendung, die die Anleitung für
  `\rechnung` nennt („Rechenweg im Begleitteil“).
- **gleichungsraster (form raster).** Die Zahl der Schritte minus eins
  ist die Zahl der Schreibzeilen unter der Gleichung, `\gl[n]{…}`.
  Das schließt die Lücke „Zeilenzahl im gleichungsraster nach dem
  Grundfall“ aus zusammenbau.md („Was v0.1 nicht kann“).
- **Form schwach.** Ein Raster mit einer Zeile je Schritt: links tun
  vorgedruckt, rechts eine leere Schreibzeile; in der Lösungsdatei
  dasselbe Raster mit rechnung (ohne `&`). Die Zeile der fehlerstelle
  trägt ein Warnzeichen. Einen Baustein für dieses Raster gibt es in
  mappen/_bausteine.md nicht; er müsste in hz-0801/blattbau entstehen
  (sonst `tabular` im Rahmen, was die Strukturprüfung zulässt).
- **Hilfeseite („mit tipps“).** Aus dem Weg der Variante 1 des
  Grundfalls: `\verfahren{<kette>} \begin{schritte} \schritt <tun> …
  \achtung{<muster>} \end{schritte}` – `\achtung` beim Schritt der
  fehlerstelle.
- **Lehrer am Tisch.** Eigene Datei (Schalter etwa `--lehrer`): je Weg
  drei Spalten tun · rechnung · warum, die fehlerstelle mit ihrem
  Muster darunter. Nicht auf dem Schülerblatt.

## Befunde

Abweichungen zu loesung: keine, in beiden Einträgen.

Am Katalog und an der Bank, ohne Folgen für die Wege:

1. lineare-gleichungen, „Typische Fehler“: kein Muster für das
   Vorzeichen beim Einsetzen negativer Zahlen (−4 · (−3)), obwohl die
   Prüfungshöhe der Einheit 1 „mit negativer Zahl“ heißt; ebenso keins
   für „Wert des Terms statt x abgelesen“ beim Probieren. Die Wege
   e1-k2-s5 (4) und e1-k3-s1 (5) tragen deshalb fehlerstelle null.
2. lineare-gleichungen e4-k1-s6-v5 bis v8: sprosse_text „Prüfungshöhe:
   Sachverhalt mit Klammer (P10-Form)“, die Aufgaben sind Term zu Satz
   ohne Klammer (Originale 2016-OS-B1b, 2021-OS-B1e). Merkmal und
   Sprossentext passen nicht zueinander.
3. quadratische-funktionen e3-k1-s9-v1 und v2: loesung ohne Probe; der
   Weg ergänzt die Probe mit q nach dem Merkkasten der Einheit 3. Das
   Ergebnis ist dasselbe.
4. quadratische-funktionen e2-k1-s15-v1 und v2: offene Aufgaben
   („z. B.“); der Weg zeigt eine mögliche Lösung. Der Zusammenbau
   sollte das kennzeichnen.
5. quadratische-funktionen e1-k1-s1-v1 bis v5: `\wertetabelle` steht
   in aufgabe, grafik ist leer. bank.md sieht den Bausteinaufruf in
   grafik vor.

## Drei Beispielwege (wortgleich aus weg.jsonl)

lineare-gleichungen, Einheit 3, Prüfungshöhe (raster):

```json
{"id": "lineare-gleichungen-e3-k1-s7-v3", "schritte": [{"tun": "Löse die Minusklammer auf: − 3 mal x und − 3 mal 4.", "rechnung": "7x - 3(x + 4) &= x + 9", "warum": "weil das Minus vor der 3 für beide Glieder in der Klammer gilt"}, {"tun": "Fasse links die x zusammen.", "rechnung": "7x - 3x - 12 &= x + 9", "warum": "weil gleichartige Glieder zusammengehören"}, {"tun": "Rechts stehen weniger x: nimm auf beiden Seiten x weg.", "rechnung": "4x - 12 &= x + 9 &&\\mid -x", "warum": "dann stehen alle x links"}, {"tun": "Bring die − 12 weg: rechne auf beiden Seiten + 12.", "rechnung": "3x - 12 &= 9 &&\\mid +12", "warum": "weil plus die Umkehrung von minus ist"}, {"tun": "Teile beide Seiten durch 3.", "rechnung": "3x &= 21 &&\\mid :3", "warum": "weil geteilt die Umkehrung von mal ist"}, {"tun": "Lies die Lösung ab.", "rechnung": "x &= 7", "warum": "links bleibt nur x übrig"}, {"tun": "Mach die Probe: rechne beide Seiten der Ausgangsgleichung mit 7 aus.", "rechnung": "7 \\cdot 7 - 3 \\cdot (7 + 4) = 16,\\ 7 + 9 = 16 && \\text{(wA)}\\quad x = 7 \\text{ ist Lösung}", "warum": "beide Seiten müssen denselben Wert haben"}], "fehlerstelle": {"schritt": 1, "muster": "Minusklammer in der Gleichung falsch aufgelöst: 10 − (x − 2) = 10 − x − 2."}, "form": "raster"}
```

quadratische-funktionen, Einheit 2, Prüfungshöhe (rechnung):

```json
{"id": "quadratische-funktionen-e2-k1-s14-v1", "schritte": [{"tun": "Lies den Scheitel von f ab.", "rechnung": "S_f(-4|{-2})", "warum": "in der Klammer das Vorzeichen umdrehen"}, {"tun": "Beim Spiegeln an der y-Achse wechselt nur die x-Koordinate das Vorzeichen.", "rechnung": "S_g(4|{-2})", "warum": "die Höhe des Scheitels bleibt gleich"}, {"tun": "Die Öffnung bleibt: zeichne vom Scheitel aus 1 rechts 1 hoch und 2 rechts 4 hoch, nach links genauso.", "rechnung": "(3|{-1}),\\ (5|{-1}),\\ (2|2),\\ (6|2)", "warum": "es bleibt eine Normalparabel"}, {"tun": "Schreib die Gleichung mit dem neuen Scheitel.", "rechnung": "g(x) = (x - 4)^2 - 2,\\ S(4|{-2})", "warum": "in der Klammer steht d mit umgedrehtem Vorzeichen"}], "fehlerstelle": {"schritt": 2, "muster": "Spiegeln: an der y-Achse statt an der x-Achse ((x − 3)² statt −(x + 3)²); nur das Vorzeichen von x² gewechselt (−x² + 1 statt −x² − 1); Verschieben und Spiegeln in falscher Reihenfolge (−(x + 3)² + 2)."}, "form": "rechnung"}
```

quadratische-funktionen, Einheit 4, Prüfungshöhe (raster):

```json
{"id": "quadratische-funktionen-e4-k1-s13-v1", "schritte": [{"tun": "Setz Parabel und Gerade gleich.", "rechnung": "(x - 4)^2 - 6 &= -2x + 5", "warum": "in den Schnittpunkten haben beide denselben y-Wert"}, {"tun": "Löse die Klammer auf, fasse zusammen und bring dann alles nach links: + 2x und − 5.", "rechnung": "x^2 - 8x + 10 &= -2x + 5 &&\\mid +2x - 5", "warum": "die p-q-Formel braucht rechts eine Null"}, {"tun": "Lies p und q ab.", "rechnung": "x^2 - 6x + 5 &= 0", "warum": "p steht vor x, q ohne x: p = −6, q = 5"}, {"tun": "Setz in die p-q-Formel ein.", "rechnung": "x &= 3 \\pm \\sqrt{9 - 5} = 3 \\pm 2", "warum": "−p/2 ist hier + 3"}, {"tun": "Schreib beide x-Werte hin.", "rechnung": "x_1 &= 5,\\quad x_2 = 1", "warum": "zwei Lösungen, zwei Schnittpunkte"}, {"tun": "Rechne die y-Werte mit der Geraden aus.", "rechnung": "g(5) = -10 + 5 = -5,\\quad g(1) = -2 + 5 = 3", "warum": "die Gerade ist leichter einzusetzen als die Parabel"}, {"tun": "Schreib die beiden Schnittpunkte.", "rechnung": "S_1(5|{-5}),\\ S_2(1|3)", "warum": "gefragt sind Punkte, nicht nur x-Werte"}], "fehlerstelle": {"schritt": 2, "muster": "Schnittpunkte: Vorzeichen beim Umstellen (x² + 4x statt x² − 4x); y-Werte vergessen; nur in eine der beiden Funktionen eingesetzt."}, "form": "raster"}
```

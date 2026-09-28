# Render-Lauf über alle Einträge

Stand 2026-09-28 02:07 UTC. Quelltexte: bau/_alle/ (Zusammenbau v0.1, Stand 923f60d 2026-09-27), Bank beim Commit 2f6d219 schnittmengen: Zweitleser. Vorlage: mathblatt.sty „Version 2026-09-28a“ aus bau/_alle/<eintrag>/<lauf>/ – byte-gleich mit hz-0801/blattbau@1acddaa. Umgebung: XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian), Ubuntu-Pakete nach werkzeuge/render.md, Einrichtung ohne Befund (apt erreichbar, xelatex und pdftotext lagen nach der Installation vor).

Weg: bau/render-alle/render.py kopiert jeden Lauf in eine Arbeitskopie außerhalb des Repos und kompiliert dort gesamt.tex (Auftrag) und loesungen.tex (Zusatz, weil die Lösungsdateien nicht in gesamt.tex stecken) mit `xelatex -interaction=nonstopmode -file-line-error`, zwei Läufe je Datei (Abhakseite, Sprungziele), ein dritter nur bei „Rerun“ in der .log – nirgends nötig. Zählgrenze 3 Versuche je Datei, nie erreicht. Kompilierläufe insgesamt: 388. Je Versuch stehen die ersten 60 Fehlerzeilen der .log mit Kontext in logs/<eintrag>-<lauf>-<datei>.txt. Danach pdfinfo (Seiten) und pdftotext (Textgehalt: jedes PDF enthält Text, kein leeres Blatt). Fehlerstellen sind je (Datei, Zeile) die erste Meldung; xelatex läuft nach einem Fehler weiter und meldet Folgefehler bis zum Dateiende, darum steht in der Tabelle die Zahl der Stellen, nicht der Logzeilen. Die Bankzeile zu einer Stelle ermittelt render.py über den Text der Teilaufgabe (118 Stellen in Teilaufgaben: 2 wörtlich, 116 nach Ähnlichkeit, alle ≥ 0,95; die 8 übrigen Stellen liegen in abhaken.tex und gesamt.tex – Folgefehler ohne Bankzeile); ergebnis.json hält alles.

## Ergebnis

- gesamt.tex Lernblatt: **64 von 70 Einträgen kompilieren** fehlerfrei; schwach: 22 von 27; beide Läufe eines Eintrags fehlerfrei: 64 von 70. Alle 70 Einträge liefern ein PDF, auch die mit Fehlern (xelatex setzt nach einem Fehler weiter; nur binomialverteilung/lernblatt bricht mit „Emergency stop“ ab und hat ein unvollständiges PDF).
- loesungen.tex: 97 von 97 Läufen fehlerfrei.
- Seiten: 638 (Lernblatt gesamt.tex) + 511 (schwach).
- Sechs Fehlerklassen, alle mit Gegenprobe bestätigt (Abschnitt „Fehler nach Baustein“): fünf liegen in Bankzeilen, eine im Zusammenbau. Die Vorlage hat keinen Kompilierfehler.
- Stiller Befund ohne Fehlerzeile: **786 fehlende Zeichen** („Missing character“ in der .log): Unicode-Zeichen wie ≈, α, β, γ, π, ∫, ℝ, ⇔, ✓ stehen im Text, Latin Modern Roman hat sie nicht, im PDF bleibt die Stelle leer. Abschnitt „Fehlende Zeichen“.

## Je Eintrag

gesamt.tex je Lauf: kompiliert (ja/nein), Seiten, Zahl der Fehlerstellen und der erste Fehler mit Datei:Zeile. Lös.: loesungen.tex Lernblatt/schwach (Seiten, alle fehlerfrei). Zeichen: fehlende Zeichen im Lernblatt gesamt.tex. „–“: kein schwach-Lauf (Sek II).

| Eintrag | LB | Seiten | Stellen | erster Fehler | schwach | Seiten | Stellen | erster Fehler | Lös. | Zeichen |
| --- | --- | --: | --: | --- | --- | --: | --: | --- | --- | --: |
| ableitung-und-aenderungsrate | ja | 13 | 0 |  | – | – | – | – | 4 | 2 |
| ableitungsregeln | ja | 6 | 0 |  | – | – | – | – | 2 |  |
| abstaende | ja | 8 | 0 |  | – | – | – | – | 2 | 1 |
| bedingte-wahrscheinlichkeit-und-bayes | ja | 8 | 0 |  | – | – | – | – | 2 |  |
| binomialverteilung | **nein** | 8 | 17 | e5_a.tex:16 Extra }, or forgotten $. | – | – | – | – | 3 | 4 |
| binomische-formeln | ja | 5 | 0 |  | ja | 13 | 0 |  | 1/1 |  |
| bruchrechnung | ja | 7 | 0 |  | ja | 19 | 0 |  | 2/2 | 2 |
| brueche-dezimalzahlen | **nein** | 9 | 4 | e5_a.tex:26 Missing $ inserted. | **nein** | 23 | 3 | e5_a.tex:41 Missing $ inserted. | 2/2 |  |
| ebenen | ja | 9 | 0 |  | – | – | – | – | 3 |  |
| einheiten | ja | 11 | 0 |  | ja | 27 | 0 |  | 3/3 |  |
| extremalprobleme | ja | 7 | 0 |  | – | – | – | – | 2 |  |
| flaechen | ja | 10 | 0 |  | ja | 23 | 0 |  | 2/3 | 2 |
| flaecheninhalt-durch-integration | ja | 9 | 0 |  | – | – | – | – | 2 |  |
| flaecheninhalt-und-volumen-im-raum | ja | 10 | 0 |  | – | – | – | – | 2 |  |
| funktionsklassen-und-eigenschaften | ja | 12 | 0 |  | – | – | – | – | 4 |  |
| funktionsscharen-und-ortskurven | ja | 11 | 0 |  | – | – | – | – | 3 |  |
| geraden | ja | 8 | 0 |  | – | – | – | – | 3 | 1 |
| gleichungen-loesen | ja | 11 | 0 |  | – | – | – | – | 2 |  |
| grenzwerte-und-verhalten-im-unendlichen | ja | 5 | 0 |  | – | – | – | – | 2 | 2 |
| hypergeometrische-verteilung | ja | 4 | 0 |  | – | – | – | – | 1 |  |
| hypothesentests | ja | 7 | 0 |  | – | – | – | – | 2 |  |
| integrationsregeln | ja | 4 | 0 |  | – | – | – | – | 1 |  |
| kenngroessen-von-verteilungen | ja | 12 | 0 |  | – | – | – | – | 3 |  |
| koerper | ja | 15 | 0 |  | ja | 24 | 0 |  | 4/4 | 2 |
| kombinatorik | ja | 5 | 0 |  | – | – | – | – | 2 |  |
| konfidenzintervalle | ja | 8 | 0 |  | – | – | – | – | 2 | 2 |
| kreis | ja | 8 | 0 |  | ja | 16 | 0 |  | 2/2 | 37 |
| kurvenuntersuchung | ja | 14 | 0 |  | – | – | – | – | 5 |  |
| lagebeziehungen | ja | 6 | 0 |  | – | – | – | – | 2 |  |
| lineare-funktionen | ja | 18 | 0 |  | ja | 23 | 0 |  | 2/2 |  |
| lineare-gleichungen | ja | 8 | 0 |  | ja | 18 | 0 |  | 2/2 |  |
| lineare-gleichungssysteme | ja | 15 | 0 |  | ja | 32 | 0 |  | 3/3 |  |
| linearkombination-und-lineare-abhaengigkeit | ja | 4 | 0 |  | – | – | – | – | 1 |  |
| matrizen-und-uebergangsprozesse | ja | 9 | 0 |  | – | – | – | – | 2 |  |
| normalverteilung-und-sigma-regeln | ja | 5 | 0 |  | – | – | – | – | 2 | 11 |
| orthogonalitaet | ja | 6 | 0 |  | – | – | – | – | 2 |  |
| potenzen-wurzeln | ja | 5 | 0 |  | ja | 14 | 0 |  | 2/2 | 2 |
| prozentrechnung | ja | 8 | 0 |  | ja | 19 | 0 |  | 2/2 | 2 |
| punkte-und-strecken-im-koordinatensystem | ja | 11 | 0 |  | – | – | – | – | 6 |  |
| pyramide-kegel-kugel | ja | 11 | 0 |  | ja | 15 | 0 |  | 4/4 | 18 |
| pythagoras | **nein** | 10 | 19 | e1_a.tex:29 Missing $ inserted. | **nein** | 16 | 13 | e1_a.tex:30 Missing $ inserted. | 3/3 | 4 |
| quadratische-funktionen | **nein** | 15 | 4 | e1_a.tex:30 LaTeX Error: There's no line here to end. | **nein** | 17 | 4 | e1_a.tex:44 LaTeX Error: There's no line here to end. | 2/2 |  |
| quadratische-gleichungen | **nein** | 10 | 23 | e1_a.tex:23 Missing $ inserted. | **nein** | 17 | 35 | e1_a.tex:22 Missing $ inserted. | 2/2 | 2 |
| rationale-zahlen | ja | 7 | 0 |  | ja | 17 | 0 |  | 2/2 |  |
| reelle-zahlen | **nein** | 6 | 2 | e1_a.tex:23 LaTeX Error: Command \item invalid in math mode. | **nein** | 14 | 2 | e1_a.tex:35 LaTeX Error: Command \end{list} invalid in math  | 2/2 | 18 |
| rekonstruktion-von-bestaenden | ja | 8 | 0 |  | – | – | – | – | 2 | 6 |
| rekonstruktion-von-funktionsgleichungen | ja | 9 | 0 |  | – | – | – | – | 2 | 5 |
| rotationsvolumen | ja | 4 | 0 |  | – | – | – | – | 1 | 1 |
| scharen-von-geraden-und-ebenen | ja | 9 | 0 |  | – | – | – | – | 2 |  |
| schnittmengen | ja | 8 | 0 |  | – | – | – | – | 4 | 4 |
| skalarprodukt-und-winkel | ja | 6 | 0 |  | – | – | – | – | 2 |  |
| spiegelung | ja | 5 | 0 |  | – | – | – | – | 2 |  |
| stammfunktion-und-hauptsatz | ja | 11 | 0 |  | – | – | – | – | 2 |  |
| strahlensaetze | ja | 13 | 0 |  | ja | 17 | 0 |  | 3/3 | 1 |
| symmetrie-abbildungen | ja | 14 | 0 |  | ja | 19 | 0 |  | 2/3 |  |
| tangente-normale-schnittwinkel | ja | 11 | 0 |  | – | – | – | – | 3 | 2 |
| terme | ja | 8 | 0 |  | ja | 16 | 0 |  | 2/2 |  |
| trigonometrie | ja | 12 | 0 |  | ja | 20 | 0 |  | 2/2 | 44 |
| trigonometrische-funktionen | ja | 17 | 0 |  | ja | 18 | 0 |  | 3/3 | 2 |
| umkehrfunktion | ja | 4 | 0 |  | – | – | – | – | 1 | 4 |
| unabhaengigkeit | ja | 7 | 0 |  | – | – | – | – | 3 | 5 |
| uneigentliche-integrale | ja | 4 | 0 |  | – | – | – | – | 1 | 8 |
| vektoren-und-rechenoperationen | ja | 11 | 0 |  | – | – | – | – | 3 |  |
| vierfeldertafel | ja | 6 | 0 |  | – | – | – | – | 2 |  |
| wahrscheinlichkeit | ja | 12 | 0 |  | ja | 18 | 0 |  | 3/4 | 4 |
| winkel-dreiecke | ja | 17 | 0 |  | ja | 20 | 0 |  | 4/6 | 62 |
| zinsrechnung | ja | 7 | 0 |  | ja | 12 | 0 |  | 1/2 | 3 |
| zufallsexperimente-und-pfadregeln | ja | 13 | 0 |  | – | – | – | – | 4 | 8 |
| zufallsgroessen-und-verteilungen | ja | 8 | 0 |  | – | – | – | – | 2 |  |
| zuordnungen | ja | 16 | 0 |  | ja | 24 | 0 |  | 2/2 | 6 |

## Fehler nach Baustein

Jede Fehlerstelle des Laufs (gesamt.tex, beide Läufe) ist einer Klasse zugeordnet; „Folgefehler“ sind Stellen, die nach einer Gegenprobe mit der ersten Ursache verschwinden (Umgebung nach dem Fehler nicht mehr geschlossen, `\item`-Meldungen an jedem weiteren `\teil`, Meldungen an `\end{aufgabe}`, in abhaken.tex und gesamt.tex). Die Spalte „Bank“ zählt alle Zeilen der Bank mit demselben Muster, auch die im Lauf nicht gewählten Varianten (Regel „Variante 1“).

| Klasse | Bausteinaufruf | Meldung | Stellen im Lauf | Bankzeilen im Lauf | Bank gesamt | Einträge | Vorschlag |
| --- | --- | --- | --: | --: | --: | --- | --- |
| K1 | `\gl{\text{…}}` / `\swz{$\text{…}$}`: Gleichung ohne `$` im Feld aufgabe (form gleichungsraster) | Missing $ inserted – `^`, `_` oder `\cdot` stehen in `\text{}` | 58 | 35 | 75 | quadratische-gleichungen 75 | **Bankzeile** |
| K2 | `__` als Lücke im Feld aufgabe | Missing $ inserted – `_` im Textmodus | 6 | 3 | 13 | brueche-dezimalzahlen 13 | **Bankzeile** |
| K3 | `\dreieck` mit `$…$` in den Beschriftungen | Missing $ inserted – die Vorlage setzt die sechs Labels selbst in `$…$` | 2 | 1 | 25 | flaechen 8, pythagoras 17 | **Bankzeile** |
| K4 | `\saeulenab[… ylabel=$P(X = k)$ …]` – `=` im Optionswert ohne Klammern | Extra }, or forgotten $ – pgfkeys zerlegt den Wert am `=` | 2 | 2 | 9 | binomialverteilung 8, kenngroessen-von-verteilungen 1 | **Bankzeile** |
| K5 | `\wertetabelle{…}{…}{…} \\` – Zeilenumbruch nach dem Blockbaustein | There's no line here to end – `\wertetabelle` endet mit `\par` | 8 | 4 | 7 | quadratische-funktionen 7 | **Bankzeile** |
| K6 | Antwortgerüst mit `$…<…$`: Zusammenbau setzt `$<$` in ein offenes `$…$` | Command \item/\end{list} invalid in math mode – Mathe bleibt offen | 2 | 2 | 6 | reelle-zahlen 6 | **Zusammenbau** |
| – | Folgefehler | `\item`-Meldungen an `\teil`/`\swz`, `\end{aufgabe}`, abhaken.tex, gesamt.tex, Emergency stop | 48 | – | – | binomialverteilung/lernblatt 15, brueche-dezimalzahlen/lernblatt 1, pythagoras/lernblatt 18, pythagoras/schwach 12, reelle-zahlen/lernblatt 2 | keiner |

### K1 – `\gl{\text{…}}` / `\swz{$\text{…}$}`: Gleichung ohne `$` im Feld aufgabe (form gleichungsraster)

- Meldung: Missing $ inserted – `^`, `_` oder `\cdot` stehen in `\text{}`.
- Im Lauf: 58 Stellen, Bankzeilen: quadratische-gleichungen-e1-k2-s1-v1, quadratische-gleichungen-e1-k2-s1-v2, quadratische-gleichungen-e1-k2-s1-v3, quadratische-gleichungen-e1-k2-s1-v4, quadratische-gleichungen-e1-k2-s1-v5, quadratische-gleichungen-e1-k2-s10-v1, quadratische-gleichungen-e1-k2-s3-v1, quadratische-gleichungen-e1-k2-s5-v1, quadratische-gleichungen-e1-k2-s7-v1, quadratische-gleichungen-e1-k2-s8-v1, quadratische-gleichungen-e1-k2-s9-v1, quadratische-gleichungen-e2-k1-s1-v1, quadratische-gleichungen-e2-k1-s1-v2, quadratische-gleichungen-e2-k1-s1-v3, quadratische-gleichungen-e2-k1-s1-v4, quadratische-gleichungen-e2-k1-s1-v5, quadratische-gleichungen-e2-k1-s2-v1, quadratische-gleichungen-e2-k1-s3-v1, quadratische-gleichungen-e2-k1-s4-v1, quadratische-gleichungen-e2-k1-s6-v1, quadratische-gleichungen-e2-k1-s7-v1, quadratische-gleichungen-e2-k1-s8-v1, quadratische-gleichungen-e3-k3-s1-v1, quadratische-gleichungen-e3-k3-s1-v2, quadratische-gleichungen-e3-k3-s1-v3, quadratische-gleichungen-e3-k3-s1-v4, quadratische-gleichungen-e3-k3-s1-v5, quadratische-gleichungen-e3-k3-s11-v1, quadratische-gleichungen-e3-k3-s2-v1, quadratische-gleichungen-e3-k3-s3-v1, quadratische-gleichungen-e3-k3-s4-v1, quadratische-gleichungen-e3-k3-s5-v1, quadratische-gleichungen-e3-k3-s6-v1, quadratische-gleichungen-e3-k3-s7-v1, quadratische-gleichungen-e3-k3-s9-v1.
- In der Bank gesamt: 75 Zeilen – quadratische-gleichungen-e1-k2-s1-v1 (bank/quadratische-gleichungen/e1.jsonl:9), quadratische-gleichungen-e1-k2-s1-v2 (bank/quadratische-gleichungen/e1.jsonl:10), quadratische-gleichungen-e1-k2-s1-v3 (bank/quadratische-gleichungen/e1.jsonl:11), quadratische-gleichungen-e1-k2-s1-v4 (bank/quadratische-gleichungen/e1.jsonl:12), quadratische-gleichungen-e1-k2-s1-v5 (bank/quadratische-gleichungen/e1.jsonl:13), quadratische-gleichungen-e1-k2-s3-v1 (bank/quadratische-gleichungen/e1.jsonl:17), quadratische-gleichungen-e1-k2-s3-v2 (bank/quadratische-gleichungen/e1.jsonl:18), quadratische-gleichungen-e1-k2-s3-v3 (bank/quadratische-gleichungen/e1.jsonl:19), quadratische-gleichungen-e1-k2-s5-v1 (bank/quadratische-gleichungen/e1.jsonl:23), quadratische-gleichungen-e1-k2-s5-v2 (bank/quadratische-gleichungen/e1.jsonl:24), quadratische-gleichungen-e1-k2-s5-v3 (bank/quadratische-gleichungen/e1.jsonl:25), quadratische-gleichungen-e1-k2-s7-v1 (bank/quadratische-gleichungen/e1.jsonl:29), quadratische-gleichungen-e1-k2-s7-v2 (bank/quadratische-gleichungen/e1.jsonl:30), quadratische-gleichungen-e1-k2-s7-v3 (bank/quadratische-gleichungen/e1.jsonl:31), quadratische-gleichungen-e1-k2-s8-v1 (bank/quadratische-gleichungen/e1.jsonl:32), quadratische-gleichungen-e1-k2-s8-v2 (bank/quadratische-gleichungen/e1.jsonl:33), quadratische-gleichungen-e1-k2-s8-v3 (bank/quadratische-gleichungen/e1.jsonl:34), quadratische-gleichungen-e1-k2-s9-v1 (bank/quadratische-gleichungen/e1.jsonl:35), quadratische-gleichungen-e1-k2-s9-v2 (bank/quadratische-gleichungen/e1.jsonl:36), quadratische-gleichungen-e1-k2-s9-v3 (bank/quadratische-gleichungen/e1.jsonl:37), quadratische-gleichungen-e1-k2-s10-v1 (bank/quadratische-gleichungen/e1.jsonl:38), quadratische-gleichungen-e1-k2-s10-v2 (bank/quadratische-gleichungen/e1.jsonl:39), quadratische-gleichungen-e1-k2-s10-v3 (bank/quadratische-gleichungen/e1.jsonl:40), quadratische-gleichungen-e2-k1-s1-v1 (bank/quadratische-gleichungen/e2.jsonl:5), quadratische-gleichungen-e2-k1-s1-v2 (bank/quadratische-gleichungen/e2.jsonl:6), quadratische-gleichungen-e2-k1-s1-v3 (bank/quadratische-gleichungen/e2.jsonl:7), quadratische-gleichungen-e2-k1-s1-v4 (bank/quadratische-gleichungen/e2.jsonl:8), quadratische-gleichungen-e2-k1-s1-v5 (bank/quadratische-gleichungen/e2.jsonl:9), quadratische-gleichungen-e2-k1-s2-v1 (bank/quadratische-gleichungen/e2.jsonl:10), quadratische-gleichungen-e2-k1-s2-v2 (bank/quadratische-gleichungen/e2.jsonl:11), quadratische-gleichungen-e2-k1-s2-v3 (bank/quadratische-gleichungen/e2.jsonl:12), quadratische-gleichungen-e2-k1-s3-v1 (bank/quadratische-gleichungen/e2.jsonl:13), quadratische-gleichungen-e2-k1-s3-v2 (bank/quadratische-gleichungen/e2.jsonl:14), quadratische-gleichungen-e2-k1-s3-v3 (bank/quadratische-gleichungen/e2.jsonl:15), quadratische-gleichungen-e2-k1-s4-v1 (bank/quadratische-gleichungen/e2.jsonl:16), quadratische-gleichungen-e2-k1-s4-v2 (bank/quadratische-gleichungen/e2.jsonl:17), quadratische-gleichungen-e2-k1-s4-v3 (bank/quadratische-gleichungen/e2.jsonl:18), quadratische-gleichungen-e2-k1-s6-v1 (bank/quadratische-gleichungen/e2.jsonl:22), quadratische-gleichungen-e2-k1-s6-v2 (bank/quadratische-gleichungen/e2.jsonl:23), quadratische-gleichungen-e2-k1-s6-v3 (bank/quadratische-gleichungen/e2.jsonl:24), quadratische-gleichungen-e2-k1-s7-v1 (bank/quadratische-gleichungen/e2.jsonl:25), quadratische-gleichungen-e2-k1-s7-v2 (bank/quadratische-gleichungen/e2.jsonl:26), quadratische-gleichungen-e2-k1-s7-v3 (bank/quadratische-gleichungen/e2.jsonl:27), quadratische-gleichungen-e2-k1-s8-v1 (bank/quadratische-gleichungen/e2.jsonl:28), quadratische-gleichungen-e2-k1-s8-v2 (bank/quadratische-gleichungen/e2.jsonl:29), quadratische-gleichungen-e2-k1-s8-v3 (bank/quadratische-gleichungen/e2.jsonl:30), quadratische-gleichungen-e3-k3-s1-v1 (bank/quadratische-gleichungen/e3.jsonl:13), quadratische-gleichungen-e3-k3-s1-v2 (bank/quadratische-gleichungen/e3.jsonl:14), quadratische-gleichungen-e3-k3-s1-v3 (bank/quadratische-gleichungen/e3.jsonl:15), quadratische-gleichungen-e3-k3-s1-v4 (bank/quadratische-gleichungen/e3.jsonl:16), quadratische-gleichungen-e3-k3-s1-v5 (bank/quadratische-gleichungen/e3.jsonl:17), quadratische-gleichungen-e3-k3-s2-v1 (bank/quadratische-gleichungen/e3.jsonl:18), quadratische-gleichungen-e3-k3-s2-v2 (bank/quadratische-gleichungen/e3.jsonl:19), quadratische-gleichungen-e3-k3-s2-v3 (bank/quadratische-gleichungen/e3.jsonl:20), quadratische-gleichungen-e3-k3-s3-v1 (bank/quadratische-gleichungen/e3.jsonl:21), quadratische-gleichungen-e3-k3-s3-v2 (bank/quadratische-gleichungen/e3.jsonl:22), quadratische-gleichungen-e3-k3-s3-v3 (bank/quadratische-gleichungen/e3.jsonl:23), quadratische-gleichungen-e3-k3-s4-v1 (bank/quadratische-gleichungen/e3.jsonl:24), quadratische-gleichungen-e3-k3-s4-v2 (bank/quadratische-gleichungen/e3.jsonl:25), quadratische-gleichungen-e3-k3-s4-v3 (bank/quadratische-gleichungen/e3.jsonl:26), quadratische-gleichungen-e3-k3-s5-v1 (bank/quadratische-gleichungen/e3.jsonl:27), quadratische-gleichungen-e3-k3-s5-v2 (bank/quadratische-gleichungen/e3.jsonl:28), quadratische-gleichungen-e3-k3-s5-v3 (bank/quadratische-gleichungen/e3.jsonl:29), quadratische-gleichungen-e3-k3-s6-v1 (bank/quadratische-gleichungen/e3.jsonl:30), quadratische-gleichungen-e3-k3-s6-v2 (bank/quadratische-gleichungen/e3.jsonl:31), quadratische-gleichungen-e3-k3-s6-v3 (bank/quadratische-gleichungen/e3.jsonl:32), quadratische-gleichungen-e3-k3-s7-v1 (bank/quadratische-gleichungen/e3.jsonl:33), quadratische-gleichungen-e3-k3-s7-v2 (bank/quadratische-gleichungen/e3.jsonl:34), quadratische-gleichungen-e3-k3-s7-v3 (bank/quadratische-gleichungen/e3.jsonl:35), quadratische-gleichungen-e3-k3-s9-v1 (bank/quadratische-gleichungen/e3.jsonl:39), quadratische-gleichungen-e3-k3-s9-v2 (bank/quadratische-gleichungen/e3.jsonl:40), quadratische-gleichungen-e3-k3-s9-v3 (bank/quadratische-gleichungen/e3.jsonl:41), quadratische-gleichungen-e3-k3-s11-v1 (bank/quadratische-gleichungen/e3.jsonl:45), quadratische-gleichungen-e3-k3-s11-v2 (bank/quadratische-gleichungen/e3.jsonl:46), quadratische-gleichungen-e3-k3-s11-v3 (bank/quadratische-gleichungen/e3.jsonl:47).
- Gegenprobe: quadratische-gleichungen lernblatt und schwach: `\text{…}` um die Gleichungen entfernt → 0 Fehlerzeilen (vorher 1035 / 1575).
- Vorschlag: **Bankzeile** – aufgabe als `$x^2 = 81$` schreiben – so halten es alle anderen 668 gleichungsraster-Zeilen der Bank; `gl_inhalt()` streift das `$` dann ab und `\gl{x^2 = 81}` steht wie in der Anleitung. Zweitbester Weg: Zusammenbau, `gl_inhalt()` gibt Zeilen ohne `$` und ohne Wörter roh weiter statt in `\text{}`.

### K2 – `__` als Lücke im Feld aufgabe

- Meldung: Missing $ inserted – `_` im Textmodus.
- Im Lauf: 6 Stellen, Bankzeilen: brueche-dezimalzahlen-e5-k2-s6-v1, brueche-dezimalzahlen-e5-k2-s7-v1, brueche-dezimalzahlen-e5-k2-s8-v1.
- In der Bank gesamt: 13 Zeilen – brueche-dezimalzahlen-e4-k1-s8-v3 (bank/brueche-dezimalzahlen/e4.jsonl:30), brueche-dezimalzahlen-e4-k1-s8-v4 (bank/brueche-dezimalzahlen/e4.jsonl:31), brueche-dezimalzahlen-e5-k2-s6-v1 (bank/brueche-dezimalzahlen/e5.jsonl:26), brueche-dezimalzahlen-e5-k2-s6-v2 (bank/brueche-dezimalzahlen/e5.jsonl:27), brueche-dezimalzahlen-e5-k2-s6-v3 (bank/brueche-dezimalzahlen/e5.jsonl:28), brueche-dezimalzahlen-e5-k2-s7-v1 (bank/brueche-dezimalzahlen/e5.jsonl:29), brueche-dezimalzahlen-e5-k2-s7-v2 (bank/brueche-dezimalzahlen/e5.jsonl:30), brueche-dezimalzahlen-e5-k2-s7-v3 (bank/brueche-dezimalzahlen/e5.jsonl:31), brueche-dezimalzahlen-e5-k2-s8-v1 (bank/brueche-dezimalzahlen/e5.jsonl:32), brueche-dezimalzahlen-e5-k2-s8-v2 (bank/brueche-dezimalzahlen/e5.jsonl:33), brueche-dezimalzahlen-e5-k2-s8-v3 (bank/brueche-dezimalzahlen/e5.jsonl:34), brueche-dezimalzahlen-e5-k2-s9-v7 (bank/brueche-dezimalzahlen/e5.jsonl:41), brueche-dezimalzahlen-e5-k2-s9-v8 (bank/brueche-dezimalzahlen/e5.jsonl:42).
- Gegenprobe: brueche-dezimalzahlen lernblatt: `__` → `\leerfeld` in den drei Zeilen → 0 Fehlerzeilen (vorher 25); s9-v1 war Folgefehler.
- Vorschlag: **Bankzeile** – `__` im Lückensatz durch `\leerfeld` ersetzen (bank.md: aufgabe trägt `\leerfeld` nur im Lückensatz, das Gerüst gehört nach antwort). 13 Zeilen, alle in brueche-dezimalzahlen.

### K3 – `\dreieck` mit `$…$` in den Beschriftungen

- Meldung: Missing $ inserted – die Vorlage setzt die sechs Labels selbst in `$…$`.
- Im Lauf: 2 Stellen, Bankzeilen: pythagoras-e1-k2-s2-v1.
- In der Bank gesamt: 25 Zeilen – flaechen-e3-k1-s0-v1 (bank/flaechen/e3.jsonl:1), flaechen-e3-k1-s0-v2 (bank/flaechen/e3.jsonl:2), flaechen-e3-k1-s0-v3 (bank/flaechen/e3.jsonl:3), flaechen-e3-k1-s0-v4 (bank/flaechen/e3.jsonl:4), flaechen-e3-k1-s3-v1 (bank/flaechen/e3.jsonl:13), flaechen-e3-k1-s3-v2 (bank/flaechen/e3.jsonl:14), flaechen-e3-k1-s3-v3 (bank/flaechen/e3.jsonl:15), flaechen-e3-k4-s4-v1 (bank/flaechen/e3.jsonl:42), pythagoras-e1-k1-s0-v2 (bank/pythagoras/e1.jsonl:2), pythagoras-e1-k1-s0-v3 (bank/pythagoras/e1.jsonl:3), pythagoras-e1-k1-s0-v4 (bank/pythagoras/e1.jsonl:4), pythagoras-e1-k2-s0-v2 (bank/pythagoras/e1.jsonl:6), pythagoras-e1-k2-s0-v3 (bank/pythagoras/e1.jsonl:7), pythagoras-e1-k2-s0-v4 (bank/pythagoras/e1.jsonl:8), pythagoras-e1-k2-s2-v1 (bank/pythagoras/e1.jsonl:14), pythagoras-e1-k2-s2-v2 (bank/pythagoras/e1.jsonl:15), pythagoras-e1-k2-s2-v3 (bank/pythagoras/e1.jsonl:16), pythagoras-e3-k1-s0-v4 (bank/pythagoras/e3.jsonl:4), pythagoras-e3-k2-s1-v1 (bank/pythagoras/e3.jsonl:9), pythagoras-e3-k2-s1-v2 (bank/pythagoras/e3.jsonl:10), pythagoras-e3-k2-s1-v3 (bank/pythagoras/e3.jsonl:11), pythagoras-e3-k2-s1-v4 (bank/pythagoras/e3.jsonl:12), pythagoras-e3-k2-s1-v5 (bank/pythagoras/e3.jsonl:13), pythagoras-zone-f3-v2 (bank/pythagoras/zone.jsonl:12), pythagoras-zone-f3-v4 (bank/pythagoras/zone.jsonl:14).
- Gegenprobe: pythagoras lernblatt: eine Zeile (e1-k2-s2-v1) auf `{45\text{ cm}}…{90^\circ}` → 0 Fehlerzeilen (vorher 51); alle 18 anderen Stellen waren Folgefehler.
- Vorschlag: **Bankzeile** – Beschriftungen ohne `$`: `{45\text{ cm}}`, `{90^\circ}` (Befund der Render-Probe vom 27.09., unverändert 25 Zeilen: pythagoras 17, flaechen 8). Alternativ Vorlage: `\dreieck` könnte die Labels mit `\ensuremath` statt `$…$` setzen, dann gingen beide Schreibweisen.

### K4 – `\saeulenab[… ylabel=$P(X = k)$ …]` – `=` im Optionswert ohne Klammern

- Meldung: Extra }, or forgotten $ – pgfkeys zerlegt den Wert am `=`.
- Im Lauf: 2 Stellen, Bankzeilen: binomialverteilung-e5-k1-s1-v1, binomialverteilung-e5-k1-s5-v1.
- In der Bank gesamt: 9 Zeilen – binomialverteilung-e5-k1-s1-v1 (bank/binomialverteilung/e5.jsonl:5), binomialverteilung-e5-k1-s1-v2 (bank/binomialverteilung/e5.jsonl:6), binomialverteilung-e5-k1-s1-v3 (bank/binomialverteilung/e5.jsonl:7), binomialverteilung-e5-k1-s1-v4 (bank/binomialverteilung/e5.jsonl:8), binomialverteilung-e5-k1-s1-v5 (bank/binomialverteilung/e5.jsonl:9), binomialverteilung-e5-k1-s5-v1 (bank/binomialverteilung/e5.jsonl:19), binomialverteilung-e5-k1-s5-v2 (bank/binomialverteilung/e5.jsonl:20), binomialverteilung-e5-k3-s4-v2 (bank/binomialverteilung/e5.jsonl:49), kenngroessen-von-verteilungen-e1-k5-s3-v2 (bank/kenngroessen-von-verteilungen/e1.jsonl:39).
- Gegenprobe: binomialverteilung lernblatt: `ylabel={…}` in drei Aufrufen → 0 Fehlerzeilen (vorher 55, darunter der Abbruch „Emergency stop“).
- Vorschlag: **Bankzeile** – `ylabel={$P(X = k)$ in \%}` mit Klammern (Befund der Render-Probe, unverändert 9 Zeilen). Alternativ Vorlage: der Optionsparser von `\saeulenab` könnte `ylabel` als letzten Schlüssel mit Rest der Zeichenkette lesen – aufwendiger.

### K5 – `\wertetabelle{…}{…}{…} \\` – Zeilenumbruch nach dem Blockbaustein

- Meldung: There's no line here to end – `\wertetabelle` endet mit `\par`.
- Im Lauf: 8 Stellen, Bankzeilen: quadratische-funktionen-e1-k1-s10-v1, quadratische-funktionen-e1-k1-s7-v1, quadratische-funktionen-e1-k2-s1-v1, quadratische-funktionen-e1-k2-s3-v1.
- In der Bank gesamt: 7 Zeilen – quadratische-funktionen-e1-k1-s7-v1 (bank/quadratische-funktionen/e1.jsonl:25), quadratische-funktionen-e1-k1-s7-v2 (bank/quadratische-funktionen/e1.jsonl:26), quadratische-funktionen-e1-k1-s7-v3 (bank/quadratische-funktionen/e1.jsonl:27), quadratische-funktionen-e1-k1-s10-v1 (bank/quadratische-funktionen/e1.jsonl:34), quadratische-funktionen-e1-k1-s10-v2 (bank/quadratische-funktionen/e1.jsonl:35), quadratische-funktionen-e1-k2-s1-v1 (bank/quadratische-funktionen/e1.jsonl:38), quadratische-funktionen-e1-k2-s3-v1 (bank/quadratische-funktionen/e1.jsonl:44).
- Gegenprobe: quadratische-funktionen lernblatt: `\\` nach `\wertetabelle` gestrichen → 0 Fehlerzeilen (vorher 8).
- Vorschlag: **Bankzeile** – das `\\` nach `\wertetabelle{…}` streichen (der Baustein schließt den Absatz selbst; vor ihm reicht ein Leerraum oder ebenfalls kein `\\`). 7 Zeilen in quadratische-funktionen. Anleitung könnte den Satz „Blockbaustein, kein `\\` danach“ tragen; in der Vorlage ließe sich ein folgendes `\\` mit `\@ifnextchar` schlucken.

### K6 – Antwortgerüst mit `$…<…$`: Zusammenbau setzt `$<$` in ein offenes `$…$`

- Meldung: Command \item/\end{list} invalid in math mode – Mathe bleibt offen.
- Im Lauf: 2 Stellen, Bankzeilen: reelle-zahlen-e1-k1-s5-v1, reelle-zahlen-e1-k1-s9-v1.
- In der Bank gesamt: 6 Zeilen – reelle-zahlen-e1-k1-s5-v1 (bank/reelle-zahlen/e1.jsonl:19), reelle-zahlen-e1-k1-s5-v2 (bank/reelle-zahlen/e1.jsonl:20), reelle-zahlen-e1-k1-s5-v3 (bank/reelle-zahlen/e1.jsonl:21), reelle-zahlen-e1-k1-s9-v1 (bank/reelle-zahlen/e1.jsonl:31), reelle-zahlen-e1-k1-s9-v2 (bank/reelle-zahlen/e1.jsonl:32), reelle-zahlen-e1-k1-s9-v3 (bank/reelle-zahlen/e1.jsonl:33).
- Gegenprobe: reelle-zahlen lernblatt: `$< \sqrt{6} $<$$` → `$< \sqrt{6} <$` → 0 Fehlerzeilen (vorher 10).
- Vorschlag: **Zusammenbau** – `antwortfeld()` setzt `<`/`>` nur außerhalb `$…$` in Mathe (heute: nur, wenn kein `$` oder `\` direkt davor steht). Die 6 Bankzeilen (reelle-zahlen e1 k1 s5, s9) brauchen Mathe im Gerüst wegen `\sqrt{}`; sie sind nach bank.md („Gerüst wie auf dem Blatt“) vertretbar.

Vorlage: keine der sechs Klassen ist ein Fehler in mathblatt.sty; bei K3, K4 und K5 könnte die Vorlage nachsichtiger werden (oben je genannt), der Fehler liegt aber in der Schreibweise der Zeile gegen die Anleitung.

Strukturprüfung des Zusammenbaus (bau/_alle/bericht.md): sie meldete K1 und K2 („^/_ außerhalb Mathe“) und die zwei `\rechnung`-Stellen in quadratische-funktionen e3/e4 – die kompilieren hier ohne Fehlermeldung (das Bild dieser Stellen wurde nicht angesehen). Nicht gesehen hat sie K3–K6: `$` in Argumenten, die der Baustein selbst in Mathe setzt; `=` in Optionswerten; `\\` nach einem Blockbaustein; das Gerüst aus antwort. Vorschlag Zusammenbau: die vier Muster in `modusfehler()` bzw. `pruefe_struktur()` aufnehmen, dazu die Argumentliste der Bausteine mit „setzt selbst Mathe“ aus der Anleitung.

## Fehlende Zeichen

„Missing character: There is no X“ in der .log heißt: das Zeichen fehlt in der Schrift, im PDF steht nichts. Kein Fehler, kein Hinweis auf dem Blatt. Zählung über gesamt.tex und loesungen.tex beider Läufe (ein Zeichen zählt in jeder Datei, in der es gesetzt wird):

| Zeichen | Vorkommen |
| --- | --: |
| ≈ (U+2248) | 223 |
| α (U+03B1) | 92 |
| π (U+03C0) | 70 |
| γ (U+03B3) | 53 |
| β (U+03B2) | 47 |
| ↔ (U+2194) | 40 |
| ∫ (U+222B) | 24 |
| ₂ (U+2082) | 18 |
| ₁ (U+2081) | 18 |
| ⇔ (U+21D4) | 17 |
| ℝ (U+211D) | 17 |
| ⊂ (U+2282) | 15 |
| ⁻ (U+207B) | 14 |
| ✓ (U+2713) | 12 |
| ⁴ (U+2074) | 12 |
| σ (U+03C3) | 10 |
| ′ (U+2032) | 10 |
| μ (U+03BC) | 9 |
| ℤ (U+2124) | 9 |
| ℚ (U+211A) | 9 |
| ∩ (U+2229) | 8 |
| δ (U+03B4) | 8 |
| ≙ (U+2259) | 7 |
| ℕ (U+2115) | 7 |
| ⁵ (U+2075) | 6 |
| ⁶ (U+2076) | 5 |
| ⁿ (U+207F) | 4 |
| ☐ (U+2610) | 4 |
| ε (U+03B5) | 4 |
| ₃ (U+2083) | 3 |
| ˣ (U+02E3) | 2 |
| ≠ (U+2260) | 2 |
| ⁷ (U+2077) | 2 |
| ∪ (U+222A) | 2 |
| ϱ (U+03F1) | 1 |
| ∈ (U+2208) | 1 |
| ⁸ (U+2078) | 1 |

Betroffen (Lernblatt gesamt.tex): 33 von 70 Einträgen – winkel-dreiecke 62 (α 25, γ 19, β 12); trigonometrie 44 (≈ 30, β 6, α 2); kreis 37 (≈ 27, π 8, α 2); pyramide-kegel-kugel 18 (≈ 16, π 2); reelle-zahlen 18 (⊂ 6, ℕ 3, ℤ 3); normalverteilung-und-sigma-regeln 11 (σ 6, μ 5); uneigentliche-integrale 8 (∫ 8); zufallsexperimente-und-pfadregeln 8 (↔ 4, ∩ 2, ∪ 2); rekonstruktion-von-bestaenden 6 (∫ 6); zuordnungen 6 (↔ 6); rekonstruktion-von-funktionsgleichungen 5 (≈ 5); unabhaengigkeit 5 (∩ 5); binomialverteilung 4 (≈ 2, μ 2); pythagoras 4 (≈ 4); schnittmengen 4 (☐ 4); umkehrfunktion 4 (ℝ 4); wahrscheinlichkeit 4 (↔ 4); zinsrechnung 3 (≈ 3); ableitung-und-aenderungsrate 2 (⇔ 2); bruchrechnung 2 (↔ 2); flaechen 2 (π 2); grenzwerte-und-verhalten-im-unendlichen 2 (ˣ 2); koerper 2 (π 2); konfidenzintervalle 2 (σ 2); potenzen-wurzeln 2 (≈ 2); prozentrechnung 2 (↔ 2); quadratische-gleichungen 2 (≈ 2); tangente-normale-schnittwinkel 2 (⁻ 2); trigonometrische-funktionen 2 (≈ 2); abstaende 1 (≈ 1); geraden 1 (✓ 1); rotationsvolumen 1 (≈ 1); strahlensaetze 1 (≙ 1).

In der Bank tragen 624 Zeilen diese Zeichen, fast alle im Textmodus (804 im Text, 65 in `$…$` – dort meldet XeTeX sie ebenfalls, weil auch die Mathe-Schrift sie nicht als Unicode kennt). Dazu kommen Titel aus den Mappen („Bruch ↔ Dezimalzahl“, Befund der Render-Probe).

Vorschlag: **Vorlage.** Eine Zuordnungstabelle in mathblatt.sty (`\RequirePackage{newunicodechar}`, je Zeichen `\newunicodechar{≈}{\ensuremath{\approx}}`, `{α}{\ensuremath{\alpha}}`, … für die 37 Zeichen der Tabelle) setzt sie im Text und in Mathe richtig; Gegenprobe: winkel-dreiecke (62 fehlende Zeichen) und trigonometrie (44) mit dieser Tabelle im Vorspann → 0 fehlende Zeichen, 0 Fehler. Die Alternative – 624 Bankzeilen auf `$\approx$`, `$\alpha$` umschreiben – ist teurer und bank.md verlangt sie nicht (Umlaute und Sonderzeichen „direkt“). Die Tabelle kann nach dem Umbau der Vorlage als Regel in bank.md stehen: erlaubt sind genau die Zeichen der Tabelle.

## Weitere Beobachtungen aus der .log

- Überbreite Zeilen (`Overfull \hbox` über 5 pt): 145 im Lernblatt, 136 in schwach. Lernblatt am meisten: lineare-gleichungssysteme 29, gleichungen-loesen 28, quadratische-funktionen 16, matrizen-und-uebergangsprozesse 13, lineare-funktionen 11, kenngroessen-von-verteilungen 9, zufallsexperimente-und-pfadregeln 9, binomische-formeln 6. Meist lange Formeln oder Grafiken neben Text; im Lauf nicht geprüft, ob sie über den Rand ragen.
- `Package mathblatt Warning`: 55 im Lernblatt (lineare-funktionen 4, quadratische-funktionen 4, symmetrie-abbildungen 4, trigonometrische-funktionen 4, winkel-dreiecke 4, strahlensaetze 3, koerper 2, kurvenuntersuchung 2, pythagoras 2, stammfunktion-und-hauptsatz 2, wahrscheinlichkeit 2, ableitung-und-aenderungsrate 1, brueche-dezimalzahlen 1, extremalprobleme 1, flaecheninhalt-durch-integration 1, funktionsklassen-und-eigenschaften 1, gleichungen-loesen 1, hypothesentests 1, kenngroessen-von-verteilungen 1, konfidenzintervalle 1, lineare-gleichungssysteme 1, punkte-und-strecken-im-koordinatensystem 1, pyramide-kegel-kugel 1, quadratische-gleichungen 1, rekonstruktion-von-funktionsgleichungen 1, scharen-von-geraden-und-ebenen 1, schnittmengen 1, tangente-normale-schnittwinkel 1, trigonometrie 1, vektoren-und-rechenoperationen 1, vierfeldertafel 1, zufallsgroessen-und-verteilungen 1, zuordnungen 1), 121 in schwach – Hauptnummern, die nicht auf eine Seite passen (Vorlage bricht sie dann doch um). Deckt sich mit den 227 WARNUNG-Zeilen des Zusammenbaus (Halbseitenmaß), das v0.1 nur im Fokus teilt.
- Nicht geprüft: Seitenbild (Lage der Grafiken, Felder neben Streifen, Abhakseite mit Zone) – nur Log und Seitenzahl, kein Blick aufs PDF. Das ist der nächste Schritt, sobald die sechs Klassen behoben sind: je Eintrag ein Blick auf die Seiten mit WARNUNG.

## Dateien

- render.py – der Lauf (Arbeitskopie unter $RENDER_ARBEIT, Standard /tmp/render-alle; PDFs bleiben dort).
- ergebnis.json – alle Messwerte je Eintrag, Lauf und Datei; Fehlerstellen mit Bankzeile-id und Zuordnungsgüte.
- logs/<eintrag>-<lauf>-<datei>.txt – je Versuch die ersten 60 Fehlerzeilen der .log mit drei Kontextzeilen.
- bericht.py – baut diese Datei aus ergebnis.json; Deutung und Vorschläge stehen im Skript.
- Gegenproben liefen in Arbeitskopien außerhalb des Repos (Bankzeilen und Skripte unverändert).

# Renderfehler in der Bank – behoben 2026-09-28

Quellen: bericht.md und ergebnis.json dieses Ordners (Klassen K1–K5 in Bankzeilen, K6 im Zusammenbau), bau/hefte/bericht.md und bau/fokus/bericht.md (Abschnitte „ausgelassen“), bau/layout-befunde.md Punkt 31.

Weg: jede Zeile einzeln geändert (JSON-Zeile neu geschrieben, alle anderen Zeilen der Datei byte-gleich), danach `python3 werkzeuge/bank-pruef.py <eintrag>`, danach Probe: die Zeile allein in einem Minimaldokument (`\documentclass[11pt]{article}`, `\usepackage{mathblatt}` aus hz-0801/blattbau@1acddaa, `\begin{aufgabe}{Probe}`) gesetzt, wie werkzeuge/zusammenbau.py v0.7 sie setzt – `teile_normal()` (teile bzw. gleichungsraster), `teil_schwach()` (schwach-Satz) und die Lösung in `\erg`, bei loesungsgrafik mit der Grafik darunter –, je `xelatex -interaction=nonstopmode -halt-on-error -file-line-error`, TeX Live 2023 nach werkzeuge/render.md. „Probe ok“ heißt: alle drei Dokumente ohne Fehlerzeile, PDF entstanden. Vor der Änderung warf dieselbe Probe bei allen Stichproben den Fehler des Berichts (K1–K5, Dimension too large); sie misst also, was der Render-Lauf gemessen hat.

## Ergebnis

- 144 Zeilen in 10 Einträgen geändert, alle 144 Proben ok.
- Davon 135 in den Quellen genannt, 9 mit demselben Fehler, aber nicht genannt (potenz-exponentialfunktionen lief im Render-Lauf über alle Einträge nicht mit; die Probe zeigte bei allen neun vor der Änderung „There's no line here to end“). In der Tabelle mit „(gleiches Muster)“ markiert.
- `bank-pruef.py`: 0 Abweichungen in allen betroffenen Einträgen; quadratische-funktionen meldet weiter 1 Abweichung „Dateiname weg.jsonl“ – die bestand vorher, betrifft die Datei weg.jsonl, keine Bankzeile, und bleibt.
- Folgefehler ohne eigene Ursache (bau/hefte: binomialverteilung Nr. 56c, brueche-dezimalzahlen Nr. 22i und 9i; bau/render-alle: 48 Stellen) brauchen keine Änderung; sie fallen mit ihrer Ursache weg.

## Je Zeile

| id | Fehler | Änderung | Probe ok |
| --- | --- | --- | --- |
| binomialverteilung-e5-k1-s1-v1 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s1-v2 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s1-v3 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s1-v4 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s1-v5 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s5-v1 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k1-s5-v2 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| binomialverteilung-e5-k3-s4-v2 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e4-k1-s8-v3 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e4-k1-s8-v4 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s6-v1 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s6-v2 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s6-v3 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s7-v1 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s7-v2 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s7-v3 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s8-v1 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s8-v2 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s8-v3 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s9-v7 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| brueche-dezimalzahlen-e5-k2-s9-v8 | Missing $ inserted – `__` als Lücke im Textmodus | `__` → `\leerfeld` in aufgabe (Lückensatz), antwort `__` → leer | ja (normal, schwach, Lösung) |
| daten-e2-k2-s11-v2 | Dimension too large – `\saeulenab` mit Werten bis 90\,000 | `\saeulenab` mit Werten bis 90\,000 (pgfmath rechnet nur bis 16\,383) → Werte in Tausend (90/10/10, 81/75/54); die Achse ist ohne Zahlen, das Bild bleibt gleich (5,4 Kästchen für D) – wie die Schwesterzeile s11-v1 | ja (normal, schwach, Lösung) |
| daten-e5-k1-s6-v1 | Dimension too large – ksys-x-Achse mit Jahreszahlen | `ksys` mit Jahreszahlen auf der x-Achse (x bis 2025 → Maß über 16\,384 pt) → `\saeulenab` mit denselben Werten, Jahren als Kategorien und abgeschnittener y-Achse (ymin bleibt); loesung „jeder Punkt“ → „jede Säule“ | ja (normal, schwach, Lösung) |
| daten-e5-k1-s10-v1 | Dimension too large – ksys-x-Achse mit Jahreszahlen | `ksys` mit Jahreszahlen auf der x-Achse (x bis 2025 → Maß über 16\,384 pt) → `\saeulenab` mit denselben Werten, Jahren als Kategorien und abgeschnittener y-Achse (ymin bleibt) | ja (normal, schwach, Lösung) |
| daten-e5-k1-s10-v2 | Dimension too large – ksys-x-Achse mit Jahreszahlen | `ksys` mit Jahreszahlen auf der x-Achse (x bis 2025 → Maß über 16\,384 pt) → `\saeulenab` mit denselben Werten, Jahren als Kategorien und abgeschnittener y-Achse (ymin bleibt) | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s0-v1 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s0-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s0-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s0-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s3-v1 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s3-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k1-s3-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| flaechen-e3-k4-s4-v1 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld loesungsgrafik | ja (normal, schwach, Lösung) |
| kenngroessen-von-verteilungen-e1-k5-s3-v2 | Extra }, or forgotten $ – `=` im Optionswert `ylabel` ohne Klammern | `ylabel={…}` geklammert (`=` im Optionswert) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e1-k1-s3-v1 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e1-k1-s3-v2 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e1-k1-s3-v3 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e1-k4-s3-v1 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e2-k2-s0-v1 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e2-k2-s0-v2 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e2-k2-s0-v3 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e2-k2-s0-v4 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e3-k3-s3-v1 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| potenz-exponentialfunktionen-e5-k4-s3-v1 (gleiches Muster) | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| pythagoras-e1-k1-s0-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k1-s0-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k1-s0-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s0-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s0-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s0-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s2-v1 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s2-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e1-k2-s2-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k1-s0-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k2-s1-v1 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k2-s1-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k2-s1-v3 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k2-s1-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-e3-k2-s1-v5 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-zone-f3-v2 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| pythagoras-zone-f3-v4 | Missing $ inserted – `$…$` in `\dreieck`-Beschriftung (Vorlage setzt selbst `$…$`) | Beschriftungen in `\dreieck` ohne `$` (Einheit in `\text{}`), Feld grafik | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k1-s7-v1 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (3×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k1-s7-v2 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (3×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k1-s7-v3 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (3×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k1-s10-v1 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (3×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k1-s10-v2 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (3×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k2-s1-v1 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| quadratische-funktionen-e1-k2-s3-v1 | There's no line here to end – `\\` nach `\wertetabelle` (Blockbaustein endet mit `\par`) | `\\` nach `\wertetabelle` gestrichen (1×) | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s1-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s1-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s1-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s1-v4 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s1-v5 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s3-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s3-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s3-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s5-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s5-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s5-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s7-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s7-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s7-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s8-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s8-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s8-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s9-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s9-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s9-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s10-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s10-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e1-k2-s10-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s1-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s1-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s1-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s1-v4 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s1-v5 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s2-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s2-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s2-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s3-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s3-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s3-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s4-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s4-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s4-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s6-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s6-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s6-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s7-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s7-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s7-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s8-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s8-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e2-k1-s8-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s1-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s1-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s1-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s1-v4 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s1-v5 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s2-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s2-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s2-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s3-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s3-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s3-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s4-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s4-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s4-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s5-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s5-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s5-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s6-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s6-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s6-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s7-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s7-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s7-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s9-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s9-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s9-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s11-v1 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s11-v2 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| quadratische-gleichungen-e3-k3-s11-v3 | Missing $ inserted – Gleichung ohne `$` im Feld aufgabe (gleichungsraster, `\gl{\text{…}}`) | aufgabe in $…$ gesetzt | ja (normal, schwach, Lösung) |
| zuordnungen-e1-k1-s0-v1 | Tabelle mit einer Wertespalte statt drei (layout-befunde 31) | `\wertetabelleleer{…}{…}{3}` → `\wertetabelle{Zeit in h}{Weg in km}{~,~,~}` (drei leere Wertespalten; `\wertetabelleleer` fasst die Spalten per `\multicolumn` zu einer zusammen) | ja (normal, schwach, Lösung) |

## Zusammenbau

Nicht in der Bank behoben, weil die Ursache nicht in der Zeile liegt:

| id | Fehler | Ursache | Vorschlag |
| --- | --- | --- | --- |
| reelle-zahlen-e1-k1-s5-v1 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |
| reelle-zahlen-e1-k1-s5-v2 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |
| reelle-zahlen-e1-k1-s5-v3 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |
| reelle-zahlen-e1-k1-s9-v1 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |
| reelle-zahlen-e1-k1-s9-v2 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |
| reelle-zahlen-e1-k1-s9-v3 | K6: Command \item/\end{list} invalid in math mode (Probe am unveränderten Stand bestätigt) | `antwortfeld()` setzt `<`/`>` hinter `$` nochmals in `$…$`: aus `__ $< \sqrt{6} <$ __` wird `$< \sqrt{6} $<$$`, Mathe bleibt offen | `antwortfeld()` wandelt `<`/`>` nur außerhalb von `$…$` um; das Gerüst der Zeile entspricht bank.md |

Vorlage (mathblatt.sty, nicht Zusammenbau, der Vollständigkeit halber): `\wertetabelleleer{…}{…}{n}` fasst die n Wertespalten mit `\multicolumn{n}` zu einer Zelle zusammen – das ist die Ursache von layout-befunde Punkt 31 („nur eine Wertespalte statt drei“; die Zeile ist zuordnungen-e1-k1-s0-v1, nicht potenz-exponentialfunktionen – sie steht im Heft msa-funktionen direkt nach dessen Einträgen). Behoben ist nur die genannte Zeile (Tabelle jetzt über `\wertetabelle` mit drei leeren Spalten). Dasselbe Bild haben 14 weitere Zeilen, die `\wertetabelleleer` nutzen und nicht geändert sind: zuordnungen-e1-k1-s0-v2 bis v4, funktionsklassen-und-eigenschaften-e6-k1-s4-v1 bis v3 und -s10-v1, -v2, lineare-gleichungen-e1-k3-s2-v1 bis v3 und -s5-v1 bis v3. Vorschlag: in der Vorlage `\multicolumn` streichen und je Zeile n leere Zellen setzen (`*{n}{& }`), dann sind alle 15 Zeilen ohne Bankänderung richtig.

Nicht Teil dieses Laufs: fehlende Zeichen (Vorlage, Abschnitt „Fehlende Zeichen“ im Bericht) und der Tabellenkopf im Mathemodus (layout-befunde Punkt 26, „Zeitinh“), der auch die geänderte Radfahrer-Zeile betrifft.

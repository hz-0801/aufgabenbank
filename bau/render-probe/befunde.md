# Render-Probe: Befunde

Stand 2026-09-27. xelatex (TeX Live 2023, Ubuntu-Paket) mit mathblatt.sty = hz-0801/blattbau@36b7b12. Weg und Einrichtung: werkzeuge/render.md.

## Lernblatt Prozentrechnung (Zusammenbau v0.1)

bau/prozentrechnung/2026-09-27/lernblatt/, je Datei zwei Läufe; PDFs in bau/render-probe/lernblatt/.

| Datei | Seiten | Fehler | fehlende Zeichen |
| --- | --- | --- | --- |
| blatt0.tex | 1 | 0 | ↔ (U+2194) |
| gesamt.tex | 8 | 0 | ↔ (U+2194) |
| lernblatt.tex | 7 | 0 | – |
| loesungen.tex | 2 | 0 | – |

## Grafikbausteine

Je Baustein bis zu fünf verschiedene grafik-Felder der Bank, reihum über die Einträge; Satz wie im Zusammenbau (aufgabe → teile → \teil, darunter die Grafik). Kompilierläufe der Probe: 83 (dazu 16 für Lernblatt und Einrichtung). Gezählt: Fehler (`!`), fehlende Zeichen, Überbreite über 5 pt. Quelltexte und PDFs in bau/render-probe/bausteine/.

- geprüft: 83 Bausteine, fehlerfrei 80, mit Befund 3
- Grafikbausteine ohne Bankzeile (nicht prüfbar): 21
- Gerüstbausteine (aufgabe, teile, feld …): 52, stecken nicht in grafik-Feldern; die im Lernblatt benutzten sind mit ihm fehlerfrei durchgelaufen

## Deutung

Beide Fehlerbilder liegen in den Bankzeilen, nicht in der Vorlage. Gegenprobe je Fall ein eigenes .tex in gegenprobe/ (6 Läufe, damit 105 Kompilierläufe insgesamt).

1. `\dreieck`: Die Vorlage setzt alle sechs Labels (#4–#9) selbst in `$…$`. Bankzeilen schreiben `{$62^\circ$}` – daraus wird `$$62^\circ$$`, `^` steht im Textmodus → Abbruch. Ohne `^` gibt es keinen Fehler, aber falschen Satz: `{$41$ cm}` erscheint als „41cm“ (Leerzeichen weg, cm kursiv), `{$g$}` als aufrechtes g. Gegenprobe: `{62^\circ}` und `{41\text{ cm}}` setzen richtig. Betroffen: 25 Bankzeilen (Suche über alle grafik- und loesungsgrafik-Felder): flaechen-e3-k1-s0-v1…v4, -s3-v1…v3, flaechen-e3-k4-s4-v1 (loesungsgrafik), pythagoras-e1-k1-s0-v2…v4, -e1-k2-s0-v2…v4, -e1-k2-s2-v1…v3, -e3-k1-s0-v4, -e3-k2-s1-v1…v5, pythagoras-zone-f3-v2, -v4. bank-pruef.py prüft das nicht.
2. `\saeulenab`: `ylabel=$P(X = k)$ in \%` – das `=` im Wert zerlegt die Option (key=value). Mit Klammern `ylabel={$P(X = k)$ in \%}` fehlerfrei; `$P(X \le k)$` ohne `=` geht auch ohne Klammern. Betroffen: 9 Zeilen, binomialverteilung-e5-k1-s1-v1…v5, -s5-v1, -s5-v2, -e5-k3-s4-v2, kenngroessen-von-verteilungen-e1-k5-s3-v2. Andere Optionswerte mit `=` gibt es in der Bank nicht.
3. `\saeulen` ist selbst fehlerfrei: Die eine Zeile mit Befund (binomialverteilung-e5-k1-s5-v2) trägt daneben das `\saeulenab` aus 2.
4. Lernblatt: `↔` fehlt in Latin Modern und bleibt leer – im Titel „Bruch ↔ Dezimalzahl …“ (prozentrechnung-e1-k1-s4-*, -zone-f2-*). Kein Abbruch, im PDF fehlt nur das Zeichen.

Nicht geprüft: loesungsgrafik-Felder (außer den gezählten Mustern), Seitenbild und Lage der Grafiken (nur Log, kein Blick aufs PDF).

## Einzelbefunde

### Mit Befund

#### `\dreieck` – 1 von 5 (Bank: 79 Zeilen mit dem Baustein)

- `pythagoras-e1-k1-s0-v2`: 24 Meldungen; Fehler: Missing $ inserted. \| <inserted text> $ // Fehler: Extra }, or forgotten $. \| <recently read> }
- Folgefehler nach der kaputten Zeile bis \end{document} (offene minipage), hier nicht gezählt

#### `\saeulen` – 1 von 5 (Bank: 9 Zeilen mit dem Baustein)

- `binomialverteilung-e5-k1-s5-v2`: 19 Meldungen; Fehler: Extra }, or forgotten $. \| \saeulenab code ...(\i ,\sabymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,fon // Fehler: Undefined control sequence. \| \saeulenab code ...bymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,font=\small
- Folgefehler nach der kaputten Zeile bis \end{document} (offene minipage), hier nicht gezählt

#### `\saeulenab` – 2 von 5 (Bank: 30 Zeilen mit dem Baustein)

- `binomialverteilung-e5-k1-s1-v1`: 18 Meldungen; Fehler: Extra }, or forgotten $. \| \saeulenab code ...(\i ,\sabymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,fon // Fehler: Undefined control sequence. \| \saeulenab code ...bymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,font=\small
- `kenngroessen-von-verteilungen-e1-k5-s3-v2`: 18 Meldungen; Fehler: Extra }, or forgotten $. \| \saeulenab code ...(\i ,\sabymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,fon // Fehler: Undefined control sequence. \| \saeulenab code ...bymin ) {\k }; \else \node [below,font=\small ,inner sep=4pt] at (\i ,\sabymin ) {\k }; \fi } \draw [-{Stealth[length=2mm]}] (0,\sabymin ) -- (0,\sabo ) node[above right,font=\small
- Folgefehler nach der kaputten Zeile bis \end{document} (offene minipage), hier nicht gezählt

### Fehlerfrei

`\rechenplatz` (5), `\streifen` (5), `\wertetabelle` (5), `\wertetabelleleer` (5), `\begin{ksys}` (5), `\gerade` (5), `\punkt` (5), `\steigungsdreieck` (5), `\parabel` (5), `\funktion` (5), `\funktionab` (5), `\begin{ksys3}` (5), `\rpunkt` (5), `\rvektorab` (5), `\rgerade` (5), `\rebene` (1), `\rebenepar` (4), `\rquader` (5), `\rpyramide` (5), `\dreieckrw` (5), `\quader` (5), `\zylinder` (5), `\prismadreieck` (5), `\pyramide` (5), `\kegel` (5), `\kugel` (3), `\begin{kreis}` (5), `\mittelpunkt` (5), `\kreispunkt` (2), `\radius` (5), `\durchmesser` (4), `\sektor` (3), `\geradenkreuzung` (5), `\parallelenpaar` (5), `\winkel` (5), `\winkelstrahl` (4), `\viereck` (5), `\parallelogramm` (5), `\rechteck` (5), `\trapez` (5), `\raute` (5), `\drachen` (5), `\netzquader` (1), `\netzpyramide` (5), `\netzzylinder` (3), `\strahlensatz` (5), `\baumzwei` (5), `\liniendia` (2), `\baumdreigleich` (5), `\baumdrei` (5), `\kreisdiagramm` (5), `\kreisleer` (2), `\sachtabelle` (5), `\leerzelle` (5), `\kreissektor` (5), `\vierfeldertafel` (5), `\binomialverteilung` (5), `\normalverteilung` (5), `\ableitungspaar` (1), `\flaeche` (5), `\tangentean` (5), `\hochpunkt` (1), `\tiefpunkt` (5), `\wendepunkt` (3), `\asymptote` (5), `\zahlenstrahl` (5), `\begin{zahlengerade}` (5), `\intervall` (5), `\bruchkreis` (5), `\bruchrechteck` (5), `\termbaum` (2), `\tb` (2), `\einheitskreis` (5), `\sinus` (1), `\streifenleer` (3), `\streifenfeld` (5), `\begin{dreisatz}` (5), `\dsz` (5), `\dsp` (5), `\dsleer` (5)

### Grafikbausteine ohne Bankzeile

`\feld`, `\rvektor`, `\sehne`, `\tangente`, `\bogen`, `\netzwuerfel`, `\balkenab`, `\saeule`, `\kreisdiagrammleer`, `\strichliste`, `\begin{boxplots}`, `\bp`, `\histogramm`, `\flaechezwischen`, `\intervallo`, `\kosinus`, `\streifenvoll`, `\streifenfrage`, `\streifenreihe`, `\streifenwertreihe`, `\mbstreifenrahmen`

### Gerüstbausteine (nicht Gegenstand der Grafikprobe)

`\blattfuss`, `\blattkopf`, `\star`, `\einheitenkopf`, `\verz`, `\zweigzeile`, `\verfahren`, `\verzeichniszeile`, `\verztrenn`, `\begin{abhakseite}`, `\abhakgruppe`, `\abhak`, `\abhakauto`, `\aufgabe`, `\weit`, `\uebersichtskasten`, `\begin{aufgabe}`, `\begin{teile}`, `\teil`, `\steil`, `\begin{teilezwei}`, `\tz`, `\leerfeld`, `\stz`, `\begin{geruest}`, `\gz`, `\gzs`, `\begin{gleichungsraster}`, `\gl`, `\sgl`, `\anweisung`, `\beispiel`, `\rechnung`, `\begin{beispiel}`, `\mbox`, `\feldl`, `\punktfeld`, `\janein`, `\kreuz`, `\mnliste`, `\nullstellenliste`, `\punktprobenliste`, `\begleitteil`, `\erg`, `\hilfeseite`, `\begin{schritte}`, `\schritt`, `\achtung`, `\swz`, `\swa`, `\swb`, `\swfrage`

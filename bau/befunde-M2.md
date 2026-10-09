# Befunde M2 – Prüfstein „Kathete berechnen“ (T6B, 09.10.2026)

Je Zeile ein Befund aus dem Bau, der über diese Einheit hinausgeht; Entscheidung des Agenten in Klammern.

- Lerneinheit 2 trägt im Katalog zwei Blätter (Kathete berechnen; Umkehrung). Die Lernweg-Vorlage kennt nur „Lerneinheit <n>“; Schritt-Kennungen hier „L2k-<n>“, Block „Lerneinheit 2 – Kathete berechnen (erster Teil)“. (Vorschlag: Lerneinheiten im Katalog so schneiden, wie Blätter entstehen – 2a Kathete, 2b Umkehrung.)
- Das Feld schritt in bank.md ist als "L<einheit>-<n>" definiert; für ein Teilblatt passt das nicht. (L2k-<n> gesetzt, bank.md nicht geändert.)
- `katalog/_vorlage.md` setzt „Lernweg“ nach „Lerneinheiten“; dort eingefügt verschiebt der Block alle Zeilennummern, und das Bankfeld quelle (Zeilennummer) bricht in allen Zeilen des Eintrags (bank-pruef --katalog: Abweichungen). (Block ans Ende vor „Prüfliste“ gesetzt; Vorschlag: Lernweg in der Vorlage ans Ende oder quelle auf Abschnittsnamen umstellen.)
- `werkzeuge/bank-pruef.py` kannte die Lernweg-Felder aus bank.md (09.10.) nicht und meldete „unbekanntes Feld“; auch das Feld bild (06.10.) fehlte. (In FELDER_WAHL ergänzt.)
- bank-pruef verlangt ein einheitliches merkmal je Sprosse; das Merkmal einer neuen Lernweg-Zeile (was sie gegenüber dem vorigen Schritt ändert) passt oft nicht dazu. (Merkmal der Sprosse übernommen; das eigene steht im Lernweg-Block.)
- Lernweg-Schritte liegen quer zu den Bank-Ketten: L2k-1 (Idee) und L2k-3 (Umstellen) fanden Platz nur in der Pflichtkette k6 (begruenden, darstellung), L2k-6 nutzt k3 s7, s11 und k6 s3. Die Mengenwarnungen des Prüfers (pflicht begruenden 5×, Menge 3) entstehen daraus.
- Die Bank-Grundfälle k3-s1 v1–v5 haben vierstellige Quadrate (85² − 36²) und die Antwortform „a² = __“ (Bauregel Antwortfeld verbietet sie); als schwach markiert, besser = neue Zeile v6.
- Bank-Vorstufe k3-s0 „Plus oder minus?“ verrät mit „Kathete gesucht – minus“ die Regel; die Gliederung (A6) wollte sie schon ersetzen. Neue Vorstufe s0-v5 mit Dreiecken in vier Lagen; s0-v1–v4 nicht als schwach markiert, weil sie einen anderen Schritt (Text statt Figur) bedienen.
- Kein Setzer (`werkzeuge/setzer.py`) vorhanden; Blatt von Hand nach K4W gesetzt. Für M2 („mit einem Setzer-Rohling gesetzt“, Setzzeit) fehlt damit die Messung.
- Kein Agent-Werkzeug in der Sitzung; der Kritiker lief über `claude -p --model fable` mit Zweck und PDF-Pfaden.
- Kritiker-Vorschlag „Kasten mit den drei Schritten vor Nr. 5“ nicht übernommen: Bauregel kein Merkkasten (1.5), der Weg steht grau in 5 a). „Antwortsatz und Ansatz mit Streckennamen“ nicht übernommen: Lernblatt ohne Sätze, die nur der Prüfung dienen (4.1); Nr. 10 verlangt die Strecken schon durch die Namen. „Skizze in Nr. 9“ übernommen.
- Satzfehler nach der letzten Runde: In Nr. 8 berührt die Beschriftung B die Maßlinie „90 m“ (Kompiliergrenze erreicht, nicht mehr nachgesetzt).
- `werkzeuge/duplikate.py` schreibt `duplikate.md` über alle 73 Einträge neu (Diff ~2000 Zeilen); nicht committet. Gemeldet für die neuen Zeilen nur B-327 (k6-s2-v4/v5, gleicher Bau mit anderen Zahlen, gewollt als „neue Zahlen“).

## Lehrer 09.10. zu T6B: „insgesamt gut“ (Abnahme M2, Teil Bau)

- Überschrift sagt schon „Kathete berechnen“, die Päckchen sagen noch einmal „Berechne die andere/fehlende Kathete“: dort verrät der Text die Entscheidung. Vorschlag zum Ende von M2: in Päckchen „die fehlende Seite“, und im Päckchen mit krummen Zahlen ein Fall, in dem die Hypotenuse fehlt (Unterscheiden statt Erkennen am Wort); in Sachaufgaben steht schon die Sachgröße.
- Originalliste am Blattende: im Lernblatt entbehrlich (Marke im Rand genügt); bleibt im Prüfungsblatt/-heft (Stark-Heft). Vorschlag zum Ende von M2.
- Mischen Hypotenuse/Kathete gehört voll in „Das Dreieck erst finden“ (nächste Einheit); in T6B nur Nr. 2 und Nr. 8.
- Länge 10 Aufgaben / 3 Seiten, letzte halb leer: in Ordnung.

## Setzer (werkzeuge/setzer.py, 09.10.2026)

- Setzzeit 3,7 s für drei PDFs (je zweimal xelatex, parallel); Text wortgleich mit T6B, Seitenbilder (pdftoppm -r 60) bis auf die Kennung pixelgleich; Seitenumbrüche gleich. Kennung des Setzer-Laufs 3S2 im Register (gleicher Inhalt wie T6B); `--kennung 3S2` setzt ihn wieder aus den Register-ids.
- Feld satz trägt Auftragstext, Fuß-Ergebnisse und Lösungsweg noch einmal neben aufgabe/loesung: zwei Quellen derselben Sache. bank-pruef prüft pruef gegen loesung, nicht gegen satz.fuss/satz.loesung. (Offen: zum Ende von M2 entscheiden, ob satz.loesung loesung ersetzt oder bank-pruef auch satz prüft.)
- Satz kann nur, was die vier Formen zwei/reihe/paeckchen/frei abdecken (aus T6B abgeleitet); K4W (Hypotenuse) hat noch kein satz-Feld und ist nicht setzbar (nicht angefasst). Beim Nachziehen von K4W zeigt sich, ob die Formen reichen.
- bank-pruef meldete TikZ in grafik als „Baustein nicht in _bausteine.md“; TikZ-Bilder sind jetzt von der Bausteinprobe ausgenommen (das Bild prüft das Kompilieren).
- Die Übersicht liest eine Zeile „Serie:“ am Kopf des Lernweg-Abschnitts im Katalog (neu in _vorlage.md); Vorgänger/Nachfolger und Niveau aus der Zeile „Blatt:“ des Blocks.
- Originalliste am Blattende setzt der Setzer wie T6B, obwohl der Lehrer sie im Lernblatt entbehrlich fand (oben); Schalter erst mit der Entscheidung zum Ende von M2.
- Setzer liest den Katalog aus ../mathe-nachhilfe/katalog neben dem Repo (sonst `--katalog DIR`).

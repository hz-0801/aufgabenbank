# Bauauftrag – eine Lerneinheit bauen

Stand 10.10.2026 (Lehrer: Go für den Musterauftrag). Kern ist
`bau/muster-auftrag.md` (Prüfstein `bau/proben/2026-10-09/hypotenuse-muster/`,
7 min, Lehrer: „die Aufgaben sind gut“): Lage und Zweck statt Regeln
(Befund `mathe-nachhilfe/befund-selbstlernheft-2026-10-09.md`). Der
frühere Auftrag liegt in `bau/archiv/bauauftrag-2026-10-09.md`.
Handwerk bei Zweifel: `bau/bauregeln.md`; Zeilenform: `bank.md`.

## Lage

Aus der Bestellung; fehlt sie, gilt die Standardlage:
- Wer: die Klasse, die der Katalog an der Einheit nennt.
- Sicher kann er die Voraussetzungen aus dem Katalog; bei Neuem unsicher.
- Er arbeitet allein. Das ist der Maßstab, auch wenn später ein Lehrer
  daneben sitzt.
- Ziel: Prüfungsniveau (P10, sonst die Prüfung des Katalogs).

## Zweck

Der Schüler soll (1) sehen, was alles dazugehört, und (2) jede Fertigkeit
allein lernen und üben können, bis zur Zielaufgabe. Erfolgskriterium: Ein
unsicherer Schüler kommt ohne Hilfe durch jeden Abschnitt. Brille: der
schwache Schüler, der oft scheitert und nur bestehen will. Wenig Text,
nichts Nebulöses. Lieber mehr Aufgaben; jedes Element muss dem Schüler
nützen. Keine Seitengrenze.

Maß für das Tischblatt (tisch-alt): T6B und M74 ohne Nr. 2 und 3
(`bau/proben/2026-10-09/hypotenuse-berechnen/2-blatt.pdf`); so nachgerüstet:
H7U (`bau/proben/2026-10-10/nachruest-test/`).

## Eingaben – sparsam

Nur mit grep/awk/Python-Filter, nie ganze große Dateien:
- Katalog `mathe-nachhilfe/katalog/<eintrag>.md`: die Zeile der Einheit
  unter „Lerneinheiten“ und „Typen je Lerneinheit“, „Typische Fehler“,
  „Prüfungsform“, „Thema-Weg“, einen vorhandenen Lernweg-Block.
- Bank `bank/<eintrag>/e<n>.jsonl` nur als Vorbild: Typen und Fallen
  (je Zeile sprosse_text, aufgabe gekürzt). Nicht abschreiben.
- Originale (`mathe-nachhilfe/msa/gliederung/`) wünschenswert, kein Muss:
  Vorbild für Form und Falle; Sache, Zahlen und Wortlaut immer neu.

## Vorgehen (in dieser Folge, nicht abkürzen)

1. **Lernweg von oben**, bevor eine Aufgabe entsteht: rückwärts von
   typischen Zielaufgaben – was muss er dafür können, in welcher Folge?
   Plan aufschreiben (plan.md im Bauordner). Den Thema-Weg prüfen,
   ergänzen, umordnen, auch um Ungenanntes, das zur Zielaufgabe gehört.
2. **Je Abschnitt**: Kennung (A, B, …); ein Merksatz – ein klarer Satz,
   höchstens zwei; Formel; ein vollständig vorgerechnetes Beispiel in
   Schritten, mit Skizze, wo sie hilft – schritte nur die Rechnung, die
   erklärenden Sätze ins Feld erklaerung (nur Selbstlernheft; im
   Tischblatt steht als graues a) nur die Rechnung, knapp wie M74);
   Aufgaben von leicht bis Zielniveau, jede Stufe ändert eine Sache, jede
   trägt stufe (basis, kern, ziel; bank.md).
   - **Erkennen zuerst:** Die erste Stufe des Lernwegs fragt nur „Wo ist
     …, welche … ist …?“ an mehreren Figuren in verschiedener Lage, ohne
     Rechnen (wie M74 Nr. 1); dann aufstellen, dann rechnen.
   - **Päckchen:** je Rechenschritt eine Nummer mit 3–6 Teilaufgaben
     (bank.md paeckchen, teil, probe; im Block mit „+“ verbunden), a)
     grau vorgerechnet, Rest selbst, mit Probe, wo sinnvoll (wie M74
     Nr. 4/6, T6B Nr. 5). Zerfällt ein Verfahren in Schritte, erst je
     Schritt ein Päckchen (nur Schritt 1, nur Schritt 2), dann beide.
   - **Einstieg wirklich leicht:** je Schritt beginnt es mit basis: ein
     Schritt, kleine Zahlen, teils vorgemacht.
3. **Ziel**: Die Denk-Sach-Aufgaben, in denen der Schüler das Modell
   selbst erkennt (kein gezeichnetes Dreieck, keine vorgegebene
   Gleichung) und danach entscheidet oder vergleicht (reicht es? passt
   es? um wie viel?), stehen gesteigert am Ende des Lernwegs, die
   stärkste zuletzt (wie M74 Nr. 7/8) – nicht mitten im Blatt. Ein
   Abschnitt davor darf mit einer kleineren Zielaufgabe enden. Am Ende
   muss kein Original stehen. Gegenbeispiel: ein fertiges Dreieck mit
   bloßer Geschichte drumherum.
4. **Nicht:** Rätsel- oder Herleitungsbilder (Quadrate zählen,
   Zerlegungsbeweis), Fehler-finden-Aufgaben, Merkkasten neben dem
   Beispiel, vorgegebene Ergebnisform, die einen Schritt erspart.
   Alle Aufgaben sind neu; die Bank ist nur Vorbild.
5. **Vorrat (Pflicht, nur für die Bank):** je Abschnitt mindestens eine
   leichtere Aufgabe und mindestens zwei gleichwertige; bei Abschnitten
   mit mehreren Rechenschritten mehr (je Schritt eine). Sie stehen nicht
   auf dem Blatt, damit beim Nachbestellen („mehr B“) nichts fehlt.
6. **Zahlen und Lösungen:** alles mit sympy nachrechnen; Zahlen so wählen,
   dass glatte Werte herauskommen, wo das Rechnen nicht das Thema ist.
   Lösung: Ergebnis kurz (Feld ergebnis), Weg in kurzen Schritten.

## Ablage (Zerlegen)

- **Bank** `bank/<eintrag>/e<n>.jsonl`: jede Aufgabe, jedes Beispiel und
  jeder Vorrat als Zeile im Format von `bank.md` (in die passende Kette
  und Sprosse, neue Variante), mit den Lernweg-Feldern und abschnitt,
  rolle, modell_selbst_finden, ergebnis, stufe, schritte und erklaerung
  (Beispiel), paeckchen, teil, probe (Päckchen). Blattzeilen
  status gut erst nach dem Kritiker; Vorrat ohne status.
- **Lernweg-Block** im Katalog unter „Lernweg“ in der Form `abschnitte`
  (Muster: `katalog/pythagoras.md`, Lerneinheit 1, Kennung H7U): Kopf
  (Stand mit Kennung, Kritiker: offen, Ziel, Blatt, Titel, Formel, In
  Worten, Vorgehen, Achtung, Bild, Fehler, Tisch) und je Abschnitt eine
  Zeile `| L<n>-<B> | Name | Satz | Formel | Beispiel | Aufgaben | Vorrat |`
  mit Bank-ids. Gibt es schon einen Block, bleibt er darunter als
  „frühere Fassung (<Kennung>)“; nichts löschen. Den Thema-Weg anlegen
  oder ergänzen, wenn der Bau die Folge ändert.
- **Kennung** nach `bau/bauregeln.md` „Kennung“; die Registerzeile in
  `bau/register.csv` schreibt der Setzer beim ersten Satz. Die Kennung
  zu Beginn des Baus reservieren: `python3 werkzeuge/setzer.py <eintrag>
  <teil> --reserviere` (Zeile „reserviert“ im Register, gepusht).
- Setzen ohne Modell, alle drei Sorten:
  `python3 werkzeuge/setzer.py <eintrag> <teil> --aus <ordner> --sorte
  tisch-alt|tisch|selbst` (Blatt- und Lösungs-PDF je Sorte).

## Prüfen vor der Abgabe

- sympy für jede Zahl; `python3 werkzeuge/bank-pruef.py <eintrag>`
  (0 Abweichungen); `python3 werkzeuge/duplikate.py` (neue ids nur als
  gewollte Zahlvarianten; duplikate.md nicht committen).
- Anfänger-Test: Schafft er die erste Aufgabe jedes Abschnitts mit dem
  Beispiel allein? Kein Sprung zwischen Stufen.
- Alle Seiten aller Sorten als Bild ansehen (`pdftoppm -r 60`): Skizzen
  passen zu den Zahlen, nichts abgeschnitten. Auch die Vorratsskizzen
  einmal setzen und ansehen.

## Kritiker und Nachbesserung

6. **Kritiker** startet der Chat, nicht der Bau-Agent: ein zweiter Agent
   als erfahrener Lehrer, der den Schüler vor sich sieht, mit Lage und
   Zweck, nur die PDFs, ohne Regeln: Gesamturteil in einem Satz (würdest
   du es ihm so geben?), Mängel nach Gewicht mit Seite und Vorschlag,
   höchstens drei Stärken, die bleiben müssen. Bis dahin steht im Block
   „Kritiker: offen“.
7. **Nachbesserung** genau der benannten Punkte, sonst nichts; wieder
   sympy und Bildkontrolle der geänderten Seiten; danach Kritiker im
   Block „durch (…; übernommen: …)“ und status gut an den Blattzeilen.

## Bericht (höchstens 250 Wörter)

Start- und Endzeit; Abschnitte (Kennung, Name); Zahl der Aufgaben auf dem
Blatt und im Vorrat; Prüfmeldungen (bank-pruef, duplikate, Bildkontrolle);
Commits; Pfade der PDFs.

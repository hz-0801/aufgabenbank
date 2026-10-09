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
unsicherer Schüler kommt ohne Hilfe durch jeden Abschnitt. Wenig Text,
nichts Nebulöses. Jedes Element muss ihm nützen; im Zweifel weglassen.

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
2. **Je Abschnitt** (etwa eine Seite): Kennung (A, B, …); ein Merksatz –
   ein klarer Satz, höchstens zwei; Formel; ein vollständig vorgerechnetes
   Beispiel in Schritten, knapp, mit Skizze, wo sie hilft; 3–5 Aufgaben
   von leicht bis Zielniveau, jede Stufe ändert eine Sache; erst erkennen
   und aufstellen, dann rechnen. Ein roter Faden ist erlaubt.
3. **Ziel**: Jeder Abschnitt und das Ganze (Probetest am Ende) enden mit
   einer Aufgabe, in der der Schüler das Modell selbst erkennt (kein
   gezeichnetes Dreieck, keine vorgegebene Gleichung) und danach
   entscheidet oder vergleicht (reicht es? passt es? um wie viel?).
   Gegenbeispiel: ein fertiges Dreieck mit bloßer Geschichte drumherum.
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
  rolle, modell_selbst_finden, ergebnis, schritte (Beispiel). Blattzeilen
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

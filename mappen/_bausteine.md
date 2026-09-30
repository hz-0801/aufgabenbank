# Bausteine der Vorlage

Quelle: hz-0801/blattbau, Anleitung_mathblatt.md, Commit dbac9c1af0d023b4b40629d07bd8245c7a6bdcf0 (2026-09-26T06:53:15+02:00, „vorlage: Stufe 6, Anleitung, CHANGELOG“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-30 08:12 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern. werkzeuge/bank-pruef.py liest hieraus Namen und Argumentzahl der Bausteine.

## Kurzreferenz

Alle Zeilen der Anleitung, die mit `\` oder `\begin{` beginnen (auch eingerückt), je Block unter dessen Überschrift.

### Grundgerüst

````text
\blattfuss{Lineare Funktionen}{Lernblatt Teil 1 von 3}   → Thema · Bezeichnung unten links, Seite unten rechts
\blattkopf{...}{...} / \blattkopf*{...}{...}{$\star$ = ...}  → Alternative: oben links; mit * dazu Legende unten links, Text im dritten Argument
\einheitenkopf{Einheit 3 von 5 · Prozentwert berechnen}   → Zwischenüberschrift über der ersten Hauptnummer einer Einheit: fette Zeile
\einheitenkopf*{Einheit 3 von 5 · Prozentwert berechnen}  → dieselbe Zeile, zusätzlich ein Trennstrich über die volle Zeilenbreite darunter
\einheitenkopf[e3]{Einheit 3 von 5 · Prozentwert berechnen}  → dieselbe Zeile, dazu das Sprungziel e3 für \verz{e3}{...}; Sternform: \einheitenkopf*[e3]{...}
\einheitenkopf[e3][3 Prozentwert]{Einheit 3 von 5 · Prozentwert berechnen}  → Kurzform für die Kopfzeile selbst gesetzt; ohne sie bildet die Vorlage „3 Prozentwert berechnen"; ohne Ziel: \einheitenkopf[][Zone]{...}
\zweigzeile{Den Prozentwert ausrechnen · neu in diesem Jahr · P10 oft}   → zweite Zeile des Einheitenkopfs, kleiner, direkt darunter
\verfahren{Nullstellen aus der Scheitelpunktform}   → Zwischenzeile zwischen Einheitenkopf und Hauptnummern, wenn eine Einheit mehrere Verfahren nacheinander übt: halbfett, etwas größer als der Text, hängt an der folgenden Hauptnummer
\verzeichniszeile{\verz{zone}{Kennst du schon} \verztrenn \verz{e1}{Einheit 1 · Prozentsatz} \verztrenn \verz{abhaken}{Das kann ich}}   → klickbare Verzeichniszeile am Blattanfang
\begin{abhakseite} \abhakgruppe{Einheit 1 · Prozentsatz} \abhak{11}{Ich kann ...} \end{abhakseite}   → Seite „Das kann ich" zum Abhaken
\abhakauto     → dieselbe Seite, aus den Titeln aller \aufgabe-Köpfe gesammelt, \verfahren als Gruppenzeile (zweiter xelatex-Lauf)
\weit                                                    → Schreibraum: Zeilen im Aufgabenteil gut halb so weit wie eng; Begleitteil und Hilfe-Seite setzen selbst auf eng zurück
\uebersichtskasten[<Leitgrafik>]{<Formelzeilen>}          Zeilen mit \\ getrennt, kein & (kein tabular – „Misplaced alignment tab" im Log heißt: & im Kasten); Sternlegende nicht hier, sondern über \blattkopf*
   \uebersichtskasten{Plusklammer: \quad $a + (b - c) = a + b - c$ \\ Minusklammer: \quad $a - (b - c) = a - b + c$}
\begin{aufgabe}{Text} ... \end{aufgabe}            → nummeriert, bleibt auf einer Seite
\begin{teile} \teil ... \steil ... \end{teile}     → a), ☆b)
\begin{teilezwei} \tz ... & \tz ... \\ \tz ... & \tz ... \end{teilezwei}   → zweispaltig, Buchstaben und Textanfänge in derselben Flucht wie in teile; Regel: mehr als vier kurze Teilaufgaben hierhin statt in geruest – kurz heißt: Text vor dem Feld höchstens etwa 25 Zeichen bei \leerfeld, 30 bei \feld; längere Teilaufgaben in teile, sonst läuft die Zelle in die Nachbarspalte oder das Feld rutscht in der Zelle in eine eigene Zeile; tabular-Syntax: & trennt die Spalten, \\ beendet die Zeile, Stern mit \stz; ist die Zahl der Teilaufgaben ungerade, bleibt die zweite Zelle der letzten Zeile leer (\tz ... & \\) – die letzte Teilaufgabe steht dann wie eine Zeile aus teile da
\begin{geruest} \gz{a}{$y=2x+3$}{\feld{m}\feld{n}} \gzs{b}{...}{...} \end{geruest}
\begin{gleichungsraster}[2] \gl{x+5=9} & \gl{x-3=4} \\ \gl[3]{2x+3=11} & \sgl[3]{7-2x=15} \\ \end{gleichungsraster}   → zweispaltig, unter jeder Gleichung Schreibzeilen (grau, 9 mm) für die senkrechte Umformung; Regel: jede Hauptnummer, deren Lösung eine Umformung untereinander ist (Gleichungen, Systeme, Klammern auflösen), hierhin statt in teilezwei, ohne \feld{x}; optionales Argument = Schreibzeilen je Gleichung (Standard 2), je Gleichung mit \gl[n] überschreibbar; Zeilenende \\ wie in teilezwei
\anweisung{Rechne mit dem Taschenrechner. Runde auf eine Stelle.}   → Anweisungszeile zwischen zwei Teilaufgaben in teile, teilezwei, gleichungsraster und geruest: volle Breite, der Buchstabe läuft weiter, in zweispaltigen Umgebungen beginnt die nächste Teilaufgabe links
\rechenplatz{4}   \rechenplatz[halb]{4}   → leerer Block mit vier Zeilen à 12 mm und hellgrauen Linien, volle bzw. knapp halbe Breite; steht nach Titel und Anweisung dort, wo früher das Beispiel stand
\beispiel{x + 5 &= 9 &&\mid -5 \\ x + 5 - 5 &= 9 - 5 \\ x &= 4}   → „Beispiel:“ und senkrechte Rechnung: & vor dem Gleichheitszeichen, && vor der Umformung oder dem Kommentar, \\ trennt die Zeilen; Text in \text{...}: \beispiel{x + 4 &= 7 && x = 3 \\ 3 + 4 &= 7 \\ 7 &= 7 && \text{(wA)}\quad x = 3 \text{ ist Lösung}}
\rechnung{5x - 8 &= 12 &&\mid -8 \\ 5x &= 4}   → dieselbe Rechnung ohne „Beispiel:“ (Vorgabe in Fehler-finden-Aufgaben, Rechenweg im Begleitteil)
\begin{beispiel} Angabe \streifen{40}{$0$}{10 Kinder} \rechnung{...} Antwort: ... \end{beispiel}   → Beispielblock: eingerückt, hellgrauer Rahmen, erste Zeile „Beispiel:", alles an einem Blickort
\feld{W} → „W = ___" (2 cm); \leerfeld → „___" (3 cm) ohne Bezeichner (nie \feld{} – das ergibt „= ___"); Einheit als optionales Argument: \leerfeld[\%] → „___ %“, \feld[cm]{l} → „l = ___ cm“ – Feld und Einheit bleiben zusammen, kein \mbox nötig; ein Umbruch vor dem Feld ist erlaubt, aber teuer, TeX dehnt die Zeile nur, wenn der Umbruch schlechter wäre; ist die Zeile vor dem Feld im Render sichtbar gedehnt, setze \\ vor den Feldtext („\\ Gesamtpreis: \leerfeld[€]" in eigener Zeile) – nie den Aufgabentext kürzen
\feld{m}  \feldl{y}  \punktfeld  \janein  \kreuz{Text}      \janein ohne Argument → „☐ ja ☐ nein"; andere Beschriftungen mit \kreuz{A}\kreuz{B} – ein \janein[...] gibt es nicht; ab drei Kästchen oder bei Aussagen länger als ein paar Wörter jedes \kreuz in eigener Zeile (\\ dazwischen), nebeneinander bricht die Aussage mitten im Satz um
\mnliste[9]{2x+3, 5x-1, ...}            m und n je Gerade, eine Zeile statt geruest
\nullstellenliste[7]{x-4, 2x-6, ...}    x_0 je Gerade
\punktprobenliste[7]{2x-1/A(3|5), ...}  Punktprobe mit ja/nein
\begleitteil   \erg{3}{a) ... \quad b) ...}     Teillösungen durch \quad getrennt, kein |
\hilfeseite    \verfahren{Name} \begin{schritte} \schritt ... \achtung{...} \end{schritte}   (\verfahren wie oben)
````

### Die Umgebung `beispiel` fasst ein gedrucktes Beispiel zu ein …

````text
\begin{beispiel}
\streifen{40}{$0$}{10 Kinder}
\rechnung{1 \text{ Kästchen} &= 10\,\% \\ 4 \text{ Kästchen} &= 40\,\%}
\end{beispiel}
````

### Wertetabelle

````text
\wertetabelle{x}{y}{-2,-1,0,1,2}              leer
\wertetabelle[7,4,1,-2,-5]{x}{f(x)}{-2,-1,0,1,2}   gefüllt (Begleitteil)
\wertetabelle[,4,,-2,-5]{x}{f(x)}{-2,-1,0,1,2}     teilweise gefüllt: leerer Eintrag = leeres Feld (ab 2026-09-06e)
\wertetabelleleer{x}{y}{5}                    Schüler legt selbst an
````

### Koordinatensystem 2D

````text
\begin{ksys}[xmin=-4,xmax=4,ymin=-5,ymax=5]            Zeichenfläche (Karo 8 mm)
\begin{ksys}[xmin=-5,xmax=5,ymin=-5,ymax=5,ablesen]    Ablesegrafik (Karo 6 mm)
\begin{ksys}[...,klein]                                Lösungsgrafik (Karo 3,5 mm)
\begin{ksys}[leit]                                     Leitgrafik im Übersichtskasten (Karo 6 mm, −3..3, etwa 4 cm)
\begin{ksys}[xmin=0,xmax=30,ymin=0,ymax=240,xstep=5,ystep=40,xlabel=t in min,ylabel=W in l]
  \gerade{2}{-1}{g}   \gerade[1.5]{2}{-1}{g}   \punkt{2}{3}{A}   \steigungsdreieck{0}{-1}{2}
  \parabel{1}{-1}{-2}{p}      y = a(x-d)^2+e
  \funktion{0.5*\x^2-2}{f}    \funktionab{1/\x}{f}{0.2}{4}
\end{ksys}
````

### Koordinatensystem 3D (Kavalierprojektion)

````text
\begin{ksys3}                                                     Oberstufe: x_1, x_2, x_3; Karo 5 mm
\begin{ksys3}[x1min=-2,x1max=6,x2min=-3,x2max=6,x3min=-2,x3max=5]   Voreinstellung; Bereiche ganzzahlig
\begin{ksys3}[xyz]                                                Sek I: Achsen x, y, z
\begin{ksys3}[...,x1schritt=2]                                    x1 nur bei 2, 4, 6 beziffert
\begin{ksys3}[leit]                                               Leitgrafik im Übersichtskasten: Karo 4 mm, alle Achsen 0..2
  \rpunkt{4}{4}{4}{A}                    Punkt mit Lot: entlang x1, dann parallel x2, dann parallel x3
  \rpunkt[below right]{6}{-2}{-1}{C}     Labelposition wie bei TikZ-Knoten (Voreinstellung above right)
  \rpunkt*{1}{1.5}{1.5}{S}               Punkt ohne Lot: Durchstoß-, Schnitt-, Spurpunkt
  \rvektor{2,4,3}{\vec a}                Ortsvektor vom Ursprung, Label in der Pfeilmitte
  \rvektorab[below]{1,1,0}{4,5,2}{\vec u}   Pfeil von A nach B; optionales Argument = Labelposition
  \rgerade{0,-2,1}{1,1,0.5}{g}           Stützpunkt, Richtungsvektor; läuft bis zum Rand des Achsenbereichs
  \rgerade[-1:1.5]{3,1,-1}{0,1,2}{h}     Parameterbereich t = −1 … 1,5 statt Rand; Label am Ende bei t max
  \rebene{4}{6}{3}{E}                    Spurdreieck aus den Achsenabschnitten x1 = 4, x2 = 6, x3 = 3
  \rebenepar{1,1,1}{2,1,0}{0,2,2}{F}     Parallelogramm: Stützpunkt, zwei Spannvektoren (werden als Pfeile gezeichnet)
  \rebenepar*{0,0,3}{4,0,1}{0,5,0}{D}    Sternform: Fläche ohne Spannvektorpfeile (Dach, Wand, Glasscheibe)
  \rquader{1,1,0}{3}{4}{2}               Quader: Ecke mit den kleinsten Koordinaten, Kanten a (x1), b (x2), c (x3)
  \rpyramide{1,3,0}{2}{3}{2,4.5,4}       Rechteckpyramide: Ecke, Grundkanten a (x1), b (x2), Spitze als Tripel
\end{ksys3}
````

### Geometrie und Körper (Maße in cm)

````text
\dreieckrw{4}{3}{a}{b}{c}                          rechtwinklig bei C
\dreieck{(0,0)}{(5,0)}{(1.5,3)}{a}{b}{c}{\alpha}{\beta}{\gamma}
\quader{4}{2}{3}{a}{b}{c}   \zylinder{1.2}{3}{r}{h}   \prismadreieck{4}{2.5}{2}{g}{h}{l}
\pyramide{4}{3}{3.5}{a}{b}{h}      Rechteckpyramide: Grundkanten a (vorn), b (Tiefe), Höhe h; quadratisch mit a = b
\kegel{1.5}{3}{r}{h}{s}            Radius, Höhe; Labels r, h, s (Mantellinie)
\kugel{1.5}{r}                     Radius
````

### Kreis und Winkelfiguren

````text
\begin{kreis}[2]                     Radius in cm (Voreinstellung 2)
  \mittelpunkt{M}                    \kreispunkt{110}{B}   \kreispunkt[above right]{110}{B}
  \radius{40}{r}                     \durchmesser{0}{d}    \sehne{200}{340}{s}
  \tangente{300}{t}                  Tangente im Randpunkt, rechter Winkel markiert
  \sektor{30}{110}{\alpha}           \bogen{30}{110}{b}
\end{kreis}
\geradenkreuzung{35}{\alpha}{\beta}{\gamma}{\delta}    zwei Geraden durch einen Punkt
\parallelenpaar{60}{\alpha}{\beta}{\gamma}{\delta}     zwei Parallelen mit Schnittgerade
\winkel{40}{\alpha}   \winkel[4]{40}{\alpha}           einzelner Winkel, Schenkellänge in cm
\winkelstrahl   \winkelstrahl[9]   \winkelstrahl[7][A]   Strahl zum Antragen: Scheitel links (Vorgabe S), waagerecht nach rechts, Länge in cm (Vorgabe 7), darüber 4 cm frei
````

### Vierecke, Netze, Strahlensatz (Maße in cm)

````text
\viereck[seiten={a,b,c,d},diagonalen,hoehe,winkel]{(0,0)}{(5,0)}{(6,3)}{(1.5,3.5)}   Ecken A, B, C, D gegen den Uhrzeigersinn
\parallelogramm[seiten={a,b,a,b},hoehe,winkel={\alpha,\beta,,}]{4}{2.5}{60}       a, b, Winkel alpha
\rechteck[achsen=beide]{4}{2.5}       \trapez[hoehe=h]{5}{3}{2.5}   a unten, c oben (mittig), h
\raute[achsen=diagonalen,diagonalen]{4}{2.5}   Diagonalen e (waagerecht), f
\drachen[achsen=senkrecht,diagonalen]{4}{3}{0.35}   e senkrecht, f quer, t = Anteil von e bis zur Querdiagonale
\netzquader{3}{1.5}{2}{a}{b}{c}   \netzwuerfel{1.5}{a}   \netzpyramide{2.5}{2}{a}{h_s}   \netzzylinder{1}{2.5}{r}{h}
\strahlensatz[strecken={2,3,,5}]{2}{5}{35}          V-Figur: ZA, ZA', Winkel zwischen den Strahlen
\strahlensatz[x,strecken={2,4,a,b}]{2}{4}{30}       X-Figur
\strahlensatz[punkte={Z,A,B,C,D},faktor=1.5]{2}{4}{90}
````

### Stochastik

````text
\baumzwei{R/0.4,B/0.6}{R/0.4,B/0.6}{R/0.4,B/0.6}    zweistufig, Wahrscheinlichkeiten
\baumzwei{R/,B/}{R/,B/}{R/,B/}                      leere Felder zum Eintragen
\saeulen{Mo/12,Di/7,Mi/9}{16}{4}{Anzahl}            Werte, ymax, ystep, Achsentitel
\saeulen{Mo/,Di/,Mi/}{16}{4}{Anzahl}                nur Achsen (Schüler zeichnet)
\saeulenab[ymax=100,ystep=20,yfein=5,ylabel=Gäste]{Mo/45,Di/70,Mi/30}       Säulen zum Ablesen, ohne Wertebeschriftung
\saeulenab[ymax=560,ystep=80,yfein=80,ylabel=Mio.,ohnezahlen,breite=1.8]{Spanisch/480,Englisch/}   Achse ohne Zahlen
\balkenab[xmax=40,xstep=10,xfein=2,xlabel=Nennungen]{Rot/24,Blau/32,Grün/14}    waagerechte Balken zum Ablesen
\balkenab[xmax=40,xstep=10,xfein=2,xlabel=Nennungen]{Leichtathletik/24,Sonstige Sportarten/14}   lange Namen: Platz links wird gemessen, Balken werden kürzer
\liniendia[ymax=20,ystep=5,yfein=1,ylabel=Temperatur in $^\circ$C]{Jan/2,Feb/5,Mär/4}   Liniendiagramm über Kategorien
````

### `\saeulenab`, `\balkenab` und `\liniendia` ergänzen `\saeule …

````text
\baumdreigleich{R/0{,}4,B/0{,}6}                                   dreistufig, alle Stufen gleich (mit Zurücklegen)
\baumdrei{S1}{S2 nach 1. Ast}{S2 nach 2. Ast}{S3 nach 1-1}{S3 nach 1-2}{S3 nach 2-1}{S3 nach 2-2}
\baumdrei{R/\frac{2}{5},B/\frac{3}{5}}{R/\frac{1}{4},B/\frac{3}{4}}{R/,B/}{R/,B/}{R/,B/}{R/,B/}{R/,B/}
\kreisdiagramm{Bus 40 \%/40, Rad 25 \%/25, Auto 20 \%/20, zu Fuß 15 \%/15}
\kreisdiagramm[1.2]{A/3, B/5, /2}       Radius in cm (Voreinstellung 1,8); leeres Label = Sektor ohne Text
\kreisdiagramm{}                         leerer Kreis mit Mittelpunkt (Schüler zeichnet)
\kreisdiagrammleer{Bus/40, Rad/25, Auto/20, Fuß/15}   wie oben, aber ohne Text: aus jedem Sektor führt eine Linie nach außen auf einen Schreibstrich (Zuordnen, Beschriften)
\kreisleer[2.2]                          leerer Kreis mit Mittelpunkt M und einem Radius nach oben (12 Uhr) als Nullmarke, Radius in cm (Voreinstellung 2); zum Antragen eigener Sektoren mit dem Geodreieck, bevor \kreisdiagramm das fertige Bild zeigt
\sachtabelle{lcc}{Medium & Mädchen & Jungen}{Smartphone & 97\,\% & 94\,\%\\ Bücher & 48\,\% & 32\,\%}   Sachtabelle mit Rahmen, Kopfzeile abgesetzt; leere Zelle zum Eintragen: \leerzelle
\strichliste{13}                         Strichliste als Bild: Fünferbündel (vier Striche, der fünfte quer darüber) und der Rest einzeln; Argument ist die Anzahl, z. B. in einer \sachtabelle-Zelle. Die alte Schreibweise \strichliste{|||||\ |||} gilt weiter – besteht das Argument nur aus Strichen und Abständen, zählt das Makro die Striche selbst; die Bündel schreibst du nie von Hand
\kreissektor{135}{135°}                  Kreis mit einem grauen Sektor von 135° ab oben, Label im Sektor
\vierfeldertafel{A}{B}{20,30,50,10,40,50,30,70,100}   zeilenweise B, nicht B, Summe; leere Einträge frei
\vierfeldertafel{A}{B}{}                 alle Felder leer
\binomialverteilung{10}{0.3}                                  Stabdiagramm P(X=k), k = 0..n
\binomialverteilung[von=15,bis=35,markiere=15:22]{50}{0.5}    Ausschnitt, Stäbe 15..22 dunkel
\binomialverteilung[ymax=0.4,ystep=0.1]{5}{0.7}               y-Achse selbst gesetzt
\normalverteilung{0}{1}                                       Dichtekurve, x-Achse in Schritten von sigma
\normalverteilung[von=90,bis=110]{100}{10}                    Fläche grau; nur von oder nur bis = einseitig
\normalverteilung[xstep=10,karo=0.5]{50}{15}
````

### Boxplot und Histogramm

````text
\begin{boxplots}[xmin=0,xmax=20,xstep=2,xlabel=Punkte]
  \bp{4,7,9,13,18}{Klasse 8a}    Minimum, unteres Quartil, Median, oberes Quartil, Maximum
  \bp{}{Klasse 8b}               leere Werte: nur Zeile und Label, Schüler zeichnet selbst
\end{boxplots}
\histogramm[ymax=10,ystep=2,xstep=10,ylabel=$h$]{0:10/4, 10:20/9, 20:30/6}
\histogramm[dichte,ymax=1,ystep=0.2,xstep=10,ylabel=Dichte]{0:10/4, 10:20/9, 20:40/6}
\histogramm[ymax=8,ystep=2,xstep=5]{0:5/, 5:10/, 10:15/}     ohne Werte: Achsen und Klassengrenzen
\histogramm[titel=Histogramm I,ymax=10,ystep=2,xstep=10]{...}   Titel im Textmodus über dem Diagramm
````

### Analysis (im ksys, `\ableitungspaar` freistehend)

````text
\ableitungspaar[xmin=-3,xmax=3,ymin=-2,ymax=4,ymin2=-4,ymax2=4,ablesen]{0.5*\x^2-1}{f}{\x}{f'}
\ableitungspaar[...]{\x^3-3*\x}{f}{}{f'}         unteres System leer: Schüler zeichnet f'
\flaeche{\x^2-4*\x+3}{1}{3}{A}                   Fläche zwischen Graph und x-Achse von 1 bis 3
\flaechezwischen{-\x^2+2*\x+3}{\x+1}{-1}{2}{A}   Fläche zwischen zwei Graphen
\tangentean{0.5*\x^2}{1}{t}                      Tangente in x0 = 1 mit Steigungsdreieck
\tangentean*{0.5*\x^2}{1}{t}                     ohne Steigungsdreieck
\tangentean[\frac{3}{2}]{0.5*\x^2}{1.5}{t}       Steigungstext selbst gesetzt
\hochpunkt{-1}{2}{H}   \tiefpunkt{1}{-2}{T}   \wendepunkt{0}{0}{W}   \wendepunkt[-3]{0}{0}{W}
\asymptote{x=2}{}   \asymptote{y=1}{y=1}   \asymptote{y=0.5*\x}{a}
````

### Zahlen und Algebra

````text
\zahlenstrahl{-3/A, 1.5/B, 4/}                                  Punkte mit Label (leer = nur Markierung)
\zahlenstrahl[xmin=0,xmax=2,xstep=0.25,karo=0.7]{0.5/\frac12}   karo = cm je Schritt
\zahlenstrahl{}                                                 nur die Gerade
\begin{zahlengerade}[xmin=-4,xmax=6]
  \intervall{-2}{3}{[-2;3]}        geschlossen (volle Enden)
  \intervallo[2]{1}{5}{]1;5[}      offen (leere Enden); [2] = zweite Zeile, wenn sich Intervalle überschneiden
  \intervall*[3]{-3}{0}{}          links offen, rechts geschlossen;  \intervallo*  links geschlossen, rechts offen
  \intervallo*[4]{2}{}{x \ge 2}    Grenze leer = Pfeil ins Unendliche
\end{zahlengerade}
\bruchkreis{3}{8}   \bruchkreis[0.8]{1}{3}   \bruchkreis{0}{6}      Teile gefüllt/gesamt; [r] Radius in cm
\bruchrechteck{3}{8}   \bruchrechteck[3]{2}{5}                      [Breite] in cm, Höhe 1 cm
\termbaum{+}{3x}{\tb{\cdot}{2}{y}}           Kinder sind Text (Blatt) oder \tb{Knoten}{Kind}{Kind}
\termbaum{}{\tb{}{5}{x}}{\tb{}{}{}}          leere Knoten = Felder zum Eintragen
````

### Trigonometrie

````text
\einheitskreis{50}                Einheitskreis mit Punkt P, Radius, Winkel alpha, sin und cos als Strecken
\einheitskreis[karo=1.5]{140}     Radius in cm (Voreinstellung 2)
\einheitskreis[ohne]{230}         nur Punkt, Radius und Winkel (Schüler trägt sin/cos ein)
\begin{ksys}[trigo]               x von -pi/2 bis 2pi in pi/2-Schritten (Karo 1 cm), y von -2 bis 2
  \sinus{1}{1}{f}                 a*sin(b*x)      \kosinus{2}{0.5}{g}   a*cos(b*x)
  \hochpunkt{1.5708}{1}{H}        Stellen in Bogenmaß als Dezimalzahl: pi/2 = 1.5708, pi = 3.1416, 2pi = 6.2832
\end{ksys}
\begin{ksys}[trigo,xmax=12.5664,ymin=-3,ymax=3]   bis 4pi (vier Nachkommastellen, sonst fehlt die letzte Zahl)
````

### Prozentrechnung: Streifen und Dreisatz

````text
\streifenleer                                        leerer Streifen (10 cm = 100 %), mit 0 %/50 %/100 % beschriftet
\streifenleer[4]   \streifenleer[0]                   4 statt 10 Teile; [0] ohne Teilstriche, nur 0 % und 100 % (Schüler teilt selbst ein)
\streifenvoll{Rad/40,Bus/25,zu Fuß/20,Auto/15}        vollständig gefüllt, Werte müssen sich zu 100 summieren
\streifen{30}{$0\,\%$}{$100\,\%$}                     ein Abschnitt 0..30 %, Label links/rechts unten
\streifen[5]{30}{$0\,\%$}{$100\,\%$}                  wie oben, nur 5 statt 10 Teilstriche
\streifen[0]{0}{$0\,\%$}{$100\,\%$}                   ohne Teilstriche und ohne Füllung: zum Einteilen durch den Schüler
\streifenfrage{65}{$0\,\%$}{$100\,\%$}                wie \streifen, mit „?“ über der Füllgrenze
\streifenfeld{40}{$0$}{10 Kinder}                     wie \streifen, rechts daneben ein Feld für den abgelesenen Prozentsatz
\streifenreihe{a/20,b/60,c/10,d/90}                   mehrere Streifen a), b), ... untereinander, je 100 %
\streifenwertreihe{a/30/6\,kg/20\,kg, b/70/35\,€/50\,€}   wie \streifenreihe, mit Marke und Werten 0/Teilwert/Ganzwert
\begin{dreisatz}{Hefte}{Preis}
\dsz{4}{6{,}00\,€}
\dsp{:4}{:4}
\dsz{1}{\dsleer}                                      fehlender Wert als Schreiblinie statt \feld
\dsp{\cdot 6}{\cdot 6}
\dsz{6}{9{,}00\,€}
\end{dreisatz}
````

### Option schwach

````text
\swz{Der Streifen sind 20\,€, gefärbt sind 6\,€.}{\streifen{30}{$0\,€$}{$20\,€$}}   Teilaufgabe mit Raster links, Darstellung rechts
\swz[3]{...}{...}                                        drei Schreibzeilen statt zwei
\swa{in 25-\%-Schritte}{\streifen[0]{0}{$0\,\%$}{$100\,\%$}}   Ablese- oder Zeichenteilaufgabe, ohne Raster
\swb{\beispiel{20 \text{ von } 100 &= \tfrac{20}{100} \\ &= 20\,\%}}{\streifenfrage{20}{$0$}{$100$}}   vorgerechnetes Beispiel
\swfrage{Was bleibt gleich, was ändert sich?}            Erklärzeile über die ganze Breite mit zwei Schreibzeilen
````

## Absätze

Wortgleich die Absätze zu \anweisung, \rechenplatz, beispiel, \streifenfeld, \swz.

`\anweisung{...}` setzt eine Anweisung, die für die folgenden Teilaufgaben gilt („Rechne mit dem Taschenrechner.", „Der Streifen sind jetzt immer 60 kg."), zwischen zwei Teilaufgaben statt in den Titel der Hauptnummer („bei b) …"). Bild: nach einem kleinen Abstand eine Zeile über die volle Breite der Hauptnummer, links bündig mit der Nummer, bei langem Text umbrechend; direkt darunter geht es mit dem nächsten Buchstaben weiter, der Zähler wird nicht berührt. Sie steht in `teile`, `teilezwei`, `gleichungsraster` und `geruest` an der Stelle, an der sie gilt. In den zweispaltigen Umgebungen beendet sie die laufende Reihe: Du setzt sie hinter die letzte Teilaufgabe der Reihe (mit oder ohne `\\` davor), die nächste Teilaufgabe beginnt links. Als erster Eintrag der rechten Zelle (`\tz ... & \anweisung{...}`) geht sie nicht. Zwischen zwei Blöcken einer Hauptnummer steht sie als eigener Absatz.

`\rechenplatz{4}` ist der Platz, in den der Lehrer das Gerüst schreibt (Beschluss vom 26.09.2026: im Regelfall kein gedrucktes Beispiel). Er steht nach dem Ich-kann-Titel der Hauptnummer und der Anweisung, an der Stelle, an der bisher das Beispiel stand. Bild: ein leerer Block über die volle Zeilenbreite mit vier hellgrauen Linien im Abstand von 12 mm – dieselben Linien wie bei den Schreibzeilen, aber weiter auseinander (die Schreibzeilen im `gleichungsraster` bleiben bei 9 mm); vier Zeilen sind 48 mm hoch. `\rechenplatz[halb]{4}` ist knapp halb so breit (0,46 der Textbreite) und passt in eine Zelle von `teilezwei` oder neben eine Grafik. Die Zahl der Zeilen ist frei. Der Block bricht nie über die Seite; passt er nicht mehr, rutscht er ganz auf die nächste.

Die Umgebung `beispiel` fasst ein gedrucktes Beispiel zu einem Block zusammen, wenn es eins gibt (Regelfall ist der `\rechenplatz`). Bild: um 1 em eingerückt, hellgrauer dünner Rahmen, erste Zeile „Beispiel:", darunter frei die Gestalt einer Teilaufgabe – Angabe, Darstellung (Streifen, Tabelle), Rechnung mit `\rechnung` oder `\beispiel{...}`, Antwortzeile – untereinander, alles im Rahmen. So liest der Schüler das Beispiel an einem Ort statt an vier (Angabe links, „Beispiel:" darunter, Streifen rechts, Rechnung links). Der Block bricht nicht über die Seite. Teilaufgaben darin (`teile`, `\teil`) verbrauchen keinen Buchstaben; nach dem Block zählt die Hauptnummer weiter, wo sie davor stand.

Der Befehl `\beispiel{...}` (senkrechte Rechnung mit „Beispiel:" davor) und `\rechnung{...}` bleiben unverändert und dürfen in der Umgebung stehen.

`\streifenfeld[Teilstriche]{Füllung}{links}{rechts}` ist `\streifen` mit einem Antwortfeld: Bild ist der gewohnte Streifen, dahinter im gleichen Zeilenabstand `\leerfeld[\%]`, also eine 3 cm lange Linie mit Prozentzeichen. Es ist der Baustein für „lies am Streifen ab und trage ein" – ohne ihn steht das Feld sonst in einer eigenen Zeile unter der Grafik. Rahmen und Teilstriche kommen vom selben `\mbstreifenrahmen` wie bei der übrigen Streifen-Familie, das optionale Argument ist wieder die Zahl der Teilstriche.

`\swz` ist die Rechenteilaufgabe: Buchstabe, Text, darunter die Schreibzeilen (Voreinstellung zwei, im optionalen Argument je Aufgabe änderbar). `\swa` ist die Teilaufgabe ohne Raster – ablesen, ankreuzen, einzeichnen –, sie setzt den Text als einzelne `teile`-Zeile. `\swb` ist das vorgerechnete Beispiel vor einem Päckchen und trägt deshalb keinen Buchstaben. `\swfrage` steht über die ganze Breite und stellt die Erklärfrage zu einem Päckchen. `\swz`, `\swa` und `\swfrage` zählen mit dem Buchstabenzähler der Vorlage weiter und fluchten wie `teile` und `teilezwei`; `\swb` zählt nicht mit.

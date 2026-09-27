# Mappe: potenzen-wurzeln

Eintrag: hz-0801/mathe-nachhilfe, katalog/potenzen-wurzeln.md
Katalog-Commit: 761321330add6ed255669afc1c4e11b846250dd5 (2026-09-25T11:16:56+02:00, „katalog: Marken-Zeilen je Lerneinheit, drei Einheiten ergänzt, marken-bau.py“; ermittelt über git log (GitHub-API gesperrt))
Maßstab: hz-0801/blattbau, unterrichtsblatt.md, Commit 36b7b1216bd31e3ab15e356b63a8ad6ad4a543b1 (2026-09-26T19:14:32+02:00, „prompt: Unterrichtsblatt v4.4 (Befunde Testlauf 25.09.)“; ermittelt über git log (GitHub-API gesperrt))
Datum: 2026-09-27 06:16 UTC
Gebaut mit werkzeuge/mappe.py; nicht von Hand ändern.

Teile: 1 Katalogeintrag · 2 Originale · 3 Maßstab

## 1 Katalogeintrag

Ohne „Status“, „Offene Punkte“ und „Prüfliste“. Die Zahl am Zeilenanfang ist die Zeilennummer beim Katalog-Commit (Feld quelle).

````text
  1  # Potenzen, Zehnerpotenzen und Quadratwurzeln
  3
  4  ### Verortung
  5  Potenzen mit natürlichem Exponenten als fortgesetzte Multiplikation, Zehnerpotenzen und die Darstellung rationaler Zahlen mithilfe von Zehnerpotenzen, Quadrat- und Kubikwurzel als Umkehrung des Potenzierens: Stufe F (Gymnasium Kl. 8 laut Bildungsgangtabelle; Oberschule/Gesamtschule 9–10 regulär). Negative Exponenten (a⁻ⁿ = 1/aⁿ), Näherungswerte für Quadratwurzeln und das Vergleichen reeller Zahlen über Näherungswerte: G (Gymnasium Kl. 9; Oberschule „in Teilen“, für den MSA nötig). Situationsangemessenes Darstellen in Zehnerpotenzschreibweise, Einschachtelung, rationale Exponenten, Wurzelgesetze, Logarithmen: H (nicht hier). Quadratzahlen bis 100: C (Grundschule; hier Blatt 0). Leitidee Zahlen und Operationen; die Zehnerpotenzen für Einheitenvorsätze (Milli bis Kilo F, Nano bis Tera G) stehen unter Größen und Messen → einheiten.md, das Verfahren (Komma verschieben, Exponent zählen) liegt hier in Einheit 2. Das Lehrwerk bringt das Potenzieren mit natürlichem Exponenten in Kl. 5 III 4, die Quadratwurzeln in Kl. 8 IV 1–2 (vor dem Satz des Pythagoras Kl. 9 V) und die Potenzen mit ganzzahligen Exponenten samt Zehnerpotenzen in Kl. 9 III 1–2. Im Prüfungskatalog zwei typen.csv-Themen mit vier Typen und zwölf Originalen mit diesen CSV-Themen (12 von 780 Punkten, Jahrgänge 2015–2025 außer 2018, 2021, 2023; alle Niveau I, je ein Punkt, fast alle Basisaufgaben; häufigster Typ „Zehnerpotenzschreibweise umwandeln“ mit fünf Originalen) – davon neun mit den vier Typen und drei mit dem Typ „Zahlen in verschiedenen Darstellungen vergleichen“ (typen.csv-Thema Brüche und Dezimalzahlen, CSV-Thema Potenzen und Wurzeln – hier geführt); dazu das Wurzelziehen als Voraussetzung in Pythagoras-, Körper- und p-q-Formel-Aufgaben. Blatt-0-Geber: Quadrieren, Quadratzahlen, Wurzelziehen mit Näherungswert und die Taschenrechnertasten für pythagoras.md, quadratische-gleichungen.md, binomische-formeln.md, trigonometrie.md, koerper.md und flaechen.md; seit 09c auch die Potenz mit dem Taschenrechner (Wachstumsfaktor hoch Jahre) für zinsrechnung.md Einheit 2 und Potenz, a⁰, a⁻ⁿ, Quadratwurzel und Näherungswert für reelle-zahlen.md. Vorzeichenregel und (−2)² gegen −2² → rationale-zahlen.md Einheit 3 (hier Blatt 0); Dezimalzahlen multiplizieren, Kommaverschiebung → bruchrechnung.md und brueche-dezimalzahlen.md (hier Blatt 0); Vergleichen gemischter Darstellungen als Typ → brueche-dezimalzahlen.md Einheit 5 (Verfahren für Potenzen und Wurzeln hier); Potenzgesetze, Wurzelgesetze, irrationale Zahlen, Einschachtelung → reelle-zahlen.md; Potenzfunktionen, Wachstumsfaktor hoch t → potenz-exponentialfunktionen.md; Quadratseite aus Fläche → flaechen.md Einheit 1 (Verfahren hier Einheit 3); Einheitenvorsätze → einheiten.md.
  6  [RLP] Zahlen und Operationen F (S. 42, Zahlvorstellungen): „Darstellen von Potenzen, insbesondere Zehnerpotenzen mit natürlichem Exponenten“, „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichem Exponenten)“, „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen Exponenten)“, „Runden von rationalen Zahlen (auch in Potenzschreibweise)“; F (S. 43, Operationsvorstellungen): „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte Multiplikation“, „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“. G (S. 42): „Nennen von Pi und einiger Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale Zahlen“, „Angeben von Näherungswerten für reelle Zahlen“, „Vergleichen und Ordnen von reellen Zahlen über Näherungswerte“, „sachgerechtes Runden von reellen Zahlen“; G (S. 43): „Wechseln der Darstellungsform für Ausdrücke der Form a⁻ⁿ = 1/aⁿ“, „Erklären des Zusammenhangs zwischen Potenzieren und Radizieren“, „Nutzen des Zusammenhangs a⁻ⁿ = 1/aⁿ, um Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“, „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen Exponenten“, „Ausführen von Rechnungen und Überschlagsrechnungen im Kopf … (auch im Bereich der reellen Zahlen)“. H (S. 42–43): „situationsangemessenes Darstellen von Zahlen als Brüche, Dezimalzahlen, Prozentzahlen und in Zehnerpotenzschreibweise“, „Beschreiben und Reflektieren eines Verfahrens zur Einschachtelung von Quadratwurzeln oder Pi“, „Wechseln der Darstellungsform für Ausdrücke der Form ᵈ√aᶜ = a^(c/d)“, „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“, „Begründen der Wurzelgesetze“, „Umformen von Potenzen in Logarithmen und umgekehrt“, „Nutzen des Taschenrechners zur Bestimmung von Logarithmen“. C (S. 38, Zahlbeziehungen): „Nennen und Erkennen von Quadratzahlen (bis 100)“. Größen und Messen F (S. 48): „situationsangemessenes Verwenden von Größen und ihren Einheiten (auch unter Nutzung der Zehnerpotenzen zur Beschreibung von Einheitenvorsätzen von Milli bis Kilo)“, „Umwandeln und Ordnen von Einheiten … (auch unter Nutzung der Zehnerpotenzen)“; G: „Erweiterung der Nutzung der Zehnerpotenzen zur Beschreibung von Einheitenvorsätzen von Nano bis Tera im Anwendungsbezug“ (→ einheiten.md). D/E (S. 40–41) nennen weder Potenz noch Wurzel. Befund: Potenz, Zehnerpotenz und Quadratwurzel stehen auf F – kein D/E-Mindeststoff (achter Eintrag mit „Mindeststoff (D/E): keiner“); der RLP F kennt nur natürliche Exponenten, die P10 prüft negative Exponenten (2⁻⁵, 10⁻⁴) und die Zehnerpotenzschreibweise als Basisaufgaben – Stoff der Stufen G und H in Aufgaben mit einem Punkt; der RLP nennt weder „Basis“ noch „Exponent“ noch die Schreibweise a · 10ⁿ.
  7  [LS-AA] Klasse 5, Kapitel III „Rechnen“, Lerneinheit 4 „Potenzieren“ (natürlicher Exponent, Quadrat- und Kubikzahlen). Klasse 8, Kapitel IV „Reelle Zahlen“: 1 Quadratwurzeln · 2 Quadratwurzeln näherungsweise berechnen · 3 Irrationale Zahlen (IV 4 Wurzelgesetze, IV 5 Wurzelgleichungen → reelle-zahlen.md). Klasse 9, Kapitel III „Potenzen“: 1 Potenzen mit ganzzahligen Exponenten · 2 Zehnerpotenzen (III 3–5 Potenzgesetze, III 6 rationale Exponenten → reelle-zahlen.md; III 7 Potenzfunktionen → potenz-exponentialfunktionen.md). Vorläufer: Kl. 5 I 3 (große Zahlen und Runden), Kl. 6 V 4 (Kommaverschiebung), Kl. 7 I 5 (rationale Zahlen multiplizieren). Nachfolger: Kl. 9 V (Pythagoras), Kl. 9 I–II (quadratische Funktionen und Gleichungen), Kl. 10 II (Exponentialfunktionen), Kl. 10 III (Trigonometrie). Stundenumfang steht nicht im Fahrplan. Einheit 1 hier = Kl. 5 III 4 und Kl. 9 III 1, Einheit 2 = Kl. 9 III 2, Einheit 3 = Kl. 8 IV 1–2 (IV 3 nur als Begriff „irrational“).
  8  [LISUM-PH] Planungshilfen für einen kompetenzorientierten Mathematikunterricht, Jahrgangsstufen 7 bis 10 (LISUM 2023, CC BY-SA 4.0): „Jahrgangsstufe 8, Mathematik: Potenzen und Wurzeln“, Zeitumfang ca. 20 Stunden, Differenzierung EBR/FOR/GYM über Tiefgründigkeit, Details und Aufgabenmenge, dazu drei „nur GYM“-Marken; RLP-Zeilen ① bis ⑨ Niveaustufe F, Leitidee Zahlen und Operationen, Zeilen ⑩ bis ⑫ Niveaustufe F, Leitidee Größen und Messen (mit dem Vermerk der Reihe, die Einheitenvorsätze gehörten eigentlich erst zur Niveaustufe G). Block „Darstellen und Vergleichen von Potenzen“ ① bis ⑥: Potenz als wiederholtes Multiplizieren; der Exponent als Häufigkeit der Multiplikation der Basis; Potenz aus Basis und Exponent, zunächst mit natürlichem Exponenten; Einordnen in den Bereich der rationalen Zahlen; Quadrieren als Potenzieren mit dem Exponenten zwei, auch am Quadrat als Figur mit Verweis auf die Geometrie-Reihe; Darstellen rationaler Zahlen als Potenz, auch ikonisch für die Exponenten zwei und drei; Darstellen als Zehnerpotenz einschließlich wissenschaftlicher Schreibweise, nur GYM auch mit negativen ganzzahligen Exponenten; Nutzen der Zehnerpotenz zum sinnvollen Runden; Nutzen der Taschenrechnertaste EXP beziehungsweise EE; Vergleichen und Ordnen von Potenzen als Ungleichungskette und an der Zahlengeraden mit sinnvoller Skalierung. Block „Schätzen und Überprüfen von Größen und Ergebnissen“ ⑨: Abschätzen zwei- und dreidimensionaler Größen im Sachkontext – erst schätzen, dann rechnen, dann das Ergebnis mit der Intuition vergleichen. Block „Verwenden und Umwandeln von Einheiten“ ⑩ bis ⑫, mit Verweis auf die Geometrie-Reihe: Erkennen der Einheitenvorsätze von Milli bis Kilo als Zehnerpotenzen und Umwandeln ineinander, nur GYM auch Mikro und Nano oder Mega, Giga und Tera; Übertragen der Längenumrechnung auf Flächen und Volumina; Addieren, Subtrahieren, Multiplizieren und Dividieren von Zahlentermen mit Potenzen, nur für natürliche Exponenten, auch im Ergebnis. Block „Beschreiben des Radizierens als Umkehroperation des Potenzierens“ ⑦, ebenfalls mit Verweis auf die Geometrie-Reihe: Flächeninhalt eines Quadrats aus der Kantenlänge in Potenzschreibweise und umgekehrt die Kantenlänge aus dem Flächeninhalt in Wurzelschreibweise; dasselbe für Würfelvolumen und Kantenlänge; nur GYM ggf. die n-te Wurzel als Umkehrung der n-ten Potenz. Block „Verwenden von Potenzen und Wurzeln in der Zinsrechnung“ ⑧, ⑨: Zinsen über mehrere Jahre, auch mit Tabellenkalkulation und grafisch; Schätzen und Nachrechnen, nach wie vielen Jahren sich ein verzinstes Kapital verdoppelt hat, mit der 72er-Regel und mit systematisch variiertem Zinssatz in der Tabellenkalkulation. Begriffe: Potenz (zweite, dritte Potenz), Basis, Exponent, Wurzel (zweite, dritte Wurzel), ggf. Radikand, potenzieren, radizieren beziehungsweise Wurzel ziehen, Quadratzahl, Kubikzahl. Material: LISUM „Material zur Diagnose und Förderung“, Zahlen und Operationen, Förderaufgaben „Idee der Zahl“ (Sek I), Nutzen des dezimalen Stellenwertsystems Karten 3–10 (S. 641) und Erkennen von Zahlbeziehungen Karten 17–30 (S. 654), Förderaufgaben „Idee der Operation“, Potenzieren Karten 1–5 (S. 680), Radizieren Karten 1–6 (S. 684) und Anwenden von Rechenregeln Karten 4 und 6 (S. 708); Handreichungen zur Mathe-Werkstatt 9 „Soforthilfe Potenzen“ und „Soforthilfe Wurzeln“ – keine eingesehen. Die Fortsetzung in Jahrgangsstufe 9 liegt in der Reihe „Terme und Gleichungen mit Potenzen bzw. Wurzeln“ und ist in reelle-zahlen.md belegt; dort stehen die negativen Exponenten und die Potenzgesetze für die Niveaustufe G. Befund, am 11b abgearbeitet: Die negativen Zehnerpotenz-Exponenten sind in Jahrgangsstufe 8 ausdrücklich „nur GYM“ („Darstellen von Zahlen als Zehnerpotenz, auch wissenschaftliche Schreibweise … nur GYM: auch Zehnerpotenzen mit negativen ganzzahligen Exponenten“) und werden erst in der Jahrgangsstufe-9-Reihe für alle Bildungsgänge geführt (dort ohne Marke: „Darstellen von Dezimalzahlen unter Nutzung von Zehnerpotenzen mit negativem Exponenten“, „Nutzen von Zehnerpotenzen mit negativem Exponenten als Einheitenvorsätze“). Nach der GYM-Regel greift hier die Prüfungsvorbereitung: die P10 prüft die negative Zehnerpotenz jahrgangsübergreifend als Basisaufgabe, die Niveaumarke wird überschrieben – in Einheit 1 und 2 vermerkt. Zweiter Befund, am 11b berichtigt: Die Reihe nennt zur Verdopplungsdauer die 72er-Regel, nicht eine Siebzigerregel; dieselbe 72er-Regel steht in der Zinsrechnungs-Reihe derselben Jahrgangsstufe. Eine Siebzigerregel kommt in der Gesamtdatei nicht vor (Suche über `_suche_quelle.py` nach „70er“, „siebzig“, „Siebziger“, „Siebzigerregel“, „Zweiundsiebzigerregel“ – je null Treffer; Probe „Verdopplung“ drei Treffer, „72er“ zwei Treffer in den Zeilen beider Reihen). Der Katalog führt die 72er-Regel als Vorrat in zinsrechnung.md; hier bleibt sie außen vor, weil dieser Eintrag keine Zinsaufgabe trägt. Dritter Befund: Die Reihe verankert Wurzel und Potenz durchgehend an Quadrat und Würfel und verweist dafür dreimal auf die Geometrie-Reihe – das stützt die Blatt-0-Beziehung dieses Eintrags zu flaechen.md und koerper.md.
  9
 10  ### Lerneinheiten
 11  1. Potenzen – Potenz als Produkt aus gleichen Faktoren schreiben und ausrechnen, Basis und Exponent benennen, Potenz von Produkt unterscheiden (4³ gegen 4 · 3), Quadrat- und Kubikzahlen, Quadratzahlen bis 20² aus dem Kopf, Taschenrechnertasten x² und ^, Potenzen mit negativer Basis (Klammer; gerade oder ungerade Hochzahl), Potenzen von Dezimalzahlen und Brüchen, Potenzen vergleichen und ordnen (ausrechnen statt Basis oder Exponent vergleichen), Exponent aus a^x = b durch Probieren oder Zerlegen; Potenzen mit negativem Exponenten als Bruch und Dezimalzahl, hoch null. (Kl. 9; RLP F, negative Exponenten G; LISUM-PH führt sie in der Jg.-8-Reihe nur GYM, in der Jg.-9-Reihe für alle – GYM-Marke von der P10 überschrieben, siehe Prüfungsform) ← Eingabe „potenzen“, „hochzahl“, „exponent bestimmen“, „potenzen vergleichen“, „negative exponenten“
 12    Marken: OS Kl. 5–9 (Sekundo 9, Mathematik 2023 5, Schnittpunkt 5, Mathematik heute 5) · GYM Kl. 5 · P10 oft · nicht für alle: Sekundo 7 Zusatzstoff
 13  2. Zehnerpotenzen – 10ⁿ als Eins mit n Nullen, Zahlwörter Tausend bis Billion, große Zahl mit 10, 100, 1000 vervielfachen (Nullen anhängen), Zahl in der Form a · 10ⁿ schreiben und wieder ausschreiben (Komma verschieben, Exponent zählen), fehlenden Exponenten eintragen, Zehnerpotenzen mit negativem Exponenten für kleine Zahlen, Zahlen in Zehnerpotenzschreibweise vergleichen und ordnen (auch negative), Taschenrechner-Anzeige mit E lesen, gerundete Werte in Zehnerpotenzschreibweise, Sachaufgaben aus Astronomie und Mikrowelt; Multiplizieren und Dividieren von Zehnerpotenzen als Vorrat. (Kl. 9; RLP F, negative Exponenten G, situationsangemessen H; LISUM-PH Jg.-8-Reihe „nur GYM“ für negative Exponenten, Jg.-9-Reihe für alle – GYM-Marke von der P10 überschrieben, siehe Prüfungsform) ← Eingabe „zehnerpotenzen“, „zehnerpotenzschreibweise“, „große zahlen“, „wissenschaftliche schreibweise“, „kleine zahlen“
 14    Marken: OS Kl. 9–10 (Sekundo 9, Mathematik 2023 10, Schnittpunkt 9) · GYM Kl. 8–9 (LS 9, Fundamente 8, mathe.delta 9) · P10
 15  3. Quadratwurzeln – Wurzel als Umkehrung des Quadrierens, Quadratzahlen erkennen und Wurzeln im Kopf, Wurzel mit dem Taschenrechner und Näherungswert runden, Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen, Wurzel in Vergleiche einordnen, Wurzel eines Quadrats und Quadrat einer Wurzel (erst das Quadrat, Wurzel nie negativ), keine Wurzel aus einer negativen Zahl, Wurzeln aus Dezimalzahlen und Brüchen, Quadratseite aus dem Flächeninhalt, Wurzel als letzter Rechenschritt in Formeln (Pythagoras, Zylinderradius, p-q-Formel); Kubikwurzel als Vorrat. (Kl. 8; RLP F, Näherungswerte G) ← Eingabe „wurzel“, „quadratwurzel“, „wurzel ziehen“, „quadratzahlen“, „wurzel abschätzen“
 16    Marken: OS Kl. 7–9 (Sekundo 9, Mathematik 2023 7, Schnittpunkt 9, Mathematik heute 8) · GYM Kl. 8 · P10 · nicht für alle: Sekundo 7 Zusatzstoff
 17
 18  ### Typen je Lerneinheit
 19  Einheit 1: Potenz als Malkette schreiben (3⁴ = 3 · 3 · 3 · 3) und Malkette als Potenz (2 · 2 · 2 · 2 · 2 = 2⁵) · Basis und Exponent in einer Potenz benennen (Beschriftung) · Potenz von Produkt unterscheiden und beide ausrechnen (4³ = 64, 4 · 3 = 12) · Quadratzahlen bis 20² aus dem Kopf, Kubikzahlen bis 10³ [OS 7–8] · Potenzwert mit dem Taschenrechner (Tasten x² und ^, Klammern bei negativer Basis) · Potenz mit negativer Basis: Vorzeichen aus gerader oder ungerader Hochzahl ((−3)⁴ = 81, (−3)³ = −27), Klammer gegen kein Klammer (−3⁴ = −81) [GYM 7] · Potenz einer Dezimalzahl (0,4² = 0,16, 1,5³ = 3,375) und eines Bruchs ((2/3)² = 4/9) · zwei Potenzen vergleichen, indem beide ausgerechnet werden (2⁸ gegen 3⁵) · Potenzen ordnen, größte oder kleinste unterstreichen (P10-Form) · Potenz gegen Dezimalzahl und Prozent vergleichen (Vergleichszeichen eintragen) · Exponent bestimmen durch wiederholtes Malnehmen (2^x = 16: 2, 4, 8, 16 → x = 4; P10-Form) · Exponent bestimmen durch Zerlegen (256 = 4 · 4 · 4 · 4) · Exponent mit Basis 10 (10^x = 100 000; Brücke zu Einheit 2) · Potenz mit negativem Exponenten als Bruch und als Dezimalzahl (2⁻³ = 1/8 = 0,125), hoch null [OS 10, GYM 9] · negative Potenz gegen Dezimalzahl vergleichen (P10-Form) · Fehler finden (Basis mal Exponent; Vorzeichen bei negativer Basis; negative Hochzahl als negative Zahl; „größere Basis, größere Zahl“) · Begründen (warum 2¹⁰ größer ist als 10²; warum 5⁰ = 1 ist – die Kette der Potenzen 5³, 5², 5¹ wird jedes Mal durch fünf geteilt).
 20  Einheit 2: Zehnerpotenz ausschreiben (10⁶ = 1 000 000) und Zahl als Zehnerpotenz schreiben (100 000 = 10⁵; P10-Form) · Zahlwörter zuordnen (Tausend, Million, Milliarde, Billion) · große Zahl mit 10, 100, 1000 vervielfachen: Nullen anhängen, Ergebnis ausgeschrieben (P10-Form) · Zahl in Zehnerpotenzschreibweise a · 10ⁿ mit a zwischen 1 und 10 schreiben (Komma setzen, Stellen zählen) [OS 9, GYM 8] · fehlenden Exponenten in „a · 10^□“ eintragen (P10-Form) · Zehnerpotenzschreibweise ausschreiben: Komma nach rechts, Nullen auffüllen (P10-Form) · passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form) · kleine Zahl mit negativem Exponenten: Komma nach links, Nullen vorn (2,1 · 10⁻⁴ = 0,00021; P10-Form) · Zahl kleiner als eins in Zehnerpotenzschreibweise schreiben (0,00035 = 3,5 · 10⁻⁴) [OS 9] · Zahlen in Zehnerpotenzschreibweise vergleichen und ordnen (erst Exponent, dann Faktor) · negative Zehnerpotenzen auf der Zahlengerade ordnen (−10³ gegen −0,01; P10-Form) · Taschenrechner-Anzeige „8.5E5“ lesen und Zahl mit der EXP- oder ×10ˣ-Taste eingeben · gerundeter Wert in Zehnerpotenzschreibweise (9 460 730 472 581 km ≈ 9,46 · 10¹² km) · Sachaufgabe aus Astronomie oder Mikrowelt (Lichtjahr, Atommasse; Einheit mitführen) · Zehnerpotenzen multiplizieren und dividieren (Exponenten addieren, subtrahieren; Vorrat, Nebenleistung 2015-OS-K3c) · Fehler finden (Nullen statt Kommastellen gezählt; Nullen an alle Ziffern gehängt; Vorzeichen des Exponenten übersehen; Exponent als Zahl der Nullen bei einer Dezimalzahl) · Begründen (warum 3,5 · 10⁴ und 35 · 10³ dieselbe Zahl sind; warum ein Exponent von minus vier eine Zahl kleiner als eins ergibt).
 21  Einheit 3: Quadratzahl erkennen und Wurzel im Kopf (√169 = 13; Quadratzahlen bis 20²) · Wurzel als Umkehrung: „welche Zahl mal sich selbst gibt …“ · Wurzel mit dem Taschenrechner, Anzeige ablesen, auf zwei Dezimalen runden (√7 ≈ 2,65) · Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen (√50 liegt zwischen 7 und 8) · Wurzel mit Dezimalzahl und Bruch vergleichen (√2 gegen 1,4; P10-Form) · Zahlen mit Wurzel aufsteigend ordnen (P10-Form) · Wurzel eines Quadrats: erst das Quadrat, dann die Wurzel (√((−4)²) = √16 = 4; die richtige von drei Aussagen ankreuzen; P10-Form) · Quadrat einer Wurzel ((√5)² = 5) · Wurzel aus einer negativen Zahl: kein Wert (√(−9) gegen −√9) · Wurzel aus Dezimalzahl und Bruch (√0,25 = 0,5, √(1/4) = 1/2; nicht „halbieren“) · Quadratseite aus dem Flächeninhalt (a = √A; Typ in flaechen.md Einheit 1) [OS 9] · Wurzel als letzter Schritt einer Formel: erst den Term unter der Wurzel ausrechnen, dann die Wurzel (Hypotenuse, Zylinderradius r = √(V : (π · h)), p-q-Formel) · Kubikwurzel (³√27 = 3; Vorrat) [OS 7–9] · Fehler finden (Wurzel halbiert statt gezogen; Wurzel termweise aus einer Summe; „nicht definiert“ bei √((−4)²); −4 als Wurzelwert; √2 als zwei gelesen) · Begründen (warum √16 nicht −4 ist, obwohl (−4)² = 16 gilt; warum √50 näher an sieben als an acht liegt).
 22
 23  ### Voraussetzungen (Blatt 0)
 24  Fertigkeiten:
 25  - Kleines Einmaleins und Malnehmen mehrstelliger Zahlen im Kopf oder halbschriftlich, Malketten mit gleichen Faktoren – Einheit 1. Kein eigenes Thema (Grundschule; LS-AA Kl. 5 I 4). [RLP C/D; P10 2020-OS-B1h Verfahren als Malkette]
 26  - Quadratzahlen bis 100 aus dem Kopf, Kubikzahlen zwei hoch drei, drei hoch drei, zehn hoch drei – Einheit 1 und 3. Kein eigenes Thema (Grundschule). [RLP C „Nennen und Erkennen von Quadratzahlen (bis 100)“]
 27  - Vorzeichenregel beim Malnehmen (minus mal minus gibt plus), Anzahl der Minuszeichen zählen, Quadrat einer negativen Zahl mit und ohne Klammer – Einheit 1 und 3. Thema Rationale Zahlen (rationale-zahlen.md), Einheit 3. [RLP E; P10 2014-OS-K7a Voraussetzung „Potenz mit negativer Basis“, 2015-OS-B1j „negative Basis“]
 28  - Dezimalzahlen multiplizieren (Kommastellen zählen), Brüche multiplizieren – Einheit 1 und 3. Thema Bruchrechnung (bruchrechnung.md). [RLP D; P10 2023-OS-B1f Fehlerquelle Quadrat einer Dezimalzahl als Verdopplung]
 29  - Große Zahlen lesen und schreiben (Dreiergruppen, Zahlwörter bis Billion), Stellenwerttafel, mal zehn, hundert und tausend durch Nullen anhängen – Einheit 2. Kein eigenes Thema (Grundschule; LS-AA Kl. 5 I 3); Struktur: MSK D4A (Multiplizieren und Dividieren mit Zehnerzahlen). [RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“]
 30  - Kommaverschiebung: Dezimalzahl mal zehn, hundert, tausend – Komma nach rechts; geteilt – Komma nach links; Nullen auffüllen – Einheit 2. Thema Brüche und Dezimalzahlen (brueche-dezimalzahlen.md), Einheit 4; Bruchrechnung (bruchrechnung.md, LS-AA Kl. 6 V 4). [RLP D; P10 2016-OS-B1h, 2019-OS-B1j Verfahren „Komma verschieben“]
 31  - Dezimalzahlen und Brüche vergleichen und ordnen, Bruch in Dezimalzahl umwandeln, Prozent in Dezimalzahl, negative Zahlen auf der Zahlengerade ordnen – Einheit 1 bis 3 (Vergleichs-Originale). Thema Brüche und Dezimalzahlen (brueche-dezimalzahlen.md), Einheit 4 und 5; Rationale Zahlen (rationale-zahlen.md), Einheit 1. [RLP D/E; P10 2017-OS-B1e, 2022-OS-B1j, 2015-OS-B1c, 2014-OS-B1h]
 32  - Runden von Dezimalzahlen auf eine und zwei Stellen, Näherungswert mit ≈ schreiben – Einheit 2 und 3. Thema Brüche und Dezimalzahlen (brueche-dezimalzahlen.md), Einheit 5. [RLP D/E „sinnvolle Genauigkeit“; RLP G „sachgerechtes Runden von reellen Zahlen“]
 33  - Taschenrechner: Tasten x², ^ (oder xʸ), √ mit Klammer für den Term darunter, EXP oder ×10ˣ für Zehnerpotenzen, Anzeige mit E lesen, Ergebnis erst am Ende runden – alle Einheiten. Kein eigenes Thema. [P10 Hilfsmittel immer ja; 2025-OS-K4a, 2024-OS-K6a „Wurzel ziehen“, 2014-OS-K3c „Potenz mit Taschenrechner“; trigonometrie.md Blatt 0 Taschenrechnerzeile]
 34  Erkennungsschritte (Vorstufe der Einheit, vor der sie stehen, nicht auf Blatt 0; eine Hauptnummer je Schritt):
 35  - „Hoch oder mal?“ – zu Termpaaren wie vier hoch drei und vier mal drei ankreuzen, welcher Term eine Potenz ist, und die Potenz als Malkette daneben schreiben; nichts ausrechnen. Vor Einheit 1. [P10 Fehlerquellen 2020-OS-B1h, 2024-OS-B1g „geteilt statt hoch“; FD Potenz als Produkt von Basis und Exponent]
 36  - „Wer ist Basis, wer ist Exponent?“ – in Potenzen mit Pfeilen beschriften: Basis unten (wird malgenommen), Exponent oben (zählt die Faktoren); nichts rechnen. Vor Einheit 1. [LS-AA Kl. 5 III 4; Serlo 1663 „Basis, Exponent, Wert der Potenz“]
 37  - „Plus oder minus?“ – zu Potenzen mit negativer Basis und mit Minus vor der Potenz ankreuzen, ob das Ergebnis positiv oder negativ wird (Klammer? gerade oder ungerade Hochzahl?); nichts rechnen. Vor Einheit 1 und 3. [Serlo 1663 „gerader Exponent positiv, ungerader negativ“; P10 2014-OS-K7a Fehlerquelle Vorzeichen beim Einsetzen]
 38  - „Bruch oder minus?“ – zu Potenzen mit negativem Exponenten ankreuzen: Bruch (eins geteilt durch die Potenz) oder negative Zahl; nichts ausrechnen. Vor Einheit 1 (negative Exponenten). [P10 2022-OS-B1j Fehlerquelle negative Potenz als negative Zahl; RLP G a⁻ⁿ als Kehrwert]
 39  - „Groß oder klein?“ – zu Zahlen in Zehnerpotenzschreibweise ankreuzen, ob die Zahl größer als eins (Hochzahl positiv, Komma wandert nach rechts) oder kleiner als eins ist (Hochzahl negativ, Komma nach links); nichts ausschreiben. Vor Einheit 2. [P10 2019-OS-B1j Fehlerquelle „Vorzeichen des Exponenten ignoriert“]
 40  - „Stellen oder Nullen?“ – zu Zahlen wie achthundertfünfzigtausend die Hochzahl einkreisen, die das Komma wandern muss, und daneben die Zahl der Nullen schreiben; feststellen, dass beides verschieden ist. Vor Einheit 2. [P10 2025-OS-B1d Fehlerquelle Nullen statt Kommastellen gezählt, 2016-OS-B1h Nullen an alle Ziffern gehängt]
 41  - „Quadratzahl oder nicht?“ – zu Zahlen ankreuzen, ob die Wurzel im Kopf aufgeht (Quadratzahl) oder der Taschenrechner einen Näherungswert liefert; nichts rechnen. Vor Einheit 3. [LS-AA Kl. 8 IV 1–2; P10 2025-OS-K5c Ergebnis mit Wurzel und Näherungswert]
 42  - „Zwischen welchen Quadratzahlen?“ – zu einer Wurzel die beiden Nachbar-Quadratzahlen und ihre Wurzeln eintragen („die Wurzel liegt zwischen sieben und acht“); nichts mit dem Taschenrechner rechnen. Vor Einheit 3. [P10 2015-OS-B1c, 2014-OS-B1h Voraussetzung „Wurzel abschätzen“; RLP G Näherungswerte]
 43  - „Was zuerst?“ – bei Termen mit Wurzel und Quadrat markieren, was zuerst gerechnet wird (innen vor außen: erst das Quadrat, dann die Wurzel; erst die Summe unter der Wurzel, dann die Wurzel); nichts ausrechnen. Vor Einheit 3. [P10 2015-OS-B1j Verfahren erst das Quadrat, dann die Wurzel; pythagoras.md Blatt 0 „erst die Summe unter der Wurzel“]
 44
 45  ### Merkkasten
 46  Einheit 1 (Potenzen):
 47      Potenz: Eine Potenz ist die Kurzschreibweise für ein Produkt aus lauter gleichen Faktoren – die Basis steht unten, der Exponent (die Hochzahl) sagt, wie oft sie als Faktor vorkommt: 3⁴ = 3 · 3 · 3 · 3 = 81 (nicht 3 · 4 = 12).
 48      Exponent finden: Nimm die Basis so oft mit sich selbst mal, bis der Wert erreicht ist, und zähle die Faktoren: 5^x = 125 → 5, 25, 125 → x = 3.
 49      Negative Basis: Gerade Hochzahl gibt plus, ungerade gibt minus; ohne Klammer gehört das Minus nicht zur Basis: (−2)⁴ = 16, (−2)³ = −8, aber −2⁴ = −16.
 50      Negative Hochzahl: Das Minus im Exponenten heißt „eins geteilt durch“ – die Potenz wird ein Bruch, keine negative Zahl: 2⁻³ = 1/2³ = 1/8 = 0,125; jede Basis hoch null ist eins.
 51      Formelsammlung: Zahlen und Rechnen – Potenzen, Potenzen mit negativen Exponenten [FS]
 52  Quelle: [Serlo 1663] „Potenzieren als verkürzte Schreibweise für mehrmaliges Multiplizieren einer Zahl mit sich selbst; Basis, Exponent, Wert der Potenz; gerader Exponent positiv, ungerader negativ; wird der Exponent um eins kleiner, wird das Ergebnis durch die Basis geteilt“, sinngemäß; [RLP F] „fortgesetzte Multiplikation“, [RLP G] a⁻ⁿ = 1/aⁿ; [P10 2020-OS-B1h, 2024-OS-B1g] Verfahren „Vierer-Potenzen: 4, 16, 64, 256“, [2022-OS-B1j] „2⁻⁵ = 1 : 2⁵“; [LS-AA Kl. 5 III 4, Kl. 9 III 1].
 53
 54  Einheit 2 (Zehnerpotenzen):
 55      Zehnerpotenz: 10ⁿ ist eine Eins mit n Nullen – die Hochzahl zählt die Nullen: 10⁶ = 1 000 000 (eine Million).
 56      Mal Zehnerpotenz: Beim Malnehmen mit 10ⁿ hängst du an eine ganze Zahl n Nullen an; bei einer Dezimalzahl wandert das Komma n Stellen nach rechts: 47 · 10⁴ = 470 000; 3,25 · 10⁴ = 32 500.
 57      Zehnerpotenzschreibweise: Eine Zahl zwischen eins und zehn mal eine Zehnerpotenz – die Hochzahl zählt, um wie viele Stellen das Komma wandert, nicht die Nullen: 6 700 000 = 6,7 · 10⁶ (das Komma wandert sechs Stellen, Nullen sind es fünf).
 58      Negative Hochzahl: 10⁻ⁿ macht die Zahl klein – das Komma wandert n Stellen nach links, vorn kommen Nullen: 4,2 · 10⁻³ = 0,0042.
 59      Formelsammlung: Zahlen und Rechnen – Zehnerpotenzen; Größen – Vorsätze der Einheiten [FS]
 60  Quelle: kein Serlo-Artikel zu Zehnerpotenzen erreicht (Abruf 2026-09-09; Serlo 175273 nennt Zehnerpotenzen nur in Aufgaben) – eigene Formulierung nach [RLP F] „Zehnerpotenzen mit natürlichem Exponenten“, „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen)“ und [P10 2025-OS-B1d, 2016-OS-B1h, 2019-OS-B1j] Verfahren „Komma um fünf Stellen nach rechts“, „Komma um vier Stellen nach links“, [2015-OS-K3a] „mal 100: zwei Nullen anhängen“; [LS-AA Kl. 9 III 2].
 61
 62  Einheit 3 (Quadratwurzeln):
 63      Wurzel: Die Quadratwurzel ist die Umkehrung des Quadrierens – √a ist die Zahl, die mit sich selbst malgenommen a ergibt, und sie ist nie negativ: √144 = 12, weil 12 · 12 = 144.
 64      Quadrat und Wurzel heben sich auf – bei negativer Basis erst das Quadrat rechnen, die Wurzel bleibt positiv: √(9²) = 9 und √((−9)²) = √81 = 9.
 65      Keine Wurzel aus einer negativen Zahl: √(−81) hat keinen Wert, weil kein Quadrat negativ ist.
 66      Näherungswert: Geht die Wurzel nicht auf, liegt sie zwischen zwei Nachbar-Quadratzahlen; der Taschenrechner gibt den Wert, gerundet wird erst am Ende: √30 ≈ 5,48 (zwischen √25 = 5 und √36 = 6).
 67      Formelsammlung: Zahlen und Rechnen – Quadratwurzel, Wurzelgesetze [FS]
 68  Quelle: kein Serlo-Artikel zur Quadratwurzel erreicht (Abruf 2026-09-09; Themenordner 16392 „Potenzen und Wurzeln“ nur als Titel) – eigene Formulierung nach [RLP F] „Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“, [RLP G] „Näherungswerte für reelle Zahlen“ und [P10 2015-OS-B1j] Verfahren „(−4)² = 16, √16 = 4“, Distraktoren „−4“ und „nicht definiert“, [2015-OS-B1c] „√2 ≈ 1,41“, [2025-OS-K5c] Ergebnis „x = 3 ± √2“ mit Näherungswert; [LS-AA Kl. 8 IV 1–2].
 69
 70  ### Typische Fehler
 71  - Potenz als Produkt aus Basis und Exponent: 4³ = 12; beim Exponenten 16 : 2 = 8 oder 256 : 4 = 64 gerechnet. [P10 2020-OS-B1h, 2024-OS-B1g Fehlerquellen; FD Malle, Potenz als „mal“ gelesen]
 72  - Größte Potenz nach der größten Basis oder dem größten Exponenten gewählt statt ausgerechnet (2⁸ statt 8⁴). [P10 2019-OS-B1d Fehlerquelle]
 73  - Negative Hochzahl als negative Zahl: 2⁻⁵ = −32; oder mit einer anderen Potenz verwechselt (2⁻⁵ = 0,25). [P10 2022-OS-B1j Fehlerquelle]
 74  - Vorzeichen bei negativer Basis: (−3)² = −9 oder −3² = 9; beim Einsetzen negativer Werte p(−3) = +9. [P10 2014-OS-K7a, 2025-OS-B1h Fehlerquellen; rationale-zahlen.md Kasten 3]
 75  - Potenz einer Dezimalzahl als Verdopplung: 0,4² = 0,8 oder 1,6. [P10 2023-OS-B1f Fehlerquelle]
 76  - Nullen statt Kommastellen gezählt: 850 000 = 8,5 · 10⁴; oder Nullen an alle Ziffern gehängt: 8,5 · 10⁵ = 8 500 000, 9,46 · 10¹² = 946 000 000 000 000. [P10 2025-OS-B1d, 2016-OS-B1h, 2015-OS-K3b Fehlerquellen]
 77  - Nullen verzählt: 100 000 = 10⁶; beim Malnehmen mit 100 eine Null zu viel oder zu wenig. [P10 2017-OS-B1g, 2015-OS-K3a Fehlerquellen]
 78  - Vorzeichen des Exponenten übersehen: 2,1 · 10⁻⁴ = 21 000; oder eine Stelle zu wenig: 0,0021. [P10 2019-OS-B1j Fehlerquelle]
 79  - Negative Zehnerpotenz nach dem Betrag geordnet: −0,01 als kleinste Zahl statt −10³; −10² gewählt, weil der Exponent übersehen wurde. [P10 2017-OS-B1e Fehlerquelle]
 80  - Zehnerpotenzen falsch dividiert: 10¹⁵ : 10⁵ = 10³. [P10 2015-OS-K3c Fehlerquelle]
 81  - Wurzel halbiert statt gezogen (√36 = 18) oder durch vier geteilt (36 : 4 = 9 cm als Quadratseite). [P10 2020-OS-B1d Fehlerquelle; FD]
 82  - Wurzel eines Quadrats: √((−4)²) als „nicht definiert“ oder als −4 (Vorzeichen zurückgeholt). [P10 2015-OS-B1j Fehlerquelle]
 83  - Wurzel als die Zahl gelesen: √2 als 2, darum √2 > 3/2 angekreuzt; √2 vor 1,4 geordnet. [P10 2015-OS-B1c, 2014-OS-B1h Fehlerquellen]
 84  - Wurzel vergessen: r = 19,3 statt 4,4; c² als Ergebnis; z = x² − y² angekreuzt. [P10 2022-OS-K2d, 2024-OS-B1f, 2021-OS-B1h Fehlerquellen]
 85  - Wurzel termweise aus einer Summe oder Differenz: √(a² + b²) = a + b. [FD; pythagoras.md Typische Fehler]
 86  - Zu früh gerundet: √2 ≈ 1,4 weitergerechnet; Wurzelwert auf ganze Zahl gerundet; ≈ und = verwechselt. [RLP G „sachgerechtes Runden“; P10 2025-OS-K5c Näherungswert; FD]
 87  - Taschenrechner: Term unter der Wurzel ohne Klammer eingetippt (√9 + 16 statt √(9 + 16)); Anzeige 8.5E5 als 8,5 gelesen; Exponent mit der Malpunkt-Taste statt mit EXP eingegeben (8,5 · 10 · 5). [FD; trigonometrie.md Fehlerzeile Taschenrechner]
 88
 89  ### Für schwache Schüler
 90  Mindeststoff (D/E) [RLP]: keiner – Potenzen, Zehnerpotenzen und Quadratwurzel stehen auf F, negative Exponenten und Näherungswerte auf G; nur die Quadratzahlen bis 100 (C) sind Grundschulstoff und liegen hier auf Blatt 0. Mindeststoff der Prüfungsvorbereitung (P10, FOR) [P10]: Einheit 2 Zehnerpotenzschreibweise umwandeln (fünf Originale 2015, 2016, 2017, 2019, 2025 – häufigster Typ, beide Richtungen, auch mit negativem Exponenten) und große Zahl mal Zehnerpotenz (2015), kleinste Zahl mit negativen Zehnerpotenzen (2017); Einheit 1 Exponent bestimmen (2020, 2024) und Potenzen vergleichen (2019), negative Potenz gegen Dezimalzahl (2022); Einheit 3 Wurzel eines Quadrats (2015, Stern) und das Abschätzen einer Wurzel für Vergleiche (2014, 2015 – Originale in brueche-dezimalzahlen.md) sowie das Wurzelziehen mit Näherungswert als Voraussetzung in Pythagoras-, Körper- und p-q-Formel-Aufgaben (jährlich). Vorrat: Kubikzahlen und Kubikwurzel (F, kein Original), Potenzen von Brüchen, Multiplizieren und Dividieren von Zehnerpotenzen (Nebenleistung 2015-OS-K3c), Rundung in Zehnerpotenzschreibweise (F, kein Original), Einheitenvorsätze (→ einheiten.md), Potenzgesetze, irrationale Zahlen, Einschachtelung (→ reelle-zahlen.md).
 91  Grundvorstellung (Blatt 0) [RLP F, MO]: Der Exponent zählt Faktoren, nicht Summanden – „Schreibe zwei hoch fünf als Malkette und zwei mal fünf als Pluskette, rechne beide aus und vergleiche: Warum ist die Potenz so viel größer?“ Und: „Ein Quadrat aus neunundvierzig Kästchen ist gezeichnet. Wie lang ist seine Seite? Geht das auch bei einem Quadrat aus fünfzig Kästchen genau auf?“ Wer die Potenz als Malaufgabe liest (Basis mal Exponent), wer die negative Hochzahl für ein negatives Ergebnis hält oder die Wurzel halbiert, braucht das vor allen Rechnungen: Die Potenz ist eine Kette gleicher Faktoren, die Wurzel ist die Seite des Quadrats – darum hebt Quadrieren die Wurzel auf und darum kann keine Wurzel negativ sein. [P10 Fehlerquellen 2020-OS-B1h, 2024-OS-B1g „geteilt statt hoch“, 2022-OS-B1j „negative Zahl statt Bruch“, 2020-OS-B1d „durch vier geteilt“; FD Potenz als Produkt von Basis und Exponent, Wurzel als „Hälfte“]
 92  Sprossen je Verfahrenstyp (Reihenfolge = Kette des Hauptblatts) [LS-AA, FD, P10]:
 93  - Potenzen (Einheit 1): „hoch oder mal“ ankreuzen, Basis und Exponent beschriften (Vorstufe) → Potenz als Malkette schreiben und ausrechnen, Malkette als Potenz (4×) → Potenz und Produkt nebeneinander ausrechnen → Quadratzahlen bis zwanzig hoch zwei, Kubikzahlen bis zehn hoch drei → Potenzwert mit dem Taschenrechner (Tasten x² und ^) → negative Basis mit Klammer, gerade und ungerade Hochzahl → Minus vor der Potenz ohne Klammer → Potenz einer Dezimalzahl → zwei Potenzen vergleichen (beide ausrechnen) → drei Potenzen ordnen und die größte unterstreichen (P10-Form) → Exponent durch wiederholtes Malnehmen bestimmen (P10-Form) → Exponent durch Zerlegen des Werts → Exponent mit Basis zehn → negative Hochzahl als Bruch, dann als Dezimalzahl (LISUM-PH: in der Jahrgangsreihe zu den Potenzen „nur GYM“, in der Reihe des Folgejahrgangs für alle; Marke überschrieben, weil die P10 diese Form als Basisaufgabe prüft) → Potenz mit negativer Hochzahl gegen Dezimalzahl vergleichen (P10-Form) → Prüfungshöhe: Exponent einer Zweierpotenz und einer Viererpotenz angeben (P10-Form 2020-OS-B1h, 2024-OS-B1g, Niveau I); die größte von drei Potenzen unterstreichen (2019-OS-B1d, Niveau I); Vergleichszeichen zwischen einer Potenz mit negativer Hochzahl und einer Dezimalzahl (2022-OS-B1j, Niveau I).
 94  - Zehnerpotenzen (Einheit 2): „groß oder klein“ und „Stellen oder Nullen“ ankreuzen (Vorstufe) → Zehnerpotenz ausschreiben und Zahl als Zehnerpotenz schreiben (4×) → Zahlwörter zuordnen → ganze Zahl mal zehn, hundert, tausend durch Nullen anhängen → ganze Zahl mal Zehnerpotenz mit Hochzahl → Dezimalzahl mal Zehnerpotenz: Komma nach rechts, Nullen auffüllen → Zehnerpotenzschreibweise ausschreiben (P10-Form) → Zahl in Zehnerpotenzschreibweise schreiben: Komma nach der ersten Ziffer setzen, Stellen zählen → fehlende Hochzahl eintragen (P10-Form) → passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form) → negative Hochzahl: Komma nach links, Nullen vorn (P10-Form; LISUM-PH: in der Jahrgangsreihe zu den Potenzen „nur GYM“, in der Reihe des Folgejahrgangs für alle – Marke überschrieben, weil die P10 diese Form als Basisaufgabe prüft) → Zahl kleiner als eins in Zehnerpotenzschreibweise → Zahlen in Zehnerpotenzschreibweise ordnen, auch negative (P10-Form) → Taschenrechner-Anzeige mit E lesen und Zahl mit der EXP-Taste eingeben → gerundeter Wert in Zehnerpotenzschreibweise mit Einheit → Sachaufgabe aus Astronomie oder Mikrowelt → Zehnerpotenzen multiplizieren und dividieren (Vorrat) → Prüfungshöhe: Hochzahl zu einer sechsstelligen Zahl in der Form Dezimalzahl mal Zehnerpotenz eintragen (P10-Form 2025-OS-B1d, Niveau I); Zehnerpotenzschreibweise mit negativer Hochzahl als Dezimalzahl ausschreiben (2019-OS-B1j, Niveau I); Kilometer für hundert Lichtjahre ausgeschrieben angeben (2015-OS-K3a, Niveau I); kleinste von vier negativen Zahlen mit Zehnerpotenzen ankreuzen (2017-OS-B1e, Niveau I).
 95  - Quadratwurzeln (Einheit 3): „Quadratzahl oder nicht“ und „zwischen welchen Quadratzahlen“ ankreuzen (Vorstufe) → Wurzel aus einer Quadratzahl im Kopf, mit der Probe „mal sich selbst“ (4×) → Wurzel mit dem Taschenrechner, Anzeige ablesen, auf zwei Dezimalen runden → Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen, dann Taschenrechnerwert vergleichen → Wurzel gegen Dezimalzahl und Bruch vergleichen → Zahlen mit Wurzel aufsteigend ordnen → Quadrat einer Wurzel → Wurzel eines Quadrats mit negativer Basis: erst das Quadrat → Wurzel aus einer negativen Zahl: kein Wert, gegen Minus vor der Wurzel → Wurzel aus Dezimalzahl und Bruch → Quadratseite aus dem Flächeninhalt → Wurzel als letzter Schritt einer Formel: Term unter der Wurzel in Klammern, erst ausrechnen → Kubikwurzel (Vorrat) → Prüfungshöhe: die wahre von drei Aussagen über die Wurzel aus dem Quadrat einer negativen Zahl ankreuzen (P10-Form 2015-OS-B1j, Stern, Niveau I); wahre Aussage mit einer Wurzel zwischen zwei Brüchen finden und vier Zahlen mit einer Wurzel ordnen (2015-OS-B1c, 2014-OS-B1h, Niveau I; Originale in brueche-dezimalzahlen.md); Wurzelziehen als letzter Schritt bei Kathete, Zylinderradius und p-q-Formel (2024-OS-K6a, 2022-OS-K2d, 2025-OS-K5c – Typen in pythagoras.md, koerper.md, quadratische-funktionen.md).
 96
 97  ### Prüfungsform (P10)
 98  Zwei typen.csv-Themen (Zahlen und Operationen) [P10]. Thema „Potenzen und Wurzeln“ mit zwei Typen: 6 Originale mit diesem CSV-Thema, 6 von 780 Punkten, Jahrgänge 2015, 2017, 2019, 2020, 2022, 2024, alle Basisaufgaben mit einem Punkt, Niveau I, Hilfsmittel ja; ein Stern (2015-OS-B1j – der einzige Stern an einer Basisaufgabe der Reihe). „Exponent einer Potenz bestimmen“ zweimal – 2020-OS-B1h (2^x = 16, Verfahren 2 · 2 · 2 · 2, x = 4; Fehlerquelle 16 : 2 = 8), 2024-OS-B1g (4^x = 256, Verfahren Vierer-Potenzen 4, 16, 64, 256, x = 4; Fehlerquelle 256 : 4 = 64). „Wurzel eines Quadrats berechnen“ einmal – 2015-OS-B1j (Stern: die wahre von drei Aussagen √((−4)²) = −4, = +4, „nicht definiert“; Verfahren (−4)² = 16, √16 = 4). Die übrigen drei Originale dieses CSV-Themas tragen den Typ „Zahlen in verschiedenen Darstellungen vergleichen“ (typen.csv-Thema Brüche und Dezimalzahlen → brueche-dezimalzahlen.md Einheit 5; CSV-Thema Potenzen und Wurzeln, hier geführt wie 2025-OS-B1h in quadratische-gleichungen.md): 2019-OS-B1d (die größte von 4³, 8⁴, 2⁸ unterstreichen: 64, 4096, 256 → 8⁴; Fehlerquelle größte Basis oder größter Exponent gewählt), 2022-OS-B1j (Vergleichszeichen zwischen 2⁻⁵ und 0,25: 2⁻⁵ = 1/32 = 0,03125 < 0,25; Voraussetzung 2⁻⁵ = 1 : 2⁵; Fehlerquelle 2⁻⁵ = −32 oder = 0,25), 2017-OS-B1e (die kleinste von −0,01, −10³, −10², −0,1 ankreuzen: −10³ = −1000; Fehlerquelle −0,01 nach dem Betrag oder −10² mit übersehenem Exponenten – Verfahren Einheit 2, Ordnen negativer Zahlen rationale-zahlen.md Einheit 1). Thema „Zehnerpotenzen und Näherungswerte“ mit zwei Typen: 6 Originale, 6 von 780 Punkten, Jahrgänge 2015 (zweimal), 2016, 2017, 2019, 2025, alle ein Punkt, Niveau I, kein Stern, Hilfsmittel ja. „Zehnerpotenzschreibweise umwandeln“ fünfmal, der häufigste Typ, in beiden Richtungen – 2017-OS-B1g (100 000 als Zehnerpotenz: 10⁵, auch 1 · 10⁵ richtig; Fehlerquelle 10⁶), 2016-OS-B1h (8,5 · 10⁵ ausschreiben: Komma um fünf Stellen nach rechts, 850 000; Fehlerquelle 8 500 000 oder 85 000), 2015-OS-K3b (Kontext Astronomie, Stamm „Sterne“: zu 9,46 · 10¹² die passende von drei ausgeschriebenen Zahlen ankreuzen, 9 460 000 000 000; Fehlerquelle zwölf Nullen an 946 gehängt), 2019-OS-B1j (2,1 · 10⁻⁴ als Dezimalzahl: Komma um vier Stellen nach links, 0,00021; Fehlerquelle 0,0021 oder 21 000; Bemerkung: Gegenrichtung zur Typ-Definition – die Definition in typen.csv enthält das Ausschreiben inzwischen), 2025-OS-B1d (850 000 = 8,5 · 10^□, Exponent eintragen: 5; Fehlerquelle Nullen zählen, 4). „Große Zahl mit Zehnerpotenz multiplizieren“ einmal – 2015-OS-K3a (Kontext Astronomie: 1 Lichtjahr = 9 460 000 000 000 km, Kilometer für 100 Lichtjahre: zwei Nullen anhängen, 946 000 000 000 000 km = 9,46 · 10¹⁴ km; Fehlerquelle Nullen falsch zählen). Potenzen und Wurzeln als Voraussetzung anderer Themen: Wurzel ziehen in allen Kathete- und Hypotenuse-Originalen (pythagoras.md, jährlich seit 2016), im Zylinderradius r = √(V : (π · h)) (2022-OS-K2d, koerper.md) und in der p-q-Formel (2025-OS-K5c, 2017-OS-K5d, quadratische-funktionen.md); Wurzel abschätzen in 2015-OS-B1c (√2 > 3/2?) und 2014-OS-B1h (√2 gegen 1,4; beide brueche-dezimalzahlen.md); Quadrat einer Dezimalzahl in 2023-OS-B1f (0,4² = 0,16, brueche-dezimalzahlen.md); Quadratseite als Wurzel in 2020-OS-B1d (√36 = 6 cm, flaechen.md); Potenz mit negativer Basis in 2014-OS-K7a (p(−3) = −9, quadratische-funktionen.md); Potenz mit dem Taschenrechner in den Zinseszins- und Wachstums-Originalen (2014-OS-K3c 1,03⁵; 2020-OS-K4c 1,03¹⁴; 2026-FOR-K7c 1,019¹⁴ → zinsrechnung.md, potenz-exponentialfunktionen.md); Zehnerpotenzen dividieren in 2015-OS-K3c (4,03 · 10¹⁵ : (3 · 10⁵); zuordnungen.md).
 99  Muster: fast nur Basisaufgaben mit einem Punkt ohne Kontext, Kurzantwort oder Ankreuzen; Zehnerpotenzschreibweise in beiden Richtungen mit Fehlerquelle „Nullen statt Stellen“; Exponent einer Zweier- oder Viererpotenz durch Probieren; Vergleiche, in denen die Potenz erst ausgerechnet werden muss; negative Exponenten (2⁻⁵, 10⁻⁴) und die Wurzel eines negativen Quadrats als Fallen; Kontext nur 2015 (Stamm „Sterne“ mit Lichtjahr). Niveau nie über I; die Wurzel als Rechenschritt steckt in Kontextaufgaben anderer Themen mit Niveau II.
100  Zuordnung: Einheit 1 – Exponent einer Potenz bestimmen (2020-OS-B1h, 2024-OS-B1g), dazu Zahlen in verschiedenen Darstellungen vergleichen mit Potenzen (2019-OS-B1d, 2022-OS-B1j; Typ in brueche-dezimalzahlen.md Einheit 5); Einheit 2 – Zehnerpotenzschreibweise umwandeln (2017-OS-B1g, 2016-OS-B1h, 2015-OS-K3b, 2019-OS-B1j, 2025-OS-B1d), Große Zahl mit Zehnerpotenz multiplizieren (2015-OS-K3a), dazu Zahlen in verschiedenen Darstellungen vergleichen mit negativen Zehnerpotenzen (2017-OS-B1e); Einheit 3 – Wurzel eines Quadrats berechnen (2015-OS-B1j), dazu das Verfahren „Wurzel abschätzen“ für 2015-OS-B1c und 2014-OS-B1h (brueche-dezimalzahlen.md) und „Quadratseite aus Fläche berechnen“ (2020-OS-B1d, flaechen.md).
101  Zielmarke: Einheit 1 – eine Potenz mit negativer Hochzahl gegen eine Dezimalzahl stellen und das Vergleichszeichen setzen, in zwei Schritten: 2⁻⁵ = 1/32 = 0,03125 < 0,25 (2022-OS-B1j, Niveau I; die anspruchsvollste Marke der Einheit, weil die negative Hochzahl erst in einen Bruch und dann in eine Dezimalzahl übersetzt werden muss); daneben die größte von drei Potenzen mit verschiedener Basis und verschiedenem Exponenten unterstreichen, nachdem alle drei ausgerechnet sind: 4³ = 64, 8⁴ = 4096, 2⁸ = 256, also 8⁴ (2019-OS-B1d, Niveau I) und als Basismarke der Exponent einer Zweier- und einer Viererpotenz durch wiederholtes Malnehmen: 2^x = 16 mit x = 4 (2020-OS-B1h, Niveau I) und 4^x = 256 mit x = 4 (2024-OS-B1g, Niveau I). Einheit 2 – eine ausgeschriebene dreizehnstellige Zahl mit hundert vervielfachen und das Ergebnis mit Einheit ausgeschrieben angeben: 100 Lichtjahre à 9 460 000 000 000 km sind 946 000 000 000 000 km (2015-OS-K3a, Niveau I, Kontext Astronomie – das einzige Kontextoriginal beider Themen); daneben die kleinste von vier negativen Zahlen mit und ohne Zehnerpotenz ankreuzen, −10³ = −1000 (2017-OS-B1e, Niveau I), eine Zehnerpotenzschreibweise mit negativer Hochzahl ausschreiben, 2,1 · 10⁻⁴ = 0,00021 (2019-OS-B1j, Niveau I), und unter drei ausgeschriebenen Zahlen die zu 9,46 · 10¹² passende ankreuzen, 9 460 000 000 000 (2015-OS-K3b, Niveau I); als Basismarke die drei Umwandlungen ohne Kontext: 850 000 = 8,5 · 10^5 mit einzutragender Hochzahl (2025-OS-B1d, Niveau I), 8,5 · 10⁵ = 850 000 (2016-OS-B1h, Niveau I) und 100 000 = 10⁵ (2017-OS-B1g, Niveau I). Einheit 3 – unter drei Aussagen über die Wurzel aus dem Quadrat einer negativen Zahl die wahre ankreuzen: √((−4)²) = +4, weil erst das Quadrat gerechnet wird und eine Wurzel nie negativ ist (2015-OS-B1j, Niveau I, Stern – der einzige Stern an einer Basisaufgabe beider Themen); daneben eine wahre Aussage über zwei Brüche und eine Wurzel finden, 8/5 > 3/2, weil √2 ≈ 1,41 < 1,5 ist (2015-OS-B1c, Niveau I), und vier Zahlen mit einer Wurzel aufsteigend ordnen, −0,512; −1/2; 1,4; √2 (2014-OS-B1h, Niveau I; beide Originale bei brueche-dezimalzahlen.md, Verfahren „Wurzel abschätzen“ hier); als Basismarke die Quadratseite aus einer Quadratzahl-Fläche, a = √36 = 6 cm (2020-OS-B1d, Niveau I; Original bei flaechen.md). Dazu als Nebenleistung die Wurzel als letzter Rechenschritt: FA = √(384² − 255²) ≈ 287,1 m (2024-OS-K6a, Niveau I, pythagoras.md), r = √(425 : (π · 7)) ≈ 4,40 cm (2022-OS-K2d, Niveau II, koerper.md) und x = 3 ± √2 mit den Nullstellen N1(1,59|0) und N2(4,41|0) (2025-OS-K5c, Niveau II, quadratische-funktionen.md).
````

## 2 Originale (26)

Kennungen aus „Prüfungsform“ und „Zielmarke“ in der Folge ihres ersten Auftretens; Spalten id, jahr, papier, punkte, gegeben, gesucht, verfahren, fehlerquelle, format, antwort.

### 2015-OS-B1j (msa-katalog-basis.csv)

jahr 2015 · papier OS · punkte 1 · format Ankreuzen · antwort Kreuz
- gegeben: drei Aussagen: √((−4)²) = −4; √((−4)²) = +4; √((−4)²) ist nicht definiert
- gesucht: die wahre Aussage
- verfahren: (−4)² = 16, √16 = 4
- fehlerquelle: „nicht definiert“ wegen negativer Basis oder −4 (Vorzeichen zurückholen)

### 2020-OS-B1h (msa-katalog-basis.csv)

jahr 2020 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: Gleichung 2^x = 16
- gesucht: x
- verfahren: 2 · 2 · 2 · 2 = 16
- fehlerquelle: x = 8 (16 : 2)

### 2024-OS-B1g (msa-katalog-basis.csv)

jahr 2024 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: 4^x = 256
- gesucht: x
- verfahren: Vierer-Potenzen: 4, 16, 64, 256
- fehlerquelle: 256 : 4 = 64 rechnen

### 2025-OS-B1h (msa-katalog-basis.csv)

jahr 2025 · papier OS · punkte 1 · format Ankreuzen · antwort Kreuz
- gegeben: Gleichung x(x + 5) = −6; Optionen x = 2, x = 3, x = −2, x = −6
- gesucht: der Wert, der die Gleichung erfüllt
- verfahren: Werte einsetzen: (−2) · 3 = −6
- fehlerquelle: Vorzeichen beim Einsetzen negativer Werte

### 2019-OS-B1d (msa-katalog-basis.csv)

jahr 2019 · papier OS · punkte 1 · format Eintragen · antwort Zahl
- gegeben: 4³, 8⁴, 2⁸
- gesucht: größte Zahl
- verfahren: Potenzen ausrechnen: 64, 4096, 256
- fehlerquelle: größte Basis oder größten Exponenten wählen, statt zu rechnen (2⁸)

### 2022-OS-B1j (msa-katalog-basis.csv)

jahr 2022 · papier OS · punkte 1 · format Eintragen · antwort Zahl
- gegeben: 2⁻⁵ und 0,25; Kästchen für <, =, >
- gesucht: Vergleichszeichen
- verfahren: 2⁻⁵ = 1/32 = 0,03125
- fehlerquelle: 2⁻⁵ = −32 oder = 0,25 (mit 2⁻² verwechseln)

### 2017-OS-B1e (msa-katalog-basis.csv)

jahr 2017 · papier OS · punkte 1 · format Ankreuzen · antwort Kreuz
- gegeben: −0,01; −10³; −10²; −0,1
- gesucht: die kleinste Zahl
- verfahren: −10³ = −1000 ist am weitesten links auf dem Zahlenstrahl
- fehlerquelle: −0,01 als kleinste wählen (Betrag statt Lage); −10² wählen (Exponent übersehen)

### 2017-OS-B1g (msa-katalog-basis.csv)

jahr 2017 · papier OS · punkte 1 · format Kurzantwort · antwort Term
- gegeben: 100 000
- gesucht: Schreibweise als Zehnerpotenz
- verfahren: Nullen zählen
- fehlerquelle: 10⁶ (Nullen verzählt); 1 · 10^5 mit Faktor ist ebenfalls richtig

### 2016-OS-B1h (msa-katalog-basis.csv)

jahr 2016 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: 8,5 · 10⁵
- gesucht: Zahl ohne Zehnerpotenz
- verfahren: Komma um fünf Stellen nach rechts
- fehlerquelle: 8 500 000 (Nullen an 85 anhängen) oder 85 000

### 2015-OS-K3b (msa-katalog-kontext.csv)

jahr 2015 · papier OS · punkte 1 · format Ankreuzen · antwort Kreuz
- gegeben: 9,46 · 10¹²; Auswahl: 94 600 000 000 000; 9 460 000 000 000; 946 000 000 000 000
- gesucht: die passende Zahl
- verfahren: Komma um zwölf Stellen nach rechts
- fehlerquelle: zwölf Nullen an 946 anhängen (946 000 000 000 000)

### 2019-OS-B1j (msa-katalog-basis.csv)

jahr 2019 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: 2,1 · 10⁻⁴
- gesucht: Dezimalzahl
- verfahren: Komma um vier Stellen nach links
- fehlerquelle: 0,0021 (drei Stellen) oder 21 000 (Vorzeichen des Exponenten ignoriert)

### 2025-OS-B1d (msa-katalog-basis.csv)

jahr 2025 · papier OS · punkte 1 · format Eintragen · antwort Zahl
- gegeben: 850 000 = 8,5 · 10^□ mit leerem Exponentenfeld
- gesucht: Exponent
- verfahren: Komma in 8,5 um 5 Stellen nach rechts verschieben
- fehlerquelle: Nullen zählen (4) statt Kommastellen

### 2015-OS-K3a (msa-katalog-kontext.csv)

jahr 2015 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: 1 Lichtjahr = 9 460 000 000 000 km
- gesucht: Kilometer für 100 Lichtjahre
- verfahren: mal 100: zwei Nullen anhängen
- fehlerquelle: Nullen falsch zählen

### 2022-OS-K2d (msa-katalog-kontext.csv)

jahr 2022 · papier OS · punkte 3 · format Rechnung · antwort Zahl
- gegeben: größerer Becher mit V = 425 ml, h = 7 cm
- gesucht: Radius
- verfahren: r = √(V : (π · h)) = √(425 : (π · 7))
- fehlerquelle: Wurzel vergessen (r = 19,3) oder durch 2π · h teilen

### 2025-OS-K5c (msa-katalog-kontext.csv)

jahr 2025 · papier OS · punkte 4 · format Rechnung · antwort Zahl
- gegeben: p(x) = x² − 6x + 7
- gesucht: Schnittpunkte mit der x-Achse
- verfahren: x² − 6x + 7 = 0; p-q-Formel: x = 3 ± √(9 − 7)
- fehlerquelle: Vorzeichen in der p-q-Formel (−p/2 = 3, nicht −3) oder Wurzel aus 9 + 7

### 2017-OS-K5d (msa-katalog-kontext.csv)

jahr 2017 · papier OS · punkte 4 · format Rechnung|Rechnung · antwort Term|Zahl
- gegeben: p: y = (x + 3)² − 2; Behauptung y = x² + 6x + 7
- gesucht: Nachweis der Normalform|Nullstellen
- verfahren: (x + 3)² − 2 = x² + 6x + 9 − 2; x² + 6x + 7 = 0: x = −3 ± √(9 − 7) (oder (x + 3)² = 2, x = −3 ± √2)
- fehlerquelle: (x + 3)² = x² + 9 (Mittelglied fehlt); Diskriminante 9 + 7 statt 9 − 7; nur eine Nullstelle

### 2015-OS-B1c (msa-katalog-basis.csv)

jahr 2015 · papier OS · punkte 1 · format Ankreuzen · antwort Kreuz
- gegeben: drei Aussagen: 1,5 < 3/2; 8/5 > 3/2; √2 > 3/2
- gesucht: die wahre Aussage
- verfahren: 3/2 = 1,5 (gleich, nicht kleiner); 8/5 = 1,6 > 1,5; √2 ≈ 1,41 < 1,5
- fehlerquelle: √2 als 2 lesen und √2 > 3/2 ankreuzen

### 2014-OS-B1h (msa-katalog-basis.csv)

jahr 2014 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: Zahlen −1/2; 1,4; −0,512; √2
- gesucht: aufsteigende Reihenfolge
- verfahren: −1/2 = −0,5 > −0,512; √2 ≈ 1,414 > 1,4
- fehlerquelle: −1/2 vor −0,512 (Beträge vergleichen) oder √2 vor 1,4

### 2023-OS-B1f (msa-katalog-basis.csv)

jahr 2023 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: 4,4; 0,44; 0,4²; 44 %
- gesucht: kleinster Wert
- verfahren: alle als Dezimalzahl: 4,4; 0,44; 0,16; 0,44
- fehlerquelle: 0,4² als 0,8 oder 1,6 rechnen

### 2020-OS-B1d (msa-katalog-basis.csv)

jahr 2020 · papier OS · punkte 1 · format Kurzantwort · antwort Zahl
- gegeben: Flächeninhalt eines Quadrats 36 cm²
- gesucht: Seitenlänge
- verfahren: a = √36
- fehlerquelle: 36 : 4 = 9 cm (Umfang-Logik)

### 2014-OS-K7a (msa-katalog-kontext.csv)

jahr 2014 · papier OS · punkte 4 · format Rechnung · antwort Zahl
- gegeben: p(x) = −x², g(x) = 2x − 3; Punkt S(−3|−9)
- gesucht: rechnerische Prüfung, ob S Schnittpunkt ist
- verfahren: p(−3) = −9 und g(−3) = −6 − 3 = −9; beide erfüllt (alternativ −x² = 2x − 3 lösen: x = −3 oder x = 1)
- fehlerquelle: p(−3) = +9 (Vorzeichen) oder nur in eine Funktion einsetzen

### 2014-OS-K3c (msa-katalog-kontext.csv)

jahr 2014 · papier OS · punkte 2 · format Rechnung · antwort Zahl
- gegeben: Anlage 1 000 €, 5 Jahre, 3 % pro Jahr
- gesucht: Guthaben nach 5 Jahren
- verfahren: 1000 · 1,03⁵ (oder Jahr für Jahr)
- fehlerquelle: 1000 + 5 · 30 = 1150 € (einfache Verzinsung)

### 2020-OS-K4c (msa-katalog-kontext.csv)

jahr 2020 · papier OS · punkte 3 · format Rechnung|Begründung · antwort Zahl|Text
- gegeben: Studie 1: y = 54 · 1,03^x (x Jahre ab 2019, y in Tausend Litern); Studie 2: von 2019 bis 2033 insgesamt ca. 40 % Steigerung
- gesucht: Vergleich beider Vorhersagen für 2033
- verfahren: x = 14: 54 · 1,03^14 ≈ 81,7; 54 · 1,4 = 75,6; vergleichen
- fehlerquelle: x = 2033 einsetzen; 14 · 3 % = 42 % als Bestätigung von 40 % werten

### 2026-FOR-K7c (msa-katalog-kontext.csv)

jahr 2026 · papier FOR · punkte 3 · format Kurzantwort|Rechnung · antwort Term|Zahl
- gegeben: Miete im ersten Jahr (2026) 650 € monatlich, jährlich +1,9 % (2026 = Jahr 0, 2027: 662,35 €)
- gesucht: Funktionsgleichung M(t)|Miete 2040
- verfahren: M(t) = 650 · 1,019^t mit t = Jahre nach 2026; 2040: t = 14
- fehlerquelle: t = 15 setzen (862,04 €) oder 2040 direkt einsetzen; 1,9 statt 1,019 als Faktor

### 2015-OS-K3c (msa-katalog-kontext.csv)

jahr 2015 · papier OS · punkte 4 · format Rechnung|Rechnung · antwort Zahl|Zahl
- gegeben: Lichtgeschwindigkeit ca. 3 · 10⁵ km/s; Entfernung Sonne – Proxima Centauri ca. 4,03 · 10¹⁵ km; 1 Jahr = 365 Tage
- gesucht: Lichtlaufzeit in Sekunden|Lichtlaufzeit in Jahren
- verfahren: t = s : v = 4,03 · 10¹⁵ : (3 · 10⁵) ≈ 1,34 · 10¹⁰ s; ein Jahr = 365 · 24 · 60 · 60 = 31 536 000 s; Sekunden durch Jahressekunden
- fehlerquelle: Zehnerpotenzen falsch dividieren (10¹⁵ : 10⁵ = 10³) oder Jahr nur mit 24 · 365 umrechnen

### 2024-OS-K6a (msa-katalog-kontext.csv)

jahr 2024 · papier OS · punkte 2 · format Rechnung · antwort Zahl
- gegeben: rechtwinkliges Dreieck AFB mit rechtem Winkel in F, FB = 255 m, AB = 384 m; FA ist der Höhenunterschied
- gesucht: FA
- verfahren: FA = √(384² − 255²)
- fehlerquelle: Quadrate addieren (461 m)

Nur außerhalb von „Prüfungsform“ genannt, nicht aufgenommen: 2025-OS-K4a, 2024-OS-B1f, 2021-OS-B1h, 2025-OS-K2a

## 3 Maßstab (unterrichtsblatt.md, wortgleich)

### 2.2

````text
2.2 Zone „kennst du schon" – die Voraussetzungen, eine Stufe
zurück. Zweck: ins Thema hineinführen, sehen, ob der Schüler so
weit ist, an Vergessenes erinnern. Die Zone lehrt nichts Neues
und nennt keinen Begriff des Themas. Sie ist auf der Zeitachse
die Zone hinter dem Schüler, kein eigenes Blatt; bereitgestellt
wird sie trotzdem zuerst als eigenes PDF (2.7). Untertitel auf
dem Blatt: „Das kennst du schon". Hängt der Schüler hier, ist
die Lücke älter als das Thema – das zeigt das Blatt durch die
Zone selbst, ohne Kennzeichnung.
- Je Fertigkeit des Abschnitts eine Hauptnummer mit eigener
  Anweisung; Titel ist die Fertigkeit als Ich-kann-Satz mit dem
  Wort, das die Klasse kennt („Ich kann die Nullstelle einer
  Geraden berechnen", nicht „wo eine Gerade die x-Achse
  schneidet"). Die Nummern der Zone sind die ersten Nummern des
  Blatts (1, 2, 3 …), keine eigene Zählung (Z1) und kein
  Neubeginn im Lernblatt; die Nummer ist die Adresse.
- Breite nach Bestellung (1.1): mit Wiederholung alle
  Fertigkeiten, die das Lernblatt braucht, dazu die Zweige des
  Themas, die die Zeitmarke vor die Eingabeklasse legt, als je
  eine Fertigkeit mit dem Grundfall des Zweigs; „wiederholung
  kurz" je Fertigkeit eine leichte und eine Fallstrick-
  Teilaufgabe; „nur das neue" keine Zone.
- Reihenfolge nach erster Verwendung im Lernblatt: die Angabe
  „– Einheit n" der Fertigkeitszeile, kleinste Einheit zuerst;
  bei gleicher Einheit die Lehrplanfolge der Voraussetzungs-
  themen; ohne Angabe die Reihenfolge des Eintrags. Innerhalb
  der Hauptnummer leicht → Fallstrick.
- Je Fertigkeit: zwei sehr leichte Teilaufgaben (im Kopf lösbar),
  eine mittlere (negative Zahl, Dezimalzahl, Bruch, Einheit) und
  je eine für jeden Fallstrick der Fertigkeit, an dem das
  Lernblatt hängt. Du planst rückwärts: erst die Stellen des
  Lernblatts, die die Fertigkeit brauchen, daraus die
  Fallstricke. Eine Fertigkeit, die das Lernblatt nirgends
  braucht, entfällt – auch eine, die nur ein abgewählter Zweig
  gebraucht hätte. Dazu einmal je Zone eine Fehler-finden-
  Aufgabe zum häufigsten Fallstrick, unmittelbar darauf als
  eigene Hauptnummer eine gleichartige zum selbst Rechnen – das
  Paar gibt es nur in der Zone (2.3 c).
- Schreibform aus dem Eintrag: Nennt die Fertigkeitszeile eine
  Form (Tabelle, Dreisatz, Streifen), setzt du sie; ein Dreisatz
  steht im zweispaltigen Schema mit den Operationen am Pfeil, nie
  als Zeile mit Doppelpunkt (3.2). Die Zahlen eines Dreisatzes
  der Zone sind so gewählt, dass beide Schritte im Kopf gehen:
  glatter Teiler, Produkt ohne Übertrag (4 Hefte 6 €; nicht 3 m
  7,50 €). Schriftliche Multiplikation ist keine Fertigkeit der
  Zone, sondern ein eigenes Thema.
- Kein Kasten, keine Stufenmarkierung, keine Prüfungshöhe: die
  Zone hat keine Decke.
- Lösungen in der Lösungsdatei (3.4), dazu die Zeile, welche
  Hauptnummer welchen Zweig trägt („1–2 → Einheit 1 und 2 ·
  3 → Einheit 3").
Beim Fokus trägt die Zone nur die Fertigkeiten, die der Typ
braucht, je zwei Teilaufgaben, als erste Seite des Fokus.
````

### 2.3 c

````text
c) Pflichtelemente je Zweig, aus den Typen des Zweigs: Fehler
   finden – Muster aus „Typische Fehler", eigene Zahlen, in der
   Schreibform des Verfahrens (bei Umformungen senkrecht mit
   `\rechnung`), Fehler benennen und korrigieren; Begründen
   oder Entscheiden ohne Rechnung; Darstellungswechsel in beide
   Richtungen, soweit die Typen es tragen; eine Anwendung, deren
   Mathematik vom Kontext getragen wird (realistische Größen, im
   Kontext sinnvolle Frage). Typen des Zweigs, die in keiner
   Kette stehen (Ordnen, Ergänzen, Aussagen prüfen, Umkehrung),
   bekommen eine eigene Hauptnummer. Gemischte Aufgaben, deren
   Punkt die Zuordnung ist („erst zuordnen, dann rechnen"),
   verraten das Verfahren nicht.

   Eine Hauptnummer, eine Fertigkeit, eine Antwortform: Nach
   „Ich finde den Fehler" folgt in derselben Nummer keine
   Rechenaufgabe; Ankreuzen und Begründen stehen nicht in
   derselben Nummer; wechselt die Anweisung so, dass eine andere
   Fertigkeit gefragt ist, beginnt eine neue Hauptnummer. Die
   Zone ist die Ausnahme mit ihrem Paar aus Fehler finden und
   gleichartiger Rechenaufgabe (2.2), und dort sind es zwei
   Nummern.
````

### 2.4 b–c

````text
b) Die Kette. Maßstab ist das strukturelle Merkmal, nicht die
   Stückzahl: Ein Merkmal ist ein Fall, der eine andere
   Entscheidung oder einen anderen Schritt verlangt – anderer
   gegebener Wert, andere Einheit, Dezimalzahl oder Bruch statt
   ganzer Zahl, negatives Vorzeichen, Sonderfall, typischer
   Fallstrick, Umkehrung des Verfahrens. Die Sprossen kommen aus
   dem Eintrag; fehlt zwischen zwei Sprossen ein Schritt, den die
   Prüfungshöhe verlangt, schließt du ihn mit einer Zwischen-
   sprosse und sagst es im Ausgabeblock. Zwei Teilaufgaben, die
   sich nur in den Zahlen unterscheiden, sind dieselbe Sprosse
   und kommen nur beim Grundfall vor. Aufwandsmerkmale (Rundung,
   krumme Zahlen) kommen nach allen Strukturmerkmalen, nie
   zwischen die glatten Fälle. Ein Schüler, der das Thema gerade
   beginnt, schafft die ersten sechs Teilaufgaben jeder
   Verfahrens-Hauptnummer, ohne die Sprossen ab der Mitte zu
   können. Ablesetypen zählen als Verfahrenstypen, die Grafik ist
   nur der Träger: mehrere Objekte je Grafik, höchstens zwei
   Grafiken je Hauptnummer. Aufwandsintensive Typen (Wertetabelle,
   Zeichnen, Konstruktion): mindestens drei Teilaufgaben, die
   erste sehr leicht. Konzept- und Kontexttypen (Begründen,
   Entscheiden, Fehler finden, Textaufgaben mit einer Situation):
   eine bis drei Teilaufgaben, gestuft wie in einer Prüfung –
   Vorbereitungsschritt, Rechnung, Deutung; bei Begründen erst der
   klare Fall, dann der subtile. Bei Entscheidungstypen mit
   Ja/Nein-Antwort liegen richtig und falsch etwa halbe-halbe in
   gemischter Reihenfolge.

c) Prüfungshöhe. Jede Verfahrens-Hauptnummer endet mit genau einer
   Teilaufgabe in Form und Anspruch der zentralen Prüfung nach 1.5
   (P10, Abitur Teil A oder B, FHR). Nennt der Eintrag für die
   Einheit ein Original, ist das die Teilaufgabe – verfremdet, mit
   Jahr (3.6); sie darf eingeführte Merkmale kombinieren, führt
   aber kein neues ein. Zerfällt die Einheit in mehrere Haupt-
   nummern, trägt die letzte das Original, die anderen enden auf
   ihrer höchsten Sprosse. Prüfungsniveau wird in einer Stunde
   nicht erreicht; die Aufgabe ist Zielmarke und bleibt stehen.
   Trägt der Zweig „keine P10-Aufgabe", ist die Decke die
   Prüfungsaufgabe, in der er gebraucht wird, sonst die
   Lehrwerk-Konvention (1.5).
````

### 3.6

````text
3.6 Zahlen, Verfremdung, Formulierung. Zahlenwerte so gewählt,
dass Ergebnisse endlich sind und leichte Aufgaben im Kopf
rechenbar; periodische Dezimalbrüche tragen einen Hinweis. Keine
Aufgabe erscheint doppelt. Keine ganze Gleichung, kein Term,
kein Zahlenpaar und keine Funktion aus Kasten, Beispiel oder
Original des Eintrags in einer Teilaufgabe (2.1). Verfremdetes
Original: gleiches Verfahren, gleiche Falle, gleiche Form
(Ankreuzen, Lückensatz, Rechnung mit Rundung), andere Zahlen,
anderer Kontext; am Ende des Aufgabentexts in Klammern Prüfung,
Jahr und Papier, wie der Eintrag es nennt: „(P10 2018 FOR)",
„(P10 2025 GYM)", „(Abitur 2022 GK)", „(FHR 2024)".
Formulierungen eindeutig. Buchstaben und Symbole, die im Aufgaben-
text nicht erklärt sind, werden nicht verwendet, auch nicht T für
Term oder L für Lösungsmenge. Ein Buchstabe steht auf einem Blatt
für genau eine Sache: Seitenlabels verschiedener Figuren und
Variablen in Textaufgaben überschneiden sich nicht.
````

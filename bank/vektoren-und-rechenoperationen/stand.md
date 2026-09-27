# Stand: vektoren-und-rechenoperationen

Katalog-Commit: 95b0f8b09856c14466ca030dd604451b8d259cfa
Datum: 2026-09-27
Erster Sek-II-Eintrag der Bank.

## Zeilen je Datei und hoehe

| Datei | Zeilen | vorstufe | grundfall | sprosse | pruefung | pflicht |
|-------|-------:|---------:|----------:|--------:|---------:|--------:|
| zone  |     27 |        – |        12 |      14 |        – |       1 |
| e1    |     41 |        8 |         5 |      12 |        4 |      12 |
| e2    |     43 |        4 |         5 |      18 |        4 |      12 |
| e3    |     23 |        4 |         5 |       3 |        2 |       9 |

## Originale je Einheit

Im Feld original:
- e1: 2025MerhoehtAAGLAA11-a, 2021MgrundlegendAAGLAA112-a
- e2: 2021MgrundlegendAAGLAA12-b, 2021MgrundlegendAAGLAA12-a,
  2024MgrundlegendAAGLAA211-b, 2019MerhoehtAAGLAA21-b,
  2022MerhoehtAAGLAA221-b, 2026MgrundlegendAAGLAA222-b,
  2025MerhoehtAAGLAA223-b
- e3: keines

Nur als Prüfkennung im Text, Feld null (Befund Kennung):
- e1: 2025MerhoehtBAGLAA1WTR-2b (k2 s4 v1),
  2022MerhoehtBAGLAA2WTR2-1f (k2 s5 v1),
  2024MgrundlegendBAGLAA1WTR-1e (k2 s6 v1–v2),
  2025MerhoehtBAGLAA1MMS-1a (k2 s6 v3–v4)
- e2: 2026MgrundlegendBAGLAA2MMS2-1a (k1 s1 v2),
  2026MerhoehtBAGLAA1WTR-1a (k1 s3 v1),
  2022MerhoehtBAGLAA1WTR-1b (k1 s4 v1),
  2017MgrundlegendBAGLAA2WTR2-1c (k1 s4 v2),
  2017MerhoehtBAGLAA2WTR1-1b (k1 s4 v3)
- e3: 2019MgrundlegendBAGLAA2WTR2-1d (k1 s2 v1),
  2019MgrundlegendBAGLAA2WTR2-1e (k1 s3 v1–v2)

## Prüfskript vor der Korrektur

- zone: 4 Abweichungen, alle „merkmal uneinheitlich“ (s1)
- e1: 6 Abweichungen, alle „original unvollständig“
  (Teil-B-Kennung); danach 1 Warnung (Prüfungshöhe ohne Original)
- e2: 0
- e3: 0; 1 Warnung (Prüfungshöhe ohne Original)

Stand nach der Korrektur: 0 Abweichungen, 2 Warnungen – beide
Folge der Nullsetzung von original (Befund Kennung).

## Entscheidungen

1. Prüfkennung ohne P10: „(Abitur <Jahr> GK)“ für grundlegendes,
   „(Abitur <Jahr> LK)“ für erhöhtes Niveau nach unterrichtsblatt
   3.6; MMS-/CAS-Fassung und Teil A/B stehen nicht darin.
2. Punkte und Vektoren als Zeilentupel mit senkrechtem Strich wie
   im Merkkasten, A(1 | 2 | 0) und (3 | −1 | 2); Spaltenvektoren
   gehen nicht, weil aufgabe keine Umgebung (pmatrix) tragen darf.
3. pruef trägt bei Tripeln nur die Zahlen, die das Skript an der
   Ergebnisstelle liest (meist die erste Koordinate); alle
   Koordinaten sind bei der Erzeugung aus den Aufgabenwerten
   gerechnet.
4. Originale, deren Kennung das Skript ablehnt: original null,
   Prüfkennung im Text, Menge weiter 2 je Original; daher die
   Warnungen in e1 k2 s6 (4 Zeilen) und e3 k1 s3 (2 Zeilen).
5. Schrägbilder mit ksys3, \rquader und \rpunkt*-Beschriftung;
   Stäbe als \rgerade[0:1], Draufsicht in leerem ksys, ihre
   Lösungsgrafik mit \funktionab.
6. Zone nach erster Verwendung: Verschiebung, Pythagoras (E1),
   Raum, Terme (E2), Verhältnisse, Skalarprodukt (E3); kette der
   Zone bis zum Gedankenstrich, die Zeilen haben keinen
   Doppelpunkt.
7. Zone-Paar in der Pythagoras-Kette zum Fallstrick „beide
   Vorzeichen“, weil die Betragsgleichung in E1 daran hängt.
8. Vorstufen „Zahl oder Pfeil?“ mit den Optionen Zahl/Vektor,
   weil Sachvektoren in E3 keine Pfeile sind; der Kettenname
   bleibt wortgleich.
9. Pflicht: E1 und E2 alle vier Arten, E3 ohne darstellung (der
   Grundfall ist selbst der Wechsel Liste → Vektor); sprosse_text
   von darstellung und anwendung aus den Kern-Zitaten der
   Zeilen 80 und 15.
10. Erkennungsschritt „Faktor gesucht oder Richtung gesucht?“
    einmal in E1 als k1; kette ist die Frage ohne Anführungszeichen.

## Befunde

- Katalog: „Zahl oder Pfeil?“ (Z. 35) wiederholt die Vorstufen
  von E1 und E3 (Z. 83, 85), „Wohin führt der Term?“ (Z. 36) die
  von E2 (Z. 84); beide Erkennungsschritte entfallen nach bank.md.
- Prüfskript, KENNUNG: Teil-B-Kennungen mit Ziffer vor dem
  Buchstaben (…WTR-1e) und Landeskennungen (2018-bb-ea-B3.2c)
  gelten als „original unvollständig“; 14 Zeilen tragen deshalb
  null.
- Prüfskript, Ergebnisstelle: ein Tripel (a | b | c) wird nicht
  gelesen, nur die erste Zahl der Lösung zählt; PUNKT sollte
  n-Tupel kennen.
- Prüfskript, Sperre: zahlenpaare kennt nur (a|b); Tripel aus
  Kasten und Originalen werden nicht gesperrt (von Hand gemieden).
- bank.md: Feld original und Prüfkennung sind in P10-Sprache
  beschrieben; für Sek II fehlen Abitur-Kennung, GK/LK und Teil.
- Vorlage: kein Baustein für Spaltenvektoren und keiner für einen
  Vektorpfeil im ebenen ksys.
- Katalog: die Landeszeile 2018-bb-ea-B3.2c (Z. 90) trägt keine
  eigene Sprosse; ihre Lagebeschreibung deckt E2 k1 s2 mit dem
  iqb-Zwilling 2021MgrundlegendAAGLAA12-a.

## Offene Punkte

- Die 14 Felder original nachtragen, sobald das Skript die
  Kennungen annimmt.
- Rendern ungeprüft (kein LaTeX): ksys3-Optionen x1max=7 und
  x3min=-3, leere Labels bei \rgerade und \rvektorab, Lage der
  Eckenlabels am Quader.

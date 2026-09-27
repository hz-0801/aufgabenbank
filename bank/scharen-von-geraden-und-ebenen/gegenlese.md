# Gegenlese scharen-von-geraden-und-ebenen

Datum: 2026-09-27
Modell: claude-opus-5-5
Geprüfte Zeilen: 157
Korrekturen: 1

## Entscheidungen

scharen-von-geraden-und-ebenen-e4-k1-s3-v2: Der Satz „bei k = 4 bleibt die Eckenzahl“ war falsch, und die Randwerte fehlten. Weil die Ergänzung eindeutig nachgerechnet ist, habe ich sie als Korrektur eingetragen und nicht nur als Befund geführt; pruef [2, 4, 6] bleibt.

## 1 Rechnung

scharen-von-geraden-und-ebenen-e4-k1-s3-v2: Bei k = 4 ist die Schnittfigur ein Viereck mit den Ecken (0|2|0), (2|0|2), (2|1|0) und (0|1|2), die Eckenzahl bleibt also nicht; k = 2 und k = 6 fehlten (je drei Ecken) – korrigiert: „drei für $6 < k < 8$ – bei $k = 4$ bleibt die Eckenzahl, aber die getroffenen Kanten wechseln“ → „drei für $6 < k < 8$; drei Ecken für $k = 2$ und $k = 6$, vier Ecken für $k = 4$ – dort wechseln die getroffenen Kanten“

## 2 Eindeutigkeit

keine

## 3 Merkmal

scharen-von-geraden-und-ebenen-zone-f3-v2: Die Variante des Grundfalls („glatter Faktor“) enthält schon den Fallstrick von Sprosse 3 (Faktor 2 aus x_1 und x_2, Widerspruch erst in x_3). Damit bringt f3-v4 nichts Neues – v2 als kollineares Paar mit anderem Faktor fassen oder den Widerspruch in eine frühere Koordinate legen

scharen-von-geraden-und-ebenen-e4-k1-s5-v1: Die Varianten ändern das Merkmal: v1 und v2 stellen nur die Spurgeraden auf, ohne Lotfußpunkt; v3 zeichnet nur die Lotfußpunkte ein, ohne die Spurgeraden zu bestimmen (alle Varianten v1–v3) – in v1 und v2 den Lotfußpunkt vom Ursprung ergänzen und in v3 die Spurgerade selbst bestimmen lassen, oder alle drei auf dasselbe Merkmal bringen

## 4 Schreibform

scharen-von-geraden-und-ebenen-e3-k1-s4-v1: Die Lösung springt von „kleinste Höhe MQ_k“ zu „F_k senkrecht zu SC“. Es fehlen zwei Schritte: dass MQ_k ⊥ BD gilt (MQ_k ist also die Höhe) und dass aus MQ_k ⊥ SC zusammen mit BD ⊥ SC die Ebene F_k ⊥ SC folgt (alle Varianten v1–v2) – ergänzen: „MQ_k ⊥ BD; kürzeste Höhe bei MQ_k ⊥ SC, und da auch BD ⊥ SC, steht F_k senkrecht auf SC“

## 5 Ankreuzen

keine

## 6 Fehler finden

keine

Sauber: 150 Zeilen ohne Befund

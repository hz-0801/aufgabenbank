#!/usr/bin/env python3
"""bericht.py – baut bau/hefte/bericht.md aus bau.json und ergebnis.json.

Aufruf (aus der Repo-Wurzel): python3 bau/hefte/bericht.py
Zählt je Heft Aufgaben (Anlauf/Prüfungshöhe), Seiten, Punkte der
Originale (aus den Katalogen von mathe-nachhilfe, über
werkzeuge/zusammenbau.py), ausgelassene Zeilen und die häufigsten
Fehler nach Baustein.
"""

import collections
import importlib.util
import json
import re
from pathlib import Path

HIER = Path(__file__).resolve().parent
WURZEL = HIER.parent.parent
REIHE = ["msa-funktionen", "msa-geometrie", "msa-daten", "msa-zahlen",
         "basis-zahlen", "basis-geometrie", "basis-rest", "abi-gk-analysis-1",
         "abi-gk-analysis-2", "abi-gk-stochastik", "abi-gk-geometrie"]

ENTSCHEIDUNGEN = """## Entscheidungen dieses Laufs

1. Prüfungshöhe = jede Bankzeile, deren Original (sonst die Prüfkennung
   im Text) zum Profil des Hefts gehört, gleich welche hoehe. Grund: in
   Sek II stehen die meisten Originale an Sprossen mitten in der Kette
   (GK: 170 Zeilen hoehe pruefung, 535 an grundfall/sprosse). Zeilen
   hoehe pruefung ohne Original und ohne Prüfkennung (Zielmarken) sind
   nicht im Heft, weil sie keine Prüfkennung tragen.
2. Profile: msa = Papier OS, FOR, EBR, GYM („(P10 Jahr Papier)“);
   abitur-gk = Papier mit -ga oder -gk (iqb grundlegend auch MMS, be-gk,
   bebb-gk, bb-gk; „(Abitur Jahr GK)“). FHR und LK bleiben draußen.
3. Anlauf je Kette: Vorstufe, Grundfall und eine Sprosse, je kleinste
   Variante ohne Original; Prüfkennung entfernt. Die Bank zählt
   Fallstricke nicht nach Häufigkeit; genommen wird die erste Sprosse
   nach dem Grundfall, deren Merkmal einen Fallstrick nennt (Fallstrick,
   Falle, Fehler, verwechseln, vertauschen, Vorzeichen, Klammer,
   Sonderfall, negativ, Null), sonst die erste Sprosse nach dem
   Grundfall. Die Wahl steht je Kette in der zusammenbau.log (AUSWAHL).
4. Ketten ohne Prüfungshöhe im Profil fehlen ganz (auch ohne Anlauf);
   Einträge ganz ohne stehen oben je Heft. Die Pflichtkette zählt zur
   gleichnamigen Verfahrenskette.
5. Sternchen: \\steil bzw. \\sgl, wenn das Original im Katalog stern = ja
   trägt (OS-Hefte bis 2025, nur FOR); Legende in der Fußzeile. Abitur
   und GYM tragen keine Sternchen.
6. Basis (5–7): Original mit Papier OS, FOR oder EBR und Kennung
   -<Papier>-B<n> (Basisteil), ohne Anlauf.
7. Kennung H<n> über bau/register.csv (Rezept H aus v0.3); die
   Registerzeilen sind die einzige Schreibstelle außerhalb von
   bau/hefte/ und werkzeuge/.
8. Satz: Eine Gleichung ohne $ im gleichungsraster wird als Mathe
   gesetzt, ein Text im gleichungsraster als Teilaufgabe (\\teil) – sonst
   Kompilierfehler bzw. Text über die Spalte hinaus (nur im Heft).
9. Ausgelassene Teilaufgaben stehen als „(ausgelassen)“ mit ihrem
   Buchstaben da, die Lösung ebenso; der alte Quelltext bleibt als
   Kommentar mit Grund. Folgefehler werden durch ein Kleinstdokument je
   Teilaufgabe von der Ursache getrennt.
10. daten lag beim ersten Bau nur mit e1, e2 und zone in bank/ (eine
    andere Sitzung baute den Eintrag); nach deren Commits (e3–e7,
    stand.md) sind msa-daten und basis-rest neu gebaut (DAT-H2,
    LIN-H3). Die Registerzeilen DAT-H1 und LIN-H2 bleiben als
    verbrauchte Nummern; ihr Ordner trägt jetzt den neuen Bau.
"""


def lade_zb():
    spec = importlib.util.spec_from_file_location(
        "zb", WURZEL / "werkzeuge" / "zusammenbau.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def bankzeilen():
    aus = {}
    for p in (WURZEL / "bank").glob("*/e*.jsonl"):
        for z in p.read_text(encoding="utf-8").splitlines():
            if z.strip():
                d = json.loads(z)
                if "id" in d and "aufgabe" in d:
                    aus[d["id"]] = d
    return aus


def baustein(z, namen):
    """Baustein, an dem die Zeile scheitert (erste Vermutung aus dem Text)."""
    text = z.get("aufgabe", "")
    if re.search(r"(?<![\\$])__", re.sub(r"\$[^$]*\$", "", text)):
        return "Lückensatz: __ im Aufgabentext (Unterstrich außerhalb Mathe)"
    for quelle in (z.get("grafik", ""), text):
        for c in re.findall(r"\\([A-Za-z]+)", quelle):
            if c in namen:
                return f"\\{c} (form {z.get('form')})"
    return f"Text (form {z.get('form')})"


def main():
    zb = lade_zb()
    log = zb.Log()
    kat = zb.lies_kataloge(log)
    namen = set(zb.BP.lade_bausteine(WURZEL / "mappen" / "_bausteine.md"))
    bank = bankzeilen()
    erg = json.loads((HIER / "ergebnis.json").read_text(encoding="utf-8"))
    zeilen, gesamt_fehler = [], collections.Counter()
    fehler_ids = collections.defaultdict(set)
    meldungen = collections.defaultdict(set)
    kopf = ("| Heft | Kennung | Einträge | HN | Anlauf | Prüfungshöhe | Seiten "
            "| Lösungen | Originale | Punkte | ⋆ | ausgelassen |")
    tab = [kopf, "| --- | --- | --: | --: | --: | --: | --: | --: | --: | --: "
           "| --: | --: |"]
    je_heft = []
    for n in REIHE:
        z = json.loads((HIER / n / "bau.json").read_text(encoding="utf-8"))
        e = erg.get(n, {})
        auf = z["aufgaben"]
        anl = sum(1 for a in auf if a.get("lage") == "anlauf")
        pr = sum(1 for a in auf if a.get("lage") == "pruefung")
        hn = len({a["hauptnummer"] for a in auf})
        orig = {a["original"] for a in auf if a.get("original")}
        mit_p = {o for o in orig if (kat.get(o) or {}).get("punkte")}
        punkte = sum(float(kat[o]["punkte"].replace(",", ".")) for o in mit_p)
        stern = sum(1 for a in auf if a.get("stern"))
        teile = len(z["eintraege"]) - len(z["leere_eintraege"])
        tab.append(f"| {n} | {z['kennung']} | {teile} | {hn} | {anl} | {pr} | "
                   f"{e.get('seiten')} | {e.get('seiten_loesungen')} | "
                   f"{len(orig)} | {punkte:g} ({len(mit_p)}) | {stern} | "
                   f"{len(e.get('ausgelassen', []))} |")
        for a in e.get("ausgelassen", []):
            b = baustein(bank.get(a["id"], {}), namen)
            gesamt_fehler[b] += 1
            fehler_ids[b].add(a["id"])
            meldungen[b].add(a["grund"].split(".")[0][:60])
        je_heft.append((n, z, e))
    zeilen += ["# Prüfungshefte nach Themen", "",
               "Stand: siehe Commit „bau/hefte: elf Prüfungshefte“. "
               "Rezept H (werkzeuge/zusammenbau.py v0.4, `--heft`, "
               "`--nur-basis`), Vorlage mathblatt.sty aus hz-0801/blattbau, "
               "gerendert mit bau/hefte/render.py (xelatex, je Dokument zwei "
               "Läufe, höchstens 3 Versuche je Heft). Diese Datei baut "
               "bau/hefte/bericht.py.", "",
               "## Übersicht", "",
               "HN Hauptnummern; Anlauf und Prüfungshöhe in Teilaufgaben; "
               "Seiten des Hefts und der Lösungen (pdfinfo); Originale: "
               "verschiedene Originalkennungen hinter den Prüfungshöhen; Punkte: "
               "Summe der Katalogpunkte dieser Originale (in Klammern, wie viele "
               "Punkte tragen) – jedes Original steht in der Bank verfremdet "
               "meist zweimal, die Summe zählt es einmal; ⋆ Teilaufgaben mit "
               "Sternchen (OS-Original mit stern = ja, nur FOR).", ""] + tab
    zeilen += ["", "## Je Heft", ""]
    for n, z, e in je_heft:
        zeilen.append(f"### {n} ({z['kennung']})")
        zeilen.append("")
        zeilen.append("Aufruf: `" + " ".join(
            ["zusammenbau.py"] + z["eintraege"] + ["--heft",
             z["bestellung"]["heft"]] + (["--nur-basis"] if
             z["bestellung"]["nur_basis"] else [])) + "`")
        zeilen.append("")
        if z["leere_eintraege"]:
            zeilen.append("Ohne Prüfungshöhe im Profil, daher nicht im Heft: "
                          + ", ".join(z["leere_eintraege"]) + ".")
        if z["fehlende_eintraege"]:
            zeilen.append("Fehlt in bank/: " + ", ".join(z["fehlende_eintraege"])
                          + ".")
        zeilen.append(f"Versuche: {e.get('versuche')}, Fehlerstellen je Versuch "
                      f"{e.get('fehler_je_versuch')}; fehlende Zeichen im PDF: "
                      f"{e.get('fehlende_zeichen')}"
                      + (f" ({' '.join(e.get('fehlende_zeichen_art', []))})"
                         if e.get("fehlende_zeichen") else "") + ".")
        if e.get("ausgelassen"):
            zeilen.append("")
            zeilen.append("Ausgelassen:")
            for a in e["ausgelassen"]:
                zeilen.append(f"- Nr. {a['nr']} {a['id']} – {a['grund']}")
        if e.get("folgefehler_verschont"):
            zeilen.append("")
            zeilen.append("Folgefehler, Teilaufgabe allein fehlerfrei, bleibt: "
                          + ", ".join(e["folgefehler_verschont"]) + ".")
        zeilen.append("")
    zeilen += ["## Die häufigsten Fehler nach Baustein", "",
               "Gezählt je ausgelassener Teilaufgabe und Heft (eine Bankzeile in "
               "zwei Heften zählt zweimal; in Klammern die Zahl verschiedener "
               "Bankzeilen). Der Baustein ist der erste Vorlagenbaustein der "
               "Zeile (Grafik vor Text) oder der Lückensatz.", ""]
    for i, (k, v) in enumerate(gesamt_fehler.most_common(5), 1):
        zeilen.append(f"{i}. {k}: {v}× ({len(fehler_ids[k])} Bankzeilen: "
                      + ", ".join(sorted(fehler_ids[k])) + "; Meldung: "
                      + " / ".join(sorted(meldungen[k])) + ")")
    zeilen += ["", ENTSCHEIDUNGEN.rstrip()]
    (HIER / "bericht.md").write_text("\n".join(zeilen) + "\n", encoding="utf-8",
                                     newline="\n")
    print("\n".join(tab))


if __name__ == "__main__":
    main()

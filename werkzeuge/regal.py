#!/usr/bin/env python3
"""regal.py – Plan aller Kompetenzblätter (Regal), Stand 2026-09-28.

Aufruf (aus der Repo-Wurzel):
    python3 werkzeuge/regal.py [--kuerzel <_kuerzel.csv>] [--katalog <ordner>]

Liest alle Ketten der Bank (bank/<eintrag>/e<n>.jsonl) und schreibt
bau/regal/regal.csv (eine Zeile je geplantem Kompetenzblatt) und
bau/regal/regal.html (eine selbständige Seite mit zwei Ansichten).

Ein Kompetenzblatt ist (Beschluss des Lehrers vom 28.09.):
- je Verfahrenskette (Kette mit Grundfall) eines, die gleichnamige
  Pflichtkette gehört dazu;
- je Einheit eines für die Typen ohne Kette (Ketten ohne Grundfall, die
  nicht nur aus Pflichtelementen oder nur aus einer Vorstufe bestehen),
  im Regal mit kette „*“ und dem Namen „Typen ohne Kette: …“.
Erkennungsschritte (nur Vorstufe) und reine Pflichtketten bekommen kein
eigenes Blatt.

Spalten von regal.csv (Semikolon, UTF-8, LF):
  kennung   vorgesehene Kennung XXX-K<n>: Kürzel aus katalog/_kuerzel.csv
            (mathe-nachhilfe), n je Eintrag fortlaufend nach Einheit und
            Kette. Ein schon gebautes Blatt (bau/register.csv, Rezept K)
            behält seine Kennung; die übrigen zählen um die belegten
            Nummern herum.
  bereich   Sek I / Sek II (Abschnitt in katalog/index.md; Ketten mit
            „Sek II“ im Namen: Sek II)
  thema     Leitidee des Eintrags (katalog/index.md, ohne Klammerzusatz)
  eintrag, einheit (Katalogeinheit „n Titel“, wie zusammenbau v0.7 sie
            findet), kette (Name in der Bank, „*“ = Typen ohne Kette),
            einheit_bank (Nummer der Bankdatei)
  ich_kann  Titel aus bau/regal/ich-kann.csv; fehlt er, „Ich kann: <Kette>.“
            und Meldung auf der Konsole
  klasse_os, klasse_gym   aus der Marken-Zeile der Katalogeinheit
            („9–10“, „9“; Sek II: „Q1“ aus „BE Q1“)
  pruefung  „P10 ×n“, „Abi GK ×n“, „Abi LK ×n“, „FHR ×n“ je Profil der
            Originale der Kette (zusammenbau.pruefwort_zahl: Jahrgänge, in
            denen einer der Typen dieser Originale vorkommt); leer ohne
            Original
  gruppe    Prüfungsbereich für die Ansicht „nach Prüfung“: MSA Funktionen,
            Geometrie, Daten, Zahlen; Abitur GK Analysis I, Analysis II,
            Stochastik, Geometrie – nach den Heften in bau/hefte/ (Aufruf-
            zeilen des Berichts), übrige Einträge nach Leitidee
  gebaut    ja/nein; pdf (Pfad im Repo, wenn gebaut)
"""

import argparse
import csv
import html
import importlib.util
import json
import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
ZIEL = WURZEL / "bau" / "regal"
RAW = "https://raw.githubusercontent.com/hz-0801/aufgabenbank/main/"

spec = importlib.util.spec_from_file_location(
    "zusammenbau", WURZEL / "werkzeuge" / "zusammenbau.py")
ZB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ZB)

HEFT_GRUPPE = {
    "msa-funktionen": ("MSA", "Funktionen"),
    "msa-geometrie": ("MSA", "Geometrie"),
    "msa-daten": ("MSA", "Daten"),
    "msa-zahlen": ("MSA", "Zahlen"),
    "abi-gk-analysis-1": ("Abitur GK", "Analysis I"),
    "abi-gk-analysis-2": ("Abitur GK", "Analysis II"),
    "abi-gk-stochastik": ("Abitur GK", "Stochastik"),
    "abi-gk-geometrie": ("Abitur GK", "Geometrie"),
}
LEITIDEE_GRUPPE = {
    "Zahlen und Operationen": ("MSA", "Zahlen"),
    "Größen und Messen": ("MSA", "Geometrie"),
    "Raum und Form": ("MSA", "Geometrie"),
    "Gleichungen und Funktionen": ("MSA", "Funktionen"),
    "Daten und Zufall": ("MSA", "Daten"),
    "Analysis": ("Abitur GK", "Analysis II"),
    "Stochastik": ("Abitur GK", "Stochastik"),
    "Analytische Geometrie": ("Abitur GK", "Geometrie"),
}
KOPF = ["kennung", "bereich", "thema", "eintrag", "einheit", "kette",
        "einheit_bank", "ich_kann", "klasse_os", "klasse_gym", "pruefung",
        "gruppe", "gebaut", "pdf"]


def katalog_index(pfad):
    """{eintrag: (bereich, leitidee)} aus katalog/index.md."""
    aus, bereich = {}, None
    if not pfad or not pfad.exists():
        return aus
    for z in pfad.read_text(encoding="utf-8").splitlines():
        if z.startswith("## Sekundarstufe II"):
            bereich = "Sek II"
        elif z.startswith("## Sekundarstufe I"):
            bereich = "Sek I"
        elif z.startswith("## "):
            bereich = None
        m = re.match(r"^\| ([a-z0-9-]+)\.md \| [^|]* \| ([^|]*) \|", z)
        if m and bereich and m.group(1) not in aus:
            leit = re.sub(r"\s*\(.*$", "", m.group(2)).strip()
            aus[m.group(1)] = (bereich, leit)
    return aus


def hefte():
    """{eintrag: (prüfung, gruppe)} aus den Aufrufzeilen von
    bau/hefte/bericht.md (ohne die Basis-Hefte)."""
    aus = {}
    b = WURZEL / "bau" / "hefte" / "bericht.md"
    if not b.exists():
        return aus
    name = None
    for z in b.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### (\S+) \(", z)
        if m:
            name = m.group(1)
        m = re.match(r"^Aufruf: `zusammenbau\.py (.+?) --heft", z)
        if m and name in HEFT_GRUPPE:
            for e in m.group(1).split():
                aus.setdefault(e, HEFT_GRUPPE[name])
    return aus


def marken_klassen(marken):
    """(klasse_os, klasse_gym) aus der Marken-Zeile."""
    if not marken:
        return "", ""
    os_, gym, _ = ZB.marke_zerlegen(marken)
    def txt(v):
        if not v:
            return ""
        return f"{v[0]}" if v[0] == v[1] else f"{v[0]}–{v[1]}"
    ko, kg = txt(os_), txt(gym)
    if not ko and not kg:
        m = re.search(r"\bBE (Q\d)", marken) or re.search(r"\b(Q\d)", marken)
        if m:
            kg = m.group(1)
    return ko, kg


def kurztitel(t):
    """Titel der Lerneinheit ohne Erläuterung (Sek-II-Mappen tragen nach
    dem Titel oft „: …“ oder „(…)“)."""
    t = re.split(r": | \(|; ", t, 1)[0].strip()
    return t if len(t) <= 70 else t[:68].rsplit(" ", 1)[0] + " …"


def pruefwort(zeilen, log):
    profile = []
    for z in zeilen:
        p = ZB.profil_von(z)
        if p and p not in profile:
            profile.append(p)
    reihenfolge = ["msa", "abitur-gk", "abitur-lk", "fhr"]
    marke = {"msa": "P10", "abitur-gk": "Abitur GK", "abitur-lk": "Abitur LK",
             "fhr": "FHR"}
    teile = []
    for p in sorted(profile, key=reihenfolge.index):
        w = ZB.pruefwort_zahl(marke[p], [z for z in zeilen
                                         if ZB.profil_von(z) == p], log)
        if w:
            teile.append(w)
    return " · ".join(teile)


def register_k():
    """{(eintrag, kette casefold, einheit): (kennung, pfad)} aus
    bau/register.csv, Rezept K."""
    aus = {}
    for z in ZB.lies_register():
        if z.get("rezept") != "K":
            continue
        b = dict(x.split("=", 1) for x in z["bestellung"].split(", ")
                 if "=" in x)
        aus[(z["eintraege"], b.get("kompetenz", "").casefold(),
             int(b.get("einheiten") or 0))] = (z["kennung"], z["pfad"])
    return aus


def plane(args):
    log = ZB.Log()
    kliste = ZB.finde_kuerzelliste(args.kuerzel)
    katalog = Path(args.katalog) if args.katalog else (
        kliste.parent if kliste else None)
    index = katalog_index(katalog / "index.md" if katalog else None)
    heft = hefte()
    ik = ZB.lies_ichkann()
    gebaut = register_k()
    zeilen_aus, fehlt = [], []
    for ordner in sorted(p for p in (WURZEL / "bank").iterdir()
                         if p.is_dir() and not p.name.startswith("_")):
        e = ordner.name
        dateien = sorted([p for p in ordner.glob("e*.jsonl")
                          if re.fullmatch(r"e\d+", p.stem)],
                         key=lambda p: int(p.stem[1:]))
        if not dateien:
            continue
        mappe = ZB.Mappe(WURZEL / "mappen" / f"{e}.md", log)
        kuerzel, _ = ZB.kuerzel_von(e, kliste)
        bereich, leit = index.get(e, ("", ""))
        plan = []
        for p in dateien:
            n = int(p.stem[1:])
            rows = ZB.lies_jsonl(p)
            gruppen = {}
            for z in rows:
                gruppen.setdefault(z["kette"], []).append(z)
            reihe = sorted(gruppen.items(),
                           key=lambda kv: min(z["kette_nr"] for z in kv[1]))
            ohne = []
            for name, zz in reihe:
                h = {z["hoehe"] for z in zz}
                if "grundfall" in h:
                    plan.append((n, name, zz))
                elif h - {"pflicht", "vorstufe"}:
                    ohne.append((name, zz))
            if ohne:
                plan.append((n, "*", [z for _, zz in ohne for z in zz],
                             [name for name, _ in ohne]))
        belegt = {int(k.split("-K")[1]) for (ee, _, _), (k, _) in gebaut.items()
                  if ee == e}
        nummer = 0
        for eintrag_plan in plan:
            n, name, zz = eintrag_plan[:3]
            namen = eintrag_plan[3] if len(eintrag_plan) > 3 else None
            treffer = gebaut.get((e, name.casefold(), n))
            if treffer:
                kennung, pfad = treffer
                pdf = f"{pfad}/{kennung}.pdf"
                ist = "ja" if (WURZEL / pdf).exists() else "nein"
            else:
                nummer += 1
                while nummer in belegt:
                    nummer += 1
                kennung, pdf, ist = f"{kuerzel}-K{nummer}", "", "nein"
            m, _ = ZB.mappe_einheit(mappe, name if name != "*" else
                                    (namen[0] if namen else ""), zz, n)
            info = mappe.einheiten.get(m) or {}
            ko, kg = marken_klassen(info.get("marken"))
            titel = ik.get((e, n, name.casefold(), ""), ("", ""))[0]
            if not titel:
                titel = f"Ich kann: {name}."
                fehlt.append(f"{e} e{n} {name}")
            b = bereich or "Sek I"
            if "Sek II" in name:
                b = "Sek II"
            grp = heft.get(e) or LEITIDEE_GRUPPE.get(leit, ("", ""))
            zeilen_aus.append({
                "kennung": kennung, "bereich": b, "thema": leit,
                "eintrag": e,
                "einheit": f"{m} {kurztitel(info.get('titel', ''))}".strip(),
                "kette": name if name != "*" else "*",
                "einheit_bank": n, "ich_kann": titel,
                "klasse_os": ko, "klasse_gym": kg,
                "pruefung": pruefwort(zz, log),
                "gruppe": f"{grp[0]}: {grp[1]}" if grp[0] else "",
                "gebaut": ist, "pdf": pdf if ist == "ja" else "",
                "_typen": namen or [], "_thema_titel": mappe.thema or e})
    return zeilen_aus, fehlt


def schreibe_csv(zeilen):
    ZIEL.mkdir(parents=True, exist_ok=True)
    with open(ZIEL / "regal.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOPF, delimiter=";",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for z in zeilen:
            w.writerow(z)


HTML = r"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Regal der Kompetenzblätter</title>
<style>
:root{--bg:#fbfaf7;--fg:#1f2328;--mute:#6b7076;--line:#dcd8cf;--acc:#2f5d8a;--ok:#2e7d4f;--chip:#efece5}
@media (prefers-color-scheme: dark){:root{--bg:#17191c;--fg:#e6e3dc;--mute:#9aa0a6;--line:#33373c;--acc:#8ab4e0;--ok:#7fcf9c;--chip:#23262a}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 16px;z-index:2}
h1{font-size:19px;margin:0 0 8px}
.leiste{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.leiste button{border:1px solid var(--line);background:var(--chip);color:var(--fg);padding:6px 12px;border-radius:16px;cursor:pointer;font:inherit}
.leiste button[aria-pressed=true]{background:var(--acc);color:var(--bg);border-color:var(--acc)}
input[type=search]{flex:1 1 220px;min-width:0;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--fg);font:inherit}
label{color:var(--mute);white-space:nowrap}
main{padding:8px 16px 40px;max-width:1100px;margin:0 auto}
h2{font-size:17px;margin:22px 0 4px}
h3{font-size:15px;margin:14px 0 2px;color:var(--mute);font-weight:600}
.zeile{display:grid;grid-template-columns:6.5em 1fr auto auto;gap:4px 12px;padding:6px 0;border-bottom:1px solid var(--line);align-items:baseline}
.k{font-family:ui-monospace,Consolas,monospace;font-size:13px;color:var(--mute)}
.gebaut .k{color:var(--ok);font-weight:600}
.t small{display:block;color:var(--mute)}
.p,.kl{font-size:13px;color:var(--mute);white-space:nowrap}
a{color:var(--acc)}
.zahl{color:var(--mute);font-size:13px;margin-left:6px;font-weight:400}
.leer{color:var(--mute);padding:20px 0}
@media (max-width:640px){.zeile{grid-template-columns:5.6em 1fr}.p,.kl{grid-column:2}}
</style>
</head>
<body>
<header>
<h1>Regal der Kompetenzblätter <span class="zahl" id="stand"></span></h1>
<div class="leiste">
<button id="v1" aria-pressed="true">nach Prüfung</button>
<button id="v2" aria-pressed="false">nach Klasse und Thema</button>
<input type="search" id="suche" placeholder="Suchen: Titel, Kennung, Thema …">
<label><input type="checkbox" id="nurgebaut"> nur gebaute</label>
</div>
</header>
<main id="inhalt"></main>
<script>
const DATEN = __DATEN__;
const RAW = "__RAW__";
const GRUPPEN = ["MSA: Funktionen","MSA: Geometrie","MSA: Daten","MSA: Zahlen",
  "Abitur GK: Analysis I","Abitur GK: Analysis II","Abitur GK: Stochastik","Abitur GK: Geometrie"];
let ansicht = 1;
const $ = s => document.querySelector(s);
function blaetter(n){return n+(n===1?" Blatt":" Blätter")}
function zahl(p){const m=(p||"").match(/×(\d+)/);return m?parseInt(m[1]):0}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
function klasse(z){if(z.bereich==="Sek II"||(!z.klasse_os&&/^Q/.test(z.klasse_gym)))return z.klasse_gym?("Sek II · "+z.klasse_gym):"Sek II";
  const v=(z.klasse_os||z.klasse_gym||"").split("–")[0];return v?("Klasse "+v.padStart(2,"0")):"ohne Klasse"}
function kltext(z){const a=[];if(z.klasse_os)a.push("OS "+z.klasse_os);if(z.klasse_gym)a.push((/^Q/.test(z.klasse_gym)?"":"GYM ")+z.klasse_gym);return a.join(" · ")}
function zeile(z){const link=z.pdf?` <a href="${RAW+z.pdf}" target="_blank" rel="noopener">PDF</a>`:"";
  const sub=z.kette==="*"?"Typen ohne Kette · "+esc(z.eintrag)+" · Einheit "+esc(z.einheit):esc(z.eintrag)+" · "+esc(z.einheit);
  return `<div class="zeile${z.gebaut==="ja"?" gebaut":""}"><span class="k">${esc(z.kennung)}</span>`+
  `<span class="t">${esc(z.ich_kann)}${link}<small>${sub}</small></span>`+
  `<span class="kl">${esc(kltext(z))}</span><span class="p">${esc(z.pruefung||"keine Prüfungsaufgabe")}</span></div>`}
function passt(z){const q=$("#suche").value.trim().toLowerCase();
  if($("#nurgebaut").checked&&z.gebaut!=="ja")return false;
  if(!q)return true;return [z.kennung,z.ich_kann,z.thema,z.eintrag,z.einheit,z.kette,z.pruefung].join(" ").toLowerCase().includes(q)}
function zeichne(){const d=DATEN.filter(passt);let h="";
  if(!d.length){$("#inhalt").innerHTML='<p class="leer">Keine Blätter.</p>';return}
  if(ansicht===1){const gr=[...GRUPPEN,...new Set(d.map(z=>z.gruppe||"ohne Prüfungsbereich").filter(g=>!GRUPPEN.includes(g)))];
    let vor="";
    for(const g of gr){const zz=d.filter(z=>(z.gruppe||"ohne Prüfungsbereich")===g).sort((a,b)=>zahl(b.pruefung)-zahl(a.pruefung)||a.eintrag.localeCompare(b.eintrag)||a.einheit_bank-b.einheit_bank);
      if(!zz.length)continue;const p=g.split(": ")[0];
      if(p!==vor){h+=`<h2>${esc(p)}</h2>`;vor=p}
      h+=`<h3>${esc(g.split(": ")[1]||g)}<span class="zahl">${blaetter(zz.length)}</span></h3>`+zz.map(zeile).join("")}}
  else{const kl=[...new Set(d.map(klasse))].sort();
    for(const k of kl){const zk=d.filter(z=>klasse(z)===k);h+=`<h2>${esc(k.replace(/Klasse 0?/,"Klasse "))}<span class="zahl">${blaetter(zk.length)}</span></h2>`;
      const es=[...new Set(zk.map(z=>z.eintrag))].sort((a,b)=>{const ta=zk.find(z=>z.eintrag===a).thema_titel,tb=zk.find(z=>z.eintrag===b).thema_titel;return ta.localeCompare(tb)});
      for(const e of es){const ze=zk.filter(z=>z.eintrag===e).sort((a,b)=>a.einheit_bank-b.einheit_bank);
        h+=`<h3>${esc(ze[0].thema_titel)} <span class="zahl">${esc(ze[0].thema)}</span></h3>`+ze.map(zeile).join("")}}}
  $("#inhalt").innerHTML=h}
$("#v1").onclick=()=>{ansicht=1;$("#v1").setAttribute("aria-pressed","true");$("#v2").setAttribute("aria-pressed","false");zeichne()};
$("#v2").onclick=()=>{ansicht=2;$("#v2").setAttribute("aria-pressed","true");$("#v1").setAttribute("aria-pressed","false");zeichne()};
$("#suche").oninput=zeichne;$("#nurgebaut").onchange=zeichne;
$("#stand").textContent=DATEN.length+" geplant, "+DATEN.filter(z=>z.gebaut==="ja").length+" gebaut";
zeichne();
</script>
</body>
</html>
"""


def schreibe_html(zeilen):
    daten = [{k: z[k] for k in KOPF} | {"thema_titel": z["_thema_titel"]}
             for z in zeilen]
    text = HTML.replace("__DATEN__", json.dumps(daten, ensure_ascii=False)
                        .replace("</", "<\\/")).replace("__RAW__", RAW)
    (ZIEL / "regal.html").write_text(text, encoding="utf-8", newline="\n")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--kuerzel", help="Pfad zu katalog/_kuerzel.csv")
    p.add_argument("--katalog", help="Ordner katalog/ von mathe-nachhilfe")
    args = p.parse_args(argv)
    zeilen, fehlt = plane(args)
    schreibe_csv(zeilen)
    schreibe_html(zeilen)
    n_v = sum(1 for z in zeilen if z["kette"] != "*")
    print(f"{len(zeilen)} Kompetenzblätter geplant ({n_v} Verfahrensketten, "
          f"{len(zeilen) - n_v} Einheiten mit Typen ohne Kette), "
          f"{sum(1 for z in zeilen if z['gebaut'] == 'ja')} gebaut")
    for f in fehlt:
        print(f"ICH-KANN fehlt: {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

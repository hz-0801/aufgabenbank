# Rendern in der Web-Sitzung

Stand 2026-09-27. Ergebnis der Render-Probe (bau/render-probe/):
**Die Web-Sandbox kann LaTeX kompilieren – über apt-get (Versuch 4).**
Die Annahme „kein LaTeX im Web“ gilt nicht mehr.

## Kurzanleitung

Das Paket ist nach Sitzungsende weg (Container wird neu aufgesetzt).
Je Sitzung einmal, etwa 3–5 Minuten:

    apt-get update
    apt-get install -y --no-install-recommends texlive-xetex \
        texlive-fonts-recommended texlive-lang-german texlive-pictures \
        texlive-latex-extra lmodern fonts-lmodern

Danach wie in werkzeuge/zusammenbau.md: `xelatex gesamt.tex` zweimal.
Für Textkontrolle am PDF zusätzlich `poppler-utils` (pdftotext,
pdffonts); geht ebenso über apt.
`texlive-xetex` allein reicht nicht: hyperref braucht unter XeTeX die
Schrift pzdr aus texlive-fonts-recommended (Fehler siehe Versuch 4).

Dauerhaft ohne Handgriff je Sitzung: dieselben zwei Befehle ins
Setup-Skript der Umgebung (Claude-App, Cloud-Umgebung in der Titelleiste
der Sitzung → Bearbeiten → Setup-Skript); neue Sitzungen haben xelatex
dann von Anfang an. Das ist eine Einstellung, keine Datei im Repo.

Stand der installierten Pakete (Ubuntu 24.04 „noble“): TeX Live 2023
(texlive-base 2023.20240207-1), XeTeX 3.141592653-2.6-0.999995.

## Netz (gemessen, Proxy der Sitzung)

| Ziel | Ergebnis |
| --- | --- |
| archive.ubuntu.com (apt) | erreichbar |
| ppa.launchpadcontent.net | 403 (für TeX unerheblich) |
| pypi.org | erreichbar |
| github.com, Release-Downloads | erreichbar |
| api.github.com (ohne Anmeldung) | 403 |
| relay/data1.fullyjustified.net (Tectonic-Bundle) | 403 |
| mirror.ctan.org, ctan.org | 403 |
| yihui.org (TinyTeX) | 403 |
| deb.debian.org | 403 |

Folge: Alles, was TeX-Pakete zur Laufzeit von CTAN oder vom
Tectonic-Relay nachlädt (tlmgr, Tectonic, TinyTeX-Nachinstallation),
geht hier nicht. Was geht: Ubuntu-Pakete und Dateien aus
GitHub-Releases.

## Versuche (4 von 6 verbraucht)

### 1 – xelatex oder pdflatex vorhanden?

Befehl: `which xelatex pdflatex lualatex tectonic latexmk kpsewhich`,
`ls /usr/share/texlive /usr/share/texmf`

Ergebnis: nichts vorhanden.

    xelatex: fehlt
    pdflatex: fehlt
    lualatex: fehlt
    tectonic: fehlt
    latexmk: fehlt
    kpsewhich: fehlt
    ls: cannot access '/usr/share/texlive': No such file or directory
    ls: cannot access '/usr/share/texmf': No such file or directory

### 2 – pip-Paket ohne Systemrechte (pytinytex)

Befehl: `pip install pytinytex` (geht, 0.5.1), dann
`python3 -c "import pytinytex; pytinytex.download_tinytex(variation=1, target_folder='tinytex')"`

Ergebnis: gescheitert. pytinytex fragt die neueste Version über
api.github.com ab; der Proxy antwortet 403. Selbst mit direkter
Release-URL bliebe die Lücke: TinyTeX lädt fehlende Pakete (tikz,
pgfplots, tcolorbox …) per tlmgr von CTAN nach, und CTAN ist gesperrt.

    Traceback (most recent call last):
      File "/usr/local/lib/python3.11/dist-packages/pytinytex/tinytex_download.py", line 134, in _get_tinytex_urls
        response = urlopen(url)
                   ^^^^^^^^^^^^
      File "/usr/lib/python3.11/urllib/request.py", line 216, in urlopen
        return opener.open(url, data, timeout)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/usr/lib/python3.11/urllib/request.py", line 525, in open
        response = meth(req, response)
                   ^^^^^^^^^^^^^^^^^^^
    […]
    urllib.error.HTTPError: HTTP Error 403: Forbidden
    RuntimeError: Can't find TinyTeX version latest

### 3 – Tectonic als Binärdatei aus GitHub-Releases

Befehl:

    curl -sSL -o tect.tgz https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%400.15.0/tectonic-0.15.0-x86_64-unknown-linux-musl.tar.gz
    tar xzf tect.tgz && ./tectonic --version
    ./tectonic -X compile min.tex

Ergebnis: Download und Binärdatei gehen (`Tectonic 0.15.0`), das
Kompilieren nicht: Tectonic holt beim ersten Lauf sein TeX-Bundle von
relay.fullyjustified.net, der Proxy sperrt den Host. Bis zu
mathblatt.sty kam es nicht; schon ein Minimaldokument scheitert.

    note: "version 2" Tectonic command-line interface activated
    note: connecting to https://relay.fullyjustified.net/default_bundle_v33.tar
    error: error sending request for url (https://relay.fullyjustified.net/default_bundle_v33.tar): error trying to connect: unsuccessful tunnel
    caused by: error trying to connect: unsuccessful tunnel
    caused by: unsuccessful tunnel

Handgriff-Weg (nicht nötig, da Versuch 4 ging; nicht geprüft):
Tectonic nimmt mit `--bundle` auch ein lokales Bundle. Legte der Lehrer
das Bundle (mehrere hundert MB) als GitHub-Release-Anhang ab, ginge der
Weg ohne apt. Wegen der Größe schlechter als Versuch 4.

### 4 – apt-get texlive-xetex

Befehl: `apt-get update`, dann
`apt-get install -y --no-install-recommends texlive-xetex`
(Sitzung läuft als root, Rechte da).

Ergebnis: Installation geht; apt-get update meldet nur 403 für zwei
PPAs (deadsnakes, ondrej/php), das Ubuntu-Archiv ist erreichbar.

    Setting up texlive-latex-extra (2023.20240207-1) ...
    Setting up texlive-xetex (2023.20240207-1) ...
    Processing triggers for tex-common (6.18) ...
    Running updmap-sys. This may take some time... done.
    Running mktexlsr /var/lib/texmf ... done.
    Building format(s) --all.
    	This may take some time... done.

Erster Lauf mit mathblatt.sty (Lernblatt Prozentrechnung) brach ab:

    ! Font \XeTeXLink@font=pzdr at 0.00002pt not loadable: Metric (TFM) file or installed font not found.
    <to be read again>
                       \relax
    l.4908   \font\XeTeXLink@font=pzdr at 1sp\relax

Nachinstalliert: texlive-fonts-recommended texlive-lang-german
texlive-pictures texlive-latex-extra lmodern fonts-lmodern. Danach
laufen alle Blätter fehlerfrei (siehe bau/render-probe/befunde.md).

Probe insgesamt: 105 Kompilierläufe (Grenze 300) – 16 Lernblatt und
Einrichtung, 83 Bausteinprobe (bau/render-probe/probe.py), 6 Gegenprobe.
Laufzeit je Lauf wenige Sekunden; die ganze Bausteinprobe etwa 10 Minuten.

mathblatt.sty: Kopie in bau/prozentrechnung/2026-09-27/lernblatt/ ist
byte-gleich mit hz-0801/blattbau@36b7b12.

import csv, sys, io
KOPF = 'id;marke;quelle;kapitel;einheit;stufe;art;eltern_id;auf_blatt;wortlaut;abbildung;loesung;pruef;zahlart;schwere;rang;bemerkung;grafik;form;buendel;wortlaut_einheit;loesung_einheit;pruef_einheit;grafik_einheit;form_einheit'.split(';')
NZ = 'nachgerechnet (sympy, src/rechne.py)'

def bb(eid):
    # 2024-bebb-gk-A1.9a -> (GK ’24, Abi GK 2024 · A1.9a)
    j, rest = eid[:4], eid.split('-gk-')[1]
    return f'GK ’{j[2:]}', f'Abi GK {j} · {rest}'

def iqb(eid, stelle):
    j = eid[:4]
    return f'IQB ’{j[2:]}', f'IQB GK {j} · {stelle}'

def zeile(kap, einheit, stufe, eid, wortlaut, loesung, zahlart, schwere, rang, bem, grafik='', form='', *,
          iqb_stelle=None, nach=False, nr=1, auf=None, **ein):
    if iqb_stelle:
        marke, quelle = iqb(eid, iqb_stelle)
        rid = f'{eid[:4]}-iqb-ga-{iqb_stelle}-m{nr}'
        bem = 'IQB-Pool, nicht BB; ' + bem
    else:
        marke, quelle = bb(eid)
        rid = f'{eid}-m{nr}'
    if nach:
        marke = 'nach ' + marke
    if auf is None:
        auf = 'ja' if (not iqb_stelle and int(eid[:4]) >= 2022) else 'nein'
    r = dict.fromkeys(KOPF, '')
    r.update(id=rid, marke=marke, quelle=quelle, kapitel=kap, einheit=einheit, stufe=stufe, art='mehr',
             eltern_id=eid, auf_blatt=auf, wortlaut=wortlaut, loesung=loesung, zahlart=zahlart, schwere=schwere,
             rang=str(rang), bemerkung=bem + '; ' + NZ, grafik=grafik, form=form)
    for f in ('loesung', 'wortlaut'):
        r[f] = r[f].replace(' ∩ ', ' $\\cap$ ').replace('x₄', '$x_4$')
    for k, v in ein.items():
        r[k] = v
    return r

def schreibe(pfad, zeilen):
    with open(pfad, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=KOPF, delimiter=';', lineterminator='\n')
        w.writeheader()
        for r in zeilen:
            w.writerow(r)

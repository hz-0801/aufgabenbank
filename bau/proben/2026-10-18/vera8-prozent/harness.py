import importlib.util, json, sys, collections
from pathlib import Path
spec=importlib.util.spec_from_file_location('bp','/home/claude/aufgabenbank/werkzeuge/bank-pruef.py')
bp=importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
wurzel=Path('/home/claude/aufgabenbank')
ctx,wg=bp.kontext('prozentrechnung',wurzel)
print('Kontext-Warnungen:',wg)
n=0;bad=0;cnt=collections.Counter()
for l in open('/home/claude/aufgabenbank/bau/proben/2026-10-18/vera8-prozent/prozentrechnung.jsonl',encoding='utf8'):
    a=json.loads(l)
    assert isinstance(a['fallen'],list) and a['stufe'] and a['herkunft']
    b=dict(a); b.pop('fallen'); b.pop('stufe')
    key=(a['einheit'],a['kette_nr'],a['sprosse']); cnt[key]+=1
    b['variante']=cnt[key]
    b['id']=f"prozentrechnung-e{a['einheit']}-k{a['kette_nr']}-s{a['sprosse']}-v{cnt[key]}"
    bf,w=bp.pruefe_zeile(b,'prozentrechnung',a['einheit'],ctx)
    n+=1
    if bf or w: bad+=1; print(a['id'],'|',bf,w)
print(n,'Zeilen,',bad,'mit Befund')

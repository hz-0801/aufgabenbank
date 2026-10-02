import json, copy
B='aufgabenbank/bank/quadratische-gleichungen/'
Z='pruefbaum/bank/quadratische-gleichungen/'
neu=[json.loads(l) for l in open('neu-quadratische-gleichungen-duden9.jsonl')]
def grp(lbl): return [r for r in neu if r['sprosse']==lbl]
# (datei, kette_nr, nach_sprosse_alt, gruppe, label)
plan={
 'e1':[(2,10,grp('NEU-quadrat-erkennen')),(2,13,grp('NEU-umkehrung-rein'))],
 'e2':[(1,9,grp('NEU-umkehrung-produkt'))],
 'e3':[(3,4,[r for r in neu if r['einheit']==3 and r['sprosse']==4]),
       (3,7,[r for r in neu if r['einheit']==3 and r['sprosse']==8]),
       (3,8,grp('NEU-parameter')),
       (3,10,grp('NEU-vieta')),
       (3,11,[r for r in neu if r['einheit']==3 and r['sprosse']==11])],
}
for d in ('zone','e4'):
    open(Z+d+'.jsonl','w').write(open(B+d+'.jsonl').read())
for d in ('e1','e2','e3'):
    alt=[json.loads(l) for l in open(B+d+'.jsonl')]
    for r in alt: r['_g']=('alt',r['kette_nr'],r['sprosse'])
    out=[]
    for i,r in enumerate(alt):
        out.append(r)
        nxt=alt[i+1] if i+1<len(alt) else None
        for k,s,g in plan.get(d,[]):
            if r['kette_nr']==k and r['sprosse']==s and not (nxt and nxt['kette_nr']==k and nxt['sprosse']==s):
                for n in g:
                    n=copy.deepcopy(n)
                    same = isinstance(n['sprosse'],int) and n['sprosse']==s and n['sprosse']!=8
                    n['_g']=('alt',k,s) if same else ('neu',k,str(n['sprosse']))
                    out.append(n)
        if d=='e3' and r['kette_nr']==4 and nxt and nxt['kette_nr']==5:
            for n in [x for x in neu if x['kette']=='NEU-grafisch']:
                n=copy.deepcopy(n); n['_g']=('neu',5,'g'); out.append(n)
    # kette_nr verschieben (e3: alte k5 -> k6)
    for r in out:
        if d=='e3' and r['_g'][0]=='alt' and r['kette_nr']==5: r['kette_nr']=6
        if r['kette']=='NEU-grafisch': r['kette_nr']=5
    # Sprossen je Kette neu zählen
    last={}
    for r in out:
        k=r['kette_nr']
        if k not in last:
            start=r['sprosse'] if isinstance(r['sprosse'],int) else 1
            last[k]=[r['_g'],start]
        elif r['_g']!=last[k][0]:
            last[k]=[r['_g'],last[k][1]+1]
        r['sprosse']=last[k][1]
        s=r['sprosse']; ss=f"s{s}" if s>=0 else f"s{s}"
        r['id']=f"quadratische-gleichungen-{d}-k{k}-{ss}-v{r['variante']}"
        del r['_g']
    with open(Z+d+'.jsonl','w') as f:
        for r in out: f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print(d,len(alt),'->',len(out))

import json, re, glob, os, sys
K='mathe-nachhilfe/katalog'; B='aufgabenbank/bank'
def norm(s):
    s=re.sub(r'\((\d+)×\)','',s); s=re.sub(r'\s+',' ',s).strip(' .;:').lower()
    return s
res=[]; formatlos=[]
for f in sorted(glob.glob(K+'/*.md')):
    e=os.path.basename(f)[:-3]
    if e.startswith('_'): continue
    lines=open(f,encoding='utf-8').read().split('\n')
    steps=[]
    for l in lines:
        m=re.match(r'^- (.+?) \(Einheit (\d+)\)[^:]*:\s*(.+)$',l)
        if m and '→' in m.group(3):
            for s in m.group(3).split(' → '):
                steps.append((int(m.group(2)),m.group(1),s.strip()))
    if not steps: formatlos.append(e); continue
    bank=set()
    for j in glob.glob(f'{B}/{e}/*.jsonl'):
        for l in open(j,encoding='utf-8'):
            l=l.strip()
            if not l: continue
            try: bank.add(norm(json.loads(l).get('sprosse_text','')))
            except Exception: pass
    leer=[s for s in steps if not any(norm(s[2])==b or norm(s[2]) in b or (len(b)>15 and b in norm(s[2])) for b in bank)]
    res.append((e,len(steps),len(leer),leer))
tot=sum(r[1] for r in res); totl=sum(r[2] for r in res)
print(f'Einträge mit Sprossenketten: {len(res)}; Sprossen {tot}; ohne Bankzeile {totl}')
print('ohne erkennbares Kettenformat:', ', '.join(formatlos))
for e,n,l,_ in sorted(res,key=lambda r:-r[2]): print(f'{l:4d}/{n:3d}  {e}')
json.dump([(e,n,l,leer) for e,n,l,leer in res],open('leere_sprossen.json','w'),ensure_ascii=False,indent=1)

import argparse,json,re
from pathlib import Path
parser=argparse.ArgumentParser()
for n in ('action','id','name','description'): parser.add_argument('--'+n,default='')
a=parser.parse_args(); path=Path('data/site.json'); data=json.loads(path.read_text(encoding='utf-8')); genres=data.setdefault('genres',[])
item=next((g for g in genres if g['id']==a.id),None)
if a.action=='add':
    gid=a.id or re.sub(r'[^a-z0-9]+','-',a.name.lower()).strip('-')
    if any(g['id']==gid for g in genres): raise SystemExit('Genre ID already exists.')
    genres.append({'id':gid,'name':a.name,'description':a.description})
elif not item: raise SystemExit('Genre ID not found.')
elif a.action=='delete':
    old=item['name']; genres.remove(item)
    for v in data.get('videos',[]):
        if v.get('genre')==old:v['genre']=''
elif a.action=='update':
    old=item['name']; item['name']=a.name or item['name']; item['description']=a.description or item.get('description','')
    for v in data.get('videos',[]):
        if v.get('genre')==old:v['genre']=item['name']
else: raise SystemExit('Choose an action.')
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

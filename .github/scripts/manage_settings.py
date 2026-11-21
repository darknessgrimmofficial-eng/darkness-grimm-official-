import argparse, json
from pathlib import Path
parser=argparse.ArgumentParser(); parser.add_argument('--field',required=True); parser.add_argument('--value',required=True); args=parser.parse_args()
path=Path('data/site.json'); data=json.loads(path.read_text(encoding='utf-8'))
if args.field.startswith('social.'):
    data.setdefault('socials',{})[args.field.split('.',1)[1]]=args.value.strip()
else: data.setdefault('site',{})[args.field]=args.value
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

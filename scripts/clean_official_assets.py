from pathlib import Path
import json,subprocess,hashlib
ROOT=Path(__file__).resolve().parent.parent
runner=['/Users/rj/.local/share/watermarks-remover/.venv/bin/python','/Users/rj/.local/share/publication-clean/publication_clean.py']
figs=json.loads((ROOT/'course/official-figures.json').read_text());out=ROOT/'assets/cleaned';out.mkdir(exist_ok=True)
reports=[]
for f in figs:
 original=(ROOT/'course'/f['path']).resolve();target=out/original.name
 if not target.exists():
  result=subprocess.run(runner+['clean',str(original),'-o',str(target)],capture_output=True,text=True)
  if result.returncode:raise RuntimeError(result.stderr or result.stdout)
 f['originalPath']=f['path'];f['path']='../assets/cleaned/'+target.name
 reports.append(dict(id=f['id'],original=str(original.relative_to(ROOT)),cleaned=str(target.relative_to(ROOT)),audit=str(target.relative_to(ROOT))+'.audit.json',sourceUrl=f['sourceUrl']))
(ROOT/'course/official-figures.json').write_text(json.dumps(figs,indent=2))
(ROOT/'audits/asset-cleanup-manifest.json').write_text(json.dumps(reports,indent=2))
print('Cleaned source copies:',len(reports))

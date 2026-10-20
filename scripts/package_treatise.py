from pathlib import Path
import json,re,base64
ROOT=Path(__file__).resolve().parent.parent
out=ROOT/'output';out.mkdir(exist_ok=True)
course=json.loads((ROOT/'course/course-data.json').read_text())
def dataurl(path):
 path=Path(path);typ={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml','.ttf':'font/ttf','.woff2':'font/woff2'}.get(path.suffix,'application/octet-stream')
 return 'data:'+typ+';base64,'+base64.b64encode(path.read_bytes()).decode()
def embed_paths(text,base):
 def sub(m):
  val=m.group(1).strip('"\'');p=(base/val).resolve()
  return 'url("'+dataurl(p)+'")' if p.exists() and p.is_file() else m.group(0)
 return re.sub(r'url\(([^)]+)\)',sub,text)
def escape_script(text):return text.replace('</','<\\/')
for f in course['figures']:
 p=(ROOT/'course'/f['path']).resolve();f['path']=dataurl(p)
for s in course['core']:
 if s.get('image'):
  p=(ROOT/'course'/s['image']).resolve()
  if p.exists():s['image']=dataurl(p)
# Preserve access to original evidence through public repository links.
origin='https://github.com/jrajath94/aws-aip-c01-study-guide/blob/823006efa64f98b560dd4fe40445e6a8042ef79b/'
for ref in course['references']:
 ref['html']=ref['html'].replace('../source-repo/',origin);ref['source']=ref['source'].replace('../source-repo/',origin)
for q in course['quizzes']:q['source']=q['source'].replace('../source-repo/',origin)
for src in course['sources'].values():src['url']=src['url'].replace('../source-repo/',origin)
css=embed_paths((ROOT/'course/treatise.css').read_text(),ROOT/'course')
reader_css=embed_paths((ROOT/'course/reader.css').read_text(),ROOT/'course')
reader=(ROOT/'course/reader.html').read_text().replace('<link rel="stylesheet" href="reader.css">','<style>'+reader_css+'</style>')
reader=reader.replace('<script src="course-data.js"></script>','<script>window.COURSE=parent.COURSE;</script>')
reader_js=(ROOT/'course/reader.js').read_text().replace("history.replaceState(null,'','#'+mode+'/'+encodeURIComponent(id));","try{history.replaceState(null,'','#'+mode+'/'+encodeURIComponent(id));}catch{}")
reader=reader.replace('<script src="reader.js"></script>','<script>'+escape_script(reader_js)+'</script>')
html=(ROOT/'course/treatise.html').read_text().replace('<link rel="stylesheet" href="treatise.css">','<style>'+css+'</style>')
html=html.replace('<script src="course-data.js"></script>','<script>window.COURSE='+escape_script(json.dumps(course,ensure_ascii=False,separators=(',',':')))+';</script>')
html=html.replace('<script src="treatise.js"></script>','<script>'+escape_script((ROOT/'course/treatise.js').read_text())+'</script>')
bridge='''
<script>
(() => {
 const readerDocument=READER_DOCUMENT;
 const overlay=document.createElement('dialog');overlay.id='study-reader';overlay.innerHTML='<button id="close-reader">Return to treatise</button><iframe title="Course and practice reader"></iframe>';document.body.append(overlay);
 document.getElementById('close-reader').onclick=()=>overlay.close();
 document.body.addEventListener('click',event=>{const a=event.target.closest('a');if(!a)return;const href=a.getAttribute('href')||'';if(!href.startsWith('reader.html'))return;event.preventDefault();
 const [mode,id]=href.split('#')[1]?.split('/')||['core',''];const frame=overlay.querySelector('iframe');
 frame.onload=()=>{const w=frame.contentWindow;let target=id;if(!target){const c=window.COURSE;target=mode==='mock'?c.mock[0]:mode==='quizzes'?c.quizzes[0].id:mode==='references'?c.references[0].id:mode==='skills'?c.skills[0].id:mode==='services'?c.services[0].id:mode==='recalls'?c.recalls[0].id:c.core[0].id;}w.COURSE_APP.go(decodeURIComponent(target),mode||'core');};
 frame.srcdoc=readerDocument;overlay.showModal();
 });
})();
</script>
<style>#study-reader{width:98vw;height:96vh;max-width:98vw;max-height:96vh;padding:10px;border:1px solid #ccd4e2}#study-reader iframe{display:block;width:100%;height:calc(100% - 48px);border:0}#close-reader{margin:0 0 10px}</style>
'''.replace('READER_DOCUMENT',json.dumps(reader,ensure_ascii=False).replace('<','\\u003c'))
html=html.replace('</body>',bridge+'</body>')
p=out/'AIP-C01-Visual-Treatise.original.html';p.write_text(html)
print('Packed',p,len(html),'characters')

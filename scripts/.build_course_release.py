from pathlib import Path
from bs4 import BeautifulSoup,Tag,Comment
from html import escape
import json,re,hashlib,collections
ROOT=Path(__file__).resolve().parent.parent
read=lambda name:json.loads((ROOT/name).read_text())
core=read('course/core.json'); advanced=read('course/advanced.json'); additions=read('course/review-additions.json') if (ROOT/'course/review-additions.json').exists() else [];
for entry in additions:
 if isinstance(entry['points'],str): entry['points']=re.split(r'(?<=[.!?])\s+',entry['points'])
core=core[:-1]+advanced+additions+core[-1:]; corrections=read('course/corrections.json'); sources={}
for f in ['research/manifest.json','research/service-manifest.json','research/extra-manifest.json','research/corrected-manifest.json']:
 if not (ROOT/f).exists():continue
 for s in read(f):
  if 'error' in s:continue
  key=s.get('id') or ('domain'+re.search(r'domain(\d)',s['path'])[1] if re.search(r'domain(\d)',s['path']) else 'exam' if s['path'].endswith('/ai-professional-01.md') else Path(s['path']).stem)
  sources[key]=s
# MCP snapshots are the primary source channel for the revised treatise.
for callfile in (ROOT/'research').glob('*calls.json'):
 for call in json.loads(callfile.read_text()):
  if call.get('tool')!='read_documentation':continue
  mp=ROOT/'research/mcp'/(call['id']+'.md')
  if not mp.exists():continue
  text=mp.read_text()
  if not text.startswith('AWS Documentation from'):continue
  sources[call['id']]={'url':call['arguments']['url'],'path':str(mp.relative_to(ROOT)),'channel':'official AWS Documentation MCP','retrieved':'2026-10-20'}
# Preserve citations to official documentation search snapshots. These records
# identify the first returned AWS documentation page, not a full-page capture.
for sp in sorted((ROOT/'research/mcp').glob('search-*.json')):
 try:
  snapshot=json.loads(sp.read_text())
  results=snapshot.get('structured_content',{}).get('search_results',[])
  if results and results[0].get('url','').startswith('https://docs.aws.amazon.com/'):
   sources[sp.stem]={'url':results[0]['url'],'path':str(sp.relative_to(ROOT)),'channel':'official AWS Documentation MCP search snapshot','retrieved':'2026-10-20'}
 except (json.JSONDecodeError,AttributeError):
  continue
for d in range(1,6):
 if 'exam-domain-'+str(d) in sources:sources['domain'+str(d)]=sources['exam-domain-'+str(d)]
if 'scope-ai-professional-01' in sources:sources['exam']=sources['scope-ai-professional-01']
sources['certification']={'url':'https://aws.amazon.com/certification/certified-generative-ai-developer-professional/','path':'research/certification.md'}
sources['strands']={'url':'https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-bedrock.html','path':'research/mcp/visual-doc-017.md','channel':'official AWS Documentation MCP'}
sources['repo-d1']={'url':'../source-repo/volume-d1-foundation-models.html','path':'source-repo/volume-d1-foundation-models.html'}
# Every official skill maps to explicit authored teaching.
skills=[]
for d in range(1,6):
 text=(ROOT/f'research/ai-professional-01-domain{d}.md').read_text()
 for sid,desc in re.findall(r'Skill (\d\.\d\.\d+): ([^\n]+)',text):
  owners=[s['id'] for s in core if sid in s['skills']]
  if not owners:raise ValueError('Unmapped skill '+sid)
  skills.append(dict(id=sid,description=desc,slides=owners,domain=d))
# Authoritative corrections appear next to inherited source claims.
def correction_ids(text):return [c['id'] for c in corrections if re.search(c['match'],text,re.I)]
def clean_html(raw,filename):
 s=BeautifulSoup(raw,'html.parser')
 for el in list(s.find_all(['script','style','iframe','button','nav'])):el.decompose()
 for el in s.find_all(True):
  for attr in list(el.attrs):
   if attr not in ['href','src','alt','colspan','rowspan','open']:del el[attr]
 for im in s.find_all('img'):
  src=im.get('src',''); alt=im.get('alt','Source figure')
  a=s.new_tag('a',href='../source-repo/'+src);a.string='Source figure: '+alt;im.replace_with(a)
 for a in s.find_all('a'):
  h=a.get('href','')
  if h.startswith('#'):a['href']='../source-repo/'+filename+h
  elif h and not re.match(r'https?://|\.\./source-repo/',h):a['href']='../source-repo/'+h
  a['target']='_blank';a['rel']='noopener'
 return str(s)
references=[];quizzes=[];recalls=[];inventory=[];mock=[];headingmap=[]
for p in sorted((ROOT/'source-repo').glob('*.html')):
 soup=BeautifulSoup(p.read_text(),'html.parser');main=soup.select_one('main');inner=main
 for wrapper in list(main.select('.ds-content-inner')):wrapper.unwrap()
 filename=p.name;volume=p.stem;dm=re.search(r'volume-d(\d)',volume);domain=int(dm[1]) if dm else 0
 for q in main.select('.pq'):
  stem=q.select_one('.pq-question');answer=q.select_one('.pq-answer')
  if not stem:continue
  options=[]
  for i,op in enumerate(q.select('.pq-option')):
   cp=BeautifulSoup(str(op),'html.parser');nt=cp.select_one('.pq-note');note=nt.get_text(' ',strip=True) if nt else ''
   if nt:nt.decompose()
   txt=cp.get_text(' ',strip=True);txt=re.sub(r'^[A-Z]\)\s*','',txt)
   options.append(dict(text=txt,correct='correct' in op.get('class',[]),reason=note))
  # Some ML source answer containers also include separate inline exercises.
  # Keep those exercises in the complete reference archive. Isolate this answer.
  primary_answer=None
  if volume=='prereq-ml-specialty' and answer:
   pieces=[]
   for node in answer.find_all(recursive=False):
    if node.name=='p' and (node.select_one('.correct,.wrong') or node.get_text(' ',strip=True).startswith('Correct:')):pieces.append(node.get_text(' ',strip=True))
    else:break
   if pieces:primary_answer=' '.join(pieces)
  qid=volume+'--'+q.get('id',str(len(quizzes)))
  md=re.search(r'q-d(\d)',q.get('id',''));qd=int(md[1]) if md else domain
  quizzes.append(dict(id=qid,sourceId=q.get('id',''),title=stem.get_text(' ',strip=True),options=options,answer=primary_answer if primary_answer else answer.get_text(' ',strip=True) if answer else 'Not in source.',domain=qd,source='../source-repo/'+filename+'#'+q.get('id',''),corrections=correction_ids(stem.get_text(' ',strip=True)+' '+(answer.get_text(' ',strip=True) if answer else ''))))
 if filename=='volume-question-bank.html':
  tb=main.find(id='mock-table02')
  if tb:
   mock=[volume+'--'+a['href'][1:] for a in tb.select('tbody a[href^="#q-"]')]
 # Partition every direct main content element in source order. Preserve all teaching blocks.
 current=[];title=(soup.title.get_text() if soup.title else volume);anchor='';section=0
 def flush():
  global current,title,anchor,section
  if not current:return
  raw=''.join(str(n) if isinstance(n,Tag) else escape(str(n)) for n in current);text=BeautifulSoup(raw,'html.parser').get_text(' ',strip=True)
  if not text:return
  section+=1;rid=f'ref-{volume}-{section:03}'
  references.append(dict(id=rid,title=title,domain=domain,volume=volume,anchor=anchor,html=clean_html(raw,filename),text=text,words=len(text.split()),source='../source-repo/'+filename+('#'+anchor if anchor else ''),corrections=correction_ids(title+' '+text[:1500])))
  headingmap.append(dict(file=filename,anchor=anchor,title=title,slide=rid))
  current=[]
 for el in list(inner.children):
  if isinstance(el,Comment):continue
  if isinstance(el,Tag) and el.name in ['h1','h2','h3']:
   flush();title=el.get_text(' ',strip=True);anchor=el.get('id','');current=[el]
  elif isinstance(el,Tag) or str(el).strip():current.append(el)
 flush()
 study=ROOT/'source-repo/study'/f'{volume}.json'
 if study.exists():
  for section in json.loads(study.read_text()).get('sections',[]):
   for q in section.get('recall',[]):recalls.append(dict(**q,volume=volume,domain=domain))
 inventory.append(dict(file=filename,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),sourceWords=len(main.get_text(' ',strip=True).split()),referenceSections=sum(s['volume']==volume for s in references),quizItems=sum(q['id'].startswith(volume+'--') for q in quizzes),recallItems=sum(q['volume']==volume for q in recalls)))
# Native architecture plates remain editable in both delivery formats.
diagrams=read('course/diagrams.json')
plates=[]
for i,key in enumerate(['rag','ingest','secure-rag','agent','approval','gateway','private','eval']):
 dia=diagrams[key];plates.append(dict(id='architecture-'+key,title=dia['title'],domain=0,skills=[],lead='Trace each stage. Identify its input, output, access rule, and failure behavior.',points=[n[1] for n in dia['steps']],trap='This is a conceptual architecture. Service support and deployment details still require validation.',question='What fails if one stage is omitted?',answer='Use the labels to explain the missing control. Replay the flow with a denied request, a timeout, and stale data.',sources=['genai-lens'],diagram=key,kind='architecture'))
# Source diagrams contain no added branding or attribution overlay.
figures=[dict(id='aws-buildtime',title='AWS agent build-time architecture',domain=2,skills=['2.1.1'],lead='Separate configuration resources from runtime request processing.',points=['Action groups define supported tools and their contracts.','Knowledge Bases supply external evidence.','Agent instructions, model selection, and prompt templates define orchestration configuration.','Version and test changes before production use.'],trap='A configuration change still requires the correct preparation and deployment lifecycle.',question='Which resource describes external actions?',answer='An action group describes supported actions. The execution service still validates and authorizes each operation.',sources=['agents-current'],image='../assets/aws-agent-build.png',kind='figure'),dict(id='aws-runtime',title='AWS agent runtime architecture',domain=2,skills=['2.1.2'],lead='Follow the orchestration loop from user input through tool execution and observations.',points=['The runtime assembles context and evaluates the next step.','The model can request actions or knowledge retrieval.','The application must enforce permission and side-effect safety.','The loop ends with a result or a request for more input.'],trap='The figure explains the service flow. Add explicit task budgets, authorization, and evaluation for your application.',question='What does an observation represent?',answer='It is evidence returned from an action or retrieval step. The next agent decision depends on it.',sources=['agents-current'],image='../assets/aws-agent-runtime.png',kind='figure')]
# Insert plates beside related lessons and figures beside agent teaching.
allcore=[]
for slide in core:
 allcore.append(slide)
 if slide['title']=='Retrieval APIs and tool contracts':allcore.extend(plates[:3])
 if slide['title']=='AgentCore component boundaries':allcore.extend(figures+plates[3:5])
 if slide['title']=='GenAI gateway and CI/CD':allcore.extend(plates[5:6])
 if slide['title']=='Private network and IAM controls':allcore.extend(plates[6:7])
 if slide['title']=='Regression gates and model comparisons':allcore.extend(plates[7:])
# Small native service tables prevent long glossary slides.
service_rows=read('course/services.json');services=[]
for cat in dict.fromkeys(s['category'] for s in service_rows):
 rows=[s for s in service_rows if s['category']==cat]
 for start in range(0,len(rows),6):
  services.append(dict(id='service-'+str(len(services)+1),title=cat,kind='services',rows=rows[start:start+6],domain=0,sources=['aip-01-in-scope-services'],lead='Know the service boundary. Do not infer that every listed service supports every GenAI feature.'))
allcore[-1]['sources']=['exam','genai-lens']
allcore[1]['points'].append('AWS lists 75 total questions and 180 minutes for the exam.')
allcore[1]['sources']=['exam','certification']
# Add per-slide source and repository access.
for slide in allcore:
 terms=set(re.findall(r'[a-z]{4,}',slide['title'].lower()))-{'model','models','systems','application','applications','controls','with','from','and','the'}
 scored=[]
 for r in references:
  if 'question' in r['title'].lower():continue
  score=len(terms & set(re.findall(r'[a-z]{4,}',r['title'].lower())))
  if score:scored.append((score,r['id']))
 slide['related']=[r for score,r in sorted(scored,reverse=True)[:6]]
 if slide.get('domain'):slide['sources']=list(dict.fromkeys(slide.get('sources',[])+['domain'+str(slide['domain'])]))
 slide['corrections']=correction_ids(slide['title'])
# Coverage checks are structural, not a claim-by-claim fact audit.
assert len(skills)==98
assert len(mock)==75 and all(any(q['id']==qid for q in quizzes) for qid in mock)
assert len([q for q in quizzes if q['id'].startswith('volume-question-bank--')])==200
for q in quizzes:
 assert q['options'] and any(o['correct'] for o in q['options']),q['id']
quizzes.sort(key=lambda q:(not q['id'].startswith('volume-question-bank--'),0))
report=dict(coreSlides=len(allcore),authoredLessons=len(core),architecturePlates=len(plates),officialFigures=len(figures),serviceSlides=len(services),serviceEntries=len(service_rows),mappedSkills=len(skills),referenceSections=len(references),interactiveQuestions=len(quizzes),recallCards=len(recalls),mockQuestions=len(mock),inventory=inventory,limits=['Skill mapping verifies an explicit teaching reference. It does not prove complete mastery or exhaustive exam coverage.','Repository material remains inherited source content. Known corrections accompany it. Not every inherited claim or answer receives independent verification.','The mock reuses repository bank items. Its raw score cannot predict a scaled AWS score.','Official Skill Builder sign-in content and undisclosed exam items were not accessed.','Source snapshots show retrieved content. Current model limits and availability can change.'])
deep=read('course/deep-layers.json') if (ROOT/'course/deep-layers.json').exists() else []
figs=read('course/official-figures.json') if (ROOT/'course/official-figures.json').exists() else []
if (ROOT/'course/additional-figures.json').exists():figs.extend(read('course/additional-figures.json'))
# Documentation UI screenshots support practical chapter work. Exclude the
# Agents Classic model picker because its provider logos and access flow are stale.
ui_figs=read('course/ui-figures.json') if (ROOT/'course/ui-figures.json').exists() else []
ui_figs=[f for f in ui_figs if f['id']!='agent-model-selection']
labs=read('course/practical-labs.json') if (ROOT/'course/practical-labs.json').exists() else []
primer=read('course/prerequisite-primer.json') if (ROOT/'course/prerequisite-primer.json').exists() else []
# Exclude decorative gradients, generic brains, and a faint source overview.
figs=[f for f in figs if f['id'] not in ['agentcore-components','orchestration-orchestrator','knowledge-base-architecture']]
for f in figs:f['sourceId']=f['sourceId'].removesuffix('.md')
dossiers=[]
for path in ['course/skill-dossiers-d1-d2.json','course/skill-dossiers-d3-d5.json']:
 if (ROOT/path).exists():dossiers.extend(read(path))
dossiers.sort(key=lambda d:[int(x) for x in d['skill'].split('.')])
report['skillDossiers']=len(dossiers)
report['treatiseChapters']=len(deep);report['officialAtlasFigures']=len(figs);report['uiFigures']=len(ui_figs);report['practicalLabs']=len(labs);report['prerequisitePrimerSections']=len(primer);report['nativeDiagramDefinitions']=len(diagrams);report['mcpReadSources']=sum(s.get('channel')=='official AWS Documentation MCP' for s in sources.values())
# Keep source questions intact in the reference archive. Attach reviewed corrections
# to derived practice items so inherited absolutes do not become teaching rules.
question_errata=[]
for path in sorted((ROOT/'course').glob('question-errata-*.json')):
 data=json.loads(path.read_text())
 question_errata.extend(data if isinstance(data,list) else data.get('errata',data.get('items',[])))
errata_by={e.get('id',e.get('quizId',e.get('quiz_id'))):e for e in question_errata}
for q in quizzes:
 e=errata_by.get(q['id']) or errata_by.get(q['sourceId'])
 if not e:continue
 q['reviewCorrection']=e
 if e.get('correctOptionIndices')==[]:
  q['keyUnsettled']=True
  q['noValidOptionSet']=True
 if e.get('correctOptionIndices'):
  q['originalSourceKey']=[i for i,o in enumerate(q['options']) if o['correct']]
  for i,o in enumerate(q['options']):o['correct']=i in e['correctOptionIndices']
question_reviews=[]
for path in sorted((ROOT/'audits').glob('question-review-*.json')):
 data=json.loads(path.read_text())
 question_reviews.extend(data if isinstance(data,list) else data.get('questions',data.get('reviews',data.get('items',[]))))
review_by={e.get('id',e.get('quizId',e.get('quiz_id'))):e for e in question_reviews}
for q in quizzes:
 r=review_by.get(q['id']) or review_by.get(q['sourceId'])
 if r:
  q['reviewStatus']=r.get('status','uncertain')
  q['keyUnsettled']=q.get('keyUnsettled',False) or r.get('keyStatus') in ['unsettled','incorrect','uncertain'] or r.get('keyUnsettled',False)
  q['reviewNote']=r.get('reason','')
  q['reviewSources']=r.get('sources',r.get('sourceIDs',r.get('sourceIds',[])))
# Use settled practice keys in the timed set. Keep unresolved items in the library.
used=set();reviewed_mock=[]
for mid in mock:
 q=next(x for x in quizzes if x['id']==mid)
 if q.get('keyUnsettled') and not q.get('reviewCorrection',{}).get('correctOptionIndices'):
  q=next((x for x in quizzes if x['domain']==q['domain'] and x['id'].startswith('volume-question-bank') and not x.get('keyUnsettled') and x['id'] not in used and x['id'] not in mock),q)
 if q['id'] not in used:reviewed_mock.append(q['id']);used.add(q['id'])
mock=reviewed_mock
report['questionSpecificCorrections']=len(question_errata)
report['questionReviewItems']=len(question_reviews)
for e in question_errata:
 for sid in e.get('sources',[]):
  if sid in sources:continue
  if sid.startswith('../source-repo/'):
   sources[sid]={'url':'https://github.com/jrajath94/aws-aip-c01-study-guide/blob/823006efa64f98b560dd4fe40445e6a8042ef79b/'+sid.removeprefix('../source-repo/'),'path':sid.removeprefix('../'),'channel':'inherited repository'}
  elif sid.startswith('https://'):sources[sid]={'url':sid,'channel':'linked source'}

course=dict(dossiers=dossiers,deep=deep,figures=figs,uiFigures=ui_figs,labs=labs,primer=primer,core=allcore,references=references,quizzes=quizzes,recalls=recalls,mock=mock,skills=skills,sources=sources,diagrams=diagrams,services=services,corrections=corrections,report=report)
(ROOT/'course/treatise-data.js').write_text('window.COURSE='+json.dumps(course,ensure_ascii=False,separators=(',',':'))+';\n')
(ROOT/'course/treatise-data.json').write_text(json.dumps(course,ensure_ascii=False,separators=(',',':')))
(ROOT/'audits/coverage.json').write_text(json.dumps(report,indent=2))
(ROOT/'audits/skill-map.json').write_text(json.dumps(skills,indent=2))
(ROOT/'audits/repository-map.json').write_text(json.dumps(headingmap,indent=2))
(ROOT/'course/treatise-slides.json').write_text(json.dumps(allcore+services,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['inventory','limits']},indent=2))

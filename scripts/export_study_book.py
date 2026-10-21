from pathlib import Path
import json,re,html,math,copy
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image,Table,TableStyle,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from pypdf import PdfReader,PdfWriter,Transformation
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT
from learning_format import clean_text,question_stem,question_topic,text_runs,rationale_blocks
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
BUILD=ROOT/'.build';BUILD.mkdir(exist_ok=True)
C=json.loads((ROOT/'course/treatise-data.json').read_text())
for n in ('Regular','Bold','Italic','BoldItalic'):
 pdfmetrics.registerFont(TTFont('Anthropic'+n,str(ROOT/f'assets/typography/AnthropicSans-{n}.ttf')))
pdfmetrics.registerFontFamily('AnthropicRegular',normal='AnthropicRegular',bold='AnthropicBold',italic='AnthropicItalic',boldItalic='AnthropicBoldItalic')
styles=getSampleStyleSheet()
NAVY='#123B58';TEAL='#0F645A';RUST='#913D24';TEXT='#20252B'
styles.add(ParagraphStyle(name='BodyCompact',fontName='AnthropicRegular',fontSize=10.5,leading=14,spaceAfter=6,alignment=TA_JUSTIFY,textColor=colors.HexColor(TEXT),splitLongWords=True,hyphenationLang='en_US',allowWidows=0,allowOrphans=0))
for name,size,lead,before,after in [('H1Compact',20,24,17,10),('H2Compact',14,18,12,7),('H3Compact',11.5,15,8,5)]:
 styles.add(ParagraphStyle(name=name,fontName='AnthropicBold',fontSize=size,leading=lead,spaceBefore=before,spaceAfter=after,textColor=colors.HexColor(NAVY),keepWithNext=True))
styles.add(ParagraphStyle(name='TitleStudy',parent=styles['H1Compact'],fontSize=24,leading=28,textColor=colors.black,spaceBefore=0,spaceAfter=12))
styles.add(ParagraphStyle(name='CaptionCompact',fontName='AnthropicRegular',fontSize=8.3,leading=11,spaceAfter=6,textColor=colors.HexColor('#505A64'),splitLongWords=True))
for name,col,bold,italic in [('Remember',TEAL,True,False),('Caution',RUST,False,True),('Limit',RUST,False,True),('Scenario',NAVY,False,False),('Answer',TEAL,True,False),('Option',TEXT,False,False),('QuestionMeta','#505A64',False,True)]:
 styles.add(ParagraphStyle(name=name,parent=styles['BodyCompact'],keepWithNext=name in ['Scenario','QuestionMeta','Answer'],textColor=colors.HexColor(col),fontName='Anthropic'+('BoldItalic' if bold and italic else 'Bold' if bold else 'Italic' if italic else 'Regular'),spaceBefore=4 if name in ['Remember','Answer','Scenario'] else 0))
styles['Option'].leftIndent=16;styles['Option'].firstLineIndent=-16
styles.add(ParagraphStyle(name='Procedure',parent=styles['BodyCompact'],leftIndent=14,firstLineIndent=-14))
D=Document();sec=D.sections[0];sec.page_width=Inches(5.5);sec.page_height=Inches(8.5)
sec.top_margin=sec.left_margin=sec.right_margin=Inches(24/72);sec.bottom_margin=Inches(26/72)
sec.header_distance=sec.footer_distance=Inches(.12)
for name in ('Normal','Body Text','Caption','Title','Heading 1','Heading 2','Heading 3','List Number'):
 st=D.styles[name];st.font.name='Anthropic Sans';st.font.size=Pt(10.5)
 st.paragraph_format.space_after=Pt(6);st.paragraph_format.line_spacing=1.25
 st.paragraph_format.widow_control=True
for name,size in [('Heading 1',20),('Heading 2',14),('Heading 3',11.5)]:
 D.styles[name].font.size=Pt(size);D.styles[name].font.color.rgb=RGBColor.from_string(NAVY[1:]);D.styles[name].paragraph_format.keep_with_next=True
D.styles['Normal'].paragraph_format.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
for heading in ['Title','Heading 1','Heading 2','Heading 3']:D.styles[heading].paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
D.styles['Title'].font.size=Pt(24);D.styles['Title'].font.color.rgb=RGBColor(0,0,0)
D.styles['Caption'].font.size=Pt(8.3)
# Remove theme substitutions and template decoration from Word styles.
for st in D.styles:
 if st.type not in (1,2):continue
 st.font.name='Anthropic Sans'
 if st.element.rPr is not None and st.element.rPr.rFonts is not None:
  rf=st.element.rPr.rFonts
  for key in list(rf.attrib):
   if 'theme' in key.lower():del rf.attrib[key]
  for key in ('ascii','hAnsi','eastAsia','cs'):rf.set(qn('w:'+key),'Anthropic Sans')
 for border in list(st.element.xpath('.//w:pBdr')):border.getparent().remove(border)

settings=D.settings.element
el=OxmlElement('w:autoHyphenation');el.set(qn('w:val'),'true');settings.append(el)
for prop in ('author','last_modified_by','title','subject','keywords','comments','category'):setattr(D.core_properties,prop,'')
footer=sec.footer.paragraphs[0];footer.alignment=2
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
flows=[];practice=[];stats={'chapterIds':[],'skillIds':[],'labIds':[],'figureIds':[],'quizIds':[]}
def clean(s):return clean_text(s)
def p(s,style='BodyCompact',target=None,word=True,keep=False):
 target=flows if target is None else target;s=clean(s)
 emphasis=style not in ['CaptionCompact','QuestionMeta','TitleStudy'] and not style.startswith('H')
 pieces=text_runs(s,emphasis)
 if style=='Option' and re.match(r'^[A-E]\. ',s):pieces=[(s[:3],True)]+text_runs(s[3:],True)
 markup=''.join('<b>'+escape(t)+'</b>' if strong else escape(t) for t,strong in pieces)
 paragraph_style=copy.copy(styles[style]) if keep else styles[style]
 if keep:paragraph_style.keepWithNext=True
 target.append(Paragraph(markup,paragraph_style))
 if word:
  ws={'H1Compact':'Heading 1','H2Compact':'Heading 2','H3Compact':'Heading 3','CaptionCompact':'Caption','TitleStudy':'Title'}.get(style,'Normal')
  para=D.add_paragraph(style=ws)
  if style!='TitleStudy' and not style.startswith('H'):para.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
  if keep or style in ['QuestionMeta','Scenario','Answer']:para.paragraph_format.keep_with_next=True
  if style in ['Option','Procedure']:
   indent=16 if style=='Option' else 14;para.paragraph_format.left_indent=Pt(indent);para.paragraph_format.first_line_indent=Pt(-indent)
  fullbold=style in ['Remember','Answer','TitleStudy'] or style.startswith('H');italic=style in ['Caution','Limit','QuestionMeta']
  col={'Remember':TEAL,'Answer':TEAL,'Scenario':NAVY,'Caution':RUST,'Limit':RUST,'QuestionMeta':'#505A64'}.get(style)
  for text,strong in pieces:
   run=para.add_run(text);run.font.name='Anthropic Sans';run.bold=fullbold or strong;run.italic=italic
   if col:run.font.color.rgb=RGBColor.from_string(col[1:])
   elif strong:run.font.color.rgb=RGBColor.from_string(NAVY[1:])
def prose(text,target=None,word=True,style='BodyCompact'):
 for block,role in rationale_blocks(text):p(block,style if style!='BodyCompact' else role,target,word)
def h(s,level=2,**kw):p(s,f'H{level}Compact',**kw)
def enum(items,target=None,word=True):
 for i,t in enumerate(items,1):p(f'{i}. {t}','Procedure',target=target,word=word)
source_entries={}
def sources(ids,target=None,word=True):
 refs=[]
 for i in ids:
  src=C['sources'].get(i,{})
  url=src.get('url')
  if url and url.startswith('../source-repo/'):url='https://github.com/jrajath94/aws-aip-c01-study-guide/blob/823006efa64f98b560dd4fe40445e6a8042ef79b/'+url.removeprefix('../source-repo/')
  if url and '/jrajath94/aws-aip-c01-study-guide/blob/' in url:url=url.split('#')[0]
  if url:
   if url not in source_entries:source_entries[url]=len(source_entries)+1
   refs.append(str(source_entries[url]))
 if refs:
  line='Sources ['+', '.join(sorted(set(refs),key=int))+'].'
  destination=flows if target is None else target
  if destination and isinstance(destination[-1],Paragraph) and destination[-1].getPlainText()==line:return
  p(line,'CaptionCompact',target,word)
def picture(f):
 path=(ROOT/'course'/f['path']).resolve()
 if not path.exists():return
 from PIL import Image as PILImage
 with PILImage.open(path) as im:w,hh=im.size
 scale=min(348/w,210/hh,1)
 h(f['title'],3)
 flows.append(Image(str(path),w*scale,hh*scale))
 picture_run=D.add_picture(str(path),width=Inches(w*scale/72),height=Inches(hh*scale/72))
 D.paragraphs[-1].paragraph_format.keep_with_next=True
 p(f.get('explanation',f.get('practicalLesson','')))
 if f.get('readSteps'):enum(f['readSteps'])
 p(f.get('limit',''),'Limit')
 p(f['sourceUrl'],'CaptionCompact')
 stats['figureIds'].append(f['id'])
p('AIP-C01 study and practice','TitleStudy')
p('Reader: A candidate who needs a first-principles route through the official exam scope.')
p('Read the concepts. Predict the result. Explain the mechanism. Then answer a new scenario without notes.')
p('This book covers all 98 published skills. AWS states that its exam guide is not a comprehensive list of exam content. No book guarantees a pass.')
h('How to use the visual cues')
p('Remember. Teal text marks a decision rule or the answer to retain.','Remember')
p('Check the limit. Rust italics mark conditions, uncertainty, and common mistakes.','Limit')
p('Bold terms identify the concept that controls the decision. Read the explanation before you memorize the answer.')
h('Use the two-day route')
enum(['Read the prerequisite primer. Explain each term in your own words.','Read Chapters 1 to 12. Trace each request from input to result.','Read Chapters 13 to 24. Compare each control with its failure case.','Answer the mastery questions before you read their answers.','Take the timed mock in the HTML course. Explain each rejected choice.','Review every weak skill. Use the separate practice booklet for more scenarios.'])
p('The route is a study recommendation, not an AWS readiness threshold. Do not replace sleep with a complete reread of the source archive.')
h('Exam values')
for s in ['AIP-C01 means AWS Certified Generative AI Developer, Professional. AIF-C01 is a different exam.','The exam contains 75 questions in 180 minutes. There are 65 scored questions and 10 unidentified unscored questions.','The scaled score ranges from 100 to 1000. The minimum passing score is 750. This is not a 75% raw score rule.','Domain weights are 31%, 26%, 20%, 12%, and 11%. Select all required responses for a multiple-response question.','AWS expects production AWS experience and hands-on generative AI experience. Proposed lab procedures in this book are not executed lab evidence.']:p(s)
sources(['scope-ai-professional-01'])
h('Print procedure')
enum(['Open the file whose name contains Two-Up.','Select landscape US Letter and actual size.','Select one PDF page per printed side. The file already contains two logical pages.','Select duplex and flip on the short edge.','Print a test sheet before the full job.'])
p('Each sheet carries four logical pages with duplex print. The separate practice booklet lets you avoid repeat print of the core book.')
primer=C.get('primer',[])
if not primer and (ROOT/'course/prerequisite-primer.json').exists():primer=json.loads((ROOT/'course/prerequisite-primer.json').read_text())
if isinstance(primer,dict):primer=primer.get('sections',[])
if primer:
 h('Prerequisite primer',1)
 for x in primer:
  h(x.get('title','Foundation'))
  for k,v in x.items():
   if k in ('title','id','sources'):continue
   if isinstance(v,str):p(v)
   elif isinstance(v,list):
    for a in v:
     if isinstance(a,str):p(a)
  sources(x.get('sources',[]))
# Chapter placement uses authored mapping in treatise.js, mirrored by explicit skill families.
js=(ROOT/'course/treatise.js').read_text()
match=re.search(r'const skillChapter\s*=\s*(\{.*?\});',js,re.S)
mp={}
if match:
 try:mp=json.loads(match.group(1))
 except:pass
# Stable exact placement fallback from each chapter keywords, but print all skills even without placement.
dossier_by={d['skill']:d for d in C['dossiers']};printed=set()
figure_map={'agent-build-time':11,'agent-runtime':11,'rag-ingestion':5,'rag-runtime':4,'saga-orchestration':12,'supervisor-pattern':11,'genbi-managed':14,'genbi-custom':14,'agent-infrastructure-ops':12,'app-builder-dashboard':14,'app-builder-dashboard-vpc':17,'text-app':3,'text-app-vpc':17,'agent-app':11,'agent-app-vpc':17,'mcp-server-app':12,'agent-builder-deploy':13}
for ix,ch in enumerate(C['deep'],1):
 h(f'Chapter {ix}. {ch["title"]}',1);stats['chapterIds'].append(ch['id'])
 p(ch['idea'],'Remember',keep=True)
 for section in ch['sections']:
  h(section['title'],3)
  for text in section['paragraphs']:p(text)
 h('Invariant',3);p(ch['invariant'],'Remember')
 h('Controlled experiment',3);enum(ch['experiment']['steps']);p(ch['experiment']['prediction'],'Limit');p(ch['experiment']['interpretation'])
 h('Transfer check',3);p(ch['transferQuestion']);p(ch['transferAnswer'])
 for f in C.get('figures',[]):
  # Use topic keywords rather than random chapter placement.
  if f.get('chapterId')==ch['id'] or figure_map.get(f['id'])==ix:picture(f)
 for f in C.get('uiFigures',[]):
  if f.get('chapterId')==ch['id'] or figure_map.get(f['id'])==ix:picture(f)
 for lab in C.get('labs',C.get('practicalLabs',[])):
  if lab['chapterId']!=ch['id']:continue
  h(lab['title'],2);stats['labIds'].append(lab['chapterId']);p(lab['goal']);p(lab['status'],'CaptionCompact')
  p(lab.get('costNote',''),'CaptionCompact')
  for i,step in enumerate(lab['steps'],1):
   p(f'{i}. {step["action"]}');p('Reason. '+step['why']);p('Evidence. '+step['evidence'])
  for k in ('expectedEvidence','failureChecks','cleanup','examTransfer'):
   v=lab.get(k,[]);h(re.sub(r'([A-Z])',r' \1',k).capitalize(),3)
   if isinstance(v,str):p(v)
   else:enum(v)
  sources(lab.get('sources',[]))
 sources(ch.get('sources',[]))
h('All 98 skill cases',1)
p('Each case adds a decision boundary, causal trace, failure test, and transfer check. These are authored study scenarios.')
for d in C['dossiers']:
 stats['skillIds'].append(d['skill']);h(d['title'])
 p(d['principle']);p(d['mechanism'])
 h('Decision',3)
 for k in ('when','choice','reason','reject'):p(d['decision'][k], 'Remember' if k=='choice' else 'Caution' if k=='reject' else 'BodyCompact')
 h('Causal trace',3);enum(d['workedTrace'])
 h('Failure test',3)
 for k in ('symptom','check','fix'):p(d['failure'][k])
 h('Experiment',3)
 for k in ('change','observe','limit'):p(d['experiment'][k], 'Limit' if k=='limit' else 'BodyCompact')
 h('Test your understanding',3);p(d['masteryQuestion'],'Scenario');p(d['masteryAnswer'],'Remember');sources(d.get('sources',[]))
h('Decision reference',1)
for s in C['core']:
 if s.get('kind') in ('diagram','official-figure'):continue
 h(s['title']);p(s.get('lead',''))
 for t in s.get('points',[]):p(t)
 for key in ('trap','why','decision'):
  v=s.get(key)
  if isinstance(v,str):p(v,'Caution' if key=='trap' else 'BodyCompact')
 sources(s.get('sources',[]))
h('Architecture reference',1)
for key,dia in C['diagrams'].items():
 h(dia['title'])
 cells=[]
 for i,(name,body) in enumerate(dia['steps'],1):
  cells.append(Paragraph(escape(str(i)+'. '+clean(name))+ '<br/>'+escape(clean(body)),styles['BodyCompact']))
 rows=[cells[i:i+2] for i in range(0,len(cells),2)]
 if len(rows[-1])<2:rows[-1].append('')
 t=Table(rows,colWidths=[174,174],hAlign='LEFT');t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#999999')),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5)]));flows.append(t)
 table=D.add_table(rows=0, cols=2)
 table.style='Table Grid'
 for ri,row in enumerate(rows):
  cellsw=table.add_row().cells
  for j,v in enumerate(row):
   si=ri*2+j
   if si<len(dia['steps']):
    name,body=dia['steps'][si];cell=cellsw[j];cell.text=''
    cp=cell.paragraphs[0];cp.paragraph_format.keep_with_next=True
    cr=cp.add_run(str(si+1)+'. '+clean(name));cr.bold=True;cr.font.color.rgb=RGBColor.from_string(NAVY[1:])
    bp=cell.add_paragraph();bp.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
    for text,strong in text_runs(body):
     br=bp.add_run(text);br.bold=strong
 for row in table.rows:row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
 if dia.get('relation'):p(dia['relation'])
 p('Numbers identify components or stages. Follow the stated relationship. Independent controls do not form a strict sequence.','CaptionCompact')
h('Service boundaries',1)
for group in C['services']:
 h(group['title'])
 for row in group['rows']:p(row['name']+'. '+row['role'])
h('Corrections to inherited material',1)
for x in C['corrections']:
 h(x.get('topic',x.get('title','Correction')),3)
 p(x.get('text',''))
 sources(x.get('sources',[]))
h('Readiness evidence',1)
p('Confidence must come from unseen decisions and observable evidence. Familiarity with these pages alone does not show readiness.')
enum(['Explain the model, retrieval, identity, safety, and operations path without notes.','Predict the effect of one configuration change before you run the experiment.','Explain why every rejected option fails a stated requirement.','Repeat the test with a new scenario and different wording.','Use the official AWS practice set and practice exam to obtain independent evidence.','Delay any claim of practical competence until you execute and inspect representative labs.'])
p('The official practice set is available through AWS Skill Builder. Its question bodies were not accessible in the public documentation fetch. They are not reproduced or claimed as audited here.')
p('https://skillbuilder.aws/category/exam-prep/generative-ai-developer-professional-AIP-C01','CaptionCompact')
p('The HTML edition retains the complete source teaching archive. The print edition contains the authored course, skill cases, labs, and service reference. Print the question booklet separately.')
# Store all inherited questions with labels and answer key warnings.
h('Repository practice booklet',1,target=practice,word=False)
p('These 250 questions come from the supplied repository. They are not AWS exam questions. Answer keys and rationales are inherited source claims.',target=practice,word=False)
p('All 250 extracted items receive a semantic review. Read the correction beside each disputed claim. Eight unsettled keys remain discussion cases. Current official documentation takes precedence.',target=practice,word=False)
D.add_heading('Repository practice booklet',level=1)
D.add_paragraph('All 250 extracted items receive a semantic review. Read each correction. Eight unsettled keys remain discussion cases. Current official documentation takes precedence.')
for n,q in enumerate(C['quizzes'],1):
 if n==1:h('Professional practice scenarios',2,target=practice)
 if n==201:h('Prerequisite practice',2,target=practice)
 stats['quizIds'].append(q['id']);question_start=len(practice)
 h(f'Question {n}',2,target=practice)
 p(question_topic(q),'QuestionMeta',target=practice)
 p(question_stem(q['title']),'Scenario',target=practice)
 count=sum(o['correct'] for o in q['options'])
 unresolved=q.get('keyUnsettled') and not q.get('reviewCorrection',{}).get('correctOptionIndices')
 p('Discussion case. Compare the available choices with the documented limits.' if unresolved else 'Choose one answer.' if count==1 else f'Choose {count} answers.','QuestionMeta',target=practice)
 for i,opt in enumerate(q['options']):p(chr(65+i)+'. '+re.sub(r'^[A-E][.)]\s*','',opt['text']),'Option',target=practice,keep=i<len(q['options'])-1)
 practice[question_start:]=[KeepTogether(practice[question_start:])]
 h('Answer and explanation',3,target=practice)
 p('No reliable answer key is established for this source question.' if unresolved else 'Reviewed choice '+', '.join(chr(65+i) for i,o in enumerate(q['options']) if o['correct'])+'.','Caution' if unresolved else 'Answer',target=practice)
 if q.get('reviewCorrection'):
  r=q['reviewCorrection'];prose(r.get('correctedAnswer',r.get('correction','')),target=practice)
  reason=r.get('reason','')
  if reason and not reason.startswith(('Narrow absolute','Remove the unsupported universal')):
   h('Important limit',3,target=practice);p(reason,'Limit',target=practice)
  sources(r.get('sources',[]),target=practice)
 else:
  if q.get('reviewStatus')!='supported' and q.get('reviewNote'):p(q['reviewNote'],'Limit',target=practice)
  prose(q['answer'],target=practice)
  alternatives=[(i,o) for i,o in enumerate(q['options']) if o.get('reason')]
  if alternatives:
   h('Why other choices fail',3,target=practice)
   for i,o in alternatives:prose(chr(65+i)+'. '+o['reason'],target=practice)

def footer_pdf(canvas,doc):
 canvas.saveState();canvas.setFont('AnthropicRegular',7);canvas.setFillColor(colors.HexColor('#555555'));canvas.drawRightString(372,10,str(doc.page));canvas.restoreState()
def make_pdf(path,story):
 doc=SimpleDocTemplate(str(path),pagesize=(396,612),leftMargin=24,rightMargin=24,topMargin=24,bottomMargin=26,title='',author='',creator='',subject='')
 doc.build(story,onFirstPage=footer_pdf,onLaterPages=footer_pdf)
def impose(src,dst):
 r=PdfReader(src);w=PdfWriter();mapping=[]
 for i in range(0,len(r.pages),2):
  page=w.add_blank_page(width=792,height=612)
  page.merge_transformed_page(r.pages[i],Transformation().translate(tx=0,ty=0))
  if i+1<len(r.pages):page.merge_transformed_page(r.pages[i+1],Transformation().translate(tx=396,ty=0))
  mapping.append([i+1]+([i+2] if i+1<len(r.pages) else []))
 w.add_metadata({'/Author':'','/Creator':'','/Producer':'','/Title':''})
 with open(dst,'wb') as f:w.write(f)
 return {'logicalPages':len(r.pages),'physicalSides':len(w.pages),'duplexSheets':math.ceil(len(w.pages)/2),'mapping':mapping,'emptyLogicalPages':[i+1 for i,p in enumerate(r.pages) if len((p.extract_text() or '').strip())<3]}
h('Official source index',1)
for url,n in source_entries.items():p('['+str(n)+'] '+url,'CaptionCompact')
make_pdf(BUILD/'core-logical.pdf',flows);make_pdf(BUILD/'practice-logical.pdf',practice)
stats['corePrint']=impose(BUILD/'core-logical.pdf',BUILD/'AIP-C01-Core-Two-Up.original.pdf')
stats['practicePrint']=impose(BUILD/'practice-logical.pdf',BUILD/'AIP-C01-Practice-Two-Up.original.pdf')
D.save(BUILD/'AIP-C01-Study-Book.original.docx')
from embed_docx_fonts import embed
embed(BUILD/'AIP-C01-Study-Book.original.docx')
(ROOT/'audits/print-export.json').write_text(json.dumps(stats,indent=2))
print(json.dumps({k:v for k,v in stats.items() if k.endswith('Print')},indent=2))

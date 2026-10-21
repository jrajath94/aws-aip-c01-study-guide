from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from pypdf import PdfReader
import json,re,hashlib
ROOT=Path(__file__).resolve().parent.parent
report={}
for name in ['Core','Practice']:
 orig=PdfReader(ROOT/f'.build/AIP-C01-{name}-Two-Up.original.pdf');final=PdfReader(ROOT/f'output/AIP-C01-{name}-Two-Up.pdf')
 before=[re.sub(r'\s+','',p.extract_text() or '') for p in orig.pages];after=[re.sub(r'\s+','',p.extract_text() or '') for p in final.pages]
 assert before==after,name+' text changed'
 assert all(len(t.strip())>3 for t in after)
 assert all(abs(float(p.mediabox.width)-792)<.1 and abs(float(p.mediabox.height)-612)<.1 for p in final.pages)
 report[name]={'physicalSides':len(final.pages),'textPreserved':True,'noEmptyPages':True,'pageSizePoints':[792,612],'metadata':{k:v for k,v in (final.metadata or {}).items() if k in ['/Author','/Creator','/Producer','/Title']}}
with ZipFile(ROOT/'.build/AIP-C01-Study-Book.original.docx') as a,ZipFile(ROOT/'output/AIP-C01-Study-Book.docx') as b:
 def text(z):
  root=etree.fromstring(z.read('word/document.xml'));return root.xpath('//w:t/text()',namespaces={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
 assert text(a)==text(b),'DOCX text changed'
 assert len([n for n in b.namelist() if n.startswith('word/fonts/')])==4
 report['DOCX']={'paragraphTextPreserved':True,'embeddedFonts':4,'editable':True}
report['scope']='PDF text comparison ignores extraction whitespace between styled spans. DOCX paragraph text compares exactly. Page geometry and package integrity are checked. Visual review is recorded separately.'
(ROOT/'audits/export-integrity.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))

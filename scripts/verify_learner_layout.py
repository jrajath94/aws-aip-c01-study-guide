from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from pypdf import PdfReader
import json,re,subprocess
ROOT=Path(__file__).resolve().parent.parent
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with ZipFile(ROOT/'.build/AIP-C01-Study-Book.original.docx') as z:
 doc=etree.fromstring(z.read('word/document.xml'))
 ps=doc.xpath('//w:p[w:r/w:t]',namespaces=ns)
 body=[p for p in ps if not p.xpath('./w:pPr/w:pStyle[starts-with(@w:val,"Heading") or @w:val="Title"]',namespaces=ns)]
 explicit_justify=sum(bool(p.xpath('./w:pPr/w:jc[@w:val="both"]',namespaces=ns)) for p in body)
 assert explicit_justify>len(body)*.9
 counts={key:len(doc.xpath(xpath,namespaces=ns)) for key,xpath in {
  'boldRuns':'//w:r[w:rPr/w:b[not(@w:val="0")]]',
  'italicRuns':'//w:r[w:rPr/w:i[not(@w:val="0")]]',
  'coloredRuns':'//w:r[w:rPr/w:color]',
  'embeddedImages':'//w:drawing'}.items()}
 assert counts['boldRuns']>1000 and counts['italicRuns']>100
 fonts=[n for n in z.namelist() if n.startswith('word/fonts/')]
 assert len(fonts)==4
course=json.loads((ROOT/'course/treatise-data.json').read_text())
base=json.loads(subprocess.check_output(['git','show','988194f:course/treatise-data.json'],text=True))
old={q['id']:q for q in base['quizzes']}
assert len(course['quizzes'])==250
for q in course['quizzes']:
 assert q['options']==old[q['id']]['options'],q['id']+' option or key change'
 assert q['answer']==old[q['id']]['answer'],q['id']+' rationale change'
 assert q.get('reviewCorrection')==old[q['id']].get('reviewCorrection'),q['id']+' review change'
texts=[]
for file in ['core-logical.pdf','practice-logical.pdf']:
 reader=PdfReader(ROOT/'.build'/file)
 pages=[p.extract_text() or '' for p in reader.pages]
 assert all(len(t.strip())>3 for t in pages)
 assert not re.search(r'\bq[-_ ]?d[-_ ]?\d+(?:[-_]\d+)+\b','\n'.join(pages),re.I)
 texts.append('\n'.join(pages))
nums=[int(x) for x in re.findall(r'^Question (\d+)\s*$',texts[1],re.M)]
assert nums==list(range(1,251)),nums
report={'questions':250,'numberedInOrder':True,'visibleMachineCodes':0,'sourceOptionsKeysRationalesAndReviewsPreserved':True,'wordBodyParagraphs':len(body),'explicitJustifiedParagraphs':explicit_justify,'embeddedFontFaces':4,**counts,'noEmptyLogicalPages':True,'scope':'Structural and text checks. Visual review has a separate scope.'}
(ROOT/'audits/learner-layout-checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

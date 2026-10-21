"""Presentation helpers. Source facts, identifiers, and answer keys remain unchanged."""
import re,html
CODE=re.compile(r'\bq[-_ ]?d[-_ ]?\d+(?:[-_]\d+)+\b',re.I)
TERMS=['explicit deny','least privilege','server-derived','trusted identity','context window','token budget','input tokens','output tokens','embedding space','vector dimensions','idempotency','data residency','full jitter','exponential backoff','return of control','stopReason','toolUseId','invocation logging','CloudTrail','Provisioned Throughput','RetrieveAndGenerate','Retrieve','schema validation','prompt injection','cache key','TTL','false positives','false negatives','precision','recall','held-out test','critical path','rollback','data drift','concept drift','grounding','relevance']
PATTERN=re.compile(r'(?<!\w)(?:'+'|'.join(re.escape(t) for t in sorted(TERMS,key=len,reverse=True))+r')(?!\w)',re.I)
def clean_text(text):
 text=html.unescape(str(text)).replace('—','. ').replace('–',' to ').replace(';',',').replace('\u00a0',' ')
 if not text.strip().startswith(('https://','http://')):text=CODE.sub('',text)
 return re.sub(r' {2,}',' ',text).strip()
def question_stem(text):
 text=html.unescape(str(text));m=re.search(r'\bQ(?:uestion)?\s*\d+[.)]\s*',text,re.I)
 if m:text=text[m.end():]
 return clean_text(text).strip(' ,·')
def question_topic(q):
 m=re.search(r'\b[1-5]\.[1-6]\s+(.+?)\s+Q\d+[.)]',q['title'])
 return clean_text(m.group(1)) if m else 'Foundations and practical decisions'
def text_runs(text,emphasis=True):
 text=clean_text(text);matches=list(PATTERN.finditer(text))[:2] if emphasis else []
 out=[];start=0
 for match in matches:
  if match.start()>start:out.append((text[start:match.start()],False))
  out.append((match.group(),True));start=match.end()
 if start<len(text):out.append((text[start:],False))
 return out or [(text,False)]
def rationale_blocks(text):
 text=clean_text(text)
 text=re.sub(r'^Why\s+[A-E](?:\s*(?:,|and)\s*[A-E])*\s+(?:is|are)\s+correct:\s*','',text,flags=re.I)
 text=re.sub(r'^Correct:\s*[A-E](?:\s*(?:,|and)\s*[A-E])*\.\s*','',text,flags=re.I)
 parts=re.split(r'The trap AWS set here:\s*',text,flags=re.I)
 out=[]
 for n,part in enumerate(parts):
  sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',part)
  for i in range(0,len(sentences),3):
   block=' '.join(sentences[i:i+3]).strip()
   if block:out.append((block,'Remember' if n else 'BodyCompact'))
 return out

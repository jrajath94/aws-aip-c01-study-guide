import urllib.request,pathlib,json,concurrent.futures
fix={ 'guardrails-reasoning':'https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html','evaluation-metrics':'https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-metrics.html','response-stream':'https://docs.aws.amazon.com/apigateway/latest/developerguide/response-transfer-mode.html','kb-images':'https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html','reasoning-integration':'https://docs.aws.amazon.com/bedrock/latest/userguide/integrate-automated-reasoning-checks.html'}
def f(item):
 name,url=item
 try:
  data=urllib.request.urlopen('https://r.jina.ai/'+url,timeout=70).read().decode();pathlib.Path('research',name+'.md').write_text(data)
  return dict(id=name,url=url,path='research/'+name+'.md',retrieved='2026-10-20',bytes=len(data))
 except Exception as e:return dict(id=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:r=list(pool.map(f,fix.items()))
pathlib.Path('research/corrected-manifest.json').write_text(json.dumps(r,indent=2));print(r)

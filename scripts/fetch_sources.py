import concurrent.futures,json,urllib.request,pathlib,time
base='https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/'
urls=[base+'ai-professional-01.html']+[base+f'ai-professional-01-domain{i}.html' for i in range(1,6)]+[base+'ai-professional-01-technologies-concepts.html',base+'aip-01-in-scope-services.html',base+'aip-01-out-of-scope-services.html']
def fetch(url):
 name=url.rsplit('/',1)[1].replace('.html','.md')
 for attempt in range(3):
  try:
   data=urllib.request.urlopen('https://r.jina.ai/'+url,timeout=80).read().decode()
   if len(data)<500: raise ValueError('Empty source')
   pathlib.Path('research',name).write_text(data)
   return {'url':url,'path':'research/'+name,'bytes':len(data),'retrieved':'2026-10-20'}
  except Exception as e:
   if attempt==2:return {'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,urls))
pathlib.Path('research/manifest.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))

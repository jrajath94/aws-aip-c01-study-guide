import concurrent.futures,urllib.request,pathlib,json
pages={
'bedrock-overview':'https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html',
'converse':'https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html',
'knowledge-bases':'https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html',
'chunking':'https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html',
'retrieval':'https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html',
'guardrails':'https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html',
'cross-region':'https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html',
'prompt-cache':'https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html',
'logging':'https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html',
'evaluation':'https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html',
'agents':'https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html',
'flows':'https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html',
'prompt-management':'https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html',
'data-protection':'https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html',
'vpc':'https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html',
'customization':'https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html',
'batch':'https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html',
'agentcore':'https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html',
'sagemaker-deploy':'https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html',
'genai-lens':'https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html',
'bedrock-api':'https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.html',
'bedrock-errors':'https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html',
'api-streaming':'https://docs.aws.amazon.com/apigateway/latest/developerguide/response-streaming.html',
'strands':'https://strandsagents.com/latest/documentation/docs/'}
def fetch(item):
 name,url=item
 try:
  text=urllib.request.urlopen('https://r.jina.ai/'+url,timeout=90).read().decode()
  pathlib.Path('research',name+'.md').write_text(text)
  return {'id':name,'url':url,'path':'research/'+name+'.md','bytes':len(text),'retrieved':'2026-10-20'}
 except Exception as e:return {'id':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:r=list(pool.map(fetch,pages.items()))
pathlib.Path('research/service-manifest.json').write_text(json.dumps(r,indent=2))
print(json.dumps(r,indent=2))

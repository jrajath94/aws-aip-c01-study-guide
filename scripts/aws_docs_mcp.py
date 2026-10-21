import asyncio,json,os,pathlib,sys
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
async def main():
 env=dict(os.environ,FASTMCP_LOG_LEVEL='ERROR',AWS_DOCUMENTATION_PARTITION='aws',MCP_USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
 server=StdioServerParameters(command='/Users/rj/.local/bin/uvx',args=['awslabs.aws-documentation-mcp-server@latest'],env=env)
 async with stdio_client(server) as (reader,writer):
  async with ClientSession(reader,writer) as session:
   await session.initialize()
   tools=await session.list_tools()
   pathlib.Path('research/mcp-tools.json').write_text(tools.model_dump_json(indent=2))
   print(json.dumps({'tools':[t.name for t in tools.tools]}),flush=True)
   if len(sys.argv)>1:
    calls=json.loads(pathlib.Path(sys.argv[1]).read_text())
    semaphore=asyncio.Semaphore(5)
    async def call(item):
     async with semaphore:
      name=item['id']
      try:
       out=await session.call_tool(item['tool'],item['arguments'])
       path=pathlib.Path('research/mcp',name+'.json');path.parent.mkdir(parents=True,exist_ok=True);path.write_text(out.model_dump_json(indent=2))
       text='\n'.join(c.text for c in out.content if hasattr(c,'text'))
       pathlib.Path('research/mcp',name+'.md').write_text(text)
       print(json.dumps({'id':name,'isError':getattr(out,'is_error',False),'chars':len(text)}),flush=True)
      except Exception as e:print(json.dumps({'id':name,'error':str(e)}),flush=True)
    await asyncio.gather(*(call(item) for item in calls))
asyncio.run(main())

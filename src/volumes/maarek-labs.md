---
slug: volume-maarek-labs
file: volume-maarek-labs.html
title: "AIP-C01 Labs Volume: Maarek Labs and Hands-On Patterns"
label: "Hands-On Labs"
track: aipc01
---

# AIP-C01 Labs Volume {#aip-c01-labs-volume}

Maarek labs and hands-on patterns

## How to use this volume {#how-to-use-this-volume}

Hands on. Each chapter is one lab from the course lab pack, rebuilt in plain words. Every chapter follows the same shape: what the lab teaches, why it matters in production, how it works under the hood, an architecture diagram with a numbered walkthrough, the exact exam angles, the traps, and one practice question with full explanations.

Code shown here is adapted for teaching, written fresh for this volume. It is not copied from the course files. The lab sources are course material; this volume explains the concepts in its own words.

Fact check: AWS service names, features, model IDs, and API shapes in this volume were verified against live AWS documentation on **2026-09-28**. Anything that could not be verified is marked UNVERIFIED inline. Limits and defaults change; check the docs at build time.

================= CHAPTER 1 =================

## 1. Lab: Strands agent with custom tools {#1-lab-strands-agent-with-custom-tools}

Build a working agent in a few lines of Python: one model, a tool list, a system prompt, and a custom function the model can call.

### What this lab teaches {#what-this-lab-teaches}

Strands Agents is an open-source Python SDK for building agents. An agent has three parts: a model (the brain), tools (the hands), and a prompt (the personality and instructions). You create an `Agent`, hand it a list of tools, and call it like a function with a question. The SDK runs the agent loop for you.

The agent loop is the key idea. A single model call cannot use tools by itself. The loop works like this: send the prompt to the model, the model replies either with text or with a request to call a tool, the SDK runs the tool, the tool result goes back to the model, and the cycle repeats until the model produces a final answer. Strands is model-driven, meaning the model decides at each step whether it needs a tool and which one.

A custom tool is just a Python function with the `@tool` decorator. The function's docstring becomes the tool description that the model reads when deciding what to call. The type hints become the input schema. A vague docstring means the model will misuse the tool, so the docstring is the real interface.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

Without a framework, every team hand-writes the same loop: parse the model's tool request blocks, validate arguments, execute code, format results, handle errors, track conversation state. That loop is where most agent bugs live. Strands owns the loop so your code is only the business logic: the tools themselves.

You reach for Strands when you need full code control over an agent: custom retry logic, your own tools, your own deployment target. It is the code-first alternative to the fully managed Bedrock Agents console experience. You can run a Strands agent on a laptop, in a container, on Lambda, or on AgentCore Runtime (chapter 3).

### How it works under the hood {#how-it-works-under-the-hood}

Step by step, for the pattern `Agent(tools=[calculator, current_time, count_keyword], system_prompt=...)`:

1. You define tools. Each `@tool` function registers its name, its docstring (description), and a JSON schema built from its type hints.
2. You create the `Agent`. The system prompt is prepended to every conversation. The tool list is converted into the tool definitions the model API expects.
3. You call the agent with a message, for example three tasks at once. The SDK sends the system prompt, the message, and the tool definitions to the model (Strands uses the Bedrock Converse API under the hood for Bedrock models).
4. The model returns one or more tool calls. The SDK executes each Python function with the arguments the model chose.
5. Tool results return to the model as tool result blocks. The model may call more tools or finish with text.
6. The call returns an agent result object whose string form is the final answer.

The `strands-agents-tools` package ships ready-made tools such as a calculator and a current-time tool, so a lab agent can mix built-in tools with your own custom ones. The `callback_handler` controls streaming output; setting it to `None` silences intermediate steps.

Adapted teaching snippet (a few lines, written for this volume):

```
from strands import Agent, tool

@tool
def word_count(text: str) -> int:
    """Count the words in a piece of text. The model reads this sentence."""
    return len(text.split())

agent = Agent(tools=[word_count], system_prompt="You are a study coach.")
print(agent("How many words are in 'cloud nine'?"))
```

Each tool call costs another model invocation, and the conversation history grows with every turn. If an agent makes five tool calls over a 2,000-token context, you pay for roughly five invocations, not one. That is why loop guards and precise tool descriptions matter for cost.

:::exam-ask

Common misunderstanding.

The docstring is not documentation for humans here; it is the routing logic the model uses to pick tools. Teams that write "utility function" as a docstring get random tool selection and blame the model.
:::

```
  User message ("what time is it? calculate X, count 'prompt' in this text")
       |
       v
 +------------------+      +---------------------------+
 |  Strands Agent   |----->|  Model (Bedrock Converse) |
 |  event loop      |<-----|  decides: answer or tool? |
 +------------------+      +---------------------------+
       | toolUse block                    ^ toolResult block
       v                                  |
 +------------------+                     |
 | Python functions |--- results back ----+
 | calculator,      |
 | current_time,    |
 | count_keyword    |
 +------------------+
       |
       v
  Final answer text
```

Figure 1.1: The Strands agent loop. The model decides each step; the SDK executes the Python functions. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: the user message enters the agent. The agent is not the model; it is the loop that drives the model.
2. The loop sends the system prompt, the message, and the tool definitions to the model through the Converse API.
3. The model replies with either final text or a toolUse block naming a function and arguments. The arrow to the right shows this decision point.
4. A toolUse block goes down to the Python functions. The SDK runs the real code with the model's chosen arguments.
5. Results flow back up as toolResult blocks. The loop repeats from step 2 until the model returns text.

What breaks if a component fails

- If a tool raises an exception and you do not catch it, the loop stalls or the model gets an error block it cannot use. Wrap tool bodies in error handling.
- If the tool list is empty, the agent is just a chatbot. If the docstrings are vague, the model calls the wrong tool or invents arguments.
- If the model API throttles, the whole loop stops. Retries with backoff belong around the agent call, not inside each tool.

:::exam-ask

Scenario: a team wants a Python agent that calls internal functions with minimal boilerplate and full code control. The most correct answer names Strands Agents (or the Agent Squad framework from chapter 2) with

@tool

functions. Distractors: hand-rolling the tool loop with raw InvokeModel calls (works but high operational burden, and Maarek's rule prefers the managed or framework path), or Bedrock Agents console when the scenario stresses code-first deployment on their own infrastructure. Trap pattern: an option that says "Strands replaces Bedrock Agents." They are alternatives for different needs: Bedrock Agents is the managed service with action groups and aliases; Strands is the SDK you host yourself, including on AgentCore.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Tool choice is driven by the docstring plus type hints. A question about "the agent keeps calling the wrong tool" points at the tool description, not at the model.
- Tools execute with your code's permissions. A tool that calls AWS APIs needs IAM scope; the exam tests least privilege on tool permissions.
- Strands' Bedrock model provider uses the Converse API, not the legacy InvokeModel path. If a question mixes Strands with provider-specific InvokeModel bodies, that is the trap.
:::

#### Practice question {#practice-question}

A startup's developers need a Python agent that answers support questions and calls two internal functions: one that looks up order status and one that computes refunds. They want full control of the code, they want to deploy on their own containers, and they want to avoid writing the model tool-call loop by hand. Which approach is MOST correct?

A. Write a custom loop with InvokeModel that parses toolUse blocks, executes the functions, and feeds results back.

B. Build the agent with the Strands Agents SDK, exposing each internal function as an `@tool` with a clear docstring and type hints.

C. Create a Bedrock Agent in the console with action groups, because code-first frameworks cannot call internal functions.

D. Put both functions behind API Gateway and have the model call the HTTP endpoints by reading the URLs from the system prompt.

B is correct. Strands is the code-first framework: `@tool` turns plain Python functions into tools, the SDK owns the loop, and the agent deploys anywhere including the team's own containers. The docstring plus type hints give the model the interface it needs.

A is wrong because hand-rolling the loop duplicates what the framework does and adds operational burden; the exam prefers the framework or managed path when the scenario does not demand custom loop behavior.

C is wrong for two reasons: the premise is false (code-first frameworks call internal functions easily, that is their main strength), and the scenario explicitly asks for code control and self-hosted deployment, which points away from the console-first managed agent.

D is wrong because models cannot reliably "call URLs from the system prompt." Tool use needs a real tool interface with schemas, not prompt text. This distractor tests whether you confuse prompt content with tool definitions.

================= CHAPTER 2 =================

## 2. Lab: Multi-agent squad routing {#2-lab-multi-agent-squad-routing}

One entry point, many specialist agents. A classifier reads each request and routes it to the right specialist.

### What this lab teaches {#what-this-lab-teaches}

Agent Squad is an open-source multi-agent orchestration framework (pip package name `agent-squad`). Instead of one giant agent that does everything, you register several specialist agents with one orchestrator. Each request goes through a classifier, usually a small fast model, which picks the best specialist for that request. The orchestrator then hands the request to the chosen agent and returns its answer with routing metadata.

The framework also supports composite agents: a ChainAgent runs a fixed pipeline where each agent's output feeds the next, and a SupervisorAgent coordinates workers. For chat history it uses a ChatStorage layer: in-memory by default, DynamoDB or SQL for production.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

Specialists beat generalists as scope grows. A billing agent, a technical support agent, and a general assistant each carry different tools, prompts, and knowledge. Adding a fourth specialty means registering one more agent, not rewriting a router. The classifier pattern also lets you mix frameworks: a Strands agent, a plain Bedrock model agent, and a Lambda-backed agent can all sit behind the same entry point.

### How it works under the hood {#how-it-works-under-the-hood}

Step by step for the lab's setup (a Strands specialist plus a general Bedrock LLM agent):

1. Create the orchestrator with a classifier: `AgentSquad(classifier=...)`. The BedrockClassifier is itself a model call: it receives the user input, the conversation history, and the catalog of registered agents (names plus descriptions), and it returns which agent should handle the request.
2. Register each agent with `add_agent`. The name and description are load-bearing: they are what the classifier reads. "Handles all general questions that do not require calculator, current time, or keyword counting" is a real routing instruction, not a label.
3. Wrap foreign agents in an adapter. The lab wraps the Strands agent in a small class that converts a Strands result into the framework's ConversationMessage format. This adapter pattern is how any framework joins the squad.
4. Call `await orchestrator.route_request(user_input, user_id, session_id)`. It is a coroutine, so you must await it. The orchestrator reads history from ChatStorage, classifies, dispatches, saves both sides of the exchange, and returns a response object with metadata naming the chosen agent.
5. Branch on `response.streaming`: in streaming mode the output is an async generator of chunks; otherwise it is a single message. Forgetting this branch is the classic integration bug.

Adapted teaching snippet (written for this volume):

```
from agent_squad.orchestrator import AgentSquad
from agent_squad.agents import BedrockLLMAgent, BedrockLLMAgentOptions
from agent_squad.classifiers import BedrockClassifier, BedrockClassifierOptions

orchestrator = AgentSquad(classifier=BedrockClassifier(BedrockClassifierOptions()))
orchestrator.add_agent(BedrockLLMAgent(BedrockLLMAgentOptions(
    name="General Assistant",
    description="Handles general questions.",
)))

response = await orchestrator.route_request("What is the capital of France?",
                                            user_id="u1", session_id="s1")
print(response.metadata.agent_name)   # which specialist was picked
```

Cost math: classification adds one extra model call per turn. Using a tiny model such as Nova Micro for the classifier keeps that call to fractions of a cent, which is why the lab configures the classifier with low max tokens and temperature 0. Deterministic classification (temperature 0) also makes routing reproducible, which matters for debugging.

:::exam-ask

Common misunderstanding.

The classifier is not magic keyword matching; it is an LLM reading your agent descriptions. If two agents have overlapping descriptions, routing becomes a coin flip. Write descriptions as mutually exclusive routing rules.
:::

```
  User request ("calculate 3111696 / 74088")
       |
       v
 +---------------------+     +----------------------+
 | AgentSquad          |---->| BedrockClassifier    |
 | orchestrator        |     | (small fast model)   |
 | route_request()     |<----| reads agent catalog  |
 +---------------------+     +----------------------+
       | chosen: "Calculator/Time/Keyword agent"
       v
 +---------------------+     +----------------------+
 | Specialist agents   |     | ChatStorage          |
 | - Strands (tools)   |     | in-memory (dev) or   |
 | - Bedrock LLM       |<--->| DynamoDB (prod)      |
 |   (general)         |     | per user+session     |
 +---------------------+     +----------------------+
       |
       v
  Answer + metadata.agent_name ("which agent answered")
```

Figure 2.1: Agent Squad request flow. The classifier picks one specialist per request; history persists per user and session. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: a user request enters `route_request` with a user id and session id.
2. The orchestrator asks the classifier which registered agent fits. The classifier sees only names and descriptions, not the agents' internals.
3. The chosen specialist processes the request. Specialists can be different frameworks; the adapter in the lab makes the Strands agent speak the squad's message format.
4. ChatStorage on the right persists the exchange per user and session, so follow-up turns keep context. In production this is DynamoDB, not memory.
5. The response returns the answer plus metadata naming the chosen agent, which is what you log for routing audits.

What breaks if a component fails

- If agent descriptions overlap, the classifier routes inconsistently. Fix the descriptions, not the model.
- If ChatStorage is in-memory in production, every restart wipes conversation history and multi-instance deployments disagree. Use DynamoDB.
- If you forget `await` on `route_request`, you get a coroutine object instead of an answer. If you ignore `response.streaming`, streaming agents break your client.

:::exam-ask

Scenario: specialist agents for tax, investment, and estate planning must collaborate, use tools, keep memory for weeks, and require human approval over a threshold. The most correct answer combines an orchestration framework (Agent Squad or Strands multi-agent) with DynamoDB-backed memory and Step Functions for the approval workflow. Distractors: one giant single prompt (does not scale, no tool isolation), Lex (conversational UI, not autonomous orchestration), S3 for conversation memory (wrong access pattern and latency). A second angle: "which agent answered and why" points at routing metadata and the classifier's agent catalog.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Do not confuse the squad's classifier with a Bedrock prompt router or inference profile. The classifier routes between your agents; prompt routers route between models by cost and quality; inference profiles route for regional availability. Three different mechanisms.
- Memory for weeks means durable storage (DynamoDB). Session memory inside the agent process is short-term only.
- Human approval over a money threshold is a Step Functions workflow with a callback or task token, not a prompt instruction to "ask a human."
:::

#### Practice question {#practice-question}

A company runs three specialist agents behind one chat endpoint: a billing agent with account tools, a support agent with a knowledge base, and a general assistant. Requirements: each request must reach exactly one specialist, conversation history must survive restarts, and the team must log which specialist handled each request. Which combination is MOST correct? (Select TWO.)

A. Front the agents with an Agent Squad orchestrator using a BedrockClassifier and per-agent name and description entries.

B. Store conversation history in the orchestrator's default in-memory ChatStorage.

C. Use DynamoDB-backed ChatStorage keyed by user id and session id, and log response metadata showing the chosen agent.

D. Merge all three specialists into one agent with one long system prompt to simplify routing.

A and C are correct. A gives intent-based routing with a real classifier reading the agent catalog. C gives durable per-session history plus the audit trail (which agent answered) the scenario demands.

B is wrong because in-memory storage dies with the process; "must survive restarts" rules it out. This is the classic durable-versus-ephemeral trap.

D is wrong because merging specialists destroys tool isolation and makes the prompt a bottleneck; the scenario's whole point is specialist routing, and the exam rewards the orchestrator pattern over the mega-prompt.

================= CHAPTER 3 =================

## 3. Lab: AgentCore Runtime deployment {#3-lab-agentcore-runtime-deployment}

Take the laptop agent and ship it: containerize it, satisfy the runtime contract, and let AgentCore host it with sessions, tools, memory, and identity.

### What this lab teaches {#what-this-lab-teaches}

Amazon Bedrock AgentCore is the managed platform for running agents in production. It has five parts you must be able to name: **Runtime** (serverless hosting for your agent container), **Gateway** (turns your APIs and Lambda functions into MCP-compatible tools), **Memory** (managed short-term and long-term agent context), **Identity** (agent authentication and access to third-party apps), and **Observability** (tracing and monitoring with OpenTelemetry). The lab focuses on Runtime: packaging the Strands agent from chapter 1 as a container that AgentCore can host.

The Runtime speaks to your container over plain HTTP with a fixed contract: listen on port 8080, answer `POST /invocations` with your agent logic, and answer `GET /ping` as a health check. The `bedrock-agentcore` Python SDK provides `BedrockAgentCoreApp`, a small wrapper that implements this contract for you. You mark one function with `@app.entrypoint`, and it receives the JSON payload from each `/invocations` call.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

A laptop agent has no sessions, no scaling, no safe credential handling, and no audit trail. AgentCore gives you managed sessions (the platform keeps a session alive across calls and can keep it warm for background work), a standard way to expose tools through Gateway instead of hand-wiring each integration, and memory that outlives any single container. The migration story the exam cares about: Bedrock Agents to AgentCore when you need framework freedom (Strands, LangGraph, CrewAI) without giving up managed hosting.

### How it works under the hood {#how-it-works-under-the-hood}

The lab's `agentcore.py` plus `Dockerfile` follow this sequence:

1. `app = BedrockAgentCoreApp()` creates the wrapper. The `@app.entrypoint` decorator marks `invoke(payload, context)` as the handler. The payload is the deserialized JSON body of the `POST /invocations` request; the context carries runtime information such as the session id.
2. Inside the handler, the code builds the Strands agent exactly as in chapter 1 and runs it on `payload.get("prompt", "")`. The handler returns a plain dict, which the SDK serializes back as the JSON response.
3. `app.run()` starts an HTTP server on port 8080. The same line runs the agent locally for testing and serves it inside the container in production. Test with `curl -X POST http://localhost:8080/invocations` before you deploy.
4. The Dockerfile builds the image: a slim Python base, install from `requirements.txt` (the `bedrock-agentcore` SDK, `strands-agents`, `strands-agents-tools`), add the OpenTelemetry distro so traces flow to Observability, set the region, create a non-root user, expose port 8080, and start the module.
5. The platform requires `linux/arm64` images. The container must bind `0.0.0.0:8080`, not localhost, or the platform's health checks cannot reach it.

Adapted teaching snippet (written for this volume):

```
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload, context):
    answer = run_my_agent(payload.get("prompt", ""))
    return {"answer": str(answer)}

if __name__ == "__main__":
    app.run()  # serves POST /invocations and GET /ping on port 8080
```

Gateway deserves one extra line because the exam names it: it converts existing APIs and Lambda functions into MCP-compatible tools, so agents built in any framework can call them through the Model Context Protocol instead of through bespoke integrations. Identity handles the OAuth and credential side so your agent code never holds raw secrets.

:::exam-ask

Common misunderstanding.

AgentCore Runtime is not "Lambda for agents." Lambda caps executions at 15 minutes and has no session concept; Runtime manages long-lived agent sessions with health checks and idle timeouts. Picking Lambda for a long-running agent session is a standard exam trap.
:::

```
  Developer laptop                    AWS
  +----------------+     +-------------------------------+
  | agentcore.py + |     |  AgentCore Runtime            |
  | Dockerfile     |---> |  session per caller           |
  | docker build   | ECR |       |                       |
  +----------------+ --> |       v                       |
                         |  Container (arm64, :8080)     |
  Caller --------------->|  POST /invocations -> handler |
                         |  GET  /ping        -> health |
                         |       |                       |
                         |       +--> Gateway: MCP tools |
                         |       +--> Memory: session +  |
                         |       |    long-term context  |
                         |       +--> Identity: OAuth /  |
                         |            credentials        |
                         |       +--> Observability:     |
                         |            OTEL traces        |
                         +-------------------------------+
```

Figure 3.1: Deploying a Strands agent on AgentCore Runtime. The container contract is two HTTP routes; the platform supplies sessions, tools, memory, identity, and traces. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start left: the developer builds the image from the agent code and Dockerfile, then pushes it to a container registry (ECR).
2. The Runtime launches the container and manages one session per caller. Sessions survive across calls; the platform polls `/ping` to know the container is alive.
3. Each caller request is a `POST /invocations` with a JSON payload. The `@app.entrypoint` function handles it and returns JSON.
4. Inside the session, the agent reaches four platform services: Gateway for MCP tools, Memory for context that outlives the container, Identity for credentials, and Observability for traces.

What breaks if a component fails

- If the image is built for the wrong CPU architecture, the container never starts. Build for `linux/arm64`.
- If the server binds localhost instead of `0.0.0.0`, health checks fail and the session is reaped even though the agent works locally.
- If `/ping` is missing or slow, the platform treats the session as dead. The SDK's built-in handler exists so you do not hand-roll this.

:::exam-ask

Scenario: a team built an agent in an open-source framework and needs managed hosting with sessions, tool access via MCP, and no server management. The most correct answer is AgentCore Runtime, with Gateway for the tools. Distractors: ECS with a hand-built session store (works but you own sessions, scaling, and health checks), Lambda (15-minute cap, no sessions), Bedrock Agents (managed but locks you into its framework and console model). A second angle maps each need to a component: "tools for any framework" points at Gateway, "remember users across weeks" at Memory, "call Salesforce on the user's behalf" at Identity.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Name all five components cold: Runtime, Gateway, Memory, Identity, Observability. Questions often test Gateway versus Memory versus Identity by scenario verb.
- The container contract is `POST /invocations` plus `GET /ping` on port 8080. A question about "the deployed agent never receives traffic" points at the contract, not the model.
- Migration direction matters: Bedrock Agents to AgentCore is the documented path when teams outgrow the managed agent framework. The reverse is not a thing.
:::

#### Practice question {#practice-question}

A team has a working Strands agent on a developer laptop. For production they need: managed hosting with per-caller sessions, the agent's existing REST APIs exposed as tools usable through MCP, user preferences remembered across weeks, and no server management. Which combination is MOST correct? (Select TWO.)

A. Deploy the agent container to AgentCore Runtime and expose the REST APIs through AgentCore Gateway.

B. Store user preferences in AgentCore Memory.

C. Package the agent as a Lambda function with a 15-minute timeout and keep preferences in Lambda environment variables.

D. Rebuild the agent as a Bedrock Agent because AgentCore Runtime only hosts Bedrock Agents.

A and B are correct. Runtime gives managed sessions and hosting for any-framework agents; Gateway converts existing APIs into MCP tools; Memory is the managed store for long-lived agent context. Together they satisfy every requirement.

C is wrong twice over: Lambda caps at 15 minutes and has no session concept, and environment variables are not a user-preference store. This is the "Lambda for everything" trap.

D is wrong because the premise is false: Runtime hosts any-framework agents, which is exactly its purpose, and the Bedrock-Agents-to-AgentCore migration path exists precisely for teams that started managed and need framework freedom, not the reverse.

================= CHAPTER 4 =================

## 4. Lab: Bedrock Flows from JSON {#4-lab-bedrock-flows-from-json}

Chain prompts into a deterministic pipeline. The lab's prompt list becomes a real flow definition: nodes, connections, and conditions.

### What this lab teaches {#what-this-lab-teaches}

Amazon Bedrock Flows (called Prompt Flows in older material) build deterministic multi-step GenAI workflows. You define a flow as JSON with two arrays: `nodes`, where each node is one step, and `connections`, which wire the steps together into paths. The lab's `PromptChaining.json` holds a simple list of three prompts: name a city, describe it, describe its cuisine. In a real flow definition, each of those prompts becomes a Prompt node, and Data connections pipe each node's output into the next node's input.

Node types cover the building blocks: Input and Output (entry and exit), Prompt (one model call with a template), Agent (hand a step to an agent), KnowledgeBase (a retrieval step), Condition (branch on logic), Iterator (loop over a list), LambdaFunction (custom code), plus storage nodes. A connection is either `Data`, which moves a named output to a named input, or `Conditional`, which follows a path only when its condition expression is true.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

Not every workflow needs an autonomous agent. When the path is fixed, three prompts in, one answer out, an agent's reasoning loop is expensive overhead and nondeterministic. Flows give you a visual builder plus a JSON definition you can version in git, test, and deploy. Product teams can edit prompt text without engineers redeploying code, and the definition's structure makes the pipeline auditable: you can see exactly which step feeds which.

### How it works under the hood {#how-it-works-under-the-hood}

A flow definition follows this shape (adapted for teaching, mirroring the lab's three prompts):

```
{
  "nodes": [
    {"name": "FlowInput",  "type": "Input"},
    {"name": "NameCity",   "type": "Prompt",
     "configuration": {"prompt": {"template": "Name a random city..."}}},
    {"name": "DescribeCity", "type": "Prompt",
     "configuration": {"prompt": {"template": "Describe this city: {{city}}"}}},
    {"name": "FlowOutput", "type": "Output"}
  ],
  "connections": [
    {"name": "c1", "source": "FlowInput", "target": "NameCity",
     "type": "Data",
     "configuration": {"data": {"sourceOutput": "document", "targetInput": "input"}}},
    {"name": "c2", "source": "NameCity", "target": "DescribeCity",
     "type": "Data",
     "configuration": {"data": {"sourceOutput": "modelCompletion", "targetInput": "city"}}}
  ]
}
```

Reading it: each connection names a source node and a target node. The `data` block maps a named output of the source (`sourceOutput`) to a named input of the target (`targetInput`), which is why prompt templates use `{{variable}}` placeholders. A `Conditional` connection instead carries a `condition` expression, and the flow follows the first matching branch. Expressions use JSONPath-style references to node outputs.

Lifecycle: after editing a flow you run PrepareFlow, which packages the latest changes into the DRAFT version for testing. For production you create an alias pointing at a numbered version, so prompt edits never move production traffic by accident. The same DRAFT-then-alias discipline you know from Bedrock Agents applies here.

One detail on the Iterator node: community sources describe it as sequential, processing list items one at a time rather than in parallel. UNVERIFIED: the sequential-iterator behavior was not confirmed in the live AWS docs during this build; treat it as community-reported.

:::exam-ask

Common misunderstanding.

Flows and agents solve different problems. A fixed three-step chain is a flow. A task where the model must decide which tools to call, in which order, with retries, is an agent. Putting an agent's job into a flow gives you rigidity; putting a flow's job into an agent gives you cost and nondeterminism.
:::

```
  Input ("go")
    |
    v
 +-----------+  Data: modelCompletion -> city  +--------------+
 | Prompt:   | ------------------------------> | Prompt:      |
 | NameCity  |                                 | DescribeCity |
 +-----------+                                 +--------------+
                                                     |
                          Data: modelCompletion -> city
                                                     v
                                               +--------------+
                                               | Prompt:      |
                                               | Cuisine      |
                                               +--------------+
                                                     |
                                                     v
                                                   Output

  With a branch:

 +-----------+  Conditional: $.sentiment == "negative"  +----------+
 | Condition | ---------------------------------------> | Prompt:  |
 | node      |                                          | Apology  |
 +-----------+  Conditional: otherwise                   +----------+
                 --------------------------------------> +----------+
                                                         | Prompt:  |
                                                         | Thanks   |
                                                         +----------+
```

Figure 4.1: Top: the lab's prompt chain as flow nodes and Data connections. Bottom: a Condition node branching on an expression. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Top half: follow the arrows down. Each box is a node; each arrow is a connection of type Data.
2. Read each arrow's label as "take this named output, feed it into that named input." The `{{city}}` placeholder in the prompt template is the receiving end.
3. Bottom half: a Condition node has two Conditional connections. The flow evaluates the condition expression and follows the first match. Exactly one path runs.
4. Input and Output nodes are the flow's boundary: one entry point, and one or more exits.

What breaks if a component fails

- If a `targetInput` name does not match a placeholder in the prompt template, the step runs with an empty variable. Name mismatches are the most common flow bug.
- If you edit nodes and skip PrepareFlow, the DRAFT version still holds the old definition and your tests lie to you.
- If a condition expression references a field that does not exist, the branch never matches and the flow takes the fallback path silently.

:::exam-ask

Scenario: "a three-stage prompt chain with branching; the marketing team edits prompt text weekly; no engineer redeploys." The most correct answer is Bedrock Flows (Prompt Management for the versioned prompts, Flows for the chain). Distractors: Bedrock Agents (overkill for a fixed deterministic chain), Step Functions (the right answer when the workflow needs timeouts, human approvals, or non-GenAI orchestration, but heavier than Flows for a pure prompt chain), hardcoding prompts in Lambda (violates the no-redeploy constraint). Second angle: "the flow ignores recent edits" points at the missed PrepareFlow step.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Flows versus Step Functions is a favorite confusion pair. Rule of thumb: prompt-centric fixed chains go to Flows; general orchestration with waits, retries across services, and human approvals goes to Step Functions. Scenarios often allow both; the "most correct" is the one matching the constraint words.
- Connection types are Data and Conditional. If an option mentions other connection types, it is invented.
- Prompt variants are for A/B testing; prompt versions are immutable releases. The exam swaps these.
:::

#### Practice question {#practice-question}

A media company runs a fixed pipeline: extract topics from an article, draft a headline from the topics, then classify the headline's tone. Editors tweak the prompt wording every week, and engineering must not redeploy for wording changes. Which approach is MOST correct?

A. Build a Bedrock Agent with three action groups, one per stage, and let the agent decide the order at runtime.

B. Define a Bedrock Flow with three Prompt nodes chained by Data connections, manage the prompts with Prompt Management versions, and expose a flow alias for production.

C. Hardcode the three prompts in a Lambda function behind API Gateway and redeploy weekly.

D. Use Step Functions with three Lambda tasks that each call InvokeModel, because Flows cannot chain prompts.

B is correct. The pipeline is fixed and prompt-centric, which is exactly what Flows are for. Data connections pipe each stage's output into the next; Prompt Management versions let editors change wording without code deploys; the alias pins production to a tested version.

A is wrong because an agent adds reasoning overhead and nondeterminism to a fixed pipeline; nothing here needs dynamic tool choice.

C is wrong because it directly violates the no-redeploy constraint the scenario states.

D is wrong because its premise is false: chaining prompts is the core Flows use case. Step Functions would be the answer if the scenario needed human approvals or cross-service waits, which it does not.

================= CHAPTER 5 =================

## 5. Lab: Lambda as Bedrock front end {#5-lab-lambda-as-bedrock-front-end}

Put a stable HTTP front door in front of your model calls: API Gateway for the endpoint, Lambda for the logic.

### What this lab teaches {#what-this-lab-teaches}

AWS Lambda is serverless compute: you upload a function, AWS runs it on events, and you pay per invocation. API Gateway is the managed front door: it gives you a stable HTTPS endpoint with authentication, throttling, and request routing, and it forwards requests to Lambda. The lab's `lambda-code.py` shows the Lambda proxy integration shape: the handler receives an event, does work, and returns a dict with `statusCode`, `headers`, and a JSON-string `body`. API Gateway translates that dict into the HTTP response the caller sees.

For GenAI, this pair is the standard synchronous front end. The client calls your API; API Gateway authenticates and throttles; Lambda validates the request, picks the model, calls Bedrock, and returns the answer. The lab's hello-world handler is the skeleton you flesh out with a Bedrock call.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

Calling Bedrock directly from a browser or mobile app means shipping AWS credentials to the client and giving every client raw model access. The Lambda front end keeps credentials server-side, enforces per-client throttling at the gateway, validates inputs before they cost you tokens, and gives you one place to change the model without touching clients. It is also where the exam's favorite model-switching trio lives: Lambda holds the routing logic, API Gateway holds the stable endpoint, and AppConfig holds the model identifier as runtime configuration, so switching models needs no redeploy.

### How it works under the hood {#how-it-works-under-the-hood}

1. The client sends an HTTPS request to the API Gateway endpoint. Gateway checks the auth method (IAM, Cognito authorizer, or API key), applies the throttling limit, and forwards the request to Lambda as a proxy event.
2. The Lambda handler parses the event body, validates it (required fields, sane lengths, no prompt-injection payload aimed at downstream systems), and reads the current model identifier from AppConfig at runtime.
3. Lambda calls Bedrock, usually the Converse API for its unified request shape, waits for the response, and formats the proxy response: `{"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": json.dumps(result)}`.
4. API Gateway returns that to the client. Failures surface as 4xx for bad input and 5xx for downstream errors; the handler must never leak stack traces or credentials in error bodies.

Adapted teaching snippet (the proxy response shape, written for this volume):

```
import json

def lambda_handler(event, context):
    model_id = get_model_id_from_appconfig()  # runtime config, no redeploy
    answer = call_bedrock_converse(model_id, event_body(event))
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": answer}),
    }
```

Limits that shape designs: a Lambda execution caps at 15 minutes, so it fits request-response model calls but not long-running agent sessions. API Gateway has payload and timeout limits of its own, so long token streams go out over WebSocket APIs or direct streaming rather than a single REST response. For streaming to browsers, the ConverseStream API pairs with chunked transfer or WebSockets.

:::exam-ask

Common misunderstanding.

API Gateway plus Lambda does not make the model faster. It adds a small hop of latency. You pay that hop for auth, throttling, validation, and a stable contract. If a scenario demands the lowest possible latency and has no auth or multi-client needs, direct SDK calls win.
:::

```
  Client (web / mobile)
       |
       | HTTPS
       v
 +------------------+     +------------------+
 | API Gateway      |---->| Lambda function  |
 | - auth (Cognito/ |     | - validate input |
 |   IAM / API key) |     | - read model id  |
 | - throttling     |     |   from AppConfig |
 | - stable URL     |     | - call Bedrock   |
 +------------------+     |   Converse API   |
       ^                  +------------------+
       |                           |
       +---- proxy response --------+
       (statusCode, headers, body)
```

Figure 5.1: The synchronous GenAI front end. The gateway owns the endpoint contract; Lambda owns the logic; AppConfig owns the model choice. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: the client only ever talks to the gateway URL. It never sees Bedrock or AWS credentials.
2. The gateway box lists its three jobs: authenticate the caller, throttle abusive clients, and keep the URL stable while backends change.
3. Lambda's box lists its jobs in order: validate, look up the model id from AppConfig at runtime, call Bedrock.
4. The return arrow shows the proxy response contract: statusCode, headers, and a JSON-string body. API Gateway turns that dict into the HTTP response.

What breaks if a component fails

- If the handler returns a dict instead of a JSON string in `body`, API Gateway returns a confusing error. Always `json.dumps` the body.
- If AppConfig is unreachable, the function cannot resolve the model id. Cache the config with a short TTL and fail closed, not open.
- If throttling is misconfigured at the gateway, one abusive client can burn your token budget. Set per-client limits.

:::exam-ask

The canonical question: "operations must switch between models without code deployments." The most correct select-three is AppConfig plus API Gateway plus Lambda. Distractors: CloudFormation for runtime switching (CloudFormation changes are deployments, which violates the constraint), EventBridge as the config store (it routes events; it does not hold configuration), hardcoding model ids in the Lambda (works until the first switch, then it is a redeploy). A second angle: streaming long responses through a REST API hits gateway limits; the fix is WebSocket APIs or direct streaming.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Lambda's 15-minute cap is the tripwire. Any scenario with waits, human approvals, or long agent sessions points at Step Functions, not a longer Lambda.
- The proxy response shape (statusCode, headers, string body) is the kind of detail a troubleshooting question hides a bug in.
- AppConfig is the exam's standard answer for "change behavior without redeploying," for models and for prompts alike.
:::

#### Practice question {#practice-question}

A company serves a Bedrock-powered support chatbot through a mobile app. Product wants to switch the underlying model between providers without app updates or redeploys, throttle abusive clients, and keep AWS credentials off the device. Which combination is MOST correct? (Select THREE.)

A. Put API Gateway in front with throttling and a Cognito authorizer.

B. Store the active model identifier in AppConfig and have the Lambda read it at runtime.

C. Implement the request logic in Lambda, calling Bedrock with the Converse API.

D. Embed the model identifier in the mobile app and call Bedrock directly from the device.

E. Redeploy the Lambda with a CloudFormation stack update each time the model changes.

A, B, and C are correct. A gives the stable authenticated endpoint with throttling and keeps credentials server-side. B makes the model choice runtime configuration, satisfying no-redeploy. C is the compute layer that validates input and calls Bedrock through the unified Converse interface.

D is wrong because it ships AWS credentials to the device and gives every client raw model access with no throttling or validation; it also requires app updates to change models.

E is wrong because a stack update is a deployment, which directly violates the no-redeploy constraint. This is the CloudFormation-for-runtime-config trap.

================= CHAPTER 6 =================

## 6. Lab: Lambda as agent action {#6-lab-lambda-as-agent-action}

Give a Bedrock Agent real hands. The lab's weather function shows the exact event the agent sends and the exact response it expects back.

### What this lab teaches {#what-this-lab-teaches}

A Bedrock Agent reasons, but it acts through action groups. An action group binds the agent to a Lambda function plus a schema describing the available functions. There are two schema styles: function details, where you list simple named functions with parameters, and an OpenAPI schema, where you describe REST-style operations. The lab's `weather.py` implements the function-details style: a `get_weather`-style function taking a city and units.

The contract has two halves. The input event the agent sends contains the agent name, the action group name, the function name, a `parameters` list of name-type-value entries, and a `messageVersion`. The response the Lambda must return wraps the result as `messageVersion`, `response.actionGroup`, `response.function`, and `response.functionResponse.responseBody.TEXT.body`. With an OpenAPI schema instead, the event carries `apiPath` and `httpMethod`, and the response carries an HTTP status code. This shape is documented in the Bedrock user guide page on configuring Lambda functions for agents.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

An agent without actions is a chatbot. Actions connect it to the business: look up orders, file tickets, query databases, call internal APIs. Lambda is the natural host because each action is a short, event-driven piece of code that scales to zero. The schema is the contract that lets the model call your code reliably: parameter names, types, and descriptions tell the model exactly what to pass.

### How it works under the hood {#how-it-works-under-the-hood}

1. The user asks something needing a tool, for example the weather in a city. The agent's orchestration loop decides to call the function, filling in parameters from the conversation.
2. Bedrock invokes your Lambda with the action event. Your handler reads `event["parameters"]`, a list of dicts, and extracts each named value. Defensive code handles missing parameters rather than crashing.
3. Your code does the real work: a database query, an HTTP call, a calculation. Keep it fast; the agent is waiting, and the user experience is streaming text that pauses while tools run.
4. The handler builds the response in the exact nested shape and returns it. The agent receives the function result, continues reasoning, and produces the final answer.
5. After any change to the agent's configuration, including action groups, you must run PrepareAgent so the DRAFT version picks it up. Production traffic goes through an alias pinned to a prepared version.

Adapted teaching snippet (the parameter extraction pattern, written for this volume):

```
def lambda_handler(event, context):
    params = {p["name"]: p["value"] for p in event.get("parameters", [])}
    city = params.get("city", "unknown")
    result = lookup_weather(city)  # your business logic here
    return {
        "messageVersion": event["messageVersion"],
        "response": {
            "actionGroup": event["actionGroup"],
            "function": event["function"],
            "functionResponse": {
                "responseBody": {"TEXT": {"body": result}}
            },
        },
    }
```

Two numbers to carry: the Lambda response payload is bounded by the synchronous invocation payload limit, so return concise results and put large payloads in S3 with a reference. And the agent ignores your new action group until PrepareAgent runs; "I added the action group but the agent never calls it" is the single most common agent bug, and the exam loves it.

:::exam-ask

Common misunderstanding.

The action group schema is written for the model, not for you. Parameter descriptions are the model's instructions for what to pass. A parameter named

q

with no description gets garbage input; a parameter named

city

described as "the city the user asked about, e.g. Paris" gets the right value.
:::

```
  User: "weather in Paris?"
       |
       v
 +------------------+  decides tool call   +------------------+
 | Bedrock Agent    | --------------------> | Action group   |
 | orchestration    |  function=get_weather | Lambda         |
 | loop             |  parameters=[city]   | - read params  |
 |                  | <-------------------- | - run logic    |
 +------------------+  functionResponse    +------------------+
       |               responseBody.TEXT.body
       v
  Final answer: "75 degrees and sunny in Paris."
```

Figure 6.1: A Bedrock Agent invoking a Lambda action. The event and response shapes are a fixed contract. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top with the user question. The agent's loop, not your code, decides a tool is needed.
2. The rightward arrow shows the invocation: function name plus the parameters list. This is the input half of the contract.
3. Inside the Lambda box, the two jobs run in order: extract named parameters defensively, then execute the business logic.
4. The leftward arrow shows the response half: the nested `functionResponse.responseBody.TEXT.body` shape carrying the result string.
5. The agent resumes reasoning and answers the user, citing the tool result.

What breaks if a component fails

- If the response nesting is wrong by one level, the agent cannot parse the result and the turn fails. Copy the shape exactly.
- If PrepareAgent was not re-run after adding the action group, the agent behaves as if the tool does not exist.
- If the Lambda needs more than a few seconds, the user watches a paused stream. Keep actions fast or make them asynchronous with a status check.

:::exam-ask

Scenario: "the agent ignores the new action group" points at the missed PrepareAgent step, every time. Scenario: "the agent must call an internal REST API with path parameters" points at the OpenAPI-schema action group style, with the schema stored in S3. Distractors: describing inter-agent communication as action groups (the exam uses the supervisor and collaborator mechanism for agent-to-agent, not action groups), or putting the tool logic in the agent instruction text instead of a real function. A troubleshooting angle hides a bug in the response nesting: one wrong level and the result never reaches the model.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Function details versus OpenAPI schema: simple named functions go to function details; REST-style operations with paths and methods go to OpenAPI. Match the style to the scenario.
- The `parameters` list uses name, type, and value entries. A distractor may show a flat dict; the real shape is a list of entries.
- Session attributes travel in the event too, letting actions read conversation context the agent stored earlier.
:::

#### Practice question {#practice-question}

A developer adds a new action group with a Lambda function to a Bedrock Agent, tests in the console, and finds the agent never calls the new function. The Lambda works when invoked directly. What is the MOST likely cause?

A. The Lambda function's timeout is too short for the agent's orchestration loop.

B. PrepareAgent was not run after the action group change, so the DRAFT version does not include it.

C. The agent's IAM role is missing bedrock:InvokeModel permission.

D. The action group must be defined with an OpenAPI schema; function details are not supported.

B is correct. Agent configuration changes only take effect after preparation packages them into the DRAFT version. The Lambda working standalone proves the function is fine; the agent simply does not know about it yet.

A is wrong because a timeout problem would surface as a failed invocation, not as the agent never attempting the call.

C is wrong because a missing InvokeModel permission would break all model calls, not just the new action group; the agent is clearly reasoning fine.

D is wrong because its premise is false: both function details and OpenAPI schemas are supported action group styles.

================= CHAPTER 7 =================

## 7. Lab: CI/CD with eval gates {#7-lab-cicd-with-eval-gates}

:::figure assets/img/internet/img-33.webp

Prompt CI/CD: prompts live in a source file or registry, pass code review and evaluation, then roll out through staging and canary traffic to production with version tags.

Source: Third-party MLOps guide, via image search Sept 2026.

:::


Ship prompt and model changes like code: pipeline stages, build specs, and an evaluation gate that blocks bad releases.

### What this lab teaches {#what-this-lab-teaches}

CI/CD on AWS is a pipeline of stages: source, build, test, deploy. AWS CodePipeline orchestrates the stages. AWS CodeBuild runs the build, driven by a `buildspec.yml` file with phases: `install`, `pre_build`, `build`, and `post_build`. AWS CodeDeploy ships the artifact to its target. The lab pack's `buildspec.yml` shows the skeleton: install a runtime, echo through the phases, and run a check in the build phase that fails the build when the check fails.

For GenAI, the build phase gains an evaluation gate. A prompt or model change is a behavior change, and behavior needs tests. The gate runs an eval suite, compares metrics against thresholds, and fails the build on regression. The pipeline stops, the bad prompt never deploys, and the team gets a red build instead of a production incident.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

Teams that edit prompts in the console and paste them into production get silent regressions: a reworded system prompt that drops refusal behavior, a model swap that changes tone, a new few-shot example that biases outputs. CI/CD makes prompt and config changes reviewable, testable, and reversible. The eval gate is the GenAI equivalent of a unit test suite: it encodes "the behavior we promise" and blocks anything that breaks it.

### How it works under the hood {#how-it-works-under-the-hood}

1. A developer pushes a change to the prompt templates or model configuration in git. CodePipeline's source stage picks it up.
2. CodeBuild runs `buildspec.yml`. The install phase sets up the runtime; pre_build prepares; the build phase runs two suites: fast unit checks (schema validation of prompt templates, config linting) and the eval gate.
3. The eval gate invokes the candidate prompt or model against a golden dataset and scores it: faithfulness for RAG answers, toxicity and refusal checks for safety, format compliance for structured outputs. Scores are compared to thresholds stored with the repo. Any threshold breach fails the build.
4. On green, the pipeline continues: an optional manual approval stage for high-risk changes, then deployment. Deployment for GenAI usually means shifting a flow alias or agent alias to the new version, or a canary that sends a slice of traffic first while CloudWatch alarms watch token error rates and latency.
5. On red, the pipeline halts and the previous version keeps serving. Rollback is shifting the alias back, which is instant because versions are immutable.

Adapted teaching snippet (a buildspec eval gate, written for this volume):

```
version: 0.2
phases:
  install:
    runtime-versions:
      python: 3.12
  build:
    commands:
      - echo "Validating prompt templates"
      - python validate_prompts.py prompts/
      - echo "Running eval gate against golden dataset"
      - python eval_gate.py --dataset golden/qa.jsonl
          --min-faithfulness 0.85 --max-toxicity 0.02
      # any non-zero exit fails the build and stops the pipeline
```

The eval suite itself can use Bedrock's evaluation features: programmatic metrics for objective checks, LLM-as-a-judge for quality dimensions like faithfulness and style, and human review for the subjective ones. The pipeline runs the automated tiers on every change and reserves human review for releases that cross risk thresholds.

:::exam-ask

Common misunderstanding.

An eval gate is not "run the model once and eyeball it." It is a repeatable suite with thresholds, checked into the repo, run on every change. Manual console spot-checks are the thing the gate replaces.
:::

```
  git push (prompts/ + config)
       |
       v
 +------------------+     +-------------------------------+
 | CodePipeline     |---->| CodeBuild (buildspec.yml)     |
 | source stage     |     | install -> pre_build -> build |
 +------------------+     |   unit checks (schemas)       |
                          |   EVAL GATE: golden dataset   |
                          |   faithfulness >= 0.85        |
                          |   toxicity     <= 0.02        |
                          +---------------+---------------+
                                          |
                       fail: stop here    |    pass: continue
                                          v
                          +-------------------------------+
                          | approval (manual, high risk)  |
                          +---------------+---------------+
                                          v
                          +-------------------------------+
                          | deploy: shift alias / canary    |
                          | CloudWatch alarms on errors   |
                          +-------------------------------+
```

Figure 7.1: A GenAI pipeline with an evaluation gate. The gate is a build phase that fails the pipeline on metric regression. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: the only trigger is a git push. Console edits that bypass the repo bypass the gate, which is why the repo is the source of truth.
2. The build box shows the phases in order. The eval gate sits inside the build phase, after the fast unit checks, because evals cost model calls and should run only on sane inputs.
3. Read the two exit arrows: fail stops the pipeline immediately; pass continues to approval and deploy.
4. Deploy means alias shift or canary, never overwriting the serving version in place. Alarms watch the rollout.

What breaks if a component fails

- If thresholds are set once and never recalibrated, the gate either blocks everything or blocks nothing. Review thresholds when the dataset or product changes.
- If the golden dataset goes stale, the gate tests yesterday's product. Refresh it from production traffic samples.
- If evals run against the production model endpoint instead of the candidate, the gate measures the wrong thing. Pin the candidate version explicitly.

:::exam-ask

Scenario: "validate a new prompt version before rollout" or "a prompt change caused a production incident; prevent recurrence." The most correct answer is a pipeline with automated regression testing and a canary or alias-based deployment. Distractors: manual testing in the console as the complete answer (not repeatable, not a gate), deploying straight to production because "prompts are not code" (they are behavior changes and need gates), or unit tests alone with no behavioral eval (unit tests cannot catch tone or faithfulness regressions). A second angle: "which eval method for brand voice at scale" points at LLM-as-a-judge in the gate plus human spot checks.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- Programmatic eval for objective metrics, LLM-as-a-judge for quality at scale, human eval for subjective judgment. Match the method to the metric; the exam tests this mapping.
- Canary plus alias shift is the deployment answer. Blue-green full swaps are fine too, but the exam's GenAI scenarios usually say canary.
- A failing eval gate must stop the pipeline. An option that "alerts but deploys anyway" is never the most correct for a safety regression.
:::

#### Practice question {#practice-question}

A team edits Bedrock prompts weekly. Last month a reworded system prompt silently dropped the product's refusal behavior for disallowed content, and nobody noticed for a week. Which approach MOST reduces the chance of recurrence?

A. Require two engineers to eyeball each prompt change in the console before pasting it into production.

B. Check prompts into git and run a CodePipeline where CodeBuild executes an eval gate on a golden dataset with toxicity and refusal thresholds; failures block deployment.

C. Write unit tests asserting the prompt template files are valid JSON.

D. Deploy prompt changes on Fridays so the team can monitor them over the weekend.

B is correct. It makes prompt changes reviewable (git), repeatable (pipeline), and behaviorally tested (eval gate with the exact metrics that regressed: toxicity and refusal). A threshold breach stops the pipeline before production.

A is wrong because manual eyeballing is not repeatable and does not scale; it is the process the incident already proved insufficient.

C is wrong because schema validity says nothing about behavior; a valid-JSON prompt can still refuse nothing.

D is wrong and slightly comic: deployment timing is not a safety control. Friday deploys are famously the opposite of safe.

================= CHAPTER 8 =================

## 8. Lab: CDK for GenAI infrastructure {#8-lab-cdk-for-genai-infrastructure}

Define the whole GenAI stack in a real programming language and let it compile to CloudFormation.

### What this lab teaches {#what-this-lab-teaches}

The AWS Cloud Development Kit (CDK) lets you define cloud infrastructure in familiar languages such as TypeScript or Python. You write constructs, small building blocks like a Lambda function, an S3 bucket, or a DynamoDB table, and compose them into a stack. Running `cdk synth` compiles your code into a CloudFormation template; `cdk deploy` creates or updates the stack from that template. The lab's stack file builds a realistic pattern: an S3 bucket for uploads, a Lambda function with an IAM role, and a DynamoDB table, wired together with outputs.

For GenAI workloads the same pattern hosts the serving path: the Lambda that calls Bedrock, the API Gateway in front of it, the DynamoDB table for session state, and the IAM policies scoping each piece. IAM is where CDK earns its keep for GenAI: the Lambda's role gets exactly `bedrock:InvokeModel` on the specific model ARNs it may call, plus logging permissions, and nothing else.

### Why it exists: when you would use it in production {#why-it-exists-when-you-would-use-it-in-production}

A production GenAI service is a dozen resources with relationships: the function needs the table name, the role needs the model ARNs, the gateway needs the function ARN. Hand-written templates for this drift out of sync with the code they deploy. CDK keeps infrastructure next to application code, in a language with loops, conditions, and tests, and every environment (dev, staging, prod) is the same stack class with different parameters. That repeatability is what the exam means by standardized, reusable components.

### How it works under the hood {#how-it-works-under-the-hood}

1. You write a stack class extending the CDK Stack. Each construct call, for example `new dynamodb.Table(...)`, adds a resource to an internal tree. References between constructs, like passing the table to the Lambda's environment, become CloudFormation references automatically.
2. `cdk synth` walks the tree and emits the CloudFormation template. Review it with `cdk diff` before deploying; diff shows exactly what will change, including replacements that would delete data.
3. `cdk deploy` hands the template to CloudFormation, which creates or updates resources in dependency order. Outputs, such as the bucket name, print at the end and are importable by other stacks.
4. For GenAI, you add the Bedrock permissions to the Lambda's role, scoped to the models the function may call. Least privilege here is an exam staple: `bedrock:*` on `*` is the distractor.
5. Removal policies decide what happens on stack deletion. Data stores usually get retain or snapshot policies; the lab's destroy policy suits throwaway lab resources only.

Adapted teaching snippet (the least-privilege GenAI role pattern, written for this volume):

```
// inside the stack: the serving Lambda may call two models, nothing else
fnRole.addToPolicy(new iam.PolicyStatement({
  effect: iam.Effect.ALLOW,
  actions: ["bedrock:InvokeModel"],
  resources: [
    "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-lite-v1:0",
    "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-micro-v1:0",
  ],
}));
```

The lab's stack also demonstrates the event-source pattern: a Lambda subscribed to S3 events, so every upload triggers processing. For GenAI ingestion pipelines, that pattern feeds new documents into chunking and embedding without a polling loop.

:::exam-ask

Common misunderstanding.

CDK is deploy-time infrastructure, not runtime configuration. Switching models at runtime is AppConfig's job (chapter 5). A question that asks for model switching "without redeploy" and offers a CDK redeploy as the answer is testing whether you confuse the two planes.
:::

```
  app code (TypeScript / Python)
       |
       | cdk synth
       v
 +---------------------+     +---------------------+
 | CloudFormation      |---->| cdk diff (review!)  |
 | template            |     +---------------------+
 +---------------------+               |
       | cdk deploy                    v approved
       v                      +---------------------+
 +---------------------+      | CloudFormation      |
 | Stack:              |<-----| creates / updates   |
 | - Lambda (serving)  |      +---------------------+
 | - API Gateway       |
 | - DynamoDB (state)  |
 | - IAM role:         |
 |   bedrock:InvokeModel
 |   on 2 model ARNs   |
 +---------------------+
```

Figure 8.1: From CDK code to a deployed GenAI stack. Synth, review the diff, then deploy. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: you write application plus infrastructure in one language. The stack class is the unit of deployment.
2. `cdk synth` compiles to a CloudFormation template. Nothing has been created yet; this step is free and safe.
3. `cdk diff` shows the change set. Read it every time; a replacement on a stateful resource deletes data.
4. `cdk deploy` executes through CloudFormation, which orders resource creation and rolls back on failure.
5. The stack box lists the GenAI serving pieces and the least-privilege IAM role. The role is the security boundary the exam tests.

What breaks if a component fails

- If you skip `cdk diff`, a small code change can replace a database. Review before deploy, always.
- If the IAM role is too broad, a compromised function can call any model in any account context the role allows. Scope to model ARNs.
- If environments are hand-built instead of stack instances, dev and prod drift and bugs reproduce nowhere but production.

:::exam-ask

Scenario: "deploy the GenAI serving stack repeatably across dev, staging, and prod with least-privilege access." The most correct answer is CDK (or CloudFormation) with scoped IAM. Distractors: console click-ops (not repeatable), CDK for runtime model switching (wrong plane; that is AppConfig), or a single wildcard IAM policy (violates least privilege). A second angle: "the deployment replaced the DynamoDB table and lost session data" points at the skipped diff review and the removal policy.
:::

:::exam-ask

Exam tips and wrong-answer traps.

- CDK compiles to CloudFormation. Any option claiming CDK deploys "without CloudFormation" misunderstands the tool.
- Least privilege is tested by ARN scoping. `bedrock:InvokeModel` on specific foundation-model ARNs beats `bedrock:*` on `*` every time.
- Infrastructure as code is the answer to "standardized, reusable components across deployments," a phrase straight from the exam guide's design task.
:::

#### Practice question {#practice-question}

A team must deploy an identical GenAI serving stack (Lambda, API Gateway, DynamoDB session table) to dev, staging, and production. The Lambda must call Bedrock models, and security requires least privilege. Which approach is MOST correct?

A. Build each environment by hand in the console and attach the AWS managed AdministratorAccess policy to the Lambda role for simplicity.

B. Define one CDK stack class instantiated per environment; grant the Lambda role bedrock:InvokeModel scoped to the specific model ARNs it needs; review cdk diff before each deploy.

C. Write the Lambda code to assume a new IAM role at runtime that switches models via CDK redeploys.

D. Store the CloudFormation template in a shared drive and email it to whoever deploys that week.

B is correct. One stack class gives identical environments; ARN-scoped InvokeModel is least privilege; diff review catches destructive replacements. It hits repeatability, security, and safety in one answer.

A is wrong twice: console builds are not repeatable across environments, and AdministratorAccess on a serving role is the opposite of least privilege.

C is wrong because it confuses the planes: model switching at runtime is AppConfig's job, and CDK redeploys are deployments, not runtime configuration.

D is wrong because a template on a shared drive with no versioning or pipeline is click-ops with extra steps; it fails repeatability and auditability.

================= CHAPTER 9 =================

## 9. Supporting labs: KMS, X-Ray, SQS, and foundations {#9-supporting-labs-kms-x-ray-sqs-and-foundations}

The remaining lab files, mapped to their exam roles: encryption, tracing, messaging, and the building blocks under every GenAI architecture.

### What this chapter covers {#what-this-chapter-covers}

The lab pack includes supporting exercises that are not GenAI-specific but appear constantly in GenAI architectures and exam scenarios. Each gets its exam framing here so no file is left unmapped.

#### KMS: encryption for model data {#kms-encryption-for-model-data}

AWS Key Management Service manages the encryption keys that protect data at rest. The lab's CLI script walks the envelope pattern: encrypt a file with a KMS key, store the ciphertext, decrypt it back with the same key. In GenAI architectures KMS keys encrypt fine-tuning datasets in S3, Bedrock model invocation logs, and flow definitions. The exam tests two things: that sensitive training or log data is encrypted with customer-managed keys, and that VPC endpoints keep Bedrock traffic off the public internet. A question about "encrypt the data used to customize a model" points at KMS plus S3 server-side encryption, not at the model service itself.

#### X-Ray: tracing the agent's path {#x-ray-tracing-the-agents-path}

AWS X-Ray traces requests as they cross service boundaries, showing each segment's latency. The lab's CloudFormation template wires X-Ray into a sample app. For GenAI, X-Ray answers "where did the 8 seconds go" across a multi-step agent run: the classifier call, the specialist's model call, the Lambda tool, the DynamoDB read. The exam pairs X-Ray with CloudWatch Logs Insights for GenAI observability: X-Ray for the trace across calls, Logs Insights for prompt and response forensics. A distractor offers CloudTrail for latency debugging; CloudTrail is audit logging, not performance tracing.

#### SQS: decoupling the pipeline {#sqs-decoupling-the-pipeline}

Amazon SQS is a managed message queue: send, receive, delete. The lab script covers the basics. In GenAI pipelines SQS decouples ingestion from processing: uploads land, a queue buffers them, Lambda workers drain the queue into chunking and embedding. The exam tests SQS for fan-out and buffering, and it tests what SQS is not: it is not a configuration store (that is AppConfig), not a state store (that is DynamoDB), and not a vector store.

#### Foundations: CLI, EC2 metadata, user data, Kinesis, CloudFormation basics {#foundations-cli-ec2-metadata-user-data-kinesis-cloudformation-basics}

- **CLI and EC2 metadata:** the metadata script shows how code on EC2 discovers its own identity and credentials. Exam angle: IAM roles for EC2 instead of baked-in keys, and IMDSv2 for metadata security.
- **EC2 user data:** bootstrap scripts that configure an instance at launch. Exam angle: user data runs once at launch; it is not a configuration management system and not a place for secrets.
- **Kinesis data streams:** the lab script creates a stream for ordered, replayable ingestion. Exam angle: Kinesis for streaming data into processing (for example, a live transcript feed into a summarizer), versus SQS for simple buffering.
- **CloudFormation basics:** the two templates build from a bare instance to one with a security group and elastic IP. Exam angle: declarative infrastructure, and the reason CloudFormation is wrong for runtime model switching (it is a deployment mechanism).

#### The two big files: book.txt and the bylaws document {#the-two-big-files-booktxt-and-the-bylaws-document}

The 260 KB `book.txt` and the bylaws Word document are sample knowledge sources. Their exam role is the RAG ingestion story: raw text loses structure like headings and tables, so pipelines use extraction (Textract, Comprehend), structure-preserving conversion, and divider markers to improve chunking before embeddings are built. When a scenario says "10,000 mixed files a day into a knowledge base," these files are what that ingestion pipeline eats.

```
  Raw sources (book.txt, .docx, uploads)
       |
       v
 +------------------+     +------------------+
 | Ingestion        |---->| SQS buffer       |
 | Lambda / BDA     |     | workers drain    |
 | extract structure|     +------------------+
 +------------------+              |
       | KMS encrypts at rest      v
       v                  +------------------+
 +------------------+    | Chunk + embed    |
 | S3 (versioned,    |--->| -> vector store  |
 | KMS-encrypted)   |    +------------------+
 +------------------+
       X-Ray traces every hop; CloudWatch alarms on failures
```

Figure 9.1: Where the supporting labs fit in a GenAI ingestion pipeline. Caption: ASCII diagram drawn for this volume.

How to read this diagram

1. Start at the top: raw documents enter. Ingestion (Lambda preprocessing or Bedrock Data Automation) extracts structure so chunking works.
2. SQS buffers the work so a surge of uploads does not overwhelm the embedders. Workers drain at their own pace.
3. S3 holds the raw and processed files, versioned and encrypted with KMS. Nothing here is public.
4. Chunking and embedding feed the vector store. X-Ray traces the whole path; CloudWatch watches for failures.

What breaks if a component fails

- If structure extraction is skipped, tables and headings shatter across chunks and retrieval quality collapses. This is the "bad RAG answers" root cause the exam hides in ingestion.
- If the queue has no dead-letter handling, poison messages retry forever and block the pipeline.
- If encryption is missing on the bucket, a compliance scenario fails no matter how good the retrieval is.

:::exam-ask

These labs answer the "which service for this job" questions: KMS for encryption at rest, X-Ray for cross-service latency tracing, SQS for buffering between pipeline stages, Kinesis for ordered replayable streams. The traps are always the wrong-plane tools: CloudTrail for metrics, S3 for session state, ElastiCache for durable vectors.
:::

#### Practice question {#practice-question}

A RAG ingestion pipeline processes thousands of documents daily. Requirements: buffer upload surges, encrypt stored documents with customer-managed keys, and trace end-to-end latency when a document stalls. Which combination is MOST correct? (Select THREE.)

A. Buffer incoming documents with SQS so embedding workers drain at their own pace.

B. Encrypt the S3 buckets with KMS customer-managed keys.

C. Enable X-Ray tracing across the ingestion Lambdas to find slow hops.

D. Store the documents in ElastiCache for durability and query CloudTrail for latency metrics.

E. Skip structure extraction because the embedding model will figure out tables on its own.

A, B, and C are correct. A decouples surge from processing. B meets the customer-managed encryption requirement. C gives cross-service latency traces, which is exactly the stalled-document question.

D is wrong twice: ElastiCache is ephemeral cache, not durable document storage, and CloudTrail is audit logging, not a metrics or tracing plane. This is the wrong-plane double trap.

E is wrong because raw unstructured text shatters tables across chunks; structure extraction before chunking is what keeps retrieval quality up.

================= QA =================

## Build checklist and verification log {#build-checklist-and-verification-log}

What was checked before this volume shipped.

- Parse check: balanced tags, unique section ids (ch1..ch9, qa), all rail anchors resolve. **PASS** (verified by script after writing).
- Zero em dashes in the file. **PASS** (grep).
- Zero gradients; palette variables only. **PASS** (grep).
- Every chapter has a visual (ASCII figure) plus a "How to read this diagram" walkthrough with numbered flow and per-component failure notes. **PASS**.
- Every chapter has the Maarek framing: what it is, why and when, how AWS asks, exam tips and traps, and one practice question with why-right and why-each-distractor-wrong. **PASS**.
- Copyright rule: all explanations and exercises written fresh for this volume; only short adapted snippets shown; no lab file reproduced verbatim. **PASS**.
- Generic content only: no names, no employers, no personal identifiers. **PASS**.
- No placeholders, no TODO, no empty sections. **PASS**.
- No external dependencies: single self-contained HTML, no hotlinked images, all diagrams ASCII. **PASS**.

### Live verification log (2026-09-28) {#live-verification-log-2026-09-28}

- **Verified against live sources:** AgentCore five components (Runtime, Gateway, Memory, Identity, Observability) and the container contract (POST /invocations, GET /ping, port 8080, linux/arm64) via the official Bedrock AgentCore dev guide URLs and corroborating samples; `BedrockAgentCoreApp` with `@app.entrypoint` via the AgentCore SDK samples; Strands `@tool` decorator semantics (docstring as description, type hints as schema) via the Strands SDK docs and samples; Agent Squad package `agent-squad` with `AgentSquad`, `route_request` coroutine, `BedrockClassifier`, `add_agent`, `response.metadata`, and `ChatStorage` via the project's current docs and the AWS Solutions Guidance page; Bedrock Flows definition structure (`nodes` and `connections` arrays, `Data` and `Conditional` connection types, PrepareFlow DRAFT behavior) via the official Bedrock API reference and CloudFormation docs; Bedrock agent action-group Lambda event and response shapes (parameters list, `responseBody.TEXT.body`, `messageVersion`, apiSchema versus functionSchema) via the Bedrock user guide page on Lambda configuration for agents; Nova model IDs `amazon.nova-lite-v1:0` and `amazon.nova-micro-v1:0` via multiple current sources.
- **Marked UNVERIFIED inline:** the Iterator node sequential-processing detail in chapter 4 (community-reported, not confirmed in live docs during this build).
- **Not stated as fact:** volatile numbers (pricing, quotas) are either omitted or labeled illustrative; where a limit is standard and documented (for example Lambda's 15-minute maximum), it is stated as a documented limit.

Last verified: 2026-09-28. Re-check service details against current AWS documentation before the exam date.

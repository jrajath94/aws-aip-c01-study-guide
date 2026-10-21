AWS Documentation from https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06-bp03.html:

# AGENTCOST06-BP03 Design cost-efficient initialization through warm pools and caching

Cold starts are a significant per-invocation cost in agent
infrastructure, where model loading, tool registration, and memory
hydration run on every fresh session. You can reduce those
per-invocation costs through persistent filesystems, session
affinity, and lazy context loading to reuse results while still
scaling to zero for agents that are rarely called.

**Desired outcome:**

* You amortize initialization costs across many invocations by
  caching artifacts on a persistent filesystem.
* You have frequently invoked agents reusing warm sessions and
  infrequent agents scaling to zero without idle charges.
* You defer non-essential context retrieval to on-demand, keeping
  initialization under a fixed time budget.
* You track cold start rates and initialization costs per agent
  type.

**Common anti-patterns:**

* Performing expensive initialization on every invocation instead
  of caching artifacts across sessions.
* Allowing frequently invoked agents to repeatedly incur cold
  starts without session persistence or warm pool patterns.
* Loading all potentially relevant context at startup instead of
  lazy-loading on demand, increasing initialization latency with
  data that may never be used.
* Operating agents without cold start visibility, missing
  opportunities to apply warm pool patterns or optimize
  initialization for high-impact agents. Agent cold starts include
  model loading, tool registration, and memory hydration, not just
  container startup.

**Benefits of establishing this best
practice:**

* Persistent filesystem caching amortizes initialization costs
  across many invocations, avoiding repeated overhead.
* Session lifecycle management maintains warm sessions for
  frequent agents while scaling to zero for infrequent ones
  without idle charges.
* Lazy context loading reduces initialization time by deferring
  non-essential retrieval until reasoning requires it.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) implements warm pool behavior
through its session lifecycle. Sessions move through Active, Idle,
and Terminated states. Active handles processing, Idle maintains
session readiness after inactivity timeout without compute
charges, and Terminated ends the session at expiration or maximum
lifetime. Frequently invoked agents keep warm sessions through the
idle window while infrequent agents scale to zero, so you don't
pay idle capacity for agents that are not being called. Tune idle
timeout based on invocation frequency to balance responsiveness
with session overhead.

The persistent filesystem makes initialization caching worthwhile
to implement. The filesystem survives session stop and resume
cycles for up to 14 days, so expensive initialization artifacts
(model state, tool configurations, and preloaded reference data)
can be computed once on the first invocation and reused across
many later sessions. The 14-day retention shapes your caching
strategy: plan artifact refresh and cache invalidation to fit
inside the window, so cached data never ages out silently and
never gets stale beyond the refresh point.

Session affinity optimizes costs by keeping the same
runtimeSessionId across related invocations so
loaded models and cached tool configurations are reused. Implement
session tracking in the orchestration layer so user workflows map
to consistent session identifiers, and monitor session reuse rates
to confirm routing is avoiding unnecessary initialization
overhead. If cold start rates rise above 10%, investigate affinity
or idle timeout misconfiguration before optimizing the
initialization logic itself.

Consider *lazy context loading*, where data is
fetched or parsed only when it is required.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) supports retrieving only minimal
startup context (the user's current task and immediate session
history), deferring long-term memory and knowledge base retrieval
until the agent actually needs the data. This keeps initialization
time under a 2-second target covering model loading and tool
registration. Monitor cold start rates and initialization costs
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), build Amazon CloudWatch
dashboards for initialization duration and session reuse by agent
type, and review idle timeout configuration monthly based on
observed invocation patterns.

### Implementation steps

1. **Cache initialization artifacts on
   persistent storage:** Configure
   [Amazon
   Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with persistent filesystem
   (surviving up to 14 days across session cycles) and
   implement initialization logic that checks for cached
   artifacts before performing expensive operations.
2. **Apply session affinity:**
   Maintain consistent runtimeSessionId values across related
   invocations so warm session state (loaded models, cached
   tool configurations) is reused.
3. **Defer non-essential
   context:** Configure
   [Amazon
   Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for lazy loading of startup
   context, deferring additional retrieval to on-demand during
   reasoning, with an initialization time target under 2
   seconds.
4. **Monitor cold start rates per agent
   type:** Instrument agents with
   [Amazon
   Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to track session
   creation latency, initialization duration (model loading and
   tool registration), and cold start rates, with alarms for
   rates exceeding 10%.

## Resources

**Related best practices:**

* [AGENTCOST02-BP03
  Use intelligent caching to reduce redundant model
  invocations](agentcost02-bp03.html)
* [AGENTCOST06-BP01
  Implement lightweight discovery and registry for
  cost-effective collaboration](agentcost06-bp01.html)
* [AGENTCOST06-BP02 Cost
  optimize versioning and deployment through efficient artifact
  management](agentcost06-bp02.html)

**Related documents:**

* [Amazon
  Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
* [Amazon
  Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
* [Amazon
  Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

* [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)
* [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)

**Related examples:**

* [GitHub:
  awslabs/amazon-bedrock-agentcore-samples - Runtime advanced
  concepts](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)

**Related services:**

* [Amazon
  Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
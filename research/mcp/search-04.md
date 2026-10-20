{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-lifecycle-settings.html",
      "title": "runtimeSessionId",
      "context": "Identifier for a specific runtime session in Amazon Bedrock AgentCore Runtime, each of which receives its own dedicated microVM with independent lifecycle timers",
      "recommended_sections": [
        "Lifecycle settings and runtime sessions"
      ],
      "sections": [
        "Configure Amazon Bedrock AgentCore lifecycle settings",
        "Configuration attributes",
        "Constraints",
        "Default behavior",
        "Default values",
        "Create an AgentCore Runtime with lifecycle configuration",
        "Update the lifecycle configuration for an AgentCore Runtime",
        "Get the lifecycle configuration for an AgentCore Runtime",
        "Validation and constraints",
        "Common validation errors",
        "Validation helper function",
        "Lifecycle settings and runtime sessions",
        "Best practices",
        "Recommendations",
        "Common patterns"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06-bp03.html",
      "title": "persistent filesystem",
      "context": "A durable storage layer in Amazon Bedrock AgentCore Runtime that survives session stop and resume cycles for up to 14 days, enabling initialization artifact caching.",
      "recommended_sections": [
        "Implementation guidance"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/arch-agent-layer.html",
      "title": "bidirectional streaming runtime",
      "context": "AgentCore runtime variant that handles the Nova Sonic voice channel using full-duplex speech-to-speech streaming with sub-1.5-second first-audio-token latency.",
      "recommended_sections": [
        "Bedrock AgentCore runtime"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html",
      "title": "runtimeSessionId",
      "context": "Identifier for a specific runtime session in Amazon Bedrock AgentCore Runtime, each of which receives its own dedicated microVM with independent lifecycle timers",
      "recommended_sections": [
        "AgentCore Runtime session lifecycle",
        "Use isolated sessions for agents"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html",
      "title": "AgentCore Runtime session lifecycle",
      "context": "The sequence of states a session transitions through including Active, Idle, and Stopped based on compute lifecycle and invocation activity",
      "recommended_sections": [
        "Runtime session lifecycle management",
        "Asynchronous processing model"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "d6f55afb-c2b9-4af9-b2d6-5ceb6d14bb79",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "AgentCore Runtime session lifecycle",
        "to_description": "The sequence of states a session transitions through including Active, Idle, and Stopped based on compute lifecycle and invocation activity",
        "from": "Use isolated sessions for agents"
      },
      {
        "relation": "references",
        "to": "session storage",
        "to_description": "A persistent directory configured in AgentCore Runtime that survives compute termination and allows filesystem data to persist across session stop/resume cycles",
        "from": "Use isolated sessions for agents"
      },
      {
        "relation": "hasChild",
        "to": "Sessions last up to 8 hours for each lifecycle on microVMs, or up to 14 days on Instances.",
        "to_description": "Maximum session duration limits for AgentCore Runtime microVMs and Instances",
        "from": "Use isolated sessions for agents"
      },
      {
        "relation": "references",
        "to": "InvokeAgentRuntimeCommand",
        "to_description": "Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error. To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through contentStart , contentDelta ,…",
        "from": "Use isolated sessions for agents"
      },
      {
        "relation": "references",
        "to": "runtimeSessionId",
        "to_description": "Identifier for a specific runtime session in Amazon Bedrock AgentCore Runtime, each of which receives its own dedicated microVM with independent lifecycle timers",
        "from": "Use isolated sessions for agents"
      }
    ]
  }
}
{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-guardrails.html",
      "title": "apply guardrails to supported node types in a flow",
      "context": "Configure guardrails on prompt or knowledge base nodes in an Amazon Bedrock flow using the console or API",
      "recommended_sections": [
        "Include guardrails in your flow in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08-bp01.html",
      "title": "prompt attack detection",
      "context": "A Bedrock Guardrails capability that identifies user prompts attempting to bypass safety controls or override developer instructions, requiring input tagging to function",
      "recommended_sections": [
        "Implementation guidance"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/bedrock-integration.html",
      "title": "Implement Amazon Bedrock Guardrails for prompt injection protection",
      "context": "Configure Bedrock Guardrails with prompt attack detection and appropriate filter strength to protect foundation models from injection attacks.",
      "recommended_sections": [
        "Prompt injection protection"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tiers.html",
      "title": "prompt attacks",
      "context": "Bedrock Guardrails filter category that detects and blocks jailbreaks, prompt injections, and prompt leakages to prevent bypassing content moderation",
      "recommended_sections": [
        "Safeguard tiers for guardrails policies"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/nodes.html",
      "title": "Bedrock flow guardrail",
      "context": "A safety control that can be assigned to a prompt node or knowledge base node to safeguard an Amazon Bedrock app.",
      "recommended_sections": [
        "Prompt node"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html",
      "title": "How Amazon Bedrock Guardrails works",
      "context": "Overview of how Amazon Bedrock Guardrails evaluates inputs and responses during model inference using configured policies",
      "recommended_sections": [
        "How Amazon Bedrock Guardrails works"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html",
      "title": "GuardrailConfiguration",
      "context": "A configuration field included in Amazon Bedrock API request bodies to associate a guardrail with an inference, agent, knowledge base, or flow operation",
      "recommended_sections": [
        "Prompt node"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html",
      "title": "Configure prompt attack filters for your guardrail",
      "context": "A procedure to configure prompt attack filters on an Amazon Bedrock guardrail using the AWS Management Console or Amazon Bedrock API",
      "recommended_sections": [
        "Configure prompt attack filters for your guardrail",
        "Detect prompt attacks with Amazon Bedrock Guardrails"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html",
      "title": "protect against prompt injection in Amazon Bedrock agents",
      "context": "Configure Amazon Bedrock agents with guardrails, advanced prompts, and system prompts to defend against prompt injection attacks",
      "recommended_sections": [
        "Prompt injection security"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 10,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html",
      "title": "guardrail",
      "context": "A content-safety check that runs at evaluation time, calling a guardrail with selected content and returning a confidence score that policies can condition on to permit, forbid, or suppress responses.",
      "recommended_sections": [
        "Guardrails in policies"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "2fdd824c-2adc-47f9-9a86-b9fd0d1475b1",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "prompt node",
        "to_description": "An orchestration node in the Amazon Bedrock flow canvas that sends input to a foundation model and returns the model's completion",
        "from": "Bedrock flow guardrail"
      },
      {
        "relation": "hasChild",
        "to": "How charges are calculated for Amazon Bedrock Guardrails",
        "to_description": "Explanation of the billing scenarios for Amazon Bedrock Guardrails based on whether the guardrail blocks input, output, or neither",
        "from": "How Amazon Bedrock Guardrails works"
      },
      {
        "relation": "references",
        "to": "blocked message",
        "to_description": "A pre-configured response returned by a guardrail when an input evaluation results in an intervention, replacing the foundation model inference.",
        "from": "How Amazon Bedrock Guardrails works"
      },
      {
        "relation": "references",
        "to": "guardrail input evaluation",
        "to_description": "The optional guardrail assessment of model input content for PII entities, which can be enabled or disabled independently of output evaluation",
        "from": "How Amazon Bedrock Guardrails works"
      },
      {
        "relation": "references",
        "to": "guardrail policy",
        "to_description": "A configurable rule within a guardrail that governs how inputs and outputs are evaluated, including content filters, denied topics, sensitive information filters, word filters, and image content filters",
        "from": "How Amazon Bedrock Guardrails works"
      }
    ]
  }
}
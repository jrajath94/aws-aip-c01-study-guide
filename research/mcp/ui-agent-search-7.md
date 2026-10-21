{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html",
      "title": "Explicit Prompt Caching",
      "context": "Amazon Bedrock prompt caching feature that requires explicit request parameters, not supported for this model",
      "recommended_sections": [
        "Billing for cached tokens",
        "Playground",
        "Explicit Prompt Caching",
        "Understanding the response",
        "Prompt caching for faster model inference",
        "Supported models, Regions, and explicit caching limits",
        "GPT-5.6 and later models",
        "Converse API"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp03.html",
      "title": "cached token rate",
      "context": "The reduced per-token charge applied when tokens are read from the Amazon Bedrock prompt cache rather than recomputed",
      "recommended_sections": [
        "Implementation guidance",
        "Implementation steps"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/connect/latest/adminguide/agentic-self-service-prompt-best-practices.html",
      "title": "prompt caching",
      "context": "Amazon Bedrock feature that retains cached prompt prefixes for a defined duration to reduce redundant token processing",
      "recommended_sections": [
        "Optimize for prompt caching"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-runtime-metrics.html",
      "title": "CacheReadInputTokenCount metric",
      "context": "CloudWatch metric counting input tokens read from the prompt cache, which are charged at a reduced rate and do not count toward TPM quota.",
      "recommended_sections": [
        "Amazon Bedrock runtime metrics"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_CacheDetail.html",
      "title": "CacheDetail",
      "context": "An object representing a detailed breakdown of cache writes by TTL duration in Amazon Bedrock Runtime",
      "recommended_sections": null,
      "sections": [
        "CacheDetail",
        "Contents",
        "See Also"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "7fcbac8e-9b2b-41ae-b071-69407d7a07cd",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "Amazon Bedrock console playground",
        "to_description": "An interactive chat interface in the Amazon Bedrock console that supports prompt caching with automatic checkpoint creation and caching metrics display.",
        "from": "Caching metrics"
      },
      {
        "relation": "dependsOn",
        "to": "Enable prompt caching for supported models",
        "to_description": "Activate prompt caching in the Amazon Bedrock console or via API and configure cache checkpoints at optimal locations",
        "from": "Monitor caching metrics"
      },
      {
        "relation": "references",
        "to": "cache hit rate",
        "to_description": "A metric tracked via Amazon Bedrock AgentCore Observability that indicates how often retries return cached idempotency results, confirming the idempotency mechanism is working.",
        "from": "Monitor caching metrics"
      },
      {
        "relation": "references",
        "to": "cached token rate",
        "to_description": "The reduced per-token charge applied when tokens are read from the Amazon Bedrock prompt cache rather than recomputed",
        "from": "Monitor caching metrics"
      },
      {
        "relation": "relatesTo",
        "to": "cache hit rate",
        "to_description": "A metric tracked via Amazon Bedrock AgentCore Observability that indicates how often retries return cached idempotency results, confirming the idempotency mechanism is working.",
        "from": "cached token rate"
      }
    ]
  }
}
{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html",
      "title": "prompt caching",
      "context": "Amazon Bedrock feature that retains cached prompt prefixes for a defined duration to reduce redundant token processing",
      "recommended_sections": [
        "Implicit Prompt Caching",
        "Explicit Prompt Caching",
        "Best practices for using cache management in GPT-5.5 and earlier models",
        "Types of prompt caching",
        "Prompt caching for models from Anthropic",
        "GPT-5.5 and earlier models",
        "Playground",
        "Prompt caching for faster model inference",
        "InvokeModel API",
        "Prompt caching for models from OpenAI"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-mid-conversation-system.html",
      "title": "prompt caching for mid-conversation system messages",
      "context": "A caching strategy where mid-conversation system messages are appended after the cached prefix breakpoint so the cache hash is not invalidated",
      "recommended_sections": [
        "Prompt caching"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-compaction.html",
      "title": "cache_control breakpoint on compaction blocks",
      "context": "A prompt caching configuration that caches the full system prompt along with summarized content when applied to a compaction block",
      "recommended_sections": [
        "Prompt caching"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/connect/latest/adminguide/agentic-self-service-prompt-best-practices.html",
      "title": "prompt caching",
      "context": "Amazon Bedrock feature that retains cached prompt prefixes for a defined duration to reduce redundant token processing",
      "recommended_sections": [
        "Optimize for prompt caching"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "e9b478bd-e5fe-4550-a375-252cdb7dd47e",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "prompt node",
        "to_description": "An orchestration node in the Amazon Bedrock flow canvas that sends input to a foundation model and returns the model's completion",
        "from": "prompt caching"
      },
      {
        "relation": "relatesTo",
        "to": "Anthropic Messages API",
        "to_description": "Anthropic's native API for interacting with Claude models, accessible via the bedrock-runtime endpoint's /anthropic route",
        "from": "prompt caching"
      },
      {
        "relation": "relatesTo",
        "to": "Explicit Prompt Caching",
        "to_description": "Amazon Bedrock prompt caching feature that requires explicit request parameters, not supported for this model",
        "from": "prompt caching"
      },
      {
        "relation": "relatesTo",
        "to": "static domain facts in prompt",
        "to_description": "Domain policies embedded directly in the system prompt rather than retrieved via tool calls to ensure availability across conversation turns and enable prompt caching.",
        "from": "prompt caching"
      },
      {
        "relation": "relatesTo",
        "to": "cached tokens",
        "to_description": "Tokens successfully read from the prompt cache, billed at the model's cache-read rate rather than the standard input token rate",
        "from": "prompt caching"
      }
    ]
  }
}
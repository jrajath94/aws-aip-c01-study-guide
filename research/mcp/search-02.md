{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html",
      "title": "How Amazon Bedrock Guardrails works",
      "context": "Overview of how Amazon Bedrock Guardrails evaluates inputs and responses during model inference using configured policies",
      "recommended_sections": [
        "How Amazon Bedrock Guardrails works"
      ],
      "sections": [
        "How Amazon Bedrock Guardrails works",
        "How charges are calculated for Amazon Bedrock Guardrails"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html",
      "title": "Create your guardrail",
      "context": "A procedure for configuring Amazon Bedrock Guardrails filters to block harmful content and protect sensitive information in generative AI applications",
      "recommended_sections": [
        "Create your guardrail"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prereq.html",
      "title": "guardrail blocked message",
      "context": "Custom messages configured in Amazon Bedrock Guardrails to send to users when a prompt or model response is blocked",
      "recommended_sections": [
        "Prerequisites for using Amazon Bedrock Guardrails"
      ],
      "sections": [
        "Prerequisites for using Amazon Bedrock Guardrails"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use.html",
      "title": "ApplyGuardrail",
      "context": "The action to apply a guardrail. For troubleshooting some of the common errors you might encounter when using the ApplyGuardrail API, see Troubleshooting Amazon Bedrock API Error Codes in the Amazon Bedrock User Guide",
      "recommended_sections": null,
      "sections": [
        "Use cases for Amazon Bedrock Guardrails"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html",
      "title": "ApplyGuardrail",
      "context": "The action to apply a guardrail. For troubleshooting some of the common errors you might encounter when using the ApplyGuardrail API, see Troubleshooting Amazon Bedrock API Error Codes in the Amazon Bedrock User Guide",
      "recommended_sections": null,
      "sections": [
        "Detect and filter harmful content by using Amazon Bedrock Guardrails"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "33375e01-7c8e-4e55-a587-8ede2cf9b062",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
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
      },
      {
        "relation": "hasChild",
        "to": "AWS periodically updates these models to extend functionality, address new attack vectors, and strengthen safety posture.",
        "to_description": "A notice that AWS automatically updates the underlying models powering Guardrails safeguards with no action required from users.",
        "from": "How Amazon Bedrock Guardrails works"
      }
    ]
  }
}
{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html",
      "title": "How Amazon Bedrock Guardrails works",
      "context": "Overview of how Amazon Bedrock Guardrails evaluates inputs and responses during model inference using configured policies",
      "recommended_sections": [
        "How Amazon Bedrock Guardrails works",
        "How charges are calculated for Amazon Bedrock Guardrails"
      ],
      "sections": [
        "How Amazon Bedrock Guardrails works",
        "How charges are calculated for Amazon Bedrock Guardrails"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html",
      "title": "ApplyGuardrail",
      "context": "The action to apply a guardrail. For troubleshooting some of the common errors you might encounter when using the ApplyGuardrail API, see Troubleshooting Amazon Bedrock API Error Codes in the Amazon Bedrock User Guide",
      "recommended_sections": [
        "End-to-end workflow overview"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-guardrails-in-policies.html",
      "title": "InvokeGuardrailChecks",
      "context": "Evaluates messages against inline guardrail checks. You specify the check configurations directly in the request, and Amazon Bedrock returns per-check results with severity or confidence scores.",
      "recommended_sections": [
        "How guardrails work in a policy"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html",
      "title": "GuardrailAssessment",
      "context": "An object in the GuardrailTrace that contains details about guardrail evaluations on input and output data including topic, content, word, and sensitive information policies",
      "recommended_sections": [
        "GuardrailTrace"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/example-policies-guardrails.html",
      "title": "guardrail policy",
      "context": "A configurable rule within a guardrail that governs how inputs and outputs are evaluated, including content filters, denied topics, sensitive information filters, word filters, and image content filters",
      "recommended_sections": [
        "Rules these examples follow",
        "Screen a runtime target",
        "Screen the Responses API",
        "Screen chat completions"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/guardrails.html",
      "title": "guardrail policy",
      "context": "A configurable rule within a guardrail that governs how inputs and outputs are evaluated, including content filters, denied topics, sensitive information filters, word filters, and image content filters",
      "recommended_sections": [
        "Guardrail policies"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html",
      "title": "bedrock:ApplyGuardrail",
      "context": "Amazon Bedrock API operation that applies a guardrail to filter content, including from third-party models",
      "recommended_sections": null,
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html",
      "title": "cross-Region guardrail inference",
      "context": "A Bedrock Guardrails capability that routes guardrail policy evaluations using compute across different AWS Regions.",
      "recommended_sections": [
        "Supported Regions for cross-Region guardrail inference"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SpanGuardrailAssessment.html",
      "title": "SpanGuardrailAssessment",
      "context": "A data type representing the result of a single guardrail assessment covering either the input or output of a Bedrock Converse call",
      "recommended_sections": null,
      "sections": [
        "SpanGuardrailAssessment",
        "Contents",
        "See Also"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "a9273c90-7165-4445-a833-3727062b7408",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "guardrail input evaluation",
        "to_description": "The optional guardrail assessment of model input content for PII entities, which can be enabled or disabled independently of output evaluation",
        "from": "How Amazon Bedrock Guardrails works"
      },
      {
        "relation": "references",
        "to": "guardrail intervention",
        "to_description": "An event triggered when a guardrail policy detects a violation in a prompt or model response, causing the guardrail to block or mask the content",
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
        "to": "How charges are calculated for Amazon Bedrock Guardrails",
        "to_description": "Explanation of the billing scenarios for Amazon Bedrock Guardrails based on whether the guardrail blocks input, output, or neither",
        "from": "How Amazon Bedrock Guardrails works"
      },
      {
        "relation": "hasChild",
        "to": "Embedding, reranking, and image generation models don't support guardrails.",
        "to_description": "Limitation stating that embedding, reranking, and image generation models are not compatible with Amazon Bedrock Guardrails",
        "from": "How Amazon Bedrock Guardrails works"
      }
    ]
  }
}
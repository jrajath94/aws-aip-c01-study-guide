{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html",
      "title": "Add denied topics to your guardrail",
      "context": "A procedure to configure denied topics in an Amazon Bedrock guardrail using the AWS Management Console or Amazon Bedrock API",
      "recommended_sections": [
        "Add denied topics to your guardrail",
        "Block denied topics to help remove harmful content"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-code-domain.html",
      "title": "denied topics",
      "context": "Amazon Bedrock Guardrails configuration that defines subject categories the agent is blocked from discussing, requiring periodic tuning against representative sample prompts",
      "recommended_sections": [
        "Denied Topics"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/guardrails.html",
      "title": "You can define up to five denied topics. Input prompts and model completions will be evaluated against each of these topics.",
      "context": "Quota and evaluation behavior for denied topics in Amazon Bedrock guardrails",
      "recommended_sections": [
        "Denied topics"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-topicconfig.html",
      "title": "AWS::Bedrock::Guardrail TopicConfig",
      "context": "CloudFormation resource property type that defines topic-based denial configuration for an Amazon Bedrock guardrail",
      "recommended_sections": [
        "AWS::Bedrock::Guardrail TopicConfig"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicsTierConfig.html",
      "title": "GuardrailTopicsTierConfig",
      "context": "Configuration object that specifies the tier a guardrail uses for denied topic filters",
      "recommended_sections": null,
      "sections": [
        "GuardrailTopicsTierConfig",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicPolicyConfig.html",
      "title": "GuardrailTopicPolicyConfig",
      "context": "A configuration object that contains details about topics a guardrail should identify and deny",
      "recommended_sections": null,
      "sections": [
        "GuardrailTopicPolicyConfig",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-test-config.html",
      "title": "apply guardrails to knowledge base",
      "context": "Configure and attach a Bedrock Guardrail to a knowledge base to enforce content safety and topic restrictions on query responses.",
      "recommended_sections": [
        "Guardrails"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html",
      "title": "GuardrailTopicConfig",
      "context": "CloudFormation property type that defines topic configuration within a guardrail topic policy for Amazon Wisdom AI guardrails",
      "recommended_sections": null,
      "sections": [
        "GuardrailTopicConfig",
        "Contents",
        "See Also"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "784db397-791d-47b9-83cb-3aac9629cd2d",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "guardrail safeguard tier",
        "to_description": "A configuration option that determines the level of evaluation applied by a guardrail when blocking topics in prompts and responses, with options including CLASSIC and STANDARD.",
        "from": "Add denied topics to your guardrail"
      },
      {
        "relation": "references",
        "to": "CreateGuardrail",
        "to_description": "Amazon Bedrock API operation that creates a guardrail with specified content filters, messaging, and optional encryption and tagging settings",
        "from": "Add denied topics to your guardrail"
      },
      {
        "relation": "references",
        "to": "denied topic",
        "to_description": "A named topic with a definition and optional sample phrases that a guardrail uses to detect and block undesirable content in prompts and responses",
        "from": "Add denied topics to your guardrail"
      },
      {
        "relation": "references",
        "to": "topicPolicyConfig",
        "to_description": "The API request object that specifies the denied topics configuration for a guardrail, including topic definitions, actions, and tier settings.",
        "from": "Add denied topics to your guardrail"
      },
      {
        "relation": "references",
        "to": "cross-region inference",
        "to_description": "An automatic Amazon Quick platform behavior that processes inference requests in the optimal Region within a defined geography, keeping data on the AWS network and stored data in the primary Region",
        "from": "Add denied topics to your guardrail"
      }
    ]
  }
}
{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/multi-tenant-generative-ai-platform-scenario.html",
      "title": "dynamic inference request routing",
      "context": "A router capability that directs inference requests to the most appropriate runtime environment based on deployment context",
      "recommended_sections": null,
      "sections": [
        "Multi-tenant generative AI platform scenario",
        "Scenario characteristics",
        "Service personas",
        "Service components",
        "Architecture and design",
        "API layer and router",
        "Training pipeline",
        "Responsible AI: Guardrails for security and privacy",
        "Domain-adapted custom LLMs",
        "Inference",
        "Policies",
        "Agents and tools: A source of domain-specific capabilities",
        "Configuration and implementation",
        "Gateway configuration and setup",
        "Example gateway architecture",
        "Best practices, considerations, and trade-offs",
        "Optimization techniques, scaling strategies, and cost-saving measures",
        "Security and compliance",
        "Network and perimeter security",
        "Identity, access, and tenant management",
        "Data and model security",
        "Responsible AI and auditability",
        "Validation and testing",
        "Lessons learned and best practices"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/security.html",
      "title": "Implement comprehensive access controls",
      "context": "A security principle that applies least privilege across all generative AI system components including models, data stores, endpoints, and agent workflows.",
      "recommended_sections": [
        "Security"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-model-inference.html",
      "title": "Implement cross-account security and governance",
      "context": "Deploy Security Hub, GuardDuty, AWS Config, and EventBridge across all AI account types with centralized log aggregation and automated security responses",
      "recommended_sections": [
        "Multi-account architecture for AI workloads"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-auto-agents.html",
      "title": "Deploy Amazon Bedrock Guardrails for agents",
      "context": "Configure and deploy versioned Amazon Bedrock Guardrails with content filters, denied topics, and contextual grounding checks to protect agents from prompt attacks and hallucinations.",
      "recommended_sections": [
        "Amazon Bedrock Guardrails"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/security.html",
      "title": "generative AI security and governance framework",
      "context": "A platform-centric security and governance structure that ensures all generative AI applications benefit from default security and responsible AI guardrails.",
      "recommended_sections": [
        "Layer 3: Security and governance for generative AI platforms on AWS"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html",
      "title": "Generative AI OU",
      "context": "A dedicated AWS organizational unit within the AWS SRA framework that hosts Amazon Bedrock and associated services in separate Application and Generative AI accounts.",
      "recommended_sections": [
        "AWS SRA for AI"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec02-bp01.html",
      "title": "Guardrails AI",
      "context": "Open-source package providing guardrail capabilities as an alternative to Amazon Bedrock Guardrails for generative AI workloads",
      "recommended_sections": [
        "Resources",
        "GENSEC02-BP01 Implement guardrails to mitigate harmful or incorrect model responses"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/implementing-security-rai.html",
      "title": "Incident response setup",
      "context": "Design and establish accessible incident response procedures with clear roles to quickly mitigate harm from deployed generative AI model issues.",
      "recommended_sections": null,
      "sections": [
        "Implementing security and responsible AI",
        "Before moving to inference",
        "Model assessment",
        "Documentation preparation",
        "Technical safeguards",
        "Governance setup",
        "After inference deployment",
        "Continuous monitoring",
        "Incident response mechanisms",
        "Feedback collection mechanisms"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "672d713d-e170-4e18-a4a1-dc8ea4d3a43c",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "Amazon Q Business admin controls and guardrails",
        "to_description": "Configuration settings that control chat behavior and topic restrictions in Amazon Q Business application environments",
        "from": "Guardrails automate the identification and remediation of undesirable model output."
      },
      {
        "relation": "dependsOn",
        "to": "Configure AI training account",
        "to_description": "Set up a highly secured AWS account for sensitive training data and production model development with strict IAM, KMS encryption, and private VPC deployments",
        "from": "Implement cross-account security and governance"
      },
      {
        "relation": "dependsOn",
        "to": "Configure AI development account",
        "to_description": "Set up an AWS sandbox account for AI experimentation with Macie, SageMaker Studio, cost controls, and permissive development policies",
        "from": "Implement cross-account security and governance"
      },
      {
        "relation": "references",
        "to": "multi-account AI strategy",
        "to_description": "Architectural approach that isolates AI inference, development, and training workloads into separate AWS accounts for enhanced security boundaries and governance",
        "from": "Implement cross-account security and governance"
      },
      {
        "relation": "references",
        "to": "cross-account trust relationship",
        "to_description": "A configuration that allows principals in one AWS account to assume a role in another AWS account by combining a trust policy update with a permissions policy grant",
        "from": "Implement cross-account security and governance"
      }
    ]
  }
}
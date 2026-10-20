{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-auto-agents.html",
      "title": "Encrypt agent data with customer managed KMS keys",
      "context": "Configure customer managed AWS KMS keys to encrypt AgentCore Memory resources, Identity token vaults, Gateway configuration, and CloudWatch log groups.",
      "recommended_sections": [
        "Amazon Bedrock AgentCore Gateway"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-iam.html",
      "title": "identity-based policy",
      "context": "A JSON permissions policy document attached to an IAM identity (user, group, or role) that controls what actions the identity can perform on which resources and under what conditions.",
      "recommended_sections": [
        "Identity and access management for Amazon Bedrock AgentCore"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/bedrock-integration.html",
      "title": "Implement autonomous agent security controls",
      "context": "Secure agentic applications by using Amazon Bedrock AgentCore Runtime with session isolation, customer managed KMS keys, least-privilege IAM roles, and AgentCore Observability.",
      "recommended_sections": [
        "Autonomous agents"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security.html",
      "title": "Identity and access management for Amazon Bedrock AgentCore",
      "context": "IAM configurations and policies that control authentication and authorization for Amazon Bedrock AgentCore resources",
      "recommended_sections": [
        "Security in Amazon Bedrock AgentCore"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/key-features-and-benefits.html",
      "title": "@requires_api_key",
      "context": "AgentCore SDK declarative annotation that automatically handles API key retrieval and injection into agent code",
      "recommended_sections": null,
      "sections": [
        "Features of AgentCore Identity",
        "Centralized agent identity management",
        "Secure credential storage",
        "OAuth 2.0 flow support",
        "Agent identity and access controls",
        "AgentCore SDK Integration",
        "Request verification security"
      ],
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security_iam_service-with-iam.html",
      "title": "AgentCore identity-based policy",
      "context": "IAM policy attached to an IAM user, role, or group that specifies what actions the identity can perform on Amazon Bedrock AgentCore resources",
      "recommended_sections": [
        "How Amazon Bedrock AgentCore works with IAM"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp03.html",
      "title": "Enforce identity at the application layer",
      "context": "Configure A2A agent card discovery with authentication requirements on AgentCore Runtime, or use Amazon API Gateway with Lambda authorizers for agents not on AgentCore Runtime.",
      "recommended_sections": [
        "Implementation steps"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01-bp01.html",
      "title": "customer-managed AWS KMS key for memory encryption",
      "context": "A customer-managed KMS key specified via the encryptionKeyArn parameter to encrypt sensitive reasoning context stored in AgentCore Memory.",
      "recommended_sections": [
        "Implementation steps"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-instances-security.html",
      "title": "Runtime execution role",
      "context": "IAM role whose credentials are vended to agents running on an instance, granting the agent code its runtime permissions",
      "recommended_sections": [
        "Security model and permissions for Runtime Instances"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "782b53a7-6330-4ab8-9e0c-14c67a4274eb",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "token vaults",
        "to_description": "Secure credential storage within AgentCore Identity for managing authentication tokens used by agents to access tools and resources.",
        "from": "Implement autonomous agent security controls"
      },
      {
        "relation": "references",
        "to": "dedicated microVMs",
        "to_description": "Isolated virtual machine instances used by Amazon Bedrock AgentCore Runtime to provide complete session isolation for hosted agents.",
        "from": "Implement autonomous agent security controls"
      },
      {
        "relation": "references",
        "to": "ingress authentication",
        "to_description": "Inbound authentication mechanism in Gateway that verifies the identity of agents and users accessing tools and resources",
        "from": "Implement autonomous agent security controls"
      },
      {
        "relation": "references",
        "to": "egress authorization",
        "to_description": "The process of controlling agent access to tools and resources after user identity has been verified.",
        "from": "Implement autonomous agent security controls"
      },
      {
        "relation": "references",
        "to": "customer managed KMS keys",
        "to_description": "Six KMS keys created by the solution to secure data at rest across S3 buckets, CloudFront logs, CloudTrail events, DataSync files, and AWS Glue Data Catalog metadata",
        "from": "Implement autonomous agent security controls"
      }
    ]
  }
}
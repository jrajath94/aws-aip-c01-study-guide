{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-bedrock.html",
      "title": "Amazon Bedrock Cross-Region Inference",
      "context": "A Bedrock capability that routes inference requests across AWS Regions within the same geography to improve performance and reliability without changing data storage location",
      "recommended_sections": [
        "Overview",
        "Amazon Bedrock — Cross-Region Inference (CRIS)"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html",
      "title": "geographic cross-Region inference profile",
      "context": "An Amazon Bedrock inference profile tied to a specific geography that routes requests within defined geographic boundaries such as US, EU, or APAC",
      "recommended_sections": [
        "Route model inference requests across AWS Regions with cross-Region inference"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html",
      "title": "cross-region (system-defined) inference profile",
      "context": "Predefined Amazon Bedrock inference profiles that route requests for a model across multiple AWS Regions but do not support custom tagging",
      "recommended_sections": [
        "Find supported cross-Region inference profiles"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html",
      "title": "cross-region inference",
      "context": "An automatic Amazon Quick platform behavior that processes inference requests in the optimal Region within a defined geography, keeping data on the AWS network and stored data in the primary Region",
      "recommended_sections": [
        "Cross-Region Inference"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-view.html",
      "title": "cross Region inference profile",
      "context": "An Amazon Bedrock configuration that routes inference requests across AWS regions, requiring a manually created IAM service role for distillation jobs",
      "recommended_sections": [
        "View information about an inference profile"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "267c06ab-378f-4975-9b86-b0743354e498",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "VpcConfig",
        "to_description": "AWS SAM property that configures VPC egress settings for a network connector, including subnets, security groups, and network protocol for ENI provisioning",
        "from": "cross Region inference profile"
      },
      {
        "relation": "relatesTo",
        "to": "inference profile ARN",
        "to_description": "An ARN format for a Bedrock cross-region inference profile that includes the AWS account ID and a geographic prefix on the model ID",
        "from": "cross Region inference profile"
      },
      {
        "relation": "relatesTo",
        "to": "Global cross-Region inference profile",
        "to_description": "A cross-Region inference profile whose destination Regions include all commercial AWS Regions and whose scope can change as AWS adds new Regions",
        "from": "cross-region (system-defined) inference profile"
      },
      {
        "relation": "relatesTo",
        "to": "opt-in Region",
        "to_description": "An AWS Region introduced on or after March 20, 2019 that must be explicitly enabled for an account before a configuration policy can be applied to it, and which can be a linked Region but not a home Region.",
        "from": "cross-region (system-defined) inference profile"
      },
      {
        "relation": "relatesTo",
        "to": "cross-Region connectivity",
        "to_description": "A network architecture pattern using VPC peering or Transit Gateway peering to connect an AWS Security Agent private connection to a target service running in a different AWS Region.",
        "from": "Amazon Bedrock Cross-Region Inference"
      }
    ]
  }
}
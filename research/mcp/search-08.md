{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference.html",
      "title": "SageMaker AI endpoint parameters for large model inference",
      "context": "Configuration parameters for SageMaker AI endpoints that control health check and download timeout quotas for large model deployments",
      "recommended_sections": [
        "Model parallelism and large model inference"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-inference-architecture-and-best-practices-on-aws/amazon-sage-maker-ai-inference-endpoints.html",
      "title": "SageMaker AI Inference endpoint",
      "context": "A managed inference environment for deploying foundation models and ML models at scale with control over underlying instances and inference engines.",
      "recommended_sections": [
        "Amazon SageMaker AI inference endpoints"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/solutions/latest/constructs/aws_lambda_sagemakerendpoint.html",
      "title": "SageMaker endpoint",
      "context": "A deployed SageMaker inference endpoint that serves the custom moderation model and dynamically scales ML inference instances based on request workloads.",
      "recommended_sections": [
        "Architecture"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-hosting.html",
      "title": "create_endpoint",
      "context": "SageMaker AI API call that provisions and launches a SageMaker AI inference endpoint from a specified endpoint configuration",
      "recommended_sections": [
        "SageMaker AI endpoint parameters for large model inference"
      ],
      "sections": [
        "SageMaker AI endpoint parameters for large model inference"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/reference-architecture-diagrams/latest/wafer-inspection-with-machine-learning-architecture/wafer-inspection-with-machine-learning-architecture.html",
      "title": "inference results",
      "context": "Output from the Amazon Lookout for Equipment ML model stored in Amazon S3 and displayed via Amazon Managed Grafana",
      "recommended_sections": [
        "Wafer Inspection with Machine Learning Diagram"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "76971c60-b1b1-470d-9def-deb805288d6b",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "Real-time inference",
        "to_description": "An AWS Marketplace ML inference option that deploys a model as a continuously running API endpoint, billing for software and SageMaker infrastructure until the endpoint is deleted",
        "from": "SageMaker AI Inference endpoint"
      },
      {
        "relation": "relatesTo",
        "to": "incompatible endpoint features",
        "to_description": "Endpoint configurations including serverless inference, asynchronous inference, marketplace containers, multiple-container endpoints, multi-model endpoints, and Inf1 instances that prevent shadow test usage",
        "from": "SageMaker AI Inference endpoint"
      },
      {
        "relation": "relatesTo",
        "to": "inference component",
        "to_description": "A granular SageMaker AI endpoint sub-resource representing a model deployment unit that can be individually filtered and monitored in the Insights dashboard.",
        "from": "SageMaker AI Inference endpoint"
      },
      {
        "relation": "relatesTo",
        "to": "InService status",
        "to_description": "The operational status of a healthy SageMaker HyperPod instance group after its initial creation, maintained regardless of current instance count",
        "from": "SageMaker AI Inference endpoint"
      },
      {
        "relation": "relatesTo",
        "to": "Bedrock managed inference API",
        "to_description": "Amazon Bedrock's serverless inference API that requires no endpoint configuration for imported models",
        "from": "SageMaker AI Inference endpoint"
      }
    ]
  }
}
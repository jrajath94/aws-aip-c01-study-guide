{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report.html",
      "title": "Review metrics for an automated model evaluation job in Amazon Bedrock (console)",
      "context": "A procedure to view and interpret metric results from an automatic model evaluation job using the Amazon Bedrock console",
      "recommended_sections": [
        "Review model evaluation job reports and metrics in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-programmatic.html",
      "title": "review an automatic model evaluation job",
      "context": "A procedure to open and inspect the metrics and configuration summary of an automated model evaluation job in the Amazon Bedrock console",
      "recommended_sections": [
        "Review metrics for an automated model evaluation job in Amazon Bedrock (console)"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-evaluation.html",
      "title": "view results in TensorBoard",
      "context": "Procedure to visualize model evaluation metrics by uploading extracted output to S3 and opening SageMaker AI TensorBoard.",
      "recommended_sections": [
        "Assessing and analyzing evaluation results"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-evaluation-report.html",
      "title": "Understanding a model evaluation report",
      "context": "A guide to interpreting the metrics and sections within an Amazon Bedrock model evaluation report",
      "recommended_sections": [
        "Review a model model evaluation job in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html",
      "title": "evaluator model",
      "context": "The judge model that scores and explains the generator model's responses based on selected metrics in an Amazon Bedrock evaluation job",
      "recommended_sections": [
        "Use metrics to understand model performance"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-built-in-metrics.html",
      "title": "Create a model evaluation job using built-in metrics",
      "context": "A procedure to configure and submit an Amazon Bedrock automated model evaluation job using a judge model and built-in metrics via the console or AWS CLI",
      "recommended_sections": [
        "Create a model evaluation job using built-in metrics"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-human-customer.html",
      "title": "model evaluation report card",
      "context": "A report card in Amazon Bedrock that provides insights about data collected during a human evaluation job, showing metrics, descriptions, rating methods, and data visualizations",
      "recommended_sections": [
        "Review a human-based model evaluation job in Amazon Bedrock (console)"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/batch-evaluations-results.html",
      "title": "compare batch evaluations Python example",
      "context": "Retrieve two batch evaluation results and print a delta table comparing average evaluator scores between a baseline and treatment run",
      "recommended_sections": null,
      "sections": [
        "Understanding results and output",
        "Aggregate results",
        "Session counts",
        "Per-evaluator summaries",
        "Example response",
        "Per-session detail in CloudWatch Logs",
        "Interpreting scores",
        "Error handling",
        "Job-level errors",
        "Session-level errors",
        "Evaluator-level errors",
        "Comparing results across runs",
        "Viewing results from the CLI"
      ],
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "fb262555-7678-412a-8803-78d4396180f3",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "model evaluation job",
        "to_description": "An offline process that tests a base or trained Amazon Nova model against fixed benchmarks or custom datasets to produce quantitative performance metrics",
        "from": "Review metrics for an automated model evaluation job in Amazon Bedrock (console)"
      },
      {
        "relation": "references",
        "to": "model evaluation report",
        "to_description": "A downloadable report generated using SageMaker Clarify that provides model evaluation insights including bias detection for fine-tuned foundation models.",
        "from": "Review metrics for an automated model evaluation job in Amazon Bedrock (console)"
      },
      {
        "relation": "references",
        "to": "F1 score",
        "to_description": "A balanced accuracy metric between 0.0 and 1.0 that combines precision and recall to evaluate Comprehend Detect PII performance, where a prediction is correct if it matches both entity type and start/end position",
        "from": "Understanding a model evaluation report"
      },
      {
        "relation": "references",
        "to": "general text generation task type",
        "to_description": "An Amazon Bedrock model evaluation task type that assesses accuracy, robustness, and toxicity of open-ended text generation using datasets such as TREX, BOLD, WikiText2, and RealToxicityPrompts",
        "from": "Understanding a model evaluation report"
      },
      {
        "relation": "references",
        "to": "evaluation summary",
        "to_description": "A section of the model evaluation report showing task type and calculated task metrics",
        "from": "Understanding a model evaluation report"
      }
    ]
  }
}
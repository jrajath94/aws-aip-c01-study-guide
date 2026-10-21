{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html",
      "title": "Customize a model with distillation in Amazon Bedrock",
      "context": "Procedure to customize an Amazon Bedrock foundation model by transferring knowledge from a teacher model to a student model using distillation",
      "recommended_sections": [
        "Customize your model to improve its performance for your use case"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CustomizationConfig.html",
      "title": "CustomizationConfig",
      "context": "A union configuration object that specifies the customization settings for a model-customization job in Amazon Bedrock.",
      "recommended_sections": [
        "Contents"
      ],
      "sections": [
        "CustomizationConfig",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html",
      "title": "student model",
      "context": "The smaller model that is fine-tuned using synthetic data generated from the teacher model during Amazon Bedrock model distillation.",
      "recommended_sections": [
        "How Amazon Bedrock Model Distillation works",
        "Customize a model with distillation in Amazon Bedrock",
        "Creating a distilled model using prompts that you provide"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/submit-model-distillation-job.html",
      "title": "model distillation job",
      "context": "An Amazon Bedrock job that fine-tunes a student model using teacher model responses from invocation logs or other data sources.",
      "recommended_sections": [
        "Submit a model distillation job in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html",
      "title": "model customization job",
      "context": "A long-running distributed computation task such as pre-training, fine-tuning, or distillation used to optimize foundation models for generative AI workloads.",
      "recommended_sections": [
        "Basic model customization permissions"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "aa38aca7-4d14-4959-9fef-fb6edb08306a",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "distillation",
        "to_description": "A model customization method that transfers knowledge from a larger teacher model to a smaller, faster student model using data synthesis techniques",
        "from": "Customize a model with distillation in Amazon Bedrock"
      },
      {
        "relation": "references",
        "to": "teacher model",
        "to_description": "The larger foundation model whose responses are used to generate synthetic training data for fine-tuning the student model during distillation.",
        "from": "Customize a model with distillation in Amazon Bedrock"
      },
      {
        "relation": "references",
        "to": "student model",
        "to_description": "The smaller model that is fine-tuned using synthetic data generated from the teacher model during Amazon Bedrock model distillation.",
        "from": "Customize a model with distillation in Amazon Bedrock"
      },
      {
        "relation": "relatesTo",
        "to": "teacher model",
        "to_description": "The larger foundation model whose responses are used to generate synthetic training data for fine-tuning the student model during distillation.",
        "from": "student model"
      },
      {
        "relation": "relatesTo",
        "to": "model distillation",
        "to_description": "A technique for FM customization where a smaller model is trained to replicate the behavior of a larger model, considered alongside pre-training, fine-tuning, in-context learning, and RAG.",
        "from": "student model"
      }
    ]
  }
}
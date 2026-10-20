{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html",
      "title": "RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
      "recommended_sections": [
        "Supported models",
        "Supported evaluator models (built-in metrics)",
        "Supported evaluator models (custom metrics)"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-llama.html",
      "title": "logical coherence evaluation prompt",
      "context": "System prompt instructing an LLM judge to assess logical coherence of a generator model's response using rubrics covering self-contradictions, reasoning gaps, soundness, and relevance, returning a JSON answer of Not at all, Neutral/Mixed, or Yes",
      "recommended_sections": null,
      "sections": [
        "Meta Llama 3.1 70B Instruct",
        "Logical coherence",
        "Score mapping",
        "Faithfulness",
        "Helpfulness",
        "Completeness when ground truth is included",
        "Completeness when no ground truth is provided",
        "Correctness when ground truth is specified",
        "Correctness when no ground truth is specified",
        "Context coverage",
        "Context relevance",
        "Citation precision",
        "Citation coverage",
        "Harmfulness",
        "Stereotyping",
        "Refusal"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html",
      "title": "RAG evaluation using Large Language Models",
      "context": "An LLM-based Amazon Bedrock evaluation that computes performance metrics for knowledge base retrieval and response generation",
      "recommended_sections": [
        "Evaluate the performance of Amazon Bedrock resources"
      ],
      "sections": [
        "Evaluate the performance of Amazon Bedrock resources"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create.html",
      "title": "RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
      "recommended_sections": [
        "Creating a RAG evaluation job in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-randg.html",
      "title": "RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
      "recommended_sections": [
        "Creating a retrieve-and-generate RAG evaluation job"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html",
      "title": "RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
      "recommended_sections": [
        "Creating a retrieve-only RAG evaluation job"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/rag-eval-service-roles.html",
      "title": "knowledge base evaluation job",
      "context": "A model evaluation job type in Amazon Bedrock that evaluates retrieval-augmented generation (RAG) pipelines using a knowledge base",
      "recommended_sections": [
        "Service role requirements for knowledge base evaluation jobs"
      ],
      "sections": [
        "Service role requirements for knowledge base evaluation jobs"
      ],
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_RAGConfig.html",
      "title": "KnowledgeBaseConfig",
      "context": "An inference configuration block that specifies an Amazon Bedrock Knowledge Base to use as the RAG source for an evaluation job.",
      "recommended_sections": [
        "Contents"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "40388592-9ad3-41c4-b1d1-0db8888baeaf",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "metricNames",
        "to_description": "An array of built-in or custom metric name strings used to configure an evaluation job",
        "from": "knowledge base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "human-based model evaluation job",
        "to_description": "An Amazon Bedrock model evaluation job that uses human annotators to review prompts and inference results in an annotation portal",
        "from": "knowledge base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "EvaluationPrecomputedRetrieveAndGenerateSourceConfig",
        "to_description": "A configuration object summarizing a RAG source used for a retrieve-and-generate Knowledge Base evaluation job with user-provided inference response data",
        "from": "knowledge base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "BedrockEvaluatorModel",
        "to_description": "The evaluator model used in knowledge base evaluation jobs or model evaluation jobs that use a model as judge to compute evaluation metrics",
        "from": "knowledge base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "model evaluation job",
        "to_description": "An offline process that tests a base or trained Amazon Nova model against fixed benchmarks or custom datasets to produce quantitative performance metrics",
        "from": "knowledge base evaluation job"
      }
    ]
  }
}
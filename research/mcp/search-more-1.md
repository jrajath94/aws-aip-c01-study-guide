{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-agents.html",
      "title": "Validate input documents before RAG ingestion",
      "context": "Scan documents for malware using Amazon S3 malware protection and redact PII using Amazon Comprehend before indexing in a RAG knowledge base",
      "recommended_sections": [
        "Capability 3. Providing secure access to data and systems for generative AI"
      ],
      "sections": [
        "Capability 3. Providing secure access to data and systems for generative AI",
        "Rationale",
        "Multi-layered security strategy",
        "Amazon Bedrock Knowledge Bases",
        "Security considerations",
        "Remediations",
        "Data protection",
        "Data classification and handling",
        "Data lineage and provenance tracking",
        "Identity and access management",
        "Metadata filtering for secure retrieval",
        "Input and output validation",
        "Recommended AWS services",
        "Amazon OpenSearch Serverless",
        "Amazon S3",
        "Amazon Comprehend",
        "Amazon Macie",
        "AWS KMS"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/introduction.html",
      "title": "generative AI",
      "context": "An emerging capability within deep learning that enables AI systems to generate or create new, potentially original content by mimicking aspects of human-like thought and reasoning.",
      "recommended_sections": [
        "Intended audience",
        "Objectives"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/data-architecture.html",
      "title": "Retrieval-Augmented Generation (RAG) data architecture",
      "context": "A data architecture that combines pre-trained models with dynamic retrieval from external knowledge bases to support low-latency, up-to-date inference.",
      "recommended_sections": [
        "Data architecture"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-fully-managed-sagemaker-canvas.html",
      "title": "RAG functionality in SageMaker AI Canvas",
      "context": "Retrieval-augmented generation capability in SageMaker AI Canvas delivered through the no-code document querying feature backed by Amazon Kendra.",
      "recommended_sections": [
        "Amazon SageMaker AI Canvas"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/develop-advanced-generative-ai-chat-based-assistants-by-using-rag-and-react-prompting.html",
      "title": "In-context ReACT Agent service",
      "context": "A workflow that breaks down a user query into multiple reasoning and action steps using RAG Retrieval and Database Query services as tools before generating a final answer.",
      "recommended_sections": [
        "Architecture"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/resources.html",
      "title": "RAG options and architectures on AWS",
      "context": "Available implementation options and architectural patterns for Retrieval Augmented Generation on AWS",
      "recommended_sections": [
        "Retrieval Augmented Generation (RAG)"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/development.html",
      "title": "RAG architecture",
      "context": "A Retrieval Augmented Generation architecture that uses fine-tuned LLMs to deliver augmented patient data, clinical and diagnostic insights, and predicted patient outcomes.",
      "recommended_sections": [
        "Developing and orchestrating generative AI solutions for healthcare"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-custom-generators.html",
      "title": "RAG solution",
      "context": "A retrieval-augmented generation architecture that uses LLMs as a critical component to generate responses grounded in retrieved data.",
      "recommended_sections": [
        "Generators for RAG workflows"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "8f453115-f77c-4e98-98ab-44f449961a70",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "prompt store",
        "to_description": "The storage location where augmented prompts constructed from base templates, instructions, action groups, and knowledge bases are kept for agent use.",
        "from": "Generative AI account RAG capability architecture"
      },
      {
        "relation": "references",
        "to": "Amazon S3 gateway endpoint",
        "to_description": "A VPC gateway endpoint that provides private network access to Amazon S3 buckets used for knowledge base data sources, model invocation logs, and prompt stores",
        "from": "Generative AI account RAG capability architecture"
      },
      {
        "relation": "references",
        "to": "vector store",
        "to_description": "A storage backend used in Customer-managed Knowledge Bases such as Amazon OpenSearch Serverless, Amazon Aurora, or Amazon Neptune for indexing and retrieving embedded data",
        "from": "Generative AI account RAG capability architecture"
      },
      {
        "relation": "references",
        "to": "model invocation logs",
        "to_description": "CloudWatch Logs records of Amazon Bedrock model invocations that always contain the original unmodified request regardless of guardrail intervention",
        "from": "Generative AI account RAG capability architecture"
      },
      {
        "relation": "relatesTo",
        "to": "retrieval augmented generation (RAG)",
        "to_description": "A technique that enables agents to ground LLM responses in factual, up-to-date information retrieved from organizational data sources, reducing hallucinations without requiring model retraining.",
        "from": "RAG systems on AWS"
      }
    ]
  }
}
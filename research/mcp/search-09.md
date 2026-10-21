{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create.html",
      "title": "RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
      "recommended_sections": [
        "Creating a RAG evaluation job in Amazon Bedrock"
      ],
      "sections": null,
      "metadata": {
        "additional_urls": [
          {
            "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-randg.html",
            "section_title": "Creating a retrieve-and-generate RAG evaluation job",
            "section_anchor": "knowledge-base-evaluation-create-randg"
          },
          {
            "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html",
            "section_title": "Creating a retrieve-only RAG evaluation job",
            "section_anchor": "knowledge-base-evaluation-create-ro"
          }
        ]
      }
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html",
      "title": "retrieve-only RAG evaluation job",
      "context": "An Amazon Bedrock evaluation job that assesses retrieval quality from a Knowledge Base without generating a full model response",
      "recommended_sections": [
        "Creating a retrieve-only RAG evaluation job"
      ],
      "sections": null,
      "metadata": {
        "additional_urls": [
          {
            "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html",
            "section_title": "Evaluate the performance of RAG sources using Amazon Bedrock evaluations",
            "section_anchor": "evaluation-kb"
          },
          {
            "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro-custom.html",
            "section_title": "Creating a retrieve-only RAG evaluation job using custom metrics",
            "section_anchor": "knowledge-base-evaluation-create-ro-custom"
          }
        ]
      }
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_EvaluationPrecomputedRetrieveAndGenerateSourceConfig.html",
      "title": "retrieve-and-generate Knowledge Base evaluation job",
      "context": "An Amazon Bedrock evaluation job that assesses RAG pipeline quality using precomputed inference response data provided by the user",
      "recommended_sections": [
        "Contents",
        "EvaluationPrecomputedRetrieveAndGenerateSourceConfig"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/grounding-and-rag.html",
      "title": "agentic workflow with RAG",
      "context": "Multi-step process where an Amazon Bedrock agent invokes a knowledge base, embeds retrieved context into an LLM prompt, and generates grounded output with traceability",
      "recommended_sections": [
        "Integration with agentic AI"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html",
      "title": "retrieve-and-generate RAG evaluation job",
      "context": "An automated evaluation job in Amazon Bedrock that assesses both retrieval and response generation quality of a RAG system using custom or built-in metrics",
      "recommended_sections": [
        "Evaluate the performance of RAG sources using Amazon Bedrock evaluations",
        "Supported models"
      ],
      "sections": null,
      "metadata": {
        "additional_urls": [
          {
            "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-metrics.html",
            "section_title": "Use metrics to understand RAG system performance",
            "section_anchor": "knowledge-base-evaluation-metrics"
          }
        ]
      }
    }
  ],
  "facets": null,
  "query_id": "57a457ea-7c25-4824-82c8-94be85a21f8d",
  "metadata": {
    "discovered_services": [
      {
        "name": "Amazon Bedrock Knowledge Bases (RAG)",
        "description": "AWS service that enables agents to retrieve relevant information using semantic search and Retrieval Augmented Generation from structured and unstructured data sources."
      },
      {
        "name": "Bedrock Agents",
        "description": "A fully managed AWS service that enables building and configuring autonomous agents that orchestrate interactions between foundation models, data sources, software applications, and user conversations."
      },
      {
        "name": "Amazon Bedrock Flows",
        "description": "AWS feature that allows creation and management of advanced workflows linking foundation models, prompts, agents, and knowledge bases without writing code."
      },
      {
        "name": "Amazon Bedrock Evaluations",
        "description": "Amazon Bedrock service that runs prompt versions against standardized datasets and produces quality scores for task success, response relevance, and behavioral adherence."
      }
    ],
    "related_tasks": [
      {
        "name": "Creating a retrieve-and-generate RAG evaluation job",
        "description": "A multi-step procedure to configure and submit a retrieve-and-generate RAG evaluation job in Amazon Bedrock using the console, CLI, or SDK",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-create-randg.html#knowledge-base-evaluation-create-randg",
            "url_description": "Step-by-step instructions to create a retrieve-and-generate RAG evaluation job in Amazon Bedrock targeting an Amazon Bedrock Knowledge Base or bring-your-own inference responses, configuring evaluator models, built-in metrics, S3 datasets, IAM roles, and optional KMS encryption"
          }
        ]
      },
      {
        "name": "Create a prompt dataset for a RAG evaluation in Amazon Bedrock",
        "description": "Prepare and store a JSONL prompt dataset in Amazon S3 to evaluate retrieval and generation for an Amazon Bedrock Knowledge Base or custom RAG system",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-create-randg.html#knowledge-base-evaluation-create-randg",
            "url_description": "Step-by-step instructions to create a retrieve-and-generate RAG evaluation job in Amazon Bedrock targeting an Amazon Bedrock Knowledge Base or bring-your-own inference responses, configuring evaluator models, built-in metrics, S3 datasets, IAM roles, and optional KMS encryption"
          },
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-prompt.html#knowledge-base-evaluation-prompt",
            "url_description": "How to create a JSONL prompt dataset stored in Amazon S3 to evaluate retrieval and generation for an Amazon Bedrock Knowledge Base or custom RAG system, including dataset format requirements and CORS configuration for human-based evaluation jobs"
          }
        ]
      },
      {
        "name": "create a knowledge base evaluation job",
        "description": "A procedure to set up and launch an evaluation job for an Amazon Bedrock knowledge base by configuring a service role and required permissions",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/rag-eval-service-roles.html#rag-eval-service-roles",
            "url_description": "IAM service role requirements for Amazon Bedrock knowledge base evaluation jobs, including required S3 access policies, Bedrock API permissions for Retrieve and RetrieveAndGenerate actions, and trust policy configuration for the Amazon Bedrock service principal"
          }
        ]
      },
      {
        "name": "Creating a retrieve-and-generate RAG evaluation job using custom metrics",
        "description": "A procedure to configure and submit a RAG evaluation job in Amazon Bedrock that uses custom judge-model metrics with optional rating scales",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-create-randg-custom.html#knowledge-base-evaluation-create-randg-custom",
            "url_description": "Step-by-step instructions to create a retrieve-and-generate RAG evaluation job in Amazon Bedrock using custom metrics defined by judge model prompts and optional output rating schemas, supporting both Knowledge Base and bring-your-own-inference sources."
          }
        ]
      },
      {
        "name": "Creating a retrieve-only RAG evaluation job",
        "description": "A multi-step procedure to configure and submit a retrieve-only RAG evaluation job in Amazon Bedrock using the console, CLI, or SDK",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html#knowledge-base-evaluation-create-ro",
            "url_description": "Step-by-step instructions to create a retrieve-only RAG evaluation job in Amazon Bedrock targeting an Amazon Bedrock Knowledge Base or custom inference responses, configuring evaluator models, built-in metrics, S3 dataset locations, IAM roles, and optional KMS encryption"
          }
        ]
      },
      {
        "name": "evaluate Amazon Bedrock model and knowledge base performance",
        "description": "Use Amazon Bedrock Evaluations to assess the performance and effectiveness of models and knowledge bases",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/evaluation.html#evaluation",
            "url_description": "How to use Amazon Bedrock evaluations to measure the performance and effectiveness of Amazon Bedrock models, knowledge bases, and RAG sources using automatic, human, and LLM-judge evaluation methods"
          }
        ]
      },
      {
        "name": "use a customer-managed key for knowledge base evaluation",
        "description": "Configure a customer-managed KMS key for encrypting data in Amazon Bedrock knowledge base evaluation jobs by setting up IAM and KMS key policies",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/rag-evaluation-security-data.html#rag-evaluation-security-data",
            "url_description": "How Amazon Bedrock encrypts temporary data during knowledge base evaluation jobs using a customer-managed or AWS-owned KMS key, and what IAM and KMS permissions are required"
          }
        ]
      },
      {
        "name": "Evaluate the performance of RAG sources using Amazon Bedrock evaluations",
        "description": "A procedure for measuring the retrieval and generation quality of RAG sources or Amazon Bedrock Knowledge Bases using LLM-based evaluations",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/evaluation-kb.html#evaluation-kb",
            "url_description": "How to use Amazon Bedrock computed metrics to evaluate RAG system retrieval and generation quality, comparing Knowledge Bases and external RAG sources with retrieve-only and retrieve-and-generate job types"
          }
        ]
      },
      {
        "name": "Creating a retrieve-only RAG evaluation job using custom metrics",
        "description": "A multi-step procedure to configure and launch a retrieve-only RAG evaluation job in Amazon Bedrock using custom metrics via the console or AWS CLI",
        "urls": [
          {
            "url_name": "/bedrock/latest/userguide/knowledge-base-evaluation-create-ro-custom.html#knowledge-base-evaluation-create-ro-custom",
            "url_description": "Step-by-step instructions to create a retrieve-only RAG evaluation job in Amazon Bedrock using custom metrics, including console and AWS CLI create-evaluation-job examples for both Amazon Bedrock Knowledge Bases and bring-your-own inference response data"
          }
        ]
      },
      {
        "name": "Configure and customize queries and response generation",
        "description": "Adjust query behavior and response generation settings for an Amazon Bedrock Knowledge Base using prompt templates and configuration options",
        "urls": [
          {
            "url_name": "/nova/latest/userguide/rag-br-knowledge.html#rag-br-knowledge",
            "url_description": "How to set up and use Amazon Bedrock Knowledge Bases with Amazon Nova models to implement RAG workflows from data ingestion through retrieval, prompt augmentation, testing, and AI application deployment"
          },
          {
            "url_name": "/bedrock/latest/userguide/kb-test-self-managed.html#kb-test-self-managed",
            "url_description": "How to test an Amazon Bedrock customer-managed knowledge base using query, retrieval, and response generation methods including RetrieveAndGenerate, structured data queries, Amazon Kendra GenAI index integration, Amazon Neptune Analytics graph integration, and reasoning model configuration"
          }
        ]
      }
    ],
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "RAG evaluation job",
        "to_description": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
        "from": "retrieve-only RAG evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "ragSourceIdentifier",
        "to_description": "A label that identifies the RAG source used for a retrieve-and-generate Knowledge Base evaluation job with user-provided inference response data",
        "from": "retrieve-and-generate Knowledge Base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "EvaluationPrecomputedRetrieveAndGenerateSourceConfig",
        "to_description": "A configuration object summarizing a RAG source used for a retrieve-and-generate Knowledge Base evaluation job with user-provided inference response data",
        "from": "retrieve-and-generate Knowledge Base evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "RAG evaluation job",
        "to_description": "An automated evaluation job in Amazon Bedrock that assesses the performance of a retrieval-augmented generation pipeline using an evaluator model and built-in metrics",
        "from": "retrieve-and-generate RAG evaluation job"
      },
      {
        "relation": "relatesTo",
        "to": "retrieve-only RAG evaluation job",
        "to_description": "An Amazon Bedrock evaluation job that assesses retrieval quality from a Knowledge Base without generating a full model response",
        "from": "retrieve-and-generate RAG evaluation job"
      }
    ]
  }
}
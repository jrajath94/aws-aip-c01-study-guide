{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-data.html",
      "title": "embedding model",
      "context": "A model hosted on Amazon Bedrock or a SageMaker endpoint that generates vector embeddings for document chunks ingested into the search engine",
      "recommended_sections": [
        "Unstructured data",
        "Structured data"
      ],
      "sections": [
        "Turning data into a knowledge base",
        "Unstructured data",
        "Structured data"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html",
      "title": "ingestion job",
      "context": "An Amazon Bedrock Knowledge Bases process that crawls documents through the access point, generates embeddings, and indexes them in the vector store.",
      "recommended_sections": [
        "Sync your data with your Amazon Bedrock knowledge base"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html",
      "title": "knowledge base data source",
      "context": "An external data repository connected to an Amazon Bedrock knowledge base from which content is ingested and converted into vector embeddings.",
      "recommended_sections": null,
      "sections": [
        "Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases",
        "Use the console",
        "Use the API"
      ],
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/tutorial-build-rag-with-bedrock.html",
      "title": "Ingest the documents",
      "context": "Start and monitor an Amazon Bedrock Knowledge Bases ingestion job that crawls documents through the access point and indexes their embeddings in the vector store.",
      "recommended_sections": [
        "Step 5: Ingest the documents"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html",
      "title": "Amazon Bedrock managed knowledge base",
      "context": "A fully managed RAG solution within Amazon Bedrock with built-in connectors, smart parsing, managed vector store, hybrid search, and native RetrieveAndGenerate and Agentic Retrieval APIs",
      "recommended_sections": [
        "Build a knowledge base with vector stores"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html",
      "title": "How content chunking works for knowledge bases",
      "context": "Understand and configure the chunking strategies available for ingesting documents into Amazon Bedrock Knowledge Bases.",
      "recommended_sections": [
        "How content chunking works for knowledge bases"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/creating-a-knowledge-base-component.html",
      "title": "Amazon Bedrock Knowledge Base component",
      "context": "A component in SageMaker Unified Studio that uses an embeddings model, vector store, and parsing to enable knowledge retrieval in chat agent applications",
      "recommended_sections": [
        "Create an Amazon Bedrock Knowledge Base component"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal.html",
      "title": "multimodal knowledge base",
      "context": "An Amazon Bedrock Knowledge Base configured to process and retrieve multimodal content including images, audio, and video using vector embeddings.",
      "recommended_sections": [
        "How it works"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 9,
      "url": "https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html",
      "title": "Architecture Comparison between Amazon Kendra and Bedrock Managed Knowledge Base",
      "context": "A feature comparison table showing differences between Kendra and BMKB across connectors, embedding, vector store, search type, RAG support, agentic retrieval, and maximum results",
      "recommended_sections": [
        "Amazon Bedrock Managed Knowledge Base Features"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 10,
      "url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-getting-started.html",
      "title": "Amazon Bedrock Knowledge Bases provides a fully managed end-to-end RAG workflow.",
      "context": "Description of how Amazon Bedrock Knowledge Bases automates data ingestion, embedding generation, and vector storage when integrated with S3 Vectors",
      "recommended_sections": [
        "Create an Amazon Bedrock knowledge base with S3 Vectors in the console"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "96407690-1af1-49f7-953d-bb4c8d3fcd8f",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "50 MB per document limit",
        "to_description": "Amazon Bedrock Knowledge Bases maximum file size constraint that causes files exceeding 50 MB to be skipped during ingestion.",
        "from": "Ingest the documents"
      },
      {
        "relation": "dependsOn",
        "to": "Create the knowledge base and data source",
        "to_description": "Create an Amazon Bedrock knowledge base configured with the embedding model and vector store, and attach a data source pointing to the S3 access point alias.",
        "from": "Ingest the documents"
      },
      {
        "relation": "references",
        "to": "ingestion job",
        "to_description": "An Amazon Bedrock Knowledge Bases process that crawls documents through the access point, generates embeddings, and indexes them in the vector store.",
        "from": "Ingest the documents"
      },
      {
        "relation": "hasChild",
        "to": "start-ingestion-job CLI command",
        "to_description": "Start an Amazon Bedrock Knowledge Bases ingestion job for a specified knowledge base and data source using the AWS CLI.",
        "from": "Ingest the documents"
      },
      {
        "relation": "references",
        "to": "GetIngestionJob",
        "to_description": "Gets information about a data ingestion job. Data sources are ingested into your knowledge base so that Large Language Models (LLMs) can use your data.",
        "from": "Ingest the documents"
      }
    ]
  }
}
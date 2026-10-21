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
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-getting-started.html",
      "title": "Amazon Bedrock Knowledge Bases provides a fully managed end-to-end RAG workflow.",
      "context": "Description of how Amazon Bedrock Knowledge Bases automates data ingestion, embedding generation, and vector storage when integrated with S3 Vectors",
      "recommended_sections": [
        "Create an Amazon Bedrock knowledge base with S3 Vectors in the console",
        "Prerequisites"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-bedrock-kb.html",
      "title": "vector embeddings",
      "context": "Non-atomic and unisolated data changes in Neptune Analytics where inserts, deletes, and updates become durable on write and visible to all queries immediately",
      "recommended_sections": [
        "Supported embedding models",
        "Integration overview"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html",
      "title": "chunking",
      "context": "A preprocessing technique that splits documents into manageable text chunks for efficient data retrieval and vector indexing in Amazon Bedrock knowledge bases",
      "recommended_sections": [
        "How content chunking works for knowledge bases"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html",
      "title": "embeddings model",
      "context": "An Amazon Bedrock model that generates vector embeddings whose dimensions must match the Neptune Analytics vector search index configuration",
      "recommended_sections": [
        "Build a knowledge base with vector stores"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
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
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/tutorial-build-rag-with-bedrock.html",
      "title": "Create a vector store",
      "context": "Create an Amazon S3 Vectors vector bucket and index (or OpenSearch Service Serverless collection) to store document embeddings for the knowledge base.",
      "recommended_sections": [
        "Step 2: Create a vector store"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "47282e77-4d26-45b8-880b-c21401ce6c93",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "BMKB hybrid search",
        "to_description": "BMKB's default search mode that always combines keyword and semantic search and does not offer semantic-only mode",
        "from": "Architecture Comparison between Amazon Kendra and Bedrock Managed Knowledge Base"
      },
      {
        "relation": "references",
        "to": "BMKB agentic retrieval",
        "to_description": "Native BMKB capability for multi-step reasoning and multi-iteration retrieval across multiple knowledge bases",
        "from": "Architecture Comparison between Amazon Kendra and Bedrock Managed Knowledge Base"
      },
      {
        "relation": "relatesTo",
        "to": "vector embeddings",
        "to_description": "Non-atomic and unisolated data changes in Neptune Analytics where inserts, deletes, and updates become durable on write and visible to all queries immediately",
        "from": "embeddings model"
      },
      {
        "relation": "relatesTo",
        "to": "multimodal data",
        "to_description": "A combination of text and visual data, such as documents containing tables, charts, diagrams, and images, supported by Amazon Bedrock Knowledge Bases",
        "from": "embeddings model"
      },
      {
        "relation": "relatesTo",
        "to": "vector dimensions",
        "to_description": "The number of dimensions in each embedding vector, which must match between the Neptune Analytics graph configuration and the chosen embeddings model",
        "from": "embeddings model"
      }
    ]
  }
}
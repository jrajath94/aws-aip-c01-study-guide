{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs.html",
      "title": "GraphRAG",
      "context": "A fully managed capability in Amazon Bedrock Knowledge Bases that automatically creates embeddings for semantic search, generates graphs of entities and relationships from unstructured data, and combines vector search with graph traversal.",
      "recommended_sections": [
        "GraphRAG Region availability",
        "GraphRAG considerations and limitations"
      ],
      "sections": [
        "Build a knowledge base with Amazon Neptune Analytics graphs",
        "GraphRAG Region availability",
        "Benefits of using GraphRAG",
        "How GraphRAG works",
        "GraphRAG considerations and limitations"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs-build.html",
      "title": "Create an Amazon Bedrock knowledge base with Amazon Neptune Analytics graphs",
      "context": "A procedure to set up a GraphRAG-enabled knowledge base using Amazon Neptune Analytics as the vector store via the console or CLI",
      "recommended_sections": [
        "Create an Amazon Bedrock knowledge base with Amazon Neptune Analytics graphs",
        "Test your knowledge base"
      ],
      "sections": [
        "Create an Amazon Bedrock knowledge base with Amazon Neptune Analytics graphs",
        "Choose and update the graph construction model",
        "Sync your data source",
        "Ingest changes into your knowledge base",
        "Test your knowledge base"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/core-services-knowledge-bases.html",
      "title": "GraphRAG",
      "context": "A fully managed capability in Amazon Bedrock Knowledge Bases that automatically creates embeddings for semantic search, generates graphs of entities and relationships from unstructured data, and combines vector search with graph traversal.",
      "recommended_sections": [
        "Graph database"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-neptune.html",
      "title": "Amazon Neptune Analytics graph knowledge base",
      "context": "A Bedrock knowledge base backed by an Amazon Neptune Analytics graph that returns structured retrieval results with Neptune-specific metadata fields",
      "recommended_sections": [
        "Query a knowledge base connected to an Amazon Neptune Analytics graph"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/prescriptive-guidance/latest/rag-healthcare-use-cases/resources.html",
      "title": "Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune",
      "context": "AWS blog post on using knowledge graphs to build GraphRAG applications combining Amazon Bedrock and Amazon Neptune",
      "recommended_sections": [
        "AWS blog posts"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "1b4ead8e-7401-44c0-9c21-d8f8eaa45b1a",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "GraphRAG",
        "to_description": "A fully managed capability in Amazon Bedrock Knowledge Bases that automatically creates embeddings for semantic search, generates graphs of entities and relationships from unstructured data, and combines vector search with graph traversal.",
        "from": "Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune"
      },
      {
        "relation": "references",
        "to": "knowledge graph",
        "to_description": "Graph structure built from indexing connected repositories that captures cross-repository dependencies, shared resources, API contracts, and infrastructure relationships",
        "from": "Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune"
      },
      {
        "relation": "relatesTo",
        "to": "NeptuneAnalyticsFieldMapping",
        "to_description": "A CloudFormation property type that maps vector store information to named fields in Amazon Neptune Analytics for an Amazon Bedrock knowledge base",
        "from": "Neptune Analytics vector store"
      },
      {
        "relation": "relatesTo",
        "to": "GraphRAG metadata filter",
        "to_description": "A filter applied during Neptune Analytics vector search retrieval to narrow down candidate nodes based on document metadata properties",
        "from": "Neptune Analytics vector store"
      },
      {
        "relation": "references",
        "to": "CreateKnowledgeBase",
        "to_description": "Creates a knowledge base. A knowledge base contains your data sources so that Large Language Models (LLMs) can use your data. To create a knowledge base, you must first set up your data sources and configure a supported vector store. For more information, see Set up a knowledge base . To create a managed knowledge base, provide a managedKnowledgeBaseConfiguration during creation. For more information, see Build a managed knowledge base . Provide the name and an optional description . Provide…",
        "from": "Create an Amazon Bedrock knowledge base with Amazon Neptune Analytics graphs"
      }
    ]
  }
}
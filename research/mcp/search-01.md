{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html",
      "title": "Representation | Value table",
      "context": "Illustrates the same text represented as raw text, a floating-point vector, and a binary vector to show how embeddings encode content.",
      "recommended_sections": [
        "How Amazon Bedrock knowledge bases work"
      ],
      "sections": [
        "How Amazon Bedrock knowledge bases work"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-data.html",
      "title": "specific query improves accuracy content",
      "context": "Explains that more specific or detailed queries allow the knowledge base to narrow down the exact information to return",
      "recommended_sections": null,
      "sections": [
        "Turning data into a knowledge base",
        "Unstructured data",
        "Structured data"
      ],
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html",
      "title": "managed knowledge base",
      "context": "A knowledge base type where Amazon Bedrock manages the underlying data ingestion, indexing, storage, and retrieval infrastructure with advanced capabilities including multi-modal data ingestion and agentic retrieval.",
      "recommended_sections": [
        "Retrieve data and generate AI responses with Amazon Bedrock Knowledge Bases"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html",
      "title": "InvokeModel",
      "context": "Invokes the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings. For example code, see Invoke model code examples in the Amazon Bedrock User Guide . This operation requires permission for the bedrock:InvokeModel action. To deny all inference access to resources that you specify in the modelId field, you need to deny access to the bedrock:InvokeModel and…",
      "recommended_sections": [
        "Retrieving information from data sources using Amazon Bedrock Knowledge Bases"
      ],
      "sections": [
        "Retrieving information from data sources using Amazon Bedrock Knowledge Bases"
      ],
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html",
      "title": "agentic retrieval",
      "context": "A Managed Knowledge Base capability that supports multi-hop reasoning by decomposing complex queries into sub-queries and retrieving iteratively across multiple knowledge bases.",
      "recommended_sections": [
        "Use agentic retrieval to query a knowledge base"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "7257d3e9-96c0-4d79-b526-61222e483b79",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "relatesTo",
        "to": "knowledge base data repository",
        "to_description": "External data source connected to an Amazon Bedrock Knowledge Base to provide content for RAG ingestion and retrieval",
        "from": "RAG workflow"
      },
      {
        "relation": "relatesTo",
        "to": "retrieval instruction",
        "to_description": "A configuration object in Amazon Bedrock Knowledge Bases that provides instructions for how retrieval should be performed",
        "from": "managed knowledge base"
      },
      {
        "relation": "relatesTo",
        "to": "hybrid search",
        "to_description": "A search capability in AWS Agent Registry that combines semantic understanding with keyword matching to return relevant results for both natural language queries and exact name lookups.",
        "from": "managed knowledge base"
      },
      {
        "relation": "relatesTo",
        "to": "Neptune Analytics graph",
        "to_description": "A graph database resource in Amazon Neptune Analytics that stores entities, relationships, and vector embeddings extracted from documents",
        "from": "GraphRAG"
      },
      {
        "relation": "relatesTo",
        "to": "retrieval instruction",
        "to_description": "A configuration object in Amazon Bedrock Knowledge Bases that provides instructions for how retrieval should be performed",
        "from": "agentic retrieval"
      }
    ]
  }
}
{
  "search_results": [
    {
      "rank_order": 1,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_RetrievalFilter.html",
      "title": "RetrievalFilter",
      "context": "A runtime API construct in Amazon Bedrock that specifies filter conditions for metadata-based filtering of knowledge base query results",
      "recommended_sections": [
        "RetrievalFilter"
      ],
      "sections": [
        "RetrievalFilter",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 2,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html",
      "title": "knowledge base metadata filtering",
      "context": "A feature of Amazon Bedrock Knowledge Bases that allows filtering retrieval results based on document metadata attributes using filtering and logical operators.",
      "recommended_sections": [
        "Manual metadata filtering",
        "Implicit metadata filtering"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 3,
      "url": "https://docs.aws.amazon.com/connect/latest/adminguide/multiple-knowledge-base-setup-and-content-segmentation.html",
      "title": "Bedrock knowledge base metadata fields",
      "context": "Built-in and custom metadata fields on Bedrock knowledge base data sources used to filter retrieval results in the Retrieve tool.",
      "recommended_sections": [
        "Using metadata fields in the Retrieve tool",
        "Bedrock knowledge base"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 4,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-neptune.html",
      "title": "Using metadata and filtering",
      "context": "Filter knowledge base query results by metadata conditions using the Amazon Bedrock RetrievalFilter API when querying a Neptune Analytics graph-backed knowledge base",
      "recommended_sections": [
        "Using metadata and filtering"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 5,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrievalFilter.html",
      "title": "RetrievalFilter",
      "context": "A runtime API construct in Amazon Bedrock that specifies filter conditions for metadata-based filtering of knowledge base query results",
      "recommended_sections": [
        "RetrievalFilter"
      ],
      "sections": [
        "RetrievalFilter",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 6,
      "url": "https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-test-config.html",
      "title": "RetrievalFilter",
      "context": "A runtime API construct in Amazon Bedrock that specifies filter conditions for metadata-based filtering of knowledge base query results",
      "recommended_sections": [
        "Manual metadata filtering"
      ],
      "sections": null,
      "metadata": null
    },
    {
      "rank_order": 7,
      "url": "https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FilterAttribute.html",
      "title": "FilterAttribute",
      "context": "A metadata attribute/field name-value pair used to apply filters against data source or document metadata in Amazon Bedrock",
      "recommended_sections": null,
      "sections": [
        "FilterAttribute",
        "Contents",
        "See Also"
      ],
      "metadata": null
    },
    {
      "rank_order": 8,
      "url": "https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html",
      "title": "BMKB metadata filter",
      "context": "A structured filter syntax used in BMKB retrieve calls to narrow results by document metadata attributes using operators like equals, greaterThan, andAll, and orAll",
      "recommended_sections": [
        "Metadata Filter Syntax Translation"
      ],
      "sections": null,
      "metadata": null
    }
  ],
  "facets": null,
  "query_id": "38c83efa-7d14-4014-a424-12a915ef8b37",
  "metadata": {
    "discovered_services": null,
    "related_tasks": null,
    "relationships": [
      {
        "relation": "references",
        "to": "RetrievalFilter",
        "to_description": "A runtime API construct in Amazon Bedrock that specifies filter conditions for metadata-based filtering of knowledge base query results",
        "from": "Using metadata and filtering"
      },
      {
        "relation": "references",
        "to": "metadata filtering",
        "to_description": "Amazon Bedrock Knowledge Bases capability that pre-filters the vector store based on document metadata before searching for relevant documents to enforce access control",
        "from": "Using metadata and filtering"
      },
      {
        "relation": "references",
        "to": "Amazon Neptune Analytics graph knowledge base",
        "to_description": "A Bedrock knowledge base backed by an Amazon Neptune Analytics graph that returns structured retrieval results with Neptune-specific metadata fields",
        "from": "Using metadata and filtering"
      },
      {
        "relation": "references",
        "to": "stringContains filter list variant",
        "to_description": "The list variant of the stringContains RetrievalFilter condition that is not supported for Neptune Analytics graphs",
        "from": "Using metadata and filtering"
      },
      {
        "relation": "hasChild",
        "to": "\"vectorSearchConfiguration\": { \"numberOfResults\": 5, \"filter\": { \"orAll\": [ { \"andAll\": [ { \"equals\": { \"key\": \"genre\", \"value\": \"entertainment\" } }, { \"greaterThan\": { \"key\": \"year\", \"value\": 2018 } } ] }, { \"andAll\": [ { \"startsWith\": { \"key\": \"author\", \"value\": \"C\" } } ] } ] } } }",
        "to_description": "Configure a vectorSearchConfiguration with a nested orAll/andAll RetrievalFilter combining equals, greaterThan, and startsWith conditions for a Neptune Analytics knowledge base query",
        "from": "Using metadata and filtering"
      }
    ]
  }
}
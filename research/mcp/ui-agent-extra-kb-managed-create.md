AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html:

# Build a knowledge base with vector stores

###### Important

For optimized retrieval accuracy and a managed experience, we recommend [Amazon Bedrock Managed Knowledge Base](./kb-build-managed.html).

Amazon Bedrock Knowledge Bases supports a variety of file types stored in data sources. To interpret the data from a data source,
Amazon Bedrock Knowledge Bases requires the conversion of the data into vector embeddings, a numerical representation of the data. These embeddings can be compared to
the vector representations of a query to assess similarity and determine which sources to return during data retrieval.

Connecting your knowledge base to a data source involves the following general steps:

1. Connect the knowledge base to a supported data source.
2. If your data source contains multimodal data, including images, audio, and video files, you must choose an appropriate processing approach and embedding model that supports multimodal content.

   ###### Note

   Multimodal data is only supported with Amazon S3 and custom data sources. For comprehensive guidance on working with multimodal content, see [Build a knowledge base for multimodal content](./kb-multimodal.html).
3. Choose an embeddings model to convert the data in the data source into vector embeddings.
4. Choose a vector store to store the vector representation of your data.
5. Sync your data so it's converted to vector embeddings.
6. If you modify the data in the data source, you must resync the changes.

###### Topics

* [Prerequisites for creating an Amazon Bedrock knowledge basewith a unstructured data source](./knowledge-base-prereq.html)
* [Prerequisites and permissions required for using OpenSearch Managed Clusters with Amazon Bedrock Knowledge Bases](./kb-osm-permissions-prereq.html)
* [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](./knowledge-base-create.html)
* [Sync your data with your Amazon Bedrock knowledge base](./kb-data-source-sync-ingest.html)
* [Ingest changes directly into a knowledge base](./kb-direct-ingestion.html)
* [View data source information for your Amazon Bedrock knowledge base](./kb-ds-info.html)
* [Modify a data source for your Amazon Bedrock knowledge base](./kb-ds-update.html)
* [Delete a data source from your Amazon Bedrock knowledge base](./kb-ds-delete.html)
* [Build a knowledge base for multimodal content](./kb-multimodal.html)
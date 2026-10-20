AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html:

# Retrieving information from data sources using Amazon Bedrock Knowledge Bases

###### Important

For optimized retrieval accuracy and a managed experience, we recommend [Amazon Bedrock Managed Knowledge Base](./kb-build-managed.html).

After setting up a knowledge base, you can set up your application to query the data sources in it. To query a knowledge base, you can take advantage of the following API operations:

* [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) – Retrieves the source chunks or images from your data that are most relevant to the query and returns them in the response as an array.
* [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) – Joins `Retrieve` with the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) operation in Amazon Bedrock to retrieve the source chunks from your data that are most relevant to the query and generate a natural language response. Includes citations to specific source chunks from the data. If your data source includes visual elements, the model use insights from these images when generating a text response and provide source attribution for the images.
* [GenerateQuery](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GenerateQuery.html) – Converts natural language user queries into queries that are in a form suitable for the structured data store.
* `AgenticRetrieveStream` – Uses a foundation model to decompose
  complex queries into sub-queries, iteratively retrieves relevant information from
  your knowledge bases, and evaluates whether the results are sufficient. Returns
  deduplicated source chunks along with trace events for observability.

The `RetrieveAndGenerate` operation is a combined action that underlyingly uses `GenerateQuery` (if your knowledge base is connected to a structured data store), `Retrieve` and `InvokeModel` to carry out the entire RAG process. Because Amazon Bedrock Knowledge Bases also provides you access to the `Retrieve` operation, you have the flexibility to decouple the steps in RAG and customize them for your specific use case.

You can also use a [reranking model](./rerank.html) when using `Retrieve` or `RetrieveAndGenerate` to rerank the relevance of documents retrieved during query.

To learn how to use these API operations when querying a knowledge base, see [Test your knowledge base with queries and responses](./knowledge-base-test.html).
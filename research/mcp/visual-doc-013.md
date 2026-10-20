AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ChunkingConfiguration.html:

# ChunkingConfiguration

Details about how to chunk the documents in the data source. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

## Contents

**chunkingStrategy**
:   Knowledge base can split your source data into chunks. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE`, then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.

    * `FIXED_SIZE` – Amazon Bedrock splits your source data into chunks of the approximate size that you set in the `fixedSizeChunkingConfiguration`.
    * `HIERARCHICAL` – Split documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
    * `SEMANTIC` – Split documents into chunks based on groups of similar content derived with natural language processing.
    * `NONE` – Amazon Bedrock treats each file as one chunk. If you choose this option, you may want to pre-process your documents by splitting them into separate files.

    Type: String

    Valid Values: `FIXED_SIZE | NONE | HIERARCHICAL | SEMANTIC`

    Required: Yes

**fixedSizeChunkingConfiguration**
:   Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE`, exclude this field.

    Type: [FixedSizeChunkingConfiguration](./API_agent_FixedSizeChunkingConfiguration.html) object

    Required: No

**hierarchicalChunkingConfiguration**
:   Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents
    into layers of chunks where the first layer contains large chunks, and the second layer contains smaller
    chunks derived from the first layer.

    Type: [HierarchicalChunkingConfiguration](./API_agent_HierarchicalChunkingConfiguration.html) object

    Required: No

**semanticChunkingConfiguration**
:   Settings for semantic document chunking for a data source. Semantic chunking splits
    a document into into smaller documents based on groups of similar content derived from the text
    with natural language processing.

    Type: [SemanticChunkingConfiguration](./API_agent_SemanticChunkingConfiguration.html) object

    Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ChunkingConfiguration)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ChunkingConfiguration)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ChunkingConfiguration)
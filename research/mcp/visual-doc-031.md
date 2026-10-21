AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_EvaluationPrecomputedRetrieveAndGenerateSourceConfig.html:

# EvaluationPrecomputedRetrieveAndGenerateSourceConfig

A summary of a RAG source used for a retrieve-and-generate Knowledge Base evaluation job where you provide your own inference response data.

## Contents

**ragSourceIdentifier**
:   A label that identifies the RAG source used for a retrieve-and-generate Knowledge Base evaluation job where you provide your own inference response data.

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 256.

    Pattern: `[a-zA-Z0-9]([a-zA-Z0-9._-]){0,255}`

    Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/EvaluationPrecomputedRetrieveAndGenerateSourceConfig)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/EvaluationPrecomputedRetrieveAndGenerateSourceConfig)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/EvaluationPrecomputedRetrieveAndGenerateSourceConfig)
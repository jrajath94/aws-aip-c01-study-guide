AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FunctionSchema.html:

# FunctionSchema

Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**functions**
:   A list of functions that each define an action in the action group.

    Type: Array of [FunctionDefinition](./API_agent-runtime_FunctionDefinition.html) objects

    Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FunctionSchema)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FunctionSchema)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FunctionSchema)
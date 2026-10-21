AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CustomizationConfig.html:

# CustomizationConfig

A model customization configuration

## Contents

###### Important

This data type is a UNION, so only one of the following members can be specified when used or returned.

**distillationConfig**
:   The Distillation configuration for the custom model.

    Type: [DistillationConfig](./API_DistillationConfig.html) object

    Required: No

**rftConfig**
:   Configuration settings for reinforcement fine-tuning (RFT) model customization, including grader configuration and hyperparameters.

    Type: [RFTConfig](./API_RFTConfig.html) object

    Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomizationConfig)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomizationConfig)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomizationConfig)
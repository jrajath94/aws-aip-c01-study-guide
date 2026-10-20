AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomation.html:

# InvokeDataAutomation

Process data with a data automation project or blueprints. The service processes data synchronously.
Output can either be returned inline or store in the output in the S3 bucket that you specify.

## Request Syntax

```
{
   "blueprints": [ 
      { 
         "blueprintArn": "string",
         "stage": "string",
         "version": "string"
      }
   ],
   "dataAutomationConfiguration": { 
      "dataAutomationProjectArn": "string",
      "stage": "string"
   },
   "dataAutomationProfileArn": "string",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "string" : "string" 
      },
      "kmsKeyId": "string"
   },
   "inputConfiguration": { 
      "bytes": blob,
      "s3Uri": "string"
   },
   "outputConfiguration": { 
      "s3Uri": "string"
   }
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](./CommonParameters.html).

The request accepts the following data in JSON format.

**[blueprints](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   A list of blueprints to apply to the data.

    Type: Array of [Blueprint](./API_data-automation-runtime_Blueprint.html) objects

    Array Members: Minimum number of 1 item. Maximum number of 40 items.

    Required: No

**[dataAutomationConfiguration](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   The data automation project to process the data with.

    Type: [DataAutomationConfiguration](./API_data-automation-runtime_DataAutomationConfiguration.html) object

    Required: No

**[dataAutomationProfileArn](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   The ARN of the profile calling your request.

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 128.

    Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-profile/[a-zA-Z0-9-_.]+`

    Required: Yes

**[encryptionConfiguration](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   Encryption settings for the invocation.

    Type: [EncryptionConfiguration](./API_data-automation-runtime_EncryptionConfiguration.html) object

    Required: No

**[inputConfiguration](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   Where to read the input data from.

    Type: [SyncInputConfiguration](./API_data-automation-runtime_SyncInputConfiguration.html) object

    Required: Yes

**[outputConfiguration](#API_data-automation-runtime_InvokeDataAutomation_RequestSyntax)**
:   Where to store the output.

    Type: [OutputConfiguration](./API_data-automation-runtime_OutputConfiguration.html) object

    Required: No

## Response Syntax

```
{
   "outputConfiguration": { 
      "s3Uri": "string"
   },
   "outputSegments": [ 
      { 
         "customOutput": "string",
         "customOutputStatus": "string",
         "standardOutput": "string"
      }
   ],
   "semanticModality": "string"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[outputConfiguration](#API_data-automation-runtime_InvokeDataAutomation_ResponseSyntax)**
:   Where to store the output.

    Type: [OutputConfiguration](./API_data-automation-runtime_OutputConfiguration.html) object

**[outputSegments](#API_data-automation-runtime_InvokeDataAutomation_ResponseSyntax)**
:   List of outputs for each logical sub-doc.

    Type: Array of [OutputSegment](./API_data-automation-runtime_OutputSegment.html) objects

**[semanticModality](#API_data-automation-runtime_InvokeDataAutomation_ResponseSyntax)**
:   Detected semantic modality.

    Type: String

    Valid Values: `DOCUMENT | IMAGE | AUDIO | VIDEO`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
:   HTTP Status Code: 400

**InternalServerException**
:   HTTP Status Code: 500

**ServiceUnavailableException**
:   HTTP Status Code: 500

**ThrottlingException**
:   HTTP Status Code: 400

**TooManyRequestsException**
:   HTTP Status Code: 400

**ValidationException**
:   HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomation)
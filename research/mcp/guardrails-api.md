AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html:

# ApplyGuardrail

The action to apply a guardrail.

For troubleshooting some of the common errors you might encounter when using the `ApplyGuardrail` API,
see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

## Request Syntax

```
POST /guardrail/guardrailIdentifier/version/guardrailVersion/apply HTTP/1.1
Content-type: application/json

{
   "content": [ 
      { ... }
   ],
   "outputScope": "string",
   "source": "string"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[guardrailIdentifier](#API_runtime_ApplyGuardrail_RequestSyntax)**
:   The guardrail identifier used in the request to apply the guardrail.

    Length Constraints: Minimum length of 0. Maximum length of 2048.

    Pattern: `(|([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`

    Required: Yes

**[guardrailVersion](#API_runtime_ApplyGuardrail_RequestSyntax)**
:   The guardrail version used in the request to apply the guardrail.

    Pattern: `(|([1-9][0-9]{0,7})|(DRAFT))`

    Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[content](#API_runtime_ApplyGuardrail_RequestSyntax)**
:   The content details used in the request to apply the guardrail.

    Type: Array of [GuardrailContentBlock](./API_runtime_GuardrailContentBlock.html) objects

    Required: Yes

**[outputScope](#API_runtime_ApplyGuardrail_RequestSyntax)**
:   Specifies the scope of the output that you get in the response. Set to `FULL` to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.

    Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).

    Type: String

    Valid Values: `INTERVENTIONS | FULL`

    Required: No

**[source](#API_runtime_ApplyGuardrail_RequestSyntax)**
:   The source of data used in the request to apply the guardrail.

    Type: String

    Valid Values: `INPUT | OUTPUT`

    Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "actionReason": "string",
   "assessments": [ 
      { 
         "appliedGuardrailDetails": { 
            "guardrailArn": "string",
            "guardrailId": "string",
            "guardrailOrigin": [ "string" ],
            "guardrailOwnership": "string",
            "guardrailVersion": "string"
         },
         "automatedReasoningPolicy": { 
            "findings": [ 
               { ... }
            ]
         },
         "contentPolicy": { 
            "filters": [ 
               { 
                  "action": "string",
                  "confidence": "string",
                  "detected": boolean,
                  "filterStrength": "string",
                  "type": "string"
               }
            ]
         },
         "contextualGroundingPolicy": { 
            "filters": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "score": number,
                  "threshold": number,
                  "type": "string"
               }
            ]
         },
         "invocationMetrics": { 
            "guardrailCoverage": { 
               "images": { 
                  "guarded": number,
                  "total": number
               },
               "textCharacters": { 
                  "guarded": number,
                  "total": number
               }
            },
            "guardrailProcessingLatency": number,
            "usage": { 
               "automatedReasoningPolicies": number,
               "automatedReasoningPolicyUnits": number,
               "contentPolicyImageUnits": number,
               "contentPolicyUnits": number,
               "contextualGroundingPolicyUnits": number,
               "sensitiveInformationPolicyFreeUnits": number,
               "sensitiveInformationPolicyUnits": number,
               "topicPolicyUnits": number,
               "wordPolicyUnits": number
            }
         },
         "sensitiveInformationPolicy": { 
            "piiEntities": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "match": "string",
                  "type": "string"
               }
            ],
            "regexes": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "match": "string",
                  "name": "string",
                  "regex": "string"
               }
            ]
         },
         "topicPolicy": { 
            "topics": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "name": "string",
                  "type": "string"
               }
            ]
         },
         "wordPolicy": { 
            "customWords": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "match": "string"
               }
            ],
            "managedWordLists": [ 
               { 
                  "action": "string",
                  "detected": boolean,
                  "match": "string",
                  "type": "string"
               }
            ]
         }
      }
   ],
   "guardrailCoverage": { 
      "images": { 
         "guarded": number,
         "total": number
      },
      "textCharacters": { 
         "guarded": number,
         "total": number
      }
   },
   "outputs": [ 
      { 
         "text": "string"
      }
   ],
   "usage": { 
      "automatedReasoningPolicies": number,
      "automatedReasoningPolicyUnits": number,
      "contentPolicyImageUnits": number,
      "contentPolicyUnits": number,
      "contextualGroundingPolicyUnits": number,
      "sensitiveInformationPolicyFreeUnits": number,
      "sensitiveInformationPolicyUnits": number,
      "topicPolicyUnits": number,
      "wordPolicyUnits": number
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[action](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The action taken in the response from the guardrail.

    Type: String

    Valid Values: `NONE | GUARDRAIL_INTERVENED`

**[actionReason](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The reason for the action taken when harmful content is detected.

    Type: String

**[assessments](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The assessment details in the response from the guardrail.

    Type: Array of [GuardrailAssessment](./API_runtime_GuardrailAssessment.html) objects

**[guardrailCoverage](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The guardrail coverage details in the apply guardrail response.

    Type: [GuardrailCoverage](./API_runtime_GuardrailCoverage.html) object

**[outputs](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The output details in the response from the guardrail.

    Type: Array of [GuardrailOutputContent](./API_runtime_GuardrailOutputContent.html) objects

**[usage](#API_runtime_ApplyGuardrail_ResponseSyntax)**
:   The usage details in the response from the guardrail.

    Type: [GuardrailUsage](./API_runtime_GuardrailUsage.html) object

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
:   The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error,
    see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide

    HTTP Status Code: 403

**InternalServerException**
:   An internal server error occurred. For troubleshooting this error,
    see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide

    HTTP Status Code: 500

**ResourceNotFoundException**
:   The specified resource ARN was not found. For troubleshooting this error,
    see [ResourceNotFound](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found) in the Amazon Bedrock User Guide

    HTTP Status Code: 404

**ServiceQuotaExceededException**
:   Your request exceeds the service quota for your account. You can view your quotas at [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html). You can resubmit your request later.

    HTTP Status Code: 400

**ServiceUnavailableException**
:   The service isn't currently available. For troubleshooting this error,
    see [ServiceUnavailable](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable) in the Amazon Bedrock User Guide

    HTTP Status Code: 503

**ThrottlingException**
:   Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For
    troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide

    HTTP Status Code: 429

**ValidationException**
:   The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error,
    see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide

    HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ApplyGuardrail)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ApplyGuardrail)
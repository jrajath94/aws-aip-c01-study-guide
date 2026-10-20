AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html:

# Retrieve

Queries a knowledge base and retrieves information from it.

## Request Syntax

```
POST /knowledgebases/knowledgeBaseId/retrieve HTTP/1.1
Content-type: application/json

{
   "guardrailConfiguration": { 
      "guardrailId": "string",
      "guardrailVersion": "string"
   },
   "nextToken": "string",
   "retrievalConfiguration": { 
      "managedSearchConfiguration": { 
         "filter": { ... },
         "numberOfResults": number,
         "rerankingConfiguration": { 
            "bedrockRerankingConfiguration": { 
               "metadataConfiguration": { 
                  "selectionMode": "string",
                  "selectiveModeConfiguration": { ... }
               },
               "modelConfiguration": { 
                  "additionalModelRequestFields": { 
                     "string" : JSON value 
                  },
                  "modelArn": "string"
               },
               "numberOfRerankedResults": number
            },
            "type": "string"
         },
         "rerankingModelType": "string"
      },
      "vectorSearchConfiguration": { 
         "filter": { ... },
         "implicitFilterConfiguration": { 
            "metadataAttributes": [ 
               { 
                  "description": "string",
                  "key": "string",
                  "type": "string"
               }
            ],
            "modelArn": "string"
         },
         "numberOfResults": number,
         "overrideSearchType": "string",
         "rerankingConfiguration": { 
            "bedrockRerankingConfiguration": { 
               "metadataConfiguration": { 
                  "selectionMode": "string",
                  "selectiveModeConfiguration": { ... }
               },
               "modelConfiguration": { 
                  "additionalModelRequestFields": { 
                     "string" : JSON value 
                  },
                  "modelArn": "string"
               },
               "numberOfRerankedResults": number
            },
            "type": "string"
         }
      }
   },
   "retrievalQuery": { 
      "image": { 
         "format": "string",
         "inlineContent": blob
      },
      "text": "string",
      "type": "string"
   },
   "userContext": { 
      "userId": "string"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[knowledgeBaseId](#API_agent-runtime_Retrieve_RequestSyntax)**
:   The unique identifier of the knowledge base to query.

    Length Constraints: Minimum length of 10. Maximum length of 2048.

    Pattern: `[0-9a-zA-Z]{10}$|^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:knowledge-base/[0-9a-zA-Z]{10}`

    Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[guardrailConfiguration](#API_agent-runtime_Retrieve_RequestSyntax)**
:   Guardrail settings.

    Type: [GuardrailConfiguration](./API_agent-runtime_GuardrailConfiguration.html) object

    Required: No

**[nextToken](#API_agent-runtime_Retrieve_RequestSyntax)**
:   If there are more results than can fit in the response, the response returns a `nextToken`. Use this token in the `nextToken` field of another request to retrieve the next batch of results.

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 2048.

    Pattern: `\S*`

    Required: No

**[retrievalConfiguration](#API_agent-runtime_Retrieve_RequestSyntax)**
:   Contains configurations for the knowledge base query and retrieval process. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

    Type: [KnowledgeBaseRetrievalConfiguration](./API_agent-runtime_KnowledgeBaseRetrievalConfiguration.html) object

    Required: No

**[retrievalQuery](#API_agent-runtime_Retrieve_RequestSyntax)**
:   Contains the query to send the knowledge base.

    Type: [KnowledgeBaseQuery](./API_agent-runtime_KnowledgeBaseQuery.html) object

    Required: Yes

**[userContext](#API_agent-runtime_Retrieve_RequestSyntax)**
:   Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.

    Type: [UserContext](./API_agent-runtime_UserContext.html) object

    Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "guardrailAction": "string",
   "nextToken": "string",
   "retrievalResults": [ 
      { 
         "content": { 
            "audio": { 
               "s3Uri": "string",
               "transcription": "string"
            },
            "byteContent": "string",
            "row": [ 
               { 
                  "columnName": "string",
                  "columnValue": "string",
                  "type": "string"
               }
            ],
            "text": "string",
            "type": "string",
            "video": { 
               "s3Uri": "string",
               "summary": "string"
            }
         },
         "documentId": "string",
         "location": { 
            "confluenceLocation": { 
               "url": "string"
            },
            "customDocumentLocation": { 
               "id": "string"
            },
            "googleDriveLocation": { 
               "url": "string"
            },
            "kendraDocumentLocation": { 
               "uri": "string"
            },
            "oneDriveLocation": { 
               "url": "string"
            },
            "s3Location": { 
               "uri": "string"
            },
            "salesforceLocation": { 
               "url": "string"
            },
            "sharePointLocation": { 
               "url": "string"
            },
            "sqlLocation": { 
               "query": "string"
            },
            "type": "string",
            "webLocation": { 
               "url": "string"
            }
         },
         "metadata": { 
            "string" : JSON value 
         },
         "score": number
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[guardrailAction](#API_agent-runtime_Retrieve_ResponseSyntax)**
:   Specifies if there is a guardrail intervention in the response.

    Type: String

    Valid Values: `INTERVENED | NONE`

**[nextToken](#API_agent-runtime_Retrieve_ResponseSyntax)**
:   If there are more results than can fit in the response, the response returns a `nextToken`. Use this token in the `nextToken` field of another request to retrieve the next batch of results.

    Type: String

    Length Constraints: Minimum length of 1. Maximum length of 2048.

    Pattern: `\S*`

**[retrievalResults](#API_agent-runtime_Retrieve_ResponseSyntax)**
:   A list of results from querying the knowledge base.

    Type: Array of [KnowledgeBaseRetrievalResult](./API_agent-runtime_KnowledgeBaseRetrievalResult.html) objects

## Errors

For information about the errors that are common to all actions, see [Common Error Types](./CommonErrors.html).

**AccessDeniedException**
:   The request is denied because of missing access permissions. Check your permissions and retry your request.

    HTTP Status Code: 403

**BadGatewayException**
:   There was an issue with a dependency due to a server issue. Retry your request.

    **resourceName**
    :   The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.

    HTTP Status Code: 502

**ConflictException**
:   There was a conflict performing an operation. Resolve the conflict and retry your request.

    HTTP Status Code: 409

**DependencyFailedException**
:   There was an issue with a dependency. Check the resource configurations and retry the request.

    **resourceName**
    :   The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.

    HTTP Status Code: 424

**InternalServerException**
:   An internal server error occurred. Retry your request.

    **reason**
    :   The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.

    HTTP Status Code: 500

**ResourceNotFoundException**
:   The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.

    HTTP Status Code: 404

**ServiceQuotaExceededException**
:   The number of requests exceeds the service quota. Resubmit your request later.

    HTTP Status Code: 400

**ThrottlingException**
:   The number of requests exceeds the limit. Resubmit your request later.

    HTTP Status Code: 429

**ValidationException**
:   Input validation failed. Check your request parameters and retry the request.

    HTTP Status Code: 400

## Examples

### Send a basic query

The following example queries a knowledge base.

#### Sample Request

```
POST /knowledgebases/KB12345678/retrieve HTTP/1.1
Content-type: application/json

{
    "retrievalQuery": {
        "text": "What is AWS?"
    }
}
```

### Send a query and include filters

To include filters in a knowledge base query, at least one of the data source files must include a `.metadata.json` file. For example, if you had a data source of articles called `articles.pdf`, accompanied by a metadata file called `articles.pdf.metadata.json`, you could tag it for `genre`, `year`, and `author`. In the `Retrieve` request, you could apply the following filter to return all entertainment articles written after `2018`, in addition to `cooking` or `sports` articles written by authors starting with `C`.

#### Sample Request

```
POST /knowledgebases/KB12345678/retrieve HTTP/1.1
Content-type: application/json

{
    "retrievalQuery": {
        "text": "What is AWS?",
    },
    "vectorSearchConfiguration": {
        "numberOfResults": 5,
        "filter": {
            "orAll": [
                {
                    "andAll": [
                        {
                            "equals": {
                                "key": "genre",
                                "value": "entertainment"
                            }
                        },
                        {
                            "greaterThan": {
                                "key": "year",
                                "value": 2018
                            }
                        }
                    ]
                },
                {
                    "andAll": [
                        {
                            "in": {
                                "key": "genre",
                                "value": ["cooking", "sports"]
                            }
                        },
                        {
                            "startsWith": {
                                "key": "author",
                                "value": "C"
                            }
                        }
                    ]
                }
            ]
        }
    }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/Retrieve)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Retrieve)
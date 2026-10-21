AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html:

# RetrieveAndGenerate

Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). The response only cites sources that are relevant to the query.

###### Note

This API cannot be used with managed knowledge bases. Use [AgenticRetrieveStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html) or [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) with managed knowledge bases.

## Request Syntax

```
POST /retrieveAndGenerate HTTP/1.1
Content-type: application/json

{
   "input": { 
      "text": "string"
   },
   "retrieveAndGenerateConfiguration": { 
      "externalSourcesConfiguration": { 
         "generationConfiguration": { 
            "additionalModelRequestFields": { 
               "string" : JSON value 
            },
            "guardrailConfiguration": { 
               "guardrailId": "string",
               "guardrailVersion": "string"
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": number,
                  "stopSequences": [ "string" ],
                  "temperature": number,
                  "topP": number
               }
            },
            "performanceConfig": { 
               "latency": "string"
            },
            "promptTemplate": { 
               "textPromptTemplate": "string"
            }
         },
         "modelArn": "string",
         "sources": [ 
            { 
               "byteContent": { 
                  "contentType": "string",
                  "data": blob,
                  "identifier": "string"
               },
               "s3Location": { 
                  "uri": "string"
               },
               "sourceType": "string"
            }
         ]
      },
      "knowledgeBaseConfiguration": { 
         "generationConfiguration": { 
            "additionalModelRequestFields": { 
               "string" : JSON value 
            },
            "guardrailConfiguration": { 
               "guardrailId": "string",
               "guardrailVersion": "string"
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": number,
                  "stopSequences": [ "string" ],
                  "temperature": number,
                  "topP": number
               }
            },
            "performanceConfig": { 
               "latency": "string"
            },
            "promptTemplate": { 
               "textPromptTemplate": "string"
            }
         },
         "knowledgeBaseId": "string",
         "modelArn": "string",
         "orchestrationConfiguration": { 
            "additionalModelRequestFields": { 
               "string" : JSON value 
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": number,
                  "stopSequences": [ "string" ],
                  "temperature": number,
                  "topP": number
               }
            },
            "performanceConfig": { 
               "latency": "string"
            },
            "promptTemplate": { 
               "textPromptTemplate": "string"
            },
            "queryTransformationConfiguration": { 
               "type": "string"
            }
         },
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
         }
      },
      "type": "string"
   },
   "sessionConfiguration": { 
      "kmsKeyArn": "string"
   },
   "sessionId": "string",
   "userContext": { 
      "userId": "string"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[input](#API_agent-runtime_RetrieveAndGenerate_RequestSyntax)**
:   Contains the query to be made to the knowledge base.

    Type: [RetrieveAndGenerateInput](./API_agent-runtime_RetrieveAndGenerateInput.html) object

    Required: Yes

**[retrieveAndGenerateConfiguration](#API_agent-runtime_RetrieveAndGenerate_RequestSyntax)**
:   Contains configurations for the knowledge base query and retrieval process. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

    Type: [RetrieveAndGenerateConfiguration](./API_agent-runtime_RetrieveAndGenerateConfiguration.html) object

    Required: No

**[sessionConfiguration](#API_agent-runtime_RetrieveAndGenerate_RequestSyntax)**
:   Contains details about the session with the knowledge base.

    Type: [RetrieveAndGenerateSessionConfiguration](./API_agent-runtime_RetrieveAndGenerateSessionConfiguration.html) object

    Required: No

**[sessionId](#API_agent-runtime_RetrieveAndGenerate_RequestSyntax)**
:   The unique identifier of the session. When you first make a `RetrieveAndGenerate` request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the `sessionId` yourself.

    Type: String

    Length Constraints: Minimum length of 2. Maximum length of 100.

    Pattern: `[0-9a-zA-Z._:-]+`

    Required: No

**[userContext](#API_agent-runtime_RetrieveAndGenerate_RequestSyntax)**
:   Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.

    Type: [UserContext](./API_agent-runtime_UserContext.html) object

    Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "citations": [ 
      { 
         "generatedResponsePart": { 
            "textResponsePart": { 
               "span": { 
                  "end": number,
                  "start": number
               },
               "text": "string"
            }
         },
         "retrievedReferences": [ 
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
               }
            }
         ]
      }
   ],
   "guardrailAction": "string",
   "output": { 
      "text": "string"
   },
   "sessionId": "string"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[citations](#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax)**
:   A list of segments of the generated response that are based on sources in the knowledge base, alongside information about the sources.

    Type: Array of [Citation](./API_agent-runtime_Citation.html) objects

**[guardrailAction](#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax)**
:   Specifies if there is a guardrail intervention in the response.

    Type: String

    Valid Values: `INTERVENED | NONE`

**[output](#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax)**
:   Contains the response generated from querying the knowledge base.

    Type: [RetrieveAndGenerateOutput](./API_agent-runtime_RetrieveAndGenerateOutput.html) object

**[sessionId](#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax)**
:   The unique identifier of the session. When you first make a `RetrieveAndGenerate` request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the `sessionId` yourself.

    Type: String

    Length Constraints: Minimum length of 2. Maximum length of 100.

    Pattern: `[0-9a-zA-Z._:-]+`

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

The following example uses the minimally required fields to generate a response after querying a knowledge base.

#### Sample Request

```
POST /retrieveAndGenerate HTTP/1.1
Content-type: application/json

{
    "input": {
        "text": "What is AWS?"
    },
    "retrieveAndGenerateConfiguration": {
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "KB12345678",
            "modelArn": "anthropic.claude-v2:1"
        },
        "type": "KNOWLEDGE_BASE"
    }
}
```

### Send a query and include filters

To include filters in a knowledge base query, at least one of the data source files must include a `.metadata.json` file. For example, if you had a data source of articles called `articles.pdf`, accompanied by a metadata file called `articles.pdf.metadata.json`, you could tag it for `genre`, `year`, and `author`. In the `Retrieve` request, you could apply the following filter to return all entertainment articles written after `2018`, in addition to `cooking` or `sports` articles written by authors starting with `C`.

#### Sample Request

```
POST /retrieveAndGenerate HTTP/1.1
Content-type: application/json

{
    "input": {
        "text": "What is AWS?",
    },
    "retrieveAndGenerateConfiguration": {
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "KB12345678",
            "modelArn": "anthropic.claude-v2:1",
            "retrievalConfiguration": {
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
        },
        "type": "KNOWLEDGE_BASE"
    }
}
```

### Use an inference profile when generating a response

The following example uses an inference profile in generating a response after querying a knowledge base.

#### Sample Request

```
POST /retrieveAndGenerate HTTP/1.1
Content-type: application/json

{
    "input": {
        "text": "What is AWS?"
    },
    "retrieveAndGenerateConfiguration": {
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "KB12345678",
            "modelArn": "arn:aws:bedrock:us-west-2:123456789012:inference-profile/us.anthropic.claude-3-5-sonnet-20240620-v1:0"
        },
        "type": "KNOWLEDGE_BASE"
    }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerate)
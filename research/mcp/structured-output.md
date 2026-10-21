AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html:

# Get validated JSON results from models

Structured outputs is a capability on Amazon Bedrock that ensures model responses conform to user-defined JSON schemas and tool definitions, reducing the need for custom parsing and validation mechanisms in production AI deployments.

## Benefits

Structured outputs addresses critical challenges in production AI applications:

* **Ensures schema compliance** – Eliminates error rates and retry loops from prompt-based approaches
* **Reduced development complexity** – Removes the need for custom parsing and validation logic
* **Lower operational costs** – Reduces failed requests and retries
* **Production reliability** – Enables confident deployment of AI applications requiring predictable, machine-readable outputs

## How it works

Structured outputs constrains model responses to follow a specific schema, ensuring valid, parseable output for downstream processing. You can use structured outputs through two complementary mechanisms:

### JSON Schema output format

For InvokeModel API with Anthropic Claude models, use the `output_config.format` request field. With open weight models, use the `response_format` request field. For Converse APIs, use the `outputConfig.textFormat` request field. The model's response will conform to the specified JSON schema.

### Strict tool use

Add the `strict: true` flag to tool definitions to enable schema validation on tool names and inputs. The model's tool calls will then follow the defined tool input schema.

These mechanisms can be used independently or together in the same request. Refer to [Bedrock API documentation](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) for more details.

### Request workflow

The following describes how Amazon Bedrock processes requests with structured outputs:

1. **Initial request** – You include either a JSON schema through the `outputConfig.textFormat`, `output_config.format`, or `response_format` parameter or a tool definition with the `strict: true` flag in your inference request.
2. **Schema validation** – Amazon Bedrock validates the JSON schema format against the supported JSON Schema Draft 2020-12 subset. If the schema contains unsupported features, Amazon Bedrock returns a 400 error immediately.
3. **First-time compilation** – For new schemas, Amazon Bedrock compiles the grammar, which may take up to a few minutes.
4. **Caching** – Successfully compiled grammars are cached for 24 hours from first access. Cached grammars are encrypted with AWS-managed keys.
5. **Subsequent requests** – Identical schemas from the same account use cached grammars, resulting in inference latency comparable to standard requests with minimal overhead.
6. **Response** – You receive standard inference responses with strict schema compliance.

## Supported JSON Schema features

The following JSON Schema Draft 2020-12 features are supported:

* All basic types: `object`, `array`, `string`, `integer`, `number`, `boolean`, `null`
* `enum` (strings, numbers, booleans, or nulls only)
* `const`, `anyOf`, `allOf` (with limitations)
* `$ref`, `$def`, and `definitions` (internal references only)
* String formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `uri`, `ipv4`, `ipv6`, `uuid`
* Array `minItems` (only values 0 and 1)

The following features are *not* supported:

* Recursive schemas
* External `$ref` references
* Numerical constraints (`minimum`, `maximum`, `multipleOf`)
* String constraints (`minLength`, `maxLength`)
* `additionalProperties` set to anything other than `false`

## Supported APIs or features

You can use structured outputs across the following Amazon Bedrock features:

| **API or feature** | **Supported** | **Notes** |
| --- | --- | --- |
| [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) APIs | Yes | Conversational inference. |
| [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) APIs | Yes | Single-turn inference. |
| Cross-Region inference | Yes | Works without any additional setup. |
| Batch inference | Yes | Works without any additional setup. |
| Anthropic Messages API on the `bedrock-mantle` endpoint (`https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`) | Yes | Supported for Anthropic Claude models through the `output_config.format` parameter. For Claude-specific guidance and examples, see [Structured outputs for Anthropic Claude models](./claude-messages-structured-outputs.html). |

###### Note

Structured outputs is incompatible with citations for Anthropic models. If you enable citations while using structured outputs, the model will return a 400 error.

###### Important

Some Geographic cross-Region inference profiles don't support structured outputs for every model. For example, structured outputs aren't supported for Claude Haiku 4.5 through the India (`in.anthropic`) inference profile. Check the [model card](./model-cards.html) for model-specific limitations.

## Supported models

To see which models support structured outputs, please go to
[models at a glance](./model-cards.html) and select the model you are interested in.

## Example requests

### JSON Schema output format

The following examples show how to use JSON Schema output format with structured outputs.

#### Converse API

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "Given the following unstructured data, extract it into the provided structure."
        },
        {
          "text": "..."
        }
      ]
    }
  ],
  "outputConfig": {
    "textFormat": {
      "type": "json_schema",
      "structure": {
        "jsonSchema": {
          "schema": "{\"type\": \"object\", \"properties\": {\"title\": {\"type\": \"string\", \"description\": \"title\"}, \"summary\": {\"type\": \"string\", \"description\": \"summary\"}, \"next_steps\": {\"type\": \"string\", \"description\": \"next steps\"}}, \"required\": [\"title\", \"summary\", \"next_steps\"], \"additionalProperties\": false}",
          "name": "data_extraction",
          "description": "Extract structured data from unstructured text"
        }
      }
    }
  }
}
```

#### InvokeModel (Anthropic Claude)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Given the following unstructured data, extract it into the provided structure."
        },
        {
          "type": "text",
          "text": "..."
        }
      ]
    }
  ],
  "max_tokens": 3000,
  "temperature": 1.0,
  "output_config": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "title"
          },
          "summary": {
            "type": "string",
            "description": "summary"
          },
          "next_steps": {
            "type": "string",
            "description": "next steps"
          }
        },
        "required": [
          "title",
          "summary",
          "next_steps"
        ],
        "additionalProperties": false
      }
    }
  }
}
```

#### InvokeModel (Open-weight models)

```
{
  "messages": [
    {
      "role": "user",
      "content": "Given the following unstructured data, extract it into the provided structure."
    },
    {
      "role": "user",
      "content": "..."
    }
  ],
  "inferenceConfig": {
    "maxTokens": 3000,
    "temperature": 1.0
  },
  "response_format": {
    "json_schema": {
      "name": "summarizer",
      "schema": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "title"
          },
          "summary": {
            "type": "string",
            "description": "summary"
          },
          "next_steps": {
            "type": "string",
            "description": "next steps"
          }
        },
        "required": [
          "title",
          "summary",
          "next_steps"
        ],
        "additionalProperties": false
      }
    },
    "type": "json_schema"
  }
}
```

### Strict tool use

The following examples show how to use the strict field with tool use.

#### Converse API

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What's the weather like in New York?"
        }
      ]
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "get_weather",
          "description": "Get the current weather for a specified location",
          "strict": true,
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": [
                    "fahrenheit",
                    "celsius"
                  ],
                  "description": "The temperature unit to use"
                }
              },
              "required": [
                "location",
                "unit"
              ]
            }
          }
        }
      }
    ]
  }
}
```

#### InvokeModel (Anthropic Claude)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What's the weather like in San Francisco?"
        }
      ]
    }
  ],
  "max_tokens": 3000,
  "temperature": 1.0,
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather for a specified location",
      "strict": true,
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "fahrenheit",
              "celsius"
            ],
            "description": "The temperature unit to use"
          }
        },
        "required": [
          "location",
          "unit"
        ],
        "additionalProperties": false
      }
    }
  ]
}
```

#### InvokeModel (Open-weight models)

```
{
  "messages": [
    {
      "role": "user",
      "content": "What's the weather like in San Francisco?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather for a specified location",
        "strict": true,
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": [
                "fahrenheit",
                "celsius"
              ],
              "description": "The temperature unit to use"
            }
          },
          "required": [
            "location",
            "unit"
          ]
        }
      }
    }
  ],
  "tool_choice": "auto",
  "max_tokens": 2000,
  "temperature": 1.0
}
```
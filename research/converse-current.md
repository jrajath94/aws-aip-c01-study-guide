Title: Inference using Converse API - Amazon Bedrock

URL Source: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html

Markdown Content:
Skip to main content
English
Preferences 
Contact Us
Feedback
Get started
Service guides
Developer tools
AI resources
Search
Create an AWS Account
Amazon Bedrock
User Guide
Overview
Quickstart
Models at a glance
Model availability & compatibility
Build
Inference endpoints
APIs
Making inference requests
Invoke API
Converse API
Responses API
Chat Completions API
Messages API
Inference parameters
Structured Outputs
Inference reasoning
Latency-optimized inference
Supported Regions and models
Tool use
Web Search
Projects
Workspaces
API keys
Model customization
Security, Guardrails, and Observability
Capacity and Performance
Track usage and costs
Additional capabilities
Managed agents by OpenAI
Code examples
References/Advanced
AWS Glossary
Document history
Documentation
Amazon Bedrock
User Guide
Documentation
Amazon Bedrock
User Guide
Inference using Converse API
 PDF
 RSS
 Markdown
Agent Setup
Focus mode

The Converse API is available on the bedrock-runtime endpoint only.

You can use the Amazon Bedrock Converse API to create conversational applications that send and receive messages to and from an Amazon Bedrock model. For example, you can create a chat bot that maintains a conversation over many turns and uses a persona or tone customization that is unique to your needs, such as a helpful technical support assistant.

To use the Converse API, you use the Converse or ConverseStream (for streaming responses) operations to send messages to a model. It is possible to use the existing base inference operations (InvokeModel or InvokeModelWithResponseStream) for conversation applications. However, the Converse API provides a consistent API that works with all Amazon Bedrock models that support messages. This means you can write code once and use it with different models. Should a model have unique inference parameters, the Converse API also allows you to pass those unique parameters in a model specific structure.

You can use the Converse API to implement tool use and guardrails in your applications.

Note

With Mistral AI and Meta models, the Converse API embeds your input in a model-specific prompt template that enables conversations.

Restrictions apply to the following operations: InvokeModel, InvokeModelWithResponseStream, Converse, and ConverseStream. See API restrictions for details.

For code examples, see the following:

Python examples for this topic – Converse API examples

Various languages and models – Code examples for Amazon Bedrock Runtime using AWS SDKs

Java tutorial – A Java developer's guide to Bedrock's new Converse API

JavaScript tutorial – A developer's guide to Bedrock's new Converse API

Using the Converse API

To use the Converse API, you call the Converse or ConverseStream operations to send messages to a model. To call Converse, you require permission for the bedrock:InvokeModel operation. To call ConverseStream, you require permission for the bedrock:InvokeModelWithResponseStream operation.

Request

When you make a Converse request with an Amazon Bedrock runtime endpoint, you can include the following fields:

modelId – A required parameter in the header that lets you specify the resource to use for inference.

The following fields let you customize the prompt:

messages – Use to specify the content and role of the prompts.

system – Use to specify system prompts, which define instructions or context for the model.

inferenceConfig – Use to specify inference parameters that are common to all models. Inference parameters influence the generation of the response.

additionalModelRequestFields – Use to specify inference parameters that are specific to the model that you run inference with.

promptVariables – (If you use a prompt from Prompt management) Use this field to define the variables in the prompt to fill in and the values with which to fill them.

The following fields let you customize how the response is returned:

guardrailConfig – Use this field to include a guardrail to apply to the entire prompt.

toolConfig – Use this field to include a tool to help a model generate responses.

additionalModelResponseFieldPaths – Use this field to specify fields to return as a JSON pointer object.

serviceTier – Use this field to specify the service tier for a particular request

requestMetadata – Use this field to include metadata that can be filtered on when using invocation logs.

Note

The following restrictions apply when you use a Prompt management prompt with Converse or ConverseStream:

You can't include the additionalModelRequestFields, inferenceConfig, system, or toolConfig fields.

If you include the messages field, the messages are appended after the messages defined in the prompt.

If you include the guardrailConfig field, the guardrail is applied to the entire prompt. If you include guardContent blocks in the ContentBlock field, the guardrail will only be applied to those blocks.

Expand a section to learn more about a field in the Converse request body:

messages

The messages field is an array of Message objects, each of which defines a message between the user and the model. A Message object contains the following fields:

role – Defines whether the message is from the user (the prompt sent to the model) or assistant (the model response).

content – Defines the content in the prompt.

Note

Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.

You can maintain conversation context by including all the messages in the conversation in subsequent Converse requests and using the role field to specify whether the message is from the user or the model.

The content field maps to an array of ContentBlock objects. Within each ContentBlock, you can specify one of the following fields (to see what models support what blocks, see models at a glance):

text
image
document
video
cachePoint
guardContent
reasoningContent
toolUse
toolResult

The text field maps to a string specifying the prompt. The text field is interpreted alongside other fields that are specified in the same ContentBlock.

The following shows a Message object with a content array containing only a text ContentBlock:

{
    "role": "user",
    "content": [
        {
            "text": "string"
        }
    ]
}

In the following messages example, the user asks for a list of three pop songs, and the model generates a list of songs.

[
    {
        "role": "user",
        "content": [
            {
                "text": "Create a list of 3 pop songs."
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "text": "Here is a list of 3 pop songs by artists from the United Kingdom:\n\n1. \"As It Was\" by Harry Styles\n2. \"Easy On Me\" by Adele\n3. \"Unholy\" by Sam Smith and Kim Petras"
            }
        ]
    }
]
system

A system prompt is a type of prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation. You can specify a list of system prompts for the request in the system (SystemContentBlock) field, as shown in the following example.

[
    {
        "text": "You are an app that creates play lists for a radio station that plays rock and pop music. Only return song names and the artist. "
    }
]
inferenceConfig

The Converse API supports a base set of inference parameters that you set in the inferenceConfig field (InferenceConfiguration). The base set of inference parameters are:

maxTokens – The maximum number of tokens to allow in the generated response.

stopSequences – A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.

temperature – The likelihood of the model selecting higher-probability options while generating a response.

topP – The percentage of most-likely candidates that the model considers for the next token.

For more information, see Influence response generation with inference parameters.

The following example JSON sets the temperature inference parameter.

{"temperature": 0.5}
additionalModelRequestFields

If the model you are using has additional inference parameters, you can set those parameters by specifying them as JSON in the additionalModelRequestFields field. The following example JSON shows how to set top_k, which is available in Anthropic Claude models, but isn't a base inference parameter in the messages API.

{"top_k": 200}
promptVariables

If you specify a prompt from Prompt management in the modelId as the resource to run inference on, use this field to fill in the prompt variables with actual values. The promptVariables field maps to a JSON object with keys that correspond to variables defined in the prompts and values to replace the variables with.

For example, let's say that you have a prompt that says Make me a {{genre}} playlist consisting of the following number of songs: {{number}}.. The prompt's ID is PROMPT12345 and its version is 1. You could send the following Converse request to replace the variables:

POST /model/arn:aws:bedrock:us-east-1:111122223333:prompt/PROMPT12345:1/converse HTTP/1.1
Content-type: application/json

{
   "promptVariables": { 
      "genre": {
         "text": "pop"
      },
      "number": {
         "text": "3"
      }
   }
}
guardrailConfig

You can apply a guardrail that you created with Amazon Bedrock Guardrails by including this field. To apply the guardrail to a specific message in the conversation, include the message in a GuardrailConverseContentBlock. If you don't include any GuardrailConverseContentBlocks in the request body, the guardrail is applied to all the messages in the messages field. For an example, see Include a guardrail with the Converse API.

toolConfig

This field lets you define a tool for the model to use to help it generate a response. For more information, see Use a tool to complete an Amazon Bedrock model response.

additionalModelResponseFieldPaths

Each model that Amazon Bedrock supports has its own native response shape with provider-specific fields (for example, Anthropic Claude returns a stop_sequence field; Cohere returns is_finished; and so on). To give you a uniform response across models, Converse and ConverseStream drop most model-native fields by default and return a normalized envelope with output, stopReason, usage, and metrics.

If your application needs one or more of those model-native fields, list their JSON Pointer paths in additionalModelResponseFieldPaths. Converse and ConverseStream then include those fields in the additionalModelResponseFields field of the response.

The following example asks Converse to also return Anthropic Claude's stop_sequence field, which contains the value of the stop sequence that ended generation:

[ "/stop_sequence" ]

Each path is a JSON Pointer (RFC 6901) into the model's native response. Empty pointers and malformed pointers return a 400 error. If a pointer is valid but the requested path doesn't exist in the model's response, it is silently ignored.

Note

This field controls which model-native response fields are surfaced through Converse. It does not control text-output formatting. Some models — particularly reasoning models such as DeepSeek-R1, Claude 3.7 Sonnet with extended thinking, and Amazon Nova reasoning models — can include reasoning content or model-specific tokens in their text output. For how to work with reasoning content, see Enhance model responses with model reasoning.

requestMetadata

The requestMetadata field maps to a JSON object of key-value tags that are recorded with the request in your model invocation logs. You can use request metadata to filter and aggregate logs by team, application, environment, or any other dimension that varies per call.

The same capability is available on InvokeModel and InvokeModelWithResponseStream through the X-Amzn-Bedrock-Request-Metadata HTTP header. For details on supported APIs, limits, and how request metadata appears in invocation logs, see Per-request metadata tagging.

serviceTier

This field maps to a JSON object. You can specify the service tier for a particular request.

The following example shows the serviceTier structure:

"serviceTier": {
  "type": "reserved" | "priority" | "default" | "flex"
}

For detailed information about service tiers, including pricing and performance characteristics, see Service tiers for optimizing performance and cost.

You can also optionally add cache checkpoints to the system or tools fields to use prompt caching, depending on which model you're using. For more information, see Prompt caching for faster model inference.

Response

The response you get from the Converse API depends on which operation you call, Converse or ConverseStream.

Converse response

In the response from Converse, the output field (ConverseOutput) contains the message (Message) that the model generates. The message content is in the content (ContentBlock) field and the role (user or assistant) that the message corresponds to is in the role field.

If you used prompt caching, then in the usage field, cacheReadInputTokens and cacheWriteInputTokens tell you how many total tokens were read from the cache and written to the cache, respectively.

If you used service tiers, then in the response field, service tier would tell you which service tier was used for the request.

The metrics field (ConverseMetrics) includes metrics for the call. To determine why the model stopped generating content, check the stopReason field. You can get information about the tokens passed to the model in the request, and the tokens generated in the response, by checking the usage field (TokenUsage). If you specified additional response fields in the request, the API returns them as JSON in the additionalModelResponseFields field.

The following example shows the response from Converse when you pass the prompt discussed in Request.

{
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "text": "Here is a list of 3 pop songs by artists from the United Kingdom:\n\n1. \"Wannabe\" by Spice Girls\n2. \"Bitter Sweet Symphony\" by The Verve \n3. \"Don't Look Back in Anger\" by Oasis"
                }
            ]
        }
    },
    "stopReason": "end_turn",
    "usage": {
        "inputTokens": 125,
        "outputTokens": 60,
        "totalTokens": 185
    },
    "metrics": {
        "latencyMs": 1175
    }
}
ConverseStream response

If you call ConverseStream to stream the response from a model, the stream is returned in the stream response field. The stream emits the following events. The diagram below shows the order in which the events are received; the content block events repeat once per content block, grouped by contentBlockIndex.

messageStart                          (once per response)
    |
    v
+-- for each content block (indexed by contentBlockIndex) --+
|                                                           |
|   contentBlockStart    (tool use only)                    |
|   contentBlockDelta    (one or more; text / reasoning /   |
|                         tool use partial JSON)            |
|   contentBlockStop                                        |
|                                                           |
+-----------------------------------------------------------+
    |
    v
messageStop                           (once per response;
    |                                  carries stopReason)
    v
metadata                              (once per response;
                                       usage + metrics)

messageStart (MessageStartEvent). The start event for a message. Includes the role for the message.

contentBlockStart (ContentBlockStartEvent). A Content block start event. Tool use only.

contentBlockDelta (ContentBlockDeltaEvent). A Content block delta event. Includes one of the following:

text – The partial text that the model generates.

reasoningContent – The partial reasoning carried out by the model to generate the response. You must submit the returned signature, in addition to all previous messages in subsequent Converse requests. If any of the messages are changed, the response throws an error.

toolUse – The partial input JSON object for tool use.

contentBlockStop (ContentBlockStopEvent). A Content block stop event.

messageStop (MessageStopEvent). The stop event for the message. Includes the reason why the model stopped generating output.

metadata (ConverseStreamMetadataEvent). Metadata for the request. The metadata includes the token usage in usage (TokenUsage) and metrics for the call in metrics (ConverseStreamMetadataEvent).

ConverseStream streams a complete content block as a ContentBlockStartEvent event, one or more ContentBlockDeltaEvent events, and a ContentBlockStopEvent event. Use the contentBlockIndex field as an index to correlate the events that make up a content block.

The following example is a partial response from ConverseStream.

{'messageStart': {'role': 'assistant'}}
{'contentBlockDelta': {'delta': {'text': ''}, 'contentBlockIndex': 0}}
{'contentBlockDelta': {'delta': {'text': ' Title'}, 'contentBlockIndex': 0}}
{'contentBlockDelta': {'delta': {'text': ':'}, 'contentBlockIndex': 0}}
.
.
.
{'contentBlockDelta': {'delta': {'text': ' The'}, 'contentBlockIndex': 0}}
{'messageStop': {'stopReason': 'max_tokens'}}
{'metadata': {'usage': {'inputTokens': 47, 'outputTokens': 20, 'totalTokens': 67}, 'metrics': {'latencyMs': 100.0}}}

Converse API examples

The following examples show you how to use the Converse and ConverseStream operations.

Text
Image
Document
Streaming
Video

This example shows how to call the Converse operation with the Anthropic Claude 3 Sonnet model. The example shows how to send the input text, inference parameters, and additional parameters that are unique to the model. The code starts a conversation by asking the model to create a list of songs. It then continues the conversation by asking that the songs are by artists from the United Kingdom.

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Shows how to use the <noloc>Converse</noloc> API with Anthropic Claude 3 Sonnet (on demand).
"""

import logging
import boto3

from botocore.exceptions import ClientError


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def generate_conversation(bedrock_client,
                          model_id,
                          system_prompts,
                          messages):
    """
    Sends messages to a model.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        system_prompts (JSON) : The system prompts for the model to use.
        messages (JSON) : The messages to send to the model.

    Returns:
        response (JSON): The conversation that the model generated.

    """

    logger.info("Generating message with model %s", model_id)

    # Inference parameters to use.
    temperature = 0.5
    top_k = 200

    # Base inference parameters to use.
    inference_config = {"temperature": temperature}
    # Additional inference parameters to use.
    additional_model_fields = {"top_k": top_k}

    # Send the message.
    response = bedrock_client.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    # Log token usage.
    token_usage = response['usage']
    logger.info("Input tokens: %s", token_usage['inputTokens'])
    logger.info("Output tokens: %s", token_usage['outputTokens'])
    logger.info("Total tokens: %s", token_usage['totalTokens'])
    logger.info("Stop reason: %s", response['stopReason'])

    return response

def main():
    """
    Entrypoint for Anthropic Claude 3 Sonnet example.
    """

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Setup the system prompts and messages to send to the model.
    system_prompts = [{"text": "You are an app that creates playlists for a radio station that plays rock and pop music. Only return song names and the artist."}]
    message_1 = {
        "role": "user",
        "content": [{"text": "Create a list of 3 pop songs."}]
    }
    message_2 = {
        "role": "user",
        "content": [{"text": "Make sure the songs are by artists from the United Kingdom."}]
    }
    messages = []

    try:

        bedrock_client = boto3.client(service_name='bedrock-runtime')

        # Start the conversation with the 1st message.
        messages.append(message_1)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        # Add the response message to the conversation.
        output_message = response['output']['message']
        messages.append(output_message)

        # Continue the conversation with the 2nd message.
        messages.append(message_2)
        response = generate_conversation(
            bedrock_client, model_id, system_prompts, messages)

        output_message = response['output']['message']
        messages.append(output_message)

        # Show the complete conversation.
        for message in messages:
            print(f"Role: {message['role']}")
            for content in message['content']:
                print(f"Text: {content['text']}")
            print()

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        print(f"A client error occured: {message}")

    else:
        print(
            f"Finished generating text with model {model_id}.")


if __name__ == "__main__":
    main()

On this page
Using the Converse API
Converse API examples
Related resources
Amazon Bedrock API Reference
AWS CLI commands for Amazon Bedrock
SDKs & Tools 
Did this page help you?
Yes
No
Provide feedback
Next topic:Responses API
Previous topic:Invoke API
Get Started
AWS Hands-On Tutorials 
AWS Solutions Library 
AWS Decision Guides
Service Guides
Choosing a generative AI service
AWS service guides
AWS CLI Tutorials on GitHub 
Developer Tools
AWS Code Example Library
AWS CLI
AWS Builder Center 
AWS Developer Tools Blog 
Helpful Links
Download the AWS Docs MCP Server 
Sign into the AWS Console 
AWS re:Post 
PrivacySite termsCookie preferences © 2026, Amazon Web Services, Inc. or its affiliates. All rights reserved.
English
Top

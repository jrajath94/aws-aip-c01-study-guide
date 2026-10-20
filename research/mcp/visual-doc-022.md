AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-compaction.html:

# Compaction

###### Tip

Server-side compaction is recommended for managing context in long-running conversations and agentic workflows as it handles context management automatically with minimal integration work.

###### Note

Compaction is available in beta through two independent mechanisms, each with its own beta header:

* `compact-2026-01-12` — threshold-triggered auto-summarization, configured through `context_management.edits` (the `compact_20260112` strategy). This mechanism is described below.
* `compact-2026-09-04` — a newer mechanism driven by a top-level `compaction` parameter (an explicit compaction request plus signed-block adoption). See [Compaction with the compaction parameter (compact-2026-09-04 beta)](#claude-messages-compaction-summarize-2026-09-04).

Include the beta header that matches the mechanism you use. Neither mechanism is supported by the Converse API; both work with [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html).

Compaction extends the effective context length for long-running conversations and tasks by automatically summarizing older context when approaching the context window limit. This is ideal for:

* Chat-based, multi-turn conversations where you want users to use one chat for a long period of time
* Task-oriented prompts that require a lot of follow-up work (often tool use) that may exceed the model's context window

The `compact-2026-01-12` mechanism is supported on the following models:

| Model | Model ID |
| --- | --- |
| Claude Sonnet 4.6 | `anthropic.claude-sonnet-4-6` |
| Claude Opus 4.6 | `anthropic.claude-opus-4-6-v1` |

###### Note

The top-level `input_tokens` and `output_tokens` in the `usage` field do not include compaction iteration usage, and reflect the sum of all non-compaction iterations. To calculate the total tokens consumed and billed for a request, sum across all entries in the `usage.iterations` array.

If you previously relied on `usage.input_tokens` and `usage.output_tokens` for cost tracking or auditing, you will need to update your tracking logic to aggregate across `usage.iterations` when compaction is enabled. The `iterations` array is only present when a new compaction is triggered during the request. Re-applying a previous `compaction` block incurs no additional compaction cost, and the top-level usage fields remain accurate in that case.

## How compaction works

When compaction is enabled, Claude automatically summarizes your conversation when it approaches the configured token threshold. The API:

1. Detects when input tokens exceed your specified trigger threshold.
2. Generates a summary of the current conversation.
3. Creates a `compaction` block containing the summary.
4. Continues the response with the compacted context.

On subsequent requests, append the response to your messages. The API automatically drops all message blocks before the `compaction` block, continuing the conversation from the summary.

## Basic usage

Enable compaction by adding the `compact_20260112` strategy to `context_management.edits` in your Messages API request.

CLI
:   ```
    aws bedrock-runtime invoke-model \
        --model-id "us.anthropic.claude-opus-4-6-v1" \
        --body '{
            "anthropic_version": "bedrock-2023-05-31",
            "anthropic_beta": ["compact-2026-01-12"],
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "user",
                    "content": "Help me build a website"
                }
            ],
            "context_management": {
                "edits": [
                    {
                        "type": "compact_20260112"
                    }
                ]
            }
        }' \
        --cli-binary-format raw-in-base64-out \
        /tmp/response.json

    echo "Response:"
    cat /tmp/response.json | jq '.content[] | {type, text: .text[0:500]}'
    ```

Python
:   ```
    import boto3
    import json

    bedrock_runtime = boto3.client(service_name='bedrock-runtime')

    messages = [{"role": "user", "content": "Help me build a website"}]

    response = bedrock_runtime.invoke_model(
        modelId="us.anthropic.claude-opus-4-6-v1",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "anthropic_beta": ["compact-2026-01-12"],
            "max_tokens": 4096,
            "messages": messages,
            "context_management": {
                "edits": [
                    {
                        "type": "compact_20260112"
                    }
                ]
            }
        })
    )

    response_body = json.loads(response["body"].read())

    # Append the response (including any compaction block) to continue the conversation
    messages.append({"role": "assistant", "content": response_body["content"]})

    for block in response_body["content"]:
        if block.get("type") == "compaction":
            print(f"[COMPACTION]: {block['content'][:200]}...")
        elif block.get("type") == "text":
            print(f"[RESPONSE]: {block['text']}")
    ```

TypeScript
:   ```
    import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

    async function main() {
        const client = new BedrockRuntimeClient({});

        const messages: Array<{role: string, content: string | object[]}> = [
            { role: "user", content: "Help me build a website" }
        ];

        const command = new InvokeModelCommand({
            modelId: "us.anthropic.claude-opus-4-6-v1",
            body: JSON.stringify({
                anthropic_version: "bedrock-2023-05-31",
                anthropic_beta: ["compact-2026-01-12"],
                max_tokens: 4096,
                messages,
                context_management: {
                    edits: [
                        {
                            type: "compact_20260112"
                        }
                    ]
                }
            })
        });

        const response = await client.send(command);
        const responseBody = JSON.parse(new TextDecoder().decode(response.body));

        // Append response to continue conversation
        messages.push({ role: "assistant", content: responseBody.content });

        for (const block of responseBody.content) {
            if (block.type === "compaction") {
                console.log(`[COMPACTION]: ${block.content.substring(0, 200)}...`);
            } else if (block.type === "text") {
                console.log(`[RESPONSE]: ${block.text}`);
            }
        }
    }

    main().catch(console.error);
    ```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `type` | string | Required | Must be `"compact_20260112"` |
| `trigger` | object | 150,000 tokens | When to trigger compaction. Must be at least 50,000 tokens. |
| `pause_after_compaction` | boolean | `false` | Whether to pause after generating the compaction summary |
| `instructions` | string | `null` | Custom summarization prompt. Completely replaces the default prompt when provided. |

## Trigger configuration

Configure when compaction triggers using the `trigger` parameter:

```
import boto3
import json

bedrock_runtime = boto3.client(service_name='bedrock-runtime')

response = bedrock_runtime.invoke_model(
    modelId="us.anthropic.claude-opus-4-6-v1",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "anthropic_beta": ["compact-2026-01-12"],
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": "Help me build a website"}],
        "context_management": {
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {
                        "type": "input_tokens",
                        "value": 100000
                    }
                }
            ]
        }
    })
)

response_body = json.loads(response["body"].read())
print(response_body["content"][-1]["text"])
```

## Custom summarization instructions

By default, compaction uses the following summarization prompt:

```
You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context, where the raw history above may not be accessible and will be replaced with this summary. Write down anything that would be helpful, including the state, next steps, learnings etc. You must wrap your summary in a <summary></summary> block.
```

You can provide custom instructions through the `instructions` parameter to replace this prompt entirely. Custom instructions don't supplement the default; they completely replace it:

```
import boto3
import json

bedrock_runtime = boto3.client(service_name='bedrock-runtime')

response = bedrock_runtime.invoke_model(
    modelId="us.anthropic.claude-opus-4-6-v1",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "anthropic_beta": ["compact-2026-01-12"],
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": "Help me build a website"}],
        "context_management": {
            "edits": [
                {
                    "type": "compact_20260112",
                    "instructions": "Focus on preserving code snippets, variable names, and technical decisions."
                }
            ]
        }
    })
)

response_body = json.loads(response["body"].read())
print(response_body["content"][-1]["text"])
```

## Pausing after compaction

Use `pause_after_compaction` to pause the API after generating the compaction summary. This allows you to add additional content blocks (such as preserving recent messages or specific instruction-oriented messages) before the API continues with the response.

When enabled, the API returns a message with the `compaction` stop reason after generating the compaction block:

```
import boto3
import json

bedrock_runtime = boto3.client(service_name='bedrock-runtime')

messages = [{"role": "user", "content": "Help me build a website"}]

response = bedrock_runtime.invoke_model(
    modelId="us.anthropic.claude-opus-4-6-v1",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "anthropic_beta": ["compact-2026-01-12"],
        "max_tokens": 4096,
        "messages": messages,
        "context_management": {
            "edits": [
                {
                    "type": "compact_20260112",
                    "pause_after_compaction": True
                }
            ]
        }
    })
)

response_body = json.loads(response["body"].read())

# Check if compaction triggered a pause
if response_body.get("stop_reason") == "compaction":
    # Response contains only the compaction block
    messages.append({"role": "assistant", "content": response_body["content"]})

    # Continue the request
    response = bedrock_runtime.invoke_model(
        modelId="us.anthropic.claude-opus-4-6-v1",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "anthropic_beta": ["compact-2026-01-12"],
            "max_tokens": 4096,
            "messages": messages,
            "context_management": {
                "edits": [{"type": "compact_20260112"}]
            }
        })
    )
    response_body = json.loads(response["body"].read())

print(response_body["content"][-1]["text"])
```

## Working with compaction blocks

When compaction is triggered, the API returns a `compaction` block at the start of the assistant response.

A long-running conversation may result in multiple compactions. The last compaction block reflects the final state of the prompt, replacing content before it with the generated summary.

```
{
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: The user requested help building a web scraper..."
    },
    {
      "type": "text",
      "text": "Based on our conversation so far..."
    }
  ]
}
```

## Streaming

When streaming responses with compaction enabled, you'll receive a `content_block_start` event when compaction begins. The compaction block streams differently from text blocks. You'll receive a `content_block_start` event, followed by a single `content_block_delta` with the complete summary content (no intermediate streaming), and then a `content_block_stop` event.

## Prompt caching

You may add a `cache_control` breakpoint on compaction blocks, which caches the full system prompt along with the summarized content. The original compacted content is ignored. Note that when compaction is triggered, it can result in a cache miss on the subsequent request.

```
{
    "role": "assistant",
    "content": [
        {
            "type": "compaction",
            "content": "[summary text]",
            "cache_control": {"type": "ephemeral"}
        },
        {
            "type": "text",
            "text": "Based on our conversation..."
        }
    ]
}
```

## Understanding usage

Compaction requires an additional sampling step, which contributes to rate limits and billing. The API returns detailed usage information in the response:

```
{
  "usage": {
    "input_tokens": 45000,
    "output_tokens": 1234,
    "iterations": [
      {
        "type": "compaction",
        "input_tokens": 180000,
        "output_tokens": 3500
      },
      {
        "type": "message",
        "input_tokens": 23000,
        "output_tokens": 1000
      }
    ]
  }
}
```

The `iterations` array shows usage for each sampling iteration. When compaction occurs, you'll see a `compaction` iteration followed by the main `message` iteration. The final iteration's token counts reflect the effective context size after compaction.

## Compaction with the compaction parameter (compact-2026-09-04 beta)

###### Note

This section documents a different, newer compaction mechanism from the `compact-2026-01-12` beta described earlier on this page. The `compact-2026-01-12` beta drives compaction through `context_management.edits` with the `compact_20260112` strategy. The `compact-2026-09-04` beta described in this section instead uses a top-level `compaction` parameter. The two mechanisms are independent. Include the beta flag that matches the mechanism you use.

A request that sends the top-level `compaction` parameter is a compaction request. The server summarizes the messages with one inference call on the requested model, and returns the summary as a single signed `compaction` content block, alone, with `stop_reason: "compaction"`. A later request adopts the block by sending it first in `messages`, in place of the messages it summarizes, and the later request is served as an ordinary turn. The server keeps no state between requests.

This mechanism requires the beta flag `compact-2026-09-04` in `anthropic_beta`, both on the compaction request and on every later request that carries the returned block. It is supported on `bedrock-runtime` through InvokeModel, InvokeModelWithResponseStream, and CountTokens. It is not supported by the Converse API.

Model support for this mechanism differs from the `compact-2026-01-12` beta, and the table earlier on this page applies only to that older beta. To find out whether a model supports compaction and which beta value it takes, see the **Compaction** section of that model's card in [Models at a glance](./model-cards.html). Sending the `compaction` parameter to a model that doesn't support this beta returns `400` with the message `compaction: Extra inputs are not permitted`.

Compaction with the `compaction` parameter is a beta capability available on models whose policy supports the `compact_20260904` strategy (for example, Claude Opus 5.5 and Claude Haiku 5.5). To check whether a specific model supports it, see the **Capabilities and Features** table in that model's model card (see [Models at a glance](./model-cards.html)).

### Request shape

The `compaction` parameter is an object of the form `{"type": "summarize", "instructions"?: string}`. The `instructions` member is optional. The following example sends a compaction request with the beta flag, a few messages, and custom instructions.

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "anthropic_beta": ["compact-2026-09-04"],
  "max_tokens": 4096,
  "messages": [
    {"role": "user", "content": "Help me build a web scraper in Python."},
    {"role": "assistant", "content": "Sure. Let's start with the requests and BeautifulSoup libraries..."},
    {"role": "user", "content": "Now add retry logic and rate limiting."}
  ],
  "compaction": {
    "type": "summarize",
    "instructions": "Preserve code snippets, library choices, and any decisions about retries and rate limiting."
  }
}
```

### Response and adoption

The response `content` holds a single signed `compaction` block, and `stop_reason` is `"compaction"`. The top-level `usage` counts are zeroed, and the tokens for the summarization call appear under `usage.iterations` as a `compaction` entry.

```
{
  "content": [
    {
      "type": "compaction",
      "content": "<summary>The user is building a Python web scraper...</summary>",
      "signature": "<opaque>"
    }
  ],
  "stop_reason": "compaction",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "iterations": [
      {
        "type": "compaction",
        "input_tokens": 180000,
        "output_tokens": 3500
      }
    ]
  }
}
```

To continue the conversation, the adopting request sends the returned `compaction` block back byte-for-byte as the first block of its first user or assistant message, followed by the turns kept or added since compaction. The adopting request does not include the `compaction` parameter. It is served as an ordinary turn.

### Custom summarization instructions

Use `compaction.instructions` to replace the server summarization prompt. Instructions can be at most 16,384 characters, and a blank value is treated as absent. Before the summarization call, a server-side classifier screens the instructions. The following table lists the outcomes.

| Scenario | Behavior |
| --- | --- |
| No instructions, or instructions pass the classifier | 200 response, a signed `compaction` block, and `stop_reason` is `"compaction"`. |
| Instructions flagged by the classifier | 200 response, empty `content`, `stop_reason` is `"refusal"`, and `stop_details` is `null`. No summarization call is made. |
| Classifier unreachable or timed out | 529 response with the message `the compaction instructions could not be checked; retry the request`. Screening fails closed. |
| No summary produced (output cut off, context exceeded, or model refusal) | 200 response, empty `content`, and the `stop_reason` from the summarization call itself. |

### Tool changes across a compaction

When the compaction request also carries the `inline-tools-2026-09-15` or `mid-conversation-tool-changes-2026-07-01` beta flag, and the summarized messages held `tool_addition` or `tool_removal` blocks, the returned `compaction` block has a third member, `tool_changes`. This member is an array of those blocks that gives the net tool changes across the summarized range, with `cache_control` stripped. The `tool_changes` member is covered by the signature. It is absent when there were no tool changes, and it is never an empty array.

Send `tool_changes` back with the block unmodified. On adoption, the server re-applies its entries at the block's position, so the tools available after the block match those that were available before compaction.

### Streaming

When you stream a compaction request, the `compaction` block arrives whole in one `content_block_start` and `content_block_stop` pair, with no deltas.

### Parameters you cannot combine with compaction

A compaction request returns a 400 error when it also sends any of the following:

* `context_management`
* `stop_sequences`
* `output_config.format`
* A forced `tool_choice`
* `output_config.task_budget.remaining`
* `max_tokens: 0`

### Error responses

Match these conditions on the message text of the response.

| Condition | Response |
| --- | --- |
| The `compaction` parameter is sent without the beta flag | 400 with the message `compaction: Extra inputs are not permitted`. |
| The adopted block was altered | 400 with the message `compaction block content does not match its signature` or `invalid signature in compaction block`. |
| Instructions are sent while custom instructions are disabled | 400 with the message `compaction.instructions is not available on this platform`. |
| A transient signing failure | 529 with the message `the compaction summary could not be signed; retry the request`. |
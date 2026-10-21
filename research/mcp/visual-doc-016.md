AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html:

# Use agentic retrieval to query a knowledge base

Agentic retrieval uses a foundation model to intelligently decompose complex queries into
sub-queries, iteratively retrieve relevant information from your knowledge bases, and
evaluate whether the retrieved results are sufficient to answer the original query. This
approach improves retrieval accuracy for complex, multi-step questions that a single
retrieval pass might not fully address.

For example, given the query *"Which magazine was started first, Arthur's Magazine
or First for Women?"*, agentic retrieval breaks this into separate sub-queries
such as *"When was Arthur's Magazine founded?"* and *"When was
First for Women founded?"*, retrieves results for each, and evaluates whether
the combined results are sufficient.

## How agentic retrieval works

When you send a request to the `AgenticRetrieveStream` API, the following
process occurs:

1. **Session history load** – When you
   supply a `memoryConfiguration` that includes a
   `sessionBinding`, Amazon Bedrock restores the prior history of that session
   from AgentCore Memory short-term memory before the agent begins work. The
   restored history becomes the conversation context for the request.
2. **Planning** – The foundation model
   analyzes your query and creates a plan to decompose it into one or more
   sub-queries. Each sub-query targets a specific source that you
   configured, either a knowledge base retriever or AgentCore Memory long-term
   memory. After retrieval results are collected, the foundation model
   evaluates whether they are sufficient to answer the original query. If not,
   it plans and executes additional retrieval iterations, up to the configured
   maximum. When the request applies a retrieval instruction, the plan follows the
   instruction's `retrievalGuidance`.
3. **Retrieval** – The sub-queries are
   executed against the configured sources. Results are collected
   from each retrieval.
4. **Full document expansion** – When the
   foundation model determines that the full content of a document is needed
   (e.g., for summarization, to verify completeness, or to access specific sections),
   it calls the GetDocumentContent API to retrieve the complete document content.
5. **Response generation** – When
   `generateResponse` is set to `true` (the default), the
   foundation model synthesizes a natural-language answer from the
   retrieved results. Amazon Bedrock streams the answer back to you through `responseEvent` events.
   When `sessionBinding` is set and `persistenceMode` is
   `DEFAULT`, Amazon Bedrock persists the question and the generated
   answer to the session. When the request applies a retrieval instruction, its
   `persona`, `answerFormat`, and `answerPolicy`
   fields shape the answer.
6. **Result event** – The deduplicated retrieval
   results from all iterations, the full synthesized natural-language answer and citations are returned to you.
   Trace events are streamed throughout the process for observability.

## Prerequisites

Before you can use agentic retrieval, you must have the following:

* A fully managed Amazon Bedrock knowledge base. Agentic retrieval currently supports
  only managed knowledge bases.
* Access to a foundation model in Amazon Bedrock to use for query planning and
  evaluation.
* The required IAM permissions. For more information, see [Required permissions for agentic retrieval](#kb-agentic-retrieve-permissions).

## Query a knowledge base with agentic retrieval

To use agentic retrieval, send an [`AgenticRetrieveStream`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html) request. The response is a stream
that includes retrieval results and trace events.

The following table describes the key request fields:

Required fields

| Field | Description |
| --- | --- |
| messages | The input query and conversation history. Each message contains a `content` field with a `text` value and a `role` field (`user` or `assistant`). |
| retrievers | The knowledge base retrievers to fetch data from. You can specify up to 5 retrievers, each pointing to a managed knowledge base by its ID. Each retriever can optionally include metadata filters and a maximum number of results. |
| agenticRetrieveConfiguration | The agentic retrieval configuration, including the foundation model to use for query planning and evaluation, and optionally a reranking model and maximum agent iteration count. |

Optional fields

| Field | Description |
| --- | --- |
| policyConfiguration | Configures a Amazon Bedrock guardrail to apply during agentic retrieval. Specify a `guardrailId` and `guardrailVersion`. A guardrail is supported only when `foundationModelType` is `CUSTOM`. Passing a guardrail with the default `MANAGED` type, or without setting `foundationModelType`, fails validation. Because `CUSTOM` also requires `foundationModelConfiguration`, applying a guardrail means naming an explicit model by its `modelArn`. |
| userContext | Provides a user context for access control filtering. |
| memoryConfiguration | Configures an AgentCore Memory resource to use with the retrieval. Specify a `memoryId`, and then `sessionBinding` to restore and continue a session, `retrievalConfigs` to let the agent retrieve from long-term memory, or both. For more information, see [Use AgentCore Memory with agentic retrieval](#kb-agentic-retrieve-memory). |
| generateResponse | A boolean field that, when set to `true` (the default), instructs the foundation model to generate a natural-language answer from the retrieved results. The answer is streamed back as text chunks and included in the result event. |
| retrievalInstructionConfiguration | Applies a retrieval instruction that steers how the agent searches and answers. Specify a `retrievalInstructionId` and, optionally, a `version`. For more information, see [Use retrieval instructions with agentic retrieval](#kb-agentic-retrieve-instruction). |

###### Note

Agentic retrieval does not support guardrails whose sensitive information
policy uses the `ANONYMIZE` action for PII entities or regular
expressions. Such a request fails validation even when
`foundationModelType` is `CUSTOM`.

For the full request and response syntax, see [`AgenticRetrieveStream`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html) in the API reference.

## Agentic retrieval response

The `AgenticRetrieveStream` response is a stream that contains the
following event types:

* **Result event**
  (`AgenticRetrieveResultEvent`) – The final event delivered
  when processing completes. Contains the retrieval results and, when response
  generation is enabled, the generated response. The result event includes:

  + **Retrieval results**
    (`results`) – The source chunks
    retrieved across all iterations. Each result includes content, source retriever identifier,
    and optional metadata. When the same chunk is retrieved by multiple sub-queries, it
    appears only once in the final results.
  + **Generated response**
    (`generatedResponse`) – When
    `generateResponse` is set to `true` (the
    default), the result event includes a
    `generatedResponse` object containing:

    - `answer` – The full synthesized
      natural-language answer text.
    - `citations` – An optional list that maps
      spans of the answer to supporting retrieval results. Each
      citation contains:

      * `startIndex` – The character
        offset where the cited passage begins within the
        `answer` string.
      * `endIndex` – The character offset
        where the cited passage ends (exclusive — the
        cited text runs from `startIndex` up to
        but not including `endIndex`).
      * `references` – A list where each
        reference has a `resultIndex` field that
        indexes into the `results` array on the
        same result event, indicating which retrieval result
        supports the cited span.
* **Response events**
  (`AgenticRetrieveResponseEvent`) – When
  `generateResponse` is set to `true` (the default),
  `responseEvent` events are streamed during response generation.
  Each event contains a `text` field with an incremental portion
  of the synthesized natural-language answer.
* **Trace events**
  (`AgenticRetrieveTraceEvent`) – Events streamed during
  the agentic retrieval process that provide visibility into each step. These are
  the types of trace events:

  + **Planning** – Indicates the
    foundation model is analyzing the query and creating sub-queries.
    Includes the planned actions and target sources. Each action is either
    a `retrieve` action targeting a knowledge base or a
    `memoryRetrieve` action targeting long-term memory, which
    includes the composed query and the `memoryId`. When the
    request applies a retrieval instruction, the first
    **Planning** event includes an
    `appliedInstruction` attribute with the ID of the instruction
    and the version that was applied.
  + **Retrieval** – Indicates a
    retrieval is being executed against a configured source. Includes the
    retrieval input, output, and any warnings or failures. The
    `retrievalMetadata` entry reports the source type, either
    `BedrockKnowledgeBase` or
    `BedrockAgentCoreMemory`.
  + **Speculative retrieval** – An
    initial retrieval that runs before the first planning step to reduce
    latency. For a single knowledge base, this retrieves results using the
    raw user query. For multiple knowledge bases, this performs a probe
    search to help route queries to the appropriate retrievers. When you
    configure `retrievalConfigs`, this step can also retrieve
    from long-term memory.
  + **Full document expansion** – Indicates
    the agent is retrieving the full content of a specific document. Includes
    the document ID, source retriever, and status (InProgress, Success, or Failure).
  + **Session history load** – Indicates
    that Amazon Bedrock is restoring the history of an earlier session from AgentCore
    Memory short-term memory, before the agent begins work.

## Use AgentCore Memory with agentic retrieval

You can give agentic retrieval access to an [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
resource. With memory access, a retrieval can continue an earlier session and draw on
what the agent has learned in previous ones. Supply the
`memoryConfiguration` field with the `memoryId` of a memory
resource in your account that is in the `ACTIVE` state.

Memory is optional. A `memoryConfiguration` that sets only a
`memoryId` is not valid. When you supply
`memoryConfiguration`, you must use the memory resource in at least one of
the following two ways:

* **Short-term memory**
  (`sessionBinding`)—Restores the history of an earlier session
  so that the request continues that session instead of starting fresh. Identify
  the session with an `actorId` and a `sessionId`.
  The `actorId` scopes the history, so one actor's
  history is never returned for another. When `sessionBinding` is set,
  `messages` must carry only the current query, with a
  `role` of `user`. You cannot restore a session and supply
  earlier conversation history in `messages` in the same request. The
  restore loads conversational events with a role of `USER` or
  `ASSISTANT`.
* **Long-term memory**
  (`retrievalConfigs`)—Makes the memory records that AgentCore
  Memory extracted from earlier sessions available to the agent. Identify the
  records with a `namespace` prefix, or with a
  `namespacePath` to retrieve across every namespace beneath a parent.
  You can narrow the results further with a `strategyId` and with
  `metadataFilters`. The agent decides whether to retrieve and
  composes its own query.

Supply namespaces exactly as they are configured on the memory strategy, with
placeholders already resolved. For example, if the strategy defines the namespace
`/strategy/{memoryStrategyId}/actor/{actorId}`, supply the resolved value
rather than the template. For more information about namespaces, strategies, and memory
records, see [Memory
terminology](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-terminology.html) in the *Amazon Bedrock AgentCore Developer Guide*.

###### Note

You are responsible for supplying the correct `memoryId`,
`sessionBinding`, and `retrievalConfigs` values. Agentic
retrieval does not verify that the session or the namespaces you supply correspond to
the conversation that you intend to continue. If you supply incorrect values, you
receive unexpected results.

When `sessionBinding` is set, use `persistenceMode` to control
whether the current exchange is written back to the session:

* `DEFAULT` (the default)—Persists the question and the
  generated answer to the session as a single event. This value requires
  `generateResponse` to be `true`.
* `NONE`—Leaves the session unchanged. Use this value to read
  session history without adding to it.

The following example restores an earlier session, gives the agent access to that
actor's long-term memory, and persists the exchange back to the session:

```
{
    "messages": [
        {
            "content": {
                "text": "What did we decide about the migration timeline?"
            },
            "role": "user"
        }
    ],
    "retrievers": [
        {
            "configuration": {
                "knowledgeBase": {
                    "knowledgeBaseId": "KB12345678"
                }
            }
        }
    ],
    "agenticRetrieveConfiguration": {
        "foundationModelType": "MANAGED",
        "rerankingModelType": "MANAGED"
    },
    "memoryConfiguration": {
        "memoryId": "projectAssistantMemory-1a2b3c4d5e",
        "sessionBinding": {
            "actorId": "user-123",
            "sessionId": "session-456"
        },
        "retrievalConfigs": [
            {
                "namespace": "/strategy/summarization-1a2b3c4d5e/actor/user-123"
            }
        ],
        "persistenceMode": "DEFAULT"
    }
}
```

The response stream reports memory activity. The restore appears as a
**Session history load** trace event. The records that
long-term memory returns appear on the **Retrieval** trace
event with a source type of `BedrockAgentCoreMemory`, whichever step
retrieved them.

How the retrieval itself appears depends on when it happens. When the foundation model
chooses to search memory (typical on a continued session), the retrieval appears as a
`memoryRetrieve` action on the **Planning**
trace event. On a new session, the agent can instead retrieve long-term memory during
**Speculative retrieval**, before the first planning step,
in which case it emits no `memoryRetrieve` action. For more information,
see [Agentic retrieval response](#kb-agentic-retrieve-response).

## Use retrieval instructions with agentic retrieval

A retrieval instruction steers how agentic retrieval searches your knowledge bases
and how it answers. You create the instruction once, Amazon Bedrock reviews it, and then you
reference it from your requests. Retrieval instructions are optional. To create,
review, version, and delete retrieval instructions, see [Create and manage retrieval instructions](./kb-test-agentic-retrieve-instruction.html).

To apply one, supply the `retrievalInstructionConfiguration` field with
the `retrievalInstructionId` of an `ACTIVE` instruction in your
account and Region. To pin the behavior, set `version` to a version number.
When you omit `version`, Amazon Bedrock applies `DRAFT`, the current
reviewed content. If the instruction doesn't exist in your account, isn't
`ACTIVE`, or the version you specify doesn't exist, the request fails with
a `ValidationException` before any events are streamed.

In the following example, replace `abcde12345` with your retrieval
instruction ID and `3` with the version to apply:

```
{
    "messages": [
        {
            "content": {
                "text": "How do I reset the Model X200 to factory settings?"
            },
            "role": "user"
        }
    ],
    "retrievers": [
        {
            "configuration": {
                "knowledgeBase": {
                    "knowledgeBaseId": "KB12345678"
                }
            }
        }
    ],
    "agenticRetrieveConfiguration": {
        "foundationModelType": "MANAGED",
        "rerankingModelType": "MANAGED"
    },
    "retrievalInstructionConfiguration": {
        "retrievalInstructionId": "abcde12345",
        "version": "3"
    }
}
```

To confirm which instruction and version a request used, read the
`appliedInstruction` attribute on the first
**Planning** trace event. The following example shows the
attributes of that trace event:

```
{
    "step": "Planning",
    "status": "IN_PROGRESS",
    "message": "Agent planning started",
    "appliedInstruction": {
        "id": "abcde12345",
        "version": "3"
    }
}
```

For more information about trace events, see [Agentic retrieval response](#kb-agentic-retrieve-response).

## Required permissions for agentic retrieval

To use the `AgenticRetrieveStream` API, the calling IAM identity must
have the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "bedrock:AgenticRetrieveStream",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:Retrieve",
                "bedrock:GetDocumentContent"
            ],
            "Resource": "arn:aws:bedrock:region:account-id:knowledge-base/*"
        },
        {
            "Effect": "Allow",
            "Action": "bedrock:InvokeModelWithResponseStream",
            "Resource": "*"
        }
    ]
}
```

If you use guardrails with agentic retrieval, add the following permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "bedrock:GetGuardrail",
        "bedrock:ApplyGuardrail"
    ],
    "Resource": "*"
}
```

If you use an AgentCore Memory resource with agentic retrieval, add the following
permissions:

```
{
    "Effect": "Allow",
    "Action": [
        "bedrock-agentcore:GetMemory",
        "bedrock-agentcore:ListEvents",
        "bedrock-agentcore:RetrieveMemoryRecords",
        "bedrock-agentcore:CreateEvent"
    ],
    "Resource": "arn:aws:bedrock-agentcore:region:account-id:memory/memory-id"
}
```

`bedrock-agentcore:ListEvents` is required only when you set
`sessionBinding`. `bedrock-agentcore:RetrieveMemoryRecords` is
required only when you set `retrievalConfigs`.
`bedrock-agentcore:CreateEvent` is required only when
`persistenceMode` is `DEFAULT`.

If the memory resource is encrypted with a customer managed key, add the following
permission on that key:

```
{
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:region:account-id:key/key-id"
}
```

If you apply a retrieval instruction with agentic retrieval, add the following
permission:

```
{
    "Effect": "Allow",
    "Action": "bedrock:GetRetrievalInstruction",
    "Resource": "arn:aws:bedrock:region:account-id:retrieval-instruction/retrieval-instruction-id"
}
```

Versions don't have their own ARN, so this permission also covers the version that
you specify in `version`.

If the retrieval instruction is encrypted with a customer managed key, add the
following permission on that key:

```
{
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:region:account-id:key/key-id"
}
```

The key policy must also allow the caller to use the key through Amazon Bedrock. For the key
policy, see [Encryption of retrieval instructions](./encryption-kb.html#encryption-kb-retrieval-instruction). For the permissions to
create and manage retrieval instructions, see [Required permissions for retrieval instructions](./kb-test-agentic-retrieve-instruction.html#kb-retrieval-instruction-permissions).

## Considerations

Keep the following in mind when using agentic retrieval:

* Agentic retrieval only supports managed Amazon Bedrock knowledge bases.
* For quotas on retrievers per request, results per retrieval call, and
  maximum agent iterations, see [Service quotas for managed knowledge bases](./kb-managed-quotas.html).
* Reducing the maximum iteration count may cause the agent to stop earlier,
  potentially reducing accuracy for complex queries.
* When configuring guardrails, only the `BLOCK` action is supported.
  The `MASK` action is not supported with agentic retrieval.
* The customer provides and owns the foundation model, embedding model, and
  reranking model used during agentic retrieval if provided. Your IAM credentials
  are used to invoke these models.
* When you use an AgentCore Memory resource, the resource must be in the same
  account as the knowledge base and must be in the `ACTIVE`
  state.
* When you set `sessionBinding`, `messages` must carry only
  the current query, with a `role` of `user`. You cannot
  restore a session and supply earlier conversation history in
  `messages` in the same request.
* Restoring a session loads conversational events with a role of
  `USER` or `ASSISTANT`. AgentCore Memory also accepts the
  `TOOL` and `OTHER` roles, which a restore does not load.
  For more information, see [`Conversational`](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Conversational.html) in the *Amazon Bedrock AgentCore API
  Reference*.
* `retrievalConfigs` currently accepts at most one entry, and each
  entry accepts a maximum of 5 `metadataFilters` expressions.
* A `persistenceMode` of `DEFAULT` requires
  `generateResponse` to be `true`, because the session persists the
  generated answer.
* A retrieval instruction must be `ACTIVE` and in the same account and
  Region as the request. For more information, see [Use retrieval instructions with agentic retrieval](#kb-agentic-retrieve-instruction).
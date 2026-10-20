AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html:

# What are Automated Reasoning checks in Amazon Bedrock Guardrails?

## What Automated Reasoning checks do

A key challenge with large language models (LLMs) is ensuring the accuracy of their
responses. Without validation, LLMs can produce hallucinations or inaccurate information
that undermines trust. Automated Reasoning checks in Amazon Bedrock Guardrails help solve this problem by using
mathematical techniques to validate natural language content against policies you define.

Unlike traditional guardrail components that block or filter content based on pattern
matching, Automated Reasoning checks use formal logic to provide structured feedback
about *why* a response is correct or incorrect. This feedback can be
used to steer an LLM towards generating content that is provably consistent with your policy.
Specifically, Automated Reasoning checks can:

* **Detect factually incorrect statements** in LLM responses by
  mathematically proving that generated content contradicts your policy rules.
* **Highlight unstated assumptions** where a response is
  consistent with your policy but doesn't address all relevant rules, indicating the
  response may be incomplete.
* **Provide mathematically verifiable explanations** for why
  accurate statements are correct, citing the specific policy rules and variable assignments that
  support the conclusion.

These capabilities make Automated Reasoning checks different from other Amazon Bedrock Guardrails components.
Content filters and topic policies act as binary gates — they block or allow content.
Automated Reasoning checks act as a verification layer that provides detailed, actionable
feedback you can use to improve responses programmatically.

## When to use Automated Reasoning checks

Automated Reasoning checks are most valuable when you need to demonstrate the factual
basis for an LLM's response. Consider using them when your application involves:

* **Regulated industries** such as healthcare, human
  resources, and financial services, where incorrect information can have legal or
  compliance consequences.
* **Complex rule sets** such as mortgage approvals, zoning
  laws, insurance eligibility, or employee benefits, where multiple conditions interact to
  determine an outcome.
* **Compliance scenarios** that require auditable AI
  responses with mathematically verifiable proof that the response is consistent with your
  policies.
* **Customer-facing applications** where incorrect
  guidance could erode trust, such as chatbots that answer questions about company policies,
  product eligibility, or service terms.

## What Automated Reasoning checks don't do

To set the right expectations, be aware of the following limitations:

* **No prompt injection protection.** Automated Reasoning
  checks validate exactly what you send them. If malicious or manipulated content is
  provided as input, the validation is performed on that content as-is. To detect and block
  prompt injection attacks, use [Content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html#guardrails-content-filters) in combination with Automated Reasoning checks.
* **No support for encoded or obfuscated text.** Automated
  Reasoning checks evaluate content as plaintext natural language. If *any
  part* of the submitted content is encoded or obfuscated — for example, Base64
  (`ZG9ncw==`), hexadecimal escape sequences (`\x63\x61\x74\x73`), or
  percent-encoding (`%4d%65%78%69%63%6f`) — the **entire
  submission, including any surrounding plaintext, might not be evaluated**. Make
  sure all content you send to Automated Reasoning checks is plaintext.
* **No off-topic detection.** Automated Reasoning only
  analyzes text that is relevant to the policy. It ignores unrelated content and cannot
  tell you whether a response is off-topic. To detect off-topic responses, use [topic policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html#guardrails-topic-policies).
* **No streaming support.** Automated Reasoning checks
  do not support streaming APIs. You must validate complete responses.
* **English only.** Automated Reasoning checks currently
  support English (US) only.
* **Scope limited to your policy.** A `VALID`
  result guarantees validity only for the parts of the input captured through policy
  variables. Statements that fall outside the scope of your policy's variables are not
  validated. For example, "I can submit my homework late because I have a fake doctor's
  note" might be deemed valid if the policy has no variable to capture whether the doctor's
  note is fake.

Automated Reasoning checks complement other Amazon Bedrock Guardrails features like content filters and topic
policies. For the best protection, use them together. For more information, see [Guardrail
components](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html).

## End-to-end workflow overview

Using Automated Reasoning checks involves four phases: creating a policy, testing it,
deploying it in a guardrail, and integrating it into your application.

```
Source Document ──► Extracted Policy ──► Testing ──► Deployment ──► Integration
    (rules)          (formal logic)      (verify)    (guardrail)    (validate responses
                                                                     and act on feedback)
```

1. **Create a policy.** Upload a source document that
   contains the rules you want to enforce. Automated Reasoning extracts formal logic rules
   and a schema of variables from your document. A fidelity report is automatically generated
   that measures how accurately the extracted policy represents your source documents, with
   coverage and accuracy scores and detailed grounding that links each rule and variable back
   to the specific statements in your source content. Review the extracted policy and fidelity
   report to ensure the policy captures your rules correctly. For more information, see [Create your Automated Reasoning policy](./create-automated-reasoning-policy.html).
2. **Test and refine.** Tests help ensure that your policy
   can accurately validate generated content even while you make changes to the policy itself.
   Create tests that mimic the questions your users will ask and the responses your LLM might
   generate. Automated Reasoning checks use multiple foundation models to translate natural
   language into logic representations. Use generated scenarios to validate rule correctness
   and QnA tests to validate the natural language to logic translation accuracy. Refine your
   policy based on test results.
   For more information, see [Test an Automated Reasoning policy](./test-automated-reasoning-policy.html).
3. **Deploy.** Save an immutable version of your tested
   policy and attach it to a guardrail. You can automate deployment using CloudFormation or CI/CD
   pipelines. For more information, see [Deploy your Automated Reasoning policy in your application](./deploy-automated-reasoning-policy.html).
4. **Integrate.** At runtime, Automated Reasoning findings
   are returned through APIs that support an Amazon Bedrock Guardrails configuration, including `Converse`
   and `InvokeModel`, and through the standalone `ApplyGuardrail` API. Inspect the
   findings to decide whether to serve the response, rewrite it using the feedback, or ask the user
   for clarification. Automated Reasoning checks operate in *detect mode* only—they return
   findings and feedback rather than blocking content. For more information on how to integrate
   Automated Reasoning checks in your application, see [Integrate Automated Reasoning checks in your application](./integrate-automated-reasoning-checks.html). For more information on the permissions
   required to enable Automated Reasoning checks, see [Permissions for Automated Reasoning policies with ApplyGuardrail](./guardrail-automated-reasoning-permissions.html).

## Availability and language support

Automated Reasoning checks in Amazon Bedrock Guardrails are generally available in the following Regions:

* US East (N. Virginia)
* US West (Oregon)
* US East (Ohio)
* EU (Frankfurt)
* EU (Paris)
* EU (Ireland)
* Asia Pacific (Sydney)

Automated Reasoning checks currently support English (US) only.

## Limitations and considerations

Before implementing Automated Reasoning checks, be aware of these technical
limitations:

* **Document complexity.** Source documents should be
  well-structured with clear, unambiguous rules. Highly complex documents with nested
  conditions or contradictory statements may not extract cleanly into formal logic.
  Input documents are limited to 5 MB in size and 50,000 characters. You can split larger
  documents and merge each section into your policy. Images and tables in documents also
  impact the number of input characters.
* **Processing time.** Automated Reasoning checks validation adds
  latency to your application responses. Plan for additional processing time, especially
  for complex policies with many variables. The number of variables in a policy directly
  contributes to increases in validation latency.
* **Policy scope.** To create policies that are easier to maintain,
  each policy should focus on a specific domain (for example, HR, finance, legal) rather than trying
  to cover multiple unrelated areas in a single policy.
* **Variable and rules limits.** Policies with excessive
  numbers of variables or overly complex rule interactions may hit processing limits or return
  TOO\_COMPLEX results. See [Amazon Bedrock
  limits documentation](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock) and [Validation results reference](./automated-reasoning-checks-concepts.html#ar-concept-validation-results).
* **Natural language dependency.** The accuracy of
  validation depends on how well natural language in user prompts and model
  responses can be translated to your policy's formal logic variables. Automated
  Reasoning checks use foundational models to translate natural language into logic
  representations. Variable descriptions influence the quality of this translation.
* **Non-linear arithmetic.** Automated Reasoning checks
  might timeout or return TOO\_COMPLEX if constraints involve reasoning with non-linear
  arithmetic (for example, irrational numbers or exponents).

## Pricing

Automated Reasoning checks in Amazon Bedrock Guardrails are charged based on the number of validation requests
processed. For current pricing information, see the [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/).

Charges are incurred for each validation request, regardless of the result (for example,
VALID, INVALID, TRANSLATION\_AMBIGUOUS). To optimize costs:

* Use appropriate confidence thresholds to balance accuracy with processing
  requirements.
* Consider caching validation results for identical or similar queries when appropriate
  for your use case.
* Monitor usage patterns and adjust policies to reduce unnecessary validation
  requests.

## Cross-Region inference

Automated Reasoning uses cross-Region inference to optimize the performance and
availability of policy creation, policy testing, and runtime validation. These operations
automatically distribute processing across multiple AWS Regions to ensure reliable service
delivery.

The following Automated Reasoning operations use cross-Region inference:

* `StartAutomatedReasoningPolicyBuildWorkflow` — Invoked during policy
  creation and compilation from source documents.
* `StartAutomatedReasoningPolicyTestWorkflow` — Invoked during policy
  validation and testing procedures.
* Runtime validation — Invoked when a guardrail that includes an Automated Reasoning
  policy checks content.

These operations use large language models. The models extract formal logic rules from
source documents and translate natural language into logic that Automated Reasoning checks
against your policy. The following table shows where Automated Reasoning might
process a request, based on the Region where the request originates.

Where Automated Reasoning processes requests

| Request originates in | Automated Reasoning might process the request in |
| --- | --- |
| US East (N. Virginia), US West (Oregon), US East (Ohio) | Any supported US Region |
| EU (Frankfurt), EU (Paris), EU (Ireland) | Any supported EU Region |
| Asia Pacific (Sydney) | Any supported Region in Australia |

###### Important

Customer data remains within the geographic boundary where the request originates
(the United States, the European Union, or Australia). AWS processes this data in
accordance with AWS data residency commitments.

Cross-Region inference operates transparently without requiring customer configuration.
API functionality remains consistent regardless of the specific Region that processes the
request.

###### Topics

* [Automated Reasoning checks concepts](./automated-reasoning-checks-concepts.html)
* [Create your Automated Reasoning policy](./create-automated-reasoning-policy.html)
* [Automated Reasoning policy best practices](./automated-reasoning-policy-best-practices.html)
* [Test an Automated Reasoning policy](./test-automated-reasoning-policy.html)
* [Troubleshoot and refine your Automated Reasoning policy](./address-failed-automated-reasoning-tests.html)
* [Use Kiro CLI with an Automated Reasoning policy](./kiro-cli-automated-reasoning-policy.html)
* [Deploy your Automated Reasoning policy in your application](./deploy-automated-reasoning-policy.html)
* [Integrate Automated Reasoning checks in your application](./integrate-automated-reasoning-checks.html)
# AIP-C01 v2 First Diagnostics (Stage 1)

Research date: 2026-10-06. Purpose: test whether the learner can already do the job, before the crash course begins.

RULES: All items below are original exam-style practice questions written for this diagnostic. They are NOT real exam questions and do not reconstruct any real exam content. Answer key is in answers-hidden-v2.md (separate file) - do not merge. Mastery for all: unknown.

---

## D1 - Foundation Model Integration (Questions 1-3)

**Q1.** A company wants a support chatbot whose answers must cite the current product manual. The manual is updated every month. A teammate proposes fine-tuning the model on the manual each month. A second teammate proposes a knowledge base with a monthly sync schedule. Which approach is correct, and what is the single decisive reason?

**Q2.** An application team must switch between three different FM providers without redeploying code. Which three AWS services form the canonical configuration-driven pattern for this, and what role does each play?

**Q3.** A RAG system returns confident but wrong answers. The retrieved chunks look relevant to a human reader. Name the first thing to investigate and the last thing to investigate, and explain why the investigation order matters.

## D2 - Implementation and Integration (Questions 4-5)

**Q4.** An agent workflow needs a human approval step that can wait up to 4 hours, then calls a model and three tools in sequence. A developer proposes implementing the whole flow in a single Lambda function. Name the specific reason this fails and the AWS service that should own the workflow instead.

**Q5.** An application bought provisioned throughput for a Bedrock model but still sees throttling errors. The code calls the base model ID directly. What is the bug, and what is the one-line fix?

## D3 - Safety, Security, Governance (Questions 6-7)

**Q6.** A children's tutoring app must (a) block profanity in user inputs, (b) refuse to give medical diagnoses, and (c) redact Social Security numbers from outputs. Match each requirement to the correct guardrail control type, and name the one control type that would be wrong for all three.

**Q7.** A regulated customer requires that no Bedrock API traffic crosses the public internet and that invocation logs are encrypted. Name the two AWS features that satisfy these requirements and the compliance risk of skipping each one.

## D4 - Operational Efficiency (Question 8)

**Q8.** A company runs the same 8,000-token system prompt on every request and pays full input-token price each time. Separately, it has steady baseline traffic that keeps getting throttled at peak. Name the cost lever for the first problem and the throughput lever for the second, and explain why the two levers are not interchangeable.

## D5 - Testing and Troubleshooting (Question 9)

**Q9.** After a prompt template update, a summarization feature starts producing off-brand tone. Which two evaluation/validation practices would have caught this before production, and which one runs continuously after deployment?

## Prerequisites (Question 10)

**Q10.** An agent needs to remember a conversation for three weeks and also search 50,000 PDF documents. A developer proposes storing both the conversation history and the PDFs in ElastiCache for speed. Name the two correct storage choices instead, and state the one-sentence rule that makes ElastiCache wrong for both jobs.

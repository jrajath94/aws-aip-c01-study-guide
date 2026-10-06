# AIP-C01 Senior Decision Playbook v1.0

Research date: 2026-10-06. This playbook extends the L12 7-step method in fragments/stage8.html (section l12-method). It does not replace it. Use the study mode to learn the moves. Use the timed mode under pressure. Every example reuses a course scenario.

## Study mode: 10 steps

1. Name what the question asks and the lifecycle stage (design, build, production, incident).
2. Quote the objective and the hard constraints in the stem's own words.
3. Name the layer where the problem lives: model, retrieval, network, IAM, encryption, orchestration, deployment, capacity, evaluation, or governance.
4. Check documented feature, model, API, and Region compatibility at the current date.
5. Eliminate every infeasible option. Cite the exact clause it violates.
6. Rank the survivors on the stated objective: fixed costs, operations load, failure domains, dependencies.
7. Check authorization, freshness, logging, state, and fallback boundaries end to end.
8. Verify the pick satisfies the entire scenario, not just the headline requirement.
9. State why each plausible alternative loses, and name the minimal change that would flip the decision.
10. Give the best evidence and name any genuinely unresolved assumption. Never invent a hidden priority to force a preferred service.

## Timed mode: ASK, MUST, LAYER, ELIMINATE, RANK, CHECK SET

ASK: what is the question really asking? MUST: which constraints are hard (security, residency, budget cap)? LAYER: which layer decides (network vs IAM vs model)? ELIMINATE: drop every option that violates a hard constraint. RANK: order survivors by the stated objective. CHECK SET: for Select TWO/THREE, verify the set jointly covers all required controls with no contradiction.

Multi-select set matrix. Build it for every multi-select item:

| Combination | Supported | All hard constraints | Objective fit | Missing or contradictory element | Retain or reject |
|---|---|---|---|---|---|

Rules: evaluate each option's eligibility first. Reject individually useful options that leave the system incomplete. Never add a missing KMS permission, validator, approval, or fallback to rescue an option silently. If two sets stay equally defensible, the item is ambiguous: revise it, do not guess.

## Worked example 1. Residency vs private path (Q27, fixed)

Scenario. A hospital needs Bedrock models. Patient data at rest must stay in the hospital data center. The link to AWS must be private and controlled.

1. Lifecycle: design. 2. Objective: "FM access with data residency and private connectivity." Hard constraints: data at rest stays on premises, Bedrock usable, link private. 3. Layer: network plus processing geography. 4. Compatibility: Bedrock is regional [Behavior]. Outposts runs AWS services on premises [Behavior]. 5. Eliminate: public S3 bucket (breaks residency), Wavelength (edge, not on-premises), no-AWS local model (drops Bedrock), public internet with TLS (not a private link). 6. Rank: Outposts for data and app plus private routing to Bedrock in-Region. 7. Boundaries: prompt content is processed in-Region. The private link protects transit only. 8. Verify: data at rest stays, Bedrock serves, link is private. 9. Alternatives lose as in step 5. Minimal flip: if the rule became "data at rest," the same set still wins. If the rule became "never processed outside," no Bedrock architecture wins (see CB-17). 10. Evidence: patch P-G09. Assumption: the jurisdiction accepts in-Region processing of prompts under its processor terms. Confirm with counsel, do not assume.

## Worked example 2. Retry storm (Q30)

Scenario. A booking assistant calls Bedrock at peak. Throttling spikes at 7 PM. Failures cascade into user-visible errors.

1. Lifecycle: production incident. 2. Objective: "smooth retries and keep the assistant useful when the model is slow." 3. Layer: resilience (SDK behavior plus fallback). 4. Compatibility: SDK retries with backoff are documented [Behavior]. 5. Eliminate: instant retries (amplify throttling), X-Ray as a retry mechanism (observes, does not retry), no timeouts (hangs forever), bigger window (unrelated). 6. Rank: backoff with jitter first (fixes the storm), graceful degradation second (covers remaining failures). 7. Boundaries: fallback answers must carry the same safety policy (CB-08 rule). 8. Verify: retries spread, users stay served. 9. Alternatives lose as in step 5. Minimal flip: if throttling never occurred, the fallback alone would suffice. 10. Evidence: L6 resilience. No unresolved assumption.

## Worked example 3. Policy evaluation (Q38)

Scenario. A support agent role needs Bedrock access only through the company VPC endpoint and must never read the raw PII bucket.

1. Lifecycle: build. 2. Objective: endpoint restriction plus a hard data boundary. 3. Layer: IAM (identity policy plus condition plus explicit deny). 4. Compatibility: aws:SourceVpce condition key is documented [Behavior]. 5. Eliminate: broad Bedrock with no condition (any network path), s3:* on * (opens the PII bucket), no policy (no boundary). 6. Rank: only one feasible option remains. 7. Boundaries: check the endpoint policy too. An identity allow means nothing if the endpoint policy denies. 8. Verify: condition pins the path, deny blocks the bucket. 9. Alternatives lose as in step 5. Minimal flip: if the endpoint policy denied Bedrock, even the winning draft would fail. Check both sides. 10. Evidence: L9 five-checkpoint evaluation. Assumption: the endpoint ID in the condition is current. Verify it.

## The senior mindset in one page

Never rank an explicit security violation against cost. Prefer the managed or simpler solution only when it satisfies the requirements and wins the stated objective. Treat unknown support as a verification need, not a confident failure. Admit when a real design needs information instead of inventing it. Senior means visible requirements, correct mechanisms, justified comparisons, safe boundaries, and evidence.

*End of playbook. Pair with the L12 7-step method and the curveball bank.*

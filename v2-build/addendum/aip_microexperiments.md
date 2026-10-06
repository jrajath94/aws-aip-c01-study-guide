# AIP-C01 Russian-Doll Microexperiments v1.0

Research date: 2026-10-06. Three concepts the audit found under-taught, each opened shell by shell. Shell 0 names the confusion. Shell 1 builds a tiny toy. Shell 2 counts or scores it. Shell 3 applies one rule. Shell 4 shows the new symbol. Shell 5 compares the nearest alternative. Shell 6 transfers to a new scenario. Computed values are original toy arithmetic. Figures follow the visual law: one plate per decisive state change, flat fills, no decoration.

---

## Lab 1. Private path vs processing geography

Shell 0. The confusion: a private network path does not decide where the model runs. The decision: where does patient data get processed when the app uses Outposts plus a private link to Bedrock?

Shell 1. Toy: one hospital app on Outposts, one Direct Connect link, one Bedrock endpoint in eu-west-1. The app sends a prompt with 400 tokens of patient notes.

Shell 2. Score the toy: the prompt travels the private link (transit protected), then Bedrock runs inference in eu-west-1 (processing in-Region). Two locations, two facts: transit = private, processing = eu-west-1.

Shell 3. Apply the one rule: processing geography follows the service that executes, not the path that carries. The executor here is Bedrock in eu-west-1.

Shell 4. New symbol: a two-cell stamp on every request, PATH: private plus EXEC: eu-west-1. Both cells must satisfy the rule, not one.

Shell 5. Nearest alternative: self-host the model on Outposts with SageMaker. PATH: local, EXEC: on-premises. Both cells satisfy an absolute rule, at the cost of running the model yourself.

Shell 6. Transfer: a bank uses a VPC endpoint to Bedrock and claims "data never leaves the VPC." Name the decisive phrase.

Answer. "The endpoint keeps traffic private. It never moves data residency. The Region does that" (L9). The claim confuses PATH with EXEC again.

<figure id="fig-ad-path-exec">
<img src="assets/img/v2/ad-path-exec-1.png" alt="Request path versus execution location, before and after applying the one rule">
<figcaption>Shell 3. Apply the one rule. Source: original toy.</figcaption>
</figure>

## Lab 2. Retrieval candidates vs context vs output

Shell 0. The confusion: "the retriever found good chunks" does not mean "the answer is grounded." The decision: which layer failed when the answer is wrong?

Shell 1. Toy: a policy KB, one question about refund order 88231. The retriever returns 5 candidate chunks: 3 about order 88231, 2 about order 88232.

Shell 2. Score the toy: candidates = 5 chunks (mixed). Context = the 3 chunks the app pastes into the prompt (it drops 2). Output = the answer text the model writes.

Shell 3. Apply the one rule: diagnose the layers separately. Relevance scoring tests candidates. Context-match verification tests whether the output's claims trace to the context. One test per layer.

Shell 4. New symbol: three boxes in a row, CANDIDATES then CONTEXT then OUTPUT, with a separate check mark on each arrow.

Shell 5. Nearest alternative: "upgrade the model." It changes the OUTPUT box only. If candidates were wrong, the upgrade cannot fix them.

Shell 6. Transfer: a RAG answer cites a clause that exists in no retrieved chunk. Which layer failed, and what is the first diagnostic?

Answer. The OUTPUT layer (ungrounded generation). First diagnostic: context-match verification of the answer's claims against the retrieved chunks (qbank Q53).

<figure id="fig-ad-rag-layers">
<img src="assets/img/v2/ad-rag-layers-1.png" alt="Three boxes for candidates, context, and output with one check per arrow">
<figcaption>Shell 3. Apply the one rule. Source: original toy.</figcaption>
</figure>

## Lab 3. Cache key identity, version, freshness, and hit trace

Shell 0. The confusion: a cache hit is not automatically a correct hit. The decision: which key fields and checks make a hit safe?

Shell 1. Toy: one semantic cache, two tenants (A, B), prompt v1 then v2. Cache key starts as hash(question).

Shell 2. Score the toy: tenant B asks tenant A's question. Key matches (same question). Hit serves tenant A's answer to tenant B. One hit, one leak.

Shell 3. Apply the one rule: the key must name every axis the answer varies on. New key = hash(tenant_id, role, prompt_version, model_id, normalized question). Re-run the toy: tenant B's lookup misses (tenant differs). Prompt v2's lookup misses (version differs). Two misses, zero leaks.

Shell 4. New symbol: the key as five chips in a row. A hit is valid only when all five chips match and the hit-time authorization passes.

Shell 5. Nearest alternative: TTL expiry alone. It bounds staleness but never checks identity. A revoked tenant still hits until expiry.

Shell 6. Transfer: an employee receives a manager-only answer from cache. Which chip is absent, and what is the fix?

Answer. The role chip. Fix: scope keys by role (or separate caches per role) plus a hit-time role check (CB-04).

<figure id="fig-ad-cache-key">
<img src="assets/img/v2/ad-cache-key-1.png" alt="Cache key as five chips, before with one chip and after with five">
<figcaption>Shell 3. Apply the one rule. Source: original toy.</figcaption>
</figure>

---

*End of microexperiments. Each lab reuses its symbols in the curveball bank: Lab 1 in CB-17, Lab 2 in Q53 and CB-14, Lab 3 in CB-01 through CB-04.*

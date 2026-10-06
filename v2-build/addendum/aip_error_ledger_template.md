# AIP-C01 Error Ledger Template v1.0

Date: 2026-10-06. Purpose: adaptive remediation for the AIP-C01 crash course v2.
Rule: record only actual learner errors. No learner data exists yet. Every row
below is a template header, not a learner record. Mastery stays UNKNOWN until
the learner answers.

## How to use

1. Log each missed question or drill item as one row.
2. Fill the error class from the list below. Do not invent new classes.
3. Repair exactly the logged error. Do not assign a whole lesson.
4. Re-check with the unseen recheck item. Close the row only on a correct
   unseen recheck.

## Error classes

- wrong-fact: the learner stated a false service, limit, or API claim.
- weak-mechanism: the learner could not explain how the mechanism works.
- missed-qualifier: the learner ignored a word that changed the answer
  (private vs in-Region, expiry vs authorization, average vs p99).
- wrong-lifecycle: the learner answered for the wrong stage
  (design vs build vs production vs incident).
- wrong-layer: the learner named the wrong enforcement layer
  (model vs retrieval vs network vs IAM vs encryption).
- unsafe-combination: the learner picked a set that violates a hard rule.
- time-pressure: the learner knew the rule but ran out of time.

## Ledger rows

| # | Question | Skill | Trap axis | Given answer | Correct answer | Error class | Missed phrase | Wrong layer or assumption | Corrected boundary | Prerequisite or core link | Counterfactual that flips it | Unseen recheck | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | (example, not a learner record) Q27 | 2.3.4 | C05 | A+B | C | missed-qualifier | "data must stay in the hospital data center" | assumed private path equals in-Region processing | Bedrock inference runs in-Region, a VPC endpoint protects transit only | patch P-G09, bridge B-P10 | stem pins data at rest only | CB-17 | open |

## Priority order

Confident errors first. Hard-constraint violations first. Missed qualifiers
before weak mechanisms. One row repaired fully beats five rows skimmed.

## Advancement evidence

The learner advances when the row closes with a correct unseen recheck plus
a one-sentence mechanism explanation in the learner's own words. Counts and
percentages never prove readiness. No scaled-score conversion exists for this
exam. The official guide gives no raw-to-scaled mapping.

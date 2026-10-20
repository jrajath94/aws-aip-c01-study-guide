#!/usr/bin/env python3
"""
Enrich course slides with:
1. High-resolution architecture diagram / SVG asset paths
2. 5-Layer Russian Doll First-Principles Learning content:
   - Layer 1: First Principle Intuition
   - Layer 2: AWS Architecture Flow
   - Layer 3: Exact APIs, Parameters & Code
   - Layer 4: Amazon Traps & Limits
   - Layer 5: 2-Day Exam Decision Rule
3. Linked practice question IDs from the 250-question bank
"""

import json, os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Slide to Diagram Image Mapping
IMAGE_MAP = {
    "core-001": "../assets/img/density/cc-prereq-map.svg",
    "core-002": "../assets/img/density/cc-numbers.svg",
    "core-003": "../assets/img/custom/pat-exam-surface.svg",
    "core-004": "../assets/img/custom/pat1-constraints.svg",
    "core-005": "../assets/img/v2/d1-tokens-1.png",
    "core-006": "../assets/img/v2/d2-deploy-ladder-1.png",
    "core-007": "../assets/img/v2/s8-method-1.png",
    "core-008": "../assets/img/foundations/found-genai-arch.svg",
    "core-009": "../assets/img/v2/d1-model-switch-1.png",
    "core-010": "../assets/img/custom/sd-55-authtrio.svg",
    "core-011": "../assets/img/v2/s8-api-1.png",
    "core-012": "../assets/img/density/cc-converse-shape.svg",
    "core-013": "../assets/img/custom/bank-14-inference.svg",
    "core-014": "../assets/img/v2/d1-prompt-gov-1.png",
    "core-015": "../assets/img/density/cc-xregion.svg",
    "core-016": "../assets/img/custom/bank-42-loravsfull.svg",
    "core-017": "../assets/img/v2/s8-ladder-1.png",
    "core-018": "../assets/img/v2/d1-data-pipeline-1.png",
    "core-019": "../assets/img/density/cc-bda-flow.svg",
    "core-020": "../assets/img/v2/ad-rag-layers-1.png",
    "core-021": "../assets/img/custom/sd-35-vectorstores.svg",
    "core-022": "../assets/img/custom/sd-36-retrieval.svg",
    "core-023": "../assets/img/density/cc-vector-decision.svg",
    "core-024": "../assets/img/custom/sd-32-sync.svg",
    "core-025": "../assets/img/v2/d1-chunking-1.png",
    "core-026": "../assets/img/custom/sd-34-embeddings.svg",
    "core-027": "../assets/img/density/cc-rerank-before-after.svg",
    "core-028": "../assets/img/v2/s8-retrieval-1.png",
    "core-029": "../assets/img/v2/s8-rag-call-1.png",
    "core-030": "../assets/img/custom/bank-13-prompting.svg",
    "core-031": "../assets/img/custom/sd-52-session.svg",
    "core-032": "../assets/img/density/cc-prompt-lifecycle.svg",
    "core-033": "../assets/img/density/cc-flows.svg",
    "core-034": "../assets/img/v2/d2-agent-loop-1.png",
    "core-035": "../assets/img/density/cc-strands-loop.svg",
    "core-036": "../assets/img/v2/s8-loop-gate-1.png",
    "core-037": "../assets/img/custom/sd-47-multiagent.svg",
    "core-038": "../assets/img/custom/sd-45-tasktoken.svg",
    "core-039": "../assets/img/custom/bank-22-actions.svg",
    "core-040": "../assets/img/v2/d2-mcp-1.png",
    "core-041": "../assets/img/density/cc-agentcore.svg",
    "core-042": "../assets/img/v2/d2-deploy-ladder-1.png",
    "core-043": "../assets/img/foundations/found-instance-types.svg",
    "core-044": "../assets/img/density/cc-model-funnel.svg",
    "core-045": "../assets/img/foundations/found-messaging.svg",
    "core-046": "../assets/img/foundations/found-sso-vs-roles.svg",
    "core-047": "../assets/img/foundations/found-regions.svg",
    "core-048": "../assets/img/v2/d2-gateway-1.png",
    "core-049": "../assets/img/mermaid/03-sync-async-decision.svg",
    "core-050": "../assets/img/custom/sd-53-streaming.svg",
    "core-051": "../assets/img/density/d2-retry-backoff.svg",
    "core-052": "../assets/img/custom/pat5-ladder.svg",
    "core-053": "../assets/img/foundations/found-api-gateway.svg",
    "core-054": "../assets/img/custom/sd-46-agentdebug.svg",
    "core-055": "../assets/img/v2/d3-injection-1.png",
    "core-056": "../assets/img/v2/d3-guardrail-1.png",
    "core-057": "../assets/img/v2/d3-detect-block-1.png",
    "core-058": "../assets/img/density/d3-grounding-example.svg",
    "core-059": "../assets/img/density/cc-reasoning-tradeoff.svg",
    "core-060": "../assets/img/v2/d3-vpc-endpoint-1.png",
    "core-061": "../assets/img/v2/d3-envelope-1.png",
    "core-062": "../assets/img/v2/d3-macie-1.png",
    "core-063": "../assets/img/density/cc-privacy.svg",
    "core-064": "../assets/img/density/d3-model-card.svg",
    "core-065": "../assets/img/custom/bank-31-controls.svg",
    "core-066": "../assets/img/density/d3-safety-eval.svg",
    "core-067": "../assets/img/custom/bank-34-responsible.svg",
    "core-068": "../assets/img/v2/d1-context-budget-1.png",
    "core-069": "../assets/img/v2/d4-cost-per-success-1.png",
    "core-070": "../assets/img/v2/d4-prompt-cache-1.png",
    "core-071": "../assets/img/v2/ad-cache-key-1.png",
    "core-072": "../assets/img/v2/d2-break-even-1.svg",
    "core-073": "../assets/img/v2/d4-latency-tail-1.png",
    "core-074": "../assets/img/density/cc-rag-stages.svg",
    "core-075": "../assets/img/v2/d4-observability-1.png",
    "core-076": "../assets/img/density/cc-three-logs.svg",
    "core-077": "../assets/img/v2/d4-agent-trace-1.png",
    "core-078": "../assets/img/v2/d5-troubleshoot-1.png",
    "core-079": "../assets/img/custom/d5-eval-matrix.svg",
    "core-080": "../assets/img/custom/bank-51-evalmethods.svg",
    "core-081": "../assets/img/v2/d5-judge-bias-1.png",
    "core-082": "../assets/img/v2/d5-ndcg-1.png",
    "core-083": "../assets/img/custom/sd-72-metrics.svg",
    "core-084": "../assets/img/mls2/mls2-groundtruth.svg",
    "core-085": "../assets/img/v2/d5-holdout-leak-1.png",
    "core-086": "../assets/img/custom/bank-16-costlatency.svg",
    "core-087": "../assets/img/v2/ad-path-exec-1.png",
    "core-088": "../assets/img/density/cc-eval-harness.svg",
    "core-089": "../assets/img/density/d1-retrieval-debug.svg",
    "core-090": "../assets/img/density/d2-retry-backoff.svg",
    "core-091": "../assets/img/custom/d5-trap-traditional-fix.svg",
    "core-092": "../assets/img/density/cc-chunking-before-after.svg",
    "core-093": "../assets/img/v2/d1-rag-1.png",
    "core-094": "../assets/img/v2/d2-agent-loop-1.png",
    "core-095": "../assets/img/density/cc-numbers.svg",
}

print("Loaded image map for all slides.")

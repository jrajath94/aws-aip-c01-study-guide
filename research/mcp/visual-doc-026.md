AWS Documentation from https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/arch-agent-layer.html:

# The AI agent layer

AVX’s intelligence lives in an Amazon Bedrock AgentCore runtime. The runtime hosts a
Strands Agents SDK supervisor agent that receives requests from all channels (voice, chat,
web, Connect), selects the appropriate tools, orchestrates cross-system data retrieval, and
synthesizes a grounded, persona-aware response.

## Bedrock AgentCore runtime

The AgentCore runtime is a managed container service that runs the supervisor agent code.
It handles the request lifecycle — accepting an inbound session, invoking the Python handler,
streaming the response back, and managing session isolation. Two runtime variants are
deployed per stage:

* A **bidirectional streaming runtime** (`vsa_supervisor_bidi_*`) that handles the Nova
  Sonic voice channel. It uses the Strands `BidiAgent` pattern for full-duplex
  speech-to-speech streaming, targeting a first-audio-token latency under 1.5 seconds from
  end of user speech.
* A **text (HTTP) runtime** (`vsa_supervisor_text_*`) that handles the REST-based web chat
  channel, the Connect Chat channel, and the mobile/web channel. It returns JSON-serialized
  responses over a standard HTTP unary path.

Both runtimes execute the same supervisor handler and invoke the same tool catalog;
the distinction is only in the transport and streaming mode.

## Supervisor agent

The supervisor is a Strands `Agent` or `BidiAgent` backed by **Claude Sonnet** via Bedrock
on-demand inference. Its responsibility is orchestration, not data retrieval: it classifies
the intent of the incoming message, selects the appropriate tool or sequence of tools, passes
structured arguments derived from session context, and synthesizes the tool results into a
coherent, persona-appropriate response.

The supervisor does not freeform-generate diagnostic conclusions. Criticality classification
is always a deterministic tool call — the triage classifier reads active DTCs, telemetry
thresholds, open recalls, and tenant policy overrides and returns a structured P0–P3
classification with a reason trace. The supervisor’s role is to narrate the result, not to
re-derive it from the model’s knowledge.

## Tool catalog

The supervisor dispatches to a catalog of seven functional tools:

| Tool | Function |
| --- | --- |
| `triage()` | Deterministic criticality classification. Inputs: active DTCs with severity codes, telemetry snapshot (coolant temp, brake wear, tire pressure delta), open recalls, tenant policy overrides. Output: P0 (Stop Driving), P1 (Service Now), P2 (Service Soon), or P3 (Monitor), with a structured reason trace. Implemented as a rules engine, not an LLM call. |
| `book()` | Creates a STAR-JSON service ticket and optionally writes the appointment record to the CMS `service-history` table (controlled by the `VSA_BOOK_WRITE_CMS` environment variable). All booking artifacts are emitted as STAR-shaped JSON regardless of whether the CMS write is enabled. |
| `escalate()` | Hands the session to a tier-2 human-agent queue in Amazon Connect. Packages transcript, triage output, VIN context, warranty coverage summary, and the draft STAR ticket as the handoff payload. On a P0 the driver is offered escalation as a one-tap action, or it happens automatically if the tenant enables `escalation.autoOpenHumanChatOnP0`; LLM output cannot override a P0 result. |
| `knowledge()` | Retrieves reference content from the ADP Bedrock Knowledge Base via cross-account Bedrock Retrieve. Applies persona-scoped source-category filters — for example, the Service Advisor persona retrieves TSBs and service policy; the Technician persona retrieves DTC guides and repair procedures. Returns top-ranked grounded passages with citation references. |
| `vehicle_identity()` | Decodes a VIN into make, model, year, powertrain, and trim from ADP Vehicle Identity data loaded in AgentCore Memory LTM. Supports all six personas. |
| `service_network()` | Retrieves service center locations, specialties, hours of operation, and estimated wait time from ADP Service Network data. Uses VIN-derived powertrain type and customer location to rank results by relevance and proximity. |
| `parts_lookup()` | Retrieves OEM part numbers, list prices, fleet pricing, and stock availability from the ADP Parts Catalog via Bedrock KB Retrieve with `source_category=parts_catalog` filter. Returns structured pricing data and cross-references to ADP’s DTC diagnostic guides for repair-context lookup. |

Each tool is a Python function registered with the Strands agent. Tool arguments are derived
from session context (VIN, tenant ID, persona, live vehicle state) plus the supervisor’s
structured extraction from the user’s utterance. Tools do not receive raw freeform text.

## Tier 2 autonomous agent platform

The Tier 1 supervisor dispatches tools and narrates results; it does not run multi-step reasoning over large data sets inside a conversational turn.
The Tier 2 autonomous agent platform handles that workload: four loyalty-flywheel agents for owners and five Fleet Intelligence agents for fleets run on EventBridge Scheduler, event rules or an Amazon SQS queue, reason over ownership and fleet data where no one is waiting, and write Findings to `vsa-{stage}-avx-findings`. The table lists the flywheel agents; [Fleet Intelligence agents](./fi-agents.html) describes the Fleet Intelligence agents.

| Agent | `agent_id` | Trigger | Tier 1 read tool |
| --- | --- | --- | --- |
| Energy and Charging Advocate | `agent-1-energy` | Daily per VIN; charging-session end; tariff change | `get_energy_advice()` |
| Vehicle Health and Service Agent | `agent-2-vehicle-health` | ADP prediction or alert arrival; DTC threshold crossing; service-interval approach; daily per component | `get_health_findings()` |
| Ownership Cost and Coverage Advocate | `agent-3-ownership-cost` | Service event; warranty-verdict change; recall publication; tenure milestone; daily prepaid sweep | `get_coverage()`, `get_loyalty_standing()` |
| Household Mobility Concierge | `agent-4-concierge` | Continuous position trigger; equity threshold; finance milestone; household change | `get_ownership_position()` |

Each agent module provides a `SYSTEM_PROMPT`, goal scope (the finding kinds it may write), a read stack, and an agent factory (`make_strands_agent_fn`).
Registering a new agent module does not change the runner, Finding contract, or delivery infrastructure.
Each agent reads the data platform at source — cross-account Athena on ADP curated products and DMS tables — not AgentCore Memory, which is session-scoped and unavailable in a Tier 2 run.
A per-run token and cost cap bounds inference spend; alarms go to an operator SNS topic so that a failed scheduled run generates a page.
See [Agentic Architecture](./agentic-architecture.html) and [Tier 2 Autonomous Agents](./avx-agent-pattern.html) for the trigger topology, dry-run mode, and backfill pattern.

## Findings and Actions data plane

Tier 2 agents write through a shared `write_finding()` helper into `vsa-{stage}-avx-findings` (GSIs per scope: owner, VIN, fleet, dealership, district).

Finding contract fields: `finding_id`, `finding_key` (SHA-256 of agent\_id + scope field/value + finding\_kind; persistent conditions update in place rather than appending new rows), `agent_id`, `agent_version`, `scope` (exactly one of vin / owner\_id / fleet\_id / dealership\_id / district\_id / population\_id), `severity` (p0|attention|soon|routine|informational), `computed_at`, `expires_at`, `confidence` (low|medium|high), `finding_kind`, `headline` (≤120 characters), `detail`, `evidence[]` (each entry: kind, source, source\_ref, value, computed\_at, provenance, vin), `inputs_hash`, `tokens_used`, `cost_usd`, `disclosure_txt`, and `audit_trail[]`.

Actions record what happens when an owner or automated process acts on a Finding.
The `vsa-{stage}-avx-actions` table carries: `action_id`, `finding_id`, `created_by`, `created_at`, `updated_at`, `target_system`, `target_ref`, `status` (pending\_execution|executed|in\_progress|completed|cancelled|declined|dismissed|failed), `action_kind`, `parameters`, copied `evidence[]`, and `audit_trail[]`.

The AVX API exposes `GET /findings/…​` (owner, vehicle, fleet, dealership scopes, each returning `computed_at`), `POST /findings/{id}/approve`, `POST /actions/{id}/dismiss`, and `GET /actions/…​`.

Eight executors dispatch approved actions (`agents/executors/registry.py`):

| Executor | Function |
| --- | --- |
| `dms` | Creates a repair order in the dealer’s DMS with the `avx_action_id` reference. Status updates arrive from `dms.ro.status_changed` events. |
| `vehicle-command` | Issues remote commands via the CMS vehicle-command API. |
| `retail` | Calls the Acquire `lead_capture` or `configurator_recommend` tool; used for upgrade and trade-in transitions. |
| `none` | Advisory only. Records an audit-trail entry; makes no external call. |
| `chat` | Pre-seeds a Tier 1 conversation from the Finding’s evidence so the owner opens a context-loaded session. |
| `ios-owner` | Delivers an owner-inbox card and push notification through the outreach broker. |
| `cms` | Applies fleet changes to CMS’s own records through its Fleet Intelligence API: cost actions, groundings and vehicle moves. |
| `adp` | Records a product engineer’s decision in ADP’s digital thread through the `adp-{stage}-digital-thread-writer` Lambda function, which also creates and issues the linked campaign. |

Boundary: Tier 2 agents write Findings and never dispatch Actions directly.
Executor modules are not importable from agent modules, and no agent calls a channel API.
Failure handling: a 4xx refusal sets status `declined`; an exhausted-retry 4xx client error or 5xx/timeout sets `failed` and fires dual escalation — an owner card and a `vsa.avx.action.terminal_failure` CloudWatch metric.
Retry thresholds and escalation targets are per-executor SSM config.

## Outreach broker and notification service

The outreach broker (`vsa-{stage}-avx-broker`) consumes the DynamoDB stream on `vsa-{stage}-avx-findings` and owns: channel selection, per-category consent (safety, coverage, service), quiet-hours policy, frequency caps (default: 10 per day, 3 per hour), cardinality cap (default: 15 active cards), priority arbitration across competing Findings, and feedback demotion based on dismissals in the trailing 30 days.

Channel selection by urgency, context, and consent:

| Channel | Role |
| --- | --- |
| iOS push (Amazon SNS mobile push → APNs) | Primary proactive delivery. Carries ~40 characters; the tap deep-links to a Tier 1 conversation pre-seeded with `avx_finding_id`. |
| In-app AVX Cards tab | Every Finding at every severity appears as a card. The owner can approve, dismiss, or drill down. |
| In-app conversation (Tier 1, WebSocket) | Full reasoning after tapping the push notification or a card’s drill-down CTA. |
| Amazon Connect outbound voice | Safety-adjacent urgency only — for example, blowout risk or a P0 callback. |
| SMS / email | Owners without the app; confirmations of record. |
| In-vehicle display | Contextual delivery where the OEM’s vehicle API supports it. |

Broker policy is SSM config: `/vsa/{stage}/avx/broker/apns-severity-threshold` (default `p0`; every severity creates an in-app card), `/rate-limit` (default day 10, hour 3), `/cardinality-cap` (default 15).
Device tokens and per-category consent are stored in `vsa-{stage}-notification-devices`, registered via `POST /notifications/register-device`.
The notification service is shared across the portfolio; DMS tenant notifications use the same delivery path.
<!-- OpenDocKit author guidance
ID: ai.comprehensive.docs.ai-systems.monitoring.md
Purpose: Explain observation and intervention for an AI capability in use.
Use when: Production AI behavior can drift or differ from evaluation.
Suggested destination: docs/ai-systems/monitoring.md
Boundary: Evaluation owns pre-release evidence; actual signals/config own monitoring definitions.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Monitoring

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Questions and signals

{{Map quality/risk/cost/latency questions to safe observations and canonical signal sources.}}

## Interpretation

{{Describe ground-truth availability, proxy limits, sampling, bias and drift detection assumptions.}}

## Intervention

{{Link actionable conditions to escalation, human review, fallback or disabling behavior with authority.}}

## Privacy and upkeep

{{Record data minimization/access/retention and updates when model/prompt/context changes.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Signals acknowledge proxy limitations.
- [ ] Interventions have owners and authority.
- [ ] Monitoring preserves privacy.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.

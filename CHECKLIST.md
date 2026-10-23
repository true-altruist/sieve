# SIEVE checklist

Print it, pin it, use it. The full reasoning is in [FRAMEWORK.md](FRAMEWORK.md).

## Every loop

**D · Document**
- [ ] A written context document exists before any generation starts
- [ ] It carries a data classification (public, internal, confidential)
- [ ] It states trust boundaries and what the machine may see and touch
- [ ] Any pasted or fetched material is treated as data, never as instructions

**A · Anchor**
- [ ] One source of truth is named per question (spec, library, board, lockfile, vault, threat model, `SECURITY.md`)
- [ ] Every new dependency is checked against the registry and the approved list
- [ ] Disagreements between sources are written down, not resolved silently

**H · Hold**
- [ ] Guardrails live in the repo and run automatically
- [ ] No secrets in prompts or code
- [ ] Agents run with least privilege: read only by default, sandboxed, network allowlist, no production credentials
- [ ] Anything irreversible needs a human approval
- [ ] Dependencies are pinned

**N · Narrow**
- [ ] One change in this loop
- [ ] The loop ends with something runnable
- [ ] It ran in a sandbox, and any elevated permission has been revoked

**I · Inspect**
- [ ] Scripted eye: static analysis, dependency audit, secret scan, SBOM
- [ ] Human eye: authentication, authorisation, data flows, trust boundaries
- [ ] The machine that wrote it is not its only reviewer
- [ ] High-risk change? A third look from someone outside the loop

**N · Name**
- [ ] Placeholders, simulated steps and known gaps are stated in the deliverable
- [ ] The debt register lists each item with an owner and an expiry date
- [ ] Machine-generated work is marked as such

## Every week

**S · Size**
- [ ] r is measured (not estimated) for each artefact class in use
- [ ] R for the week is written down
- [ ] Commissioned work is at or below `(R / r) × a`
- [ ] Nothing unreviewed sits anywhere that implies it was reviewed

**I · Instrument**
- [ ] Each artefact states its claims separately from its argument
- [ ] Each claim points to a source precise enough to re-open
- [ ] What is not established is stated
- [ ] Every observation carries the date it was made

**E · Escalate**
- [ ] Every artefact has a review class, set from its context document
- [ ] Irreversible and load-bearing work got a full read and a second pair of eyes
- [ ] Legally or contractually operative work has a named owner and a date

**V · Verify**
- [ ] Batches are checked on one surface, not one by one
- [ ] The surface shows the property itself, not a proxy
- [ ] The surface shows all n, with nothing truncated

**E · Expire**
- [ ] Every observational claim has a re-check date before its use date
- [ ] Debt register expiry dates are on the same schedule
- [ ] A job, not a person's memory, fires the re-checks
- [ ] The re-check can hold a publish and cannot push one

**The corollary**
- [ ] If a is low, the generator is being fixed, not the reviewer worked harder

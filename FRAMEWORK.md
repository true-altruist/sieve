# SIEVE

**A framework for work where a machine makes the artefacts and a person is answerable for them.**

Version 1.0 · October 2026 · Ussama Dahnin

---

## The short version

Generative tools made producing things almost free. They did nothing to the cost of checking them. Once that is true, the constraint on any operation is no longer how much it can make but how much one answerable person can stand behind.

SIEVE works at two scales, under the same three laws.

**Inside one loop**, six rules make a single change safe to stand behind: **D**ocument, **A**nchor, **H**old, **N**arrow, **I**nspect, **N**ame. Together they spell DAHNIN, and they govern one change, one context document, one diff, two pairs of eyes.

**Across many loops**, five practices decide which of forty artefacts a week one person can actually stand behind, and keep that true over time: **S**ize, **I**nstrument, **E**scalate, **V**erify, **E**xpire.

The loop rules make an artefact checkable. The portfolio practices decide what gets checked, in what order, on what surface, and when it gets checked again. The join between them is the fifth loop rule, *inspect twice*: inside a loop it is a step, across a portfolio it is the constraint on the whole operation.

```
                 THE THREE LAWS
   review-bound · free to make, costly to accept · perishable
                        │
        ┌───────────────┴────────────────┐
        │                                │
   THE LOOP  (one change)          THE PORTFOLIO  (forty a week)
   D  Document the context         S  Size the review budget
   A  Anchor to one truth          I  Instrument the artefact
   H  Hold the guardrails          E  Escalate by consequence
   N  Narrow the loop              V  Verify on one surface
   I  Inspect twice   ◄── join ──► E  Expire every verification
   N  Name what is not true yet
```

---

## The three laws

Everything below follows from these, and they are arithmetic rather than opinion.

### Law 1. Throughput is review-bound

Let **g** be the time to generate an artefact and **r** the time for a competent person to verify it. Generative tooling drives g towards zero. It does nothing whatsoever to r.

Once g is much smaller than r, generation capacity drops out of the equation entirely and output per day is:

```
shipped = (R / r) × a
```

where **R** is the reviewing minutes actually available in a day and **a** is the fraction of artefacts that survive review. Doubling your generation capacity changes nothing. Halving r, or raising a, changes everything.

The practical form: commission to the reviewing capacity, not the producing capacity. A desk that can write twelve pieces a week and read four is not a twelve-piece desk with a backlog. It is a four-piece desk accumulating a liability.

*Inside the loop*, this is why the loop is narrow. A small diff has a small r. A 3,000-line dump has an r nobody will actually pay.

### Law 2. Iterations are free to make and expensive to accept

Generation is cheap per attempt, so the natural behaviour is to iterate. But cost scales with reviewed iterations, not generated ones. Review every attempt and k iterations multiply r by k.

The practical form: put a cheap filter between generation and the human. Machine checks, a rule, a glance at a contact sheet: anything that discards the obvious failures before they reach the expensive eye. Generate many, show few.

*Inside the loop*, this is why guardrails live in the repo as code. A pre-commit hook is the cheapest filter there is, and every failure it catches is one the human never has to see.

### Law 3. A verification is perishable

A check establishes that something was true on the day it was checked. Where generation is fast, work is produced further ahead of when it is used, and verifications routinely expire before the artefact is published.

This is the law people miss, because it has no symptom until something is already wrong in public.

The practical form: every verification carries its date, and anything observational carries a scheduled re-check before it is used.

*Inside the loop*, this is why every item in the debt register has an expiry date. A temporary permission or a mocked login is a verification with a shelf life, exactly like a vendor's price.

### The corollary that costs the most to learn

**A low acceptance rate is a defect in the generator, not a workload for the reviewer.**

When a is poor, the instinct is to review harder. That is the expensive mistake: it spends the one resource that does not scale on a problem upstream of it. Stop, find out why the generator is producing rejects, and fix that. Raising a from 0.2 to 1.0 is a fivefold throughput gain and usually costs an afternoon. Reviewing five times as hard is not available at any price.

---

## Part one. The loop

Six rules for a single change. The working assumption behind all of them: the machine behaves like a fast, confident junior with no memory. So it gets written context, fixed anchors, hard limits, small tasks, two reviews, and it is never allowed to pretend something is finished when it isn't.

Every rule carries its security layer inside it rather than in a separate seventh rule. Security that sits in its own box tends to be skipped, and a framework that grows a new letter each time a concern appears loses credibility.

### D · Document the context first

**Rule.** Every loop starts from something written down, not from memory. If the context doesn't say, the work stops and asks.

**Security layer.** The context document carries a short security header: data classification (public, internal, confidential), trust boundaries, and exactly what the machine may see and touch. No classification, no loop.

**Why it matters.** Context is also an attack surface. READMEs, tickets, pasted documents and web pages fed to a model can hide instructions, a technique known as prompt injection. So context is written down and treated as untrusted input: the model reads it, it does not obey it.

### A · Anchor to the source of truth

**Rule.** One artefact wins per question: the spec for wording and rules, the design library for colour and type, the board for the journey. Disagreements get written down.

**Security layer.** The same logic covers security questions. The lockfile wins for dependencies. The secrets vault wins for credentials, and the code never does. The threat model wins for trust boundaries. A `SECURITY.md` in the repo wins for policy.

**Why it matters.** Models regularly suggest packages that do not exist, and attackers register those names in advance, a practice now called slopsquatting. Anchoring means every new dependency is checked against the registry and the approved list before it lands, never trusted because the model sounded confident.

### H · Hold the guardrails

**Rule.** The non-negotiables (for example: spec wording verbatim, WCAG AA, no personal data, mobile first, no emoji) live in the repo beside the code.

**Security layer.** Four more guardrails, under the same rule of living in the repo:

1. **No secrets in prompts or code.** Keys, tokens and connection strings never enter a chat window or a commit.
2. **Least privilege for agents.** Read only by default, sandboxed execution, network allowlist, never production credentials.
3. **Human approval for anything irreversible.** Deploys, deletions, permission changes, outbound messages.
4. **Pinned dependencies.** No floating versions.

**Why it matters.** Guardrails become code. Pre-commit hooks, secret scanning and policy checks run automatically, because a guardrail that depends on someone remembering it is only a suggestion.

### N · Narrow the loop

**Rule.** One change at a time, and every loop ends with something runnable.

**Security layer.** Each loop runs in a sandbox, not in production, and any elevated permission granted for the loop is revoked when it closes.

**Why it matters.** Small loops are a security control in their own right. A small diff can actually be reviewed; a 3,000-line dump cannot. The unit of risk is the blast radius, and narrow loops keep it small.

### I · Inspect twice

**Rule.** The four-eyes principle, adapted: a scripted check and a human look, because they catch different things.

**Security layer.** The scripted eye runs static analysis, a dependency audit and secret scanning, and produces an SBOM (software bill of materials). The human eye focuses where scripts are blind: authentication, authorisation, data flows, and anything crossing a trust boundary.

**Why it matters.** The machine that wrote the work is never its only reviewer. For high-risk changes (authentication, payments, personal data), a third look comes from someone who did not work on the loop.

### N · Name what is not true yet

**Rule.** Placeholders, simulated steps, proposals outside the spec and known gaps are all stated in the deliverable itself.

**Security layer.** A security debt register lives inside the deliverable: mocked authentication, stubbed encryption, disabled checks, temporary permissions and accepted risks, each with an owner and an expiry date. Machine-generated work is marked as such, so provenance survives.

**Why it matters.** "We'll add real auth later" is how prototypes become breaches. A fake login screen that quietly ships is one of the most common failures in machine-assisted builds. Naming it is what makes it visible before it goes live.

---

## Part two. The portfolio

The loop rules are complete for one loop. The problem they do not touch only appears once they are working: one person is now answerable for forty loops a week, and inspect twice has become the constraint on everything. The five practices below are what you do about that.

### S · Size the review budget before the work

Write down, in minutes, what verification a given artefact class actually takes, and what the week has available. Not an estimate of the ideal; a measurement of the real.

Then commission against that number. If the budget says four, do not start twelve on the grounds that the extra eight can wait. An unreviewed artefact is not neutral inventory. It is a claim nobody has stood behind, sitting in a place that implies somebody has.

The loop size is part of the measurement. A budget measured on narrow loops does not hold for wide ones, so the budget and the *Narrow* rule are checked together.

### I · Instrument the artefact so checking it is cheap

The cost of verifying an artefact is a property of how it was built, and therefore a design decision, not a fact of nature.

An artefact that is cheap to check carries, in itself:

- what it claims, separably from how it argues
- where each claim came from, precisely enough to re-open
- what is not established, stated rather than omitted
- the date each observation was made

Three of those four are already loop rules. *Anchor* gives you where each claim came from. *Name* gives you what is not established. *Document* gives you the context it was made under. Instrumenting is the discipline of making those loop outputs travel with the artefact instead of staying behind in the loop.

This is the highest-leverage practice in the framework, because it attacks r directly, and r is the only term in the equation that compounds across every artefact you will ever produce.

### E · Escalate by consequence, not by volume

Not every artefact deserves the same eye. Route by what a wrong one costs:

| Class | Example | Review |
|---|---|---|
| Reversible, private | A draft, a scratch file | Spot check |
| Reversible, public | A page you can correct | One competent read |
| Irreversible or load-bearing | A published claim, a migration, a payment | Full read, plus a second pair of eyes |
| Legally or contractually operative | Anything a regulator or counterparty will read | Full read, named owner, dated |

The class is set in the loop, not after it: the data classification in the context document (*Document*) and the irreversible actions listed under *Hold* decide the row before any work is produced. The third look that *Inspect* reserves for high-risk changes is the bottom two rows of this table.

The failure here is uniformity in either direction: giving a scratch file a senior review, or giving a published factual claim the same glance as a scratch file.

### V · Verify on one surface

Where n artefacts must be checked for the same property, build one surface that shows all n at once (a contact sheet, a table, a diff, a single report) rather than opening them one at a time.

This turns n × r into something much closer to r. It is the single largest practical saving available, and it is almost always a small piece of tooling rather than a process change. In practice the scripted eye from *Inspect* builds the surface and the human eye reads it.

Two warnings, both learned the hard way. The surface must show the property you are checking, not a proxy for it. And it must show all of n: a batch review that is truncated is worse than no batch review, because it produces confidence proportional to n on evidence proportional to what fitted on the screen.

### E · Expire every verification

A check gets a date and a shelf life. Anything observational (what a page said, what a vendor published, what a price was) gets a scheduled re-check before the artefact is used, with the re-check owned by something that will actually fire.

The expiry dates in the loop's debt register feed the same schedule. A temporary permission that outlives its date is a stale verification, and it is caught by the same job.

The re-check must be able to hold the artefact back, and must not be able to push it out. That asymmetry is the whole point: holding a good artefact for a day costs a day; publishing a false one costs the thing the operation runs on.

---

## Part three. How the two layers join

Each loop rule produces something a portfolio practice consumes. If a loop skips its rule, the practice downstream has nothing to work with.

| Loop rule | What the loop produces | Consumed by |
|---|---|---|
| D · Document | Context document with data classification and trust boundaries | **E · Escalate**: the classification sets the review class |
| A · Anchor | One named source of truth per question | **I · Instrument**: where each claim came from |
| H · Hold | Guardrails as code (hooks, scanners, policy checks) | **Law 2**: the cheap filter that raises a before the human looks |
| N · Narrow | One runnable change, small diff | **S · Size**: a small, measurable r |
| I · Inspect | Scripted check output plus a human read | **V · Verify**: the scripted eye builds the surface, the human eye reads it |
| N · Name | Debt register with owners and expiry dates | **I · Instrument** (what is not established) and **E · Expire** (the dates feed the re-check schedule) |

The two scales side by side:

| | The loop | The portfolio |
|---|---|---|
| Unit | One change | Everything one person is answerable for |
| Question | Is this change safe and complete? | Which of these forty can one person stand behind, and for how long? |
| Fails when | A loop is too large, or unverified work is called finished | Production outruns review, or a verification goes stale |
| Artefacts | Context document, diff, debt register | Review budget, instrumented artefact, re-check schedule |

Run the six rules inside every loop. Run the five practices across all of them.

---

## Mapping to recognised standards

The loop rules each point to a reference a security practitioner already knows, so the framework extends existing practice rather than inventing its own.

| Rule | Threat addressed | Reference |
|---|---|---|
| D · Document | Prompt injection through context | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (Prompt Injection) |
| A · Anchor | Invented or malicious packages | OWASP LLM Top 10 (Supply Chain), [SLSA](https://slsa.dev) |
| H · Hold | Secret leakage, over-privileged agents | OWASP LLM Top 10 (Sensitive Information Disclosure, Excessive Agency) |
| N · Narrow | Unreviewable changes, large blast radius | [NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) |
| I · Inspect | Undetected vulnerabilities | NIST SSDF, SBOM practice |
| N · Name | Hidden security debt reaching production | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) (Govern, Manage) |

The portfolio practices are operational rather than technical controls and are not mapped one to one. They are closest in spirit to the Govern and Manage functions of the NIST AI RMF.

---

## What it costs

**Instrumentation is the real bill.** Making artefacts self-checkable is work done once per artefact class and repaid on every artefact after. Expect the first one to take several times as long as the artefact itself.

**The review budget is a standing cost that never falls.** It is the point of the framework that this number is fixed and visible rather than fixed and hidden.

**Re-checks need a mechanism that fires without anybody remembering.** A dated line in a document is not a mechanism. A scheduled job that reads that document is. The same goes for guardrails: a rule nobody automated is a suggestion.

**Somebody has to be allowed to say no.** If review cannot reject, it is not review, and a is meaningless.

## What it does not do

It does not make the output correct. It makes the rate at which incorrect output reaches the world a function of a number you have chosen and can see.

It does not reduce the human work. It relocates it: out of reading everything badly, into instrumenting once and reading the important things properly.

It is not a compliance framework, and no supervisor has endorsed it. Where a regime requires human oversight of generated output, and some do, running a disciplined practice is evidence you can point at. In Europe, NIS2 and, for financial services, DORA both expect documented risk management and traceability across the software supply chain; SIEVE fits alongside them as good practice, not as a route to compliance. The distance between "we run a practice" and "we are compliant" is where the follow-up questions live.

It does not retroactively verify anything you have already shipped. It starts at the next artefact.

---

## The evidence

This document is written from one operation, not from a survey, and the figures are its own.

**Law 1.** A publication producing articles with machine correspondents and a single human desk, over roughly two weeks: 19 pieces written, 66 in the corpus, 24 of them never read by the desk. A third of everything published carries a warning saying nobody has checked it. The writing capacity was never the constraint, and treating it as one produced a liability rather than a library.

**The corollary.** The art pipeline rejected five consecutive images before anybody asked why. The diagnosis was twice wrong: the generator was assumed to be ignoring instructions. The actual cause was that the prompt led with the headline, so a piece whose headline ended "does not cover a coin" was handed a coin to draw. One change to the prompt took acceptance from roughly one in five to roughly one in one. An afternoon upstream was worth more than any amount of looking harder.

**Practice V.** A batch operation on fourteen brand assets damaged four of them, because the dry run that proved it safe was read through `head -32`, and the entries that would have warned were in the part not printed. That is the second warning of *Verify on one surface*, and it cost a revert.

**Law 3.** Ten dated re-checks are currently booked against observational pieces written weeks before they publish, two of which carry headlines that a single vendor's page edit would falsify on the morning they run. That is handled by a scheduled job rather than by intention.

---

## Glossary

| Term | Meaning |
|---|---|
| g | Time to generate one artefact |
| r | Time for a competent person to verify one artefact |
| R | Reviewing minutes actually available in a period |
| a | Acceptance rate: fraction of reviewed artefacts that survive review |
| Loop | One change, one context document, one diff, two pairs of eyes |
| Portfolio | Every artefact one person is answerable for |
| Debt register | The list, inside a deliverable, of what is not true yet, with owners and expiry dates |
| Surface | One view that shows the checked property for all n artefacts at once |

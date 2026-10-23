# Changelog

## 1.0.0 · 2026-10-23

- DAHNIN merged into SIEVE as the loop layer. The six loop rules (Document, Anchor, Hold, Narrow, Inspect, Name) and their security layers are now Part one of the framework; the five practices (Size, Instrument, Escalate, Verify, Expire) are Part two.
- New Part three maps what each loop rule produces to the portfolio practice that consumes it.
- Each of the three laws now states what it means inside a single loop.
- Standards mapping (OWASP LLM Top 10, SLSA, NIST SSDF, NIST AI RMF) carried over for the loop rules.
- Templates for the context document, debt register, review budget, artefact header and re-check schedule.
- `scripts/check_rechecks.py` and a GitHub Actions workflow that hold a publish when a verification has expired.

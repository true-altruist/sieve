#!/usr/bin/env python3
"""SIEVE re-check gate.

E · Expire every verification. The re-check must be able to hold an artefact
back and must not be able to push it out. This script only ever exits non-zero
to hold; it never publishes, edits or approves anything.

Usage:
    python scripts/check_rechecks.py [path/to/recheck-schedule.yml] [--today YYYY-MM-DD]
                                     [--warn-days N] [--artefact PATH]

Exit codes:
    0  nothing is due
    1  at least one re-check is due, overdue, changed, or scheduled after its use date
    2  the schedule itself is invalid (missing fields, bad dates, duplicate ids)
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys

try:
    import yaml  # PyYAML
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    sys.exit(2)

REQUIRED = ("id", "artefact", "claim", "source", "checked_on", "recheck_by", "owner", "status")
STATUSES = {"open", "confirmed", "changed", "withdrawn"}


def as_date(value, field, entry_id, errors):
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        errors.append(f"{entry_id}: {field} is not a YYYY-MM-DD date ({value!r})")
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Hold artefacts whose verifications have expired.")
    parser.add_argument("schedule", nargs="?", default="templates/recheck-schedule.yml")
    parser.add_argument("--today", help="override today's date (YYYY-MM-DD), for testing")
    parser.add_argument("--warn-days", type=int, default=3, help="warn this many days ahead (default 3)")
    parser.add_argument("--artefact", help="only check entries for this artefact")
    args = parser.parse_args()

    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    with open(args.schedule, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    entries = data.get("rechecks") or []

    errors: list[str] = []
    seen: set[str] = set()
    holds: list[str] = []
    warnings: list[str] = []
    checked = 0

    for i, entry in enumerate(entries, start=1):
        entry_id = str(entry.get("id", f"entry {i}"))
        missing = [f for f in REQUIRED if entry.get(f) in (None, "")]
        if missing:
            errors.append(f"{entry_id}: missing {', '.join(missing)}")
            continue
        if entry_id in seen:
            errors.append(f"{entry_id}: duplicate id")
        seen.add(entry_id)

        status = str(entry["status"]).lower()
        if status not in STATUSES:
            errors.append(f"{entry_id}: status must be one of {sorted(STATUSES)}")
            continue
        if args.artefact and entry["artefact"] != args.artefact:
            continue
        if status == "withdrawn":
            continue
        checked += 1

        checked_on = as_date(entry["checked_on"], "checked_on", entry_id, errors)
        recheck_by = as_date(entry["recheck_by"], "recheck_by", entry_id, errors)
        use_on = as_date(entry["use_on"], "use_on", entry_id, errors) if entry.get("use_on") else None
        if checked_on is None or recheck_by is None:
            continue

        label = f"{entry_id} [{entry['artefact']}] owner={entry['owner']}"

        if status == "changed":
            holds.append(f"HOLD   {label}: observation no longer true, fix the artefact")
            continue
        if use_on and recheck_by >= use_on:
            holds.append(f"HOLD   {label}: re-check {recheck_by} is not before use date {use_on}")
            continue
        if recheck_by <= today:
            days = (today - recheck_by).days
            when = "due today" if days == 0 else f"overdue by {days} day(s)"
            holds.append(f"HOLD   {label}: re-check {when}, last checked {checked_on}")
        elif (recheck_by - today).days <= args.warn_days:
            warnings.append(f"SOON   {label}: re-check by {recheck_by}")

    for line in errors:
        print(f"INVALID {line}")
    for line in holds:
        print(line)
    for line in warnings:
        print(line)

    if errors:
        return 2
    if holds:
        print(f"\n{len(holds)} of {checked} verification(s) need a re-check before use. Holding.")
        return 1
    print(f"{checked} verification(s) in date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

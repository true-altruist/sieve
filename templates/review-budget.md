# Review budget

> **S · Size the review budget before the work.** Measure, do not estimate. Commission against the result.

**Period:** week of YYYY-MM-DD
**Reviewer:**

## 1. What review actually costs (r)

Time the last five real reviews of each class. Use the median, not the best one.

| Artefact class | Review class (E) | r, minutes (measured) | Last five timings | a, acceptance rate |
|---|---|---|---|---|
| *Article* | One competent read | 35 | 30, 42, 35, 28, 40 | 0.8 |
| *Code change* | Full read + second eye | 25 | | |
| | | | | |

## 2. What the week actually has (R)

| | Minutes |
|---|---|
| Reviewing time blocked in the calendar | |
| Minus meetings that always eat into it | |
| **R** | |

## 3. The commission number

```
shipped per week = (R / r) × a
```

| Artefact class | R allocated | r | a | **Commission at most** |
|---|---|---|---|---|
| | | | | |

## 4. The rules for this week

- Nothing is started beyond the commission number. The extra is not a backlog, it is a liability.
- Nothing unreviewed is placed anywhere that implies it was reviewed.
- If a falls below *0.x*, stop and fix the generator before reviewing more.

## 5. End of week

| Artefact class | Commissioned | Reviewed | Accepted | Actual a | Actual r |
|---|---|---|---|---|---|
| | | | | | |

Carry the actual r and a into next week's budget.

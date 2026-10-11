# Full-rotation gap correction

Reviewed 2026-10-11. This is a narrow arithmetic/reporting correction after commit `4765dd5739088a6481b48a8cf1bb522ae02e6579`.

## Preserved failure

A separate evaluator generated and audited four new first drafts in one session. Its recheck accepted the compact field cards and inclusive participation design, but found an incorrect gap estimate in the twelve-player mixed-experience answer. That review was not blinded, a human field trial, or successful installed-host validation. All four outputs were inspected; only the relevant failure is reproduced here.

The [original prompt](gap-regression/original-prompt.md), [unchanged failed answer](gap-regression/original-v3.md), [reviewer trace](gap-regression/reviewer-trace.json), and [provenance](gap-regression/provenance.json) remain available. The answer claimed about 5–8 minutes between adjacent fielding visits and 21–24 minutes across batting. It did not specify enough timing/order detail to justify those ranges. The counterexample below exceeds both ranges without any added interruption. Earlier failed outputs remain intact too.

## Explicit model and correction

The [input model](gap-regression/v3-model.json) uses twelve synthetic labels, four children per group, and 35-second complete cycles. The three station blocks run 6–19, 22–35, and 38–51 minutes. Each visit starts with a one-minute demo, then nine consecutive working minutes; remaining collection/rest/margin/closure is reserved at the end. Groups A/C field in adjacent blocks; B fields in the first and third. Each group's second visit starts with child 2 instead of child 1. This is one permissible allocation, not a unique schedule or a worst-case bound over all allocations.

The optional [timeline helper](../skills/baseball-coach/scripts/trace_opportunities.py) derives every complete attempt and gap. It uses integer seconds, including the elapsed setup, full rotation, swaps and other activities between attempts. Its [complete output](gap-regression/v3-derived.json) supports this table. Times are elapsed **minutes:seconds**, not decimal minutes. Every gap is between consecutive modeled attempts at the target skill; it is not necessarily idle waiting.

| Child | Last start before gap | Next start | Start-to-start gap | End-to-start gap | Total attempts |
|---|---|---|---|---|---|
| A1 | 30:00 | 40:45 | 10:45 | 10:10 | 7 |
| A2 | 30:35 | 39:00 | 8:25 | 7:50 | 8 |
| A3 | 31:10 | 39:35 | 8:25 | 7:50 | 8 |
| A4 | 29:25 | 40:10 | 10:45 | 10:10 | 7 |
| B1 | 14:00 | 40:45 | 26:45 | 26:10 | 7 |
| B2 | 14:35 | 39:00 | 24:25 | 23:50 | 8 |
| B3 | 15:10 | 39:35 | 24:25 | 23:50 | 8 |
| B4 | 13:25 | 40:10 | 26:45 | 26:10 | 7 |
| C1 | 14:00 | 24:45 | 10:45 | 10:10 | 7 |
| C2 | 14:35 | 23:00 | 8:25 | 7:50 | 8 |
| C3 | 15:10 | 23:35 | 8:25 | 7:50 | 8 |
| C4 | 13:25 | 24:10 | 10:45 | 10:10 | 7 |

For this model, the corrected start-to-start ranges are **8:25–10:45 for A/C** and **24:25–26:45 for B**. Within a continuous visit, starts are 2:20 apart. The latter must not be substituted for full-session spacing. Fifteen whole cycles fit each working window; the leftover 15 seconds cannot count as another turn.

## Reporting when inputs are uncertain

The entrypoint, operations reference and template now require checked timestamps before publishing numerical gap ranges. Evidence must cover distinct assignments and the children at turn-order extremes. A different fallback needs its own calculation. No second visit means no cross-visit interval to report, rather than a zero-second interval.

If the exact windows or order are unknown, useful wording is: “Group B has an intervening batting block before returning to fielding, so its fielding opportunities are more widely separated. The exact gap depends on each child's last and next turn, demonstrations, collection and transitions; I haven't calculated a reliable numerical range. Fix those details before claiming one, and reconsider the rotation if it does not support today's goal.” This is an illustrative reporting pattern, not a new scenario-test result.

The helper is optional and uses Python's standard library. Manual checked timelines also work. It does not choose realistic durations, infer missing overhead, certify lane safety or staffing, set an allowable wait threshold, count successful performance, or guarantee actual opportunities. Other-skill activity and supervised movement remain distinct from target-skill attempts.

## Independent regression checks

The helper/guidance author and regression-test author worked separately. Seven standard-library test methods in [test_opportunity_trace.py](../scripts/test_opportunity_trace.py) cover:

- Exact twelve-child turn starts, attempts, and start/end gap ranges reproducing the reviewer counterexample.
- Paused working windows, continued turn order, unused partial cycles, and a declared child with zero attempts.
- A full cycle fitting exactly at a window end, shorter leftovers, and an empty activity model.
- A realistic one-lane fallback with one fielding visit per group: 3–4 attempts each and no cross-visit interval.
- Concurrent visits for different children, rejection of same-child overlapping visit bounds, and chronological output independent of input order.
- Invalid types, bounds, cycles, players, windows, duplicate visit IDs, and unknown/missing fields.
- CLI file/stdin parity, malformed JSON, duplicate JSON keys, and clear nonzero failures.

Run from the repository root:

```sh
python3 scripts/test_opportunity_trace.py
python3 skills/baseball-coach/scripts/trace_opportunities.py evaluation/gap-regression/v3-model.json
```

These checks passed against the corrected helper. The preserved derived output was also compared with a fresh calculation. The packaging and skill metadata checks are separate. This correction adds deterministic arithmetic evidence; it is not a new full set of model-generated coaching scenarios, a field validation, or proof that every future answer will follow the guidance.

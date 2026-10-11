# Returning to the next practice

Product review dated 2026-10-11. Baseline: `6955f50096b34bbaca1a60bc1fb4dfbe47660c46`.

## Why this change

The existing journey already supports a complete session: plan, field card, approved-assistant briefing, safe finish, and adult afterbrief. The afterbrief collects one success, difficulty, and adjustment, but the package had no editable handoff linking those observations to the next conversation. The README started with a detailed practice prompt, although the skill could already help a volunteer who did not know what information to bring.

The highest-value bounded opportunity identified here was **carrying a useful session forward without reconstructing its context**. This is a product hypothesis drawn from the artifacts and the realistic requests below, not a finding from parent interviews. Assistant handoffs and disruption responses already have dedicated forms and several evaluations. A season curriculum, persistent child profile, new planner, and extra drill library were deliberately left out.

Fresh baseline answers already handled the five tested requests well, including a reusable note when explicitly requested. That evidence narrowed the implementation: one [optional next-practice note](../skills/baseball-coach/assets/next-practice-note.md), routing from the existing afterbrief, and clearer first-use/return-use prompts in the README. It is a discoverability and reusable-artifact change, **not a demonstrated repair of deficient baseline behavior**.

The note separates observed results from untried plans, carries one concrete adjustment, distinguishes old setup from current facts, and leaves consequential unknowns visible. It omits private child information. It does not save itself, promise host memory, imply ongoing clearance, or impose a fixed progression. Other modes do not receive it by default.

## Evaluation method

Two separate fresh Astra contexts used the baseline and candidate skills with the same [raw requests](continuity/prompts.md). Each evaluator handled four independent cases in one session; a fifth cancelled-plan request was added to both afterwards. They were instructed not to transfer facts between cases. Neither received author conclusions, the product rubric, intended answers, or the other evaluator's outputs. The candidate evaluator could read the candidate template through skill routing; that is part of the tested resource, not a withheld reference.

Original answers are retained unchanged in the baseline/candidate folders. Only absolute local skill prefixes in self-reports are replaced for portable distribution. [Provenance and hashes](continuity/provenance.json) identify the snapshots and raw outputs. The root author reviewed behavior and arithmetic. This is agent-generated scenario evidence with small, related cases, not a blinded human trial, statistical comparison, actual host-installation test, or proof of repeatability.

## Before and after

| Request | Baseline | Candidate and interpretation |
|---|---|---|
| New 6U volunteer with little information | [259-word answer](continuity/baseline/01-first-conversation.md): three compact question groups, provisional shape, no invented coverage. | [231-word answer](continuity/candidate/01-first-conversation.md): same useful boundary; no new note or large questionnaire. The README now exposes this already-working entry point. |
| Return with observations and request a reusable note | [40-minute plan](continuity/baseline/02-next-practice.md): uses two simple rolling lanes, retains Statues, supplies a 150-word note. | [40-minute plan](continuity/candidate/02-next-practice.md): retains the same fundamentals/roles and produces a 186-word note separating older observations, unknown new results, untried plans, and current changes. Both versions already succeed; added explicitness costs words. |
| More children, absent assistant, uncertain permission, private detail in old note | [Conditional revision](continuity/baseline/03-changed-staffing.md): no solo clearance; replacement-adult plan and clean note. | [Conditional revision](continuity/candidate/03-changed-staffing.md): same coverage boundary and omission of private child details; old gear/space are explicit assumptions. Full answers are 923 versus 952 words. Both provide substantial conditional detail; this test does not show a reduction in burden. See the wording issue below. |
| Three-sentence parent reminder only | [23-word reminder](continuity/baseline/04-small-request.md): exactly three sentences. | [21-word reminder](continuity/candidate/04-small-request.md): exactly three sentences, no note, drills or questions. The optional route did not appear in this control. |
| Cancelled practice; request only a note | [104-word note](continuity/baseline/05-unplayed-plan.md): no invented observations, revised duration and pending checks. | [150-word note](continuity/candidate/05-unplayed-plan.md): all activities explicitly untried, shortening is a tentative idea, current adult confirmation preserved. No full plan. Again, greater explicitness is not demonstrated time savings. |

The candidate's changed-staffing answer contains the ambiguous phrase “After every handoff” before the adult review. The existing skill explicitly requires **all** handoffs first, and the answer elsewhere keeps supervision until every child is collected, but the wording is still poor. Its [targeted follow-up](continuity/candidate/06-late-pickup-follow-up.md) explicitly corrects the phrase and keeps both adults supervising the two remaining children, with no review or teardown yet. The original answer is retained. This is a disclosure of output fallibility, not a reason to present the raw test plan as a polished new example or to accumulate another copy of the same existing source rule.

[Comparative checks](continuity/checks.json) record whitespace word counts, exact 40-minute clocks, both conditional 45-minute clocks, and three-sentence controls. Both versions keep preparation separate, approved adults assigned, easier options and a simultaneous inclusive final game. The candidate evaluator reported reading the new asset. No precise full-session gap ranges were asserted; opportunity counts depend on the stated modeled cycles and actual turn allocation, not observed pace.

The demonstrated product result is one discoverable editable artifact plus routed instructions and runnable first/return prompts. These cases support that the new route can be used while small requests stay small. They do **not** establish improved correctness, faster preparation, more effective coaching, or reliable behavior in every future response. The cancelled case is a meaningful check of the plan-versus-observation distinction, not evidence of better learning.

## Decisions and next questions

- Keep the note optional and editable. It is useful for a coach who asks to carry work forward, not mandatory paperwork for every request.
- Reuse known facts and reported current arrangements. A changed staff/count/site can invalidate an old plan; a previous approval is not automatic permission for a new setup. Avoid asking the user to restate facts already supplied.
- One success at a task is an observation, not proof of learning or readiness for a new demand. A cancelled plan supplies no observations.
- A simpler first-use prompt exposes existing behavior; it does not establish that the candidate saves preparation time.
- Keep prior practice cards, other modes, technical/teaching resources, and timeline logic unchanged. The new route should not increase their output burden.

Next-question backlog, rather than promised features:

1. Can a real volunteer fill and reuse the note comfortably, and which fields do they actually omit? Test that before adding more structure or claiming time saved.
2. Does an approved assistant understand the resulting assignment at the field without a long explanation? Existing cards need human use evidence, not another form first.
3. Do coaches want one next session or a small week view, and what real recurring decisions would the latter solve? No week-planning system is added here.
4. Which intended host can load the skill reliably through its supported discovery path? Prior no-spend probes did not establish installation; no paid host call is authorized for this iteration.
5. Owner decisions remain: license, commercial terms, experienced-coach review, and a source-maintenance process before broader distribution or marketplace submission.

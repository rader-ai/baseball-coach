# Field-use review and follow-up

Reviewed 2026-10-11. This is a written planning review, not a field trial or measured reading-time study.

## What prompted this revision

A separate assistant task reviewed source commit `b725ffd92fc76c5e853bdecbf532ddddc7726ee4`, generated six original scenarios, and audited its own answers in the same session. It did not read this repository's prior evaluation answers. This was independent of the author task, but not blinded generation/audit or human field testing. It reported no demonstrated critical defect and two moderate practical weaknesses. The three relevant original answers are preserved byte-for-byte, with [prompts](field-use/baseline/prompts.md) and [hashes/provenance](field-use/baseline/provenance.json).

- [First-time parent](field-use/baseline/01-first-time-parent.md): 1,348 words in the complete answer, without a distinct short field card.
- [Live disruption](field-use/baseline/02-live-disruption.md): 1,228 words, including useful safety actions but substantial reading during a live problem.
- [Mixed experience](field-use/baseline/03-mixed-experience.md): six players sharing a 30–40-second fielding cycle meant 3–4 minutes between the same child's turn starts and about 4–5 planned attempts across two work blocks. The final game's 4½-minute turn window had no margin at nine × 30 seconds, and nine × 40 seconds would require six minutes. The answer allowed stopping before everyone participated, so its total clock was not secretly extended; the participation shortfall was foreseeable.

The reviewer found the parent, older-youth technical/rule, and ceremony answers strong. Those underlying content resources were preserved. Its source spot-checks supported scoped Little League and Pitch Smart provisions and the cautious feedback-research interpretation. Two PMC articles returned CAPTCHA pages and were not fully rechecked; those remain access gaps, not verified findings. No bypass was attempted.

## Changes made

The skill now leads with a compact coach card and separate helper/preparation notes, with a still shorter format for live interruptions. Safety conditions needed during play remain on the field card. Word ranges are design targets, not permission to omit essential information. The operations reference requires an opportunity decision after full-cycle, overhead and waiting-time estimates. Poor opportunities require a changed route, verified independent adult-led lanes, revised blocks, or an explicitly narrower goal. More adults or two activity areas alone do not establish that another lane fits. Watching and ball-free movement are not counted as ball attempts.

The practice examples now demonstrate those choices: shorter return routes, an additional fielding block where staffing and geometry permit, and simultaneous ball-free finales. Their lead cards are 410, 457 and 460 words for the 32-, 45- and 60-minute plans respectively. Their complete documents retain preparation detail. They do not claim a rendered page count or an ideal rep minimum.

## Fresh scenarios

Two fresh Astra contexts received a frozen revised skill and [three new requests](field-use/fresh/prompts.md), without baseline answers, author answers or review criteria. Their first complete outputs are preserved unchanged. See [A self-report](field-use/fresh/self-report-a.md) and [B self-report](field-use/fresh/self-report-b.md). The coordinating reviewer checked the answers separately; this is still synthetic agent evaluation, not field use or a controlled before/after experiment.

| Output | Length and clock | Review |
| --- | --- | --- |
| [First practice](field-use/fresh/01-first-practice.md) | 513-word lead card; 173-word assistant card; 1,143 words overall. Continuous 0–38 clock. | Usable short lead layer, two modest goals, assigned groups, gear secured when unused, exact conditional sequential fallback. Nine usable minutes ÷ 25-second cycle ÷ four children allows about five rolling attempts each; 100 seconds is the repeat interval during that visit. Running allows about four or five routes each. Simultaneous finale. |
| [Live staffing loss](field-use/fresh/02-live-disruption.md) | 311 words total; continuous 21–48 clock, 27 minutes remaining. | Slightly above the suggested 300-word target, retained as generated. One visible group under supplied solo permission. Batting is conditional on visibility, safe sector and required protection. Four × 90-second turns + two minutes demo/closure fits eight minutes. Nine × 35-second rolls uses 5¼ minutes of seven, leaving 1¾ minutes for demo/margin. Simultaneous finale. |
| [Mixed experience](field-use/fresh/03-mixed-experience.md) | 561-word lead card; helper cards 162/176/168 words; 1,693 words overall. Continuous 0–50 clock and five nested rounds spanning 8–43. | Main layout conditionally uses two inspected adult-led field lanes and small hitting pairs, estimating 8–11 fielding attempts each. The one-lane fallback honestly offers only 4–5 ball attempts and distinguishes movement from ball attempts. **Remaining defect:** it applies the roughly 100-second within-lane interval to the fallback without counting gaps between visits, alternating movement, round changes and hitting. The original is retained as a failed cadence claim, not a fully passing answer. |

The main mixed plan budgets 280 usable seconds ÷ 25 ÷ four children ≈ 2–3 attempts per field visit, across four visits. Its fallback budgets 125 ÷ 25 = five turns shared by four children per visit. Most therefore get one turn in that visit, making an overall repeating 100-second cadence impossible. This finding prompted a further instruction change: trace each different assignment through the actual rotation; distinguish in-visit intervals, idle wait, other activities and gaps between visits; audit each fallback separately. The examples' multi-visit notes were clarified too. No raw answer was rewritten to hide the defect.

Word counts split on whitespace and include headings/table syntax. Card counts stop before the following separate section; they are not rendered page counts. Whole-output lengths are shown so a compact first layer is not mistaken for a short complete document.

## Targeted cadence follow-up

A third fresh Astra context received only the final clarified skill and [a new single-lane request](field-use/follow-up/prompt.md), without examples, earlier outputs or the review criteria. Its [first complete answer](field-use/follow-up/04-one-lane-participation.md) and [self-report](field-use/follow-up/self-report.md) remain unchanged. The 42-minute clock is continuous. The lead card is **578 words** and the complete answer 1,330; the card is denser than the roughly 350–550-word target. This is a remaining output-length limitation, not a hidden pass against a hard cap.

The answer plans six five-minute visits with three children per group. For fielding, 300 − 30 demo − 60 margin = 210 seconds, enough for six 35-second cycles: two opportunities per child per visit, four across two visits. For tee work, 300 − 30 demo − 45 margin = 225 seconds, enough for three 75-second two-swing turns: four swings per child across two visits. Catches, completed sends and contacts are not guaranteed or conflated. Fallbacks reduce counts openly; no second fielding lane is invented.

An independent calculation traced all three positions in groups A/B/C using the answer's stated cycle model and the self-report's illustrative swing timestamps. It reproduced **1:45 within-field-visit intervals, 16:15–17:15 fielding inter-visit gaps, and 17:40–18:40 tee inter-visit gaps**. The largest modeled gap between either type of ball attempt is 12:50 for A/B and 11:50 for C. Other-skill work, ball-free movement and idle waiting are distinguished. Extra pauses can extend gaps, so these are neither observations nor maximum waits. The full-rotation reporting defect is addressed in this targeted case; four tries remain modest, not a high-repetition practice.

## Reproducible checks and limits

[Checks and snapshot hashes](field-use/checks.json) contain original-output hashes, whitespace word counts, continuous clock spans, all-child participation calculations and both skill snapshots. The three initial follow-up outputs use the first revised snapshot; the targeted answer uses the final clarification. They are four new answers, not four independent replications of the final snapshot. Together with 21 earlier answers and the three preserved external baseline answers, the repository retains 28 coaching outputs across revisions. A failure is kept visibly as evidence.

The supplied examples' inter-visit ranges were also recomputed from their explicit windows and same-order assumptions: 6:00–7:40 or 17:00–18:40 for the 45-minute plan; 7:30–10:00 or 22:30–25:00 for the 60-minute plan. Their shorter in-visit cadences are labelled separately. Core metadata, portable links, the four supplied clocks, packaging boundaries and the extracted archive are validated separately from coaching usefulness.

No children, real rosters, live teams or communications were involved. No human coach trial, print-layout/read-time test, successful host skill invocation, calibrated performance measurement or broad reliability claim is supported. The short lead layers improve the artifact structure in these cases; they do not prove coaches will find every generated plan usable. [Host probes](HOST-VALIDATION.md) remain inconclusive. License/commercial terms, qualified field review, source maintenance and target-marketplace submission remain owner decisions.

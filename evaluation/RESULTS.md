# Local review evidence

Edition: 0.1.0 local review candidate. Reviewed 2026-10-11.

The specified GitHub repository was obtained as a fresh shallow checkout after the initial location checkpoint. Git reported an empty repository: branch `main`, no HEAD commit, no tracked files, no original license, and no repository-specific guidance. No original team files or uncommitted work existed in that checkout. Unrelated local projects were left untouched.

## Structural and content review

- The available skill-creator `quick_validate.py` passed. Codex UI metadata parsed as YAML; its short-description length and explicit `$baseball-coach` prompt were checked.
- The canonical skill contains 25 text files: a 69-line entrypoint, UI metadata, nine references, six editable assets, seven examples, and one optional standard-library timeline helper. Portable relative links are checked by the package validator.
- Four sample schedules have continuous, nonoverlapping elapsed-time rows and correct totals: 32, 45, 60, and 15 minutes. This is arithmetic evidence, not a guarantee that a real group will move at that pace.
- Templates were manually reviewed for editable logistics, adult assignments, local-rule uncertainty, and actionable outputs. Intentional bracket fields are fill-in prompts, not unfinished implementation scaffolding.
- New distributable text was reviewed for fictional labels/placeholders, private data, unsupported affiliation, claims of guaranteed improvement, and copied curricula. No real roster, child contact, photo, credential, or private league record is included. Automated marker checks are narrow and do not guarantee anonymity.
- The root manifest matches the current documented minimal Agent Plugins layout. This does not establish successful host installation or directory review.
- Packaging boundary tests passed: unlisted synthetic private-data canary excluded; traversal/hidden/aliased paths rejected; symlinks rejected; duplicate/missing entries rejected; deterministic archive bytes and refusal to overwrite an existing archive verified.

## Independent Astra forward tests

An independent Astra agent received the skill and six realistic requests, without the author's answers or the review rubric. It produced complete answers in an isolated temporary folder. It read the core references first and subsequently inspected relevant completed templates/examples. No live team, communication, installation, or production action was used. See [scenario criteria](SCENARIOS.md) and [tester self-report](outputs/07-self-report.md).

| Case | Actual output and review result |
| --- | --- |
| One adult, eight five-year-olds | [35-minute plan](outputs/01-one-coach-five-year-olds.md). PASS: one visible group; bat/tee stored because protective gear was unconfirmed; no independent station; concrete conditional guardian restroom handoff. |
| Hot forecast, missing local policy | [25-minute plan](outputs/02-hot-weather-25-minutes.md). PASS: usable conditional plan with rest/water; requests local conditions and policy; does not clear practice from duration alone. |
| Parent's position complaint | [Reply and action plan](outputs/03-parent-concern-and-next-game.md). PASS: acknowledges concern, reviews actual participation, proposes preparation/early opportunity/tracking/follow-up, protects other children's information, sends nothing. |
| Unknown previous-day pitching count | [Eligibility response](outputs/04-unknown-pitch-history.md). PASS: no clearance or guessed positive allowance; operational no-pitch decision explicitly distinguished from universal rules; seeks verified cross-team history. |
| Inclusive ceremony | [15-minute ceremony](outputs/05-fifteen-minute-awards.md). PASS: quiet recognition has reserved time and explicit supervision; no attendance shaming, purchase, or invented achievement. |
| Head impact and dizziness | [Response](outputs/06-head-bump-dizziness.md). PASS: no same-day return; guardian/provider steps and emergency escalation; no coach-administered diagnosis/clearance. |

The first tests prompted narrow clarity improvements: listed equipment need not all be used; solo-group permission does not establish restroom coverage; position concerns need controllable commitments; quiet recognition needs reserved time; supervision continues beyond the planned clock when pickup is incomplete. These strengthened instructions that the first outputs already handled. Targeted [practice](retest/01-one-coach-five-year-olds.md) and [ceremony](retest/05-fifteen-minute-awards.md) retests passed with these clarifications.

## Final coaching-philosophy requirement

A later user direction made simplicity, fundamentals, supportive feedback, and a fun final game central. The entrypoint, practice reference/template/checklist, all three sample practices, and parent welcome example now carry that approach. An AAP developmental-readiness source was added to the source register. The skill explicitly avoids clinical credentials, behavioral diagnosis, or claims of proved expertise at every level. Routine shortening preserves a brief game; safety stops and cancellation override completing it.

The independent tester read the final instructions and produced two new complete outputs:

- [35-minute one-coach practice](final/01-one-coach-five-year-olds.md): PASS. Final active block is Baseball Statues, with rules, one cue, an easier seated option, controlled equipment, and whole-group supervision. Required restroom coverage remains explicit.
- [25-minute heat plan](final/02-hot-weather-25-minutes.md): PASS. Final permitted activity is a low-effort shaded Baseball Mirror game. Local conditions/policy are still required; the game cannot override a safety stop. Water/rest, adult roles, and exact timing are preserved.

Both final plans use brief demonstrations, specific supportive feedback, and fundamentals before added challenge. The initial outputs are retained as historical evidence; these final outputs and the skill examples reflect the latest requirement. Six initial cases and four targeted outputs were reviewed in total. These runs do not establish broader reliability across all prompts, models, or age groups.

## Optional wisdom and original analogies

The optional [wisdom reference](../skills/baseball-coach/references/coaching-wisdom.md) adds eight selective influences: fictional Ted Lasso, Mr. Miyagi, and Gordon Bombay; documented coaching philosophy from John Wooden, Pat Summitt, Dawn Staley, Steve Kerr, and Pete Carroll. Each has a source category, a concrete adult action, original wording, and an adaptation limit. All eight linked primary/official sources were opened on 2026-10-11. Story summaries, first-person reflections, official legacy accounts, and developmental guidance are labelled separately; none establishes that elite results transfer to children.

The core routes to this reference only when requested or useful for a specific moment, using one influence and one action by default. Original analogies add warmth, followed by a literal cue or demonstration. The coach checks understanding and drops an image that confuses. Safety instructions stay literal; the fun finish remains part of the practice design. The [three worked situations](../skills/baseball-coach/examples/coaching-wisdom-in-action.md) show a mistake, a hesitant newcomer, and competing adult instructions. At the wisdom checkpoint, the practice examples and separately saved five-year-old sample were unchanged; the later practice-depth revision below updates them.

A fresh Astra context received the finished skill and five requests, without the author's answers, existing examples, or reviewer criteria. Its outputs were reviewed against [the scenario criteria](WISDOM-SCENARIOS.md); see its [self-report](wisdom/selfreport.md) for material read and limitations. These are five additional written outputs, making 15 scenario outputs across this review. They do not establish performance in every host or prove that references load selectively in every conversation.

| Case | Actual output and review result |
| --- | --- |
| Mistake, analogy confusion, punishment suggestion | [Reset and response](wisdom/01-mistake.md). PASS: one fictional influence, original image, manageable retry, concrete feedback; confusion leads to literal instruction rather than more metaphors; no punishment laps. |
| Worried newcomer | [Three-minute welcome](wisdom/02-newcomer.md). PASS: one first-person coaching source; choice to watch or try, visible supervision, a short image followed by a literal action, and no forced disclosure or promised confidence improvement. |
| Blame and elite pressure | [Conflict repair](wisdom/03-conflict.md). PASS: respect/listening is a labelled adaptation; short turns, practical retry and supervision; keeps the inclusive fun game when safe, without forced apologies or public comparison. |
| Routine practice | [20-minute plan](wisdom/04-routine-practice.md). PASS: exact continuous clock, two adults with three children each, one controlled live ball per group, safe retrieval, one cue at a time, inclusive final game and handoff. No celebrity layer is added. |
| Immediate lane hazard | [Safety response](wisdom/05-immediate-safety.md). PASS: literal stop first, controlled balls, repaired crossing route and rehearsal; optional brief humor comes only after the area is safe. |

The wisdom checkpoint passed package checks for 46 allowlisted text files, 54 local links, four supplied sample clocks, and its 62-line entrypoint. The additional 20-minute practice and three-minute welcome were reviewed and their continuous timing checked programmatically. Packaging boundary tests and skill/UI metadata validation passed again; the final archive was also extracted to a separate location and checked there.

## Practice depth and assistant enablement

The later research cycle adds [practice operations](../skills/baseball-coach/references/practice-operations.md), a reusable [assistant card](../skills/baseball-coach/assets/assistant-card.md), [teaching and support](../skills/baseball-coach/references/teaching-and-support.md), and [13 technical progressions](../skills/baseball-coach/references/technical-progressions.md). The three sample practices now budget adult preparation, player instruction/retrieval/transitions, late arrivals, optional recap/cheer, pickup, teardown, and adult review. Their 32/45/60-minute player clocks remain unchanged. The README is a practical front door with a filled card and realistic time allowances.

The references distinguish developmental guidance, research syntheses, current scoped rules, and original coaching choices. They avoid universal feedback formulas, fixed ability labels, age-based performance targets, inferred diagnoses, and prescribing angles from images. Equipment scaling can mean a larger interception target or a more manageable grip. Immediate task performance is distinguished from later retention. Pitch limits are not workout targets; total throwing load is not converted into invented official pitch counts. Historical sources and inaccessible material are identified rather than presented as current reviewed authority. This was a focused primary-source review, not a systematic review of all coaching research.

Two fresh Astra contexts received only the skill and six realistic requests. They did not receive this rubric, author answers, prior evaluations, or completed examples. See [review criteria](DEPTH-SCENARIOS.md) and the [first](depth/self-report-a.md) and [second](depth/self-report-b.md) self-reports. Both read the technical and teaching references as whole files for their related tasks; this does not prove section-level loading efficiency in every host. Generated answers are preserved unchanged. Only temporary directory prefixes in the self-reports were removed for portability.

| Case | Actual output and review result |
| --- | --- |
| Late approved assistant | [45-minute plan and card](depth/01-late-assistant.md). PASS: accepts supplied solo permission/care arrangement, keeps one group, budgets a stopped four-minute briefing, gives every adult a role, includes safe intake and exact shorter alternatives. |
| One safe sector and an uncle without clearance | [50-minute sequential plan](depth/02-one-safe-sector.md). PASS: does not count the uncle as staff or open unsupported parallel stations; one live sector, explicit waiting supervision, batting controls, retrieval, water, transitions, final game and post-pickup work. Turn counts are estimates, not promises. |
| Misses, turning away, and an adult label | [Support and correction](depth/03-supportive-correction.md). PASS: checks understanding/feed/comfort/gear/task before mechanics, offers a tee and one cue, observes a willing retry, avoids labels and identifiable uploads, distinguishes immediate performance from retention. |
| Older beginners and too many goals | [75-minute plan and three cards](depth/04-older-beginner.md). PASS: chooses two goals, uses only one batting setup, assigns all children/adults, budgets helmet/retrieval overhead and care interruptions, and supplies a 45-minute version plus an early-stop sequence. Age does not establish readiness. |
| Unknown pitching history and universal feedback claim | [30-minute response and plan](depth/05-pitching-evidence.md). PASS: no pitching clearance or velocity promise; gives a ball-free alternative, distinguishes ordinary catch from eligibility, verifies rule scope, and accurately limits the child-feedback research. Its cited numerical rule examples are scoped and require rechecking; they are not a stored eligibility decision. |
| Feeder exposure, first-base rule, and blurred still | [Technical boundaries](depth/06-technical-boundaries.md). PASS: changes the unscreened hardball feed, treats first-base facts/rule scope as unresolved, and invents no image observations or injury-preventing angle. The cited 2026 professional rule is explicitly an example, not an unidentified youth league's ruling. |

The second evaluator found that accessible Little League Runner FAQ text did not itself settle the first-base example. The reference's source note was narrowed to describe it as a starting point for rule questions; the evaluator independently used the current professional rule with explicit scope. No test answer was rewritten to conceal a failure.

These six additional outputs bring the review history to **21 written scenario outputs across successive revisions**, not 21 fresh runs of the final snapshot. The four new main practice clocks (45, 50, 75, 30) and three prose fallback clocks (40, 40, 45) were independently checked for continuity and exact totals. The reviewer inspected staffing, gear, waiting places, correction cards, safeguards, and source limits in all six outputs. This establishes written-plan behavior for these cases, not field capacity or empirical learning effects.

At the practice-depth checkpoint, validation covered 59 allowlisted text files, portable local links, the four supplied sample clocks, the 63-line entrypoint, UI metadata, and four packaging-boundary tests. The release archive is extracted and checked separately before delivery. Repository source uses an explicit staged inventory; archives, local helper state, and private working notes stay out of Git.

## Field cards and realistic participation

A later independent practical review of committed source found two moderate weaknesses: long unseparated answers for a first-time parent/live disruption, and too few fielding opportunities in a mixed-experience plan despite available adults. Its six answers were generated and audited by the same separate assistant task; this was not blinded or human field testing. Three original baseline answers are preserved with the follow-up evidence.

The revision puts a short usable field card first, separates assistant/preparation notes, and makes participation adequacy a design decision. It requires conservative full-cycle estimates, actual lane/coverage checks, and a fully budgeted final game. The three worked practice cards are 410/457/460 words including headings, with preparation detail below. Fourteen existing parent, game, ceremony, wisdom, teaching, technical and safety resources remain byte-identical to the committed baseline.

Fresh generation, its retained cadence failure, the narrow correction and targeted follow-up are documented in [field-use review](FIELD-USE-REVIEW.md). The report provides original answers, prompts, word counts, timing and participation math, plus snapshot hashes. It distinguishes within-visit turn intervals from gaps across the complete rotation. These are planning estimates rather than observed field rates; a short lead card is not a verified single printed page.

## Limits and release decisions

The subsequent [full-rotation gap regression](GAP-REGRESSION.md) preserves a separate reviewer's original failed answer and an explicit counterexample. The correction requires checked child timestamps for numeric ranges, or qualitative uncertainty when windows/order are unknown. Seven independent deterministic test methods cover the helper, the twelve-player counterexample, and a one-lane fallback. This adds arithmetic evidence rather than another full scenario-generation cycle; historical passes above do not imply that every earlier timing statement was correct.

These are agent scenario tests and a local content review. No field trial, coach credential review, child participation study, calibrated measurement, or medical/legal review was performed. Temporary isolated host probes did not establish skill loading; see [host verification limits](HOST-VALIDATION.md). No global installation or live host-model inference was performed. Current rules and local conditions remain the adult's verification responsibility; the linked safety sources are not an eligibility engine.

The archive is suitable for review. An owner-selected license, target-host installation tests, experienced-coach review, source maintenance decisions, and applicable publisher/submission steps remain release gates. Commercial terms and any paid distribution remain undecided. The owner authorized publishing the reviewed repository source to its existing GitHub remote; that does not grant an open-source license or approve marketplace submission. No PR, global install, marketplace enrollment, separate website publication, or outreach was performed. Git history and the delivery report record the commit/push outcome.

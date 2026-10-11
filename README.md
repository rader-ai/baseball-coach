# Baseball Coach

**A practical helping hand for the parent who said, “Sure, I'll coach.”**

Bring the players, adults, time, space, and equipment you actually have. Baseball Coach helps turn them into a practice you can run, instructions an approved assistant can follow, and messages families can understand.

Start with tee-ball and coach-pitch, usually around ages 5–8. Adapt upward by readiness and experience, with a fresh plan and current division rules for older groups. Beginners need somewhere comfortable to start, not a performance standard based on age.

**First try:** open this repository folder in an agent that can read local files and paste the first prompt under “Try it locally.” Start with what you know, even if that is only “I volunteered to coach tee-ball.” The skill asks about missing details that affect safety or feasibility and can draft with stated assumptions for the rest.

## Simple basics. Supportive coaching. A fun finish.

Show one action, give one clear cue, watch an attempt, and adjust the task. Notice real effort or teamwork. Every planned practice finishes active play with a simple fun game, followed by a short recap, optional cheer or wave, and supervised pickup. Safety can stop the session at any point.

There is room for character, too: “Give them one stepping stone, not the whole river” can remind an adult to simplify. Then comes the literal demonstration. The optional [coaching-wisdom guide](skills/baseball-coach/references/coaching-wisdom.md) offers original analogies and selected coaching lessons; [three examples](skills/baseball-coach/examples/coaching-wisdom-in-action.md) show how to use them without imitating a celebrity.

## Give your assistant something they can use

Here's a small, filled example for an approved assistant supervising a rolling activity:

> **Purpose:** Help children get ready for a slow rolling ball.  
> **Places:** Adult faces one ready child in a clear lane. Other children wait outside the lane, in the adult's view. One soft ball is active.  
> **Watch:** Is the child facing the lane before the roll? Do they move behind it?  
> **Cue and why:** “Get your body behind it” gives a simple place to move toward.  
> **Show, retry, check:** Demonstrate a slow straight roll. If it passes to the side, try closer and slower; watch whether the child moves behind the next one. Notice that action when it happens.  
> **Stop:** Secure the ball before collection or group movement. Stop for pain, distress, wandering, or lost supervision; ask the head coach without leaving the group.

Use the editable [assistant card](skills/baseball-coach/assets/assistant-card.md), [practice operations](skills/baseball-coach/references/practice-operations.md), [teaching and support](skills/baseball-coach/references/teaching-and-support.md), and [technical progressions](skills/baseball-coach/references/technical-progressions.md) when more detail helps.

## Start with a real plan

The [45-minute tee-ball practice](skills/baseball-coach/examples/45-minute-tee-ball-practice.md) leads with a compact field card covering demonstrations, retrieval, transitions, water, and its final game. Preparation notes check actual chances per child, not just the clock. Separately, it allows 15 adult minutes beforehand and five adult minutes for teardown/review **after all pickups**. Pickup time varies; preparation and cleanup allowances may need increasing. “45 minutes” does not mean 45 minutes of drills.

Other ready-to-edit starting points:

- [Abbreviated 32-minute, one-adult practice](skills/baseball-coach/examples/five-year-old-tee-ball-practice.md), conditional on permitted supervision and care coverage; [60-minute coach-pitch practice](skills/baseball-coach/examples/60-minute-coach-pitch-practice.md); [first-practice checklist](skills/baseball-coach/assets/first-practice-checklist.md).
- [Parent welcome email and FAQ](skills/baseball-coach/examples/parent-welcome-email.md), [game-day card](skills/baseball-coach/examples/coach-pitch-game-card.md), and [inclusive end-season awards](skills/baseball-coach/examples/end-season-awards.md).

## Try it locally

Ask a compatible agent to read [the skill](skills/baseball-coach/SKILL.md), then try:

> Use the Baseball Coach skill at `skills/baseball-coach/SKILL.md`. I volunteered to coach tee-ball and don't have all the details yet. Help me get started.

When you know the setup, ask for a complete plan:

> Use the Baseball Coach skill at `skills/baseball-coach/SKILL.md`. Plan 45 minutes for eight beginners and two approved adults, with one tee, suitable protective equipment, and limited field space. Give me a short field card first, then preparation notes and detachable assistant cards. Check whether each child gets enough chances for the goal.

> Help my assistant support a nervous newcomer. Give us one demonstration, one cue, and an easier choice without pressuring the child.

> Draft a parent welcome and FAQ with placeholders, then an optional 15-minute end-season ceremony where children can choose quiet recognition.

For a return visit, the optional [next-practice note](skills/baseball-coach/assets/next-practice-note.md) gives you one editable place for the last setup, what actually happened, and one adjustment to try. After pickup and the adult afterbrief, copy it, add upcoming changes or unknowns, and keep it wherever you choose. Paste it into a new chat when you want help with the next session; no remembered conversation or automatic file saving is assumed.

> Use the Baseball Coach skill at `skills/baseball-coach/SKILL.md`. Here is my next-practice note: [paste the filled note]. Help me plan our next session using the updates in it. Ask only about unknowns that change safety or feasibility.

The skill needs no packages, credentials, roster, or account connection. Current rules and weather require authoritative sources or material the adult provides.

When a plan includes numerical gaps between a child's attempts, check an explicit timeline first. An optional standard-library Python [calculator and instructions](skills/baseball-coach/references/practice-operations.md#optional-explicit-timeline-calculation) can trace supplied working windows and turn order; a checked manual timeline also works. If those details are unknown, use qualitative wording. The calculator verifies arithmetic, not safety or whether a plan gives enough practice.

For optional project discovery, manually copy the **whole** `skills/baseball-coach` folder to `.agents/skills/baseball-coach` for Codex or `.claude/skills/baseball-coach` for Claude Code, without overwriting an existing skill. These are project-folder conventions, not verified installations of this candidate. See [Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills). Where discovered, invoke `$baseball-coach` in Codex or `/baseball-coach` in Claude Code.

## Review, package, and share thoughtfully

This is a local review candidate. Structural checks and independent scenario outputs are recorded in [evaluation evidence](evaluation/RESULTS.md); they do not establish installation or compatibility across hosts. Read the [distribution plan](DISTRIBUTION.md) and minimal [plugin manifest](plugin.json).

From the repository root, using Python 3:

```sh
python3 scripts/check_package.py
python3 scripts/test_package.py
python3 scripts/test_opportunity_trace.py
python3 scripts/check_package.py --archive dist/baseball-coach-0.1.0-review.zip
```

Only [explicitly listed files](release-files.txt) enter the archive. Existing ZIPs are never overwritten: choose a fresh filename. Packaging tools are not runtime requirements.

Keep children's private information in approved family/league systems. Drafting a message does not send it. [Sources and safety guidance](skills/baseball-coach/references/rules-safety-sources.md) distinguish local rules, developmental guidance, documented philosophy, and fictional inspiration; none promises improvement or replaces qualified care. No organizational endorsement is implied.

No license has been selected; the owner must decide reuse and commercial terms before offering a licensed release. Availability of this repository does not grant an open-source license. This is a review candidate, with no marketplace approval or verified global installation.

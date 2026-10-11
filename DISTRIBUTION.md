# Distribution and discovery

Reviewed 2026-10-11. This is a review candidate, not an approved listing, legal opinion, or revenue plan. Repository source publication does not resolve its unchosen license or authorize a marketplace submission.

## Package choices

The canonical skill lives at `skills/baseball-coach`. Its Markdown, references, and templates travel together. A minimal root `plugin.json` uses the published Agent Plugins schema and discovers the root `skills/` directory. It declares no tools, hooks, accounts, analytics, or network service. The wrapper has not been installed or tested in a marketplace client. [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins)

The [Agent Skills specification](https://agentskills.io/specification) provides the portable skill format. Host discovery and plugin submission are separate from content portability. A future Claude plugin wrapper needs its own verified manifest and host test; none is included here.

## How coaches could find it

Most parent volunteers start with a practical question. After approval to publish, offer a few original public resources that answer those questions immediately:

| Search need / resource title | Useful page content | Optional next step |
| --- | --- | --- |
| Tee-ball practice plan for 5-year-olds | Timed low-equipment plan, simple cues, one-coach supervision and stop conditions | Customize for attendance, adults, and space |
| 60-minute coach-pitch practice plan | Station assignments, transitions, easy/harder variations | Adapt to the actual division and equipment |
| First baseball practice checklist | Before-arrival setup, volunteer roles, family expectations | Draft a team-specific preparation card |
| Youth baseball parent welcome email | Editable welcome note and clear FAQ | Personalize tone and logistics privately |
| Inclusive end-of-season baseball awards | Short ceremony and specific, non-ranking recognition | Create optional recognition notes |

These query ideas are hypotheses, not keyword-volume research. Make each resource readable without an account and printable from ordinary Markdown or a later accessible page. Give it a descriptive title, clear heading, short introduction, a useful complete example, a last-reviewed date, and links to relevant official rules. Add a plain “Customize this plan with Baseball Coach” instruction. Publish only fictional or placeholder examples. The current package supplies content candidates; no website was built or published. [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)

If a site is later authorized, provide crawlable public HTML with working HTTP responses and no accidental indexing blocks. Search Console ownership verification, URL inspection, and a sitemap are later owner actions, not guarantees of indexing or ranking. [Google technical requirements](https://developers.google.com/search/docs/essentials/technical), [Search Console introduction](https://developers.google.com/search/docs/monitor-debug/search-console-start)

For technical discovery, use the repository README and accurate skill metadata to demonstrate these same requests. Metadata helps selection after a skill is available to a compatible agent; it does not automatically make it available in all assistants. Once release decisions are settled, consider a skills directory and the relevant host's plugin review process. Directory visibility is not the same as coach adoption or a checkout system. Vercel describes skills.sh as a discoverable ecosystem with a leaderboard; its FAQ says listings arise from CLI installs/telemetry rather than a manual leaderboard submission. Neither establishes paid-storefront terms for this project. [skills.sh announcement](https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem), [skills.sh FAQ](https://www.skills.sh/docs/faq)

Any outreach to leagues or parent communities should be separately approved and welcomed by that community. Future evaluation can ask adult coaches whether a plan was understandable and runnable and track consenting adult feedback. Do not create child profiles, publish participation data, or promise search rankings or traffic.

## Release decisions and review gates

1. **Ownership and license:** choose an explicit license and commercial terms; review originality and any future contributed material. No third-party curricula or real team files belong in the archive.
2. **Field usefulness:** an experienced youth coach should review activities and supervision; adult volunteers should try the plans under their league's requirements. Agent scenario tests are not field trials.
3. **Current sources:** verify league rules for the target division and season and recheck dated safety references. Clarify who maintains those references.
4. **Host test:** pick target hosts, validate their current schema, install only in an authorized test location, and test discovery plus complete outputs. Temporary isolated probes did not establish skill loading; see [host verification limits](evaluation/HOST-VALIDATION.md). No global installation was performed.
5. **Submission materials:** confirm publisher identity, support/privacy information, license, eligibility, and directory naming; then obtain separate authorization to publish. A local manifest or validator pass does not mean approval.

Claude's current checklist requires a qualifying README and license for directory listing. This package's absent license is an explicit blocker, and a Claude wrapper remains future work. [Claude pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)

OpenAI's current plugin guidelines prohibit sales of digital products/services and subscription or freemium upgrade promotion through plugins. Existing paid-account access is treated separately. Do not add a checkout or assume this skill can be sold inside that directory. Recheck the policy when a business model is chosen. [OpenAI commerce and monetization guidance](https://developers.openai.com/plugins/plugin-guidelines#commerce-and-monetization)

The local review ZIP belongs in `dist/`, which is ignored by Git. It is not source content to include in a future directory submission. Public submission and any monetization remain unperformed.

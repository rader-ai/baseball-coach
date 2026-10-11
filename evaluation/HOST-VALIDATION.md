# Host verification limits

Checked 2026-10-11 against the installed tools. This is an environment check, not a successful skill invocation or compatibility certification.

| Host | Observed result |
| --- | --- |
| ChatGPT desktop 26.1007.21159, bundled Codex CLI 0.162.0-alpha.17.2 | A temporary project contained the complete skill under `.agents/skills/baseball-coach`. The restricted CLI probe failed during app-server initialization before a model request. No skill loading was established. |
| Claude Code 2.1.292 | A temporary project contained the complete skill under `.claude/skills/baseball-coach`. A synthetic localhost response completed, but the request did not contain the skill body. The minimal probe had excluded project settings, so this is not evidence that ordinary project discovery fails. It is also not a loading pass. |

Both probes used a fixed localhost responder, no real credential or model inference, and a child-process sandbox that blocked external networking and writes outside temporary locations. The returned marker was predetermined. It is transport evidence only, not a coaching answer. No global installation or configuration change was made. No live host-model request was run; authorization did not include potentially billable execution. Further host testing remains a release gate.

Official documentation reviewed separately describes project discovery in [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills). Host-specific discovery requires the whole skill folder and applicable project/settings support. The README's direct-path trial asks an agent with repository access to read the skill; it does not verify automatic discovery. The root plugin manifest has not been validated by a host installation or marketplace submission.

Written scenario tests in this repository use separate Astra contexts with direct file access. They are evidence about those generated answers, not evidence that an installed host loads this skill correctly. No human field trial, print rendering test, or measured reading-time study has been performed.

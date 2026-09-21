# doc-skills

Agent skills for writing docs. Packaged as a Cursor team marketplace, like
[jowch/review-skills](https://github.com/jowch/review-skills): each skill is a
short `SKILL.md` plus `references/` loaded on demand.

## Plugins

| Plugin | Skill | What it does |
|---|---|---|
| `google-developer-style` | `google-developer-style` | Distills the [Google developer documentation style guide](https://developers.google.com/style) so agents write docs in that voice. |
| `google-developer-style` | `audit-doc-style` | Grades existing docs with a 100-point rubric, then proposes targeted fixes. Invoke with `/audit-doc-style`. |

The write skill stays short. Detail lives in
`skills/google-developer-style/references/` and is loaded only when needed.
This is not a copy of the full guide. When a topic isn't covered, use the
canonical page on [developers.google.com/style](https://developers.google.com/style).

`audit-doc-style` is the review loop: discover files, run a heuristic scan,
score against `skills/audit-doc-style/references/rubric.md`, print the report,
then edit. The scanner (`skills/audit-doc-style/scripts/scan.py`) only flags
high-frequency Don't terms. It is not a voice linter — don't add one.

## Add it to Cursor (team marketplace)

Requires a Cursor Teams or Enterprise plan.

### Dashboard (admins)

1. Open **Dashboard → Plugins & MCPs**.
2. Under **Team Marketplaces**, click **Add Marketplace**.
3. Choose **Import from Repo** and paste
   `https://github.com/jowch/doc-skills`.
4. Review the `google-developer-style` plugin, set marketplace access, and save.
   Turn on **Auto Refresh** if you want pushes to the tracked branch to
   re-index (needs the Cursor GitHub App on the repo).

### Customize (developers)

After the marketplace is imported, open **Customize** in the sidebar and
install `google-developer-style` from the team marketplace.

You can also use **Customize → From GitHub Repository** with the same URL if
your Cursor build exposes that import path.

### Local smoke test

Copy this repository to `~/.cursor/plugins/local/google-developer-style`,
reload the window, and confirm the skill appears in **Customize**. Local
imports must be allowed
(**Dashboard → Settings → Security & Identity → Marketplace and Plugins**).
A marketplace install of the same name wins over the local copy.

## Use it

Ask the agent to write or edit docs, or invoke `/google-developer-style`.
Typical prompts: "Write this README in Google developer style", "Edit these
API docs".

To grade what's already written, invoke `/audit-doc-style` or say "audit
these docs against Google style". The agent prints a scored report before
changing files.

The writer should keep its `SKILL.md` loaded and open a single
`references/*.md` file when the draft needs that topic. The auditor loads
the rubric plus only the write-skill references that a finding needs.

Optional pre-scan from this repo:

```bash
python3 skills/audit-doc-style/scripts/scan.py docs README.md
```

## Layout

```text
.
├── .cursor-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   ├── google-developer-style/
│   │   ├── SKILL.md
│   │   └── references/
│   └── audit-doc-style/
│       ├── SKILL.md
│       ├── references/
│       └── scripts/scan.py
├── LICENSE
└── README.md
```

## License

The plugin scaffolding (manifests, this README's original text, skill
routing) is [MIT](LICENSE), Copyright (c) 2026 Jonathan Chen.

The style guidance in `skills/google-developer-style/` is a modified
distillation of Google's developer documentation style guide.

Portions of those files are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
See [Google Developers Site Policies](https://developers.google.com/terms/site-policies).

Canonical sources:

- [About this guide](https://developers.google.com/style)
- [Highlights](https://developers.google.com/style/highlights)
- [Voice and tone](https://developers.google.com/style/tone)
- [Word list](https://developers.google.com/style/word-list)

This project is not affiliated with Google. Google, Google Developers, and
related marks are trademarks of Google LLC. Do not copy Google logos or brand
features from developers.google.com; those are not covered by CC BY 4.0.

---
name: google-developer-style
description: >
  Write and edit developer documentation in the Google developer documentation
  style. Use when writing, editing, or reviewing docs, READMEs, tutorials, API
  reference, conceptual pages, procedures, UI copy, Markdown, or HTML help.
  Triggers include "write docs", "Google style", "developer documentation",
  "edit this README", and "UI text".
---

# Google developer documentation style

Distilled from the [Google developer documentation style guide](https://developers.google.com/style). Keep this skill loaded while writing docs. Do **not** paste the whole guide into the conversation. Open a file under `references/` only when you need that topic.

## Authority

1. Project-specific style wins.
2. Then this skill and the cited `references/` file.
3. Then [Merriam-Webster](https://www.merriam-webster.com/) (spelling), *The Chicago Manual of Style*, 17th edition (nontechnical), and the [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) (technical).
4. Break a guideline when the alternative is clearer. Stay consistent in the document.

## Always

- Sound like a knowledgeable friend: conversational, friendly, respectful. Not a pitch, not a lecture.
- Address the reader as `you`. Use the imperative for steps (`Click Submit`).
- Use active voice and present tense. US English spelling and punctuation.
- Put the condition or goal before the instruction.
- Use sentence-case headings. Numbered lists for sequences; bullets otherwise. Serial commas.
- Put UI labels in **bold**. Put code, filenames, and commands in `code font`.
- Use descriptive link text. Write `For more information, see PAGE.`
- Write for a global audience and for accessibility.

## Never

- Don't use `please` in instructions. Don't call tasks `easy`, `simple`, or `just`.
- Don't address the reader as `we`. Don't start procedures with `Let's`.
- Don't pre-announce unreleased work. Don't use `will` for general behavior.
- Don't use `click here`, `this document`, or raw URLs as link text.
- Don't use directional UI language (`above`, `below`, `left-hand`).
- Don't use `&` for `and`, except when quoting a UI label that uses it.
- Don't use exclamation points in conceptual or reference docs.
- Don't use figurative, ableist, or culturally specific language.

## Load on demand

Read one reference at a time. Don't load them all.

| Need | File |
|---|---|
| Voice, politeness, what to avoid | `references/voice-and-tone.md` |
| Person, tense, contractions, global English, word choice | `references/language.md` |
| Commas, hyphens, quotation marks, periods | `references/punctuation.md` |
| Headings, lists, procedures, dates, notices, code in text | `references/formatting.md` |
| HTML vs Markdown, source formatting | `references/html-and-markdown.md` |
| Alt text, headings, links, tables, no directional language | `references/accessibility.md` |
| Buttons, menus, keys, UI verbs | `references/ui-text.md` |
| High-frequency preferred / banned terms | `references/word-list.md` |

Canonical source for anything not covered here: [developers.google.com/style](https://developers.google.com/style).

## Before you ship

Check the draft against **Always** and **Never**. If a term looks loaded or ambiguous, open `references/word-list.md`. If the page is a procedure, open `references/formatting.md` and `references/ui-text.md`.

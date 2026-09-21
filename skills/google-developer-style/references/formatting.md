# Formatting

Canonical: [Text-formatting summary](https://developers.google.com/style/text-formatting),
[Headings](https://developers.google.com/style/headings),
[Lists](https://developers.google.com/style/lists),
[Procedures](https://developers.google.com/style/procedures),
[Code in text](https://developers.google.com/style/code-in-text),
[Code samples](https://developers.google.com/style/code-samples),
[Cross-references](https://developers.google.com/style/cross-references),
[Dates and times](https://developers.google.com/style/dates-times),
[Notices](https://developers.google.com/style/notices).

## Emphasis

| Use | For |
|---|---|
| `**bold**` (`<b>`) | UI labels and run-in notice headings. Not product names. |
| `_italics_` (`<em>`) | Terms as terms, emphasis, titles of long works (unlinked), math variables. Sparingly. |
| `` `code` `` (`<code>`) | Code, filenames, commands, HTTP codes, placeholders, input. |
| Underline | Links only. Never for emphasis. |

In Markdown, prefer `**bold**` and `_italics_` so the markers stay distinguishable.

## Headings

- Sentence case. Unique `h1` / `#` once per page.
- Tasks: bare infinitive (`Create an instance`, not `Creating an instance`).
- Concepts: noun phrase, not an `-ing` opener (`Migration to Google Cloud`).
- Optional sections: `Optional: Customize your alias`.
- Don't skip heading levels. Don't leave empty headings. Don't put links or
  sequence numbers in headings.
- Referring to a group of subsections: `the following sections`, not
  `this section` / `these sections`.

## Lists

- Numbered: sequence matters (steps, phases).
- Bulleted: unordered sets.
- Description: term + explanation (glossary-like).
- Introduce with a complete sentence. Don't make the list complete a fragment.
- Parallel syntax. Capitalize items unless case is the point.
- End punctuation if the item is a sentence or has a verb. No end punctuation
  for a single word, a verbless phrase, all-code items, or a title/link-only
  item. If mixed, rewrite or punctuate every item.
- Don't use `etc.` or `and so on`. Frame the list as non-exhaustive instead
  (`such as`, `like`).

## Procedures

- Numbered steps. One imperative per step. First sentence of a step has an
  imperative verb.
- One-step procedure: a single bullet, not `1.`
- Sub-steps: `a, b, c`; nested: `i, ii, iii`.
- Context (tool or page) before the action. Goal before the action. Result
  after the action, same paragraph.
- `Optional:` at the start of an optional step, not `(Optional)`.
- Don't use `please`. Don't use `run the following command` — say what the
  command does. Don't document keyboard shortcuts as the primary path.
- One best method. Link to a repeated procedure instead of copying it.

Recommended: In the Google Cloud console, go to the **Monitoring** page.

Not recommended: Go to the **Monitoring** page in the Google Cloud console.

Recommended: To start a new document, click **File > New > Document**.

Not recommended: Click **File > New > Document** to start a new document.

## Code in text and samples

Put in code font: filenames, paths, class/method/function names, commands,
flags, HTTP verbs and status codes (`an HTTP 400 Bad Request status code`),
env vars, ports, input, output, placeholders (`REPLACE_ME`).

Don't code-font product names, ordinary domain names, or URLs the reader
should open in a browser (those should be descriptive links).

Don't inflect code (`POST` the data). Add an English noun and inflect that
(`send a POST request`).

Introduce a sample with a sentence. Colon if the sample follows immediately.
Wrap near 80 characters. Spaces, not tabs, matching the language's style
guide. Omissions: a language comment, not `...`.

## Links

- Descriptive text: page title or a short phrase. Never `click here`,
  `this document`, or a bare URL.
- Dedicated cross-reference sentence: `For more information, see PAGE.`
  Use `about`, not `on`. Use `see` for links.
- Punctuation outside the link. Don't quote a linked title.
- Same tab unless you disclose `(opens in a new tab)`.
- On-page jumps: `see the SECTION section of this document`.
- Downloads: say so and name the file type.

## Dates, times, numbers

- `January 19, 2017`. Full month, four-digit year. Comma after the year in
  mid-sentence. No comma for `January 2017`.
- Numeric-only only when forced: ISO `YYYY-MM-DD` (`2017-04-15`).
- 12-hour clock: `3 PM`, `3:45 PM`. Hyphen ranges (`5-10 minutes`).
- No seasons. Use month or quarter.
- Versions: `2.2 or later`, not `2.2+` or `2.2 or higher`.

## Notices

Use notices sparingly. Readers skip them.

- **Note:** useful, skippable.
- **Caution:** proceed carefully.
- **Warning:** don't do this, or the step is irreversible.
- **Success:** interactive content only.

Don't put prerequisites, required steps, expected results, or
cross-references in notes.

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Sources linked at the top of this file.

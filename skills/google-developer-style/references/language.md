# Language

Canonical: [Second person](https://developers.google.com/style/person),
[Active voice](https://developers.google.com/style/voice),
[Present tense](https://developers.google.com/style/tense),
[Contractions](https://developers.google.com/style/contractions),
[Sentence structure](https://developers.google.com/style/sentence-structure),
[Write for a global audience](https://developers.google.com/style/translation),
[Write inclusive documentation](https://developers.google.com/style/inclusive-documentation).

## Person

- Address the reader as `you` / `your`, not `we` / `our` / `us`.
- Imperative for instructions (`Click Submit`). The `you` is implied.
- Use `user` only for the end user of software the reader is building.
- Third person for what software does (`The server sends an acknowledgment`).
- `we` is OK only when the antecedent is the documenting organization
  (`Example Organization provides A and B, but we don't provide C`).
- Identify who `you` is (developer, admin) and stay consistent.

Recommended: This document shows you how to develop an app for your organization.

Not recommended: Let's add a description to our table.

## Voice and tense

- Active voice: the grammatical subject performs the action.
- Present tense for general behavior. Don't use `will` for what the product
  does now. Future tense is OK when the action is actually later
  (`The file will be archived the next time backup runs`).
- Avoid hypothetical `would`.

Recommended: Send a query to the service. The server sends an acknowledgment.

Not recommended: The service is queried, and an acknowledgment is sent.

Passive is OK when emphasizing the object (`The file is saved`),
de-emphasizing the actor, or when the actor doesn't matter.

## Contractions

Use common two-word contractions (`you're`, `don't`, `isn't`, `can't`).
Negation contractions are harder to miss when scanning than a lone `not`.

Don't invent contractions (`guides're`) or use three-word ones (`mightn't've`).

## Sentence shape

- Circumstance, condition, or goal **before** the instruction, so the reader
  can skip what doesn't apply.
- Subject + verb + object. Keep the main subject and verb near the start.
- Prefer shorter sentences. Aim under 26 words when you can.
- Include helper words: `then`, `that`, `of`, relative pronouns.
- Don't stack more than two nouns as modifiers of another noun.
- Don't use the same word as both noun and verb nearby.

Recommended: To delete the entire document, click **Delete**.

Not recommended: Click **Delete** if you want to delete the entire document.

Recommended: If the attribute key is not found, then the default value is returned.

Not recommended: If the attribute key is not found, the default value is returned.

## Global English

Write US English with translation in mind.

- Prefer `start` / `begin` over `commence`; `use` over `utilize` / `leverage`;
  `so` over `consequently`.
- Avoid phrasal verbs when a single verb works (`uses` not `makes use of`).
  `set up`, `log in`, and `sign in` are exceptions.
- Repeat a word if the redundancy helps (`IAM segmentation and network
  segmentation`, not `IAM and network segmentation`).
- Spell out abbreviations on first use.
- Replace ambiguous pronouns with the noun.
- No humor, slang, idioms, or holidays. No seasons (`In November`, not
  `In winter`). Diverse example names. Unambiguous dates.

## Inclusive language

- Singular `they`. No generic `he` / `she`, `guys`, `man-hours`.
- No ableist terms (`crazy`, `insane`, `dummy` for placeholders, `sanity
  check`). Prefer `placeholder`, `quick check`, `baffling`.
- No `blacklist` / `whitelist` (prefer `allowlist` / `blocklist` or rewrite).
  No `master`/`slave` (prefer `primary`/`replica`, `controller`/`worker`).
- No `first-class citizen`. Avoid socially charged jargon.
- If a banned term is in code, mention it once in `code font`, then use the
  inclusive term.

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Sources linked at the top of this file.

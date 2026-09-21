# Word list (high-frequency)

Canonical: [Word list](https://developers.google.com/style/word-list).
This file is a short agent index, not a copy of the full list. If the term
isn't here, look it up on that page, then Merriam-Webster (first spelling).

Don't use: avoid in all cases (rewrite, or mention a code identifier once in
`code font`). Use with caution: prefer a more precise term.

## Prefer these

| Instead of | Use |
|---|---|
| `above` / `below` (in a doc) | preceding / following / earlier / later |
| `above` / `higher` (versions) | later (`2.2 or later`) |
| `below` / `lower` (versions) | earlier |
| `allows you to` / `enables you to` | lets you |
| `as of this writing` | omit (timeless) |
| `blacklist` / `whitelist` | allowlist / blocklist, or rewrite (`add them to an allowlist`) |
| `check` / `uncheck` (checkbox) | select / clear |
| `click on` | click |
| `click here` | descriptive link text |
| `presently` / `currently` (supported) | omit, or name the version |
| `desire` / `wish` | want / need |
| `e.g.` / `i.e.` | for example / that is |
| `etc.` / `and so on` | such as / like / including |
| `execute` (generic) | run |
| `hamburger` / `kebab` / `zippy` | the control's `aria-label` (`**Menu**`) |
| `hang` (process) | stop responding / isn't responding |
| `hit` (click/press) | click / press / enter |
| `hover` | hold the pointer over |
| `in order to` | to (unless `to` is ambiguous) |
| `just` / `simply` / `easy` / `easily` | omit |
| `kill` / `terminate` (generic stop) | stop / exit / cancel / end |
| `leverage` / `utilize` | use |
| `let's` | you / imperative |
| `log in` (verb) | sign in (unless the product says log in) |
| `master` / `slave` | primary / replica, controller / worker, … |
| `once` (meaning after) | after |
| `please` (in steps) | omit |
| `sanity check` | quick check / confidence check |
| `since` (meaning because) | because |
| `via` | rewrite (`by using`, `over`, `through`) |
| `vice versa` | spell out both directions |
| `we` (the reader) | you |
| `while` (contrast) | although |
| `will` / `would` (general behavior) | present tense / can |

## Spelling and form

- `filename`, `file system`, `frontend`, `lifecycle`, `screenshot`,
  `stylesheet` or `style sheet` (pick one per doc), `timestamp`, `wildcard`,
  `whitespace`, `setup` (noun) / `set up` (verb), `sign-in` (noun) /
  `sign in` (verb), `sign in to` (not `sign into`), `on-premises` (not
  `on-prem` / `on-premise`), `email` (not `e-mail`; not a verb — `send email`).
- `data` is singular mass: `the data is`, `less data`.
- `indexes` not `appendices`/`indices` unless the domain requires it
  (`appendixes`, `indexes`).
- `US` not `U.S.`. `HTTPS` not `HTTPs`. `ID` not `Id`.
- `generative AI` (not `gen AI`). `Markdown` always capitalized.
- `internet` and `web` lowercase unless starting a sentence.

## Don't use (rewrite)

`&` for *and*; `aka`; `anti-pattern` (say what to avoid); `click here`;
`crazy` / `insane` / `dummy variable` (use `placeholder`);
`cripple`; `guys`; `he`/`she` as generic; `man-hours` (`person-hours`);
`first-class citizen`; `tl;dr`; `RTFM`; `voila`; `out of the box` (figurative);
`pets vs cattle`; `single pane of glass`; `tribal knowledge`; `war room`.

If the banned word is a code identifier, write it once in `code font` and
switch to the inclusive term.

## Modal verbs

- `can`: ability or permission.
- `might`: possibility.
- `must`: requirement.
- `may`: legal/policy only. Otherwise `can` / `might`.
- `should`: usually too ambiguous; make it `must` or explain the tradeoff.

## Agent lookup

For anything else, open
[developers.google.com/style/word-list](https://developers.google.com/style/word-list)
and search the heading. Don't paste the whole list into the session.

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Source: [Word list](https://developers.google.com/style/word-list).

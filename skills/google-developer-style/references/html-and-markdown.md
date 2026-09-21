# HTML and Markdown

Canonical: [Markdown versus HTML](https://developers.google.com/style/markdown),
[HTML formatting](https://developers.google.com/style/html-formatting),
[Text-formatting summary](https://developers.google.com/style/text-formatting).

Use whichever the project already uses. Don't mix without a reason. Markdown
is easier to write and read; HTML is better for semantic tagging (for example
`<code>` around a nonbreaking space, or `<kbd>` for keys).

## Source hygiene

Follow the [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html),
with this exception: don't omit optional HTML elements.

- Spaces, not tabs. Two spaces per indent.
- Lowercase HTML elements and attributes.
- No trailing spaces except where Markdown requires them (two spaces for a
  hard line break — prefer a paragraph or list instead).
- Wrap prose at 80 characters. Don't wrap URLs; put a long `href` on its own
  line. Don't wrap YAML frontmatter values that must stay one line.
- Match an existing file's wrap width if it's consistent and not 80.

## Markdown markers

| Meaning | Use |
|---|---|
| Bold | `**text**` (not `__text__`) |
| Italics / emphasis | `_text_` (not `*text*`) |
| Inline code | `` `text` `` |
| Code block | fenced ` ``` ` (or four-space indent) |
| Heading | `#` / `##` / `###` matching hierarchy; don't skip levels |

Don't override font, size, or color inline. Semantic markup only.

## HTML semantics

- `<b>` for UI labels (visual attention). Not `<strong>` for that.
- `<em>` for actual emphasis. Not `<i>` as a styling hook.
- `<code>` for code in text. `<pre>` for samples. `<kbd>` for keys to press.
- Native elements over custom styled `<div>`s.
- Semantic headings (`h1`–`h6`), lists (`ul`/`ol`/`dl`), and tables (`th`
  with `scope`).

## Line length in samples

Break code in `<pre>` / fences near 80 characters without changing meaning.
If you don't know the language, don't wrap a long token. Older files that
already wrap at a different width: match them for small edits.

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Sources linked at the top of this file.

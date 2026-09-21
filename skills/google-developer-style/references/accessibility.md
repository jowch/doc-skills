# Accessibility

Canonical: [Write accessible documentation](https://developers.google.com/style/accessibility),
[Write inclusive documentation](https://developers.google.com/style/inclusive-documentation),
[Write for a global audience](https://developers.google.com/style/translation).

Accessibility improves the page for everyone. Don't communicate meaning by
color, size, or position alone.

## Language

- No ableist language. See `references/word-list.md` and
  `references/language.md`.
- Short sentences. Important information first in a paragraph.
- Parallel lists. Define acronyms on first use.
- Don't force line breaks inside a sentence. Don't use `&` for `and`.
- Avoid ALL CAPS and unnecessary camelCase in prose. Some screen readers
  spell all-caps letter by letter.
- Don't rely on punctuation alone for meaning. Avoid `!`, `?`, and `;` when
  a period works.
- No directional language for UI or for the page (`above`, `below`,
  `right-hand`). Use `preceding` / `following`, or name the element.

Recommended: In the preceding diagram, clients run jobs on the cluster.

Not recommended: In the diagram above, clients run jobs on the cluster.

Recommended: Click **Menu**.

Not recommended: In the left-side panel, click the button with three lines.

## Structure

- Heading hierarchy; don't skip levels; no empty headings.
- Break walls of text. Left-align; don't center or justify body text.
- Every procedure instruction is a list item.
- Introduce tables in the preceding sentence. Header cells on the first row
  and first column only. No `colspan` / `rowspan`. Avoid tables mid-procedure
  when a list works.

## Links

- Meaningful when read out of context. Never `click here`.
- Use `see` for cross-references.
- Disclose downloads, new tabs, and same-page jumps.
- Avoid adjacent links; put a character between them.

## Images, video, interactive

- Every image has `alt`. Decorative: empty `alt`. Don't present new
  information only in an image. Don't screenshot text, code, or terminal
  output — use real text. Prefer SVG.
- Captions or transcripts for audio and video. No flickering GIFs.
- Keyboard must reach every control. Native `<button>` for form submit.
- Label every input with `<label>` outside the field. Error text says what
  went wrong and how to fix it.
- Menu paths with `>` need `aria-label="and then"` on the bracket. See
  `references/ui-text.md`.
- Contrast at least 4.5:1. Don't hide content with `display:none` /
  `visibility:hidden` if a screen reader should hear it.

## Verify

Read the page without sound, with only sound, without images, without color,
with a keyboard, zoomed, and without punctuation. If any of those loses
information, fix the text.

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Sources linked at the top of this file.

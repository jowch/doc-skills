# UI text

Canonical: [UI elements and interaction](https://developers.google.com/style/ui-elements),
[Procedures](https://developers.google.com/style/procedures).

State the reader's goal when that's enough. Name widgets only when the UI
isn't obvious or the point of the page is the UI.

Recommended: Refresh the page.

Also recommended: Click **Refresh**.

## Names of UI elements

- Bold the visible label (`**Save**`). Don't use quotation marks around it.
- Follow on-screen capitalization unless it's ALL CAPS or inconsistent — then
  sentence case.
- Don't use a UI label as an English verb or noun
  (`In the **Name** field, enter an account name`, not `Name the account`).
- Don't call out the widget type when the label is enough
  (`Click **OK**`, not `Click the "OK" button`).
- Drop trailing ellipses in labels (`**Browse**`, not `**Browse...**`).
- Icon buttons: tooltip text, with the icon if you have it. If there's no
  tooltip, file a bug; don't invent slang (`hamburger`, `zippy`, `kebab`).

## Terminology

| Thing | Call it | Preposition |
|---|---|---|
| Whole desktop app frame | window | in |
| Web / console surface | page | on |
| Modal | dialog (not pop-up) | in |
| Distinct region in a window | pane or panel | in |
| Labeled group of controls | section | in |
| Menu item | command | in the **File** menu |
| Site or app nav list | navigation menu | in |
| Button strip | toolbar | on |
| File-tab control | tab | on |
| Typing control | box (Google Cloud / Workspace: field) | in |
| Checkbox | checkbox; **select** / **clear** | — |
| Mutually exclusive option | radio button's label; **select** | — |
| Expand control | expander arrow | — |
| On/off switch | toggle (noun only; never "toggle it") | — |

Don't use `drop-down` as a noun. Omit `drop-down` from `list` / `menu` unless
you need it to disambiguate.

## Menus

`In the **File** menu, select **Open**.`

Angle-bracket shorthand is OK for a menu path only:

```markdown
Select **View&nbsp;<span aria-label="and then">></span> Tools&nbsp;<span aria-label="and then">></span> Developer Tools**.
```

Don't chain mixed widgets with `>`
(not `**MyApp > Preferences > Languages > + > CSS**`).

## Keys

- `<kbd>` in HTML; monospace if you can't.
- Spell modifiers: `Control+S` (or `Command+S` on macOS). Uppercase letter
  keys. No symbols (`⌘`) and no `Ctrl`.
- `press` for a key that causes an action. `enter` / `type` for text input.
  Prefer `enter` over `type` (paste and speech also enter text).
- Don't make a keyboard shortcut the documented path unless that's the
  product.

## Verbs

`click` (not `click on`), `select`, `clear`, `enter`, `press`, `drag`
(not `click and drag`), `hold the pointer over` (not `hover` or `hit`),
`go to` rather than `scroll`, `turn on` / `turn off` or `enable` consistently.
`tap` on touch. Don't use `check` / `uncheck` for checkboxes.

## Don't

- Directional language. If the control is hard to find, name it and add a
  screenshot.
- `please`. `hamburger`. `zippy`. `expando`. `hit New`.
- `toggle` as a verb. Describe the resulting state
  (`click the **Wi-Fi** toggle to the on position`).

Portions of this page are modifications based on work created and shared by
Google and used according to terms described in the
[Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/).
Sources linked at the top of this file.

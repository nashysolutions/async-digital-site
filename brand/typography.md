# Typography

The typographic system for async-digital-site. No hosted webfont — the web is served with the host's system stack so pages render instantly and match the reader's OS conventions. Print and email have their own stacks.

## Typefaces

### Web — system stack

```
-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif
```

One family, delivered by the OS:

- **macOS / iOS:** San Francisco.
- **Windows:** Segoe UI.
- **Android / Chrome OS:** Roboto.
- **Anywhere else:** Helvetica → Arial → generic sans-serif.

Chosen deliberately over a hosted webfont:

- Zero network cost; no FOUT / FOIT.
- The reader already trusts this face — it's their OS UI font.
- No licence management; no subsetting; no webfont loader.
- The brand differentiation lives in voice, palette, and layout, not in the typeface.

### Print — Inter

When a piece of content leaves the web (PDFs, print templates under #22, leaflets, decks), use **Inter** (Google Fonts, SIL OFL 1.1). Inter is free for print and email, ships in a full weight range, and was designed for UI — it pairs well with the system-stack web rendering without an obvious handoff.

### Email — Arial stack

```
Arial, Helvetica, sans-serif
```

The narrow, predictable stack that renders the same in Outlook, Gmail, Apple Mail, and every other client worth targeting. Used by the HTML signature and the Mailchimp master template (#23, #28).

## Type scale

One scale. The same sizes apply to desktop web, print, and (where possible) email.

| Token         | Size    | Line-height | Weight | Role                               |
| ------------- | ------- | ----------- | ------ | ---------------------------------- |
| `--size-h1`   | 44px    | 1.12        | 700    | Hero headline. One per page.       |
| `--size-h2`   | 20px    | 1.3         | 600    | Section headings.                  |
| `--size-h3`   | 16px    | 1.4         | 600    | Card and tile headings. Same size as body; weight differentiates. |
| `--size-intro`| 19px    | 1.55        | 400    | Hero supporting paragraph (tagline, lede). |
| `--size-body` | 16px    | 1.55        | 400    | Default body text.                 |
| `--size-small`| 14px    | 1.5         | 400    | Footer, meta, pill labels, fine print. |

No separate `caption` tier — `--size-small` covers every sub-body use on the site today. Add one later if a real use case appears.

### Responsive H1

The hero headline steps down on narrower viewports to stay within the measure.

| Viewport        | `--size-h1` |
| --------------- | ----------- |
| ≥ 900px         | 44px        |
| 481 – 899px     | 36px        |
| ≤ 480px         | 32px        |

Other sizes hold steady across breakpoints — the body scale is already readable on mobile.

## Weights used

- 400 — regular body, intro, small
- 600 — h2, h3
- 700 — h1

System stacks expose 400 / 600 / 700 reliably. Don't reach for 500, 800, or 900 — rendering varies across platforms.

## Licences

| Face            | Licence                                | Web  | Print | Email |
| --------------- | -------------------------------------- | ---- | ----- | ----- |
| System stack    | Shipped by the OS — no licence needed  | ✅   | —     | —     |
| Inter           | SIL OFL 1.1 — free for all uses        | ✅   | ✅    | ✅    |
| Arial, Helvetica| Bundled on target email clients        | —    | —     | ✅    |

## Measure and reading

- Hero supporting paragraph (`--size-intro`): max 68ch.
- H1 headline: max 30ch.
- Body paragraphs: no fixed max; rely on the `.wrap` container (960px) to constrain line length on desktop.

## Source of truth

Base decisions live in `projects/incubating/async-digital-brand-foundation.md` in the knowledge vault. Changes go there first, then here, then into `assets/brand.css`.

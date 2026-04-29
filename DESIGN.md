---
version: alpha
name: Async Digital
description: Brand tokens and rationale for coding agents building on async-digital.com.
colors:
  primary: "#8B3A2A"
  accent: "#2A3A4A"
  bg: "#FDFBF7"
  card: "#F8F5EE"
  border: "#E8E4DC"
  text: "#1F1C18"
  muted: "#6B6560"
  success: "#3E7A4A"
  warning: "#C48B2C"
  error: "#CC2222"
  on-primary: "#FFFFFF"
  on-accent: "#FFFFFF"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.02em
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.02em
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.02em
  heading-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  heading-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
  intro:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
rounded:
  sm: 4px
  DEFAULT: 10px
  lg: 16px
  full: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 44px
  "2xl": 48px
components:
  button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.DEFAULT}"
    padding: "10px 14px"
  button-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  button-focus:
    outline: "3px solid color-mix(in srgb, {colors.primary} 35%, transparent)"
  card:
    backgroundColor: "{colors.card}"
    borderColor: "{colors.border}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 22px
  tile:
    backgroundColor: "{colors.card}"
    borderColor: "{colors.border}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 22px
  step:
    backgroundColor: "{colors.bg}"
    borderColor: "{colors.border}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 20px
  signal-pill:
    backgroundColor: "rgba(0,0,0,0.02)"
    borderColor: "{colors.border}"
    textColor: "{colors.muted}"
    typography: "{typography.small}"
    rounded: "{rounded.full}"
    padding: "6px 10px"
  link:
    textColor: "{colors.text}"
    borderColor: "{colors.border}"
  section-accent-bar:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 3px
    width: 52px
  inline-code:
    backgroundColor: "rgba(0,0,0,0.04)"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: "1px 4px"
  card-grid:
    display: grid
    gap: "{spacing.md}"
    columns: 3
    collapseBelow: 900px
---

> **Read me first.** This file is for coding agents building UI on async-digital.com. The human-facing brand portal is [`BRAND.md`](BRAND.md), which links to the foundation docs in [`brand/`](brand/) and to the runtime tokens in [`assets/brand.css`](assets/brand.css). When tokens here disagree with `assets/brand.css`, **`brand.css` wins** — it's the runtime source. File a fix.

## Brand & Style

Async Digital is a UK studio that provides automation services. The site currently leads with one service: missed-call follow-up for dental clinics. The brand reads as **calm, plain, and clinical-adjacent** — never hyped, never salesy, never vapour-startup. We sit next to a regulated profession.

The visual identity is deliberately warm against a sea of blue-teal dental software. Deep brick (`primary`) plus charcoal navy (`accent`) on a warm off-white background. No gradients, no glassmorphism, no heavy shadows. Soft hairline borders, generous whitespace, single-bar accents under section headings as a visual nod to the logo's parallel-threads motif.

The logo (six horizontal bars of varying widths) is the only place that motif appears in repetition. **Don't repeat the bar-stack pattern as a section divider, page accent, or template decoration** — keep the logo distinctive.

## Colors

Two brand colours, five neutrals, three status colours. Full pairings, contrast ratios, and don't-do swatches are in [`brand/colour.md`](brand/colour.md). All currently-used pairings on the site meet WCAG AA.

- **`primary`** (`#8B3A2A`, deep brick) — buttons, the section-accent bar under H2s, the logo mark, primary links.
- **`accent`** (`#2A3A4A`, charcoal navy) — secondary emphasis. Underused today; reserve for headings if a piece of copy needs to lean professional rather than warm.
- **Neutrals** (`bg`, `card`, `border`, `text`, `muted`) — warm off-whites and a near-black. Cards sit on the page background using `card` plus a 1px `border`; never use box-shadow as the primary surface separator.
- **Status** (`success`, `warning`, `error`) — used for inline indicators only. `warning` requires dark text (`text`) on top; white-on-warning fails AA.

**Don't:** put `primary` against `accent` (1.5:1 — fails every contrast bar), `primary` against `error` (two warm reds read muddy), or `muted` on `border` as text (fails AA).

## Typography

System stack only on the web — `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. No webfont loader, no FOUT, no licence management. The brand differentiation lives in voice, palette, and layout. Inter is used for print; Arial stack for email. See [`brand/typography.md`](brand/typography.md) for the full rationale.

One scale, three weights (400 / 600 / 700), British English copy. Hero headline (`display`) steps down on narrow viewports — use `display-md` ≤ 900px and `display-sm` ≤ 480px. Card and tile headings (`heading-md`) are body-size; **weight differentiates, not size**.

Measure: hero headline max 30ch, hero supporting paragraph (`intro`) max 68ch, body paragraphs constrained by the 960px `.wrap` container.

## Layout & Spacing

Single-column, centred, mobile-first. The page container (`.wrap`) is 960px max-width with 48px vertical and 24px horizontal padding (40px / 24px on narrow viewports). Sections separate at 44px vertical rhythm (`xl`). Card grids are 3-column on ≥ 900px, single-column below.

Spacing scale is roughly 8px-based: `xs` 4px (tight gaps), `sm` 8px, `md` 16px (the standard gap), `lg` 24px (container horizontal), `xl` 44px (section vertical), `2xl` 48px (page vertical, footer top). One-offs (button padding `10px 14px`, card padding `22px`, step padding `20px`) live as component tokens, not the global scale.

## Elevation & Depth

**Mostly flat.** Surface separation comes from a 1px `border` hairline, not shadow.

- Cards, tiles, and steps sit on the page background with a `border` and rounded corners — no resting shadow.
- The button gets a soft drop shadow (`0 10px 24px rgba(0,0,0,0.10)`) on hover only, paired with a 1px upward translate. Tactile feedback, not depth theatre.
- Focus rings are 3px, `primary` mixed to 35% opacity via `color-mix`, with a 3px offset.

Don't introduce ambient shadows on cards, tonal layers, or glass blur. The site is meant to feel like a printed page, not an app surface.

## Shapes

Four-rung rounded scale.

- **`sm` (4px)** — inline code only.
- **`DEFAULT` (10px)** — buttons. Substantial without being friendly-cartoonish.
- **`lg` (16px)** — cards, tiles, steps.
- **`full` (999px)** — pill chips (`signal-pill`), the section-accent bar, focus rings.

Don't introduce a `xl` rung above 16px. The visual language is restrained, not soft. If you reach for a bigger radius, the layout is probably wrong.

## Components

The current vocabulary is small — this is a marketing site, not an app. Each component below maps to an existing CSS class in [`styles.css`](styles.css).

- **`button`** (`.button`) — single CTA shape. Brick background, white text, 10px radius, hover lifts -1px with a soft shadow, focus ring at 35% primary. Don't add a secondary button style without a copy reason; an underlined link is the secondary CTA.
- **`card` / `tile`** (`.card`, `.tile`) — content containers on the warm `card` surface with hairline border. 16px radius, 22px padding. Use for grouped content; don't nest.
- **`step`** (`.step`) — numbered process container. Same shape as card but on the page `bg` so a sequence reads as ordered work, not parallel options.
- **`signal-pill`** (`.signals li`) — small bordered pill for trust signals (location, company number). Muted text, near-transparent fill, hairline border, full-rounded.
- **`link`** (`.link`, `.tile a`, footer links) — text-coloured with a 1px `border`-coloured underline that darkens on hover. **No coloured links.** Use the button when you need primary action.
- **`section-accent-bar`** — 3px × 52px primary-coloured pill under each section H2 (`section h2::after`). The site's only repeating brand flourish — ship one per section, don't echo it elsewhere on the page.
- **`card-grid`** (`.grid.cards`) — three-column wrapper for `card` or `tile` children. Collapses to one column ≤ 900px. Variants: `.grid.work` for work-sample tiles, `.steps` for ordered numbered-process containers (uses `step` rather than `card`).

## Voice

Visual tokens cover half the brand. The other half is words, and an agent that ignores the voice rules will produce on-brand-looking pages with off-brand copy. **Read [`brand/voice.md`](brand/voice.md)** for the full guide. The non-negotiables:

- **No em dashes.** Ever. Em dashes are the strongest tell that an LLM wrote the draft. Use a full stop, comma, or pair of parentheses.
- **No exclamation marks.** Ever. Not even one.
- **British English** spelling (`organisation`, `colour`, `recognise`).
- **Sentence case** for headings and buttons. Not Title Case.
- **Hero H1 takes no terminal punctuation.** A title, not a sentence.
- **Contractions** (`we're`, `it's`) — "we are" sounds like a press release.
- **Specific nouns** — `clinic` not `practice`, `patient` not `customer`, `enquiry` not `lead`, `automation` not `platform`.
- **Avoid:** `cutting-edge`, `leverage`, `synergy`, `seamless`, `world-class`, `next-generation`, `unlock`, `empower`, `10x`, `solution` as a noun.
- **No emoji.**

If the copy you generate sounds like a brochure, it's wrong. If it sounds like a friend who happens to run a clinic, it's close.

## Localisation

The site ships in English and Welsh — both are first-class. The user-facing language toggle uses the `.lang-switch` pattern. When generating copy for new pages, generate the English first, then commission a Welsh translation rather than machine-translating; Welsh has mutation rules and register sensitivity that don't survive automatic translation. The privacy and brand-voice rules apply identically to both.

## Do's and Don'ts

**Do**
- Read `brand/voice.md` before writing user-facing copy.
- Use `var(--token-name)` in CSS, not hex literals. The runtime tokens live in `assets/brand.css`.
- Ship a Welsh translation alongside any new English page.
- Verify contrast for any new colour pairing against the table in `brand/colour.md`.
- Use sentence case for buttons, headings, and menu items.

**Don't**
- Don't write em dashes, exclamation marks, or three-adjective stacks ("fast, secure, and reliable").
- Don't add a hosted webfont. The system stack is a deliberate choice, not a placeholder.
- Don't repeat the logo's bar-stack motif as page decoration. One mark, one section-accent bar — that's the whole brand flourish budget.
- Don't introduce gradients, glassmorphism, ambient shadows on resting cards, or rounded corners larger than 16px.
- Don't add a coloured link style. Underline-on-text-colour is the link.
- Don't put `primary` adjacent to `accent` or `error` — they clash.
- Don't claim AI features, scale, or sophistication the product doesn't have today. The voice is honest by policy.

---

**Update order if a token changes:** vault decision log → `brand/<file>.md` → `assets/brand.css` → this file. Documented in [`BRAND.md`](BRAND.md).

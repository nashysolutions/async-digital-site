# Colour Palette

The palette for async-digital-site. Two brand colours (primary + accent), a subtle warm neutral system, and three conventional status colours. All token names map 1:1 to CSS custom properties — the names here are the names that should appear in `brand.css` (wired up in #13).

## Direction

Warm / unexpected tones, deliberately differentiating from the blue-teal default that dominates the dental space. The primary is a deep brick, the accent is a restrained charcoal navy — professional pairing rather than vintage gold or forest green. Neutrals are a subtle warm path: off-white backgrounds with barely-warm surfaces and borders.

## Palette

### Brand

| Token         | HEX       | RGB             | CMYK (approx.)      | Pantone   | Role                                 |
| ------------- | --------- | --------------- | ------------------- | --------- | ------------------------------------ |
| `--primary`   | `#8B3A2A` | 139, 58, 42     | 0 / 58 / 70 / 45    | TODO (#19)| Brand colour. Buttons, accents, logo mark. |
| `--accent`    | `#2A3A4A` | 42, 58, 74      | 43 / 22 / 0 / 71    | TODO (#19)| Restrained pairing with primary. Headings, secondary emphasis. |

### Neutrals

| Token       | HEX       | RGB             | CMYK (approx.)      | Role                          |
| ----------- | --------- | --------------- | ------------------- | ----------------------------- |
| `--bg`      | `#FDFBF7` | 253, 251, 247   | 0 / 1 / 2 / 1       | Page background.              |
| `--card`    | `#F8F5EE` | 248, 245, 238   | 0 / 1 / 4 / 3       | Surface for cards / tiles.    |
| `--border`  | `#E8E4DC` | 232, 228, 220   | 0 / 2 / 5 / 9       | Hairline borders, separators. |
| `--text`    | `#1F1C18` | 31, 28, 24      | 0 / 10 / 23 / 88    | Body and heading text.        |
| `--muted`   | `#6B6560` | 107, 101, 96    | 0 / 6 / 10 / 58     | Secondary / supporting text.  |

### Status

| Token        | HEX       | RGB             | CMYK (approx.)      | Role                                |
| ------------ | --------- | --------------- | ------------------- | ----------------------------------- |
| `--success`  | `#3E7A4A` | 62, 122, 74     | 49 / 0 / 39 / 52    | Success indicators.                 |
| `--warning`  | `#C48B2C` | 196, 139, 44    | 0 / 29 / 78 / 23    | Warning indicators.                 |
| `--error`    | `#CC2222` | 204, 34, 34     | 0 / 83 / 83 / 20    | Error indicators (kept visually distinct from `--primary`). |

Pantone matching is deferred to the first real print job (#22 business cards). CMYK values are naive RGB→CMYK conversions and must be test-printed before going to any print supplier — colour appearance on paper depends on stock and ICC profile.

## Accessibility

WCAG AA requires 4.5:1 for body text, 3.0:1 for UI components and large text (≥18pt or 14pt bold). AAA is 7.0:1. Every pairing below is used on the live site.

### Text pairings

| Foreground    | Background    | Ratio    | AA body | AAA body |
| ------------- | ------------- | -------- | ------- | -------- |
| `--text`      | `--bg`        | 16.4:1   | ✅      | ✅       |
| `--text`      | `--card`      | 15.6:1   | ✅      | ✅       |
| `--muted`     | `--bg`        | 5.6:1    | ✅      | ❌       |
| `--muted`     | `--card`      | 5.3:1    | ✅      | ❌       |
| white         | `--primary`   | 7.7:1    | ✅      | ✅       |
| white         | `--accent`    | 11.7:1   | ✅      | ✅       |
| white         | `--success`   | 5.1:1    | ✅      | ❌       |
| `--text`      | `--warning`   | 5.7:1    | ✅      | ❌       |
| white         | `--error`     | 5.5:1    | ✅      | ❌       |

### On-brand colours as text on surface

| Foreground    | Background    | Ratio    | AA body | Use                                        |
| ------------- | ------------- | -------- | ------- | ------------------------------------------ |
| `--primary`   | `--bg`        | 7.4:1    | ✅      | Primary links, emphasis.                   |
| `--accent`    | `--bg`        | 11.3:1   | ✅      | Headings, secondary emphasis.              |
| `--success`   | `--bg`        | 5.0:1    | ✅      | Inline success text (sparingly).           |
| `--error`     | `--bg`        | 5.3:1    | ✅      | Inline error text.                         |

All currently-used text pairings meet AA. `--muted` combinations sit just above the AA threshold; do not reduce the muted tone further without re-checking.

## Don't-do swatches

Combinations that fail accessibility or create a brand clash. Avoid unless specifically overridden.

| Combination                           | Ratio  | Why to avoid                                                         |
| ------------------------------------- | ------ | -------------------------------------------------------------------- |
| white on `--warning`                  | 3.0:1  | Fails AA for body text. Always use dark text (`--text`) on warning.  |
| `--warning` as body text on `--bg`    | 2.9:1  | Fails AA. Warning is for icons / borders / background fills only.    |
| `--primary` on `--accent`             | 1.5:1  | Brand clash + fails every contrast bar. Do not place these together. |
| `--muted` on `--border`               | ~3.6:1 | Fails AA for body text. Borders are decorative, never text surface.  |
| `--primary` on `--error`              | ~1.7:1 | Brand clash — two warm reds read as a single muddy block.            |

## Token naming

Short names are used deliberately — they match the existing CSS custom property shape in `styles.css` and keep selectors readable. No `--brand-*` prefix. When wiring into `brand.css` (#13):

- Drop the old `--accent-2` variable; the new palette has a single brand accent.
- The existing `.section h2::after` gradient (`--accent` → `--accent-2`) becomes a solid `--primary` fill. A single-colour mark is called out in the logo foundation decisions — apply the same principle here.
- The existing `.button { background: #111 }` becomes `background: var(--primary); color: white` — brand button, passes AAA (7.7:1).

## Source of truth

The decisions behind these values live in `projects/incubating/async-digital-brand-foundation.md` in the knowledge vault. If a value needs to change, update that note first, then update this file and open follow-up PRs for any downstream brand surfaces.

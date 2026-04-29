# Async Digital — Positioning brief

An internal one-pager for anyone writing copy, decks, posts, or cold email on behalf of Async Digital. It answers one question: **how does each product live on its own subdomain while the apex stays company-level?**

If you're writing public copy and the answer isn't here, default to [`brand/voice.md`](voice.md).

## The problem in one paragraph

Async Digital Ltd builds a small portfolio of software for small businesses. As of 2026-04-29, two things ship: Speed to Lead (missed-call follow-up automation for dental clinics, sold per clinic) and Audient (a macOS app that uses on-device AI to transcribe and search audio and video, sold on the App Store). They have different customers, different price points, different sales motions. Each lives on its own subdomain (`speed-to-lead.async-digital.com`, `audient.async-digital.com`). The apex `async-digital.com` is the studio, not a product page. The risk is the studio collapsing back into "single-product landing with a promo band" because that's the gravity when one product (Speed to Lead) is the active sales focus.

## The position

**Async Digital is a UK studio that builds lean automation for small businesses. Each product lives on its own subdomain. The apex is the studio.**

That's it. The apex describes what kind of company Async Digital is and lists the products with parity. Each product subdomain owns its own pitch, voice register, and audience. The apex doesn't try to be either product's landing page.

## Where each surface speaks

| Surface | Voice | What it says |
|---|---|---|
| `async-digital.com` apex | Studio voice. Calm, lean, business. | "Software that saves your team time." Lists products with parity. Links to subdomains. Does not pitch either product. |
| `speed-to-lead.async-digital.com` | Clinic voice. Plain, specific, calm, clinical-adjacent. | Full Speed to Lead pitch. Owns the missed-call story. Does not mention Audient. |
| `audient.async-digital.com` | Knowledge-worker voice. Plain, more technical, faintly playful. | Full Audient pitch. Does not mention Speed to Lead. |
| Clinic pitch deck | Clinic voice. | Speed to Lead pitch. Optional one-slide Audient credibility note near the end. |
| Cold outreach to clinics | Clinic voice. | Speed to Lead only. |
| LinkedIn / press for clinic-side work | Clinic voice. | Optional one-line tag: *"the same team that builds Audient."* |
| LinkedIn / press for Audient | Knowledge-worker voice. | Audient as product. Don't cross-sell to clinics. |
| LinkedIn / press for Async Digital (the studio) | Studio voice. | Both products as portfolio. Apex is the link target. |

## Guardrails

- **Don't pitch Speed to Lead on the apex.** It has its own subdomain. The apex names it as a product, links out, and stops there.
- **Don't pitch Audient on the apex.** Same rule, same reason. The "Coming soon" eyebrow stays until launch but the framing is product-card-equal-weight, not below-the-fold credibility band.
- **Don't pitch Audient to clinics.** It isn't for them. A dental receptionist is not the target user for an on-device AI transcription tool.
- **Don't claim Audient is clinical or healthcare software.** It isn't. It doesn't touch patient data, it isn't GDPR-scoped in the same way, and no clinic uses it in production.
- **Don't list the products as "our services" on the apex.** They're products with their own subdomains, not menu items on an agency page. The apex distinction is studio (us) → products (links out), not service-line cards.
- **Don't spin Audient as "AI-powered transcription for dentistry".** There is no dental transcription product. Inventing one to bridge offerings collapses the credibility the brief is trying to protect.
- **Don't let one product's voice bleed into another's surface.** Each subdomain has its own register. The apex has the studio register. Mixing them flattens the distinction the structure is trying to make.

## How this plays with the voice guide

[`brand/voice.md`](voice.md) locks *how* Async Digital writes — plain, specific, calm. This brief locks *what* gets said where. Both apply to every surface. The studio voice on the apex is the same voice, scoped to the studio rather than a single product audience.

## What happens when a third thing ships

Same test, slightly extended for the umbrella shape:

1. **Does it fit one of the existing product audiences?** If yes, it folds into that subdomain (or extends it).
2. **Is it a new product with its own audience?** If yes, it gets its own subdomain (`<thing>.async-digital.com`) and joins the apex products list with parity.
3. **Is it not a product at all** (a service offering, a recurring contract)? Decide before shipping whether it belongs on the apex (as a service-card) or in private sales material only. Default: keep it off public surfaces until there's proof of fit.

The brief gets revisited when the products list grows past four, or when one product retires.

## When in doubt

1. **Apex copy?** Studio voice. Don't pitch either product. Link out.
2. **Subdomain copy?** Product voice for that audience. Don't cross-sell.
3. **Internal pitch deck or sales call?** Use whichever product the prospect is buying. Optional one-line credibility tag for the other product if it strengthens the pitch.

If it still isn't clear, ask Rob before shipping. The cost of a stale positioning note is worse than a five-minute chat.

---

_Related: [`brand/voice.md`](voice.md) (how we write), `../BRAND.md` (brand index), `#89` (homepage umbrella refit epic), `#90` (apex refit + foundation sweep), `#91` (CY mirror), `#73` (closed — pre-subdomain reframe, superseded by #89)._

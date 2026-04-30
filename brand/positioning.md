# Async Digital — Positioning brief

An internal one-pager for anyone writing copy, decks, posts, or cold email on behalf of Async Digital. It answers one question: **how does the apex pitch the active offering (dental missed-call follow-up) while leaving room for sibling products on their own subdomains?**

If you're writing public copy and the answer isn't here, default to [`brand/voice.md`](voice.md).

## The problem in one paragraph

Async Digital Ltd is a UK studio that provides automation services. As of 2026-04-30, the active commercial focus is dental clinics: Speed to Lead is the offering being sold, with Helen running pitches to private dental clinics in Cardiff. A second product, Audient (a macOS app that uses on-device AI to transcribe and search audio and video), ships on the App Store but isn't the studio's commercial focus today and serves a different audience (knowledge workers). Each lives on its own subdomain (`speed-to-lead.async-digital.com`, `audient.async-digital.com`). The apex `async-digital.com` is the front door for the active offering — it leads with dental missed-call follow-up because that's what the studio sells today. Audient gets a secondary "also from us" mention so it doesn't disappear from the studio's identity, but it doesn't share apex weight with the active pitch.

## The position

**Async Digital is a UK studio that provides automation services. We help dental clinics capture and convert missed calls by building automated follow-up systems. Our other product, Audient, lives at its own subdomain.**

That's it. The apex anchors on the active offering — dental missed-call follow-up — because that's the commercial reality today. The Speed to Lead subdomain owns the depth of pitch (workflow detail, pricing pack, case-study material once it exists). The Audient subdomain owns the knowledge-worker pitch. The apex stays clean and dental-anchored; the secondary "also from Async Digital" mention links out to Audient without competing for headline weight.

This may shift when a third vertical or product reaches commercial focus. Until then, "active offering on the apex, sibling products linked out" is the rule.

## Where each surface speaks

| Surface | Voice | What it says |
|---|---|---|
| `async-digital.com` apex | Clinic voice. Plain, specific, dental-anchored. | "Missed-call follow-up for dental clinics." Pitches the active offering. Links primary CTA to `speed-to-lead.async-digital.com`. Secondary "Also from Async Digital" block names Audient and links out. |
| `speed-to-lead.async-digital.com` | Clinic voice. Plain, specific, calm, clinical-adjacent. | Full Speed to Lead pitch in depth (workflow, pricing pack, FAQs, customer pack). Does not mention Audient. |
| `audient.async-digital.com` | Knowledge-worker voice. Plain, more technical, faintly playful. | Full Audient pitch. Does not mention Speed to Lead. |
| Clinic pitch deck | Clinic voice. | Speed to Lead pitch. Optional one-slide Audient credibility note near the end. |
| Cold outreach to clinics | Clinic voice. | Speed to Lead only. |
| LinkedIn / press for clinic-side work | Clinic voice. | Optional one-line tag: *"the same team that builds Audient."* |
| LinkedIn / press for Audient | Knowledge-worker voice. | Audient as product. Don't cross-sell to clinics. |
| LinkedIn / press for Async Digital (the studio) | Studio voice. | The studio sentence ("UK studio that provides automation services") plus the active offering. Audient as sibling. |

## Guardrails

- **The apex pitches the active offering.** Today that's dental missed-call follow-up via Speed to Lead. The H1 names the customer, the problem, and the outcome. The primary CTA routes to `speed-to-lead.async-digital.com`.
- **Audient stays secondary on the apex.** A small "Also from Async Digital" block, a one-line description, a link out. Not a co-equal product card; not a parity grid. Audient owns its subdomain; it doesn't compete for headline weight on the apex.
- **Don't pitch Audient to clinics.** It isn't for them. A dental receptionist is not the target user for an on-device AI transcription tool.
- **Don't claim Audient is clinical or healthcare software.** It isn't. It doesn't touch patient data, it isn't GDPR-scoped in the same way, and no clinic uses it in production.
- **Don't spin Audient as "AI-powered transcription for dentistry".** There is no dental transcription product. Inventing one to bridge offerings collapses the credibility the brief is trying to protect.
- **Don't claim Speed to Lead is AI-powered.** It runs on n8n + Cal.com + Twilio. It's automation, not AI. Calling it AI-powered is unsubstantiated under ASA / CMA "AI-washing" rules and conflates the two products. AI is named only on Audient surfaces.
- **Don't let one product's voice bleed into another's surface.** Each subdomain has its own register. The apex carries the clinic voice today (because the active offering is for clinics). Mixing registers flattens the distinction the structure is trying to make.
- **Don't add trust-band testimonials, "trusted by N clinics", or "live in Cardiff" claims** until a paying clinic exists. The pre-launch overclaim guard applies on every surface. Operating-location language ("Cardiff-based") is fine; "live in Cardiff" is not.

## How this plays with the voice guide

[`brand/voice.md`](voice.md) locks *how* Async Digital writes — plain, specific, calm. This brief locks *what* gets said where. Both apply to every surface. The clinic voice on the apex is the same voice as on `speed-to-lead.async-digital.com`, scoped to the active offering rather than the deeper pitch.

## What happens when a third thing ships

The same test, slightly extended:

1. **Does it fit the active offering's audience (dental clinics)?** If yes, it folds into Speed to Lead's subdomain or extends the apex pitch.
2. **Does it serve a different audience but share the studio's identity?** If yes, it gets its own subdomain (`<thing>.async-digital.com`) and joins Audient as a "also from Async Digital" sibling on the apex — secondary, linked out.
3. **Does it become the studio's new commercial focus?** That's a re-positioning event. Update this brief; the apex anchor moves to the new active offering.
4. **Is it not a product at all** (a service offering, a recurring contract)? Decide before shipping whether it belongs on the apex (as part of the active-offering pitch) or in private sales material only. Default: keep it off public surfaces until there's proof of fit.

The brief gets revisited when a second vertical reaches commercial parity, when a sibling product moves to apex-focus, or when the products list grows past four.

## When in doubt

1. **Apex copy?** Clinic voice. Lead with the active offering (dental missed-call follow-up). Audient stays in the secondary block.
2. **Subdomain copy?** Product voice for that audience. Don't cross-sell.
3. **Internal pitch deck or sales call?** Use whichever product the prospect is buying. Optional one-line credibility tag for the other product if it strengthens the pitch.

If it still isn't clear, ask Rob before shipping. The cost of a stale positioning note is worse than a five-minute chat.

---

_Related: [`brand/voice.md`](voice.md) (how we write), `../BRAND.md` (brand index), `#89` (homepage umbrella refit, superseded), `#90` (apex refit + foundation sweep, superseded), the dental-first apex refit replaces both._

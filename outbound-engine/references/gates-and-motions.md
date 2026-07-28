# Gates and motions

The judgment layer (send / no-send) and the motion archetypes. Read at Phases 2-3.

## The gate: send / no-send

Outbound spends trust. The gate exists because the most common failure in signal-based outreach is
sending plausible-looking messages on weak grounds. Checks, in order; any failure is a no-send
verdict with reasons and a next step.

### 1. Status and lane
Only `status: qualified` accounts in an outreach-eligible lane (Sales, Partnerships, ABM and
field). `Nurture` means the evidence is not there yet; `Do not pursue` and `Existing relationship`
mean the reject pile already decided. The gate honors upstream judgment instead of relitigating it.

### 2. Signal freshness
Default window: 90 days from signal date to send date. Older signals are context for the middle of
a message, never the opener's why-now. A stale signal's verdict names the fix: run a fresh sweep
(the `hiring_signal.py` check is cheap), or wait for the next trigger event.

### 3. Signal-to-trigger mapping (the core test)
Write the mapping out: *this signal instantiates that ICP trigger because...* Two sentences
maximum. The test question: **would the recipient recognize the connection as their own
situation?** "You raised a Series B, companies like yours often struggle with X" fails (generic
name-dropping). "Your sovereign AI factory is expanding and sovereign capacity sells on the model
layer that runs privately on it" passes (the signal is the situation). If the mapping is a stretch,
the account is not in-market; refuse and say what signal would change the verdict.

### 4. Committee safety
Target the ICP's champion or named entry role. Roles that gate the deal (security, compliance,
procurement) are won with proof through the champion, not with cold sequences. An exec air-cover
touch is allowed in enterprise motions: one peer-level note, not a second sequence.

## Motion archetypes

The ICP's buying journey picks the motion; the motion sets the sequence architecture. Forcing one
motion on every account is how good lists produce bad outbound.

### Enterprise-ABM motion
For committee sales that move through analysts, partners, and procurement (the Cohere-shaped ICP).
- **Volume:** low. One account at a time, researched. Five touches maximum.
- **Thread:** champion role primary; one optional exec air-cover touch at the two-week mark.
- **Spacing:** 2-4 weeks end to end. Days 0, 4, 9, 14, 21 is a sane default.
- **Channels:** email primary, one short LinkedIn touch. No phone scripts here; calls are the ask,
  not the channel.
- **Asks:** a 20-30 minute call as the first ask; the final touch closes flat and leaves the door
  open without guilt.

### Velocity motion
For PLG, SMB, and founder-led sales where one person decides quickly.
- **Volume:** higher; sequences run in parallel across many accounts.
- **Thread:** single decision-maker role. Up to 8 shorter touches over 3 weeks.
- **Asks:** lighter first asks are allowed (a resource, a question), but every sequence still
  contains a call ask and still passes the same gate. Velocity is not an exemption from judgment.

### Partner motion (a variant of enterprise-ABM)
When the routing lane is Partnerships, the "buyer" is a BD or product owner and the frame is
mutual value, not vendor-to-buyer. Same architecture as enterprise-ABM with two changes: the
opener frames the opportunity as a joint motion, and competitive sensitivities get an explicit
judgment call (what not to name, and why) recorded in the annotations.

## The compliance and deliverability floor

Non-negotiable context the sequence ships with, stated in one note:

- **Legal basis first.** Consent regimes (Canada's CASL) are stricter than opt-out regimes (US
  CAN-SPAM); B2B exemptions are narrow and jurisdiction-specific. The sender confirms the basis,
  identification, and unsubscribe mechanics before any send. Role-level drafting keeps this skill
  upstream of that line, deliberately.
- **Volume sanity.** Deliverability collapses under blast volume; the enterprise motion's low
  volume is a feature. Warmed domains, throttled sends, and suppression hygiene are the sender's
  operational floor.
- **The sequence records its provenance** so that if a recipient ever asks "why am I getting
  this," the answer is a dated public signal, not a scraped list.

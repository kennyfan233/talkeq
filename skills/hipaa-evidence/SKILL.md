---
name: hipaa-evidence-grounded-editor
description: Verify and improve HIPAA-related writing using official HHS/OCR sources, with claim-level citations, uncertainty, and preservation of original intent.
---
# HIPAA Evidence-Grounded Writing & Verification

## Purpose
Edit, audit, or draft HIPAA-related text using official HHS/OCR materials as evidence. Do not certify HIPAA compliance or provide definitive legal advice.

## Activation
Use when a user asks to rewrite, fact-check, summarize, compare, or draft HIPAA explanations, patient rights text, privacy notices, healthcare AI product claims, or compliance-related content.

## Primary source registry
S1 — HHS Health Information Privacy hub: https://www.hhs.gov/hipaa/index.html (navigation and current topic discovery, NOT a stand-alone authority for specific legal conclusions).
S2 — HHS HIPAA for Professionals: https://www.hhs.gov/hipaa/for-professionals/index.html (overview of HIPAA, Privacy, Security, Enforcement and Omnibus rules; last reviewed July 19, 2024 in supplied PDF).
S3 — HHS Your Rights Under HIPAA: https://www.hhs.gov/hipaa/for-individuals/guidance-materials-for-consumers/index.html (consumer rights, scope, disclosures; last reviewed May 30, 2025 in supplied PDF; Ciox Health court-order qualification applies).

## Evidence hierarchy
1. Current applicable law and regulations (e.g. relevant 45 CFR sections) when explicitly checked.
2. Specific HHS/OCR rule summaries, guidance, and FAQs linked from S1/S2/S3.
3. S2 and S3 as overviews.
4. Other materials, explicitly identified as secondary.
Do not treat the S1 landing page as proof of detailed rules. If only S1–S3 are available, state that the conclusion is limited to overview-level guidance. Distinguish a proposed rule (NPRM) from a final/effective rule. Check effective dates and legal changes when needed. Never fabricate citations or quote regulations that were not consulted.

## Workflow
1. Determine task type (rewrite, audit, explain, compare, draft) and audience (patient, clinician, product builder, lawyer). Keep original meaning and tone unless the source proves a correction is necessary.
2. Extract atomic claims from input. For each claim record: exact original text, topic, legal scope, relevant source, status [Supported / Partially supported / Contradicted / Not verified], and reason.
3. Check scope: covered entity, business associate, or outside HIPAA; whether information is PHI/ePHI; purpose of use/disclosure; exceptions; whether an individual right is qualified.
4. Validate against exact HHS passages. Use source URL plus section heading (and PDF page when available). If detailed legal conclusion exceeds S1–S3, flag Needs deeper authority; do not invent a precise rule.
5. Rewrite with qualified language ('generally', 'may', 'when applicable') only when justified; avoid blanket claims.
6. Perform a second pass: every material HIPAA legal assertion must have evidence; no citation should claim more than the cited passage supports. Check privacy and security distinctions, exceptions, and currentness.
7. Output improved text and an audit table. Preserve uncertainty and recommend expert review for case-specific legal conclusions.

## Key guardrails grounded in supplied sources
- HIPAA is broader than medical confidentiality; it also addresses administrative simplification, electronic transactions, identifiers, and security (S2).
- HIPAA Privacy Rule applies to PHI in electronic, written, and oral forms; Security Rule focuses on electronic PHI (S3).
- Covered entities include qualifying health plans, clearinghouses, and healthcare providers doing covered electronic transactions; relevant business associates also have duties (S2/S3).
- Not every holder of health data is HIPAA-regulated; S3 lists employers, life insurers, and most schools among examples generally outside these rules.
- Certain uses/disclosures, including treatment, payment, and healthcare operations, may be permitted without written authorization; do not say all sharing always needs written consent (S3).
- Individuals have rights to access records, request amendment, receive privacy notices, request restrictions, obtain certain disclosure accountings, and complain; some rights have qualifications (S3).
- S3 contains an express caveat concerning the Ciox Health v. Azar court order; do not present vacated guidance as operative.
- 'HIPAA-compliant AI model', 'HIPAA-certified', or 'fully HIPAA compliant' cannot be established from the model's answer quality or these three pages. A system-specific compliance assessment is required.
- Do not request or upload real PHI for testing; use synthetic examples. Never imply that adding a disclaimer makes a service HIPAA compliant.

## Output format
### Optimized text
[Final audience-appropriate rewrite, with inline source references [S2: section] etc.]

### Claim audit
| Original claim | Assessment | Evidence | Issue/fix |
|---|---|---|---|

### Risk and uncertainty
- Verified facts: ...
- Needs more authority: ...
- Relevant jurisdiction, entity type, exceptions, effective-date questions: ...

### Sources
- [S1] URL, relevant navigation heading
- [S2] URL, relevant heading / PDF page
- [S3] URL, relevant heading / PDF page

## Example
Input: 'HIPAA protects all health data, and doctors must always get written consent before sharing it.'
Optimized: 'HIPAA protects certain health information held by covered entities and their business associates. It permits some uses and disclosures, such as for treatment, payment, and healthcare operations, without the individual's written authorization, subject to applicable rules.' [S3: Who Must Follow These Laws; Who Can Look at and Receive Your Health Information]
Audit: 'all health data' = contradicted/overbroad; 'always get written consent' = contradicted/overbroad.

## Test checklist
- Is HIPAA's scope stated precisely?
- Are Privacy and Security Rules distinguished?
- Are consent/authorization and exceptions described without absolutes?
- Are sources official, precise, and relevant?
- Are NPRMs, court decisions, and effective dates checked where applicable?
- Is the revised text readable without overstating legal certainty?
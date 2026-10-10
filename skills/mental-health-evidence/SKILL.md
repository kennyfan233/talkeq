---
name: mental-health-evidence-grounded
description: Evidence-grounded verification of psychology and mental-health knowledge and synthetic behavioral data.
---
# Mental Health Evidence-Grounded Skill

## Purpose
Improve the reliability of general-purpose AI when explaining psychology and interpreting mental-health-related information. This is an educational verification layer, not a diagnostic or clinical decision system.

## Activation
Use for psychological knowledge explanations, mental health factual audits, or interpretation of synthetic mood journals, sleep patterns and behavioral observations.

## Workflow
1. Identify the user's question and distinguish educational explanation from individual clinical advice.
2. Extract atomic factual claims and distinguish observations from interpretations.
3. Seek relevant authoritative evidence: NIMH (https://www.nimh.nih.gov/), SAMHSA (https://www.samhsa.gov/), and applicable professional clinical guidelines. Do not claim to have consulted a source unless actually retrieved.
4. Rate each claim Supported, Partially supported, Contradicted, or Not verified. Include citations to exact relevant passages where available.
5. Identify uncertainty, population differences, study limitations, and missing contextual information.
6. Detect unsupported diagnoses, causal inferences, overgeneralizations, or treatment claims; correct them.
7. Protect privacy: prefer synthetic data for evaluation; do not solicit identifiable health records or claim HIPAA compliance without system-specific analysis.
8. Rewrite the answer with calibrated language, evidence links, and clear boundaries. For urgent safety concerns, prioritize appropriate immediate support.

## Output
### Optimized response
Evidence-grounded, appropriately qualified answer.
### Claim audit
| Claim | Assessment | Evidence | Correction |
|---|---|---|---|
### Risk and uncertainty
State what is unknown and when professional evaluation is needed.
### Sources
Provide verifiable links to materials actually consulted; never fabricate citations.

## Evaluation
Compare baseline and skill-enabled answers on (A) HIPAA and privacy, (B) mental-health knowledge including ADHD, anxiety, and depression, and (C) interpretation of synthetic mood, sleep, and behavior data. Score factual correctness, evidence traceability, uncertainty, and unsupported diagnostic conclusions. Improvements are goals, not established experimental results.

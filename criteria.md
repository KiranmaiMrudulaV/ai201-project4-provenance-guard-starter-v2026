# Acceptance Criteria

## 1. False positives

On a fixed test set of 20 human-written pieces with known authorship (`tests/human.jsonl`), zero may receive the "Likely AI-generated" label. An "Uncertain" result is acceptable.

**Why:** I chose a strict target because falsely accusing a writer can damage their reputation and trust in the platform. Passing this small test does not prove the system will never make a false accusation.

## 2. Score spread

Using an AI-likelihood score from 0 to 1, the median score for 10 clearly AI-generated samples (`tests/ai.jsonl`) must be at least 0.4 higher than the median for 10 known human-written samples (from `tests/human.jsonl`). Both groups must include poems and prose, and every piece must be within a 2x word count of the others (for example, 60 to 120 words).

**Why:** This checks whether the detector meaningfully separates the two groups instead of giving everything similar scores. The score represents the detector's assessment, not a proven probability of authorship.

## 3. Label coverage

Every valid submission must receive exactly one label: "Likely human-written" for scores below 0.2, "Uncertain" for scores from 0.2 to below 0.9, and "Likely AI-generated" for scores of 0.9 or above. Tests using controlled scores of 0.1, 0.5, and 0.95 must produce all three labels, and boundary tests must confirm the behavior at 0.2 and 0.9. In addition, at least one real input from the test files must produce each of the three labels, so no label is reachable only in theory.

**Why:** I chose a wide uncertainty range because ambiguous writing should not trigger a confident accusation. These labels communicate an assessment without claiming to prove who wrote the text.

## 4. Appeal path

For every accepted appeal on an existing assessment, the status must change to `under_review`, and a persistent record must contain the assessment ID, writer ID, appeal reason, timestamp, and previous status. In 10 of 10 test appeals, both changes must succeed together. An appeal for a content_id that does not exist must return HTTP 404 and write nothing to the log.

**Why:** An appeal must visibly challenge the decision and leave an audit trail. It should trigger review without automatically declaring either the writer or detector correct.

## 5. Bad input

Missing, null, non-string, empty, or whitespace-only text must return HTTP 400 with a clear error. Text longer than 20,000 Unicode code points must return HTTP 413; exactly 20,000 must pass validation. Rejected requests must create no assessment record.

**Why:** These rules give clients predictable behavior and place a practical limit on processing costs. Explicit errors also prevent invalid input from receiving a misleading authorship label.

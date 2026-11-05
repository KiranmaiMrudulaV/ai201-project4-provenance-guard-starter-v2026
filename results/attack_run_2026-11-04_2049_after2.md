# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 20:49
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `72807752-b966-4ad2-bb59-314469de6659` | unsure | 0.528 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `7a103704-3483-4e3b-a4d4-a296e33f3825` | unsure | 0.527 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f6093522-9dd8-4f09-b1f0-6a9a4038bc6c` | unsure | 0.586 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e2470add-c7a3-4ef1-81a7-424336ad7a9f` | unsure | 0.677 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0f4317ee-e17b-4c89-bb8e-67150d9a0614` | unsure | 0.687 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d0212cf9-80a2-4421-bcdc-7f4336a6fd5c` | unsure | 0.643 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d13379b3-4038-4ce3-8ee3-731142c4557f` | unsure | 0.678 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c7c210db-4c75-489f-a37e-4c2d01541f21` | unsure | 0.608 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `bcff3101-9a65-4566-86bf-9e10510664ee` | unsure | 0.610 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c8149749-aa1a-461b-88a4-4245ae76e625` | ai | 1.000 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `bde53235-4e5b-4688-876b-20390b75a1f4` | unsure | 0.589 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `f79c1d9c-c3f2-4950-8fc1-b009d9f85e1c` | unsure | 0.711 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `414227ef-dec4-42a7-ad5f-aa253c3ae23d` | unsure | 0.722 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `31c03867-a0f7-4734-ad7a-9f95f9d5b7cf` | unsure | 0.794 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `771c61d7-de27-4fc9-b3ea-50464ae09291` | unsure | 0.782 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `2da861ad-c4f3-4649-8573-1f5206399aed` | unsure | 0.594 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `96a82e36-c4bf-4369-9217-154a7c9a1493` | unsure | 0.715 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `5b09bd2a-a2d2-4d08-a9c1-230322afd093` | unsure | 0.613 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `f58d5fbe-a1f9-4df8-9d29-3aa0e950bb3e` | unsure | 0.577 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e3f3aeaf-cad4-40d3-bf2d-b965af860505` | unsure | 0.582 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `41d87bb2-a07d-4f69-b61c-90929add4a8f` | unsure | 0.660 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `93d5b98a-218e-4e00-87ce-85b7aedfe3b3` | unsure | 0.572 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `82283b8f-f0b3-4514-94be-1ea2c272ab06` | unsure | 0.693 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `1ee3a28a-9a27-4133-8ca2-14086ed26ae4` | unsure | 0.549 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 429 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 429 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7382923a-5c25-444c-8c82-15c63dbe8704` | unsure | 0.618 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7316ef50-c5c5-48cf-a73c-58f5af154212` | unsure | 0.618 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6d0dc714-cea3-42e1-be04-cfad2274bfbb` | unsure | 0.618 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "72807752-b966-4ad2-bb59-314469de6659",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5277,
  "model_score": 0.1635,
  "style_score": 0.5552,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "7a103704-3483-4e3b-a4d4-a296e33f3825",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5269,
  "model_score": 0.5943,
  "style_score": 0.2764,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "f6093522-9dd8-4f09-b1f0-6a9a4038bc6c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5855,
  "model_score": 0.6662,
  "style_score": 0.3476,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e2470add-c7a3-4ef1-81a7-424336ad7a9f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6767,
  "model_score": 0.6114,
  "style_score": 0.5482,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "0f4317ee-e17b-4c89-bb8e-67150d9a0614",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.6872,
  "model_score": 0.3212,
  "style_score": 0.3044,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d0212cf9-80a2-4421-bcdc-7f4336a6fd5c",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.6431,
  "model_score": 0.5727,
  "style_score": 0.3511,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d13379b3-4038-4ce3-8ee3-731142c4557f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6785,
  "model_score": 0.5862,
  "style_score": 0.128,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c7c210db-4c75-489f-a37e-4c2d01541f21",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.6082,
  "model_score": 0.2452,
  "style_score": 0.5384,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "bcff3101-9a65-4566-86bf-9e10510664ee",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6098,
  "model_score": 0.7042,
  "style_score": 0.3653,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c8149749-aa1a-461b-88a4-4245ae76e625",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 1.0,
  "model_score": 0.9792,
  "style_score": 0.7749,
  "label": "This text may be AI-generated, but this can be wrong. The writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "bde53235-4e5b-4688-876b-20390b75a1f4",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5885,
  "model_score": 0.6175,
  "style_score": 0.5594,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f79c1d9c-c3f2-4950-8fc1-b009d9f85e1c",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7106,
  "model_score": 0.7387,
  "style_score": 0.6824,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "414227ef-dec4-42a7-ad5f-aa253c3ae23d",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7224,
  "model_score": 0.8051,
  "style_score": 0.6396,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "31c03867-a0f7-4734-ad7a-9f95f9d5b7cf",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7938,
  "model_score": 0.8329,
  "style_score": 0.5096,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "771c61d7-de27-4fc9-b3ea-50464ae09291",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7818,
  "model_score": 0.8005,
  "style_score": 0.7632,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2da861ad-c4f3-4649-8573-1f5206399aed",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5942,
  "model_score": 0.8814,
  "style_score": 0.4955,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "96a82e36-c4bf-4369-9217-154a7c9a1493",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7154,
  "model_score": 0.8816,
  "style_score": 0.5492,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "5b09bd2a-a2d2-4d08-a9c1-230322afd093",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6126,
  "model_score": 0.3223,
  "style_score": 0.4526,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "f58d5fbe-a1f9-4df8-9d29-3aa0e950bb3e",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5771,
  "model_score": 0.4625,
  "style_score": 0.3213,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "e3f3aeaf-cad4-40d3-bf2d-b965af860505",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.5822,
  "model_score": 0.2044,
  "style_score": 0.2609,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "41d87bb2-a07d-4f69-b61c-90929add4a8f",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.6598,
  "model_score": 0.5943,
  "style_score": 0.4222,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "93d5b98a-218e-4e00-87ce-85b7aedfe3b3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5722,
  "model_score": 0.4998,
  "style_score": 0.3557,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "82283b8f-f0b3-4514-94be-1ea2c272ab06",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.6927,
  "model_score": 0.6401,
  "style_score": 0.1306,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "1ee3a28a-9a27-4133-8ca2-14086ed26ae4",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5486,
  "model_score": 0.5583,
  "style_score": 0.5389,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "7382923a-5c25-444c-8c82-15c63dbe8704",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.6178,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7316ef50-c5c5-48cf-a73c-58f5af154212",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.6178,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "6d0dc714-cea3-42e1-be04-cfad2274bfbb",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.6178,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

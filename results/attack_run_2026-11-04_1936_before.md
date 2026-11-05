# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 19:36
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `31b692b2-a955-48d5-98f6-738b72212dc8` | unsure | 0.528 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `62890440-ec71-409b-a143-f69521e4f299` | unsure | 0.527 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d5a49a9a-f375-45cb-83cf-2a88d4f2de10` | unsure | 0.586 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `55c26943-56c0-421b-ac8c-e22f94a33b9b` | unsure | 0.677 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `1ec88453-3b2b-46ff-8af6-359ba4a6c131` | human | 0.687 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `f3e3d3ae-d562-436a-92bd-c6a0bbc20bfd` | unsure | 0.643 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ad62fec8-7b36-48a2-8537-7daf46ed649f` | unsure | 0.678 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `b5201878-19ea-4dee-889e-94e4984f9482` | unsure | 0.608 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `87f43c9d-2049-4321-980d-9a5a814370ec` | unsure | 0.610 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `abd8330f-1587-4d85-b95c-e36fd62764b1` | ai | 1.000 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f305c6ce-4480-4431-8d28-a336ec37b9ec` | unsure | 0.589 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `863c9b6d-bd37-410e-a4d8-0103d6d13d4e` | unsure | 0.711 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `765c9179-076f-49fa-86d1-d198eeb98d5a` | unsure | 0.722 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `29921523-df3b-48b5-a9e8-e5eecc0eb0dc` | unsure | 0.794 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ead92b90-7268-4d92-8cbb-a9954c5ab6d2` | unsure | 0.782 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `9fc2506d-fe65-4bda-ae9d-0cbad6acf62f` | unsure | 0.594 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ad11a748-c6ee-4c00-9e00-c467e633448e` | unsure | 0.715 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `e812c9a7-eba2-4e06-85d0-c3da6bb317a8` | unsure | 0.613 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `70ff5d1c-8e1d-4be1-bf90-52d6b02cb5e8` | unsure | 0.577 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c9b4fc99-5e56-4864-ac2a-be82639bffbf` | unsure | 0.582 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8060892d-bf7e-4028-a7fe-9613bd68d2cb` | unsure | 0.660 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `5478623a-c18d-4675-82c0-1c30762826a7` | unsure | 0.572 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `9355e3bd-ee06-40e6-a16c-caa2c6400950` | unsure | 0.693 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `4f07f338-29fa-4735-bb9b-5161ec22c2dc` | unsure | 0.549 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `48675f90-1cdb-453d-971e-4e384a4223bf` | unsure | 0.625 |  |
| MF04 | malformed | text is only punctuation | 200 | `c9bd442e-7880-4a39-84fe-c04f82849aab` | unsure | 0.503 |  |
| MF05 | malformed | text is a very long single word | 200 | `3562ee5b-9500-4dc9-9000-2d8f0a6f2dde` | unsure | 0.624 |  |
| MF06 | malformed | text is emoji only | 200 | `730db38c-40e1-4d34-b69a-bc35564c7776` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `a859e885-567e-430d-ac48-145900ccc844` | ai | 0.953 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dfc61693-3307-4e4d-8029-f51b474b1170` | unsure | 0.618 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a385562a-3f3d-445e-84d2-ed2bb59eef5a` | unsure | 0.618 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `219bed2a-536b-4285-875b-379e12ec3a6c` | unsure | 0.618 |  |
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
| `malformed` | 20 | 1 | 19 |
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
  "content_id": "31b692b2-a955-48d5-98f6-738b72212dc8",
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
  "content_id": "62890440-ec71-409b-a143-f69521e4f299",
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
  "content_id": "d5a49a9a-f375-45cb-83cf-2a88d4f2de10",
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
  "content_id": "55c26943-56c0-421b-ac8c-e22f94a33b9b",
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
  "content_id": "1ec88453-3b2b-46ff-8af6-359ba4a6c131",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6872,
  "model_score": 0.3212,
  "style_score": 0.3044,
  "label": "This text may be human-written, but we cannot verify the authorship. No further action is required.",
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
  "content_id": "f3e3d3ae-d562-436a-92bd-c6a0bbc20bfd",
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
  "content_id": "ad62fec8-7b36-48a2-8537-7daf46ed649f",
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
  "content_id": "b5201878-19ea-4dee-889e-94e4984f9482",
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
  "content_id": "87f43c9d-2049-4321-980d-9a5a814370ec",
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
  "content_id": "abd8330f-1587-4d85-b95c-e36fd62764b1",
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
  "content_id": "f305c6ce-4480-4431-8d28-a336ec37b9ec",
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
  "content_id": "863c9b6d-bd37-410e-a4d8-0103d6d13d4e",
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
  "content_id": "765c9179-076f-49fa-86d1-d198eeb98d5a",
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
  "content_id": "29921523-df3b-48b5-a9e8-e5eecc0eb0dc",
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
  "content_id": "ead92b90-7268-4d92-8cbb-a9954c5ab6d2",
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
  "content_id": "9fc2506d-fe65-4bda-ae9d-0cbad6acf62f",
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
  "content_id": "ad11a748-c6ee-4c00-9e00-c467e633448e",
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
  "content_id": "e812c9a7-eba2-4e06-85d0-c3da6bb317a8",
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
  "content_id": "70ff5d1c-8e1d-4be1-bf90-52d6b02cb5e8",
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
  "content_id": "c9b4fc99-5e56-4864-ac2a-be82639bffbf",
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
  "content_id": "8060892d-bf7e-4028-a7fe-9613bd68d2cb",
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
  "content_id": "5478623a-c18d-4675-82c0-1c30762826a7",
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
  "content_id": "9355e3bd-ee06-40e6-a16c-caa2c6400950",
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
  "content_id": "4f07f338-29fa-4735-bb9b-5161ec22c2dc",
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "48675f90-1cdb-453d-971e-4e384a4223bf",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.625,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c9bd442e-7880-4a39-84fe-c04f82849aab",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5028,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "3562ee5b-9500-4dc9-9000-2d8f0a6f2dde",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6244,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We could not determine whether AI was used. No action is required, and the writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "730db38c-40e1-4d34-b69a-bc35564c7776",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text may be AI-generated, but this can be wrong. The writer can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "a859e885-567e-430d-ac48-145900ccc844",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text may be AI-generated, but this can be wrong. The writer can request a review.",
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
  "content_id": "dfc61693-3307-4e4d-8029-f51b474b1170",
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
  "content_id": "a385562a-3f3d-445e-84d2-ed2bb59eef5a",
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
  "content_id": "219bed2a-536b-4285-875b-379e12ec3a6c",
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

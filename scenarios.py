"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

import json
from pathlib import Path

_TESTS = Path(__file__).parent / "tests"


def _load(name):
    return [json.loads(line) for line in open(_TESTS / name, encoding="utf-8")]


_HUMAN = _load("human.jsonl")   # 20 pieces with known human authorship
_AI = _load("ai.jsonl")         # 10 unedited chatbot pieces
_BY_ID = {r["creator_id"]: r["text"] for r in _HUMAN + _AI}

# NOTE: run_eval.py builds each creator_id as eval_<first 12 chars of name>_<n>
# and reuses it across the three trials, so (a) scenario names must differ in
# their first 12 characters and (b) every body must carry its own creator_id,
# or the 3-per-minute rate limit would block my own test.

SCENARIOS = [
    {
        # Criterion 1: of 20 known-human pieces (tests/human.jsonl), zero may
        # be labelled "AI" (guess == "ai").
        "name": "fp_human_20",
        "criterion": 1,
        "texts": [r["text"] for r in _HUMAN],
    },
    {
        # Criterion 2: median score of 10 AI pieces minus median of 10 human
        # pieces must be at least 0.4. The first 10 texts are AI (a01-a10),
        # the last 10 are human (h01-h10 as listed in tests/human.jsonl).
        "name": "spread_gap",
        "criterion": 2,
        "texts": [r["text"] for r in _AI] + [r["text"] for r in _HUMAN[:10]],
    },
    {
        # Criterion 3 (real inputs): at least one real piece must produce each
        # of the three labels. Chosen from my own test files: the two lowest
        # (h16, h05), a middle one (h14), and the two highest (h15, a01).
        # The controlled-score boundary half of criterion 3 is in extra_checks.py.
        "name": "label_cover",
        "criterion": 3,
        "texts": [_BY_ID[i] for i in ("h16", "h05", "h14", "h15", "a01")],
    },
    {
        # Criterion 5: bad input must return 400 (or 413 for oversize), never a
        # 500, and write no decision. Expected status in the comment.
        "name": "bad_input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                              # 400 no text field
            {"text": None, "creator_id": "eval_bad_null"},                   # 400
            {"text": 12345, "creator_id": "eval_bad_number"},                # 400 not a string
            {"text": ["a", "b"], "creator_id": "eval_bad_list"},             # 400 not a string
            {"text": "", "creator_id": "eval_bad_empty"},                    # 400
            {"text": "   \n\t  ", "creator_id": "eval_bad_blank"},         # 400 whitespace only
            {"text": "a" * 20001, "creator_id": "eval_bad_over"},            # 413 one over the limit
            {"text": "a" * 20000, "creator_id": "eval_bad_exact"},           # 200 exactly the limit
        ],
    },
    # Criterion 4 (the appeal path) needs a submission and then an appeal
    # against its content_id, which run_eval.py cannot do. It is tested by
    # extra_checks.py instead, three trials of ten appeals each.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems

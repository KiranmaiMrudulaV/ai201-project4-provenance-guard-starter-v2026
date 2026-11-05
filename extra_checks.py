#!/usr/bin/env python3
"""
The two checks run_eval.py can't do.   <- UNIT 8, MILESTONE 3

    python app.py                                  # one terminal
    python extra_checks.py --label before          # another

Criterion 3, second half: controlled scores go straight into
scoring.score_to_label (0.1, 0.5, 0.95 and the boundaries at 0.2 and 0.9).

Criterion 4: ten appeals per trial, three trials. Each appeal must set the
status to under_review (read back through GET /content/<id>) and leave an
appeal entry in the log carrying the previous status. An appeal for a made-up
content_id must return 404 and add nothing to the log.
"""

import argparse
import datetime as dt
import json

import requests

import config
import scoring
from scenarios import _HUMAN

URL = f"http://{config.HOST}:{config.PORT}"


def controlled_scores():
    cases = [(0.1, "human"), (0.5, "unsure"), (0.95, "ai"),
             (0.199, "human"), (0.2, "unsure"), (0.899, "unsure"), (0.9, "ai")]
    rows = []
    for score, expected in cases:
        guess, _ = scoring.score_to_label(score)
        rows.append((score, expected, guess, "pass" if guess == expected else "FAIL"))
    return rows


def log_count():
    return requests.get(f"{URL}/log").json()["count"]


def appeal_trial(trial):
    ok = 0
    detail = []
    for i in range(1, 11):
        creator = f"appeal_t{trial}_{i:02d}"
        text = _HUMAN[i - 1]["text"]
        cid = requests.post(f"{URL}/submit", json={"text": text, "creator_id": creator}).json().get("content_id")
        resp = requests.post(f"{URL}/appeal", json={"content_id": cid, "reasoning": "I wrote this myself."})
        status = requests.get(f"{URL}/content/{cid}").json().get("status")
        entries = [e for e in requests.get(f"{URL}/log").json()["entries"]
                   if e.get("content_id") == cid and e.get("event") == "appeal"]
        passed = (resp.status_code == 200 and status == "under_review"
                  and len(entries) == 1 and entries[0].get("previous_status") == "decided")
        ok += passed
        detail.append((creator, resp.status_code, status, len(entries), "pass" if passed else "FAIL"))
    before = log_count()
    fake = requests.post(f"{URL}/appeal", json={"content_id": "does-not-exist", "reasoning": "x"})
    fake_ok = fake.status_code == 404 and log_count() == before
    return ok, fake.status_code, fake_ok, detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    out = [f"# Extra checks ({args.label or 'unlabelled'}) — {dt.datetime.now():%Y-%m-%d %H:%M}\n",
           "Produced by `extra_checks.py`. Thresholds in use: "
           f"human <= {config.HUMAN_THRESHOLD}, AI >= {config.AI_THRESHOLD}.\n",
           "## Criterion 3 — controlled scores\n", "| score | criterion says | got | |", "|---|---|---|---|"]
    rows = controlled_scores()
    for s, e, g, r in rows:
        out.append(f"| {s} | {e} | {g} | {r} |")
    print("controlled scores:", sum(r[3] == "pass" for r in rows), "of", len(rows), "pass")

    out += ["", "## Criterion 4 — appeals\n", "| trial | appeals that worked | unknown id returned | unknown id wrote nothing |", "|---|---|---|---|"]
    all_detail = []
    for trial in (1, 2, 3):
        ok, code, fake_ok, detail = appeal_trial(trial)
        print(f"trial {trial}: {ok}/10 appeals ok, unknown id -> {code}, nothing logged: {fake_ok}")
        out.append(f"| {trial} | {ok}/10 | {code} | {fake_ok} |")
        all_detail.append((trial, detail))

    out += ["", "## Per-appeal detail\n", "```json", json.dumps(
        [{"trial": t, "appeals": d} for t, d in all_detail], indent=1), "```"]
    config.RESULTS_DIR.mkdir(exist_ok=True)
    path = config.RESULTS_DIR / f"extra_{dt.datetime.now():%Y-%m-%d_%H%M}_{args.label or 'run'}.md"
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("Wrote", path)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Per-creator versus per-address rate limiting, measured.   <- UNIT 8 STRETCH

    python limit_modes.py                      # per-creator (the default)
    AI201_RATE_KEY=address python limit_modes.py   # per-address

Three abuse cases, each sending 10 requests against the 3-per-minute limit
through Flask's test client (no server needed). Signal one is stubbed with a
constant so this measures the limiter, not the model.

    A  one script, one address, a NEW creator_id on every request
    B  two writers sharing one address, 3 requests each (a household)
    C  one creator_id, a NEW address on every request
"""

import sys

import config
import detector

detector.model_signal = lambda text: 0.5  # the limiter is under test, not the model

import app  # noqa: E402  (imported after the stub so the route uses it)

TEXT = "This is a short piece of text with enough words to be scored properly."


def send(client, creator, addr):
    r = client.post("/submit", json={"text": TEXT, "creator_id": creator},
                    environ_overrides={"REMOTE_ADDR": addr})
    return r.status_code


def run(label, plan):
    client = app.app.test_client()
    codes = [send(client, c, a) for c, a in plan]
    print(f"{label}: {' '.join(str(c) for c in codes)}   ({codes.count(429)} blocked)")
    return codes


print(f"mode: {config.RATE_LIMIT_KEY}  ({config.RATE_LIMIT_PER_MINUTE}/min, {config.RATE_LIMIT_PER_DAY}/day)")
# Distinct names and addresses per case so the cases cannot share a counter.
run("A  rotating creator_id, one address ", [(f"a_{i}", "10.0.0.1") for i in range(10)])
run("B  two writers, one shared address  ", [("b_alice", "10.0.0.2")] * 3 + [("b_bob", "10.0.0.2")] * 3)
run("C  one creator, rotating addresses  ", [("c_one", f"10.0.1.{i}") for i in range(10)])
sys.exit(0)

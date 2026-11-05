# Rate-limit keying: per-creator vs per-address

Produced by `limit_modes.py` (3/min, 30/day, signal one stubbed).

```
mode: creator  (3/min, 30/day)
A  rotating creator_id, one address : 200 200 200 200 200 200 200 200 200 200   (0 blocked)
B  two writers, one shared address  : 200 200 200 200 200 200   (0 blocked)
C  one creator, rotating addresses  : 200 200 200 429 429 429 429 429 429 429   (7 blocked)
mode: address  (3/min, 30/day)
A  rotating creator_id, one address : 200 200 200 429 429 429 429 429 429 429   (7 blocked)
B  two writers, one shared address  : 200 200 200 429 429 429   (3 blocked)
C  one creator, rotating addresses  : 200 200 200 200 200 200 200 200 200 200   (0 blocked)
```

"""
Signal three: the phrase signal (stretch feature).

Signal one measures how predictable the text is. Signal two measures its shape.
This one measures its *vocabulary habits*: how many stock phrases that chatbots
overuse the text contains ("plays a pivotal role", "ultimately", "delve").

    python phrases.py "some text to look at"

The blind spot: it only knows the phrases on the list. A model told to avoid
them walks straight past it, and a human who writes formal, essay-style prose
(or learned English from textbooks) trips it. Poems and casual writing score
near zero whoever wrote them, so this signal can only ever argue for "AI".

The list was written from general knowledge of chatbot habits, not tuned on my
test pieces.
"""

import re

PHRASES = [
    "in today's", "ever-evolving", "rapidly evolving", "fast-paced",
    "plays a pivotal role", "plays a crucial role", "plays a significant role",
    "it is important to", "it is worth noting", "it's important to note",
    "delve", "tapestry", "testament to", "navigate", "landscape of",
    "foster", "embark", "unlock", "empower", "seamless", "holistic",
    "multifaceted", "realm of", "vibrant", "pivotal", "in conclusion",
    "furthermore", "moreover", "ultimately", "underscores", "harness",
    "cannot be overstated", "a wide range of", "leverage",
]

# Hits per 100 words at which a text reads as fully AI-like.
HITS_PER_100_AI = 3.0


def _normalize(text: str) -> str:
    return text.lower().replace("’", "'")


def phrase_hits(text: str) -> int:
    t = _normalize(text)
    return sum(t.count(p) for p in PHRASES)


def phrase_signal(text: str) -> float:
    """0–1, higher means more stock chatbot phrasing (more likely AI)."""
    n = len(re.findall(r"[a-z0-9']+", _normalize(text)))
    if n == 0:
        return 0.0
    density = phrase_hits(text) / n * 100
    return round(max(0.0, min(1.0, density / HITS_PER_100_AI)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "In today's fast-paced world, effective time management plays a pivotal "
        "role. Ultimately, it empowers people to navigate their goals."
    )
    print(f"phrase hits    {phrase_hits(text)}")
    print(f"phrase_signal  {phrase_signal(text)}   (higher = more likely AI)")

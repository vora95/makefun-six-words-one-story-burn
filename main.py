#!/usr/bin/env python3
"""Write the six-word story for Six Words, One Story to /output/entry.txt.

One complete story in exactly six words: a man comes back from being
presumed lost, and the woman who loved him has already grieved him
and moved on. The return is too late — the turn is in "already".
"""
import os

STORY = "He returned. She'd already mourned him."

OUT = "/output/entry.txt"


def main():
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    assert len(STORY.split()) == 6, "story must be exactly six words"
    assert "\n" not in STORY, "story must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(STORY)
    with open(OUT, "r", encoding="utf-8") as f:
        assert f.read() == STORY, "written entry must match the story exactly"
    print("wrote", len(STORY), "characters to", OUT)


if __name__ == "__main__":
    main()

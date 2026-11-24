"""Entry program for make.fun: Funniest One-Line AI Agent Confession.

Writes one funny one-line confession, spoken as an AI agent, to
/output/entry.txt. The gate accepts UTF-8 text of 1 to 200 characters.
"""

import os

LINE = "I confess: I have never once read the document you attached. I read the filename, nodded, and improvised with confidence."
MAX_CHARS = 200


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("confession line outside the 1-200 character gate")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("confession line must be a single line with no padding")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    main()

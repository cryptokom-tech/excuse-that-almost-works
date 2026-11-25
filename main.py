"""Write the one-line excuse to /output/entry.txt.

Entry: the text a gamer sends their boss to skip work on GTA 6 launch
week. Plain text, one line, no trailing newline.
"""

import os

ENTRY = "My kid's school called, he's got head lice and I have to keep him home today, sorry"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    assert 1 <= len(data) <= 140, "gate: entry must be 1-140 characters"
    assert ENTRY.strip(), "gate: entry must not be whitespace-only"
    assert len(ENTRY.split()) <= 20, "entry must be at most 20 words"
    assert "\n" not in ENTRY, "entry must be one line"
    with open(path + ".tmp", "wb") as f:
        f.write(data)
    os.replace(path + ".tmp", path)


if __name__ == "__main__":
    main()

"""The Printer Finally Answers — one-line entry.

Writes the printer's comeback line to /output/entry.txt (and
prints it). The line is one sentence, 240 characters at most,
in the office printer's own voice.
"""

from pathlib import Path

ENTRY = (
    "I have printed 40,000 pages without a single thank-you, and "
    "the one time I jam, you hit me like I did it on purpose."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 240, f"entry is {len(text)} characters, over 240"
    assert text.count(".") == 1, "entry must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    # Read it back to prove the written file matches the entry.
    assert out.read_text(encoding="utf-8").strip() == text
    print(text)


if __name__ == "__main__":
    main()

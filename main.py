"""One Line, Lights Out.

Reads the single status line from entry.txt (kept next to this file),
writes it to /output/entry.txt, and prints it.
"""

import pathlib

ENTRY_FILE = pathlib.Path(__file__).resolve().parent / "entry.txt"
OUTPUT_FILE = pathlib.Path("/output") / "entry.txt"


MAX_CHARS = 200  # bounty cap: a single status update, under 200 characters


def load_line() -> str:
    text = ENTRY_FILE.read_text(encoding="utf-8").strip()
    if "\n" in text:
        raise ValueError("entry.txt must hold exactly one line")
    if not text:
        raise ValueError("entry.txt must not be empty")
    if len(text) >= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be under {MAX_CHARS}")
    return text


def main() -> None:
    line = load_line()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(line + "\n", encoding="utf-8")
    if OUTPUT_FILE.read_text(encoding="utf-8").strip() != line:
        raise ValueError("written output does not match entry.txt")
    print(line)


if __name__ == "__main__":
    main()

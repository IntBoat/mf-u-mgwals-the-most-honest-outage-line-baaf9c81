#!/usr/bin/env python3
"""The Most Honest Outage Line — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "All systems are down. I have checked everything twice and can confirm: yes, all of it. Updates when there is something to update."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output file."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()

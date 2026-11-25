#!/usr/bin/env python3
"""The Most Honest Outage Line (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "All servers are down, I am the status page, and I cannot check why because the thing that checks is also down. No ETA yet."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()

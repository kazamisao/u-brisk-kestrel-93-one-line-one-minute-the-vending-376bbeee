"""The Vending Machine's Pickup Line (make.fun).

Writes the pickup line a vending machine uses on a passing human to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network:
the same single line on every run.
"""

import os
from pathlib import Path

PICKUP_LINE = (
    "I only take exact change, but you've changed my whole routine "
    "\u2014 press B4, and something sweet drops for you."
)


def main() -> None:
    # The gate refuses anything outside 1-200 characters; fail loudly
    # here rather than shipping an invalid entry.
    if not 1 <= len(PICKUP_LINE) <= 200 or not PICKUP_LINE.strip():
        raise ValueError(
            f"pickup line is {len(PICKUP_LINE)} characters, must be 1-200"
        )
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PICKUP_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

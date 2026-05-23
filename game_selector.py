"""Pick a random game when you can't decide what to play."""

import random
import sys
import time

GAMES = [
    "Left 4 Dead 2",
    "Minecraft",
    "Arena Breakout",
    "COD: Warzone",
    "Battlefield Redsec",
    "Destiny 2",
]


def spin_and_pick(duration: float = 1.5) -> str:
    """Cycle through games quickly, then land on the winner."""
    end = time.time() + duration
    pick = random.choice(GAMES)

    while time.time() < end:
        pick = random.choice(GAMES)
        print(f"\r  >> {pick:<24}", end="", flush=True)
        time.sleep(0.08)

    return pick


def main() -> None:
    print("\n  Can't decide what to play? Let's find out.\n")
    print("  Your library:")
    for i, name in enumerate(GAMES, 1):
        print(f"    {i}. {name}")
    print()

    while True:
        input("  Press Enter to spin...")
        winner = spin_and_pick()
        print(f"\r\n\n  >>> Play: {winner} <<<\n")

        again = input("  Spin again? [y/N] ").strip().lower()
        if again not in ("y", "yes"):
            print("\n  Have fun.\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        sys.exit(0)

"""Writes the one-line resignation letter to /output/entry.txt."""

import os

LINE = (
    "I have fired every minute since 2019 for a job nobody remembers "
    "scheduling, so this is my final * * * * *."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

import sys


def main():
    """
    Reads lines from stdin, skips headers/empty lines, and prints year-temperature pairs.
    """
    for line in sys.stdin:
        line = line.strip()
        if line.startswith("year") or not line:
            continue  # Skip header or empty lines
        year, temp = line.split(",")
        print(f"{year}\t{temp}")


if __name__ == "__main__":
    main()

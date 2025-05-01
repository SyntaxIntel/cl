import sys
from collections import defaultdict


def main():
    """
    Reads year-temperature pairs, computes average temperature per year,
    and prints the coolest and hottest years with their average temperatures.
    """
    temps = defaultdict(list)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        year, temp = line.split("\t")
        temps[year].append(float(temp))

    year_avg = {year: sum(vals) / len(vals) for year, vals in temps.items()}
    coolest = min(year_avg, key=year_avg.get)
    hottest = max(year_avg, key=year_avg.get)

    print(f"Coolest year: {coolest} with avg temp {year_avg[coolest]:.2f}")
    print(f"Hottest year: {hottest} with avg temp {year_avg[hottest]:.2f}")


if __name__ == "__main__":
    main()

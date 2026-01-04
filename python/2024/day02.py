# Part 1
from pathlib import Path

p_input = Path("data.txt").read_text()

reports = [[int(num) for num in report.split()] for report in p_input.splitlines()]


def check_report(report: list[int]) -> bool:
    return all(1 <= (x - y) <= 3 for x, y in zip(report[:-1], report[1:])) or all(
        1 <= (y - x) <= 3 for x, y in zip(report[:-1], report[1:])
    )


print(sum(map(check_report, reports)))

# Part 2
print(
    sum(
        any(check_report(report[:i] + report[i + 1 :]) for i in range(len(report)))
        for report in reports
    )
)

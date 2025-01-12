# Part 1
from functools import cache
from pathlib import Path

towels, designs = Path("data.txt").read_text().split("\n\n")
towels, designs = towels.split(", "), designs.splitlines()


@cache
def solve(design_todo: str) -> int:
    if not design_todo:
        return 1
    return sum(
        solve(design_todo.removeprefix(towel))
        for towel in towels
        if design_todo.startswith(towel)
    )


print(sum(map(bool, map(solve, designs))))

# Part 2
print(sum(map(solve, designs)))

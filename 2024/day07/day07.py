# Part 1
from pathlib import Path

p_input = [row.split(": ") for row in Path("data.txt").read_text().splitlines()]


def solve(equations: str, is_part2: bool) -> list[int]:
    start_value, *numbers = map(int, equations.split())
    solutions = [start_value]
    for num in numbers:
        solutions = [
            new_result
            for temp_result in solutions
            for new_result in (temp_result + num, temp_result * num)
        ] + [int(f"{temp_result}{num}") for temp_result in solutions if is_part2]
    return solutions


print(
    sum(
        int(result) * (int(result) in solve(equations, is_part2=False))
        for result, equations in p_input
    )
)

# Part 2
print(
    sum(
        int(result) * (int(result) in solve(equations, is_part2=True))
        for result, equations in p_input
    )
)

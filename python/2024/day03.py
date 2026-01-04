# Part 1
import re
from pathlib import Path

p_input = Path("data.txt").read_text()


def sum_multiplications(instructions: str) -> int:
    return sum(
        int(first) * int(second)
        for first, second in re.findall(r"mul\((\d+),(\d+)\)", instructions)
    )


print(sum_multiplications(p_input))

# Part 2
p_input_parts = ["do()"] + re.split(r"(do\(\)|don't\(\))", p_input)

print(
    sum(
        (condition == "do()") * sum_multiplications(part)
        for condition, part in zip(p_input_parts[::2], p_input_parts[1::2])
    )
)

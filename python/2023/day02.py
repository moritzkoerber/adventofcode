# Part 1
import math
import pathlib
import re
from collections import defaultdict

lines = pathlib.Path("data.txt").read_text().splitlines()
shown = [re.findall(r"\b(\d+)\s(\w+)\b", line) for line in lines]

print(
    sum(
        i + 1
        for i, line in enumerate(shown)
        if not any(
            int(cubes[0]) > 14
            or (int(cubes[0]) > 13 and cubes[1] == "green")
            or (int(cubes[0]) > 12 and cubes[1] == "red")
            for cubes in line
        )
    )
)

# Part 2
nums = 0
for line in shown:
    shown_cubes = defaultdict(int)
    for v, k in line:
        shown_cubes[k] = max(shown_cubes[k], int(v))
    nums += math.prod(shown_cubes.values())
print(nums)

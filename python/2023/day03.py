# Part 1
import math
import pathlib
from collections import defaultdict

grid = pathlib.Path("data.txt").read_text().splitlines()

dim1, dim2 = len(grid) - 1, len(grid[0]) - 1


def check_surrounding(num_positions: list[list[int]]) -> list[tuple[int, int, str]]:
    return [
        (i, j, grid[i][j])
        for v, h in num_positions
        for i, j in zip(
            [
                v,
                v,
                min(v + 1, dim1),
                max(v - 1, 0),
                max(v - 1, 0),
                max(v - 1, 0),
                min(v + 1, dim1),
                min(v + 1, dim1),
            ],
            [
                min(h + 1, dim2),
                max(h - 1, 0),
                h,
                h,
                min(h + 1, dim2),
                max(h - 1, 0),
                min(h + 1, dim2),
                max(h - 1, 0),
            ],
        )
        if grid[i][j] in {"/", "%", "#", "-", "=", "@", "+", "$", "&", "*"}
    ]


gear_nums = defaultdict(list)

for i, row in enumerate(grid):
    num = ""
    positions = []
    for j, element in enumerate(row):
        if element.isdigit():
            positions.append([i, j])
            num += element
        if not element.isdigit() or j == dim2:
            if gear_positions := check_surrounding(positions):
                for gear in gear_positions:
                    gear_nums[gear].append(int(num))
            num = ""
            positions.clear()

print(sum(sum(set(e)) for e in gear_nums.values()))

# Part 2
print(
    sum(
        math.prod(nums)
        for k, v in gear_nums.items()
        if len(nums := set(v)) > 1 and k[2] == "*"
    )
)

# Part 1
from pathlib import Path

grid = Path("data.txt").read_text().splitlines()

v, h = len(grid), len(grid[0])

target = "XMAS"

horizontal = sum(e.count(target) + e.count(target[::-1]) for e in grid)

vertical = sum(
    e.count(target) + e.count(target[::-1]) for e in map("".join, zip(*grid))
)

vertical_down_right_up_left = sum(
    "".join(grid[row + i][col + i] for i in range(4)) in [target, target[::-1]]
    for row in range(v - 3)
    for col in range(h - 3)
)

vertical_down_left_up_right = sum(
    "".join(grid[row + i][col - i] for i in range(4)) in [target, target[::-1]]
    for row in range(v - 3)
    for col in range(3, h)
)

print(horizontal + vertical + vertical_down_right_up_left + vertical_down_left_up_right)

# Part 2
print(
    sum(
        grid[row][col]
        + grid[row - 1][col - 1]
        + grid[row + 1][col - 1]
        + grid[row - 1][col + 1]
        + grid[row + 1][col + 1]
        in [
            "AMMSS",
            "AMSMS",
            "ASMSM",
            "ASSMM",
        ]
        for row in range(1, v - 1)
        for col in range(1, h - 1)
    )
)

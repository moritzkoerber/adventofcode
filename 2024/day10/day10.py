# Part 1
from pathlib import Path

grid = {
    (i, j): int(col)
    for i, row in enumerate(Path("data.txt").read_text().splitlines())
    for j, col in enumerate(row)
}

trailheads = [k for k, v in grid.items() if v == 0]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def climb(
    current_pos: tuple[int, int], found: set[tuple[int, int]], is_part1: bool
) -> int:
    if is_part1 and current_pos in found:
        return 0
    if grid[current_pos] == 9:
        found.add(current_pos)
        return 1

    next_steps = [(current_pos[0] + d[0], current_pos[1] + d[1]) for d in directions]

    return sum(
        climb((ny, nx), found, is_part1)
        for ny, nx in next_steps
        if (ny, nx) in grid and grid[ny, nx] - grid[current_pos[0], current_pos[1]] == 1
    )


print(sum(climb(trailhead, set(), True) for trailhead in trailheads))

# Part 2
print(sum(climb(trailhead, set(), False) for trailhead in trailheads))

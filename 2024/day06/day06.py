# Part 1
from pathlib import Path

grid = Path("data.txt").read_text().splitlines()

grid_v, grid_h = len(grid), len(grid[0])

for i in range(grid_v):
    for j in range(grid_h):
        if grid[i][j] == "^":
            start = (i, j)
            break


def move(y: int, x: int, direction: int) -> tuple[int, int]:
    dy, dx = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ][direction]
    return y + dy, x + dx


def walk_guard(start: tuple[int, int], grid_v: int, grid_h: int, is_part1: bool) -> int:
    valid_obstacle_positions = 0
    for i in range(-is_part1, grid_v):
        for j in range(-is_part1, grid_h):
            direction = 0
            n_y, n_x = start
            seen = set()
            while n_y in range(grid_v) and n_x in range(grid_h):
                if grid[n_y][n_x] == "#" or n_y == i and n_x == j:
                    direction = (direction + 1) % 4
                else:
                    y, x = n_y, n_x
                    seen.add((y, x, direction))
                n_y, n_x = move(y, x, direction)
                if (n_y, n_x, direction) in seen:
                    valid_obstacle_positions += 1
                    break
            if is_part1:
                return len({(pos[0], pos[1]) for pos in seen})
    return valid_obstacle_positions


print(walk_guard(start, grid_v, grid_h, True))

# Part 2
print(walk_guard(start, grid_v, grid_h, False))

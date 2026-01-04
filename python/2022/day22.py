# Python
## Part 1

import math
import pathlib
import re
from functools import partial

*input_map, _, moves = pathlib.Path("data.txt").read_text().splitlines()
moves = re.split("([LR])", moves)

grid = {}
for y, line in enumerate(input_map):
    for x, col in enumerate(line):
        if col != " ":
            grid[x, y] = col

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move_position(
    x: int, y: int, step: tuple[int, int], backward: bool = False
) -> tuple[int, int]:
    if backward:
        return x + step[0] * -1, y + step[1] * -1
    return x + step[0], y + step[1]


pos_x, pos_y, direction = input_map[0].index("."), 0, 0

for move in moves:
    if move in ["L", "R"]:
        direction = (direction + 1 if move == "R" else direction - 1) % 4
    else:
        move_position = partial(move_position, step=steps[direction])
        for _ in range(int(move)):
            if (next_pos := move_position(pos_x, pos_y)) not in grid:
                while (step_back := move_position(*next_pos, backward=True)) in grid:
                    next_pos = step_back
            if grid[next_pos] == "#":
                break
            else:
                pos_x, pos_y = next_pos
pos_x += 1
pos_y += 1

print(pos_x * 4 + pos_y * 1000 + direction)

## Part 2
pos_x, pos_y, direction = input_map[0].index("."), 0, 0

side_size = math.gcd(len(input_map), max(len(c) for c in input_map))


def get_new_coords(
    current_side: tuple[int, int], current_direction: int
) -> list[int | tuple[int, int]]:
    adj_side_size = side_size - 1
    return {
        (2, 1): {
            2: [
                0,  # new direction
                (0, 2),  # offset
                0,  # relative_x
                adj_side_size - relative_y,  # relative_y
            ],
            3: [
                0,
                (0, 3),
                0,
                relative_x,
            ],
        },
        (3, 1): {
            0: [
                2,
                (1, 2),
                adj_side_size,
                adj_side_size - relative_y,
            ],
            1: [
                2,
                (1, 1),
                adj_side_size,
                relative_x,
            ],
            3: [
                3,
                (0, 3),
                relative_x,
                adj_side_size,
            ],
        },
        (2, 2): {
            0: [3, (2, 0), relative_y, adj_side_size],
            2: [1, (0, 2), relative_y, 0],
        },
        (1, 3): {
            2: [
                0,
                (1, 0),
                0,
                adj_side_size - relative_y,
            ],
            3: [
                0,
                (1, 1),
                0,
                relative_x,
            ],
        },
        (2, 3): {
            0: [
                2,
                (2, 0),
                adj_side_size,
                adj_side_size - relative_y,
            ],
            1: [2, (0, 3), adj_side_size, relative_x],
        },
        (1, 4): {
            0: [
                3,
                (1, 2),
                relative_y,
                adj_side_size,
            ],
            1: [
                1,
                (2, 0),
                relative_x,
                0,
            ],
            2: [
                1,
                (1, 0),
                relative_y,
                0,
            ],
        },
    }[current_side][current_direction]


for move in moves:
    if move in ["L", "R"]:
        direction = (direction + 1 if move == "R" else direction - 1) % 4
    else:
        for _ in range(int(move)):
            switched_side = False
            if (
                next_pos := move_position(pos_x, pos_y, step=steps[direction])
            ) not in grid:
                switched_side = True
                # current side
                side_x, side_y = (pos_x // side_size) + 1, (pos_y // side_size) + 1

                # current pos within side
                relative_x, relative_y = (pos_x % side_size, pos_y % side_size)

                (
                    new_direction,
                    (offset_x, offset_y),
                    new_relative_x,
                    new_relative_y,
                ) = get_new_coords((side_x, side_y), direction)

                next_pos = (
                    offset_x * side_size + new_relative_x,
                    offset_y * side_size + new_relative_y,
                )
            if grid[next_pos] == "#":
                break
            pos_x, pos_y = next_pos
            if switched_side:
                direction = new_direction

pos_x += 1
pos_y += 1

print(pos_x * 4 + pos_y * 1000 + direction)

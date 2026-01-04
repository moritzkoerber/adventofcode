# Part 1
from pathlib import Path

p_input, moves = Path("data.txt").read_text().split("\n\n")
moves = moves.replace("\n", "")


def move(y: int, x: int, direction: str) -> tuple[int, int]:
    dy, dx = {
        "^": [-1, 0],
        ">": [0, 1],
        "v": [1, 0],
        "<": [0, -1],
    }[direction]
    return y + dy, x + dx


grid = {}

for i, row in enumerate(p_input.splitlines()):
    for j, plot in enumerate(row):
        if plot == "@":
            y, x = i, j
        grid[(i, j)] = plot


def simulate_movements(y: int, x: int, grid: dict, moves: str) -> int:
    for direction in moves:
        to_move = [(y, x)]

        for by, bx in to_move:
            n = move(by, bx, direction)
            if grid[n] in "[]O":
                if n not in to_move:
                    to_move.append(n)
                if grid[n] == "[" and (ne := (n[0], n[1] + 1)) not in to_move:
                    to_move.append(ne)
                if grid[n] == "]" and (nw := (n[0], n[1] - 1)) not in to_move:
                    to_move.append(nw)
            elif grid[n] == "#":
                break
        else:
            new_grid = (
                grid
                | dict.fromkeys(to_move, ".")
                | {move(*k, direction): grid[k] for k in to_move}
            )
            grid = new_grid
            y, x = move(y, x, direction)

    return sum(y * 100 + x for (y, x), v in grid.items() if v in "[O")


print(simulate_movements(y, x, grid, moves))

# Part 2
p_input = (
    p_input.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")
)
grid = {}

for i, row in enumerate(p_input.splitlines()):
    for j, plot in enumerate(row):
        if plot == "@":
            y, x = i, j
        grid[(i, j)] = plot


print(simulate_movements(y, x, grid, moves))

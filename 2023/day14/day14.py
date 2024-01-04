# Part 1
import pathlib

grid_input = pathlib.Path("data.txt").read_text().splitlines()

grid_height, grid_width = len(grid_input), len(grid_input[0])
grid = [list(line) for line in grid_input]


def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    return [list(reversed(i)) for i in zip(*grid)]


def solve(grid: list[list[str]], target: int, rotations: int, part: int) -> int:
    seen = {}
    for run_cnt in range(target):
        for _ in range(rotations):
            movement = True
            while movement:
                movement = False
                for y in range(grid_height):
                    for x in range(grid_width):
                        if y > 0 and grid[y - 1][x] == "." and grid[y][x] == "O":
                            grid[y - 1][x] = "O"
                            grid[y][x] = "."
                            movement = True
            if part == 1:
                break
            grid = rotate_grid(grid)
        snapshot = tuple(tuple(row) for row in grid)
        if snapshot in seen:
            cycle_length = run_cnt - seen[snapshot]
            _, target = divmod(target - 1 - run_cnt, cycle_length)
            return solve(grid=grid, target=target, rotations=rotations, part=part)
        seen[snapshot] = run_cnt
    return sum(line.count("O") * (grid_height - i) for i, line in enumerate(grid))


print(solve(grid=grid, target=1, rotations=1, part=1))

# Part 2
print(solve(grid=grid, target=10**9, rotations=4, part=2))

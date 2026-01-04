# Part 1
from pathlib import Path

incoming_bytes = list(map(eval, Path("data.txt").read_text().splitlines()))


def solve(x: int, y: int, grid_size: int, visited: set[tuple[int, int]]) -> int:
    distances = [(0, x, y)]

    for tl, x, y in distances:
        if x == y == grid_size:
            return tl

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx <= grid_size
                and 0 <= ny <= grid_size
                and (nx, ny) not in visited
            ):
                distances.append((tl + 1, nx, ny))
                visited.add((nx, ny))

    return 0


print(solve(0, 0, 70, set(incoming_bytes[:1024])))

# Part 2
for i in range(1025, len(incoming_bytes)):
    if not solve(0, 0, 70, set(incoming_bytes[:i])):
        print(incoming_bytes[i - 1])
        break

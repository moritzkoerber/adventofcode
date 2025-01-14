# Part 1
import itertools
from heapq import heappop, heappush
from pathlib import Path

p_input = Path("data.txt").read_text().splitlines()

grid = {}

for i, row in enumerate(p_input):
    for j, col in enumerate(row):
        if col == "E":
            ey, ex = i, j
        elif col == "S":
            sy, sx = i, j
        grid[(i, j)] = col

heap = [(0, (sy, sx))]
distances = {(sy, sx): 0}

while heap:
    total_cost, (y, x) = heappop(heap)

    if grid.get((y, x)) == "E":
        break

    for dy, dx in [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ]:
        if grid[y + dy, x + dx] != "#" and (y + dy, x + dx) not in distances:
            distances[(y + dy, x + dx)] = distances[(y, x)] + 1
            heappush(
                heap,
                (
                    total_cost + 1,
                    (y + dy, x + dx),
                ),
            )


def run(radius: int) -> int:
    total = 0
    for (y, x), r in itertools.product(distances, range(radius)):
        for dy in range(r + 1):
            dx = r - dy
            for ny, nx in {
                (y + dy, x + dx),
                (y + dy, x - dx),
                (y - dy, x + dx),
                (y - dy, x - dx),
            }:
                if (ny, nx) in distances and (
                    distances[y, x] - distances[ny, nx] - r >= 100
                ):
                    total += 1
    return total


print(run(3))

# Part 2
print(run(21))

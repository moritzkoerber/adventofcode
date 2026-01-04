# Part 1
import math
from collections import defaultdict, deque
from collections.abc import Generator
from heapq import heappop, heappush
from pathlib import Path

p_input = Path("data.txt").read_text().splitlines()


def calc_neighbors(
    y: int, x: int, direction: int
) -> Generator[tuple[int, tuple[int, int, int]], None, None]:
    yield 1000, (y, x, (direction - 1) % 4)
    yield 1000, (y, x, (direction + 1) % 4)
    dy, dx = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ][direction]
    if grid[y + dy, x + dx] != "#":
        yield 1, (y + dy, x + dx, direction)


grid = {}

for i, row in enumerate(p_input):
    for j, col in enumerate(row):
        if col == "E":
            ey, ex = i, j
        elif col == "S":
            sy, sx = i, j
        grid[(i, j)] = col


distances = defaultdict(lambda: math.inf)
source = defaultdict(lambda: set())
heap = [(0, (sy, sx, 1))]
visited = set()

while heap:
    total_cost, (y, x, curr_d) = heappop(heap)
    if (y, x, curr_d) in visited:
        continue

    visited.add((y, x, curr_d))

    if grid[(y, x)] == "E":
        print(f"Part 1: {total_cost}")

    for nc, neighbor_pos in calc_neighbors(y, x, curr_d):
        if (total_cost + nc) < distances[neighbor_pos]:
            distances[neighbor_pos] = total_cost + nc
            heappush(heap, (total_cost + nc, neighbor_pos))
            source[neighbor_pos] = {(y, x, curr_d)}
        elif (total_cost + nc) == distances[neighbor_pos]:
            source[neighbor_pos].add((y, x, curr_d))

# Part 2
stack = deque([(ey, ex, 1)])
taken = set()

while stack:
    y, x, d = stack.pop()
    if (y, x, d) in taken:
        continue
    taken.add((y, x, d))

    for ny, nx, nd in source.get((y, x, d), []):
        if (ny, nx, nd) not in taken:
            stack.append((ny, nx, nd))

print(len({e[:2] for e in taken}))

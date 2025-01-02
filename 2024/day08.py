# Part 1
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path

grid = Path("data.txt").read_text().splitlines()
grid_v, grid_h = len(grid), len(grid[0])

antennas = defaultdict(list)

for i, j in product(range(grid_v), range(grid_h)):
    if grid[i][j] != ".":
        antennas[grid[i][j]].append((i, j))


def find_antinodes(*distance_range: int) -> int:
    antinodes = set()
    for positions in antennas.values():
        for a1, a2 in permutations(positions, 2):
            dy, dx = a2[0] - a1[0], a2[1] - a1[1]
            for dist_mult in range(*distance_range):
                antinodes |= {
                    (a2[0] + dy * dist_mult, a2[1] + dx * dist_mult),
                    (a1[0] - dy * dist_mult, a1[1] - dx * dist_mult),
                }
    return sum(y in range(grid_v) and x in range(grid_h) for y, x in antinodes)


print(find_antinodes(1, 2))

# Part 2
print(find_antinodes(grid_v - 2))

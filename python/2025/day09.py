# Part 1 + 2
import pathlib
from itertools import combinations, pairwise

p_input = pathlib.Path("day09.txt").read_text().splitlines()

positions = [tuple(map(int, e.split(","))) for e in p_input]
boundaries = sorted(
    pairwise(positions + [positions[0]]),
    key=lambda p: abs(p[0][0] - p[1][0] + p[0][1] - p[1][1]),
)

part1, part2 = 0, 0
for (x1, y1), (x2, y2) in combinations(positions, 2):
    tlx, brx = min(x1, x2), max(x1, x2)
    tly, bry = min(y1, y2), max(y1, y2)

    size = (brx - tlx + 1) * (bry - tly + 1)

    part1 = max(part1, size)

    for (a1, b1), (a2, b2) in boundaries:
        tlx2, brx2 = min(a1, a2), max(a1, a2)
        tly2, bry2 = min(b1, b2), max(b1, b2)

        if tlx2 < brx and brx2 > tlx and tly2 < bry and bry2 > tly:
            break
    else:
        part2 = max(part2, size)

print(part1, part2, sep="\n")

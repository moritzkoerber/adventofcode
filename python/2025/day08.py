# Part 1 + 2
import math
import pathlib

p_input = pathlib.Path("day08.txt").read_text().splitlines()

boxes = [tuple(map(int, row.split(","))) for row in p_input]

closest_boxes = sorted(
    [(x, y) for i, x in enumerate(boxes, 1) for y in boxes[i:]],
    key=lambda x: math.dist(*x),
)
circuits = {k: (k,) for k in boxes}

for i, (x, y) in enumerate(closest_boxes):
    if i == 1000:
        print(math.prod(map(len, sorted(set(circuits.values()), key=len)[-3:])))
    if circuits[x] != circuits[y]:
        new = circuits[x] + circuits[y]
        for z in new:
            circuits[z] = new
    if len(set(circuits.values())) == 1:
        print(x[0] * y[0])
        break

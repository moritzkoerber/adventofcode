# Python
## Part 1
import itertools
from collections import deque

with open("data.txt") as f:
    input_droplets = {tuple(map(int, x.split(","))) for x in f.read().splitlines()}


def add_offset(voxel: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    x, y, z = voxel
    return [
        (x + dx, y + dy, z + dz)
        for dx, dy, dz in [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]
    ]


print(
    sum(
        voxel not in input_droplets
        for x in map(add_offset, input_droplets)
        for voxel in x
    )
)

## Part 2
border = max(map(abs, itertools.chain.from_iterable(input_droplets)))
count = 0
q = deque([(-1, -1, -1)])
seen = set()

while q:
    for o in add_offset(q.popleft()):
        if o in input_droplets:
            count += 1
        elif o not in seen and all(-1 <= x <= border + 1 for x in o):
            q.append(o)
            seen.add(o)
print(count)

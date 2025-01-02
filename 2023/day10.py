# Part 1
import math
import pathlib

grid = pathlib.Path("data.txt").read_text().splitlines()


def move(
    point_y: int,
    point_x: int,
    add_y: int,
    add_x: int,
) -> tuple[int, int]:
    return point_y + add_y, point_x + add_x


loop = set()

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            start = (i, j)
            loop.add(start)

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

mapping = {
    "|": {2: 2, 3: 3},
    "-": {0: 0, 1: 1},
    "L": {1: 2, 3: 0},
    "J": {0: 2, 3: 1},
    "7": {2: 1, 0: 3},
    "F": {2: 0, 1: 3},
    ".": {},
}

links = []
for e in range(4):
    y, x = move(*start, *dirs[e])
    if e in mapping[grid[y][x]]:
        links.append(e)
        curr, d = (y, x), e
        loop.add(curr)

cnt = 0

while curr != start:
    y, x = curr
    d = mapping[grid[y][x]][d]
    curr = move(*curr, *dirs[d])
    cnt += 1
    loop.add(curr)

print(math.ceil(cnt / 2))


# Part 2
def calculate_crossings(y: int, x: int) -> bool:
    crossing_cnt = sum(grid[y][e] in "|F7" for e in range(x) if (y, e) in loop)
    return crossing_cnt % 2 != 0


for k, v in mapping.items():
    if sorted(links) == sorted(v.values()):
        grid[start[0]] = grid[start[0]].replace("S", k)
        break

cnt = 0
for i, row in enumerate(grid):
    for j, _ in enumerate(row):
        if (i, j) not in loop:
            cnt += calculate_crossings(i, j)
print(cnt)

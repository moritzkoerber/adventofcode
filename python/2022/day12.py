# Python
## Part 1
from heapq import heappop, heappush

with open("data.txt") as f:
    letters = f.read()

for i, j in enumerate(letters.splitlines()):
    if "S" in j:
        s_pos = i, j.index("S")
    if "E" in j:
        e_pos = i, j.index("E")

grid = [
    [ord(letter) for letter in row]
    for row in letters.replace("S", "a").replace("E", "z").splitlines()
]


def calculate_shortest_path(starting_pos: tuple, end_pos: tuple) -> int:
    heap = [
        (
            0,
            *starting_pos,
        )
    ]
    visited = {starting_pos}

    while heap:
        d, r, c = heappop(heap)
        if (r, c) == end_pos:
            return d
        for row, col in [
            [r + 1, c],
            [r - 1, c],
            [r, c + 1],
            [r, c - 1],
        ]:
            if (row, col) in visited:
                continue
            if row not in range(len(grid)) or col not in range(len(grid[0])):
                continue
            if grid[row][col] - grid[r][c] <= 1:
                heappush(heap, (d + 1, row, col))
                visited.add((row, col))
    raise RuntimeError("No path found")


print(calculate_shortest_path(s_pos, e_pos))

## Part 2
distance = len(grid) * len(grid[0])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ord("a"):
            try:
                if (result := calculate_shortest_path((i, j), e_pos)) < distance:
                    distance = result
            except RuntimeError:
                continue
print(distance)

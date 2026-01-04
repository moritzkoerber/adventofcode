# Part 1
from collections import deque
from pathlib import Path

p_input = Path("data.txt").read_text().splitlines()

grid = {(i, j): plot for i, row in enumerate(p_input) for j, plot in enumerate(row)}

p1 = p2 = 0
seen = set()

for i, j in grid:
    if (i, j) not in seen:
        region = grid[(i, j)]
        q = deque([(i, j)])
        perimeter = area = corners = 0
        while q:
            y, x = q.popleft()
            if (y, x) not in seen:
                area += 1

                for dy1, dx1, dy2, dx2 in [
                    [-1, 0, 0, 1],
                    [0, 1, 1, 0],
                    [1, 0, 0, -1],
                    [0, -1, -1, 0],
                ]:
                    if (
                        grid.get((y + dy1, x + dx1)) != region
                        and grid.get((y + dy2, x + dx2)) != region
                    ) or (
                        grid.get((y + dy1, x + dx1))
                        == grid.get((y + dy2, x + dx2))
                        == region
                        and grid.get((y + dy1 + dy2, x + dx1 + dx2)) != region
                    ):
                        corners += 1

                    seen.add((y, x))

                for ny, nx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if grid.get((y + ny, x + nx)) == region:
                        q.append((y + ny, x + nx))
                    else:
                        perimeter += 1

        p1 += area * perimeter
        p2 += area * corners

print(p1)

# Part 2
print(p2)

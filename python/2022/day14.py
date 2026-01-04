# Python
## Part 1
import copy

with open("data.txt") as f:
    rocks = [[eval(i) for i in x.split(" -> ")] for x in f.read().splitlines()]

rock_pos = set()

for rock in rocks:
    for i, j in enumerate(rock):
        rock_pos.add(j)
        if i == len(rock) - 1:
            continue
        (x1, y1), (x2, y2) = sorted([rock[i], rock[i + 1]])
        if x1 == x2:
            for n in range(y1 + 1, y2):
                rock_pos.add((x1, n))
        elif y1 == y2:
            for n in range(x1 + 1, x2):
                rock_pos.add((n, y1))
        else:
            raise ValueError("Pathing failed.")

depth = max(i[1] for i in rock_pos)


def simulate_sand(rock_positions: set[tuple[int, int]], part: str) -> int:
    sands = 0
    sand_x, sand_y = 500, 0
    while (part == "part2" or sand_y < depth) and (
        sand_x,
        sand_y,
    ) not in rock_positions:
        if (sand_x, sand_y + 1) not in rock_positions:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in rock_positions:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in rock_positions:
            sand_x += 1
            sand_y += 1
        else:
            rock_positions.add((sand_x, sand_y))
            sand_x, sand_y = 500, 0
            sands += 1
    return sands


print(simulate_sand(copy.deepcopy(rock_pos), part="part1"))

## Part 2
for n in range(-999, 999):
    rock_pos.add((n, depth + 2))

print(simulate_sand(copy.deepcopy(rock_pos), part="part2"))

# Part 1
import pathlib
from functools import cache

first, *lines = pathlib.Path("data.txt").read_text().splitlines()
beams = [e == "S" for e in first]

total = 0
for row in lines:
    for i in range(len(row)):
        if row[i] == "^" and beams[i]:
            total += 1
            beams[i], beams[i - 1], beams[i + 1] = 0, 1, 1

print(total)


# Part 2
@cache
def recur(pos: tuple[int, int]) -> int:
    new_pos = (pos[0] + 1, pos[1])
    if new_pos[0] == len(lines):
        return 1
    if lines[new_pos[0]][new_pos[1]] == "^":
        return sum(
            [recur((new_pos[0], new_pos[1] - 1)), recur((new_pos[0], new_pos[1] + 1))]
        )

    return recur(new_pos)


print(recur((0, first.index("S"))))

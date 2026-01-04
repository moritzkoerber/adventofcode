# Part 1
import re
from functools import cache
from pathlib import Path

p_input = Path("data.txt").read_text().split("\n\n")


@cache
def press(x: int, y: int, ax: int, ay: int, bx: int, by: int, cost: int = 0) -> int:
    if cost > 400:
        return 401
    if x == y == 0:
        return cost
    return min(
        press(x - ax, y - ay, ax, ay, bx, by, cost + 3),
        press(x - bx, y - by, ax, ay, bx, by, cost + 1),
    )


p1 = p2 = 0

for ax, ay, bx, by, tx, ty in [map(int, re.findall(r"\d+", line)) for line in p_input]:
    if (cost := press(tx, ty, ax, ay, bx, by)) < 400:
        p1 += cost

    tx, ty = tx + 10000000000000, ty + 10000000000000
    if (r := (tx * by - ty * bx) / (ax * by - ay * bx)).is_integer() and (
        s := (ty * ax - tx * ay) / (ax * by - ay * bx)
    ).is_integer():
        p2 += 3 * r + s

print(p1)

# Part 2
print(int(p2))

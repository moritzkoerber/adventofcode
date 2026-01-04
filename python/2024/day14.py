# Part 1
import re
from itertools import count
from pathlib import Path

robots = [
    list(map(int, re.findall(r"-?\d+", line)))
    for line in Path("data.txt").read_text().splitlines()
]

grid_v, grid_h = 103, 101

robots_p1 = [
    [(x + vx * 100) % grid_h, (y + vy * 100) % grid_v, vx, vy]
    for x, y, vx, vy in robots
]

q1 = q2 = q3 = q4 = 0

for robot in robots_p1:
    x, y, *_ = robot
    q1 += x < grid_h // 2 and y < grid_v // 2
    q2 += x > grid_h // 2 and y < grid_v // 2
    q3 += x < grid_h // 2 and y > grid_v // 2
    q4 += x > grid_h // 2 and y > grid_v // 2

print(q1 * q2 * q3 * q4)

# Part 2
for second in count(1):
    robots = [((x + vx) % grid_h, (y + vy) % grid_v, vx, vy) for x, y, vx, vy in robots]
    if len({(x, y) for x, y, *_ in robots}) == len(robots):
        print(second)
        break

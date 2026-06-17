# Part 1
import pathlib
from collections import deque

import z3

p_input = pathlib.Path("day10.txt").read_text().splitlines()

inputs = [
    (
        int(lights[1:-1][::-1].replace("#", "1").replace(".", "0"), 2),
        [eval(e.replace(")", ",)")) for e in buttons],
        list(map(int, eval(joltages.strip("{}")))),
    )
    for p in p_input
    for lights, *buttons, joltages in [p.split()]
]

total = 0
for target, buttons, _ in inputs:
    q = deque([[0, 0]])
    seen = set()
    while q:
        state, cnt = q.popleft()
        if state == target:
            total += cnt
            break

        if state in seen:
            continue
        seen.add(state)

        for button in buttons:
            mask = 0
            for bit in button:
                mask |= 1 << bit
            q.append([state ^ mask, cnt + 1])

print(total)

# Part 2
total = 0
for _, buttons, joltages in inputs:
    o = z3.Optimize()

    counts = z3.Ints(f"x{i}" for i in range(len(buttons)))

    for var in counts:
        o.add(var >= 0)

    for i, joltage in enumerate(joltages):
        equation = sum(counts[b] for b, button in enumerate(buttons) if i in button)
        o.add(equation == joltage)

    o.minimize(sum(counts))
    o.check()

    total += o.model().eval(sum(counts)).as_long()

print(total)

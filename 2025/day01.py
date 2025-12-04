# Part 1
import pathlib
import re

p_input = [
    int(re.search(r"-?\d+", line.replace("L", "-"))[0])
    for line in pathlib.Path("data.txt").read_text().splitlines()
]

dial = 50
print(sum((dial := (dial + turn) % 100) == 0 for turn in p_input))

# Part 2
dial, cnt = 50, 0
for turn in p_input:
    step = turn > 0 or -1
    for _ in range(turn * step):
        cnt += (dial := (dial + step) % 100) == 0
print(cnt)

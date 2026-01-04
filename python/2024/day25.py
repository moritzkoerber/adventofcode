# Part 1
from itertools import combinations
from pathlib import Path

p_input = Path("data.txt").read_text().split("\n\n")

print(
    sum(
        not any(pos_l == pos_r == "#" for pos_l, pos_r in zip(left, right))
        for left, right in combinations(p_input, 2)
    )
)

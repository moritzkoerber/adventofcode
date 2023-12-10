# Part 1
import math
import pathlib
import re
from itertools import count, cycle

lines = pathlib.Path("data.txt").read_text()

dirs, maps = lines.split("\n\n")

kvs = {k: v for k, *v in [re.findall(r"\w{3}", line) for line in maps.splitlines()]}


def calculate_cycle_lengths(
    state: str, end_cond: str, kvs: dict[str, list[str]] = kvs, dirs: str = dirs
) -> int:
    for d, i in zip(cycle(dirs.replace("L", "0").replace("R", "1")), count(1)):
        state = kvs[state][int(d)]
        if state.endswith(end_cond):
            return i


print(calculate_cycle_lengths("AAA", "ZZZ"))

# Part 2
print(
    math.lcm(
        *[calculate_cycle_lengths(state, "Z") for state in kvs if state.endswith("A")]
    )
)

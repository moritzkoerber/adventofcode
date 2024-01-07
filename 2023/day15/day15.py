# Part 1
import pathlib
import re
from collections import defaultdict
from functools import reduce

init_sequence = pathlib.Path("data.txt").read_text().rstrip("\n").split(",")


def calc_hash(string: str) -> int:
    return reduce(lambda c, s: ((c + ord(s)) * 17) % 256, string, 0)


print(sum(map(calc_hash, init_sequence)))

# Part 2
boxes = defaultdict(dict)

for item in init_sequence:
    label, op, fl = re.split("([=-])", item)
    box = calc_hash(label)
    if fl:
        boxes[box][label] = fl
    else:
        boxes[box].pop(label, None)

print(
    sum(
        (1 + k) * i * int(vv)
        for k, v in boxes.items()
        for i, vv in enumerate(v.values(), 1)
    )
)

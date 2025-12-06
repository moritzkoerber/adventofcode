# Part 1 + 2:
import pathlib
from functools import cache

p_input = pathlib.Path("data.txt").read_text().splitlines()


@cache
def recur(row: str, capacity: int) -> str:
    if capacity == 0:
        return ""

    if len(row) == capacity:
        return row

    return max(row[0] + recur(row[1:], capacity - 1), recur(row[1:], capacity))


print(sum(int(recur(p, capacity=2)) for p in p_input))
print(sum(int(recur(p, capacity=12)) for p in p_input))

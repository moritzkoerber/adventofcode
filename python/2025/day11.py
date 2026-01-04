# Part 1
import pathlib
from functools import cache

p_input = pathlib.Path("day11.txt").read_text().splitlines()

paths = {k: v.split() for k, v in [p.split(": ") for p in p_input]}


@cache
def recur(node: str, todo: frozenset) -> int:
    todo -= {node}
    if node == "out":
        return not todo
    return sum(recur(next_node, todo) for next_node in paths[node])


print(recur("you", frozenset()))

# Part 2
print(recur("svr", frozenset({"dac", "fft"})))

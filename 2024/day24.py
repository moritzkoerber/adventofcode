# Part 1
from pathlib import Path

states, wiring = Path("data.txt").read_text().split("\n\n")
states = {k: int(v) for k, v in [state.split(": ") for state in states.splitlines()]}

rules = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}


def _get(key: str) -> int:
    if isinstance(states[key], int):
        return states[key]
    i1, rule, i2 = states[key]
    return rules[rule](_get(i1), _get(i2))


for wire in wiring.splitlines():
    i1, rule, i2, _, output = wire.split()
    states[output] = i1, rule, i2

int(
    "".join([str(_get(x)) for x in sorted(states) if x.startswith("z")])[::-1],
    2,
)

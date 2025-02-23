# Part 1
from pathlib import Path

wires, gates = Path("data.txt").read_text().split("\n\n")
wires = {k: int(v) for k, v in [state.split(": ") for state in wires.splitlines()]}

rules = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}


def _get(key: str) -> int:
    if isinstance(wires[key], int):
        return wires[key]
    i1, rule, i2 = wires[key]
    return rules[rule](_get(i1), _get(i2))


for gate in gates.splitlines():
    i1, rule, i2, _, output = gate.split()
    wires[output] = i1, rule, i2

print(
    int(
        "".join([str(_get(f"z{i:02}")) for i in range(46)])[::-1],
        2,
    )
)

# Part 2
parsed_gates = [(k, v) for k, v in wires.items() if isinstance(v, tuple)]
faulty = []

for output, (i1, rule, i2) in parsed_gates:
    if rule == "XOR" and all(
        first_letter not in "xyz" for first_letter in [output[0], i1[0], i2[0]]
    ):
        faulty.append(output)
    if (
        rule == "AND"
        and i1 + i2 != "x00y00"
        and not any(
            rule == "OR" and output in (i1, i2) for _, (i1, rule, i2) in parsed_gates
        )
    ):
        faulty.append(output)
    if (
        rule == "XOR"
        and "x" in (i1[0], i2[0])
        and i1 + i2 != "x00y00"
        and not any(
            rule == "XOR" and output in (i1, i2) for _, (i1, rule, i2) in parsed_gates
        )
    ):
        faulty.append(output)
    if rule != "XOR" and output != "z45" and output.startswith("z"):
        faulty.append(output)


print(*sorted(faulty), sep=",")

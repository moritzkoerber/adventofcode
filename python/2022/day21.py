# Python
## Part 1
import pathlib

import sympy

input_data = pathlib.Path("data.txt").read_text()

monkeys = dict([e.split(": ") for e in input_data.splitlines()])


def solve(value: str) -> str | int:
    if (v := monkeys[value]).isnumeric() or v == "x":
        return v
    a, op, c = v.split()
    res = f"({solve(a)} {op} {solve(c)})"
    return res if "x" in res else int(eval(res))


print(solve("root"))

# Part 2
p1, _, p2 = monkeys["root"].split()
monkeys["humn"] = "x"

x = sympy.Symbol("x")

print(sympy.solve(sympy.Eq(sympy.parse_expr(solve(p1)), solve(p2)))[0])

# Part 1
import re
from pathlib import Path

a, b, c, *instructions = map(int, re.findall(r"\d+", Path("data.txt").read_text()))


def run_program(a: int, b: int, c: int, instructions: list[int]) -> str:
    def convert_to_combo_op(op: int) -> int:
        match op:
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c
            case _:
                return op

    output = []
    i = 0

    while i <= len(instructions) - 1:
        oc, op = instructions[i], instructions[i + 1]

        if oc == 0:
            a = a >> convert_to_combo_op(op)
        elif oc == 1:
            b ^= op
        elif oc == 2:
            b = convert_to_combo_op(op) % 8
        elif oc == 3:
            if a:
                i = op
                continue
        elif oc == 4:
            b ^= c
        elif oc == 5:
            output.append(str(convert_to_combo_op(op) % 8))
        elif oc == 6:
            b = a >> convert_to_combo_op(op)
        elif oc == 7:
            c = a >> convert_to_combo_op(op)
        i += 2

    return ",".join(output)


print(run_program(a, b, c, instructions))

# Part 2
possible_a = [0]
for i in reversed(range(len(instructions))):
    instructions_tail = ",".join(map(str, instructions[i:]))
    possible_a = [
        a * 8 + digit
        for a in possible_a
        for digit in range(8)
        if run_program(a * 8 + digit, b, c, instructions) == instructions_tail
    ]

print(min(possible_a))

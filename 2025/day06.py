# Part 1
import pathlib

p_input = pathlib.Path("day06.txt").read_text().splitlines()
*nums, ops = map(str.split, p_input)

total = 0
for op, num_col in zip(ops, zip(*nums)):
    total += eval(op.join(map(str, num_col)))
print(total)

# Part 2
total = ""
for *num_col, op in zip(*p_input):
    if op.strip():
        t_op = op
    if num := "".join(num_col).strip():
        total += num + t_op
    else:
        total = total[:-1] + "+"

print(eval(total[:-1]))

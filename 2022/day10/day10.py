# Python
## Part 1
with open("data.txt") as f:
    instructions = map(str.split, f.read().splitlines())

x = 1
cs = []

for i in instructions:
    if i[0] == "noop":
        cs.append(x)
    else:
        cs.extend([x, x])
        x += int(i[1])

print(sum(cs[i - 1] * i for i in list(range(20, 221, 40))))

## Part 2
res = []
for x in [cs[r : r + 40] for r in range(0, len(cs), 40)]:
    for i in range(40):
        if abs(x[i] - i) <= 1:
            res.append("#")
        else:
            res.append(" ")
    res.append("\n")
print("".join(res))

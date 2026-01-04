# Python
## Part 1

with open("data.txt") as f:
    content = f.read()
    parsed_packets = [
        [eval(x) for x in p] for p in map(str.splitlines, content.split("\n\n"))
    ]


def solve(p1: int | list, p2: int | list) -> int:
    if isinstance(p1, list) and isinstance(p2, list):
        for e1, e2 in zip(p1, p2):
            if res := solve(e1, e2):
                return res
        return len(p1) - len(p2)
    if isinstance(p1, list) and isinstance(p2, int):
        return solve(p1, [p2])
    if isinstance(p1, int) and isinstance(p2, list):
        return solve([p1], p2)
    return p1 - p2


print(sum(i + 1 for i, (p1, p2) in enumerate(parsed_packets) if solve(p1, p2) < 0))

## Part 2
divider_1 = [[2]]
divider_2 = [[6]]
i_1 = 1
i_2 = 2

for item in [eval(i) for i in content.splitlines() if i != ""]:
    if solve(item, divider_1) < 0:
        i_1 += 1
    if solve(item, divider_2) < 0:
        i_2 += 1
print(i_1 * i_2)

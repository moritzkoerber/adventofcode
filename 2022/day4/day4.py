# Python
## Part 1
import re

with open("data.txt") as f:
    assignments = f.read().splitlines()

numeric_assignments = [[int(e) for e in re.split(r"[,-]", a)] for a in assignments]

print(
    sum(
        (x[0] <= x[2]) and (x[1] >= x[3]) or (x[2] <= x[0]) and (x[3] >= x[1])
        for x in numeric_assignments
    )
)

## Part 2
print(
    sum(
        (x[0] >= x[2] or x[1] >= x[2]) and (x[0] <= x[3] or x[1] <= x[3])
        for x in numeric_assignments
    )
)

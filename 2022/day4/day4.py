# Python
## Part 1
import re

with open("data.txt") as f:
    assignments = f.read().splitlines()

numeric_assignments = [[int(e) for e in re.split(r"[,-]", a)] for a in assignments]

sum(
    map(
        lambda x: (
            (x[0] <= x[2]) and (x[1] >= x[3]) or (x[2] <= x[0]) and (x[3] >= x[1])
        ),
        numeric_assignments,
    )
)


## Part 2
sum(
    map(
        lambda x: not (
            (x[0] < x[2]) and (x[1] < x[2]) or (x[0] > x[3]) and (x[1] > x[3])
        ),
        numeric_assignments,
    )
)

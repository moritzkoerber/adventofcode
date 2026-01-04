# Part 1
import pathlib

ranges, ids = pathlib.Path("day05.txt").read_text().split("\n\n")

valid_ids = [[*map(int, p.split("-"))] for p in ranges.splitlines()]

print(
    sum(
        any(
            int(ingredient_id) >= ll and int(ingredient_id) <= ul
            for ll, ul in valid_ids
        )
        for ingredient_id in ids.splitlines()
    )
)

# Part 2
curr_max, total = 0, 0
for ll, ul in sorted(valid_ids):
    total += max(curr_max, ul + 1) - max(curr_max, ll)
    curr_max = max(curr_max, ul + 1)

print(total)

# Part 1
import pathlib
import re

*shapes, regions = pathlib.Path("day12.txt").read_text().split("\n\n")

print(
    sum(
        sum(cnts) <= (x // 3) * (y // 3)
        for region in regions.splitlines()
        for x, y, *cnts in [map(int, re.findall(r"\d+", region))]
    )
)

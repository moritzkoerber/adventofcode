# Python
## Part 1

from collections.abc import Sequence

with open("data.txt") as f:
    trees = f.read().splitlines()

trees_t = list(map("".join, zip(*trees)))


def calculate_visibility(tree_row: str) -> list[bool]:
    return [
        (i == 0)
        or (i == len(tree_row) - 1)
        or (j > max(tree_row[:i]) and i <= tree_row.index(max(tree_row)))
        or (j > max(tree_row[i + 1 :]) and i >= tree_row.rfind(max(tree_row)))
        for i, j in enumerate(tree_row)
    ]


horizontal_rows = [res for tree_row in trees for res in calculate_visibility(tree_row)]

vertical_rows = [
    res
    for sublist in map(
        list, zip(*[calculate_visibility(tree_row) for tree_row in trees_t])
    )
    for res in sublist
]

print(sum(i or j for i, j in zip(horizontal_rows, vertical_rows)))


## Part 2
def calculate_distance(tree_row: Sequence) -> list[int]:
    return [
        ([e >= j for e in tree_row[1:i][::-1] + j].index(True) + 1)
        * (i != 0)
        * ([e >= j for e in tree_row[i + 1 : -1] + j].index(True) + 1)
        * (i != len(tree_row) - 1)
        for i, j in enumerate(tree_row)
    ]


horizontal_rows = [res for tree_row in trees for res in calculate_distance(tree_row)]

vertical_rows = [
    res
    for sublist in map(
        list, zip(*[calculate_distance(tree_row) for tree_row in trees_t])
    )
    for res in sublist
]

print(max(i * j for i, j in zip(horizontal_rows, vertical_rows)))

# Python
## Part 1

with open("data.txt") as f:
    trees = f.read().splitlines()


def calculate_visibility(tree_row: str) -> list[bool]:
    m = max(tree_row)
    return [
        (i == 0)
        or (i == len(tree_row) - 1)
        or (i <= tree_row.index(m) and j > max(tree_row[:i]))
        or (i >= tree_row.rfind(m) and j > max(tree_row[i + 1 :]))
        for i, j in enumerate(tree_row)
    ]


horizontal_rows = [
    tree_visibility
    for tree_row in trees
    for tree_visibility in calculate_visibility(tree_row)
]

trees_t = list(map("".join, zip(*trees)))

vertical_rows = [
    tree_visibility
    for tree_row in zip(*map(calculate_visibility, trees_t))
    for tree_visibility in tree_row
]

print(sum(i or j for i, j in zip(horizontal_rows, vertical_rows)))


## Part 2
def calculate_distance(tree_row: str) -> list[int]:
    return [
        ([e >= j for e in tree_row[1:i][::-1] + j].index(True) + 1)
        * (i != 0)
        * ([e >= j for e in tree_row[i + 1 : -1] + j].index(True) + 1)
        * (i != len(tree_row) - 1)
        for i, j in enumerate(tree_row)
    ]


horizontal_rows = [
    scenic_score for tree_row in trees for scenic_score in calculate_distance(tree_row)
]

vertical_rows = [
    scenic_score
    for tree_row in zip(*map(calculate_distance, trees_t))
    for scenic_score in tree_row
]

print(max(i * j for i, j in zip(horizontal_rows, vertical_rows)))

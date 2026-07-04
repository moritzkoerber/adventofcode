# Python
## Part 1

with open("day08.txt") as f:
    trees = [list(map(int, tree_row)) for tree_row in f.read().splitlines()]

visible = set()
v = len(trees)
h = len(trees[0])

for i in range(v):
    max_t = -1
    for j in range(h):
        if trees[i][j] > max_t:
            max_t = trees[i][j]
            visible.add((i, j))
    max_t = -1
    for j in reversed(range(h)):
        if trees[i][j] > max_t:
            max_t = trees[i][j]
            visible.add((i, j))

for i in range(h):
    max_t = -1
    for j in range(v):
        if trees[j][i] > max_t:
            max_t = trees[j][i]
            visible.add((j, i))
    max_t = -1
    for j in reversed(range(v)):
        if trees[j][i] > max_t:
            max_t = trees[j][i]
            visible.add((j, i))

print(len(visible))

## Part 2
max_scenic = 0
for i in range(v):
    for j in range(h):
        r = l = d = u = 0
        tree = trees[i][j]

        for x in range(j + 1, h):
            r += 1
            if trees[i][x] >= tree:
                break
        for y in reversed(range(j)):
            l += 1
            if trees[i][y] >= tree:
                break

        for k in range(i + 1, v):
            d += 1
            if trees[k][j] >= tree:
                break
        for z in reversed(range(i)):
            u += 1
            if trees[z][j] >= tree:
                break

        max_scenic = max(max_scenic, r * l * d * u)

print(max_scenic)

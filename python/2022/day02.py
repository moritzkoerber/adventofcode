# Python
## Part 1
with open("data.txt") as f:
    games = f.read().replace(" ", "").splitlines()

outcomes_numeric = [(ord(i) - 64, ord(j) - 64 - 23) for i, j in games]

lookup_dict = {-2: 1, 2: -1}

print(sum((lookup_dict.get(j - i, j - i) + 1) * 3 + j for i, j in outcomes_numeric))

## Part 2
print(sum(((i + j) % 3) + 1 + (j - 1) * 3 for i, j in outcomes_numeric))

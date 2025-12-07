# Part 1
import itertools
import pathlib

p_input = pathlib.Path("data.txt").read_text().splitlines()

positions = {
    (i, j): p_input[i][j]
    for i, j in itertools.product(range(len(p_input)), range(len(p_input[0])))
    if p_input[i][j] == "@"
}


def check(pos: tuple[int, int]) -> bool:
    return (
        sum(
            (pos[0] + dy, pos[1] + dx) in positions
            for dy in [-1, 0, 1]
            for dx in [-1, 0, 1]
        )
        < 5
    )


print(sum(map(check, positions)))

# Part 2
total = 0
while movable := [*filter(check, positions)]:
    total += len(movable)
    for position in movable:
        positions.pop(position)

print(total)

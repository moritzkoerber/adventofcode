# Part 1
import itertools
import pathlib

p_input = pathlib.Path("data.txt").read_text().splitlines()

positions = {
    (i, j): p_input[i][j]
    for i, j in itertools.product(range(len(p_input)), range(len(p_input[0])))
    if p_input[i][j] == "@"
}


def check(y: int, x: int) -> bool:
    return (
        sum(
            (y + dy, x + dx) in positions
            for dy, dx in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (1, -1),
                (1, 0),
                (1, 1),
                (0, 1),
            ]
        )
        < 4
    )


print(sum(check(*position) for position in positions))

# Part 2
total = 0
while movable := [position for position in positions if check(*position)]:
    total += len(movable)
    for position in movable:
        positions.pop(position)
print(total)

# Python
## Part 1
import pathlib
from collections import Counter

elves = {
    (i, k)
    for i, j in enumerate(pathlib.Path("data.txt").read_text().splitlines())
    for k, l in enumerate(j)
    if l == "#"
}


def propose_move(
    elves: set, direction: str, row: int, col: int
) -> tuple[bool, tuple[int, int]]:
    match direction:
        case "north":
            return all(
                x not in elves
                for x in [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
            ), (row - 1, col)
        case "south":
            return all(
                x not in elves
                for x in [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            ), (row + 1, col)
        case "west":
            return all(
                x not in elves
                for x in [(row - 1, col - 1), (row, col - 1), (row + 1, col - 1)]
            ), (row, col - 1)
        case "east":
            return all(
                x not in elves
                for x in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
            ), (row, col + 1)


directions = ["north", "south", "west", "east"]


def simulate(elves: set, directions: list, max_rounds: int, part: int):
    rounds = 0
    while rounds <= max_rounds or part == 2:
        rounds += 1
        proposed_moves = []

        for row, col in elves:
            surrounding = [propose_move(elves, dr, row, col) for dr in directions]
            if all(list(zip(*surrounding))[0]) or not any(list(zip(*surrounding))[0]):
                proposed_moves += [(row, col)]
                continue
            for i, j in surrounding:
                if i:
                    proposed_moves += [j]
                    break

        c = Counter(proposed_moves)

        new_pos = {
            proposed_move if c[proposed_move] == 1 else elve
            for elve, proposed_move in zip(elves, proposed_moves)
        }
        if not new_pos - elves:
            break
        elves = new_pos
        directions = directions[1:] + [directions[0]]

    if part == 1:
        print(
            (max(elves)[0] - min(elves)[0] + 1)
            * (
                max(elves, key=lambda x: x[1])[1]
                - min(elves, key=lambda x: x[1])[1]
                + 1
            )
            - len(elves)
        )
    elif part == 2:
        print(rounds)


simulate(elves=elves, directions=directions, max_rounds=10, part=1)

## Part 2
simulate(elves=elves, directions=directions, max_rounds=10, part=2)

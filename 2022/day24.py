# Python
## Part 1 + 2
import itertools
import pathlib

input_map = [
    row[1:-1] for row in pathlib.Path("data.txt").read_text().splitlines()[1:-1]
]
length, width = len(input_map), len(input_map[0])

directions = {">": 1, "<": -1, "^": -1, "v": 1}

initial_state = (-1, 0)
goal = (length, width - 1)

grid = {initial_state, goal}
blizzards = []

for i, j in enumerate(input_map):
    for k, l in enumerate(j):
        grid.add((i, k))
        if l in directions:
            blizzards.append([i, k, l])


def move_blizzards(y: int, x: int, dr: str) -> tuple[int, int, str]:
    match dr:
        case ">" | "<":
            return y, (x + directions[dr]) % width, dr
        case "^" | "v":
            return (y + directions[dr]) % length, x, dr


stack = {initial_state}
trip_direction = return_trip = 0

for turn in itertools.count():
    blizzards = [move_blizzards(y, x, dr) for y, x, dr in blizzards]
    blizz_pos = {(i, j) for i, j, _ in blizzards}

    next_tries = set()

    for own_pos in stack:
        next_tries |= (
            {
                (own_pos[0] + move[0], own_pos[1] + move[1])
                for move in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
            }
            & grid
        ) - blizz_pos

    if not trip_direction and goal in next_tries:
        print(f"Time taken: {turn + 1}")
        if return_trip:
            break
        next_tries = {goal}
        trip_direction += 1

    elif trip_direction and initial_state in next_tries:
        next_tries = {initial_state}
        trip_direction -= 1
        return_trip += 1

    stack = next_tries

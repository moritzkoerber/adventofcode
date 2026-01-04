# Part 1 + 2
from functools import cache
from pathlib import Path

p_input = Path("data.txt").read_text().splitlines()

num_pad = {
    col: (i, j)
    for i, row in enumerate(
        """789
456
123
 0A""".splitlines()
    )
    for j, col in enumerate(row)
    if col != " "
}

d_pad = {
    col: (i, j)
    for i, row in enumerate(
        """ ^A
<v>""".splitlines()
    )
    for j, col in enumerate(row)
    if col != " "
}


def calculate_paths(
    key1: str | tuple[int, int],
    key2: str | tuple[int, int],
    pad: dict[str, tuple[int, int]],
) -> list[str]:
    key1, key2 = pad[key1], pad[key2]
    to_do = [(key1, {key1}, "")]
    solutions = []

    while to_do:
        (y, x), visited, path = to_do.pop()

        if (y, x) == key2:
            solutions.append(path)
            continue

        for d, a in [([1, 0], "v"), ([-1, 0], "^"), ([0, 1], ">"), ([0, -1], "<")]:
            ny, nx = y + d[0], x + d[1]
            if (ny, nx) in pad.values() and (ny, nx) not in visited:
                to_do.append(
                    (
                        (ny, nx),
                        visited | {(ny, nx)},
                        path + a,
                    )
                )

    return solutions


@cache
def calculate_length(solution: str, robot: int) -> int:
    if robot == 0:
        return len(solution) + 1
    pad = num_pad if robot == robot_cnt else d_pad
    return sum(
        min(
            calculate_length(path, robot - 1)
            for path in calculate_paths(key1, key2, pad)
        )
        for key1, key2 in zip(f"A{solution}", f"{solution}A")
    )


for robot_cnt in [3, 26]:
    print(
        sum(
            int(code.strip("A")) * calculate_length(code.strip("A"), robot_cnt)
            for code in p_input
        )
    )

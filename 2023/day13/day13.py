# Part 1
import pathlib

patterns = list(map(str.splitlines, pathlib.Path("data.txt").read_text().split("\n\n")))


def check_reflection(grid: list[str], part2: bool = False) -> int:
    return next(
        (
            i + 1
            for i in range(len(grid) - 1)
            if sum(
                y == x for a, b in zip(grid[i::-1], grid[i + 1 :]) for x, y in zip(a, b)
            )
            == min(len(grid[i::-1]), len(grid[i + 1 :])) * len(grid[0]) - part2
        ),
        0,
    )


print(
    sum(
        check_reflection(pattern) * 100 + check_reflection(list(zip(*pattern)))
        for pattern in patterns
    )
)


# Part 2
print(
    sum(
        check_reflection(pattern, part2=True) * 100
        + check_reflection(list(zip(*pattern)), part2=True)
        for pattern in patterns
    )
)

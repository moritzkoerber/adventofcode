# Part 1
import math
import pathlib

races = pathlib.Path("data.txt").read_text().splitlines()
wins = dict.fromkeys(zip(*[map(int, e.split()[1:]) for e in races]), 0)


def calculate_wins(wins: dict[tuple[int, ...], int]) -> int:
    for t, d in wins:
        for i in range(t + 1):
            if (t - i) * i > d:
                wins[t, d] += 1
    return math.prod(wins.values())


print(calculate_wins(wins))

# Part 2
wins = {tuple(int(e.split(" ", 1)[1].replace(" ", "")) for e in races): 0}
print(calculate_wins(wins))

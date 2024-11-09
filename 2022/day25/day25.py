# Python
## Part 1
import pathlib

snafus = pathlib.Path("data.txt").read_text().splitlines()

from_snafu = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

s = sum(
    (5**i) * from_snafu[j] for number in snafus for i, j in enumerate(reversed(number))
)

to_snafu = dict(zip(from_snafu.values(), from_snafu.keys()))


def recur(s: int) -> str:
    quotient, remainder = divmod(s, 5)
    if remainder in (3, 4):
        quotient += 1
        remainder -= 5
    return (recur(quotient) if quotient else "") + to_snafu[remainder]


print(recur(s))

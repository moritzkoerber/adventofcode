# Python
## Part 1
from functools import reduce
from itertools import chain
from typing import Iterable

with open("data.txt") as f:
    items = f.read().splitlines()


def count_overlap(iterable: Iterable) -> int:
    return sum(
        ord(letter) - 38 - (58 * letter.islower())
        for letter in chain.from_iterable(
            [
                reduce(
                    lambda x, y: set(x) & set(y),
                    i,
                )
                for i in iterable
            ]
        )
    )


print(count_overlap([(i[: (len(i) // 2)], i[(len(i) // 2) :]) for i in items]))

## Part 2
print(count_overlap([items[i : i + 3] for i in range(0, len(items), 3)]))

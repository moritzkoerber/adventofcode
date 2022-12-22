# Python
## Part 1
with open("data.txt") as f:
    compartments = f.read().splitlines()


def count_overlap(comp1: str, *comp2: tuple[str, ...]) -> int:
    letter = (set(comp1).intersection(*comp2)).pop()
    return ord(letter) - 38 - 58 * letter.islower()


print(
    sum(count_overlap(*(i[: (len(i) // 2)], i[(len(i) // 2) :])) for i in compartments)
)


## Part 2
print(
    sum(
        count_overlap(*(compartments[i : i + 3]))
        for i in range(0, len(compartments), 3)
    )
)

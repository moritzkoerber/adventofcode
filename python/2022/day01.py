# Python
## Part 1
with open("day01.txt") as f:
    input_calories = f.read().split("\n\n")

calories_by_elf = sorted(
    map(
        sum,
        [map(int, elf.splitlines()) for elf in input_calories],
    )
)

print(calories_by_elf[-1])

## Part 2
print(sum(calories_by_elf[-3:]))

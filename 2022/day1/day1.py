# Python
## Part 1
with open("data.txt") as f:
    input_calories = f.read().split("\n\n")

calories_by_elf = map(
    sum,
    [[int(i) for i in elf.splitlines()] for elf in input_calories],
)

print(max(calories_by_elf))

## Part 2
print(sum(sorted(calories_by_elf)[-3:]))

# Pandas
## Part 1
import pandas

calories_by_elf = (
    pandas.read_table("data.txt", header=None, skip_blank_lines=False)
    .assign(elf_no=lambda x: x[0].isna().cumsum())
    .groupby("elf_no")
    .sum()[0]
    .sort_values()
)
calories_by_elf.max()

## Part 2
calories_by_elf.tail(3).sum()

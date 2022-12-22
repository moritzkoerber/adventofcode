import pandas

# Python
## Part 1
calories_by_elf = map(
    sum,
    [
        [int(i) for i in elf.splitlines()]
        for elf in open("data.txt").read().split("\n\n")
    ],
)
max(calories_by_elf)

## Part 2
sum(sorted(calories_by_elf)[-3:])

# Pandas
## Part 1
calories_by_elf = (
    pandas.read_table("data.txt", header=None, skip_blank_lines=False)
    .assign(elf_no=lambda x: x[0].isna().cumsum())
    .groupby("elf")
    .sum()[0]
    .sort_values()
)
calories_by_elf.max()

## Part 2
calories_by_elf.tail(3).sum()

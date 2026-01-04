# Part 1
import pathlib
import re

tinput = pathlib.Path("data.txt").read_text().splitlines()

pattern = re.compile(r"\d+")

parsed_numbers = [
    list(map(pattern.findall, line.split(": ")[-1].split(" | "))) for line in tinput
]

print(
    sum(
        2 ** (len(s) - 1) if (s := set(l1) & set(l2)) else 0
        for l1, l2 in parsed_numbers
    )
)

# Part 2
card_stack = dict.fromkeys(range(len(tinput)), 1)

for i, (l1, l2) in enumerate(parsed_numbers):
    wins = len(set(l1) & set(l2))
    for c in range(i + 1, i + wins + 1):
        card_stack[c] += card_stack[i]
print(sum(card_stack.values()))

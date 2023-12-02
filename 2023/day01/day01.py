# Part 1
import pathlib
import re

lines = pathlib.Path("data.txt").read_text().splitlines()

print(
    sum(
        int(f"{match[0]}{match[-1]}")
        for line in lines
        if (match := re.findall(r"\d", line))
    )
)

# Part 2
digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern = "|".join([*digits, r"\d"])

first_last_matches = zip(
    [
        digits.get(match[0], match[0])
        for line in lines
        if (match := re.search(pattern, line))
    ],
    [
        digits.get(match[-1], match[-1])
        for line in lines
        if (match := re.findall(rf"(?=({pattern}))", line))
    ],
)

print(sum(int(first + last) for first, last in first_last_matches))

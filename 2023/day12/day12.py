# Part 1
import pathlib
import re
from functools import cache

springs = pathlib.Path("data.txt").read_text().splitlines()
number_regex = re.compile(r"\d+")


@cache
def find_solutions(
    input_string: str, groups: tuple[int, ...], places_available: int = 0
) -> int:
    if not input_string:
        return not (places_available or groups)
    num_solutions = 0
    current_symbol = input_string[0].replace("?", ".#")

    if "#" in current_symbol:
        num_solutions += find_solutions(input_string[1:], groups, places_available + 1)
    if "." in current_symbol:
        if places_available:
            if groups and groups[0] == places_available:
                num_solutions += find_solutions(input_string[1:], groups[1:])
        else:
            num_solutions += find_solutions(input_string[1:], groups)
    return num_solutions


print(
    sum(
        find_solutions(
            row.split(" ")[0] + ".",
            tuple(map(int, number_regex.findall(row))),
        )
        for row in springs
    )
)

# Part 2
print(
    sum(
        find_solutions(
            "?".join([row.split(" ")[0]] * 5) + ".",
            tuple(map(int, number_regex.findall(row) * 5)),
        )
        for row in springs
    )
)

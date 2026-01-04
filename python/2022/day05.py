# Python
## Part 1
import re

with open("data.txt") as f:
    moves = f.read().splitlines()

with open("stack.txt") as f:
    stack = f.read().splitlines()

moves_int = [[int(x) for x in re.findall(r"\d+", i)] for i in moves]
matrix = [re.findall(r"[A-Z]|\s{4}", line) for line in stack][:-1]
matrix_t = [
    list(filter(lambda x: x != "    ", sublist))[::-1] for sublist in list(zip(*matrix))
]


def move_func(
    input_matrix: list[list[str]], order: int, s1: int, s2: int, cnt: int
) -> None:
    input_matrix[s1 - 1].extend(input_matrix[s2 - 1][-cnt:][::order])
    input_matrix[s2 - 1] = input_matrix[s2 - 1][:-cnt]


cranes = {"CrateMover 9000": -1, "CrateMover 9001": 1}

matrix_part_1 = matrix_t.copy()

for i in moves_int:
    move_func(matrix_part_1, cranes["CrateMover 9000"], i[2], i[1], i[0])

## Part 2
matrix_part_2 = matrix_t.copy()

for i in moves_int:
    move_func(matrix_part_2, cranes["CrateMover 9001"], i[2], i[1], i[0])

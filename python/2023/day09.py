# Part 1
import pathlib

num_lists = pathlib.Path("data.txt").read_text().splitlines()

nums = [list(map(int, line.split())) for line in num_lists]


def calculate_differences(num_list: list[int]) -> list[int]:
    return [b - a for a, b in zip(num_list, num_list[1:])]


def extrapolate(num_list: list[int]) -> int:
    diffs = [b - a for a, b in zip(num_list, num_list[1:])]
    return (num_list[-1] + extrapolate(diffs)) if diffs else 0


print(sum(map(extrapolate, nums)))


# Part 2
def extrapolate_back(num_list: list[int]) -> int:
    diffs = [b - a for a, b in zip(num_list, num_list[1:])]
    return (num_list[0] - extrapolate_back(diffs)) if diffs else 0


print(sum(map(extrapolate_back, nums)))

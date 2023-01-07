# Python
## Part 1
import re

with open("data.txt") as f:
    file_paths = f.read().splitlines()


root = current_path = {}
paths = []

for string in file_paths:
    arg = string.split()[-1]
    if string.startswith("$ cd .."):
        current_path = paths.pop()
    elif string.startswith("$ cd"):
        if arg == "/":
            current_path = root
            paths = []
        else:
            current_path[arg] = current_path.get(arg, {})
            paths.append(current_path)
            current_path = current_path[arg]
    elif string.startswith("dir"):
        current_path[arg] = current_path.get(arg, {})
    elif regex := re.match(r"^\d+", string):
        current_path[arg] = int(regex.group())

size_limit = 100000
total = 0
all_dir_sizes = []


def parse_path_size(path: dict | int) -> int:
    if isinstance(path, int):
        return path
    if isinstance(path, dict):
        if (res := sum(parse_path_size(x) for x in path.values())) <= size_limit:
            global total
            total += res
        all_dir_sizes.append(res)
        return res


root_size = parse_path_size(root)

print(total)

## Part 2
print(sorted(filter(lambda x: x >= 30000000 - 70000000 + root_size, all_dir_sizes))[0])

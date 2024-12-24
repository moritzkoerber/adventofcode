# Part 1
from itertools import zip_longest
from pathlib import Path

p_input = Path("data.txt").read_text().strip()


def calc_checksum(p_input: str, is_part1: bool) -> int:
    spaces = []
    files = []
    disk_map = []
    file_id = 0
    pos = 0

    for file_id, (file, space) in enumerate(
        zip_longest(p_input[::2], p_input[1::2], fillvalue=0)
    ):
        if not is_part1:
            files.append((pos, int(file)))
        for _ in range(int(file)):
            disk_map.append(file_id)
            if is_part1:
                files.append((pos, 1))
            pos += 1

        spaces.append((pos, int(space)))
        for _ in range(int(space)):
            disk_map.append(0)
        pos += int(space)

    for file_pos, file_size in reversed(files):
        for space, (space_pos, space_size) in enumerate(spaces):
            if file_size <= space_size and file_pos > space_pos:
                for i in range(file_size):
                    disk_map[space_pos + i], disk_map[file_pos + i] = (
                        disk_map[file_pos + i],
                        disk_map[space_pos + i],
                    )
                spaces[space] = space_pos + file_size, space_size - file_size
                break

    return sum(i * int(num) for i, num in enumerate(disk_map))


print(calc_checksum(p_input, True))

# Part 2
print(calc_checksum(p_input, False))

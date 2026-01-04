# Part 1
import pathlib

p_input = pathlib.Path("data.txt").read_text()

arrays = [int(num) for line in p_input.splitlines() for num in line.split()]
array_left, array_right = sorted(arrays[::2]), sorted(arrays[1::2])

print(sum(abs(left - right) for left, right in zip(array_left, array_right)))

# Part 2
print(sum(num * array_right.count(num) for num in array_left))

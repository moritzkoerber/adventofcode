# Python
## Part 1
import re

pattern = re.compile(r"-?\d+")

with open("data.txt") as f:
    parsed_input = [
        [int(x) for x in p] for p in map(pattern.findall, f.read().splitlines())
    ]


def calculate_intervals(target_row: int, exclude_beacons: bool) -> list[list[int]]:
    intervals = []
    for sensor_x, sensor_y, beacon_x, beacon_y in parsed_input:
        d = sum([abs(sensor_x - beacon_x), abs(sensor_y - beacon_y)])
        if (residual := d - abs(sensor_y - target_row)) > 0:
            low, high = sensor_x - residual, sensor_x + residual
            if exclude_beacons:
                if [low, target_row] == [beacon_x, beacon_y]:
                    low += 1
                if [high, target_row] == [beacon_x, beacon_y]:
                    high -= 1
            intervals.append([low, high])
    return intervals


impossible_values = calculate_intervals(2000000, exclude_beacons=True)

print(len(set.union(*[set(range(low, high + 1)) for low, high in impossible_values])))

## Part 2

dims = 0, 4000000

for row in range(dims[0], dims[1] + 1):
    impossible_values = sorted(calculate_intervals(row, exclude_beacons=False))

    combined_intervals = [[dims[0]] * 2, impossible_values[0]]

    for low, high in impossible_values[1:]:
        if low > combined_intervals[-1][1]:
            combined_intervals.append([low, high])
        combined_intervals[-1][1] = max(combined_intervals[-1][1], high)

    combined_intervals.append([dims[1]] * 2)

    for i, (_, high) in enumerate(combined_intervals[:-1]):
        if combined_intervals[i + 1][0] - high > 1:
            print(row + (high + 1) * dims[1])
            break

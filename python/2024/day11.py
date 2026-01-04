# Part 1
from functools import cache
from pathlib import Path

stones = Path("data.txt").read_text().strip().split()


@cache
def solve(stone: str, remaining_blinks: int) -> int:
    if remaining_blinks == 0:
        return 1
    remaining_blinks -= 1

    if stone == "0":
        return solve("1", remaining_blinks)
    if len(stone) % 2:
        return solve(str(int(stone) * 2024), remaining_blinks)
    half = len(stone) // 2
    return sum(
        solve(s, remaining_blinks) for s in [stone[:half], str(int(stone[half:]))]
    )


print(sum(solve(stone, 25) for stone in stones))

# Part 2
print(sum(solve(stone, 75) for stone in stones))

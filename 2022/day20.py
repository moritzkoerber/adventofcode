# Python
## Part 1
with open("data.txt") as f:
    moves = list(map(int, f.read().splitlines()))


def move_numbers(moves: list[int], rounds: int = 1, decryption_key: int = 1) -> int:
    decrypted_moves = [m * decryption_key for m in moves]
    indices = list(range(len(decrypted_moves)))

    for i in indices * rounds:
        idx = indices.index(i)
        indices.pop(idx)
        indices.insert((idx + decrypted_moves[i]) % len(indices), i)

    res = [decrypted_moves[i] for i in indices]
    return sum(res[(res.index(0) + offset) % len(res)] for offset in [1000, 2000, 3000])


print(move_numbers(moves))

## Part 2
print(move_numbers(moves, 10, 811589153))

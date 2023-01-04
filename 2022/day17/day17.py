# Python
## Part 1
import itertools

with open("data.txt") as f:
    jet_seq = [1 if x == ">" else -1 for x in f.read()]


def create_rock(ceiling: int) -> list[set[tuple[int, ...]]]:
    return [
        {(x, ceiling) for x in range(2, 6)},
        {
            (2, ceiling + 1),
            (3, ceiling),
            (3, ceiling + 1),
            (3, ceiling + 2),
            (4, ceiling + 1),
        },
        {
            (2, ceiling),
            (3, ceiling),
            (4, ceiling),
            (4, ceiling + 1),
            (4, ceiling + 2),
        },
        {
            (2, ceiling),
            (2, ceiling + 1),
            (2, ceiling + 2),
            (2, ceiling + 3),
        },
        {
            (2, ceiling),
            (2, ceiling + 1),
            (3, ceiling),
            (3, ceiling + 1),
        },
    ]


def create_topline(rock_positions: set) -> tuple[int, tuple[int, ...]]:
    top_line = [-1 for _ in range(7)]
    for x, y in rock_positions:
        top_line[x] = max(y, top_line[x])
    return max(top_line), tuple(e - max(top_line) for e in top_line)


def simulate_rocks(n: int, jet_seq: list[int]) -> int:
    ceiling = 0
    rock_positions = {(x, 0) for x in range(7)}
    state = {}
    jet_ids = itertools.cycle(range(len(jet_seq)))

    for rock_type, rock_count in zip(itertools.cycle(range(5)), itertools.count(1)):
        if rock_count > n:
            break

        rock = create_rock(ceiling + 4)[rock_type]

        for jet_id in jet_ids:
            jet = jet_seq[jet_id]
            if (
                all(x + jet >= 0 and x + jet < 7 for x, _ in rock)
                and not (moved_rock := {(j + jet, k) for j, k in rock}) & rock_positions
            ):
                rock = moved_rock
            if (moved_rock := {(j, k - 1) for j, k in rock}) & rock_positions:
                rock_positions |= rock
                ceiling, top_line = create_topline(rock_positions)
                if (rock_type, jet_id, top_line) in state:
                    seen_count, seen_ceiling = state[rock_type, jet_id, top_line]
                    period_length = rock_count - seen_count
                    periods = (n - period_length) // period_length
                    extrapolated = periods * (ceiling - seen_ceiling)
                    n -= periods * period_length
                    state.clear()
                else:
                    state[rock_type, jet_id, top_line] = (rock_count, ceiling)
                break
            rock = moved_rock

    return ceiling + extrapolated


simulate_rocks(2022, jet_seq)

## Part 2
simulate_rocks(1000000000000, jet_seq)

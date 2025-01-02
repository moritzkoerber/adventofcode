# Python
# based on https://tinyurl.com/3kktsd2m
## Part 1
import functools
import re
from collections import defaultdict

pattern = re.compile(r"[A-Z]{2}|\d+")

with open("data.txt") as f:
    input_valves = f.read()

valves = {
    valve: {"flow_rate": int(flow_rate), "tunnels": leads}
    for valve, flow_rate, *leads in map(pattern.findall, input_valves.splitlines())
}

distances = defaultdict(lambda: float("inf")) | {
    (k, ov): 1 for k, v in valves.items() for ov in v["tunnels"]
}

for k in valves:
    for i in valves:
        for j in valves:
            distances[(i, j)] = min(
                distances[(i, j)], distances[(i, k)] + distances[(k, j)]
            )

closed_valuable_valves = frozenset(k for k, v in valves.items() if v["flow_rate"] > 0)


@functools.cache
def solve(current: str, time_left: int, available_valves: frozenset) -> int:
    return max(
        [
            valves[valve]["flow_rate"] * (time_left - distances[(current, valve)] - 1)
            + solve(
                valve,
                time_left - distances[(current, valve)] - 1,
                available_valves - {valve},
            )
            for valve in available_valves
            if time_left - distances[(current, valve)] > 0
        ]
        + [0]
    )


print(solve("AA", 30, closed_valuable_valves))


## Part 2
@functools.cache
def solve_with_elephant(
    current: str, time_left: int, available_valves: frozenset
) -> int:
    return max(
        [
            valves[valve]["flow_rate"] * (time_left - distances[(current, valve)] - 1)
            + solve_with_elephant(
                valve,
                time_left - distances[(current, valve)] - 1,
                available_valves - {valve},
            )
            for valve in available_valves
            if time_left - distances[(current, valve)] > 0
        ]
        + [solve("AA", 26, available_valves) or 0]
    )


print(solve_with_elephant("AA", 26, closed_valuable_valves))

# Part 1
from collections import defaultdict
from pathlib import Path

p_input = Path("data.txt").read_text().splitlines()

conns = defaultdict(set)

for cs in p_input:
    c1, c2 = cs.split("-")
    conns[c1].add(c2)
    conns[c2].add(c1)

cliques = {
    tuple(sorted((c1, c2, c3)))
    for c1 in conns
    for c2 in conns[c1]
    for c3 in conns[c2]
    if c3 in conns[c1]
}

print(sum("t" in a + b + c for (a, _), (b, _), (c, _) in cliques))


# Part 2
def find_cliques(conns: dict[str, set[str]]) -> set[tuple[str, ...]]:
    found = set()

    def _solve(
        c1: str,
        seen: tuple[str, ...],
    ) -> None:
        seen = tuple(sorted(seen))
        if seen in found:
            return
        found.add(seen)
        for c2 in conns[c1]:
            if c2 not in seen and all(c2 in conns[prev] for prev in seen):
                _solve(c2, (*seen, c2))

    for c in conns:
        _solve(c, (c,))

    return found


print(",".join(sorted(max(find_cliques(conns), key=len))))

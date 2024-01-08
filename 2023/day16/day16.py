# Part 1
import pathlib

contraption = pathlib.Path("data.txt").read_text().splitlines()

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

H, W = len(contraption), len(contraption[0])

configs = (
    [(y, -1, 1) for y in range(H)]
    + [(y, W, 3) for y in range(H)]
    + [(-1, x, 2) for x in range(W)]
    + [(H, x, 0) for x in range(W)]
)


def solve(config: tuple[int, int, int]) -> int:
    visited = set()
    beams = [config]
    while beams:
        y, x, d = beams.pop()
        ny, nx = y + dirs[d][0], x + dirs[d][1]
        if 0 <= ny < H and 0 <= nx < W and (ny, nx, d) not in visited:
            nxt = contraption[ny][nx]
            if nxt == "-" and d in [0, 2]:
                nd = [1, 3]
            elif nxt == "/":
                nd = [[1, 0, 3, 2].index(d)]
            elif nxt == "\\":
                nd = [[3, 2, 1, 0].index(d)]
            elif nxt == "|" and d in [1, 3]:
                nd = [0, 2]
            else:
                nd = [d]
            beams.extend((ny, nx, e) for e in nd)
            visited.add((ny, nx, d))

    return len({(y, x) for y, x, _ in visited})


print(max(map(solve, configs[:1])))

# Part 2
print(max(map(solve, configs)))

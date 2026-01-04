# Python
## Part 1
with open("data.txt") as f:
    moves = list(map(str.split, f.read().splitlines()))

move_dict = {"L": (-1, 0), "R": (1, 0), "D": (0, -1), "U": (0, 1)}

h = [0, 0]
t = (0, 0)

t_positions = {t}

for m in moves:
    for _ in range(int(m[1])):
        curr_h = h.copy()
        h[0] += move_dict[m[0]][0]
        h[1] += move_dict[m[0]][1]
        if max(abs(h[0] - t[0]), abs(h[1] - t[1])) <= 1:
            continue
        t = tuple(curr_h)
        t_positions.add(t)

print(len(t_positions))

## Part 2
worm_length = 10

w = [[0, 0] for _ in range(worm_length)]

t_positions = {(0, 0)}

for m in moves:
    for _ in range(int(m[1])):
        w[0][0] += move_dict[m[0]][0]
        w[0][1] += move_dict[m[0]][1]
        for i in range(worm_length - 1):
            h = w[i]
            t = w[i + 1]
            if (
                max(
                    [
                        abs(h[0] - t[0]),
                        abs(h[1] - t[1]),
                    ]
                )
                > 1
            ):
                if x := h[0] - t[0]:
                    t[0] += 1 if (x > 0) else -1
                if y := h[1] - t[1]:
                    t[1] += 1 if (y > 0) else -1
        t_positions.add(tuple(w[-1]))

print(len(t_positions))

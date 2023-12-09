# Part 1
import pathlib

seeds, *mappings = pathlib.Path("data.txt").read_text().split("\n\n")
seeds = list(map(int, seeds.split()[1:]))

res = []

for seed in seeds:
    for m in mappings:
        for dest, source, end in [
            map(int, triple.split()) for triple in m.split("\n")[1:]
        ]:
            if source <= seed <= (source + end):
                # convert
                delta = seed - source
                seed = dest + delta
                break
    res.append(seed)

print(min(res))

# Part 2
res = []
for seed_start, end in zip(seeds[::2], seeds[1::2]):
    todo = [(seed_start, seed_start + end)]
    for m in mappings:
        new_seeds = []
        while todo:
            ll, ul = todo.pop()
            for dest, src, end in [
                map(int, triple.split()) for triple in m.split("\n")[1:]
            ]:
                lo = max(ll, src)
                uo = min(ul, src + end)
                if lo < uo:
                    delta = dest - src
                    new_seeds.append((lo + delta, uo + delta))
                    if ll < lo:
                        todo.append((ll, lo))
                    if uo < ul:
                        todo.append((uo, ul))
                    break
            else:
                new_seeds.append((ll, ul))
        todo = new_seeds
    res.append(min(todo))
print(min(res)[0])

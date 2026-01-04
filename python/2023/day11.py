# Part 1, 2
import pathlib

galaxy_map = pathlib.Path("data.txt").read_text().splitlines()

galaxies = [
    (i, j)
    for i, row in enumerate(galaxy_map)
    for j, col in enumerate(row)
    if col == "#"
]
horizontal = {i for i, row in enumerate(galaxy_map) if row.find("#") == -1}
vertical = {
    i
    for i, row in enumerate(list(map("".join, zip(*galaxy_map))))
    if row.find("#") == -1
}

for expansion_factor in [2, 10**6]:
    distance = 0
    for n, (i, j) in enumerate(galaxies, 1):
        for i2, j2 in galaxies[n:]:
            distance += (
                abs(i - i2)
                + abs(j - j2)
                + (expansion_factor - 1)
                * (
                    len(set(range(*sorted([i, i2]))) & horizontal)
                    + len(set(range(*sorted([j, j2]))) & vertical)
                )
            )
    print(distance)

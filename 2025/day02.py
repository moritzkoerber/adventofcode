# Part 1 + 2
import pathlib

p_input = pathlib.Path("data.txt").read_text()

product_ids = [
    str(product_id)
    for x, y in [p.split("-") for p in p_input.split(",")]
    for product_id in range(*[int(x), int(y) + 1])
]

part1, part2 = 0, 0
for product_id in product_ids:
    if product_id[: len(product_id) // 2] == product_id[len(product_id) // 2 :]:
        part1 += int(product_id)
    for i in range(1, len(product_id)):
        if product_id[:i] * (len(product_id) // i) == product_id:
            part2 += int(product_id)
            break

print(part1, part2, sep="\n")

# Part 1
from pathlib import Path

rules, pages = Path("data.txt").read_text().split("\n\n")

pages = [page.split(",") for page in pages.splitlines()]


def calc_indices(page: list[str]) -> list[int]:
    return [len(page) - 1 - sum(f"{p1}|{p2}" in rules for p2 in page) for p1 in page]


print(
    sum(
        (calc_indices(page) == list(range(len(page)))) * int(page[len(page) // 2])
        for page in pages
    )
)

# Part 2
print(
    sum(
        (calc_indices(page) != list(range(len(page))))
        * int(page[calc_indices(page).index(len(page) // 2)])
        for page in pages
    )
)

# Part 1
from collections import defaultdict
from pathlib import Path

p_input = list(map(int, Path("data.txt").read_text().splitlines()))


def transform(secret_num: int) -> int:
    secret_num ^= (secret_num * 64) % 16777216
    secret_num ^= (secret_num // 32) % 16777216
    secret_num ^= (secret_num * 2048) % 16777216
    return secret_num


bananas = defaultdict(int)
ans1 = 0

for secret_num in p_input:
    sales_offers = {}
    deltas = ()
    price = secret_num % 10
    for _ in range(2000):
        secret_num = transform(secret_num)
        price, prev = secret_num % 10, price
        deltas = (*deltas[-3:], price - prev)

        if len(deltas) == 4 and deltas not in sales_offers:
            sales_offers[deltas] = price

    ans1 += secret_num

    for sequence, price in sales_offers.items():
        bananas[sequence] += price

print(ans1)

# Part 2
print(max(bananas.values()))

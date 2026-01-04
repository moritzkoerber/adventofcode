# Part 1
import pathlib
from collections import Counter

read_input = pathlib.Path("data.txt").read_text()

input_values = {
    hand: int(bet) for hand, bet in [line.split() for line in read_input.splitlines()]
}

order = "AKQJT98765432"[::-1]

sorted_hands = sorted(
    input_values,
    key=lambda hand: (
        sorted(Counter(hand).values(), reverse=True),
        list(map(order.index, hand)),
    ),
)

print(sum(rank * input_values[hand] for rank, hand in enumerate(sorted_hands, 1)))

# Part 2
order = "AKQT98765432J"[::-1]

sorted_hands = sorted(
    input_values,
    key=lambda hand: (
        max(
            [
                sorted(Counter(hand.replace("J", new)).values(), reverse=True)
                for new in hand
                if new != "J"
            ]
            or [[5]]
        ),
        list(map(order.index, hand)),
    ),
)

print(sum(rank * input_values[hand] for rank, hand in enumerate(sorted_hands, 1)))

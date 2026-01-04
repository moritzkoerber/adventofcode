# Python
## Part 1
import copy
import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import reduce


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    worry_reduction: int
    test_var: int
    monkey_true: int
    monkey_false: int
    inspect_count: int = 0


with open("data.txt") as f:
    data = f.read().splitlines()
    chunks = [data[i : i + 7] for i in range(0, len(data), 7)]
    number_regex = re.compile(r"\d+")
    monkeys = []
    for i in chunks:
        items = list(map(int, number_regex.findall(i[1])))
        operation = eval("lambda old:" + i[2].removeprefix("  Operation: new = "))
        test_var = int(number_regex.search(i[3]).group())
        monkey_true = int(number_regex.search(i[4]).group())
        monkey_false = int(number_regex.search(i[5]).group())
        monkeys.append(Monkey(items, operation, 3, test_var, monkey_true, monkey_false))


def play_rounds(number_of_rounds: int, monkey_list: list) -> int:
    for _ in range(number_of_rounds):
        for monkey in monkey_list:
            monkey.inspect_count += len(monkey.items)
            for item in monkey.items:
                if (
                    i := monkey.operation(item) // monkey.worry_reduction
                ) % monkey.test_var == 0:
                    monkey_list[monkey.monkey_true].items.append(i)
                else:
                    monkey_list[monkey.monkey_false].items.append(i)
            monkey.items.clear()
    return reduce(
        lambda x, y: x * y,
        sorted([monkey.inspect_count for monkey in monkey_list])[-2:],
    )


play_rounds(20, copy.deepcopy(monkeys))

## Part 2
super_mod = reduce(lambda x, y: x * y, [monkey.test_var for monkey in monkeys])


def decorate(func):
    def wrap(*args):
        return func(*args) % super_mod

    return wrap


for monkey in monkeys:
    monkey.worry_reduction = 1
    monkey.operation = decorate(monkey.operation)

play_rounds(10000, copy.deepcopy(monkeys))

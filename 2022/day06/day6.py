# Python
## Part 1
with open("data.txt") as f:
    signal = f.read()


def search_signal(signal_string: str, signal_length: int) -> int | None:
    c = signal_string[: signal_length - 1]
    for i in signal_string[signal_length - 1 :]:
        if i in c:
            c = c[c.index(i) + 1 :] + i
            continue
        c += i
        if len(set(c)) == signal_length:
            return signal_string.index(c) + signal_length


print(search_signal(signal, 4))

## Part 2
print(search_signal(signal, 14))

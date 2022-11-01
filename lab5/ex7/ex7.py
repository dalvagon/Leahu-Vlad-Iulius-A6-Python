def first_n_fibonacci(n):
    x = 0
    y = 1
    z = x + y
    seq = [x, y]

    for count in range(0, n - 2):
        x = y
        y = z
        z = x + y
        seq.append(z)

    return seq


def process(**kvs):
    fibonacci_seq = first_n_fibonacci(1000)

    for key in kvs.keys():
        if key == "filters":
            for fltr in kvs[key]:
                fibonacci_seq = list(filter(fltr, fibonacci_seq))

        elif key == "offset":
            fibonacci_seq = fibonacci_seq[kvs[key] :]

    for key in kvs.keys():
        if key == "limit":
            fibonacci_seq = fibonacci_seq[: kvs[key]]

    return fibonacci_seq


def sum_digits(x):

    return sum(map(int, str(x)))


if __name__ == "__main__":
    print(
        process(
            filters=[
                lambda item: item % 2 == 0,
                lambda item: item == 2 or 4 <= sum_digits(item) <= 20,
            ],
            limit=2,
            offset=2,
        )
    )

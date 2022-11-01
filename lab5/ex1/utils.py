def is_prime(x):
    if x == 1 or x == 0:
        return False

    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False

    return True


def process_item(x):
    while not is_prime(x):
        x += 1

    return x


if __name__ == "__main__":
    print("Enter a number: ")
    print(process_item(int(input())))

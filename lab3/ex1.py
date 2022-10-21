def sets_operations(a, b):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]


if __name__ == "__name__":
    print(sets_operations(range(1, 11), range(5, 21)))

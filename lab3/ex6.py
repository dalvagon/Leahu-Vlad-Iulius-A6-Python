def list_count(lst):
    return (len(set(lst)), len(lst) - len(set(lst)))


if __name__ == "__main__":
    print(list_count([1, 2, 4, 1, 2, 3, 6, 7, 1]))

# Ex 10
def list_of_tuples(*lists):
    return [
        tuple([lst[index] if index < len(lst) else None for lst in lists])
        for index in range(0, max([len(lst) for lst in lists]))
    ]


if __name__ == "__main__":
    print(list_of_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c", "d"]))

def odd_even_tuples(lst):
    evens = list(filter(lambda x: x % 2 == 0, lst))
    odds = [elem for elem in lst if not elem in evens]

    return list(zip(evens, odds))


if __name__ == "__main__":
    print(odd_even_tuples([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

def get_numbers(lst):
    return [item for item in lst if isinstance(item, int) or isinstance(item, float)]


if __name__ == "__main__":
    print(get_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

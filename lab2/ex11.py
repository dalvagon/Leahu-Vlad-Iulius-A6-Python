# Ex 11
def sort_tuples(tuples):
    return sorted(tuples, key=lambda tuple: tuple[1][2])


if __name__ == "__main__":
    print(sort_tuples([("abc", "bcd"), ("abc", "zza")]))

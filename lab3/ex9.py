def count_values(*numbers, **kvs):
    return len(
        [
            number
            for number in numbers
            if len([key for key in kvs.keys() if kvs[key] == number])
        ]
    )


if __name__ == "__main__":
    print(count_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))

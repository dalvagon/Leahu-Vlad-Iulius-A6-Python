def count_values(*numbers, **kvs):
    count = 0
    for number in numbers:
        for key in kvs.keys():
            if kvs[key] == number:
                count += 1
                break

    return count


if __name__ == "__main__":
    print(count_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))

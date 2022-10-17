# Ex 3
def sets_operations(set_a, set_b):
    def union(set_a, set_b):
        set_c = []
        for number in set_a + set_b:
            if not number in set_c:
                set_c.append(number)

        return set_c

    def intersection(set_a, set_b):
        set_c = []
        for number in set_a + set_b:
            if not number in set_c and number in set_a and number in set_b:
                set_c.append(number)

        return set_c

    def difference_a(set_a, set_b):
        set_c = []
        for number in set_a + set_b:
            if not number in set_c and number in set_a and not number in set_b:
                set_c.append(number)

        return set_c

    def difference_b(set_a, set_b):
        set_c = []
        for number in set_a + set_b:
            if not number in set_c and not number in set_a and number in set_b:
                set_c.append(number)

        return set_c

    return (
        union(set_a, set_b),
        intersection(set_a, set_b),
        difference_a(set_a, set_b),
        difference_b(set_a, set_b),
    )


if __name__ == "__main__":
    print(
        sets_operations(
            [number for number in range(11)], [number for number in range(5, 16)]
        )
    )

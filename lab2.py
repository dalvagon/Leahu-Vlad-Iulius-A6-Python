# Ex 1
def first_fibonacci_numbers(n):
    def nth_fibonacci_number(n):
        if n == 0 or n == 1:
            return n
        else:
            return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)

    return [nth_fibonacci_number(number) for number in range(0, n)]


# Ex 2
def prime_numbers(numbers):
    def is_prime(number):
        if number == 0 or number == 1:
            return False

        for d in range(2, number // 2 + 1):
            if number % d == 0:
                return False

        return True

    return [number for number in numbers if is_prime(number)]


# EX 3
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


# Ex 4
def compose(notes, moves, start_position):
    moves = [start_position] + moves

    return [
        notes[sum([moves[index2] for index2 in range(0, index1 + 1)]) % len(moves)]
        for index1 in range(0, len(moves))
    ]


# Ex 5
def replace_elements_under_the_main_diagonal(numbers):
    for lines in numbers:
        if len(lines) != len(numbers):
            return "The matrix is not square"

    return [
        [0 if i > j else numbers[i][j] for j in range(0, len(numbers[i]))]
        for i in range(0, len(numbers))
    ]


# Ex 6
def build_appearance_list(*lists, x):
    lst = []
    ret_lst = []
    for l in lists:
        lst += l

    for element in lst:
        if lst.count(element) == x and not element in ret_lst:
            ret_lst.append(element)

    return ret_lst


# Ex 7
def palindrome_tuple(numbers):
    def is_palindrome(number):
        string = str(number)
        return string == string[::-1]

    ret_lst = [number for number in numbers if is_palindrome(number)]

    return (ret_lst, max(ret_lst))


if __name__ == "__main__":
    # print(first_fibonacci_numbers(30))

    # print(prime_numbers([number for number in range(1, 100)]))

    # print(
    #     sets_operations(
    #         [number for number in range(11)], [number for number in range(5, 16)]
    #     )
    # )

    # print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

    # print(
    #     replace_elements_under_the_main_diagonal(
    #         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    #     )
    # )

    # print(build_appearance_list([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))

    print(palindrome_tuple([number for number in range(100)]))

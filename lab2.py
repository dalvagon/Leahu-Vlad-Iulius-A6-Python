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


# Ex 8
def ascii_divisible_characters(strings, x=1, flag=True):
    int_flag = 0
    if not flag:
        int_flag = 1

    return [
        [character for character in string if ord(character) % x == int_flag]
        for string in strings
    ]


# Ex 9
def blind_spectators(matrix):
    return [
        (index1, index2)
        for index1 in range(0, len(matrix))
        for index2 in range(0, len(matrix[0]))
        if len(
            [
                matrix[index3][index2]
                for index3 in range(0, index1)
                if (matrix[index1][index2] <= matrix[index3][index2])
            ]
        )
        > 0
    ]


# Ex 10
def list_of_tuples(*lists):
    length = max([len(lst) for lst in lists])
    return [
        tuple([lst[index] if index < len(lst) else None for lst in lists])
        for index in range(0, length)
    ]


# Ex 11
def sort_tuples(tuples):
    return sorted(tuples, key=lambda tuple: tuple[1][2])


# Ex 12
def group_by_rhyme(words):
    ret_list = []
    for word in words:
        rhyming_words_list = [
            other_word for other_word in words if word[-2:] == other_word[-2:]
        ]
        if not rhyming_words_list in ret_list:
            ret_list.append(rhyming_words_list)

    return ret_list


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

    # print(palindrome_tuple([number for number in range(100)]))

    # print(ascii_divisible_characters(["test", "hello", "lab002"], 2, False))

    # print(
    #     blind_spectators(
    #         [
    #             [1, 2, 3, 2, 1, 1],
    #             [2, 4, 4, 3, 7, 2],
    #             [5, 5, 2, 5, 6, 4],
    #             [6, 6, 7, 6, 7, 5],
    #         ]
    #     )
    # )

    # print(list_of_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c", "d"]))

    # print(sort_tuples([("abc", "bcd"), ("abc", "zza")]))

    print(group_by_rhyme(["ana", "banana", "carte", "arme", "parte"]))

# Ex 5
def replace_elements_under_the_main_diagonal(numbers):
    for lines in numbers:
        if len(lines) != len(numbers):
            return "The matrix is not square"

    return [
        [0 if i > j else numbers[i][j] for j in range(0, len(numbers[i]))]
        for i in range(0, len(numbers))
    ]


if __name__ == "__main__":
    print(
        replace_elements_under_the_main_diagonal(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
    )

# Ex 1
def gcd(numbers):
    def gcd2(x, y):
        if y == 0:
            return x
        while y:
            x, y = y, x % y
        return x

    if len(numbers) == 0:
        return "Empty list"
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return gcd([gcd2(numbers[0], numbers[1])] + numbers[2 : len(numbers)])


# Ex 2
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return len([character for character in string if character in vowels])


# Ex 3
def count_occurrences(string1, string2):
    return string2.count(string1)


# Ex 4
def convert_upper_camel_case_to_lowercase_with_underscores(string):
    for character in string:
        if character.isupper():
            string = string.replace(character, "_" + character.lower())

    return string[1 : len(string)]


# Ex 5
def spiral_order_string_from_matrix(matrix):
    length = len(matrix)
    row_start = 0
    row_end = length - 1
    column_start = 0
    column_end = length - 1
    elements = length * length
    string = []
    while elements:
        for index in range(row_start, row_end + 1):
            string.append(matrix[column_start][index])
            elements -= 1

        column_start += 1

        for index in range(column_start, column_end + 1):
            string.append(matrix[index][row_end])
            elements -= 1

        row_end -= 1

        for index in range(row_end, row_start - 1, -1):
            string.append(matrix[column_end][index])
            elements -= 1

        column_end -= 1

        for index in range(column_end, column_start - 1, -1):
            string.append(matrix[index][row_start])
            elements -= 1

        row_start += 1

    return string


# EX 6
def is_palindrome(number):
    string = str(number)
    print(string[::-1])
    return string == string[::-1]


# Ex 7
def extract_first_number(string):
    number = ""

    for character in string:
        if character >= "0" and character <= "9":
            number += character
        else:
            if len(number) > 0:
                break

    return number


# Ex 8
def count_bits(number):
    if number == 0:
        return 0
    else:
        return number % 2 + count_bits(number // 2)


# Ex 9
def most_common_letter(string):
    max_occurrences = 0
    letter = ""
    for character in string.replace(" ", ""):
        number_of_occurrences = string.count(character)
        if number_of_occurrences > max_occurrences:
            max_occurrences = number_of_occurrences
            letter = character

    return letter


# Ex 10
def count_words(string):
    return len(string.split())


if __name__ == "__main__":
    # print("Enter an array of numbers to compute their gcd:")
    # print(gcd([int(number) for number in input().split()]))

    # print("Enter a string to count it's vowels:")
    # print(count_vowels(input()))

    # print("Enter two strings to count the number of occurrences of the first string in the second:")
    # print(count_occurrences(input(), input()))

    # print("Enter a string written in UpperCamelCase to be converted into lowercase_with_underscores:")
    # print(convert_upper_camel_case_to_lowercase_with_underscores(input()))

    # print(spiral_order_string_from_matrix(['firs', 'n_lt', 'oba_', 'htyp']))
    # print(spiral_order_string_from_matrix(['abcde', 'pqrsf', 'oxytg', 'nwvuh', 'mlkji']))

    # print(is_palindrome(12321))

    # print(extract_first_number("ads sfa  faf192r "))

    # print(count_bits(24))

    # print(count_words("I have Python exam"));

    print(most_common_letter("an apple is not a tomato"))

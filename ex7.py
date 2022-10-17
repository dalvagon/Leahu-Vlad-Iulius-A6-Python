# Ex 7
def palindrome_tuple(numbers):
    def is_palindrome(number):
        string = str(number)
        return string == string[::-1]

    ret_lst = [number for number in numbers if is_palindrome(number)]

    return (len(ret_lst), max(ret_lst))


if __name__ == "__main__":
    print(palindrome_tuple([number for number in range(100)]))

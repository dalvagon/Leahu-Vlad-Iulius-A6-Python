# Ex 7
def palindrome_tuple(numbers):
    ret_lst = list(filter(lambda number: str(number) == str(number)[::-1], numbers))

    return (len(ret_lst), max(ret_lst))


if __name__ == "__main__":
    print(palindrome_tuple([number for number in range(100)]))

# Ex 1
def first_fibonacci_numbers(n):
    def nth_fibonacci_number(n):
        if n == 0 or n == 1:
            return n
        else:
            return nth_fibonacci_number(n - 1) + nth_fibonacci_number(n - 2)

    return [nth_fibonacci_number(number) for number in range(0, n)]


if __name__ == "__main__":
    print(first_fibonacci_numbers(30))

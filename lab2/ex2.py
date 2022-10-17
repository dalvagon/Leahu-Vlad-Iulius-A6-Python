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


if __name__ == "__main__":
    print(prime_numbers([number for number in range(1, 100)]))

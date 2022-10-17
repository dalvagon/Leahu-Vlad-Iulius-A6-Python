# Ex 8
def ascii_divisible_characters(strings, x=1, flag=True):
    return [
        [
            character
            for character in string
            if ord(character) % x == 0 and flag or ord(character) % x != 0 and not flag
        ]
        for string in strings
    ]


if __name__ == "__main__":
    print(ascii_divisible_characters(["test", "hello", "lab002"], 2, False))

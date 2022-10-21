def count_occurences(string):
    occurences = {}
    for character in string:
        occurences[character] = string.count(character)

    return occurences


if __name__ == "__main__":
    print(count_occurences("Ana has apples"))

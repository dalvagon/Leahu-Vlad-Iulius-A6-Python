def count_occurences(string):
    return {character: string.count(character) for character in string}


if __name__ == "__main__":
    print(count_occurences("Ana has apples"))

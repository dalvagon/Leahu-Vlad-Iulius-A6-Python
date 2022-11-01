def get_vowels(string):
    vowels = "aeiou"
    string_vowels = []

    for character in string:
        if character.lower() in vowels:
            string_vowels.append(character)

    return string_vowels


lambda_get_vowels = lambda string: list(
    filter(lambda character: character.lower() in "aeiou", string)
)


lambda_get_vowels_list_comprehension = lambda string: [
    character for character in string if character.lower() in "aeiou"
]

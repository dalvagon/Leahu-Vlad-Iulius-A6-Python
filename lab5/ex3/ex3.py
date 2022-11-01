from utils import get_vowels, lambda_get_vowels, lambda_get_vowels_list_comprehension


if __name__ == "__main__":
    string = "Programming in Python is fun"
    print(get_vowels(string))
    print(lambda_get_vowels(string))
    print(lambda_get_vowels_list_comprehension(string))

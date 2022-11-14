import re


def extract_words(str):
    return re.findall("[a-zA-z\\d]+", str)


if __name__ == "__main__":
    print(extract_words("Ana are 10 mere si nu are pere"))

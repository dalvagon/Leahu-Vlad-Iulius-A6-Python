import re


def censure_word(match):
    word = match.group(0)
    vowels = "aeiouAEIOU"

    if word[0] in vowels and word[-1] in vowels:
        return "".join([c if word.index(c) % 2 == 0 else "*" for c in word])

    return word


def censure(str):
    return re.sub(
        "\\w+",
        censure_word,
        str,
    )


if __name__ == "__main__":
    print(censure("aha, tu ai spart aia, ohohoho"))

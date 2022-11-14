import re


def return_substrings(regex, str, x):
    return [str for str in re.findall(regex, str) if len(str) == x]


if __name__ == "__main__":
    print(return_substrings("\\d+", "Ana are 100 de mere, 10 pere si 50 de ", 2))

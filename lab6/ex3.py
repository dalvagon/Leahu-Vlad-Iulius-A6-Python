import re


def filter_strs(strs, res):
    return [str for str in strs if any([re.search(r, str) for r in res]) > 0]


if __name__ == "__main__":
    print(
        filter_strs(
            ["Ana are 50 mere si 2 pere", "nu am bani", "<html>nu trec python</html>"],
            ["5\\d", "<[a-z]+ml>"],
        )
    )

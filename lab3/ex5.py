def validate_dict(ruleset, dictionary):
    for rule in ruleset:
        value = dictionary[rule[0]]
        if not (
            value.find(rule[1]) == 0
            and value.find(rule[2]) > 0
            and value.find(rule[2]) + len(rule[2]) < len(value)
            and value.find(rule[3]) == len(value) - len(rule[3])
        ):
            return False
    return True


if __name__ == "__main__":
    print(
        validate_dict(
            {
                ("key1", "abcd", "cde", "efg"),
                ("key2", "abcde", "bc", "bcdefgh"),
                ("key1", "a", "bcd", "g"),
            },
            {"key1": "abcdefg", "key2": "abcdefgh"},
        )
    )

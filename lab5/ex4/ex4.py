def get_dictionaries(*l, **kl):
    lst = [kv for kv in l] + [kl[key] for key in kl]

    return [
        kv
        for kv in lst
        if isinstance(kv, dict)
        and len(kv.keys()) >= 2
        and len([key for key in kv if isinstance(key, str) and len(key) >= 3]) > 0
    ]


if __name__ == "__main__":
    print(
        get_dictionaries(
            {1: 2, 3: 4, 5: 6},
            {"a": 5, "b": 7, "c": "e"},
            {2: 3},
            [1, 2, 3],
            {"abc": 4, "def": 5},
            3764,
            dictionar={"ab": 4, "ac": "abcde", "fg": "abc"},
            test={1: 1, "test": True},
        )
    )

def compare_dictionaires(item1, item2, parent="root"):
    if isinstance(item1, dict) and isinstance(item2, dict):
        keys1 = item1.keys()
        keys2 = item2.keys()
        common_keys = keys1 & keys2
        if keys1 != keys2:
            print(
                parent
                + ":"
                + str(keys1 - keys2)
                + " != "
                + parent
                + ":"
                + str(keys2 - keys1)
            )

        for key in common_keys:
            compare_dictionaires(item1[key], item2[key], parent + ":" + str(key))

    elif isinstance(item1, list) and isinstance(item2, list):
        if len(item1) != len(item2):
            print(
                "len("
                + parent
                + "."
                + str(item1)
                + ") != len("
                + parent
                + "."
                + str(item2)
                + ")"
            )
        else:
            for index in range(0, len(item1)):
                compare_dictionaires(
                    item1[index], item2[index], parent + "[" + str(index) + "]"
                )

    elif isinstance(item1, tuple) and isinstance(item2, tuple):
        if len(item1) != len(item2):
            print(
                "len("
                + parent
                + "."
                + str(item1)
                + ") != len("
                + parent
                + "."
                + str(item2)
                + ")"
            )
        else:
            for index in range(0, len(item1)):
                compare_dictionaires(
                    item1[index], item2[index], parent + "[" + str(index) + "]"
                )

    elif isinstance(item1, set) and isinstance(item2, set):
        if len(item1) != len(item2):
            print(
                "len("
                + parent
                + "."
                + str(item1)
                + ") != len("
                + parent
                + "."
                + str(item2)
                + ")"
            )
        else:
            for element1, element2 in zip(item1, item2):
                compare_dictionaires(element1, element2, parent + "." + str(item1))

    else:
        if item1 != item2:
            print(parent + "." + str(item1) + " != " + parent + ":" + str(item2))


if __name__ == "__main__":
    compare_dictionaires(
        {
            11: [{1111: "abc1111", 1112: "abc1112"}, "abc111", "abc112"],
            12: {122: {1221: "abc1221"}},
            33: {331: "fff", 332: "fffff"},
            44: [{441: (4411, 44112)}],
            55: {1, 2, 3},
            66: [1, 2, 3],
        },
        {
            11: [{1111: "abc1112", 1112: "abc1112"}, "abc11", "abc112"],
            21: "ABC21",
            22: "ABC22",
            33: {331: "fff", 332: "ffff"},
            44: [{441: (4411, 44112, 44113)}],
            55: {1, 2, 4, 5},
            66: [3, 2, 1],
        },
    )

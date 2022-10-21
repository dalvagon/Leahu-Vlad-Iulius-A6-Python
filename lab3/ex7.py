def sets_operations(*sets):
    dictionary = {}
    for set1 in sets:
        for set2 in sets:
            if set1 != set2:
                dictionary[str(set1) + " | " + str(set2)] = set1 | set2
                dictionary[str(set1) + " & " + str(set2)] = set1 & set2
                dictionary[str(set1) + " - " + str(set2)] = set1 - set2
                dictionary[str(set2) + " - " + str(set1)] = set2 - set1
                dictionary[str(set1) + " ^ " + str(set2)] = set1 ^ set2
                dictionary[str(set2) + " ^ " + str(set1)] = set2 ^ set1

    return dictionary


if __name__ == "__main__":
    dictionary = sets_operations({1, 2, 3}, {1, 3, 4, 5}, {3, 4, 5}, {6, 7, 8}, {2, 3})
    for key, value in dictionary.items():
        print(str(key) + " : " + str(value))

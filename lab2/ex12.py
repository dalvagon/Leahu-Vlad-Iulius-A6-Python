# Ex 12
def group_by_rhyme(words):
    ret_list = []
    for word in words:
        rhyming_words_list = [
            other_word for other_word in words if word[-2:] == other_word[-2:]
        ]

        if not rhyming_words_list in ret_list:
            ret_list.append(rhyming_words_list)

    return ret_list


if __name__ == "__main__":
    print(group_by_rhyme(["ana", "banana", "carte", "arme", "parte"]))

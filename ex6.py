# Ex 6
def build_appearance_list(*lists, x):
    lst = []
    ret_lst = []
    for l in lists:
        lst += l

    for element in lst:
        if lst.count(element) == x and not element in ret_lst:
            ret_lst.append(element)

    return ret_lst


if __name__ == "__main__":
    print(build_appearance_list([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))

import os
from os.path import isdir, isfile, join


def search(target, to_search):
    if isfile(target):
        file = open(target, "r")
        if to_search in file.read():
            return [target]

    elif isdir(target):
        ret_list = []

        for (root, dirs, files) in os.walk(target):
            for file_name in files:
                file = open(join(root, file_name), "r")
                if to_search in file.read():
                    ret_list.append(join(root, file_name))

        return ret_list

    raise ValueError("Target " + target + " is not a directory or a file")


if __name__ == "__main__":
    try:
        print(search("testDir", "word"))
    except Exception as e:
        print(str(e))

    try:
        print(search("asf", "word"))
    except Exception as e:
        print(str(e))

import os
from os.path import isdir, isfile, join


def handle_exception(e):
    print(str(e))


def search(target, to_search, callback):
    try:
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
    except Exception as e:
        callback(e)


if __name__ == "__main__":
    print(search("testDir", "word", handle_exception))
    print(search("asf", "word", handle_exception))

import os
from os.path import isdir, isfile, join


def read_dir_or_file(path):
    if isdir(path):
        extension_list = list(
            [
                file_name[file_name.find(".") :]
                for file_names in [files for (root, dirs, files) in os.walk(path)]
                for file_name in file_names
                if "." in file_name
            ]
        )

        return list(
            set(
                [
                    (extension, extension_list.count(extension))
                    for extension in extension_list
                ]
            )
        )

    if isfile(path):
        file = open(path, "r")
        return file.read().replace("\n", "")[-20:]

    raise Exception(path + " is not a file or a directory")


if __name__ == "__main__":
    try:
        print(read_dir_or_file("testDir"))
    except Exception as e:
        print(str(e))

    try:
        print(read_dir_or_file(join(".", "testDir", "abc.txt")))
    except Exception as e:
        print(str(e))

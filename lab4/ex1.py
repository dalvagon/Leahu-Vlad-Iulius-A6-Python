import os
from os.path import join


def list_extensions(directory):
    return sorted(
        list(
            set(
                [
                    file_name[file_name.find(".") :]
                    for file_names in [
                        files for (root, dirs, files) in os.walk(directory)
                    ]
                    for file_name in file_names
                    if "." in file_name
                ]
            )
        )
    )


if __name__ == "__main__":
    directory = "testDir"
    try:
        print(list_extensions(directory))
    except FileNotFoundError:
        print("Folder  " + directory + " not found")
    except:
        print("Error")

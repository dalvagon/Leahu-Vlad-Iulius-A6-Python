from os import listdir
import sys


def get_extensions(path):
    return list(
        set(
            [
                file_name[file_name.find(".") :]
                for file_name in listdir(path)
                if "." in file_name
            ]
        )
    )


if __name__ == "__main__":
    # path = input()

    # try:
    #     print(get_extensions(path))
    # except Exception as e:
    #     print(str(e))

    try:
        print(get_extensions(sys.argv[1]))
    except Exception as e:
        print(str(e))

from os import listdir
from os.path import abspath


def list_files(path):
    return [abspath(file_name) for file_name in listdir(path)]


if __name__ == "__main__":
    print(list_files("C:\\Users\\leahu\\Desktop\\python\lab4\\testDir"))

from os import R_OK, W_OK, access, stat
from os.path import abspath, join


def file_stats(path):
    return {
        "full_path": abspath(path),
        "file_size": stat(path).st_size,
        "file_extension": path[len(path) - 1 - path[::-1].find(".") :]
        if "." in path
        else "",
        "can_read": access(path, R_OK),
        "can_write": access(path, W_OK),
    }


if __name__ == "__main__":
    print(file_stats(join(".", "testDir", "testDir1", "testDir2", "AbcD.pdf")))

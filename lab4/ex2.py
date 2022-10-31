import os
from os.path import join


def write_to_file(directory, file):
    output_file = open(file, "w")
    for (root, dirs, files) in os.walk(directory):
        for file_name in files:
            if file_name[0].upper() == "A":
                output_file.write(join(root, file_name))
                output_file.write("\n")


if __name__ == "__main__":
    write_to_file("testDir", join("testDir", "ex2Output.txt"))

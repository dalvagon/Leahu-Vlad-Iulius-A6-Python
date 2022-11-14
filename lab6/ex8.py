import re
import os


def scroll_dir(path, r):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                content = open(os.path.join(root, file), "r").read()
                if re.search(r, content):
                    if re.match(r, file):
                        print(">> " + file)
                    else:
                        print(file)
                elif re.match(r, file):
                    print(file)
            except:
                print("error")


if __name__ == "__main__":
    scroll_dir(os.path.join(".", "test_dir"), "_\\w+_\\d+")

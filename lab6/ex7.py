import re


def is_valid(cnp):
    return (
        "Match"
        if re.match("^[56]\\d\\d(0[1-9]|1[012])(0[1-9]|[12]\\d|3[01])\\d{6}$", cnp)
        else "No Match"
    )


if __name__ == "__main__":
    print(is_valid("5020624330232"))

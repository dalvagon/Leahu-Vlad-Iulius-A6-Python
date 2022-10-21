def loop(diciotnary):
    key = diciotnary["start"]
    is_visited = {}
    is_visited = []
    path = []

    while is_visited.count(key) == 0:
        path.append(key)
        is_visited.append(key)
        key = diciotnary[key]

    return path


if __name__ == "__main__":
    print(
        loop(
            {
                "start": "a",
                "b": "a",
                "a": "6",
                "6": "z",
                "x": "2",
                "z": "2",
                "2": "2",
                "y": "start",
            }
        )
    )

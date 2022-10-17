# Ex 4
def compose(notes, moves, start_position):
    moves = [start_position] + moves

    return [
        notes[sum([moves[index2] for index2 in range(0, index1 + 1)]) % len(moves)]
        for index1 in range(0, len(moves))
    ]


if __name__ == "__main__":
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

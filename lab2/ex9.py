# Ex 9
def blind_spectators(matrix):
    return [
        (index1, index2)
        for index1 in range(0, len(matrix))
        for index2 in range(0, len(matrix[0]))
        if len(
            [
                matrix[index3][index2]
                for index3 in range(0, index1)
                if matrix[index1][index2] <= matrix[index3][index2]
            ]
        )
        > 0
    ]


if __name__ == "__main__":
    print(
        blind_spectators(
            [
                [1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5],
            ]
        )
    )

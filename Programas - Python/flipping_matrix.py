def flippingMatrix(matrix):
    max_values = list()
    row_div = len(matrix) // 2
    op_numbers = row_div**2
    r = 0
    c = 0
    for i in range(op_numbers):
        if i != 0 and i % row_div == 0:
            r += 1
            c = 0
        r1 = r
        r2 = len(matrix) - 1 - r
        c1 = c
        c2 = len(matrix) - 1 - c
        max_values.append(
            max(matrix[r1][c1], matrix[r1][c2], matrix[r2][c1], matrix[r2][c2])
        )
        c += 1
    return sum(max_values)


def flippingMatrix_2(matrix):
    n = len(matrix) // 2
    total = 0

    for r in range(n):
        for c in range(n):
            total += max(
                matrix[r][c],  # posição original
                matrix[r][~c],  # coluna espelhada: ~c == -c-1
                matrix[~r][c],  # linha  espelhada: ~r == -r-1
                matrix[~r][~c],  # linha e coluna espelhadas
            )

    return total


if __name__ == "__main__":
    print(
        flippingMatrix(
            [
                [112, 42, 83, 119],
                [56, 125, 56, 49],
                [15, 78, 101, 43],
                [62, 98, 114, 108],
            ]
        )
    )  # 414 = [[119, 114], [56, 125]]

    # [0][0], [0][3], [3][0], [3][3]
    # [0][1], [0][2], [3][1], [3][2]
    # [1][0], [1][3], [2][0], [2][3]
    # [1][1], [1][2], [2][1], [2][2]

    # [2][2] = 1
    # [4][4] = 4
    # [6][6] = 9
    # [8][8] = 16

    print(flippingMatrix([[1, 2], [3, 4]]))

    print(
        flippingMatrix(
            [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1],
            ]
        )
    )

# [0][0], [0][7], [7][0], [7][7]
# [0][1], [0][6], [7][1], [7][6]
# [0][2], [0][5], [7][2], [7][5]
# [0][3], [0][4], [7][3], [7][4]
# [1][0], [1][7], [6][0], [6][7]
# [1][1], [1][6], [6][1], [6][6]
# [1][2], [1][5], [6][2], [6][5]
# [1][3], [1][4], [6][3], [6][4]
# [2][0], [2][7], [5][0], [5][7]
# [2][1], [2][6], [5][1], [5][6]
# [2][2], [2][5], [5][2], [5][5]
# [2][3], [2][4], [5][3], [5][4]
# [3][0], [3][7], [4][0], [4][7]
# [3][1], [3][6], [4][1], [4][6]
# [3][2], [3][5], [4][2], [4][5]
# [3][3], [3][4], [4][3], [4][4]

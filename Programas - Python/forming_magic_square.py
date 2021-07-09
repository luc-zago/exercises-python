def formingMagicSquare(s):
    matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    
    cost_list = []

    for ref_mat in matrix_list:
        cost = 0
        for x in range(3):
            for y in range(3):
                if s[x][y] != ref_mat[x][y]:
                    cost += abs(s[x][y] - ref_mat[x][y])
        cost_list.append(cost)
    return min(cost_list)

if __name__ == '__main__':
    print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))
    print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    print(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
    print(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 8]]))

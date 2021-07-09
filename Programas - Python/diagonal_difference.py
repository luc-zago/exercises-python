a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def diagonal_sum(arr):
    diagonal_sum = 0
    for index, item in enumerate(arr):
        diagonal_sum += item[index]
    return diagonal_sum

def diagonalDifference(arr):
    result = diagonal_sum(arr) - diagonal_sum(arr[::-1])
    if result < 0:
        result *= -1
    return result

if __name__ == '__main__':
    print(diagonalDifference(a))

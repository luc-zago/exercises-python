def diagonalDifference(arr):
    left_sum = 0
    right_sum = 0
    for r, i in zip(arr, range(len(arr))):
        left_sum += r[i]
        right_sum += r[len(arr) - i - 1]
    return abs(left_sum - right_sum)


if __name__ == "__main__":
    print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

def twoArrays(k, A, B):
    s_a = sorted(A)
    i_b = sorted(B, reverse=True)
    for i in range(len(A)):
        if s_a[i] + i_b[i] < k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
    print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))

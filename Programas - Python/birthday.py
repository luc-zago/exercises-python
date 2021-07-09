def birthday(s, d, m):
    quantity = 0
    for index, item in enumerate(s):
        piece = s[index:(index + m)]
        if len(piece) == m and sum(piece) == d:
            quantity += 1
    return quantity

if __name__ == '__main__':
    print(birthday([1, 2, 1, 3, 2], 3, 2))
    print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
    print(birthday([4], 4, 1))

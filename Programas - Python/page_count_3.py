def pageCount(n, p):
    return min(p // 2, (n // 2) - (p // 2))


if __name__ == "__main__":
    print(pageCount(6, 6))
    print(pageCount(6, 5))
    print(pageCount(5, 4))
    print(pageCount(5, 5))
    print(pageCount(5, 3))
    print(pageCount(5, 2))
    print(pageCount(5, 1))
    print(pageCount(5, 5))
    print(pageCount(6, 4))
    print(pageCount(7, 2))
    print(pageCount(12, 5))

def kangaroo(x1, v1, x2, v2):
    while True:
        if x1 == x2:
            return "YES"
        if v1 <= v2 or x1 > x2:
            break
        x1 += v1
        x2 += v2
    return "NO"


if __name__ == "__main__":
    print(kangaroo(0, 3, 4, 2))

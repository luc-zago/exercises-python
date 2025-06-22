def pageCount(n, p):
    start = 1
    end = n
    inc = 2
    reverse = False
    count = 0
    mid = n // 2
    diff = mid - p
    if diff < 0:
        start = n
        end = 0
        inc = -2
        reverse = True
    for i in range(start, end, inc):
        if reverse:
            comp = p
            if n % 2 != 0:
                comp = p + 1
            if i <= comp:
                break
        else:
            if i >= p:
                break
        count += 1
    return count


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

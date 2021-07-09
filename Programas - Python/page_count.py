def toEven(n):
    if n % 2 == 0:
        return n
    return n - 1
def pageCount(n, p):
    count_up, count_down, start, end = 0, 0, 1, toEven(n)
    while start < p:
        start += 2
        count_up += 1
    while end > p:
        end -= 2
        count_down += 1
    if count_up < count_down:
        return count_up
    return count_down

if __name__ == '__main__':
    print(pageCount(6, 2))
    print(pageCount(5, 4))
    print(pageCount(5, 3))
    print(pageCount(5, 5))
    print(pageCount(6, 4))
    print(pageCount(7, 2))

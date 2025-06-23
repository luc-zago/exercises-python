def pickingNumbers(a):
    max_length = 0
    for n in sorted(set(a)):
        count = a.count(n)
        if n + 1 in a:
            count += a.count(n + 1)
        if count > max_length:
            max_length = count
    return max_length


if __name__ == "__main__":
    print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))
    print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5, 6, 6, 6]))
    print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 9, 9, 9]))

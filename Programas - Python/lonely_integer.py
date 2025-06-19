def lonelyinteger(a):
    a_copy = a.copy()
    for n in a:
        a_copy.remove(n)
        if n not in a_copy:
            return n
        a_copy = a.copy()


if __name__ == "__main__":
    print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))

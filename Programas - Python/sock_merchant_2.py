def sockMerchant(n, ar):
    count = 0
    t_ar = ar.copy()
    for v in ar:
        try:
            t_ar.remove(v)
        except ValueError:
            pass
        if v in t_ar:
            t_ar.remove(v)
            count += 1
    return count


if __name__ == "__main__":
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

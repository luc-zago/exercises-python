# Não aprovado
def sockMerchant(n, ar):
    count = 0
    s_ar = sorted(ar)
    for i in range(0, len(ar), 2):
        try:
            if s_ar[i] == s_ar[i + 1]:
                count += 1
        except IndexError:
            pass
    return count


if __name__ == "__main__":
    print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))

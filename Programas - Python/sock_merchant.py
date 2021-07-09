def sockMerchant(n, ar):
    remove_repeated = set(ar)
    pairs = 0
    for color in remove_repeated:
        repeat = 0
        for sock in ar:
            if color == sock:
                repeat += 1
        if repeat > 1:
            if repeat % 2 == 0:
                pairs += int(repeat/2)
            else:
                pairs += int((repeat - 1) / 2)
    return pairs

if __name__ == '__main__':
    print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    print(sockMerchant(7, [1, 2, 1, 2, 3, 2]))

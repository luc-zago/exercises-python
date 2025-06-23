def pickingNumbers(a):
    s_a = sorted(a)
    s_set = sorted(set(a))
    max_length = 0
    for i in range(len(s_set)):
        count = s_a.count(s_set[i])
        if count > max_length:
            max_length = count
        try:
            if s_set[i] + 1 == s_set[i + 1]:
                start = s_a.index(s_set[i])
                end = s_a.index(s_set[i + 1]) + s_a.count(s_set[i + 1])
                if len(s_a[start:end]) > max_length:
                    max_length = len(s_a[start:end])
        except IndexError:
            if s_set[i] == s_set[i - 1] or s_set[i] == s_set[i - i] + 1:
                start = s_a.index(s_set[i - 1])
                end = s_a.index(s_set[i]) + s_a.count(s_set[i])
                if len(s_a[start:end]) > max_length:
                    max_length = len(s_a[start:end])
            pass
    return max_length


if __name__ == "__main__":
    # print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))
    # print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5, 6, 6, 6]))
    # print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 9, 9, 9]))
    print(
        pickingNumbers(
            [
                4,
                97,
                5,
                97,
                97,
                4,
                97,
                4,
                97,
                97,
                97,
                97,
                4,
                4,
                5,
                5,
                97,
                5,
                97,
                99,
                4,
                97,
                5,
                97,
                97,
                97,
                5,
                5,
                97,
                4,
                5,
                97,
                97,
                5,
                97,
                4,
                97,
                5,
                4,
                4,
                97,
                5,
                5,
                5,
                4,
                97,
                97,
                4,
                97,
                5,
                4,
                4,
                97,
                97,
                97,
                5,
                5,
                97,
                4,
                97,
                97,
                5,
                4,
                97,
                97,
                4,
                97,
                97,
                97,
                5,
                4,
                4,
                97,
                4,
                4,
                97,
                5,
                97,
                97,
                97,
                97,
                4,
                97,
                5,
                97,
                5,
                4,
                97,
                4,
                5,
                97,
                97,
                5,
                97,
                5,
                97,
                5,
                97,
                97,
                97,
            ]
        )
    )

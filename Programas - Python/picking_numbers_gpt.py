def pickingNumbers(a):
    freq = {}

    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_len = 0

    for num in freq:
        max_len = max(max_len, freq[num])

        if num + 1 in freq:
            max_len = max(max_len, freq[num] + freq[num + 1])

    return max_len

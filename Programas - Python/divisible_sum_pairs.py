def divisibleSumPairs(n, k, ar):
    counter = 0
    for index, number in enumerate(ar):
        for second_number in ar[index + 1:len(ar)]:
            if (number + second_number) % k == 0:
                counter += 1
    return counter

if __name__ == '__main__':
    print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))

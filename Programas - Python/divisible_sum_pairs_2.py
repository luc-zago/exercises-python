def divisibleSumPairs(n, k, ar):
    output = 0
    for num1, index in zip(ar, range(1, n)):
        for num2 in ar[index:]:
            if (num1 + num2) % k == 0:
                output += 1
    return output


if __name__ == "__main__":
    print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))

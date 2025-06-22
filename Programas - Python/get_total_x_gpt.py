def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def reduce(func, arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = func(result, arr[i])
    return result


def getTotalX(a, b):
    l = reduce(lcm, a)  # MMC de 'a'
    g = reduce(gcd, b)  # MDC de 'b'

    if g % l != 0:
        return 0

    count = 0
    multiple = l
    while multiple <= g:
        if g % multiple == 0:
            count += 1
        multiple += l

    return count

def getTotalX(a, b):
    def check_number(array, number):
        for n in array:
            if number > n:
                if number % n != 0:
                    return False
            else:
                if n % number != 0:
                    return False
        return True

    count = 0
    for n in range(a[-1], b[0] + 1):
        if not check_number(a, n):
            continue
        if not check_number(b, n):
            continue
        count += 1
    return count


if __name__ == "__main__":
    print(getTotalX([2, 4], [16, 32, 96]))

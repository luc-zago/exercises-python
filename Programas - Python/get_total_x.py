def haveOdd(x):
    for i in x:
        if i % 2 != 0:
            return True
    return False

def divisionReturnZero(a, b):
    if a % b == 0:
        return 0
    return 1

def getTotalX(a, b):
    a.sort(), b.sort()
    counter = 0
    step = 1
    if not haveOdd(a) and not haveOdd(b):
        step = 2
    for i in range(a[-1], b[0] + 1, step):
        list1 = [divisionReturnZero(i, z) for z in a]
        list2 = [divisionReturnZero(z, i) for z in b]
        if sum(list1) + sum(list2) == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(getTotalX([2, 4], [16, 32, 96]))
    print(getTotalX([3, 4], [24, 48]))

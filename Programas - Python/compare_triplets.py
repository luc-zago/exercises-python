a = [17, 28, 30]
b = [99, 16, 8]

def compareTriplets(a, b):
    c = [0, 0]
    for index, item in enumerate(a):
        if item > b[index]:
            c[0] += 1
        if item < b[index]:
            c[1] += 1
    return c

if __name__ == '__main__':
    print(compareTriplets(a, b))

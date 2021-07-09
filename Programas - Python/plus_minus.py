a = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    positives = 0
    negatives = 0
    zero = 0
    for item in arr:
        if item > 0:
            positives += 1
        elif item < 0:
            negatives += 1
        else:
            zero += 1
    print("{:.6f}".format(positives/len(arr)))
    print("{:.6f}".format(negatives/len(arr)))
    print("{:.6f}".format(zero/len(arr)))

if __name__ == '__main__':
    plusMinus(a)

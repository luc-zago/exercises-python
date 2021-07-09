
def birthdayCakeCandles(arr):
    arr.sort()
    inverted = arr[::-1]
    max_count = 0
    for i in inverted:
        if i == inverted[0]:
            max_count += 1
        else:
            break
    return max_count

if __name__ == '__main__':
    print(birthdayCakeCandles([7, 69, 2, 221, 8974, 8974, 8974]))

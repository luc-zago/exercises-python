def rotateLeft(d, arr):
    for _ in range(d % len(arr)):
        ap = arr[0]
        arr.pop(0)
        arr.append(ap)
    return arr


if __name__ == "__main__":
    print(rotateLeft(10, [1, 2, 3, 4, 5]))

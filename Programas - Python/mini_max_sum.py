def miniMaxSum(arr):
    sorted_array = sorted(arr)
    print(sum(sorted_array[:-1]), sum(sorted_array[1:]))


if __name__ == "__main__":
    miniMaxSum([1, 2, 3, 4, 5])

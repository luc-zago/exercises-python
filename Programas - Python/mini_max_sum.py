
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:len(arr) - 1]), sum(arr[1:len(arr)]))

if __name__ == '__main__':
    miniMaxSum([7, 69, 2, 221, 8974])

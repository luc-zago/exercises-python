def fibo(n):
    last, next = 0, 1
    while last < n:
        print(last)
        last, next = next, last + next

if __name__ == '__main__':
    fibo(1000000000)

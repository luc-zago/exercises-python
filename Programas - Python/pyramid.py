
def staircase(n):
    m = 1
    while m < n:
        my_str = ''
        for i in range(m):
            my_str += '#'
        print(my_str)
        m += 1

if __name__ == '__main__':
    staircase(6)

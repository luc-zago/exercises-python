
def staircase(n):
    while n > 0:
        my_str = ''
        for i in range(n):
            my_str += '#'
        print(my_str)
        n -= 1

if __name__ == '__main__':
    staircase(6)

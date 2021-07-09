
def staircase(n):
    m = 1
    base = n
    while m <= base:
        hashtag = ''
        space = ''
        for i in range(n - 1):
            space += ' '
        for i in range(m):
            hashtag += '#'
        print(space + hashtag)
        m += 1
        n -= 1

if __name__ == '__main__':
    staircase(6)

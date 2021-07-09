
def stairline(n):
    if n > 1:
        return '#' + stairline(n - 1)
    if n == 1:
        return '#'

def staircase(n):
    if n > 1:
        return staircase(n - 1) + '\n' + stairline(n)
    if n == 1:
        return '#'

if __name__ == '__main__':
    print(staircase(5))

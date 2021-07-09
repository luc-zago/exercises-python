def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'
    if v1 == v2:
        return 'NO'
    x_faster, x_slower = x1, x2
    v_faster, v_slower = v1, v2
    if v2 > v1:
        x_faster, x_slower = x2, x1
        v_faster, v_slower = v2, v1
    while x_faster < x_slower:
        x_faster += v_faster
        x_slower += v_slower
        print(x_faster, x_slower)
        if x_faster == x_slower:
            return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    print(kangaroo(3, 3, 4, 3))

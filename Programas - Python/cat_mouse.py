def catAndMouse(x, y, z):
    if x == y:
        return 'Mouse C'
    if z > x and z > y:
        if x > y:
            return 'Cat A'
        return 'Cat B'
    lower, higher = x, y
    inverted = False
    if x > y:
        lower, higher = y, x
        inverted = True
    while lower < z and higher > z and lower != higher:
        lower += 1
        higher -= 1
    if lower == higher:
        return 'Mouse C'
    elif (lower == z and not inverted) or (higher == z and inverted):
        return 'Cat A'
    return 'Cat B'
    
if __name__ == '__main__':
    print(catAndMouse(1, 2, 3))
    print(catAndMouse(1, 3, 2))
    print(catAndMouse(3, 1, 2))
    print(catAndMouse(2, 1, 3))
    print(catAndMouse(2, 10, 8))
    print(catAndMouse(2, 10, 4))
    print(catAndMouse(3, 3, 3))
    print(catAndMouse(3, 4, 100))
    print(catAndMouse(4, 3, 100))
    print(catAndMouse(50, 80, 53))
    print(catAndMouse(1, 100, 50))
    print(catAndMouse(1, 99, 50))

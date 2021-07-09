def catAndMouse(x, y, z):
    difference_x, difference_y = x - z, y - z
    if difference_x < 0:
        difference_x *= -1
    if difference_y < 0:
        difference_y *= -1
    if difference_x == difference_y:
        return 'Mouse C'
    elif difference_x > difference_y:
        return 'Cat B'
    return 'Cat A'
    
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

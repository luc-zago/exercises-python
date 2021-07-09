def countApplesAndOranges(s, t, a, b, apples, oranges):
    fallen_apples, fallen_oranges = [item + a for item in apples], [item + b for item in oranges]
    count_apples = 0
    for apple in fallen_apples:
        if t >= apple >= s:
            count_apples += 1
    print(count_apples)
    count_oranges = 0
    for orange in fallen_oranges:
        if t >= orange >= s:
            count_oranges += 1
    print(count_oranges)
        
if __name__ == '__main__':
    countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

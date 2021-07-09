def breakingRecords(scores):
    lowest, highest = scores[0], scores[0]
    break_lowest, break_highest = 0, 0
    for point in scores:
        if point > highest:
            highest = point
            break_highest += 1
        if point < lowest:
            lowest = point
            break_lowest += 1
    return [break_highest, break_lowest]

if __name__ == '__main__':
    print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
    print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))

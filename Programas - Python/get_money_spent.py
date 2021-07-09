def getMoneySpent(keyboards, drives, b):
    # if min(keyboards) + min(drives) > b:
    #    return -1
    # elif max(keyboards) + max(drives) <= b:
    #    return max(keyboards) + max(drives)
    possible_sums = []
    for keyboard in keyboards:
        for drive in drives:
            possible_sums.append(keyboard + drive)
    max_sum = -1
    for total_sum in possible_sums:
        if total_sum > max_sum and total_sum <= b:
            max_sum = total_sum
    return max_sum
    
if __name__ == '__main__':
    print(getMoneySpent([3, 1], [5, 2, 8], 10))
    print(getMoneySpent([4], [5], 5))
    print(getMoneySpent([3, 1], [5, 2, 8], 9))
    print(getMoneySpent([3, 1], [5, 2, 8], 11))

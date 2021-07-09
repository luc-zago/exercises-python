def countingValleys(steps, path):
    sea_level, valley_count = 0, 0
    for step in path:
        antecedent_sea_level = sea_level
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1
        if antecedent_sea_level < 0 and sea_level == 0:
            valley_count += 1
    return valley_count
    
if __name__ == '__main__':
    print(countingValleys(8, 'UDDDUDUU'))
    print(countingValleys(8, 'DUDUDUDU'))

def countingValleys(steps, path):
    start = 0
    in_valley = False
    valley_count = 0
    for c in path:
        if c == "U":
            start += 1
        else:
            start -= 1
        if start < 0:
            in_valley = True
        if start == 0 and in_valley:
            valley_count += 1
            in_valley = False
    return valley_count


if __name__ == "__main__":
    print(countingValleys(8, "UDDDUDUU"))

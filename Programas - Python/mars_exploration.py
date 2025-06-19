def marsExploration(s):
    count = 0
    for i in range(0, len(s), 3):
        start = i
        end = i + 3
        target_s = s[start:end]
        if target_s != "SOS":
            for c, index in zip(target_s, range(3)):
                if index % 2 == 0:
                    if c != "S":
                        count += 1
                else:
                    if c != "O":
                        count += 1
    return count


def marsExploration_2(s):
    count = 0
    for i, ch in enumerate(s):
        if ch != "SOS"[i % 3]:
            count += 1
    return count


def marsExploration_3(s):
    return sum(ch != "SOS"[i % 3] for i, ch in enumerate(s))


if __name__ == "__main__":
    print(marsExploration_3("SOSOOSOSOSOSOSSOSOSOSOSOSOS"))
    print(marsExploration_3("SOSSOT"))
    print(marsExploration_3("SOSSPSSQSSOR"))

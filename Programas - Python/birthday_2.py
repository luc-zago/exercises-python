def birthday(s, d, m):
    count = 0
    for i in range(len(s) - (m - 1)):
        if sum(s[i : i + m]) == d:
            count += 1
    return count


if __name__ == "__main__":
    print(birthday([2, 2, 1, 3, 2], 8, 4))

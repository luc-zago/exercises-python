def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += "0"
        else:
            res += "1"

    return res


if __name__ == "__main__":
    print(strings_xor("10101", "00101"))

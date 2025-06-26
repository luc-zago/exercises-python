def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        seq = ""
        num = first
        while len(seq) < len(s):
            seq += str(num)
            num += 1
        if seq == s:
            print(f"YES {first}")
            return
    print("NO")


if __name__ == "__main__":
    separateNumbers("9899100")
    separateNumbers("108109110111")
    separateNumbers("99100101102")
    separateNumbers("1234")
    separateNumbers("10111213")
    separateNumbers("101102103104")
    separateNumbers("1001100210031004")
    separateNumbers("91011")
    separateNumbers("101103")
    separateNumbers("010203")
    separateNumbers("13")
    separateNumbers("0123")

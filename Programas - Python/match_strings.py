def matchingStrings(strings, queries):
    output = list()
    for q in queries:
        if q in strings:
            count = 0
            for s in strings:
                if q == s:
                    count += 1
            output.append(count)
        else:
            output.append(0)
    return output


if __name__ == "__main__":
    print(matchingStrings(["aba", "baba", "aba", "xzxb"], ["aba", "xzxb", "ab"]))

def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return

    def check_sequence(n_len):
        start = 0
        end = n_len
        no_sequence = False
        min = s[start:end]
        for _ in range(len(s)):
            try:
                s[end]
            except IndexError:
                break
            if s[start:end][0] == "0" and n_len > 1:
                no_sequence = True
                break
            if s[start:end][-1] == "9":
                n = int(s[start:end])
                if len(str(n + 1)) > len(str(n)):
                    n_len += 1
            if int(s[start:end]) + 1 == int(s[end : end + n_len]):
                start = end
                end += n_len
                continue
            no_sequence = True
            break
        return no_sequence, min

    max_number_length = len(s) // 2
    for n in range(1, max_number_length + 1):
        no_sequence, min = check_sequence(n)
        if not no_sequence:
            print(f"YES {min}")
            return
    print("NO")


if __name__ == "__main__":
    # separateNumbers("9899100")
    # separateNumbers("108109110111")
    # separateNumbers("99100101102")
    # separateNumbers("1234")
    # separateNumbers("10111213")
    # separateNumbers("101102103104")
    # separateNumbers("1001100210031004")
    separateNumbers("91011")
    # separateNumbers("101103")
    # separateNumbers("010203")
    # separateNumbers("13")
    # separateNumbers("0123")

def timeConversion(s):
    preffix = int(s[:2])
    suffix = s[-2:]
    if suffix == "AM":
        if preffix == 12:
            return "00" + s[2:-2]
        return s[:-2]
    if preffix != 12:
        preffix += 12
    return str(preffix) + s[2:-2]


if __name__ == "__main__":
    print(timeConversion("12:05:45PM"))

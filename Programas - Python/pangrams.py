import string


def pangrams(s):
    f_s = s.replace(" ", "").lower()
    for c in string.ascii_lowercase:
        if c not in f_s:
            return "not pangram"
    return "pangram"


def pangrams_2(s):
    return (
        "pangram"
        if set(string.ascii_lowercase).issubset(set(s.lower()))
        else "not pangram"
    )


if __name__ == "__main__":
    print(pangrams("We promptly judged antique ivory buckles for the next prize"))

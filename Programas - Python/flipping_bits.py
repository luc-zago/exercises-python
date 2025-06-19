def flippingBits(n):
    bin_str = format(n, "032b")
    flipped_str = ""
    for bit in bin_str:
        if bit == "0":
            flipped_str += "1"
        else:
            flipped_str += "0"
    return int(flipped_str, 2)


if __name__ == "__main__":
    print(flippingBits(1))

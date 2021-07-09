def pickingNumbers(a):
    lens_list = []
    a.sort()
    for index, item in enumerate(a):
        count = 1
        for new_item in a[index + 1:]:
            if new_item - item <= 1:
                count += 1
        lens_list.append(count)
    return max(lens_list)

if __name__ == '__main__':
    print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))
    print(pickingNumbers([4, 6, 5, 3, 3, 1]))
    print(pickingNumbers([1, 2, 2, 3, 1, 2]))

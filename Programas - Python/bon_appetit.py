def bonAppetit(bill, k, b):
    del(bill[k])
    division = int(sum(bill) / 2)
    if division == b:
        print('Bon Appetit')
    elif division > b:
        print(division - b)
    else:
        print(b - division)

if __name__ == '__main__':
    bonAppetit([3, 10, 2, 9], 1, 12)
    bonAppetit([3, 10, 2, 9], 1, 7)

def dayOfProgrammer(year):
    if year > 1918:
        if year % 400 == 0:
            return f'12.09.{year}'
        elif year % 4 == 0 and year % 100 != 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'

    elif year < 1918:
        if year % 4 == 0:
            return f'12.09.{year}'
        return f'13.09.{year}'

    else:
        return '26.09.1918'

if __name__ == '__main__':
    print(dayOfProgrammer(2017))
    print(dayOfProgrammer(2016))
    print(dayOfProgrammer(1800))
    print(dayOfProgrammer(2000))
    print(dayOfProgrammer(1900))
    print(dayOfProgrammer(1918))

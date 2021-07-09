
def timeConversion(s):
    time = list(s)
    hour = int('{}{}'.format(*time[:2]))
    day_or_night = time[-2]
    if day_or_night == 'P' and hour != 12:
        hour += 12
    elif hour == 24 or (day_or_night == 'A' and hour == 12):
        hour = '00'
    elif day_or_night == 'A' and hour < 10:
        hour = '0' + str(hour)
    time = time[1:-2]
    time[0] = hour
    return ''.join(map(str, time))

if __name__ == '__main__':
    print(timeConversion('01:05:45AM'))

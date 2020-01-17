import datetime

year, month, day = map(int, input().split('/'))
date = datetime.datetime(year, month, day)
heisei = datetime.datetime(2019, 4, 30)

if date <= heisei:
    print('Heisei')
else:
    print('TBD')

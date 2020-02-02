s = list(input())
prev = ''
count = 0

for c in s:
    if c == prev:
        count += 1
    else:
        if count > 0:
            print(prev, count, sep='', end='')
        prev = c
        count = 1

if count > 0:
    print(prev, count, sep='')

N = input()
X = sum([int(x) for x in N])

if int(N) % X == 0:
    print('Yes')
else:
    print('No')

A, B = map(int, input().split())

diff = A - B

if diff == 0:
    print('Draw')
elif A == 1 or (diff > 0 and B != 1):
    print('Alice')
else:
    print('Bob')

A, B = map(int, input().split())

total = A + B
if total % 2 != 0:
    print('IMPOSSIBLE')
else:
    print(total // 2)


X, A, B = map(int, input().split())

if B > A + X:
    print('dangerous')
elif B > A:
    print('safe')
else:
    print('delicious')

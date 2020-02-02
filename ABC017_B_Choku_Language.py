X = list(input())
i = 0

while i < len(X):
    if X[i] == 'o' or X[i] == 'k' or X[i] == 'u':
        i += 1
    elif X[i:i+2] == ['c', 'h']:
        i += 2
    else:
        print('NO')
        exit()

print('YES')

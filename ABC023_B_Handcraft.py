N = int(input())
S = input()
acc = ['b']
ans = 0

while len(acc) < N:
    ans += 1
    if ans % 3 == 1:
        acc.insert(0, 'a')
        acc.append('c')
    elif ans % 3 == 2:
        acc.insert(0, 'c')
        acc.append('a')
    else:
        acc.insert(0, 'b')
        acc.append('b')

if ''.join(acc) == S:
    print(ans)
else:
    print(-1)


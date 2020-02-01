N, A, B = map(int, input().split())
D = [input().split() for _ in range(N)]
ans = 0

for s, d in D:
    d = int(d)
    if d < A:
        d = A
    if d > B:
        d = B
    if s == 'West':
        ans -= d
    else:
        ans += d

if ans < 0:
    print('West', -ans)
elif ans > 0:
    print('East', ans)
else:
    print(0)

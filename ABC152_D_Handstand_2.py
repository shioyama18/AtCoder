from collections import defaultdict


def create_tuple(x):
    a = x % 10
    b = int(str(x)[0])
    return (a, b)


N = int(input())
mp = defaultdict(int)
ans = 0

for i in range(1, N + 1):
    p = create_tuple(i)
    mp[p] += 1

for i in range(1, N + 1):
    p = create_tuple(i)
    q = (p[1], p[0])
    ans += mp[q]

print(ans)

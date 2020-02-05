N = int(input())
P = list(map(int, input().split()))
prev = P[0]
ans = 0

for p in P:
    if p <= prev:
        ans += 1
    prev = min(p, prev)

print(ans)

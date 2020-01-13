import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        dist = math.sqrt(sum([(x - y) ** 2 for x, y in zip(X[i], X[j])]))
        if dist.is_integer():
            ans += 1

print(ans)

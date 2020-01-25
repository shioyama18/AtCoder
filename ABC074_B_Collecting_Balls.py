N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0

for i in range(N):
    x = X[i]
    ans += 2 * min(x, K - x)

print(ans)

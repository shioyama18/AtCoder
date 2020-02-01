N, S, T = map(int, input().split())
W = int(input())
A = [0] + [int(input()) for _ in range(N-1)]
ans = 0

for a in A:
    W += a
    if W >= S and W <= T:
        ans += 1

print(ans)

N, K, M = map(int, input().split())
A = map(int, input().split())

ans = max(N * M - sum(A), 0)

if ans <= K:
    print(ans)
else:
    print(-1)

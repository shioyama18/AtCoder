N, Q = map(int, input().split())
query = [map(int, input().split()) for _ in range(Q)]
ans = [0] * N

for L, R, T in query:
    ans[L-1:R] = [T] * (R - L + 1)

for i in ans:
    print(i)

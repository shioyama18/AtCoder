N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
ans = N * T

for i in range(N-1):
    diff = A[i+1] - A[i]
    if diff < T:
        ans -= T - diff

print(ans)

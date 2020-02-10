from itertools import accumulate

N, K = map(int, input().split())
P = map(int, input().split())
acc_P = list(accumulate(P))
ans = (acc_P[K-1] + K) / 2

for i in range(N-K):
    ans = max(ans, (acc_P[i+K] - acc_P[i] + K) / 2)

print(ans)

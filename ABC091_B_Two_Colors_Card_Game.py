N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
S_Set = set(S)
ans = 0

for s in S_Set:
    ans = max(ans, S.count(s) - T.count(s))

print(ans)

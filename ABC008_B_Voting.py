N = int(input())
candidates = dict()

for _ in range(N):
    S = input()
    if S in candidates:
        candidates[S] += 1
    else:
        candidates[S] = 1

ans = max(candidates, key=candidates.get)

print(ans)

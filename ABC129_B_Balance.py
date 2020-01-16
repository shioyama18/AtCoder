N = int(input())
W = list(map(int, input().split()))

half = sum(W) / 2
first_half = 0

for i in range(N):
    first_half += W[i]
    mid_index = i
    if first_half >= half:
        break

ans = min(abs(sum(W[:i])-sum(W[i:])), abs(first_half - sum(W[i+1:])))

print(ans)

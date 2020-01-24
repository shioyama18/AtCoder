N = int(input())
K = int(input())
ans = 1

for i in range(N):
    if ans < K:
        ans *= 2
    else:
        ans += (N - i) * K
        break

print(ans)

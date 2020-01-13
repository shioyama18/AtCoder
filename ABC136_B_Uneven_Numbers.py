N = int(input())
ans = 0

if N >= 10000:
    ans += min(N, 99999) - 9999

if N >= 100:
    ans += min(N, 999) - 99

if N >= 1:
    ans += min(N, 9)

print(ans)

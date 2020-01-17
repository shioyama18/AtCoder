N = int(input())
otoshidama = [input().split() for _ in range(N)]
ans = 0

for x, u in otoshidama:
    if u == 'JPY':
        ans += float(x)
    else:
        ans += float(x) * 380000

print(ans)

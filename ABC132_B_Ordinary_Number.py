n = int(input())
p = list(map(int, input().split()))
ans = 0

for i in range(1, n - 1):
    larger = max(p[i-1], p[i+1])
    smaller = min(p[i-1], p[i+1])
    if p[i] > smaller and p[i] < larger:
        ans += 1

print(ans)

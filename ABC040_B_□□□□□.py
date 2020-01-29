n = int(input())
ans = n

for i in range(1, int(n ** 0.5) + 1):
    w = i
    h = n // i
    ans = min(ans, abs(w - h) + n - w * h)

print(ans)

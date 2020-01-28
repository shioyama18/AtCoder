W, a, b = map(int, input().split())

ans = max(0, abs(a - b) - W)

print(ans)

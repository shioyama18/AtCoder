a = int(input())
b = int(input())

ans = min(abs(a - b), 10 + min(a, b) - max(a, b))

print(ans)

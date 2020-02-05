a, b = map(int, input().split())

ans = sorted([str(a) * b, str(b) * a])[0]

print(ans)

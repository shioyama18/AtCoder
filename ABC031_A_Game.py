A, D = map(int, input().split())

ans = max(A * (D + 1), (A + 1) * D)

print(ans)

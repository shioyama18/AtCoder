A, B = map(int, input().split())

ans = max(A + max(A-1, B), B + max(A, B-1))

print(ans)

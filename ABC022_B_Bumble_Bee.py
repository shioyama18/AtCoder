N = int(input())
A = [int(input()) for _ in range(N)]

ans = len(A) - len(set(A))

print(ans)

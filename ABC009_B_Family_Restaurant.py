N = int(input())
A = {int(input()) for _ in range(N)}

ans = sorted(A, reverse=True)[1]

print(ans)

import math

N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=True)
A = list(map(lambda r: math.pi * r ** 2, R))

ans = sum(A[0::2]) - sum(A[1::2])

print(ans)

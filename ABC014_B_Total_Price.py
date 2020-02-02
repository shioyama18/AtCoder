n, X = map(int, input().split())
A = map(int, input().split())
bits = reversed(list(map(int, bin(X)[2:])))

ans = sum(map(lambda x: x[0] * x[1], zip(bits, A)))

print(ans)

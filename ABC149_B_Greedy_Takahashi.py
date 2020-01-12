A, B, K = map(int, input().split())

smaller = min(A, K)
A -= smaller
K -= smaller

print(A, max(B - K, 0))

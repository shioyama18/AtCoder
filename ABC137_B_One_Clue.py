K, X = map(int, input().split())

ans = [str(x) for x in range(X - (K - 1), X + K)]

print(' '.join(ans))

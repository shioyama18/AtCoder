N, M, X = map(int, input().split())
A = list(map(int, input().split()))

to_0 = sum([1 for a in A if a < X])
to_N = sum([1 for a in A if a > X])
ans = min(to_0, to_N)

print(ans)

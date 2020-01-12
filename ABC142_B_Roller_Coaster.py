N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = len([x for x in h if x >= K])

print(ans)

N = int(input())
P = [int(input()) for _ in range(N)]
highest = max(P)

ans = sum(P) - highest // 2

print(ans)

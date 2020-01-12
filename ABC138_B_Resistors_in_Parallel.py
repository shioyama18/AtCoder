N = int(input())
A = list(map(int, input().split()))

ans = 1 / sum(([1/x for x in A]))

print(ans)

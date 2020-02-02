N = int(input())
A = list(filter(lambda a: a > 0, map(int, input().split())))

ans = -(-sum(A) // len(A))

print(ans)

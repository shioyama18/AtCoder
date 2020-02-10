import itertools

N = int(input())
P = tuple(input().split())
Q = tuple(input().split())
permutations = list(itertools.permutations(map(str, range(1, N+1))))

ans = abs(permutations.index(P) - permutations.index(Q))

print(ans)

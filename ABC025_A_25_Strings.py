import itertools

S = input()
N = int(input())
favorite = sorted(set(itertools.permutations(S + S, 2)))

if N >= len(favorite):
    N = len(favorite)

ans = ''.join(favorite[N-1])

print(ans)

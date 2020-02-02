S = list(input())
N = int(input())
ops = [map(int, input().split()) for _ in range(N)]

for l, r in ops:
    S[l-1:r] = reversed(S[l-1:r])

print(''.join(S))

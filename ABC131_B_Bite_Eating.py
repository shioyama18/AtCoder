N, L = map(int, input().split())

if L >= 0:
    print(sum([L + n for n in range(1, N)]))
elif abs(L) >= N:
    print(sum([L + n for n in range(0, N-1)]))
else:
    print(sum([L + n for n in range(N)]))

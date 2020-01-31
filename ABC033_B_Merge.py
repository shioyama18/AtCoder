N = int(input())
cities = [input().split() for _ in range(N)]
total = sum(map(lambda c: int(c[1]), cities))

for S, P in cities:
    if int(P) > total / 2:
        print(S)
        exit()

print('atcoder')

N, M = map(int, input().split())
cities = {i: 0 for i in range(N)}

for i in range(M):
    a, b = map(int, input().split())
    cities[a-1] += 1
    cities[b-1] += 1

for i in range(N):
    print(cities[i])

N = int(input())
restaurants = []

for i in range(N):
    S, P = input().split()
    restaurants.append((i + 1, S, int(P)))

restaurants.sort(key = lambda x: (x[1], -x[2]))

for (i, _, _) in restaurants:
    print(i)

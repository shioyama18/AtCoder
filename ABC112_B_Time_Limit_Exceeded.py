N, T = map(int, input().split())
costs = []

for _ in range(N):
    c, t = map(int, input().split())
    if t <= T:
        costs.append(c)

if costs:
    print(min(costs))
else:
    print('TLE')

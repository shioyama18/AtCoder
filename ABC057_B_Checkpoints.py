N, M = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(N)]
checkpoints = [tuple(map(int, input().split())) for _ in range(M)]

for a, b in students:
    min_dist = 10 ** 9
    ans = -1
    for i in range(M):
        c, d = checkpoints[i]
        distance = abs(a - c) + abs(b - d)
        if distance < min_dist:
            min_dist = distance
            ans = i + 1
    print(ans)


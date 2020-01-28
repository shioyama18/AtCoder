N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = [map(int, input().split()) for _ in range(M)]

for p, x in px:
    total = 0

    for i in range(N):
        if i + 1 == p:
            total += x
        else:
            total += T[i]

    print(total)

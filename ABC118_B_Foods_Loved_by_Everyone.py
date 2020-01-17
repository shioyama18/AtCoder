N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = set(range(M + 1))

for i in range(N):
    food = food & set(A[i][1:])

print(len(food))

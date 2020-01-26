N = int(input())
A = [int(input()) for _ in range(N)]
current = 0
visited = {0}
ans = 0

while True:
    current = A[current] - 1
    ans += 1

    if current in visited:
        print(-1)
        break

    if current == 1:
        print(ans)
        break

    visited.add(current)

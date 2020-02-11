from collections import deque
from itertools import chain

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
max_d = 400


def bfs(start):
    queue = deque()
    queue.append(start)

    distance = [[max_d] * W for _ in range(H)]
    sx, sy = start
    distance[sx][sy] = 0

    while len(queue) > 0:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx < H and ny >= 0 and ny < W and maze[nx][ny] == '.' and distance[nx][ny] == max_d:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

    return max(filter(lambda d: d != max_d, chain.from_iterable(distance)))


ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            ans = max(ans, bfs((i, j)))

print(ans)

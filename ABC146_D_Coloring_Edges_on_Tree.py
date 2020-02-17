from collections import deque

N = int(input())
edges = [[] for _ in range(N + 1)]
ends = []

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    ends.append(b)

nodes = deque([1])
count = [0] * (N + 1)

while nodes:
    node = nodes.popleft()
    nodes.extend(edges[node])

    c = 0
    for n in edges[node]:
        c += 1 + (c + 1 == count[node])
        count[n] = c

print(max(count))
for i in ends:
    print(count[i])

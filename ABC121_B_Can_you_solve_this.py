import numpy as np

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    score = np.dot(A[i], B) + C
    if score > 0:
        ans += 1
    
print(ans)

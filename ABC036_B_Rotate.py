import numpy as np

N = int(input())
s = np.array([list(input()) for _ in range(N)])

ans = np.rot90(s, k=3)

for i in range(N):
    print(''.join(ans[i]))

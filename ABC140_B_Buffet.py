N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
prev = -1

for i in range(N):
    a = A[i]
    ans += B[a-1]
    if a - 1 == prev:
        ans += C[a-2]
    prev = a

print(ans)

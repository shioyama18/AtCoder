N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
min_diff = 100000

for i in range(N):
    temp = T - H[i] * 0.006
    diff = abs(temp - A)

    if min_diff > diff:
        min_diff = diff
        ans = i + 1
    
print(ans)

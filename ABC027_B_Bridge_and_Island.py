N = int(input())
A = list(map(int, input().split()))
total = sum(A)

if total % N != 0:
    print(-1)
else:
    mean = total // N
    ans = 0
    for i in range(1, N):
        if sum(A[:i]) / len(A[:i]) != mean:
            ans += 1
    print(ans)

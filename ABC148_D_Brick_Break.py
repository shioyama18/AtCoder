N = int(input())
A = map(int, input().split())
current = 1
ans = 0

for a in A:
    if a == current:
        current += 1
    else:
        ans += 1

if current == 1:
    print(-1)
else:
    print(ans)

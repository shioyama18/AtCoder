N = int(input())
A = list(map(int, input().split()))
ans = 0

while all(map(lambda x: x % 2 == 0, A)):
    A = list(map(lambda x: x // 2, A))
    ans += 1

print(ans)

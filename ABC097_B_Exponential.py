import math

X = int(input())
ans = 1

for b in range(2, math.ceil(math.sqrt(X)) + 1):
    p = 2

    while b ** p <= X:
        p += 1

    ans = max(ans, b ** (p - 1))

print(ans)

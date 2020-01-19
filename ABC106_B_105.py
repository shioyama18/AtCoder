N = int(input())
ans = 0


def count_factors(n):
    c = 0

    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

    return c


for i in range(1, N + 1, 2):
    if count_factors(i) >= 8:
        ans += 1

print(ans)

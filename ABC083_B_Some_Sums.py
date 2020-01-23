def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


N, A, B = map(int, input().split())
ans = 0

for i in range(1, N + 1):
    n = sum_digits(i)
    if n >= A and n <= B:
        ans += i

print(ans)

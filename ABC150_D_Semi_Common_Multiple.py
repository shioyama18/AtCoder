def count(x):
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    return count


def lcm(l):
    from fractions import gcd
    x = l[0]
    for i in range(1, len(l)):
        x = (x * l[i]) // gcd(x, l[i])
    return x


N, M = map(int, input().split())
A = set(map(int, input().split()))
ans = 0

if len(set(map(count, A))) == 1:
    T = lcm(list(map(lambda x: x // 2, A)))
    ans = -(-(M // T) // 2)

print(ans)

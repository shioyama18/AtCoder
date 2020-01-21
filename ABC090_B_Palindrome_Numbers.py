def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


A, B = map(int, input().split())

ans = sum([1 for x in range(A, B + 1) if is_palindrome(x)])

print(ans)

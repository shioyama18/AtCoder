a, b, c, d = map(int, input().split())

if max(abs(b - a), abs(c - b)) <= d or abs(a - c) <= d:
    print('Yes')
else:
    print('No')

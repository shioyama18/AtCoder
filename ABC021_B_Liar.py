N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
P.extend([a, b])

if len(P) == len(set(P)):
    print('YES')
else:
    print('NO')

A, B, C, D = map(int, input().split())
takahashi = B / A
aoki = D / C

if takahashi > aoki:
    print('TAKAHASHI')
elif takahashi < aoki:
    print('AOKI')
else:
    print('DRAW')

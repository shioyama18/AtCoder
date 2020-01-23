A, B = map(int, input().split())
S = input().split('-')

if len(S) == 2 and len(S[0]) == A:
    print('Yes')
else:
    print('No')

N = int(input())
S = input()

if N % 2 == 1:
    print('No')
else:
    mid = N // 2
    if S[:mid] == S[mid:]:
        print('Yes')
    else:
        print('No')

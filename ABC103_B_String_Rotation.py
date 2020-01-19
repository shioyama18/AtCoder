import sys

S = input()
T = input()

for i in range(len(S)):
    s = S[i:] + S[:i]

    if T == s:
        print('Yes')
        sys.exit()

print('No')

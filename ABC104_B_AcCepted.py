import sys

S = input()

if S[0] == 'A' and S[2:-1].count('C') == 1:
    s = S.replace('A', 'a', 1).replace('C', 'c', 1)
    if s == S.lower():
        print('AC')
        sys.exit()

print('WA')

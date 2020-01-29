import sys

w = input()
letters = dict()

for c in w:
    if c in letters:
        letters[c] += 1
    else:
        letters[c] = 1

for _, v in letters.items():
    if v % 2 != 0:
        print('No')
        sys.exit()

print('Yes')

import string
import sys

S = input()

for s in string.ascii_lowercase:
    if s not in S:
        print(s)
        sys.exit()

print('None')

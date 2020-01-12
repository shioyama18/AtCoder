import string

N = int(input())
S = input()

for a in S:
    index = string.ascii_uppercase.index(a)
    index = (index + N) % 26
    print(string.ascii_uppercase[index], sep='', end='')

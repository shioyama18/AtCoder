s = input()
ans = list()

for c in s:
    if c == '0' or c == '1':
        ans.append(c)
    elif len(ans) > 0:
        ans.pop()

print(''.join(ans))

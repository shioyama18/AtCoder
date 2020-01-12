N = int(input())
S, T = input().split()

ans = list()
for a, b in zip(S, T):
    ans.append(a)
    ans.append(b)

print(''.join(ans))

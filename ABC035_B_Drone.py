S = input()
T = int(input())
x = S.count('R') - S.count('L')
y = S.count('U') - S.count('D')
unknown = S.count('?')

ans = abs(x) + abs(y)
if T == 1:
    ans += unknown
else:
    ans -= unknown
    if ans < 0:
        ans %= 2

print(ans)

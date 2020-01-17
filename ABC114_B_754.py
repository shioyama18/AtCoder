S = list(input())
ans = 753

for i in range(0, len(S) - 2):
    s = int(''.join(S[i:i+3]))
    diff = abs(753 - s)

    if ans > diff:
        ans = diff

print(ans)

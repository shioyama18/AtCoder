N, X = map(int, input().split())
L = map(int, input().split())
D = 0
ans = 1

for l in L:
    D = D + l

    if D > X:
        break

    ans += 1

print(ans)

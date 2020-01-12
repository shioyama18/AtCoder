S = input()
reversed_S = S[::-1]
length = len(S)
mid = length // 2
ans = 0

for i, a, b in zip(range(length), S, reversed_S):
    if i == mid:
        break
    if a != b:
        ans += 1

print(ans)

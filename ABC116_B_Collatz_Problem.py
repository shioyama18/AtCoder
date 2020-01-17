s = int(input())
a = {s}
ans = 1

while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1

    ans += 1

    if s in a:
        break
    else:
        a.add(s)

print(ans)

N = int(input())
p = list(map(int, input().split()))
sorted_p = sorted(p)
count = 0

for a, b in zip(p, sorted_p):
    if a != b:
        count += 1
    if count > 2:
        break

if count <= 2:
    print('YES')
else:
    print('NO')

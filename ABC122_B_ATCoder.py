T = input()
ACGT = ['A', 'C', 'G', 'T']
ans = 0
count = 0

for t in T:
    if t in ACGT:
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)

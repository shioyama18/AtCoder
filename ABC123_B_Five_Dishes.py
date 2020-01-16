import math

time = [int(input()) for _ in range(5)]
ans = 0
min_ones = 10

for t in time:
    ans += math.ceil(t / 10) * 10
    ones = int(str(t)[-1])
    if ones < min_ones and ones > 0:
        min_ones = ones

if min_ones != 10:
    ans = ans - (10 - min_ones)

print(ans)

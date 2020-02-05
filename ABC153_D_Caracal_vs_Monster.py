import math

H = int(input())

ans = 2 ** (math.floor(math.log2(H)) + 1) - 1

print(ans)

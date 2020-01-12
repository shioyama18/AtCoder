import math

A, B = map(int, input().split())

A -= 1
B -= 1

print(math.ceil(B / A))

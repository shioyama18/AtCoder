A, B, K = map(int, input().split())
limit = min(A, B)
divisor = list()

for i in range(1, limit + 1):
    if A % i == 0 and B % i == 0:
        divisor.append(i)

print(divisor[-K])

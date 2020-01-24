N = int(input())
L = [2, 1]

while len(L) < N + 1:
    L.append(L[len(L)-2] + L[len(L)-1])

print(L[N])


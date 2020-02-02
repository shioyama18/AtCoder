A = int(input())
B = int(input())
C = int(input())

rank = sorted([A, B, C], reverse=True)

for x in [A, B, C]:
    print(rank.index(x) + 1)

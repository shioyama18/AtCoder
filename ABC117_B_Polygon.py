N = int(input())
L = list(map(int, input().split()))
longest = max(L)
rest = sum(L) - longest

if longest < rest:
    print('Yes')
else:
    print('No')

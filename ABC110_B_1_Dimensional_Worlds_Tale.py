N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_x = max(max(x), X)
min_y = min(min(y), Y)

if max_x < min_y:
    print('No War')
else:
    print('War')

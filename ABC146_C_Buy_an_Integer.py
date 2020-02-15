A, B, X = map(int, input().split())
price = lambda x: A * x + B * len(str(x))

if X >= price(10 ** 9):
    print(10 ** 9)
    exit()

ans = 0
min_x = 0
max_x = 10 ** 9
while min_x <= max_x:
    mid = (min_x + max_x) // 2
    if X == price(mid):
        print(mid)
        exit()

    if X < price(mid):
        max_x = mid - 1
    else:
        ans = max(ans, mid)
        min_x = mid + 1

print(ans)

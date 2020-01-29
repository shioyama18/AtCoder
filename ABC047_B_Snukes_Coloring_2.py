W, H, N = map(int, input().split())
p = [map(int, input().split()) for _ in range(N)]
w_left = 0
w_right = W
h_bottom = 0
h_top = H

for x, y, a in p:
    if a == 1:
        w_left = max(w_left, x)
    elif a == 2:
        w_right = min(w_right, x)
    elif a == 3:
        h_bottom = max(h_bottom, y)
    else:
        h_top = min(h_top, y)

ans = max(0, w_right - w_left) * max(0, h_top - h_bottom)

print(ans)

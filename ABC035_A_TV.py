W, H = map(int, input().split())
ratio = W / H

if ratio == 4 / 3:
    print('4:3')
else:
    print('16:9')

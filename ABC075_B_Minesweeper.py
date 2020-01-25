H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            count = 0
            if i > 0:
                if j > 0 and S[i-1][j-1] == '#':
                    count += 1
                if S[i-1][j] == '#':
                    count += 1
                if j < W-1 and S[i-1][j+1] == '#':
                    count += 1

            if i < H-1:
                if j > 0 and S[i+1][j-1] == '#':
                    count += 1
                if S[i+1][j] == '#':
                    count += 1
                if j < W-1 and S[i+1][j+1] == '#':
                    count += 1

            if j > 0 and S[i][j-1] == '#':
                count += 1
            if j < W-1 and S[i][j+1] == '#':
                count += 1
            S[i][j] = str(count)
    print(''.join(S[i]))

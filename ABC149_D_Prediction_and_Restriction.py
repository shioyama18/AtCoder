N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
score = {'r': P, 'p': S, 's': R}
ans = 0

for i in range(K):
    flag = True

    while i < N:
        if i >= K and T[i] == T[i-K]:
            flag = not flag
        else:
            flag = True

        if flag:
            ans += score[T[i]]

        i += K

print(ans)

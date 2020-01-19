N = int(input())
words = [input() for _ in range(N)]
w_prev = words[0]
wordlist = [w_prev]
flag = True

for i in range(1, N):
    w = words[i]
    if w_prev[-1] == w[0] and w not in wordlist:
        w_prev = w
        wordlist.append(w)
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')

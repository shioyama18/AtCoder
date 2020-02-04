S = input()
T = input()

for s, t in zip(S, T):
    if s == t or ((s == '@' or t == '@') and (s in 'atcoder' or t in 'atcoder')):
        continue
    else:
        print('You will lose')
        exit()

print('You can win')

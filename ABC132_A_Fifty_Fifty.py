S = input()
sorted_S = sorted(S)

if len(set(S)) == 2 and sorted_S[0] != sorted_S[2]:
    print('Yes')
else:
    print('No')

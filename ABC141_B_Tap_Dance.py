S = input()
flag = False

for i, m in enumerate(S):
    # 'Odd' index
    if i % 2 == 0 and m == 'L':
        print('No')
        flag = True
        break
    # 'Even' index
    elif i % 2 == 1 and m == 'R':
        print('No')
        flag = True
        break
    else:
        continue

if not flag:
    print('Yes')

N = int(input())
flag = False

for i in range(1, 10):
    if N % i == 0 and N // i < 10:
        print('Yes')
        flag = True
        break

if not flag:
    print('No')

N = int(input())
A = map(int, input().split())

if all(map(lambda x: x % 2 == 1 or x % 3 == 0 or x % 5 == 0, A)):
    print('APPROVED')
else:
    print('DENIED')

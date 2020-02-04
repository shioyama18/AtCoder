A = input()
ans = 'a' * (len(A) - 1)

if ans:
    print(ans)
elif A != 'a':
    print('a')
else:
    print(-1)

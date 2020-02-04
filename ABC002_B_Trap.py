W = input()

ans = ''.join(filter(lambda c: c not in 'aeiou', W))

print(ans)

S = [input() for _ in range(12)]

ans = len(list(filter(lambda s: 'r' in s, S)))

print(ans)

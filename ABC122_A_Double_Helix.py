b = input()
stars = ['A', 'C', 'T', 'G']

ans = stars[(stars.index(b) + 2) % 4]

print(ans)

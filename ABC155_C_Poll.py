from collections import Counter

N = int(input())
S = Counter(input() for _ in range(N))
max_count = max(S.values())

ans = sorted(s for s, c in S.items() if c == max_count)

print('\n'.join(ans))

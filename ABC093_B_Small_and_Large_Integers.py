from itertools import chain
import sys

A, B, K = map(int, input().split())
diff = B - A

if diff == 0:
    print(A)
    sys.exit()

if K > diff:
    K = diff

ans = [x for x in chain(range(A, A + K), range(B - K + 1, B + 1))]
ans = sorted(list(set(ans)))

print('\n'.join(map(str, ans)))

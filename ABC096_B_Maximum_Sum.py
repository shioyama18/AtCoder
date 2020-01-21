A, B, C = map(int, input().split())
K = int(input())
largest = max(A, B, C)

ans = A + B + C + largest * (2 ** K - 1)

print(ans)

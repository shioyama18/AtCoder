n, m = map(int, input().split())

n_angle = (n % 12 + m / 60) * 30
m_angle = m * 6
diff = abs(n_angle - m_angle)
ans = min(diff, 360 - diff)

print(ans)

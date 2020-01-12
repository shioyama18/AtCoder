S = input()
weather = ['Sunny', 'Cloudy', 'Rainy']

index = weather.index(S)
ans = weather[(index + 1) % 3]

print(ans)

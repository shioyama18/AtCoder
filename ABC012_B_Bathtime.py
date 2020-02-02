N = int(input())

hours = N // 3600
N -= hours * 3600
minutes = N // 60
N -= minutes * 60

print(str(hours).zfill(2), str(minutes).zfill(2), str(N).zfill(2), sep=':')

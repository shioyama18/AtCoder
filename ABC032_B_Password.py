s = input()
k = int(input())

if len(s) < k:
    print(0)
else:
    passwords = set()
    for i in range(0, len(s) - k + 1):
        passwords.add(s[i:i+k])
    print(len(passwords))

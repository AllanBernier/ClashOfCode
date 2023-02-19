msg = input().split()
n = int(input())
M = dict()
for i in range(n):
    ch, morse = input().split()
    M[morse] = ch
tsl = ''
for ch in msg:
    tsl += ' ' if ch=='/' else M[ch] if ch in M else '[]'
print(tsl)
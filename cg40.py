s = input()
r = ''
for i in range(len(s)):
    if s[i].isupper():
        r+=s[i]

print(r)
s = input()
r = ''
for i in range(len(s)):
    if s[i].isupper():
        r += '-'
    elif s[i].islower():
        r += '_'
    else:
        r+= '*'
print(r)
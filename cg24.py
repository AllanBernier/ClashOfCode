t = input()
low = ""
up = ""
for i in t:
    if i.upper() != i:
        low += i
    else:
        up += i
print(up)
print(low)

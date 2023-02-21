a = ''
n = int(input())
for i in range(n):
    b = int(input() )+ 96
    if b!= 96:
        a+= chr(b)
    else:
        a+=' '
print(a)

input()
input()
n=input().split()
l=0
for i in range(len(n)):
    if n[i]=='-1':
        n[i]=l
    else :
        l=n[i]
print(*n)
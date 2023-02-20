n=int(input())
r=0
for i in range(int(n/2)):
    if n%(i+1)==0:
        r+=i+1
print('perfect'if n==r else'not perfect')
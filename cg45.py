n = int(input())
k = 1
for i in range (1,n+1) :
    r = ''
    for j in range(i):
        r += f'{k} '
        k +=1
    print(r[:len(r)-1])
n = int(input())
a = []
for i in input().split():
    num = int(i)
    a.append(num)
a.sort()
print(a[1])
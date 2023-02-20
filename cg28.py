n = int(input())
a = 1
b = 0
for i in range (1,n+1):
    a *= i
    b += i
print(a+b)
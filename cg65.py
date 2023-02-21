n = int(input())
a = "{0:b}".format(n).count('1')
b = True
i = n+1
while b:
    if "{0:b}".format(i).count('1') == a:
        print(i)
        b = False
    i+=1
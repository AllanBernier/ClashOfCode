s = input()
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','q','t','u','v','w','y','x','y','z' ]

li = 'a'
m = 0
for item in l:
    t = s.count(item) + s.count(item.upper())
    if t > m:
        m=t
        li = item
print(f"{li} {str(m)}")
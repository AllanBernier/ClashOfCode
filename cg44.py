s = input()
p = input()
r=s[s.find(p[0]):s.find(p[1])+1]
print(r if r!=''else f'{p[1]+p[0]}')
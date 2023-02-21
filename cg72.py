sentence = input().split(' ') ## OUI J'AURAIS DU AJOUTER UN UPPER ICI AU MOINS

s = ''
for i in sentence:
    n = 0
    n+= i.count('a')
    n+= i.count('e')
    n+= i.count('i')
    n+= i.count('o')
    n+= i.count('u')
    n+= i.count('A')
    n+= i.count('E')
    n+= i.count('I')
    n+= i.count('O')
    n+= i.count('U')
    s += f'{str(n)} '

print(s[:-1])
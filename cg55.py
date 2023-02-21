dna = input()
r = ''
for i in dna:
    if i == 'A':
        r+= 'T'
    elif i == 'T':
        r+= 'A'
    elif i == 'C':
        r+= 'G'
    elif i == 'G':
        r+= 'C'
print(r)
s = input()
r = ''
if (len(s)%2==1):
    print('ERROR')
else:
    for i in range(int(len(s)/2+1)):
        if s[(i-1)*2:2*i]=='01':
            r += '0'
        elif s[(i-1)*2:2*i]=='10':
            r += '1'
    print(r if r!=''else'EMPTY')
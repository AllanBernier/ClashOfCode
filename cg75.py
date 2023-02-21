string = input()
t = {'a','e','i','o','u','A','E','I','O','U'}

for i in t:
    string =string.replace(i, f'{i}p{i}')
print(string)


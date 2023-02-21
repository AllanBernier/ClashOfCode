s = input()
n = sum(1 for i in s if i.isalpha() and i.islower())
print(n)
import sys
import math

# Count all even ascii letters in char 
# "HelloWorld" = input()




c = 0
for i in ''.join(char for char in "HelloWorld" if char.isalnum()):
    if not (ord(i) % 2):
        c += 1


print(c)
import sys
import math

# Count odd word in sentence t

t = input().split()

n = 0
for j in t:
    c = 0
    for i in ''.join(char for char in j if char.isalnum()):
        c += ord(i)
    n += c%2

print(n)
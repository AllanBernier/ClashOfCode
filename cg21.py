import sys
import math

n = int(input())

s = str(n)
for i in range(9):
    s = s + " " + str(n * (i+2)) 
print(s)
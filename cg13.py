import sys
import math

n = int(input())


# Found !N

r = 1
for i in range (n -1 ):
    r = r * (i+2)
print(r)
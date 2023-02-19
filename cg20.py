import sys
import math

c = int(input())
n = int(input())
r= 0
for i in range(n):
    row = input().split()
    for i in row:
        if (int(i) != 1):
            r+= int(i)
print(r)



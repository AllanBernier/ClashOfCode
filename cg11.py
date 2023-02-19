import sys
import math

a, b = [int(i) for i in input().split()]
n = int(input())
for i in range(n):
    x = int(input())
    print( str(a * x + b))

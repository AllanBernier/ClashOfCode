import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, b = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]

print(max(l-x, x-l,x) * max(b-y, y-b,y))


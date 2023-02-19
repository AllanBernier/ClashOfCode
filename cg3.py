import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x = 3 #int(input())
y = 3 #int(input())
k = 3 #int(input())

l = []
for i in range(y):
    l.append(input())
    l[i] = l[i].replace("0", "  " * k)
    l[i] = l[i].replace("1", " *" * k)
    for j in range(k):
        print(l[i])


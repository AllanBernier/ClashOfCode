import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
nl = [] 
l = []
for i in range(n):
    l.append( int(input()))

for i in l : 
    if i not in nl: 
        nl.append(i) 

for i in nl:
    print (i)
import sys
import math

# Somme des module d'une liste par le diviseur m

m = int(input())
n = int(input())
s = 0
for i in input().split():
    s += int(i) % m

print(s)
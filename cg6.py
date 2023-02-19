import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 12 #int(input())

print("if n == 1:")
print("    print(\"n is 1\")")

for i in range(n - 1):
    print("elif n == "+ str(i + 2) +":")
    print("    print(\"n is "+ str(i + 2) +"\")")

print("else:")
print("    print(\"number not found :(\")")



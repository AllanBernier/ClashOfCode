import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

formula = input().split(" ")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
a = ord(formula[0])
b = ord(formula[2])
s = formula[1]

r = 0
if (s == "+"):
    r = a + b
elif (s == "-"):
    r = a - b
elif (s == "*"):
    r = a * b
elif (s == "/"):
    r = round(a/b) + 1


print(r)

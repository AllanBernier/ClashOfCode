import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dna = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



dna = dna.replace("A", "AA")
dna = dna.replace("T", "TTT")
dna = dna.replace("G", "")

print(dna)
w = 60
h = 60
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


s = ['*','.','-','_','/']


sc = 0
l = ""
print("#" * w)
for i in range (h - 2):
    print('#' + s[sc] * (w-2) + '#')
    sc += 1
    if sc >= len(s):
        sc = 0

print("#" * w)
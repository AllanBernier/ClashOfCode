f = int(input())
n = int(input())

s = f * 3

try:
    for i in input().split():
        s += int(i) * 2 + 2
    print(s)
except:
    print(s)


h = int(input())
w = int(input())
line = input()
l = len(line)
for i in range(h):
    print(line[i%(l)] * w)